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
        "Function_7_39DE",         # 07, 7
        "Function_8_4A51",         # 08, 8
        "Function_9_4B59",         # 09, 9
        "Function_10_61E6",        # 0A, 10
        "Function_11_62A4",        # 0B, 11
        "Function_12_6507",        # 0C, 12
        "Function_13_660F",        # 0D, 13
        "Function_14_7389",        # 0E, 14
        "Function_15_7491",        # 0F, 15
        "Function_16_856D",        # 10, 16
        "Function_17_9481",        # 11, 17
        "Function_18_94DB",        # 12, 18
        "Function_19_950C",        # 13, 19
        "Function_20_952D",        # 14, 20
        "Function_21_95A6",        # 15, 21
        "Function_22_979C",        # 16, 22
        "Function_23_A169",        # 17, 23
        "Function_24_A506",        # 18, 24
        "Function_25_A672",        # 19, 25
        "Function_26_A6E9",        # 1A, 26
        "Function_27_A825",        # 1B, 27
        "Function_28_A881",        # 1C, 28
        "Function_29_A8A2",        # 1D, 29
        "Function_30_AEC0",        # 1E, 30
        "Function_31_AF93",        # 1F, 31
        "Function_32_B02B",        # 20, 32
        "Function_33_B204",        # 21, 33
        "Function_34_B362",        # 22, 34
        "Function_35_B9E1",        # 23, 35
        "Function_36_BAAD",        # 24, 36
        "Function_37_BB64",        # 25, 37
        "Function_38_C853",        # 26, 38
        "Function_39_CBCD",        # 27, 39
        "Function_40_CD5B",        # 28, 40
        "Function_41_CFE7",        # 29, 41
        "Function_42_D0EE",        # 2A, 42
        "Function_43_D1FF",        # 2B, 43
        "Function_44_D305",        # 2C, 44
        "Function_45_D321",        # 2D, 45
        "Function_46_D4D0",        # 2E, 46
        "Function_47_D5E3",        # 2F, 47
        "Function_48_D6BE",        # 30, 48
        "Function_49_DF6F",        # 31, 49
        "Function_50_F06B",        # 32, 50
        "Function_51_FE05",        # 33, 51
        "Function_52_FE36",        # 34, 52
        "Function_53_10EAF",       # 35, 53
        "Function_54_115B9",       # 36, 54
        "Function_55_11E38",       # 37, 55
        "Function_56_12041",       # 38, 56
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
            "If you're that pleased\x01",
            "with it, then it was\x01",
            "worth making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you'd like to enjoy\x01",
            "my cooking again, please\x01",
            "come anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39DA")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2342")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(
        0xFE,
        (
            "...Goodness, gracious me. Just when I\x01",
            "thought the weirdness outside ended, it's\x01",
            "just one weird thing after the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, it looks like you\x01",
            "guys are going\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in this situation, I\x01",
            "want our police officers\x01",
            "to do their best.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A91")

    ChrTalk(
        0xFE,
        (
            "Hmm... It can't be helped. It\x01",
            "looks like you're doing your\x01",
            "best on your chef training.\x02",
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
            "After all, you somehow managed\x01",
            "to fill in that cooking\x01",
            "notebook I forced onto you.\x07\x00\x02",
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
            ""Medicinal Mapo Tofu"\x07\x00\x01",
            "recipe obtained!\x02",
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
            "#00003F(This is... It looks like\x01",
            "the last page of the\x01",
            "notebook is filled in.)\x02\x03",
            "#00000FUmm, are you ok? It's\x01",
            "such a precious recipe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. Thanks are not\x01",
            "required. I wanted to teach\x01",
            "you it, and so I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, the\x01",
            "way of the chef is very\x01",
            "strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continue to focus on\x01",
            "your training from now\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_1A91")


    ChrTalk(
        0xFE,
        (
            "Hmm... It can't be helped. It\x01",
            "looks like you're doing your\x01",
            "best on your chef training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have put my soul into\x01",
            "this dish. Please take\x01",
            "it.\x02",
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
            " received.\x02",
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
        (
            "Hmph, I don't need your\x01",
            "thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, the\x01",
            "way of the chef is very\x01",
            "strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continue to focus on\x01",
            "your training from now\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C26")


    ChrTalk(
        0x101,
        "#00011F...Huh? R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come again if you get the\x01",
            "chance. I'll give you\x01",
            "some real chef training.\x02",
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
            "feeling for about this\x01",
            "for a while, but.\x02\x03",
            "Is it possible you\x01",
            "mistook us for people who\x01",
            "came for chef training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm? Are you talking about\x01",
            "the misunderstanding of\x01",
            "many months ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no, this matter is\x01",
            "different. Here, let me have a\x01",
            "look at your cooking notebook.\x02",
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
            "As a participating store, it's\x01",
            "my duty to train anyone who\x01",
            "has one. That's all it is!\x02",
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
            "#00200FSo that cooking notebook\x01",
            "is the real deal, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FOh. I never realized.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha. Then that means\x01",
            "all of us are fine chef\x01",
            "material, right?\x02\x03",
            "It might not be too bad\x01",
            "to go for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I don't know if I\x01",
            "should say it's\x01",
            "reckless, but...\x02\x03",
            "#00000FUmm, but thank you very\x01",
            "much.\x02\x03",
            "I don't know how to say\x01",
            "this, but receiving\x01",
            "something this nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. I don't need your thanks. For nice\x01",
            "young men and women like yourselves, it\x01",
            "was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, my cooking will\x01",
            "give you energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want you to eat up,\x01",
            "and get back our daily\x01",
            "lives right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, I believe in\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DE, 4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CB")

    label("loc_21CB")

    Jump("loc_233D")

    label("loc_21D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AF")

    ChrTalk(
        0xFE,
        (
            "Seriously, nothing but weird stuff ever\x01",
            "happens. Hmph, well I don't know what'd happen\x01",
            "if I panicked, so I'll keep running the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That shining blue tree\x01",
            "is creepy. I hope peace\x01",
            "returns soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_233D")

    label("loc_22AF")


    ChrTalk(
        0xFE,
        (
            "The Old Dragon is open\x01",
            "for business. If you're\x01",
            "ordering, have a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like you're going\x01",
            "somewhere. Have a meal\x01",
            "before you go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233D")

    Jump("loc_39DA")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2411")

    ChrTalk(
        0xFE,
        (
            "I don't know how long this martial\x01",
            "law will go on and it's getting on my\x01",
            "nerves. What is with this situation!?\x02",
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
    Jump("loc_39DA")

    label("loc_2411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24BE")

    ChrTalk(
        0xFE,
        (
            "Seems like the citizens\x01",
            "are excited for\x01",
            "Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really care, but I\x01",
            "wish they'd stop making such\x01",
            "a fuss about it in my store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39DA")

    label("loc_24BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258F")

    ChrTalk(
        0xFE,
        (
            "Rixia has disappeared,\x01",
            "and it's had quite the\x01",
            "impact on Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And she had just started\x01",
            "calling her her friend...\x01",
            "That's understandable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she cheers up\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2871")

    label("loc_258F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EA")

    ChrTalk(
        0xFE,
        (
            "Shanshan looks happy\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Has she cheered up or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2871")

    label("loc_25EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E3")

    ChrTalk(
        0xFE,
        (
            "Shanshan... To think she's\x01",
            "participate in a pageant\x01",
            "without telling me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought I refused the invitation\x01",
            "of the trade association\x01",
            "president's granddaughter!\x02",
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
        (
            "#00306F(W-We can't say a\x01",
            "word...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Hehe. It'll be fun to\x01",
            "see his reaction when he\x01",
            "finds out, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2871")

    label("loc_27E3")


    ChrTalk(
        0xFE,
        (
            "Well, it's great that\x01",
            "Shanshan's smile is\x01",
            "back, though.\x02",
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

    label("loc_2871")

    Jump("loc_39DA")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_291C")

    ChrTalk(
        0xFE,
        (
            "Hmm? What's wrong? You\x01",
            "look like you're at\x01",
            "wits' end, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't fight if you're\x01",
            "hungry. That's true the world\x01",
            "over. You should eat up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39DA")

    label("loc_291C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29A1")

    ChrTalk(
        0xFE,
        (
            "I always like it when\x01",
            "there's fewer customers\x01",
            "on rainy days.\x02",
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
    Jump("loc_39DA")

    label("loc_29A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B11")

    ChrTalk(
        0xFE,
        (
            "Good grief. I tried having the part\x01",
            "time worker do some simple cooking,\x01",
            "but... He was completely useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, I'll have\x01",
            "to have him do chores\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B0C")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0C")

    Jump("loc_39DA")

    label("loc_2B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2CBC")
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C31")

    ChrTalk(
        0xFE,
        (
            "The secret to making\x01",
            "fried rice is to cook it\x01",
            "using high heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do that, it'll have\x01",
            "a nice texture without\x01",
            "sticking to the pan.\x02",
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
            "Hey! Keep your eyes on\x01",
            "it!\x02",
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
    Jump("loc_2CB3")

    label("loc_2C31")


    ChrTalk(
        0xFE,
        (
            "Ah, enough already... It\x01",
            "burned as soon as I said\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got to eat your\x01",
            "mistakes yourself. You\x01",
            "hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wah...!\x02",
    )

    CloseMessageWindow()

    label("loc_2CB3")

    OP_4C(0xC, 0xFF)
    Jump("loc_39DA")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC9")

    ChrTalk(
        0xFE,
        (
            "If Crossbell wants\x01",
            "independence, I think it\x01",
            "should be, but...\x02",
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
            "even one rege of danger. That's\x01",
            "why I oppose independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E5B")

    label("loc_2DC9")


    ChrTalk(
        0xFE,
        (
            "If security can't be\x01",
            "guaranteed, then I\x01",
            "oppose independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Shanshan is exposed to\x01",
            "even 1 rige of danger,\x01",
            "it's out of the question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5B")

    Jump("loc_39DA")

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

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
            "And I get the feeling he\x01",
            "can't stop leering at\x01",
            "Shanshan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. I think I'll give\x01",
            "them a harsh scolding\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2FC2")

    label("loc_2F2A")


    ChrTalk(
        0xFE,
        (
            "Though there are a lot\x01",
            "of people who leer at\x01",
            "Shanshan to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if any of them were\x01",
            "to lay a hand on her...\x01",
            "Hmph, no need to say it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC2")

    Jump("loc_39DA")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308D")

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
    Jump("loc_30E2")

    label("loc_308D")


    ChrTalk(
        0xFE,
        (
            "I like my store quiet,\x01",
            "see.\x02",
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

    label("loc_30E2")

    Jump("loc_39DA")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3434")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Oh, you're that little\x01",
            "customer who was at the\x01",
            "table earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How did you like my\x01",
            "food?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "C-Calling me small is\x01",
            "too much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "But, the food was good\x01",
            "as can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's just, the quality is too\x01",
            "high for the price. As\x01",
            "shopkeeper, you should raise―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, young master. So\x01",
            "young, yet so well-\x01",
            "behaved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You should remember this, though. This\x01",
            "Old Dragon is for the common people. I\x01",
            "don't want to turn them away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's why I've no\x01",
            "intention of changing\x01",
            "the prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I-I see... I\x01",
            "underestimated you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Haha. He's reserved all\x01",
            "of a sudden.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1DC, 5)
    Jump("loc_342F")

    label("loc_339A")


    ChrTalk(
        0x8,
        (
            "But, young master. Even\x01",
            "though you're still young,\x01",
            "you know these differences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd really like you to\x01",
            "follow the example of\x01",
            "Puck and Ruth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342F")

    Jump("loc_35B5")

    label("loc_3434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352F")

    ChrTalk(
        0xFE,
        (
            "For tomorrow's trade conference,\x01",
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
    Jump("loc_35B5")

    label("loc_352F")


    ChrTalk(
        0xFE,
        (
            "I think some reporters might\x01",
            "take photos of Shanshan\x01",
            "without permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If any reporters do\x01",
            "that, I won't go easy on\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B5")

    Jump("loc_39DA")

    label("loc_35BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365F")

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
            "Didn't they drink and\x01",
            "skip out on paying?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36E6")

    label("loc_365F")


    ChrTalk(
        0xFE,
        (
            "Not that I mind if guys\x01",
            "who could lay a hand on\x01",
            "Shanshan aren't around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like them to pay\x01",
            "their tab, though.\x01",
            "Seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E6")

    Jump("loc_39DA")

    label("loc_36EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_END)), "loc_386F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DA")

    ChrTalk(
        0xFE,
        (
            "And just when I thought\x01",
            "I'd gotten some new\x01",
            "disciples...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if it's a mistake,\x01",
            "it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But please, use that cooking\x01",
            "notebook as you like. You\x01",
            "should focus on your training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_386A")

    label("loc_37DA")


    ChrTalk(
        0xFE,
        (
            "But please, use that cooking\x01",
            "notebook as you like. You\x01",
            "should focus on your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trick to growing is\x01",
            "cooking. ...Understand?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386A")

    Jump("loc_39DA")

    label("loc_386F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393C")

    ChrTalk(
        0xFE,
        (
            "Customers mustn't\x01",
            "recklessly enter the\x01",
            "kitchen.\x02",
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
            "But I don't mind at all.\x01",
            "After all, you're my\x01",
            "apprentices.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39DA")

    label("loc_393C")


    ChrTalk(
        0xFE,
        (
            "If you want to learn the art\x01",
            "of Eastern cuisine, I stand\x01",
            "ready to instruct you.\x02",
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

    label("loc_39DA")

    TalkEnd(0xFE)
    Return()

    # Function_6_1556 end

    def Function_7_39DE(): pass

    label("Function_7_39DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B21")

    ChrTalk(
        0xFE,
        (
            "Hehe. It takes a real\x01",
            "master to ignore that\x01",
            "strange scenery and cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mother in the Republic is worried, but\x01",
            "the civil war that's occurring in the\x01",
            "Empire is the thing to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time for scattered\x01",
            "thoughts. I've got to study\x01",
            "properly under the master.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BFB")

    label("loc_3B21")


    ChrTalk(
        0xFE,
        (
            "My mother in the Republic is worried, but\x01",
            "the civil war that's occurring in the\x01",
            "Empire is the thing to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time for scattered\x01",
            "thoughts. I've got to study\x01",
            "properly under the master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFB")

    Jump("loc_4A4D")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C81")

    ChrTalk(
        0xFE,
        (
            "This has turned into an\x01",
            "unthinkable situation\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is probably no time\x01",
            "to be running a store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4D")

    label("loc_3C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D52")

    ChrTalk(
        0xFE,
        (
            "If I miss my chance today, it'll\x01",
            "probably be difficult to return\x01",
            "to the Republic for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder if my mother in\x01",
            "the Republic is worried.\x01",
            "Maybe I should return...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DAC")

    label("loc_3D52")


    ChrTalk(
        0xFE,
        (
            "But, just where did\x01",
            "Rixia go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shanshan is worried.\x01",
            "It'd be better if we\x01",
            "knew.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAC")

    Jump("loc_4A4D")

    label("loc_3DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DBF")
    Jump("loc_4A4D")

    label("loc_3DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E2A")

    ChrTalk(
        0xFE,
        (
            "Things sure are\x01",
            "dangerous lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not like we\x01",
            "can do anything about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4D")

    label("loc_3E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F24")

    ChrTalk(
        0xFE,
        (
            "Without a part-time\x01",
            "worker, we'll have more\x01",
            "chores than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. Up until know,\x01",
            "we've been calling Puck\x01",
            "and Ruth "no-hopers".\x02",
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
    Jump("loc_3FB4")

    label("loc_3F24")


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
            "They've become a little\x01",
            "more promising.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB4")

    Jump("loc_4A4D")

    label("loc_3FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4069")

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
    Jump("loc_4A4D")

    label("loc_4069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4168")

    ChrTalk(
        0xFE,
        (
            "That Puck and Ruth. They said\x01",
            "they want us to let them do\x01",
            "nicer jobs. Such impertinence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I said stuff like\x01",
            "that a long time ago,\x01",
            "the master got angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've got to\x01",
            "understand that chores\x01",
            "are fine work too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41FC")

    label("loc_4168")


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
            "the master's sayings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FC")

    Jump("loc_4A4D")

    label("loc_4201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D4")

    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "I've been back to the\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, working here is\x01",
            "fun, so I don't\x01",
            "particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I need to\x01",
            "contact my mom every\x01",
            "once in a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_433B")

    label("loc_42D4")


    ChrTalk(
        0xFE,
        (
            "I guess I need to contact my mom\x01",
            "every once in a while. It's been\x01",
            "a while since I've been back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433B")

    Jump("loc_4A4D")

    label("loc_4340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4503")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444C")

    ChrTalk(
        0xFE,
        (
            "Even now, I'm on the master's\x01",
            "list of "people who have tried\x01",
            "to lay a hand on Shanshan".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in charge of looking after\x01",
            "her. It's not like I'd have a\x01",
            "reason to lay a hand on her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Shanshan is like a\x01",
            "little sister to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44FE")

    label("loc_444C")


    ChrTalk(
        0xFE,
        (
            "I've been with the master for\x01",
            "a long time, and Shanshan is\x01",
            "like a little sister to me.\x02",
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

    label("loc_44FE")

    Jump("loc_4A4D")

    label("loc_4503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4603")

    ChrTalk(
        0xFE,
        (
            "According to a rumor, the master opened a business in\x01",
            "the Eastern Quarter. It's a particularly bad place\x01",
            "for a business because of a lack of public order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I met the master\x01",
            "in Crossbell, he hardly\x01",
            "ever tells me old stories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4D")

    label("loc_4603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_478B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470D")

    ChrTalk(
        0xFE,
        (
            "It seems like master is\x01",
            "fond of the Eastern\x01",
            "Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he drove out the\x01",
            "ruffians himself when he\x01",
            "lived in Eastern Quarter.\x02",
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
    Jump("loc_4786")

    label("loc_470D")


    ChrTalk(
        0xFE,
        (
            "It seems like master is\x01",
            "fond of the Eastern\x01",
            "Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, seriously. If you\x01",
            "make him angry, you'll\x01",
            "regret it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4786")

    Jump("loc_4A4D")

    label("loc_478B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488D")

    ChrTalk(
        0xFE,
        (
            "You see, the other day,\x01",
            "I tried motioning to\x01",
            "Rixia, but...\x02",
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
            "to enjoy Arc-en-Ciel more\x01",
            "than she wants love, huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4904")

    label("loc_488D")


    ChrTalk(
        0xFE,
        (
            "For Rixia, wanting to\x01",
            "enjoy Arc-en-Ciel can't\x01",
            "be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it'd be\x01",
            "embarrassing if I gave\x01",
            "her a spanking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4904")

    Jump("loc_4A4D")

    label("loc_4909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C0")

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
    Jump("loc_4A4D")

    label("loc_49C0")


    ChrTalk(
        0xFE,
        (
            "We've left all chores to\x01",
            "Puck and Ruth, our\x01",
            "newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, they've progressed\x01",
            "since when they couldn't\x01",
            "even be behind the counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4D")

    TalkEnd(0xFE)
    Return()

    # Function_7_39DE end

    def Function_8_4A51(): pass

    label("Function_8_4A51")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4B52")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Rest\x01",        # 2
            "Cancel\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AC8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4AE7")
    OP_AF(0x34)
    Jump("loc_4AE9")

    label("loc_4AE7")

    OP_AF(0x33)

    label("loc_4AE9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B48")

    label("loc_4AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B18")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B48")

    label("loc_4B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B2C")
    Jump("loc_4B48")

    label("loc_4B2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B48")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_4B48")

    Jump("loc_4A67")

    label("loc_4B4D")

    Jump("loc_4B55")

    label("loc_4B52")

    Call(0, 9)

    label("loc_4B55")

    TalkEnd(0xA)
    Return()

    # Function_8_4A51 end

    def Function_9_4B59(): pass

    label("Function_9_4B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EF5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B84")
    Call(0, 11)
    Jump("loc_4D42")

    label("loc_4B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB0")

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
            "I'll be here waiting for\x01",
            "you... Absolutely return\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah... I definitely\x01",
            "will.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D42")

    label("loc_4CB0")


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
            "I'll be here waiting for\x01",
            "you... Absolutely return\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D42")

    Jump("loc_4EF0")

    label("loc_4D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D59")
    Call(0, 10)
    Jump("loc_4EF0")

    label("loc_4D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5E")

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
            "I'll be here waiting for\x01",
            "you... Absolutely return\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EF0")

    label("loc_4E5E")


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
            "I'll be here waiting for\x01",
            "you... Absolutely return\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF0")

    Jump("loc_61E5")

    label("loc_4EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_507B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F20")
    Call(0, 11)
    Jump("loc_4FD8")

    label("loc_4F20")


    ChrTalk(
        0xA,
        (
            "*cry*... I'm so glad to\x01",
            "see you again, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without\x01",
            "saying anything, I'll never\x01",
            "forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah... I promise.\x01",
            "Thanks, Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD8")

    Jump("loc_5076")

    label("loc_4FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FEF")
    Call(0, 10)
    Jump("loc_5076")

    label("loc_4FEF")


    ChrTalk(
        0xA,
        (
            "*cry*... I'm so glad to\x01",
            "see you again, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without\x01",
            "saying anything, I'll never\x01",
            "forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5076")

    Jump("loc_61E5")

    label("loc_507B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_513B")

    ChrTalk(
        0xA,
        (
            "To think something like\x01",
            "this happened to\x01",
            "Crossbell...\x02",
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
    Jump("loc_51A5")

    label("loc_513B")


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

    label("loc_51A5")

    Jump("loc_61E5")

    label("loc_51AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5466")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51DC")
    Call(0, 53)
    Return()

    label("loc_51DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5346")

    ChrTalk(
        0xA,
        (
            "...Just before she\x01",
            "disappeared, Rixia left\x01",
            "a letter for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            ""I'll be away from\x01",
            "Crossbell due to some\x01",
            "circumstances" she wrote...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Leaving Arc-en-Ciel out\x01",
            "to dry... That doesn't\x01",
            "sound like Rixia at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I wonder what kind of circumstances\x01",
            "they were. It would have been better\x01",
            "if she discussed it with me first...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_53E4")

    label("loc_5346")


    ChrTalk(
        0xA,
        (
            "To leave Arc-en-Ciel out to\x01",
            "dry and disappear... That\x01",
            "doesn't seem like Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Something that she\x01",
            "couldn't even discuss with\x01",
            "me, her best friend...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E4")

    Jump("loc_5461")

    label("loc_53E9")


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
            "There's still time until\x01",
            "the program, so contact\x01",
            "me later, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5461")

    Jump("loc_61E5")

    label("loc_5466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_559F")

    ChrTalk(
        0xA,
        (
            "I spotted Rixia going to\x01",
            "Arc-en-Ciel early this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I greeted her, but...\x01",
            "She seemed very down for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_END)), "loc_5542")

    ChrTalk(
        0x101,
        (
            "#00008F(...I guess all we can\x01",
            "do now is keep quiet...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5597")

    label("loc_5542")


    ChrTalk(
        0x101,
        (
            "#00003F(...Rixia... Did she go\x01",
            "to Arc-en-Ciel to check\x01",
            "on the situation there?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5597")

    SetScenarioFlags(0x0, 2)
    Jump("loc_5632")

    label("loc_559F")


    ChrTalk(
        0xA,
        (
            "I saw Rixia this\x01",
            "morning... She seemed\x01",
            "very down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I wonder if something\x01",
            "happened. If it's something I\x01",
            "can help with, I would like to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5632")

    Jump("loc_61E5")

    label("loc_5637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_578C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56EB")

    ChrTalk(
        0xA,
        (
            "Rixia said she had\x01",
            "something to attend to\x01",
            "and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*, I would have liked to talk\x01",
            "to her a little longer, but... I\x01",
            "guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5787")

    label("loc_56EB")


    ChrTalk(
        0xA,
        (
            "I would have liked to\x01",
            "talk to her a little\x01",
            "longer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If she has something to attend\x01",
            "to, it can't be helped. ...I've\x01",
            "got to get back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5787")

    Jump("loc_61E5")

    label("loc_578C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_581A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A7")
    Call(0, 48)
    Jump("loc_5815")

    label("loc_57A7")


    ChrTalk(
        0xA,
        (
            "Ehehe... It must've been\x01",
            "embarrassing for Rixia\x01",
            "to say that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Let's be lifelong\x01",
            "friends, Rixia!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5815")

    Jump("loc_61E5")

    label("loc_581A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_58AF")

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
        (
            "Enough already! Papa's\x01",
            "one tough customer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E5")

    label("loc_58AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5959")

    ChrTalk(
        0xA,
        (
            "...Gourmet guide\x01",
            "coverage? Yeah, I heard\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Papa's in the kitchen.\x01",
            "Why not try asking him\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_5959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59ED")

    ChrTalk(
        0xA,
        (
            "Papa and Fei said just\x01",
            "to do the finances\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Puck and Ruth are\x01",
            "always so busy. I wonder\x01",
            "if they'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A6C")

    label("loc_59ED")


    ChrTalk(
        0xA,
        (
            "Puck is waiting on all\x01",
            "the tables today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...He looks really busy. I\x01",
            "wonder if it's really ok\x01",
            "for me not to help him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6C")

    Jump("loc_61E5")

    label("loc_5A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B36")

    ChrTalk(
        0xA,
        (
            "Welcome. Ordering\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like all our\x01",
            "customers today are talking\x01",
            "about the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The mayor said it, but\x01",
            "does it really make it\x01",
            "that important?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E5")

    label("loc_5B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C0B")

    ChrTalk(
        0xA,
        (
            "I'm the one who recommended\x01",
            "my childhood friends Puck and\x01",
            "Ruth to work here part time.\x02",
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
            "I as well as papa are\x01",
            "proud of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5C7B")

    label("loc_5C0B")


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
            "I as well as papa are\x01",
            "proud of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7B")

    Jump("loc_61E5")

    label("loc_5C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D70")

    ChrTalk(
        0xA,
        (
            "According to Papa, the Republic\x01",
            "has even more Easterners than\x01",
            "Crossbell does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because I came here when I\x01",
            "was small, I don't\x01",
            "remember it at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like a very\x01",
            "busy place. It seems\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5DFB")

    label("loc_5D70")


    ChrTalk(
        0xA,
        (
            "It seems the Republic\x01",
            "has even more Easterners\x01",
            "than Crossbell does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems lively and fun.\x01",
            "I'd like to go if I get\x01",
            "the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFB")

    Jump("loc_61E5")

    label("loc_5E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E99")
    TurnDirection(0xA, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "Ah, you're that cute\x01",
            "customer from earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Come again, ok? We'll be\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "R-Right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F2C")

    label("loc_5E99")


    ChrTalk(
        0xA,
        (
            "That lady sitting at the\x01",
            "counter says she's a\x01",
            "reporter from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha. Since she's here,\x01",
            "I wonder if she'll take\x01",
            "a cute photo of me~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F2C")

    Jump("loc_61E5")

    label("loc_5F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_609A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_602B")

    ChrTalk(
        0xA,
        (
            "I can't believe that Feng.\x01",
            "He tried to seduce Rixia.\x01",
            "He's a problem child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Rixia should be able to\x01",
            "find someone way better\x01",
            "than him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though it may be rude to\x01",
            "Feng, as Rixia's friend,\x01",
            "I can't give her to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6095")

    label("loc_602B")


    ChrTalk(
        0xA,
        (
            "Rixia should be able to\x01",
            "find someone way better\x01",
            "than him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ehehe. As her friend, I\x01",
            "guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6095")

    Jump("loc_61E5")

    label("loc_609A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_61E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6133")

    ChrTalk(
        0xA,
        (
            "Welcome. Please, sit\x01",
            "wherever you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Papa may be a little\x01",
            "scary, but his food is the\x01",
            "best thing on this earth!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_61E5")

    label("loc_6133")


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
            "All our customers are good\x01",
            "people. If it stays like this,\x01",
            "I could work here forever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E5")

    Return()

    # Function_9_4B59 end

    def Function_10_61E6(): pass

    label("Function_10_61E6")


    ChrTalk(
        0xA,
        (
            "Rixia... I wonder what\x01",
            "she's doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To think something like\x01",
            "this has happened to\x01",
            "Crossbell... I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...It might be good to\x01",
            "have her stop by later,\x01",
            "huh...)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_10_61E6 end

    def Function_11_62A4(): pass

    label("Function_11_62A4")

    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    ChrTalk(
        0xA,
        (
            "R-Rixia... Is it really\x01",
            "you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Where have you been!?\x01",
            "I was super worried\x01",
            "about you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703FSorry, Shanshan... for\x01",
            "worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oooh... Seriously!\x01",
            "You're such an idiot,\x01",
            "Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...But... Thank goodness\x01",
            "I got to see you\x01",
            "again~... Waaaaaah~~~...\x02",
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
            "*cry*... I mean, I was\x01",
            "really worried about\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without\x01",
            "saying anything, I'll never\x01",
            "forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah, I'm really sorry.\x01",
            "...Thanks for waiting\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Rixia... Thank\x01",
            "goodness.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 0)
    Return()

    # Function_11_62A4 end

    def Function_12_6507(): pass

    label("Function_12_6507")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_6608")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_651D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6603")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Rest\x01",        # 2
            "Cancel\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_657E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_657E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_659D")
    OP_AF(0x34)
    Jump("loc_659F")

    label("loc_659D")

    OP_AF(0x33)

    label("loc_659F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65FE")

    label("loc_65AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65CE")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65FE")

    label("loc_65CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65E2")
    Jump("loc_65FE")

    label("loc_65E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65FE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_65FE")

    Jump("loc_651D")

    label("loc_6603")

    Jump("loc_660B")

    label("loc_6608")

    Call(0, 13)

    label("loc_660B")

    TalkEnd(0xB)
    Return()

    # Function_12_6507 end

    def Function_13_660F(): pass

    label("Function_13_660F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66CB")

    ChrTalk(
        0xB,
        (
            "Everyone's happy with a\x01",
            "full belly. That's the\x01",
            "master's motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I open a store with Ruth\x01",
            "in the future, I think of the\x01",
            "customers in just that way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6750")

    label("loc_66CB")


    ChrTalk(
        0xB,
        (
            "And so, today we have a large\x01",
            "serving for free, and as many\x01",
            "second helpings as you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Chow down! It'll give\x01",
            "you energy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6750")

    Jump("loc_7388")

    label("loc_6755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_67D9")

    ChrTalk(
        0xB,
        (
            "I wonder if I have time to\x01",
            "clean. ...Although, there's\x01",
            "nowhere to run to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*... All I can do\x01",
            "is sigh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_67D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6867")

    ChrTalk(
        0xB,
        (
            "What's going to happen\x01",
            "now? I can't even guess,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You have to get through\x01",
            "times like these with\x01",
            "fighting spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_6867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_698D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_690C")

    ChrTalk(
        0xB,
        (
            "Fei went to help with\x01",
            "the charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm on kitchen duty\x01",
            "instead as master's\x01",
            "assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to do the best\x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6988")

    label("loc_690C")


    ChrTalk(
        0xB,
        (
            "Although what I can do\x01",
            "is only on the level of\x01",
            "simple chores...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Fei's not here, so I've\x01",
            "got to do the best I\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6988")

    Jump("loc_7388")

    label("loc_698D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A2C")

    ChrTalk(
        0xB,
        "100, 200, 300 mira...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, I'm better at the\x01",
            "register than I was\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The more you do\x01",
            "something, the better\x01",
            "you get, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_6A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2B")

    ChrTalk(
        0xB,
        (
            "When it comes to work, I think\x01",
            "you can do anything just with\x01",
            "fighting spirit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected, that line\x01",
            "of thinking might be\x01",
            "naive somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, for now, I've\x01",
            "got to do what I can! I\x01",
            "know that's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6B8C")

    label("loc_6B2B")


    ChrTalk(
        0xB,
        (
            "Me and Ruth were\x01",
            "depressed yesterday,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well for now, all I can\x01",
            "do is what I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8C")

    Jump("loc_7388")

    label("loc_6B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C2E")

    ChrTalk(
        0xB,
        "*sigh*, I'm so tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I watched Shanshan working I\x01",
            "thought it was all fun and games, but\x01",
            "it didn't turn out like that, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_6C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6CA0")

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
            "Waah, I'm so busy, my\x01",
            "head's spinning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_6CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD2")

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
            "It's certain that, for\x01",
            "our future, we have to\x01",
            "earn all we can now.\x02",
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
    Jump("loc_6E2D")

    label("loc_6DD2")


    ChrTalk(
        0xB,
        (
            "Hehe, I might have some ability\x01",
            "as an employee... I think I'll\x01",
            "try asking the master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2D")

    Jump("loc_7388")

    label("loc_6E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F51")

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
            "Ever since then, the master\x01",
            "makes scary faces at anyone\x01",
            "interested in Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Earlier, he glared at me\x01",
            "just for greeting her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, I wish he'd give\x01",
            "me a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6FDE")

    label("loc_6F51")


    ChrTalk(
        0xB,
        (
            "The master glared at me\x01",
            "just for greeting\x01",
            "Shanshan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's been like this ever\x01",
            "since Sunday School... I\x01",
            "wish he'd give me a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FDE")

    Jump("loc_7388")

    label("loc_6FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_707D")

    ChrTalk(
        0xB,
        (
            "Ruth tries to\x01",
            "standardize anything and\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's why I wouldn't mind\x01",
            "at all even if we ran a\x01",
            "restaurant like we planned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_707D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7121")

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
            "we'll definitely be big shots!\x01",
            "Nothing will come of worrying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7388")

    label("loc_7121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71A2")

    ChrTalk(
        0xB,
        (
            "Ouchie... I slipped and\x01",
            "fell just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uwah~, this pain! My\x01",
            "fighting spirit just\x01",
            "flew away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7242")

    label("loc_71A2")


    ChrTalk(
        0xB,
        (
            "...Ouchie. It hurts when you\x01",
            "try to bring out your fighting\x01",
            "spirit and it doesn't come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You guys be careful not\x01",
            "to slip and fall in\x01",
            "today's rain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7242")

    Jump("loc_7388")

    label("loc_7247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_732C")

    ChrTalk(
        0xB,
        (
            "A while back, me and my\x01",
            "partner Ruth started\x01",
            "working part time.\x02",
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
    Jump("loc_7388")

    label("loc_732C")


    ChrTalk(
        0xB,
        (
            "But, I kinda like\x01",
            "working here as an\x01",
            "assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think I'll make the\x01",
            "most of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7388")

    Return()

    # Function_13_660F end

    def Function_14_7389(): pass

    label("Function_14_7389")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_748A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_739F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7485")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Rest\x01",        # 2
            "Cancel\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7400")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7400")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_741F")
    OP_AF(0x34)
    Jump("loc_7421")

    label("loc_741F")

    OP_AF(0x33)

    label("loc_7421")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7480")

    label("loc_7430")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7450")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7480")

    label("loc_7450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7464")
    Jump("loc_7480")

    label("loc_7464")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7480")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 15)

    label("loc_7480")

    Jump("loc_739F")

    label("loc_7485")

    Jump("loc_748D")

    label("loc_748A")

    Call(0, 15)

    label("loc_748D")

    TalkEnd(0xC)
    Return()

    # Function_14_7389 end

    def Function_15_7491(): pass

    label("Function_15_7491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_767D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75DC")

    ChrTalk(
        0xC,
        (
            "I'm sure this experience of doing\x01",
            "our best in times of crisis will\x01",
            "be of use to us in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I plan to open a huge shop with my partner\x01",
            "Puck in the future, but... For now, we've got\x01",
            "to do our best with the work in front of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Alright, if that's\x01",
            "how it's going to be,\x01",
            "I'll clean!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7678")

    label("loc_75DC")


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
            "...Alright, if that's\x01",
            "how it's going to be,\x01",
            "I'll clean!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7678")

    Jump("loc_856C")

    label("loc_767D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_76E0")

    ChrTalk(
        0xC,
        (
            "Those things walking\x01",
            "around outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What are they going to\x01",
            "do to us...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_856C")

    label("loc_76E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7766")

    ChrTalk(
        0xC,
        (
            "Hyaha, they say\x01",
            "Crossbell's gonna be\x01",
            "independent, huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ah, but good for them.\x01",
            "The cleaning's heating\x01",
            "up too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_856C")

    label("loc_7766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_77E2")

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
    Jump("loc_856C")

    label("loc_77E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7898")

    ChrTalk(
        0xC,
        (
            "Hmm, if I sweep this\x01",
            "problematic square floor\x01",
            "in a circle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would have been done faster if I\x01",
            "did this from the start. Cleaning\x01",
            "is harder than I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_856C")

    label("loc_7898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7960")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage? Ah,\x01",
            "come to think of it, the master\x01",
            "said something about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Master's in the kitchen.\x01",
            "You should speak with\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AEC")

    label("loc_7960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A61")

    ChrTalk(
        0xC,
        (
            "I was crushed by my\x01",
            "experience in the kitchen\x01",
            "yesterday, but...\x02",
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
            "even do simple work, huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7AEC")

    label("loc_7A61")


    ChrTalk(
        0xC,
        (
            "In order to open a huge\x01",
            "shop with my partner Puck\x01",
            "in the future too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now, we have to become\x01",
            "able to complete chores\x01",
            "perfectly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AEC")

    Jump("loc_856C")

    label("loc_7AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7B5C")

    ChrTalk(
        0xC,
        (
            "...I'm finally free of\x01",
            "Gehenna's kitchen.\x02",
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
    Jump("loc_856C")

    label("loc_7B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BCF")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Ah, heat! And the wok,\x01",
            "it's so heavy!\x02",
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
    Jump("loc_7C51")

    label("loc_7BCF")


    ChrTalk(
        0xC,
        (
            "E-Eek... When I helped\x01",
            "before, I thought it'd\x01",
            "be cake, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To think it'd be this\x01",
            "hard to make even one\x01",
            "fried rice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C51")

    Jump("loc_856C")

    label("loc_7C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7EB0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D1E")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage? Ah,\x01",
            "come to think of it, the master\x01",
            "said something about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Master's in the kitchen.\x01",
            "You should speak with\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EAB")

    label("loc_7D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0F")

    ChrTalk(
        0xC,
        (
            "I knew we couldn't get by\x01",
            "with these part time jobs of\x01",
            "nothing but small chores...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For now, I'll try asking\x01",
            "the master how we can do\x01",
            "more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What? For I, the great\x01",
            "Ruth, any kind of work\x01",
            "is a walk in the park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7EAB")

    label("loc_7E0F")


    ChrTalk(
        0xC,
        (
            "We've got to step up and\x01",
            "rid ourselves of these\x01",
            "chores soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I helped in the kitchen a bit\x01",
            "a while back... This time,\x01",
            "I'll try asking the master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EAB")

    Jump("loc_856C")

    label("loc_7EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7FF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F89")

    ChrTalk(
        0xC,
        (
            "All of a sudden, the\x01",
            "places we have to clean\x01",
            "doubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could that Puck have\x01",
            "spoken to Shanshan in\x01",
            "front of the master?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if that's true, how\x01",
            "are we both responsible?\x01",
            "Ugh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7FF4")

    label("loc_7F89")


    ChrTalk(
        0xC,
        (
            "Ah, later I've got to\x01",
            "clean the back of the\x01",
            "store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Puck happily handled\x01",
            "another large cleanup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF4")

    Jump("loc_856C")

    label("loc_7FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80BF")

    ChrTalk(
        0xC,
        (
            "Puck said it'd be good to\x01",
            "open our own restaurant in\x01",
            "the future or something.\x02",
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
    Jump("loc_8130")

    label("loc_80BF")


    ChrTalk(
        0xC,
        (
            "I plan to open a huge\x01",
            "shop with Puck in the\x01",
            "future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A restaurant, huh? I'm\x01",
            "not sure about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8130")

    Jump("loc_856C")

    label("loc_8135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_826A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F3")

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
            "goal of opening a shop\x01",
            "together in the future...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8265")

    label("loc_81F3")


    ChrTalk(
        0xC,
        (
            "We only took this job as\x01",
            "a way to get mira for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That Puck sure looks\x01",
            "like he's enjoying\x01",
            "himself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8265")

    Jump("loc_856C")

    label("loc_826A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_840B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8370")

    ChrTalk(
        0xC,
        (
            "*sigh*... The sound of\x01",
            "the rain makes me feel\x01",
            "depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're saving little-by-\x01",
            "little, but the day we open\x01",
            "our store is still far-off.\x02",
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
    Jump("loc_8406")

    label("loc_8370")


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
            "I think I'll ask Puck\x01",
            "what he thinks about\x01",
            "this later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8406")

    Jump("loc_856C")

    label("loc_840B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_856C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84CE")

    ChrTalk(
        0xC,
        (
            "My partner Puck and I have\x01",
            "started working part time for\x01",
            "capital to open our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "These are our early days\x01",
            "for when one day we'll\x01",
            "open our store, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_856C")

    label("loc_84CE")


    ChrTalk(
        0xC,
        (
            "But the master is harsh,\x01",
            "and the pay is low...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We got hired because we're childhood\x01",
            "friends with Shanshan, but... I'm\x01",
            "kind of regretting it lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_856C")

    Return()

    # Function_15_7491 end

    def Function_16_856D(): pass

    label("Function_16_856D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86AB")

    ChrTalk(
        0xFE,
        (
            "*munch, crunch*... We've\x01",
            "resumed our shipping\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until now, our routes have been mostly to\x01",
            "the Republic, but it seems we'll have to\x01",
            "stick within state borders for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what we have to do isn't\x01",
            "all that different. We just have\x01",
            "to do our best going forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8763")

    label("loc_86AB")


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
            "I had a proper meal beforehand,\x01",
            "so I'll be able to do my best,\x01",
            "the same as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8763")

    Jump("loc_947D")

    label("loc_8768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8776")
    Jump("loc_947D")

    label("loc_8776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8859")

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen,\x01",
            "independence is a happy\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that hero, Arios\x01",
            "MacLaine, bears the\x01",
            "burden of state defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if the Empire or\x01",
            "Republic is our enemy,\x01",
            "that's reassuring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_894B")

    label("loc_8859")


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
            "After all is said and done, that\x01",
            "Divine Blade of Wind is in Crossbell.\x01",
            "I'm sure he'll protect us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894B")

    Jump("loc_947D")

    label("loc_8950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A37")

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
            "The atmosphere there is\x01",
            "a lot more tense than\x01",
            "usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like they're paying more\x01",
            "attention to the people coming\x01",
            "and going than usual, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8AA7")

    label("loc_8A37")


    ChrTalk(
        0xFE,
        (
            "I can't run my business\x01",
            "if the border gate is\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll eat my\x01",
            "food. *crunch, munch*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AA7")

    Jump("loc_947D")

    label("loc_8AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8B5F")

    ChrTalk(
        0xFE,
        (
            "To think Mainz is occupied...\x01",
            "I don't know what's happened,\x01",
            "but that's unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the CGF are elites.\x01",
            "Will it be all right if\x01",
            "we leave it to them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947D")

    label("loc_8B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8BD7")

    ChrTalk(
        0xFE,
        (
            "Rain again today,\x01",
            "unfortunately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dangerous to drive\x01",
            "in the rain. I've got to\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947D")

    label("loc_8BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8CF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C91")

    ChrTalk(
        0xFE,
        (
            "It seems the waiter girl\x01",
            "is back again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm finished, I\x01",
            "think I'll have a\x01",
            "drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Huh, what!? It's past\x01",
            "time to start the\x01",
            "deliveries!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8CF2")

    label("loc_8C91")


    ChrTalk(
        0xFE,
        (
            "T-This isn't good. I\x01",
            "should have left for\x01",
            "deliveries hours ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I've got to hurry...\x02",
    )

    CloseMessageWindow()

    label("loc_8CF2")

    Jump("loc_947D")

    label("loc_8CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8D97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D49")

    ChrTalk(
        0xFE,
        "Oh...\x02",
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
    Jump("loc_8D92")

    label("loc_8D49")


    ChrTalk(
        0xFE,
        (
            "I always knew this shop\x01",
            "exists because of that\x01",
            "waiter girl's smile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D92")

    Jump("loc_947D")

    label("loc_8D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E62")

    ChrTalk(
        0xFE,
        (
            "The most capable orbal\x01",
            "truck is Verne Co.'s\x01",
            "latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, the latest model is\x01",
            "out of reach of\x01",
            "companies like mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In short, they're just\x01",
            "that expensive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8EE1")

    label("loc_8E62")


    ChrTalk(
        0xFE,
        (
            "I can't very well buy\x01",
            "the latest orbal car\x01",
            "model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's especially tough for\x01",
            "companies that aren't in\x01",
            "the best shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EE1")

    Jump("loc_947D")

    label("loc_8EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8F80")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm a little\x01",
            "interested in the trade\x01",
            "conference, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got work to do.\x01",
            "I've got to eat while I\x01",
            "can. *crunch, munch*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947D")

    label("loc_8F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9010")

    ChrTalk(
        0xFE,
        (
            "Wow, East Street is\x01",
            "super busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, traffic regulations\x01",
            "are suspended... I've got to\x01",
            "get back to work while I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947D")

    label("loc_9010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_921D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9164")

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
            "for the trade conference, and we're\x01",
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
    Jump("loc_9218")

    label("loc_9164")


    ChrTalk(
        0xFE,
        (
            "There will be traffic restrictions\x01",
            "tomorrow from Tangram Gate to East\x01",
            "Crossbell Highway.\x02",
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

    label("loc_9218")

    Jump("loc_947D")

    label("loc_921D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C0")

    ChrTalk(
        0xFE,
        (
            "If I remember correctly,\x01",
            "they said there'll be rain\x01",
            "over a wide area today.\x02",
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
    Jump("loc_947D")

    label("loc_92C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_947D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93C3")

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
            "which flows through the border and\x01",
            "floored it through Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. The\x01",
            "transport industry isn't\x01",
            "fun at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_947D")

    label("loc_93C3")


    ChrTalk(
        0xFE,
        (
            "I crossed the huge Cyre River which\x01",
            "flows through the Republic border\x01",
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

    label("loc_947D")

    TalkEnd(0xFE)
    Return()

    # Function_16_856D end

    def Function_17_9481(): pass

    label("Function_17_9481")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm worried about my\x01",
            "stand, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are President Mors and\x01",
            "Roy all right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_9481 end

    def Function_18_94DB(): pass

    label("Function_18_94DB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Lily, I'm here, so don't\x01",
            "be sad, ok?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_94DB end

    def Function_19_950C(): pass

    label("Function_19_950C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Danes, I'm scared...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_950C end

    def Function_20_952D(): pass

    label("Function_20_952D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I hope my husband is\x01",
            "safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. Now that it's like\x01",
            "this, I have to close up\x01",
            "shop immediately.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_952D end

    def Function_21_95A6(): pass

    label("Function_21_95A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95BA")
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    label("loc_95BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95DB")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95DB")
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    label("loc_95DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F6")

    ChrTalk(
        0x25,
        (
            "#03204FWe plan to wait-and-see for now,\x01",
            "until the situation's resolved.\x02\x03",
            "After that, we'll slowly take over\x01",
            "the underworld, from which Revache\x01",
            "and Red Constellation are gone.\x02\x03",
            "#03210FHaha. It might not be too long\x01",
            "before we're enemies. I look\x01",
            "forward to then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9798")

    label("loc_96F6")


    ChrTalk(
        0x25,
        (
            "#03204FWe plan to wait-and-see\x01",
            "for now, until the\x01",
            "situation's resolved.\x02\x03",
            "#03210FHaha. It might not be too\x01",
            "long before we're enemies.\x01",
            "I look forward to then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9798")

    TalkEnd(0xFE)
    Return()

    # Function_21_95A6 end

    def Function_22_979C(): pass

    label("Function_22_979C")


    ChrTalk(
        0x25,
        (
            "#03200FOh, Lloyd and the\x01",
            "others... Good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FC-Cao? What are you\x01",
            "doing in a place like\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FHaha, is there something\x01",
            "strange about us being\x01",
            "here?\x02\x03",
            "#03200FThe city has calmed\x01",
            "down, so we were just\x01",
            "relaxing having a meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBut even so, that's a\x01",
            "little too bold, isn't\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FA-And what's more, a\x01",
            "seat right in the middle\x01",
            "of the restaurant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "I wasn't sure what\x01",
            "others would think\x01",
            "either, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "The waitress picked this\x01",
            "seat for us, and Master\x01",
            "Cao didn't refuse it.\x02",
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
            "#03204FHaha, isn't it fine? We'd appreciate if\x01",
            "you'd let us take it easy at least while\x01",
            "we're eating.\x02\x03",
            "#03200FIt's been a while since we fought against\x01",
            "Red Constellation as hard as we did in\x01",
            "the Crossbell liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Regarding that. Thank\x01",
            "you very much for your\x01",
            "cooperation.\x02\x03",
            "#00001FMr. Cao, what do you and\x01",
            "the others plan to do\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03205FWe plan to keep watching the\x01",
            "situation until it's under\x01",
            "control.\x02\x03",
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
            "#03204FNow that our Red Constellation and Revache\x01",
            "competition is gone, there's no further\x01",
            "obstacles in our way.\x02\x03",
            "#03202FHaha. There were many twists and turns, but...\x01",
            "It seems our original goal of gaining control of\x01",
            "Crossbell's underworld will finally be realized.\x02\x03",
            "And it's no exaggeration to say it's also due to\x01",
            "the efforts of Yin, who you all have worked with\x01",
            "several times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013FUgh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E09")

    ChrTalk(
        0x106,
        "#10708F...............\x02",
    )

    CloseMessageWindow()

    label("loc_9E09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E6D")

    ChrTalk(
        0x10A,
        (
            "#00603F...Sooner or later,\x01",
            "we're going to have to\x01",
            "face Heiyue once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F39")

    label("loc_9E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ED6")

    ChrTalk(
        0x109,
        (
            "#10103F...It seems we're going\x01",
            "to have to face Heiyue\x01",
            "again sooner or later...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F39")

    label("loc_9ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F39")

    ChrTalk(
        0x105,
        (
            "#10403FLooks like we're going\x01",
            "to have to face Heiyue\x01",
            "again sooner or later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F39")


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
            "#00003F...No matter what\x01",
            "Barriers you put in our\x01",
            "way...\x02\x03",
            "#00001FWe definitely won't\x01",
            "lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03209FHaha. That's why you're you.\x02\x03",
            "#03204FWell, people like us are no\x01",
            "significant Barrier.\x02\x03",
            "#03210FCompared to the chaos throughout\x01",
            "the continent... and especially\x01",
            "the threat from the west.\x02",
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
            "#03204FHaha, well for now, please\x01",
            "focus on doing something\x01",
            "about this situation.\x02\x03",
            "#03200FWe'll be rooting for you\x01",
            "here, from the shadows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 1)
    Return()

    # Function_22_979C end

    def Function_23_A169(): pass

    label("Function_23_A169")


    ChrTalk(
        0x25,
        (
            "#03204FThat's right... Once this situation\x01",
            "is under control, I was thinking of\x01",
            "forming another contract with Rixia.\x02\x03",
            "#03202FHaha. What do you say, Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F...You'll owe me for this time,\x01",
            "and I don't know how you're\x01",
            "planning on repaying me...\x02\x03",
            "#10701FAt this time, I cannot answer\x01",
            ""yes" to that question.\x02",
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
            "#03204FWell, we have no right to\x01",
            "force you.\x02\x03",
            "And after this time, we'll\x01",
            "be even, so there'll be no\x01",
            "need for payment.\x02\x03",
            "#03200FHowever, if you feel you\x01",
            "are in our debt...\x02\x03",
            "#03209FArc-en-Ciel S-seat tickets\x01",
            "will be appropriate\x01",
            "compensation, I believe.\x02",
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
            "#03204FHaha, that was a joke.\x02\x03",
            "#03200FIt's just... As I said before, to\x01",
            "reach the high place Heiyue is\x01",
            "aiming for, we want your strength.\x02\x03",
            "I will support your performances,\x01",
            "and I look forward to being\x01",
            "friends from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 2)
    Return()

    # Function_23_A169 end

    def Function_24_A506(): pass

    label("Function_24_A506")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A51B")
    Call(0, 22)
    Jump("loc_A66E")

    label("loc_A51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5ED")

    ChrTalk(
        0xFE,
        (
            "...Regarding the\x01",
            "incident this time,\x01",
            "thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We vacated our hideout\x01",
            "in the old battlefield\x01",
            "some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't help you any\x01",
            "more, but... Please, do\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A66E")

    label("loc_A5ED")


    ChrTalk(
        0xFE,
        (
            "We vacated our hideout\x01",
            "in the old battlefield\x01",
            "some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't help you any\x01",
            "more, but... Please, do\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66E")

    TalkEnd(0xFE)
    Return()

    # Function_24_A506 end

    def Function_25_A672(): pass

    label("Function_25_A672")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I came to enjoy a\x01",
            "restaurant meal with my\x01",
            "family today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems they're\x01",
            "enjoying it. I'm glad.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_A672 end

    def Function_26_A6E9(): pass

    label("Function_26_A6E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7B4")

    ChrTalk(
        0xFE,
        (
            "*breathe, breathe*,\x01",
            "*slurp, slurp*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These noodles have a\x01",
            "spicy and stimulating\x01",
            "flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think a meal could make\x01",
            "one sweat this much... But,\x01",
            "it's really delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A821")

    label("loc_A7B4")


    ChrTalk(
        0xFE,
        (
            "I absolutely love these\x01",
            "noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though they're spicy and\x01",
            "make you sweat, they're\x01",
            "quite delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A821")

    TalkEnd(0xFE)
    Return()

    # Function_26_A6E9 end

    def Function_27_A825(): pass

    label("Function_27_A825")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm eating out with my\x01",
            "family today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chew, chew*... This\x01",
            ""Mapo" is great.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_A825 end

    def Function_28_A881(): pass

    label("Function_28_A881")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*purr purr* nyaan...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_A881 end

    def Function_29_A8A2(): pass

    label("Function_29_A8A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACFF")

    ChrTalk(
        0x20,
        (
            "I'm sorry Temas, but\x01",
            "this food is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "*crunch, munch*...\x01",
            "Alright, I think I'll\x01",
            "have seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh? Why is there a CGF\x01",
            "member in a place like\x01",
            "this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FCould it be... Are you\x01",
            "Alexei?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA31")
    Jump("loc_AA7B")

    label("loc_AA31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA51")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA7B")

    label("loc_AA51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA71")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA7B")

    label("loc_AA71")

    OP_52(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA7B")

    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    ChrTalk(
        0x20,
        (
            "Oh, Sergeant Noｱl. Fancy\x01",
            "meeting you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'm on break, see? I'm\x01",
            "just relaxing here,\x01",
            "eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FYou never change, do you. Coming\x01",
            "here all the way from Tangram\x01",
            "Gate just to have lunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FTangram Gate... Is it\x01",
            "that border gate past\x01",
            "the east highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, is an important defensive\x01",
            "position for Crossbell and\x01",
            "managed by the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Recently, a new vice commander\x01",
            "was assigned and we've been\x01",
            "busy doing stuff ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Sgt. Noｱl, you must be doing\x01",
            "your best too. All of us at\x01",
            "the gate are cheering for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 6)
    ClearChrFlags(0x20, 0x10)
    Jump("loc_AEBC")

    label("loc_ACFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE11")

    ChrTalk(
        0x20,
        (
            "Recently, a new vice\x01",
            "commander was assigned and\x01",
            "we've been busy ever since.\x02",
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
            "Every once in a while, I like\x01",
            "to relax in town, eat something\x01",
            "different and refresh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_AEBC")

    label("loc_AE11")


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
            "Every once in a while, I like\x01",
            "to relax in town, eat something\x01",
            "different and refresh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEBC")

    TalkEnd(0xFE)
    Return()

    # Function_29_A8A2 end

    def Function_30_AEC0(): pass

    label("Function_30_AEC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AF3D")

    ChrTalk(
        0xFE,
        (
            "To think it'd rain when\x01",
            "it's our long-awaited\x01",
            "vacation...\x02",
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
    Jump("loc_AF8F")

    label("loc_AF3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AF8F")

    ChrTalk(
        0xFE,
        (
            "Hmm, this is really\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew Eastern cuisine\x01",
            "was the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF8F")

    TalkEnd(0xFE)
    Return()

    # Function_30_AEC0 end

    def Function_31_AF93(): pass

    label("Function_31_AF93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AFF4")

    ChrTalk(
        0xFE,
        "Now, now, old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you eat something\x01",
            "warm here, it'll warm\x01",
            "you up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B027")

    label("loc_AFF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B027")

    ChrTalk(
        0xFE,
        (
            "I knew you'd like some\x01",
            "home cooking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B027")

    TalkEnd(0xFE)
    Return()

    # Function_31_AF93 end

    def Function_32_B02B(): pass

    label("Function_32_B02B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B0C3")

    ChrTalk(
        0xFE,
        (
            "(*chatting*...) *crunch,\x01",
            "munch*... Mmm, mmm...\x01",
            "This tourist guide is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell sure has a lot\x01",
            "of nice places, doesn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B200")

    label("loc_B0C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B165")

    ChrTalk(
        0xFE,
        (
            "(*clink, clink*...)\x01",
            "*slurrrp*... This is\x01",
            "really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, those reporters that\x01",
            "were staying here really went\x01",
            "after those interviews.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B200")

    label("loc_B165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B200")

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*... I\x01",
            "always knew Crossbell was\x01",
            "a place with nice scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like the city is\x01",
            "lively to match the\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B200")

    TalkEnd(0xFE)
    Return()

    # Function_32_B02B end

    def Function_33_B204(): pass

    label("Function_33_B204")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B289")

    ChrTalk(
        0xFE,
        (
            "Dear, what am I going to\x01",
            "do with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reading books is for\x01",
            "after you've finished\x01",
            "eating. How disgraceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B35E")

    label("loc_B289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B2F8")

    ChrTalk(
        0xFE,
        (
            "Dear, what am I going to\x01",
            "do with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stop making noise when\x01",
            "you eat. How\x01",
            "disgraceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B35E")

    label("loc_B2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B35E")

    ChrTalk(
        0xFE,
        (
            "Dear, what am I going to\x01",
            "do with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stop talking while you\x01",
            "eat. How disgraceful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B35E")

    TalkEnd(0xFE)
    Return()

    # Function_33_B204 end

    def Function_34_B362(): pass

    label("Function_34_B362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4B3")

    ChrTalk(
        0xFE,
        (
            "I'm telling you, airship service will\x01",
            "end today. It can't be helped. I've\x01",
            "decided to return home to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, I'd\x01",
            "normally stay a little longer\x01",
            "to get coverage, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, security in\x01",
            "Crossbell can't be\x01",
            "guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can only place our\x01",
            "hopes in the State\x01",
            "Guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B512")

    label("loc_B4B3")


    ChrTalk(
        0xFE,
        (
            "Anyway, I hope Crossbell\x01",
            "stays safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can only place our\x01",
            "hopes in the State\x01",
            "Guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B512")

    Jump("loc_B9DD")

    label("loc_B517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B53A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B532")
    Call(0, 45)
    Jump("loc_B535")

    label("loc_B532")

    Call(0, 46)

    label("loc_B535")

    Jump("loc_B9DD")

    label("loc_B53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B880")

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
        (
            "#00005FIf I recall, you're that\x01",
            "Liberl reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou're still in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I didn't return\x01",
            "home after the trade\x01",
            "conference, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why? Why did he deliver\x01",
            "such a sensational\x01",
            "proposal...?\x02",
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
        (
            "#00104FI see, so that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, since I'm here,\x01",
            "I plan to see the Arc-en-\x01",
            "Ciel renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, it's going\x01",
            "to be on opening day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOpening day... You did\x01",
            "well to get a ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. They're hard to get,\x01",
            "and there's a significant\x01",
            "premium attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Well, we reporters\x01",
            "have our methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I expect we'll be\x01",
            "running into each other\x01",
            "around town for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 0)
    Jump("loc_B933")

    label("loc_B880")


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
            "around town for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B933")

    Jump("loc_B9DD")

    label("loc_B938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B9DD")

    ChrTalk(
        0xFE,
        (
            "Haha, this store is on\x01",
            "the same level as those\x01",
            "in Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible Nial and the\x01",
            "others are eating Eastern\x01",
            "cuisine right around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9DD")

    TalkEnd(0xFE)
    Return()

    # Function_34_B362 end

    def Function_35_B9E1(): pass

    label("Function_35_B9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9F3")
    Call(0, 37)
    Jump("loc_BAAC")

    label("loc_B9F3")

    TalkBegin(0xFE)

    ChrTalk(
        0x17,
        (
            "#02109FNow then, I'll finish eating,\x01",
            "then go around town for\x01",
            "coverage.\x02\x03",
            "#02104FThe heads of state's guards are\x01",
            "tough, but I might have a chance\x01",
            "while they're moving around♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_BAAC")

    Return()

    # Function_35_B9E1 end

    def Function_36_BAAD(): pass

    label("Function_36_BAAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BABF")
    Call(0, 37)
    Jump("loc_BB63")

    label("loc_BABF")

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
            "And, if possible, I'd\x01",
            "like to get some photos\x01",
            "of the heads of state.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_BB63")

    Return()

    # Function_36_BAAD end

    def Function_37_BB64(): pass

    label("Function_37_BB64")

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
        (
            "#6POh, it's the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 0x2)
    Sleep(200)

    ChrTalk(
        0x17,
        (
            "#12P#02100FCould you guys be here\x01",
            "to eat?\x02\x03",
            "#02109FHaha, that aside, the\x01",
            "unveiling ceremony was\x01",
            "amazing!\x02",
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
            "#12P#02106FI know, right? Especially that\x01",
            "Blood and Iron Chancellor. He's\x01",
            "the real deal!\x02\x03",
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
            "#12P#02105FRight, right, come to think of\x01",
            "it, there was that secretary-ish\x01",
            "man next to the Chancellor...\x02\x03",
            "#02103FHuh? If I'm not mistaken, he's\x01",
            "Lechter who came to Crossbell\x01",
            "before, right?\x02",
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
            "#12P#02104FHaha, well I understand\x01",
            "why that's hard to\x01",
            "answer.\x02\x03",
            "#02101FActually, I just\x01",
            "remembered something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
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
            "#02100FOf course, you guys already know about it,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, well that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWe learned some of the truth\x01",
            "by following a certain line\x01",
            "of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103FYes... But, it wasn't then.\x02\x03",
            "Crossbell's mass media\x01",
            "didn't mention it, and\x01",
            "neither did the Empire's...\x02\x03",
            "#02101FOf course, even the\x01",
            "Crossbell Police didn't\x01",
            "catch wind of it.\x02",
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
            "#6PIt's as if he was\x01",
            "casually dropping by for\x01",
            "a short walk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P...Well, that's exactly\x01",
            "why secrecy is so\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmph... What an amazing\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FYeah. To be honest, I\x01",
            "can't even believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02106FYeah, you can't believe―\x01",
            "No, that's too harsh!\x02\x03",
            "#02100FAfterwards, I looked\x01",
            "into it every way that I\x01",
            "could.\x02\x03",
            "#02103FA lot of names came up\x01",
            "in my interviews, but...\x02\x03",
            "#02101FI remember his was among\x01",
            "them. The name Lechter.\x02",
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
            "#00101FTo think arranging the\x01",
            "meeting itself was\x01",
            "Lechter's doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHow to say this... Those\x01",
            "are impressive\x01",
            "counterintelligence skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103F...Right. A mere secretary\x01",
            "shouldn't be able to do\x01",
            "something like that.\x02\x03",
            "#02102FUnless he's a member of the\x01",
            "famed Imperial Army\x01",
            "Intelligence Division, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see...\x02\x03",
            "#00003F(That's Miss Grace for\x01",
            "you. She got all that by\x01",
            "herself.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Yeah. She so tenacious,\x01",
            "it's terrifying.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02109FHaha, it looks like I hit\x01",
            "the bullseye, huh?\x02\x03",
            "#02106F*sigh*, but I couldn't\x01",
            "believe that kid was\x01",
            "Lechter.\x02\x03",
            "#02102FWell, you guys have a job\x01",
            "to do so I won't detain\x01",
            "you any further, but...\x02\x03",
            "#02100FAnyway, it's sure that\x01",
            "Lechter kid isn't anybody\x01",
            "normal.\x02\x03",
            "You guys should brace\x01",
            "yourselves if you're\x01",
            "getting involved with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, we know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you for the\x01",
            "information.\x02",
        )
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

    # Function_37_BB64 end

    def Function_38_C853(): pass

    label("Function_38_C853")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C9BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C924")

    ChrTalk(
        0xFE,
        (
            "I fought with my husband\x01",
            "and ran away from home,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I finally apologized\x01",
            "yesterday while crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmm. I feel a little\x01",
            "guilty for pushing him\x01",
            "that far, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C9B5")

    label("loc_C924")


    ChrTalk(
        0xFE,
        (
            "*sigh*, well I got tired\x01",
            "of running away from\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like some kind of\x01",
            "incident occurred too... I\x01",
            "should be getting home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9B5")

    Jump("loc_CBC9")

    label("loc_C9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CA5A")

    ChrTalk(
        0xFE,
        (
            "I found my husband I'm\x01",
            "fighting with. He told\x01",
            "me to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, that's no way to\x01",
            "apologize. I didn't sense\x01",
            "any sincerity at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBC9")

    label("loc_CA5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CAE5")

    ChrTalk(
        0xFE,
        (
            "Looks like the waitress\x01",
            "reverted to the usual\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what happened\x01",
            "to the unreliable waiter\x01",
            "from before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBC9")

    label("loc_CAE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CB49")

    ChrTalk(
        0xFE,
        (
            "The waiter seems\x01",
            "unreliable somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like him to bring my\x01",
            "food already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBC9")

    label("loc_CB49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CBC9")

    ChrTalk(
        0xFE,
        (
            "Because I'm fighting\x01",
            "with my husband, I ran\x01",
            "away from home.\x02",
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

    label("loc_CBC9")

    TalkEnd(0xFE)
    Return()

    # Function_38_C853 end

    def Function_39_CBCD(): pass

    label("Function_39_CBCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CC2B")

    ChrTalk(
        0xFE,
        (
            "Aww, man. I'm tired of\x01",
            "my grandparents' house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to see papa.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD57")

    label("loc_CC2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CC5A")

    ChrTalk(
        0xFE,
        (
            "Is papa still not here\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD57")

    label("loc_CC5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CC95")

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*...\x01",
            "Ehehe, this is good!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD57")

    label("loc_CC95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CCF6")

    ChrTalk(
        0xFE,
        (
            "Mama, the table is kind\x01",
            "of sticky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did the store people\x01",
            "forget to clean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD57")

    label("loc_CCF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CD57")

    ChrTalk(
        0xFE,
        (
            "Mama's visiting her\x01",
            "parent's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Papa's coming later.\x01",
            "He's busy with work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD57")

    TalkEnd(0xFE)
    Return()

    # Function_39_CBCD end

    def Function_40_CD5B(): pass

    label("Function_40_CD5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF82")

    ChrTalk(
        0x1D,
        (
            "#04405FAh, everyone. Fancy\x01",
            "seeing you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, you're eating... it\x01",
            "looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04400FYes, I'm on break and\x01",
            "came here for something\x01",
            "to eat.\x02\x03",
            "#04403FThis place's fried rice\x01",
            "has a deep and good\x01",
            "flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha. You're the same as\x01",
            "ever, Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FI-It looks delicious,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Looks like there's a\x01",
            "lot of plates on the\x01",
            "counter...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hehe. The Old Dragon\x01",
            "and a sister don't match\x01",
            "very well at all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Elie missed that chance\x01",
            "for a retort. Is this\x01",
            "normal...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 3)
    Jump("loc_CFE3")

    label("loc_CF82")


    ChrTalk(
        0x1D,
        (
            "#04400FI'll head back to the\x01",
            "cathedral in a little\x01",
            "bit.\x02\x03",
            "I'll be there if\x01",
            "anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFE3")

    TalkEnd(0xFE)
    Return()

    # Function_40_CD5B end

    def Function_41_CFE7(): pass

    label("Function_41_CFE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183E, 7)), scpexpr(EXPR_END)), "loc_D070")

    ChrTalk(
        0xFE,
        (
            "I volunteered for\x01",
            "various things to help\x01",
            "with the reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Food is especially good\x01",
            "after hard work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183E, 7)
    Jump("loc_D0EA")

    label("loc_D070")


    ChrTalk(
        0xFE,
        (
            "It looks like the\x01",
            "Downtown repairs are\x01",
            "still in progress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still a lot of\x01",
            "things I can help them\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0EA")

    TalkEnd(0xFE)
    Return()

    # Function_41_CFE7 end

    def Function_42_D0EE(): pass

    label("Function_42_D0EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D120")
    Call(0, 54)
    Return()

    label("loc_D120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_D1AB")

    ChrTalk(
        0xFE,
        (
            "Yeah, with this, I might\x01",
            "finally get to see my\x01",
            "dad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm leaving\x01",
            "everything to you guys.\x01",
            "Please, find my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1AB")

    Jump("loc_D1FB")

    label("loc_D1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D1FB")

    ChrTalk(
        0xFE,
        (
            "Aerie and Almin...\x01",
            "Yesterday was one\x01",
            "amazing day, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1FB")

    TalkEnd(0xFE)
    Return()

    # Function_42_D0EE end

    def Function_43_D1FF(): pass

    label("Function_43_D1FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D231")
    Call(0, 54)
    Return()

    label("loc_D231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_D2A9")

    ChrTalk(
        0xFE,
        (
            "We'll definitely see\x01",
            "Alm's father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he'll hug\x01",
            "Almin, the fruit of our\x01",
            "love!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Babuu.\x02",
    )

    CloseMessageWindow()

    label("loc_D2A9")

    Jump("loc_D301")

    label("loc_D2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D301")

    ChrTalk(
        0xFE,
        (
            "Yes, Alm... Yesterday\x01",
            "was one amazing, amazing\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Babu♪\x02",
    )

    CloseMessageWindow()

    label("loc_D301")

    TalkEnd(0xFE)
    Return()

    # Function_43_D1FF end

    def Function_44_D305(): pass

    label("Function_44_D305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D31A")
    Call(0, 45)
    Jump("loc_D31D")

    label("loc_D31A")

    Call(0, 46)

    label("loc_D31D")

    TalkEnd(0xFE)
    Return()

    # Function_44_D305 end

    def Function_45_D321(): pass

    label("Function_45_D321")


    ChrTalk(
        0x27,
        (
            "I see, so you're staying\x01",
            "at The Old Dragon Inn\x01",
            "while you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Is the food here to your\x01",
            "liking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yes. It's so good, I'm\x01",
            "having trouble not\x01",
            "overeating.\x02",
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
        (
            "Haha, please don't worry\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Walking and wandering\x01",
            "are hobbies of mine,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Haha, I see.\x02",
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

    # Function_45_D321 end

    def Function_46_D4D0(): pass

    label("Function_46_D4D0")


    ChrTalk(
        0x16,
        (
            "But Mr. Nielsen, you're\x01",
            "staying for a long time\x01",
            "this time, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You're concerned about\x01",
            "developments in your\x01",
            "hometown, aren't you?\x02",
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
            "Anyway, I plan to stay\x01",
            "in Crossbell a while\x01",
            "longer.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_46_D4D0 end

    def Function_47_D5E3(): pass

    label("Function_47_D5E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F8")
    Call(0, 48)
    Jump("loc_D6BA")

    label("loc_D5F8")


    ChrTalk(
        0x1C,
        (
            "#01803FWhen I lived in the Republic,\x01",
            "I had to move repeatedly due\x01",
            "to my father's work...\x02\x03",
            "#01802FHaha, I'm really thankful to\x01",
            "Shanshan.\x02\x03",
            "My bonds with Ilya and\x01",
            "everyone are precious to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6BA")

    TalkEnd(0xFE)
    Return()

    # Function_47_D5E3 end

    def Function_48_D6BE(): pass

    label("Function_48_D6BE")

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
        "#01802FAh... Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHaha, hello Rixia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAre you here for lunch\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802FHaha, yes.\x02\x03",
            "Right now I was chatting\x01",
            "while having an after-\x01",
            "lunch dessert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PYou guys are those\x01",
            "police, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAww. And just when I was\x01",
            "enjoying some girl talk\x01",
            "with Rixia~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00302FHaha, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, meeting an artist\x01",
            "privately isn't a chance\x01",
            "you often get.\x02",
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
            "#01809FAhaha... Don't say that.\x01",
            "I'm still new.\x02\x03",
            "#01802FShanshan often takes me\x01",
            "places on my days off when\x01",
            "I'd just sit at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHaha. We're the same\x01",
            "age, so we get along\x01",
            "pretty well, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAnd Rixia's proportions are\x01",
            "cute. It's fun shopping for\x01",
            "clothes for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01809FAhaha, I don't want to\x01",
            "be seen as cute,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F(Hmm, it's certainly\x01",
            "true that there's not\x01",
            "many of Rixia's size...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F(...Rich people's\x01",
            "problems.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, but you guys\x01",
            "really are close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802FHaha, I'm really thankful to\x01",
            "Shanshan.\x02\x03",
            "#01803FWhen I lived in the Republic,\x01",
            "I had to move repeatedly due\x01",
            "to my father's work...\x02\x03",
            "#01808FI've had trouble making\x01",
            "friends and have always been\x01",
            "by myself.\x02",
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
        "#11PHaha, don't worry Rixia.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x1)

    ChrTalk(
        0xA,
        (
            "#11PNow that you're friends\x01",
            "with me, you'll never be\x01",
            "alone again.\x02",
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
            "#01802FAhaha... Thanks,\x01",
            "Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, looks like we're\x01",
            "the third wheel here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYeah, let's leave them\x01",
            "be.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x0)

    ChrTalk(
        0x1C,
        (
            "#01806FSorry, everyone. It\x01",
            "seems I took up your\x01",
            "valuable time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FWell, speaking with you\x01",
            "made a nice breather for\x01",
            "us.\x02\x03",
            "#00002FSee you.\x02",
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

    # Function_48_D6BE end

    def Function_49_DF6F(): pass

    label("Function_49_DF6F")

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

    def lambda_E024():
        OP_98(0x101, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E024)
    Sleep(50)

    def lambda_E041():
        OP_98(0x102, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E041)
    Sleep(50)

    def lambda_E05E():
        OP_98(0x109, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E05E)
    Sleep(50)

    def lambda_E07B():
        OP_98(0x105, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E07B)
    OP_68(890, 1400, -390, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_0D()

    def lambda_E0BD():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0BD)
    Sleep(50)

    def lambda_E0CD():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0CD)
    Sleep(50)

    def lambda_E0DD():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E0DD)
    Sleep(50)

    def lambda_E0ED():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E0ED)
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
        "#12P#00001FFound him!\x02",
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
            "#03500FI see... So you're using\x01",
            "pepper flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYeah. Compared to normal\x01",
            "pepper, the flavor and heat\x01",
            "are on a whole other level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIt's only cultivated in the\x01",
            "East, but fortunately I've been\x01",
            "able to order it recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03502F#11PMan, if only my own mapo\x01",
            "tofu was this good.\x02\x03",
            "#03504FHemp huh. I really\x01",
            "learned something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 5010, 0, 15540, 45)

    ChrTalk(
        0x101,
        (
            "#00000F#NLechter... There you\x01",
            "are.\x02",
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

    def lambda_E419():
        OP_98(0x101, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E419)
    Sleep(50)

    def lambda_E436():
        OP_98(0x102, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E436)
    Sleep(50)

    def lambda_E453():
        OP_98(0x109, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E453)
    Sleep(50)

    def lambda_E470():
        OP_98(0x105, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E470)
    Sleep(50)
    OP_68(14290, 1400, 14500, 1500)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00105F(Wow, we cornered him\x01",
            "fairly quickly.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(This guy seems\x01",
            "ridiculously carefree.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(If we can just confirm\x01",
            "his identity, it's\x01",
            "mission complete.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03505FOh, you finally came.\x02\x03",
            "#03509FI was waiting for you,\x01",
            "kindred spirits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x28,
        (
            "#12P#03502FMaster, these are the\x01",
            "ones I was just telling\x01",
            "you about.\x02\x03",
            "#03504FThey are very strong\x01",
            "willed, so please give\x01",
            "them a thorough lesson.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x28, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        "Right, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#11PFour at once 'll be tough,\x01",
            "but I'm always glad to\x01",
            "spread Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDo your best to keep up\x01",
            "with me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00012FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWhat are you talking\x01",
            "about...\x02",
        )
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

    def lambda_E7DF():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7DF)
    Sleep(50)

    def lambda_E7EF():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7EF)
    Sleep(50)

    def lambda_E7FF():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E7FF)
    Sleep(50)

    def lambda_E80F():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E80F)
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
        "#11P#00011FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FH-He escaped!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10309FHaha, why am I not\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FA-After him!\x02",
    )

    CloseMessageWindow()

    def lambda_E902():
        OP_98(0x8, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E902)
    Sound(802, 0, 100, 0)
    OP_68(13640, 1400, 14410, 1000)
    MoveCamera(37, 24, 0, 1000)

    ChrTalk(
        0x8,
        (
            "Where do you think\x01",
            "you're going?\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "The lesson's just begun!\x01",
            "First up is prep\x01",
            "training!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E9A3():
        OP_93(0x101, 0x5A, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E9A3)
    Sleep(50)

    def lambda_E9B3():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E9B3)
    Sleep(50)

    def lambda_E9C3():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E9C3)
    Sleep(50)

    def lambda_E9D3():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E9D3)

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No, you've got it all\x01",
            "wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FWe're with the Crossbell\x01",
            "Police─\x02",
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
            "Sorry for the\x01",
            "misunderstanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then again, this might\x01",
            "be some kind of sign.\x01",
            "Please accept this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC32")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Old Dragon Fried Rice\x01",
            "recipe\x07\x00",
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
            "#12P#00005FA-Are you sure? You even\x01",
            "gave us a recipe book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECBA")

    label("loc_EC32")

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
            "#12P#00005FWait, are you sure?\x01",
            "We're getting this for\x01",
            "free...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECBA")

    AddItemNumber(0x2, 1)

    ChrTalk(
        0x8,
        (
            "It's just a spare we had lying\x01",
            "around, don't worry about it. I hope\x01",
            "you devote yourself to your cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FThank you very much!\x01",
            "Well then, please excuse\x01",
            "us.\x02\x03",
            "#00001FCome on guys, after him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FRoger that!\x02",
    )

    CloseMessageWindow()

    def lambda_EDC8():
        OP_93(0x101, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDC8)

    def lambda_EDD5():
        OP_93(0x102, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EDD5)

    def lambda_EDE2():
        OP_93(0x109, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EDE2)

    def lambda_EDEF():
        OP_93(0x105, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EDEF)
    WaitChrThread(0x105, 1)

    def lambda_EE00():
        OP_98(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE00)
    Sleep(50)

    def lambda_EE1D():
        OP_98(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EE1D)
    Sleep(50)

    def lambda_EE3A():
        OP_98(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE3A)
    Sleep(50)

    def lambda_EE57():
        OP_98(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE57)
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
            "You can obtain cooking\x01",
            "[Recipes] by examining\x01",
            "books or special locations.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Recipes] are recorded in the [Recipe\x01",
            "Book]. You can make various potent dishes\x01",
            "anytime by using the [Recipe Book].\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, completed dishes will change to [Great\x01",
            "Success] and [Unexpected] versions with a certain\x01",
            "probability. It's also possible to fail at cooking.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The general store and other\x01",
            "stores sell [Ingredients] used in\x01",
            "cooking. Monsters also drop them.\x02",
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

    # Function_49_DF6F end

    def Function_50_F06B(): pass

    label("Function_50_F06B")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F229")
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

    def lambda_F15D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F15D)

    def lambda_F16E():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F16E)

    def lambda_F188():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F188)

    def lambda_F199():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F199)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F1D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F1D0)

    def lambda_F1E1():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1E1)
    Sleep(200)

    def lambda_F1FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F1FE)

    def lambda_F20F():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F20F)
    Jump("loc_F4D8")

    label("loc_F229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F383")
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

    def lambda_F2B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F2B7)

    def lambda_F2C8():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F2C8)

    def lambda_F2E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F2E2)

    def lambda_F2F3():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F2F3)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F32A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F32A)

    def lambda_F33B():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F33B)
    Sleep(200)

    def lambda_F358():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F358)

    def lambda_F369():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F369)
    Jump("loc_F4D8")

    label("loc_F383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F4D8")
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

    def lambda_F411():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F411)

    def lambda_F422():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F422)

    def lambda_F43C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F43C)

    def lambda_F44D():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F44D)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F484():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F484)

    def lambda_F495():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F495)
    Sleep(200)

    def lambda_F4B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F4B2)

    def lambda_F4C3():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F4C3)

    label("loc_F4D8")

    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "The Old Dragon Inn... A store\x01",
            "on East Street where Eastern\x01",
            "cuisine is served, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FShould we take a short\x01",
            "break?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmm, I think so. And\x01",
            "just when I was getting\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I want to see just what\x01",
            "kind of food they serve\x01",
            "here.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F73A")
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
    Jump("loc_F841")

    label("loc_F73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F7C0")
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
    Jump("loc_F841")

    label("loc_F7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F841")
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

    label("loc_F841")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#11P#00102FHow do you like the Old\x01",
            "Dragon Inn?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F8F5")

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah, I'd love to hear the\x01",
            "opinion of someone who knows\x01",
            "what the real thing tastes like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9DB")

    label("loc_F8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F96A")

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, I'd love to hear the\x01",
            "opinion of someone who knows\x01",
            "what the real thing tastes like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9DB")

    label("loc_F96A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F9DB")

    ChrTalk(
        0x105,
        (
            "#6P#10302FHehe, I'd love to hear the\x01",
            "opinion of someone who knows\x01",
            "what the real thing tastes like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9DB")

    BeginChrThread(0x1A2, 3, 0, 51)
    Sleep(1000)
    EndChrThread(0x1A2, 0x3)

    ChrTalk(
        0x1A2,
        (
            "#5PRrr― What is the meaning\x01",
            "of this!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PWhy does this store sell this kind\x01",
            "of thing at this kind of price? Is\x01",
            "the owner out of his mind!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FHey now, you shouldn't\x01",
            "use such a loud voice in\x01",
            "a store...\x02",
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
            "#5PFor example this mapo tofu... The\x01",
            "flavor isn't even beat by three-star\x01",
            "restaurants in the Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PFor something this good, the\x01",
            "price should be three times\x01",
            "what it is― Why is it not!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FBEF")

    ChrTalk(
        0x104,
        "#6P#00306FT-That, huh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC68")

    label("loc_FBEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC33")

    ChrTalk(
        0x109,
        (
            "#6P#10106FSo that's what you're\x01",
            "talking about...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC68")

    label("loc_FC33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FC68")

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha, so that's what it\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC68")


    ChrTalk(
        0x1A2,
        (
            "#5PI-I don't believe\x01",
            "this... Why is a store\x01",
            "like this in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha. Well anyway, I'm\x01",
            "glad you're happy.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 1)
    OP_29(0x73, 0x1, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FD4B")
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
    Jump("loc_FDCA")

    label("loc_FD4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FD8D")
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
    Jump("loc_FDCA")

    label("loc_FD8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FDCA")
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

    label("loc_FDCA")

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

    # Function_50_F06B end

    def Function_51_FE05(): pass

    label("Function_51_FE05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FE35")

    def lambda_FE15():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE15)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_51_FE05")

    label("loc_FE35")

    Return()

    # Function_51_FE05 end

    def Function_52_FE36(): pass

    label("Function_52_FE36")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FF59")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_FF9C")

    label("loc_FF59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FF71")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_FF9C")

    label("loc_FF71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FF89")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Jump("loc_FF9C")

    label("loc_FF89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FF9C")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_FF9C")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100CA")

    ChrTalk(
        0x8,
        (
            "Hey, what are you\x01",
            "doing!? It'll burn\x01",
            "again!\x02",
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
        (
            "#00000FUmm, may I have a\x01",
            "moment?\x02",
        )
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
            "As you can see, I'm busy\x01",
            "now. Go to the counter\x01",
            "if you want to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, that's not it. You\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10167")

    label("loc_100CA")

    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "Oh, do you need\x01",
            "something with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Go to the counter if you\x01",
            "want to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10167")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah, that gourmet guide,\x01",
            "huh. I indeed heard\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it can't be helped\x01",
            "that we're busy. Wait at\x01",
            "an empty table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll give you a taste of\x01",
            "my "Peerless Fried\x01",
            "Rice", my pride and joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh. In that case, I'm\x01",
            "looking forward to this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00000FAlright then, we'll have\x01",
            "a seat.\x02",
        )
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
            "Lloyd and the others ate\x01",
            "the Peerless Fried Rice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00204F...It's delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FAh, you really are good,\x01",
            "master.\x02\x03",
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
            "Originally, fried rice was my\x01",
            "specialty... I improved it the other\x01",
            "day and the result wasn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F*chew, chew*, *chew, chew*...\x01",
            "Wow, you're not kidding!\x02\x03",
            "#10103FIt's such a simple dish. To think\x01",
            "it could have such deep flavor!\x02\x03",
            "#10109FI made it in the CGF dorm several\x01",
            "times, but when made by a pro,\x01",
            "it's on a whole other level!\x02",
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
        (
            "#00306FDon't talk with your\x01",
            "mouth full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FAnd don't gulp it down\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        (
            "Hmm, well if you like it\x01",
            "that much, then it was\x01",
            "worth making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I made a lot, so how\x01",
            "about seconds?\x02",
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
            "#00102FHaha, Noｱl... You're\x01",
            "like a growing boy.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A79")
    SetChrPos(0x8, 17080, 0, 15430, 0)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_10A8A")

    label("loc_10A79")

    SetChrPos(0x8, 16000, 0, 15990, 0)

    label("loc_10A8A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_10B37")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_10B54")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_10B67")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_10B7A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_10B97")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_10BAA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_10BC7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_10BDA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_10BF7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_10C0A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_10C27")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10C27")

    OP_29(0x80, 0x1, 0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D32")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10D29")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_10D29")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_10D32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E20")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_10E20")

    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10E40")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_10E83")

    label("loc_10E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10E58")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_10E83")

    label("loc_10E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10E70")
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Jump("loc_10E83")

    label("loc_10E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10E83")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_10E83")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2880, 0, -40, 278)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_FE36 end

    def Function_53_10EAF(): pass

    label("Function_53_10EAF")

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
            "#10300F(I think she'd be great\x01",
            "as a waitress for the\x01",
            "pageant.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She looks down, but...\x01",
            "I'll try asking her.)\x02\x03",
            "#00000FUmm, can I talk to you\x01",
            "for a moment?\x02",
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
            "Asked Shanshan to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
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
            "#00108FIf that's the case, then\x01",
            "you shouldn't force\x01",
            "yourself.\x02",
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
            "#00300FHmm... Still having\x01",
            "trouble with it?\x02",
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
            "I've been depressed, and\x01",
            "it's rubbing off on the\x01",
            "customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The customers aren't\x01",
            "enjoying themselves\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell if you're having\x01",
            "trouble, then why not\x01",
            "try participating?\x02\x03",
            "#10300FIf you think you might\x01",
            "regret it later, it's\x01",
            "better to do it.\x02",
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
        (
            "...Alright, I've\x01",
            "decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll do my best at the\x01",
            "event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whether it's a pageant\x01",
            "or a hot bath, I'll give\x01",
            "it everything I've got!\x02",
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
        "#10106FA hot bath?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FUmm, then you'll do it?\x02",
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
            "There's still time until\x01",
            "the program, so contact\x01",
            "me later, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright. And thanks.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1156B")

    ChrTalk(
        0x101,
        (
            "#00003F─Alright. With this\x01",
            "we've finally filled our\x01",
            "quota.\x02\x03",
            "#00000FLet's head to City\x01",
            "Meeting Hall and report\x01",
            "to Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_1156B")

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

    # Function_53_10EAF end

    def Function_54_115B9(): pass

    label("Function_54_115B9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D48")
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x1F,
        "Baby",
        "Zzzzz... zzzzz...\x02",
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
            "Uhuhu, look at that Alm.\x01",
            "She's fast asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yeah, looks that way,\x01",
            "Aerie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Looking at her sleeping\x01",
            "like this, she's like an\x01",
            "angel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Haha, well the goddess\x01",
            "named Aerie gave birth to\x01",
            "her, so it's only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh Alm...\x02",
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
            "#00003F...U-Umm, I'm terribly\x01",
            "sorry to interrupt,\x01",
            "but...\x02\x03",
            "#00000FAre you Alm?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1186E():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_1186E)
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
            "#00000FCrossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "We saw your request and\x01",
            "came to ask about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Oh, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Thank goodness you've\x01",
            "come!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "That's great, Alm! With\x01",
            "this, we'll finally...\x02",
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
            "just born, things are\x01",
            "really tough for us.\x02",
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
            "The first time we held\x01",
            "her, we both promised,\x01",
            "remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "No matter what\x01",
            "happens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "You, I, and this child\x01",
            "we both love...\x02",
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
        "I do too, Alm!\x02",
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
            "#10106FWow... They sure are\x01",
            "lovey-dovey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FLooks like they've been\x01",
            "sucked into their own\x01",
            "little world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYeah, looks that way.\x02\x03",
            "#00000F...Ahem. Excuse us, but,\x01",
            "can we ask about your\x01",
            "request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh, that's right!\x02",
    )

    CloseMessageWindow()

    def lambda_11CB5():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_11CB5)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        (
            "Umm... We'd like you to\x01",
            "search for a certain\x01",
            "someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Sorry to spring this on\x01",
            "you, but can you accept\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DE8")

    label("loc_11D48")

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
            "Sorry to spring this on\x01",
            "you, but can you accept\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DE8")

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

    # Function_54_115B9 end

    def Function_55_11E38(): pass

    label("Function_55_11E38")

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
            "[Cancel]\x01",      # 1
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
        (0, "loc_11E9A"),
        (1, "loc_11EA2"),
        (SWITCH_DEFAULT, "loc_12040"),
    )


    label("loc_11E9A")

    Call(0, 56)
    Jump("loc_12040")

    label("loc_11EA2")


    ChrTalk(
        0x101,
        (
            "#00006FUmm... sorry. We can't\x01",
            "do it right away...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FF0")

    ChrTalk(
        0x1E,
        (
            "N-No way... You're the\x01",
            "only ones we can count\x01",
            "on!\x02",
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
        "Ehh, ehh...\x02",
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
            "Yeah, please do. We'll\x01",
            "be waiting here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12038")

    label("loc_11FF0")


    ChrTalk(
        0x1E,
        "N-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Alright then. Get free\x01",
            "and return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Please...\x02",
    )

    CloseMessageWindow()

    label("loc_12038")

    SetScenarioFlags(0x19A, 5)
    Jump("loc_12040")

    label("loc_12040")

    Return()

    # Function_55_11E38 end

    def Function_56_12041(): pass

    label("Function_56_12041")


    ChrTalk(
        0x101,
        (
            "#00000FYes, understood. Please\x01",
            "leave it to us.\x02",
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
            "Man~, I'm saved! I'm\x01",
            "really in a bind here,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "That's great, Alm! I'm\x01",
            "so happy!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1F,
        "Baby",
        "Goo goo.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        (
            "Uh, Aerie? I think\x01",
            "Almin's happy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I think you're right,\x01",
            "Alm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...The request details,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1218A():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_1218A)
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
            "Ahem, excuse us. I'll\x01",
            "explain it right away.\x02",
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
            "#00206F(At that rate, it'd\x01",
            "never be over no matter\x01",
            "how long we waited.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Haha... I wanted to\x01",
            "watch a while longer,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Ahem, the one I want you\x01",
            "to search for is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "My father, from whom I\x01",
            "was separated when I was\x01",
            "very young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FA lifelong separation...\x01",
            "you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yeah. We live in Liberl\x01",
            "Kingdom, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I actually lived here in\x01",
            "Crossbell when I was\x01",
            "little.\x02",
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
            "A few days ago, this\x01",
            "child was born out of\x01",
            "our love for each other.\x02",
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
            "He might hate my mom,\x01",
            "but to me, he's my real\x01",
            "dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'd like to tell him\x01",
            "about the happy life\x01",
            "we've built as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "And, I persuaded my mom\x01",
            "and decided to come to\x01",
            "Crossbell.\x02",
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
            "He should have a Residental\x01",
            "Street mansion, but he's\x01",
            "completely disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I hear from my mom all the\x01",
            "time, but I haven't heard from\x01",
            "dad ever since the divorce...\x02",
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
            "Alm and I have asked\x01",
            "around at a lot of\x01",
            "different places.\x02",
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
            "#10105FCould it be that he's on\x01",
            "vacation every time we\x01",
            "stop by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, I don't know, but...\x02\x03",
            "#00000FWe have a lot of experience\x01",
            "with both Residential Street\x01",
            "and Downtown.\x02\x03",
            "Elie, do you have any ideas\x01",
            "about someone like that\x01",
            "living in Residential Street?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1E, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FHmm. I don't think so,\x01",
            "but...\x02\x03",
            "#00100FAlm, do you remember\x01",
            "your father's name and\x01",
            "occupation?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "Hmm. I asked my mom about\x01",
            "it, but I don't know if he\x01",
            "still does the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I know his name. He's\x01",
            "Geval, one of the city's\x01",
            "congressmen.\x02",
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
        "#00005FCongressman Geval!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, him.\x02",
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
            "#00103FYes. We ran into him\x01",
            "during a request not too\x01",
            "long ago.\x02\x03",
            "#00100FIn any case, I think we\x01",
            "should pay a visit to\x01",
            "his Downtown apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, exactly.\x02\x03",
            "#00000FWe might learn something\x01",
            "about why he's never\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm sure it's fate that\x01",
            "you've accepted our\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'll leave everything to\x01",
            "you! Please, find my\x01",
            "dad!\x02",
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
        (
            "#00000FYes, please leave it to\x01",
            "us.\x02",
        )
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
            "Quest [Search for Long\x01",
            "Lost Father]\x07\x00",
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

    # Function_56_12041 end

    SaveToFile()

Try(main)
