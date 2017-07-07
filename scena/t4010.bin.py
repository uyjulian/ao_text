from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4010.bin",                # FileName
        "t4010",                    # MapName
        "t4010",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 7, 0, 8],
    )

    BuildStringList((
        "t4010",                  # 0
        "Sister Marble",     # 1
        "Archbishop Ellarda",         # 2
        "Sister · Lease",       # 3
        "Jeanas Priest",           # 4
        "Priest Renton",           # 5
        "Sister Hatina",     # 6
        "Trading business morgio",         # 7
        "Sister Juzy",     # 8
        "Leyte",                 # 9
        "Keya",                 # 10
        "Ryu",                 # 11
        "Henry",                 # 12
        "peach",                   # 13
        "Pance",                 # 14
        "Tamil",                 # 15
        "Hamill",                 # 16
        "Kuta",                 # 17
        "Yuggott",               # 18
        "boy",                 # 19
        "boy",                 # 20
        "girl",                 # 21
        "girl",                 # 22
        "Pruna",               # 23
        "Linally",               # 24
        "Brick",               # 25
        "Adolescents",                   # 26
        "Daughter",                     # 27
        "doll",                   # 28
    ))

    AddCharChip((
        "chr/ch25500.itc",                   # 00
        "chr/ch26500.itc",                   # 01
        "chr/ch14000.itc",                   # 02
        "chr/ch23802.itc",                   # 03
        "chr/ch25400.itc",                   # 04
        "chr/ch25300.itc",                   # 05
        "chr/ch21802.itc",                   # 06
        "chr/ch22202.itc",                   # 07
        "chr/ch20602.itc",                   # 08
        "chr/ch20702.itc",                   # 09
        "chr/ch22302.itc",                   # 0A
        "chr/ch21402.itc",                   # 0B
        "chr/ch34202.itc",                   # 0C
        "chr/ch20602.itc",                   # 0D
        "chr/ch23802.itc",                   # 0E
        "chr/ch21502.itc",                   # 0F
        "chr/ch23902.itc",                   # 10
        "chr/ch20502.itc",                   # 11
        "chr/ch22102.itc",                   # 12
        "chr/ch20402.itc",                   # 13
        "chr/ch22802.itc",                   # 14
        "chr/ch21302.itc",                   # 15
        "chr/ch08202.itc",                   # 16
        "chr/ch20500.itc",                   # 17
        "chr/ch22100.itc",                   # 18
        "chr/ch26502.itc",                   # 19
        "chr/ch21800.itc",                   # 1A
        "chr/ch10300.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(150800,  200,     17500,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294967087, 379,     23229,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294964336, 250,     20010,   180,  257,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(99300,   0,       5679,    225,  257,  0x0, 0,   5,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(2950,    189,     19709,   165,  257,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294963447, 150,     6519,    0,    325,  0x0, 0,   26,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       180,  385,  0x0, 0,   0,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(1059,    0,       11659,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   22,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(153619,  150,     12229,   0,    453,  0x0, 0,   8,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   7,   0,   255, 255, 0,   30,  255,  0)
    DeclNpc(154929,  150,     9130,    0,    453,  0x0, 0,   9,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   10,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(148490,  150,     12229,   45,   453,  0x0, 0,   3,   0,   255, 255, 0,   33,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   3,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(147139,  150,     9130,    0,    453,  0x0, 0,   12,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   13,  0,   255, 255, 0,   37,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    453,  0x0, 0,   14,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   15,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(148490,  150,     6150,    0,    453,  0x0, 0,   16,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   23,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   24,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   19,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   20,  0,   255, 255, 0,   45,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   21,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(150910,  200,     16530,   1200,    150800,  1700,    17500,   0x007E, 0,  22, 0x0000)
    DeclActor(40,      500,     21930,   1200,    4294967086, 2100,    23230,   0x007E, 0,  9,  0x0000)
    DeclActor(50280,   0,       12800,   1200,    50160,   1000,    13560,   0x007C, 0,  48, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_64B",          # 02, 2
        "Function_3_676",          # 03, 3
        "Function_4_6A1",          # 04, 4
        "Function_5_6CC",          # 05, 5
        "Function_6_6F7",          # 06, 6
        "Function_7_848",          # 07, 7
        "Function_8_F0D",          # 08, 8
        "Function_9_1118",         # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_2BCE",        # 0B, 11
        "Function_12_2CD2",        # 0C, 12
        "Function_13_307B",        # 0D, 13
        "Function_14_3195",        # 0E, 14
        "Function_15_3323",        # 0F, 15
        "Function_16_4617",        # 10, 16
        "Function_17_5A3D",        # 11, 17
        "Function_18_6A22",        # 12, 18
        "Function_19_801B",        # 13, 19
        "Function_20_8ABF",        # 14, 20
        "Function_21_8ED1",        # 15, 21
        "Function_22_90D6",        # 16, 22
        "Function_23_9105",        # 17, 23
        "Function_24_AE71",        # 18, 24
        "Function_25_B49E",        # 19, 25
        "Function_26_B608",        # 1A, 26
        "Function_27_BC37",        # 1B, 27
        "Function_28_BD3F",        # 1C, 28
        "Function_29_BDCC",        # 1D, 29
        "Function_30_BEEF",        # 1E, 30
        "Function_31_C000",        # 1F, 31
        "Function_32_C124",        # 20, 32
        "Function_33_C427",        # 21, 33
        "Function_34_C5FB",        # 22, 34
        "Function_35_C7A6",        # 23, 35
        "Function_36_C877",        # 24, 36
        "Function_37_C8EA",        # 25, 37
        "Function_38_C927",        # 26, 38
        "Function_39_C99A",        # 27, 39
        "Function_40_CAB0",        # 28, 40
        "Function_41_CB1A",        # 29, 41
        "Function_42_CBD4",        # 2A, 42
        "Function_43_CD03",        # 2B, 43
        "Function_44_CD73",        # 2C, 44
        "Function_45_CE58",        # 2D, 45
        "Function_46_CEAE",        # 2E, 46
        "Function_47_CFF7",        # 2F, 47
        "Function_48_D366",        # 30, 48
        "Function_49_D415",        # 31, 49
        "Function_50_D912",        # 32, 50
        "Function_51_DBE9",        # 33, 51
        "Function_52_EF84",        # 34, 52
        "Function_53_F804",        # 35, 53
        "Function_54_10D89",       # 36, 54
        "Function_55_10F9D",       # 37, 55
        "Function_56_112A4",       # 38, 56
        "Function_57_11E20",       # 39, 57
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64A")
    OP_94(0xFE, 0x17A8E, 0x125C, 0x186A0, 0x1D4C, 0x3E8)
    Sleep(450)
    Jump("Function_1_620")

    label("loc_64A")

    Return()

    # Function_1_620 end

    def Function_2_64B(): pass

    label("Function_2_64B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_675")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_2_64B")

    label("loc_675")

    Return()

    # Function_2_64B end

    def Function_3_676(): pass

    label("Function_3_676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_94(0xFE, 0xBA5E, 0x319C, 0xCD46, 0xC44, 0x3E8)
    Sleep(450)
    Jump("Function_3_676")

    label("loc_6A0")

    Return()

    # Function_3_676 end

    def Function_4_6A1(): pass

    label("Function_4_6A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CB")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_4_6A1")

    label("loc_6CB")

    Return()

    # Function_4_6A1 end

    def Function_5_6CC(): pass

    label("Function_5_6CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F6")
    OP_94(0xFE, 0x24A7C, 0x17DE, 0x25170, 0x34F8, 0x3E8)
    Sleep(450)
    Jump("Function_5_6CC")

    label("loc_6F6")

    Return()

    # Function_5_6CC end

    def Function_6_6F7(): pass

    label("Function_6_6F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 1560, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 10730, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    Jump("Function_6_6F7")

    label("loc_847")

    Return()

    # Function_6_6F7 end

    def Function_7_848(): pass

    label("Function_7_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_876")
    Jump("loc_F0C")

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8A0")
    ClearChrFlags(0xE, 0x40)
    SetChrPos(0xE, 160, 0, 10850, 0)
    BeginChrThread(0xE, 0, 0, 4)
    Jump("loc_F0C")

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_F0C")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -6960, 0, 20030, 135)

    label("loc_8DF")

    SetChrPos(0x8, 8480, 0, 19550, 225)
    SetChrPos(0x16, 5350, 150, 11500, 0)
    SetChrPos(0x17, 6400, 150, 11500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    Jump("loc_F0C")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_956")
    Jump("loc_F0C")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9A1")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 48280, 0, 10730, 180)
    BeginChrThread(0xF, 0, 0, 6)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 151520, 0, 9530, 0)
    BeginChrThread(0xA, 0, 0, 5)
    Jump("loc_F0C")

    label("loc_9A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9CB")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xC, 95850, 0, 8119, 270)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_F0C")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EC")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E7")
    SetChrFlags(0xE, 0x10)

    label("loc_9E7")

    Jump("loc_F0C")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_AD0")
    SetChrPos(0x9, 100000, 150, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xF, 153000, 200, 17650, 270)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69")
    SetChrFlags(0xF, 0x10)

    label("loc_A69")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrPos(0x1E, 155440, 0, 3630, 270)
    SetChrPos(0x1F, 153430, 0, 3820, 90)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    ClearChrFlags(0x1E, 0x40)
    ClearChrFlags(0x1F, 0x40)
    Jump("loc_F0C")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_BAB")
    SetChrPos(0x9, 97640, 0, 12650, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 153790, 200, 17470, 180)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    Jump("loc_F0C")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CA0")
    SetChrPos(0xC, 49920, 0, 9850, 359)
    BeginChrThread(0xC, 0, 0, 3)
    SetChrPos(0x9, 97640, 0, 12650, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEB")
    SetChrFlags(0x9, 0x10)

    label("loc_BEB")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 150800, 200, 17500, 180)
    SetChrPos(0x8, 153790, 200, 17470, 180)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x18, 0xB)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrChipByIndex(0x19, 0xC)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0xD)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0xE)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1C, 0xF)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1D, 0x10)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jump("loc_F0C")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CEB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE6")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)

    label("loc_CE6")

    Jump("loc_F0C")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D25")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D20")
    SetChrFlags(0xD, 0x10)

    label("loc_D20")

    Jump("loc_F0C")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D33")
    Jump("loc_F0C")

    label("loc_D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xD, 0x10)

    label("loc_D68")

    SetChrPos(0xB, 160, 0, 10850, 0)
    BeginChrThread(0xB, 0, 0, 4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -1000, 0, 7830, 270)
    BeginChrThread(0xF, 0, 0, 4)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD1")
    SetChrFlags(0x8, 0x10)

    label("loc_DD1")

    SetChrFlags(0xA, 0x10)
    Jump("loc_F0C")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF3")
    SetChrFlags(0x9, 0x10)

    label("loc_DF3")

    Jump("loc_F0C")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_E55")
    SetChrPos(0x9, 100000, 150, 10610, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 100000, 0, 7200, 0)
    SetChrPos(0xC, 50430, 0, 4030, 0)
    BeginChrThread(0xC, 0, 0, 3)
    Jump("loc_F0C")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F0C")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x7)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x9)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xA)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F07")
    SetChrFlags(0x13, 0x10)

    label("loc_F07")

    SetChrFlags(0x14, 0x10)

    label("loc_F0C")

    Return()

    # Function_7_848 end

    def Function_8_F0D(): pass

    label("Function_8_F0D")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2F")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jump("loc_1036")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F4B")
    Jump("loc_1036")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F59")
    Jump("loc_1036")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F67")
    Jump("loc_1036")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F75")
    Jump("loc_1036")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F83")
    Jump("loc_1036")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F91")
    Jump("loc_1036")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F9F")
    Jump("loc_1036")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_FB1")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_FC3")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FD5")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FE3")
    Jump("loc_1036")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_1036")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FFF")
    Jump("loc_1036")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_100D")
    Jump("loc_1036")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_101B")
    Jump("loc_1036")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_102D")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1036")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1048")
    OP_65(0x0, 0x1)

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1064")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_107B")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_107B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10CD")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_18", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_27", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_10DE")

    label("loc_10CD")

    SetMapObjFrame(0xFF, "cloudwind", 0x0, 0x1)

    label("loc_10DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F1")
    OP_1B(0x2, 0x0, 0x33)

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")
    OP_1B(0x2, 0x0, 0x34)

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1117")
    OP_1B(0x4, 0x0, 0x35)

    label("loc_1117")

    Return()

    # Function_8_F0D end

    def Function_9_1118(): pass

    label("Function_9_1118")

    Call(0, 10)
    Return()

    # Function_9_1118 end

    def Function_10_111C(): pass

    label("Function_10_111C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_114A")
    Call(0, 12)
    Jump("loc_114D")

    label("loc_114A")

    Call(0, 11)

    label("loc_114D")

    Jump("loc_13EA")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133F")

    ChrTalk(
        0x9,
        (
            "\"Taiki\" that appeared in the wetland … …\x01",
            "That kind of thing is for the Seven Yigh Church\x01",
            "Which scripture is transmitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It will be managed somehow by the hands of secularists\x01",
            "It may not be something of a kind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1306")

    ChrTalk(
        0x105,
        (
            "#10400FWell, for us for the time being\x01",
            "I will leave it to you.\x02\x03",
            "#10404FAs soon as the situation is resolved,\x01",
            "By all means for future cooperation\x01",
            "I'd like to ask for a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Let me think positively.\x01",
            "If it is for crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Alright, the goddess's protection did not happen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1337")

    label("loc_1306")


    ChrTalk(
        0x9,
        (
            "…… Oldly,\x01",
            "The goddess's protection is unlikely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1337")

    SetScenarioFlags(0x0, 0)
    Jump("loc_13EA")

    label("loc_133F")


    ChrTalk(
        0x9,
        (
            "That \"Taiki\", the Seven Yigh Society's\x01",
            "Which scripture is transmitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It will be managed somehow by the hands of secularists\x01",
            "It may not be something of a kind … …\x01",
            "Let's pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EA")

    Jump("loc_2BCA")

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141A")
    Call(0, 12)
    Jump("loc_141D")

    label("loc_141A")

    Call(0, 11)

    label("loc_141D")

    Jump("loc_15B4")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(
        0x9,
        (
            "The situation of the crossbell of this time …\x01",
            "He continued to refuse to intervene in the \"Seaplastic Province\"\x01",
            "I also have a cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If they only accept them,\x01",
            "To this point\x01",
            "Perhaps it was not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also cooled my head\x01",
            "Time to look back on yourself\x01",
            "It seems necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B4")

    label("loc_151E")


    ChrTalk(
        0x9,
        (
            "If you are accepting the \"Seiyo Shrine\"\x01",
            "To this point\x01",
            "Perhaps it was not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also cooled my head\x01",
            "Time to look back on yourself\x01",
            "It seems necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B4")

    Jump("loc_2BCA")

    label("loc_15B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F6")

    ChrTalk(
        0x9,
        (
            "Sister · Leaseが\x01",
            "Have you returned to the Alteria head office …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… To the intervention in the crossbell,\x01",
            "It seems that the Ministry of Construction has started to move in earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To this era of crisis crossbells\x01",
            "I'm about to rush …\x01",
            "It may be a sign of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As I am also the head of the Crossbell parish,\x01",
            "How to shake your future\x01",
            "You seem to have to think about it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179E")

    label("loc_16F6")


    ChrTalk(
        0x9,
        (
            "The Ministry of Construction began full swing,\x01",
            "To this era of crisis crossbells\x01",
            "I'm about to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As I am also the head of the Crossbell parish,\x01",
            "How to shake your future\x01",
            "You seem to have to think about it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179E")

    Jump("loc_2BCA")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(
        0x9,
        (
            "… …. A while ago, from the Liturgy Ministry\x01",
            "The information has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cross Bell intervention of the Ministry of Construction\x01",
            "It is said that the pope himself will be admitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A raid incident or the like is happening\x01",
            "It may be useless in the current situation ……\x02",
        )
    )


    ChrTalk(
        0x9,
        (
            "But even so … …\x01",
            "They do illegal activities,\x01",
            "I can not admit it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197C")

    label("loc_18CC")


    ChrTalk(
        0x9,
        (
            "Cross Bell intervention of the Ministry of Construction\x01",
            "It is said that the pope himself is likely to approve\x01",
            "Although information is contained ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But even so … …\x01",
            "They do illegal activities,\x01",
            "I can not admit it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197C")

    Jump("loc_2BCA")

    label("loc_1981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3C")

    ChrTalk(
        0x9,
        (
            "Even now, at Mainz Mountain Road\x01",
            "Many security guards are in danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Great goddess of the sky,\x01",
            "Please help them …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And reject evil things … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A97")

    label("loc_1A3C")


    ChrTalk(
        0x9,
        (
            "Great goddess of the sky,\x01",
            "Please help them …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And reject evil things … …\x02",
    )

    CloseMessageWindow()

    label("loc_1A97")

    Jump("loc_2BCA")

    label("loc_1A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4D")

    ChrTalk(
        0x9,
        (
            "Even though the hushman came to ask,\x01",
            "It seems that Eolia you guys are missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Unfortunately it has not come to the cathedral.\x01",
            "Hmm, I wish I was safe … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BBF")

    label("loc_1B4D")


    ChrTalk(
        0x9,
        (
            "To Aioria you guys,\x01",
            "Materials procurement of drugs and escorts of priests,\x01",
            "I am taken care of in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope it is safe … …\x02",
    )

    CloseMessageWindow()

    label("loc_1BBF")

    Jump("loc_2BCA")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C65")

    ChrTalk(
        0x9,
        (
            "Now……\x01",
            "I have to schedule the schedule for the next mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The incident continued from the previous case incident ……\x01",
            "Citizens participate in the mass,\x01",
            "I have to make my heart peaceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCA")

    label("loc_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D21")

    ChrTalk(
        0x9,
        (
            "…… The matter of yesterday's flower,\x01",
            "Are you still sniffing around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On this broad continent,\x01",
            "There is a better world to touch\x01",
            "It is often present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "… … It's not too much deepening.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D9C")

    label("loc_1D21")


    ChrTalk(
        0x9,
        (
            "On this broad continent,\x01",
            "There is a better world to touch\x01",
            "It is often present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do not get too deeply,\x01",
            "Keep in mind the liver.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9C")

    Jump("loc_2BCA")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_202E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F54")

    ChrTalk(
        0x9,
        (
            "About this flower from me\x01",
            "There is nothing to talk about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Other people in the church ……\x01",
            "例えばSister Marbleでも\x01",
            "I do not know its existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let's take over from now.\x01",
            "I am too busy something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(After all, the Archbishop\x01",
            "I will not tell you … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Mr. Lease says there's a story\x01",
            "I was saying that … ….\x01",
            "Let's go over there once. )\x02\x03",
            "(She got out of the chapel immediately\x01",
            "You should be waiting at the dormitory. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2029")

    label("loc_1F54")


    ChrTalk(
        0x9,
        (
            "About this flower from me\x01",
            "There is nothing to talk about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let's take over from now.\x01",
            "I am too busy something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(As soon as Leith left the chapel\x01",
            "You should be waiting at the dormitory ……\x01",
            "Anyway, let's go. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2029")

    Jump("loc_2BCA")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20EE")

    ChrTalk(
        0x9,
        (
            "Lease Argento …\x01",
            "After all, her sister will make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm … that guy.\x01",
            "What on earth are you planning …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(It seems they are thinking something ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_211D")

    label("loc_20EE")


    ChrTalk(
        0x9,
        (
            "… … those guys.\x01",
            "What on earth are you planning …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211D")

    Jump("loc_2BCA")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2223")

    ChrTalk(
        0x9,
        (
            "On the day of the plenary session of the Trade Council ……\x01",
            "Sister · Leaseのマインツへの出張が\x01",
            "It took a long time to burn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And in the direction of Mainz\x01",
            "It should have had ruins of example ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……got it.\x01",
            "I do not know what I was doing ……\x01",
            "After all, it seems not to be wrong.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2284")

    label("loc_2223")


    ChrTalk(
        0x9,
        "…… Oh, what are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now I am doing research.\x01",
            "Let's get into the room lightly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2284")

    Jump("loc_2BCA")

    label("loc_2289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2579")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C5")
    Call(0, 57)
    Return()

    label("loc_22C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C1")

    ChrTalk(
        0x9,
        (
            "Kaitou B … … No way sacred\x01",
            "What is hiding stolen goods in Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was listening to the story\x01",
            "It seems to be a considerably unreasonable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The servant of the great goddess#2Ra servant man#As,\x01",
            "Please forgive such things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys, whatever\x01",
            "Please catch it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2434")

    label("loc_23C1")


    ChrTalk(
        0x9,
        (
            "Kaito B ……\x01",
            "As a servant of a great goddess,\x01",
            "Please forgive such things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys, whatever\x01",
            "Please catch it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2434")

    TalkEnd(0x9)
    Return()

    label("loc_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F3")

    ChrTalk(
        0x9,
        (
            "Claudia the first time ago\x01",
            "I was in a greeting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Young and pretty refined\x01",
            "It seems to have an idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of the Libert Kingdom\x01",
            "You can say that it is bright.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2574")

    label("loc_24F3")


    ChrTalk(
        0x9,
        (
            "Claudia Queen,\x01",
            "Young and pretty refined\x01",
            "It seems to have an idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of the Libert Kingdom\x01",
            "You can say that it is bright.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2574")

    Jump("loc_2BCA")

    label("loc_2579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2623")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2594")
    Call(0, 14)
    Jump("loc_261E")

    label("loc_2594")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "It's a business trip to Mainz ……\x01",
            "Somewhat worrisome, it will be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "About her\x01",
            "Please report anything again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Is that … Yes.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_261E")

    Jump("loc_2BCA")

    label("loc_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2716")

    ChrTalk(
        0x9,
        (
            "Professor Lago from Ursula Hospital\x01",
            "A letter has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I gave you lupine grass before\x01",
            "The results of research using herbs … …\x01",
            "It seems that it was written that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I am not aware of it,\x01",
            "Let me just say I did well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27AB")

    label("loc_2716")


    ChrTalk(
        0x9,
        (
            "Professor Lago of Ursula Hospital,\x01",
            "About the research that cooperated before\x01",
            "A report came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I am not aware of it,\x01",
            "Let me just say I did well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AB")

    Jump("loc_2BCA")

    label("loc_27B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CB")
    Call(0, 13)
    Jump("loc_2868")

    label("loc_27CB")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "Lease Argento ……\x01",
            "Well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sister Hatina。\x01",
            "Work hard on her\x01",
            "Tell me please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, please leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_2868")

    Jump("loc_2BCA")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AE")

    ChrTalk(
        0x9,
        (
            "……Lease Argento …\x01",
            "あのDaughterは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x153,
        "#01111FDaigashi-san, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FLease is said\x01",
            "It is Sister of a little while ago.\x02\x03",
            "#10304FHuh, is there something to worry about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "… … It is a story that you have nothing to do with you.\x01",
            "Please do not mind.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A5B")

    label("loc_29AE")


    ChrTalk(
        0x9,
        (
            "……Lease Argento …\x01",
            "あのDaughterは……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FPlease tell me if you are tummy.\x01",
            "Keya、救急箱とってくるからー！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x153, 500)

    ChrTalk(
        0x9,
        (
            "Well, yes.\x01",
            "……Please do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5B")

    Jump("loc_2BCA")

    label("loc_2A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2A6E")
    Jump("loc_2BCA")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B43")

    ChrTalk(
        0x9,
        (
            "In this Cross Bell Cathedral\x01",
            "You came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To those who seek salvation with a devout heart,\x01",
            "The goddess of the sky#8REarth#I will definitely reach out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I guess you guidance of the goddess … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BCA")

    label("loc_2B43")


    ChrTalk(
        0x9,
        (
            "To those who seek salvation with a devout heart,\x01",
            "The goddess of the sky#8REarth#I will definitely reach out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I guess you guidance of the goddess … …\x02",
    )

    CloseMessageWindow()

    label("loc_2BCA")

    TalkEnd(0x9)
    Return()

    # Function_10_111C end

    def Function_11_2BCE(): pass

    label("Function_11_2BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C76")

    ChrTalk(
        0x9,
        (
            "…… No way No way\x01",
            "What is causing it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This also refused to intervene \"them\"\x01",
            "It may be my responsibility … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CD1")

    label("loc_2C76")


    ChrTalk(
        0x9,
        (
            "This also refused to intervene \"them\"\x01",
            "It may be my responsibility … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2CD1")

    Return()

    # Function_11_2BCE end

    def Function_12_2CD2(): pass

    label("Function_12_2CD2")

    TurnDirection(0x9, 0x105, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Otaku is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400Fやあ、Archbishop Ellarda。\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… That's it.\x01",
            "Wadi Hemisphere,\x01",
            "Naka is still …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sister · Leaseを隠れ蓑に、\x01",
            "This eyes of me\x01",
            "That is why it was devastated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… It seems to be the idea of \"Seiyo Shrine\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FAbout Huff, that matter\x01",
            "I will apologize again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Regarding this matter,\x01",
            "I kept refusingly refusing the intervention of a new naked eye\x01",
            "I also have a cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Conclude and apologize\x01",
            "There is no obligation to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FArchbishop … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FIt is a tough person as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FWell, considering your position\x01",
            "I think it's unbelievable.\x02\x03",
            "#10400FHuff, in the future we will work\x01",
            "Just a little eye closure\x01",
            "I am glad if you do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FHey, well … Waa …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FThe request is too blatant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I can not answer in two turns.\x01",
            "But let me consider again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "このI also cooled my head\x01",
            "Time to look back on yourself\x01",
            "It seems necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 1)
    Return()

    # Function_12_2CD2 end

    def Function_13_307B(): pass

    label("Function_13_307B")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "……彼女はSister Marbleの\x01",
            "You seem to be helping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Sister · Leaseですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, she is very\x01",
            "It is early to memorize the job ……\x01",
            "We have been helped a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "(… … Well, OK.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_13_307B end

    def Function_14_3195(): pass

    label("Function_14_3195")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "HM……\x01",
            "Sister · Leaseに\x01",
            "Have you leave a business trip tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, classes at Sunday school too\x01",
            "It seems that it is not the first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, the Archbishop.\x01",
            "Sister · Leaseが何か……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "From this point on very much\x01",
            "You seem to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… No, it's not a big deal.\x01",
            "Just a while, for the first time in a while\x01",
            "It is worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "About her\x01",
            "Please report anything again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Is that … Yes.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_14_3195 end

    def Function_15_3323(): pass

    label("Function_15_3323")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E6")

    ChrTalk(
        0xFE,
        (
            "Although the president was detained,\x01",
            "The circumstances surrounding the crossbell are\x01",
            "You will never be optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The day when this land is involved in the battle again\x01",
            "It may not be far …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3458")

    label("loc_33E6")


    ChrTalk(
        0xFE,
        (
            "This crossbell is\x01",
            "Again on the day of getting involved in the battle,\x01",
            "It may not be so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's pray, to the goddess … …\x02",
    )

    CloseMessageWindow()

    label("loc_3458")

    Jump("loc_4613")

    label("loc_345D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(
        0xFE,
        (
            "The Archbishop\x01",
            "A lot of responsibility\x01",
            "It seems to be feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For yourself\x01",
            "Because it is a strict one,\x01",
            "There is no impossibility, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as it is, we\x01",
            "Lead as usual\x01",
            "I would like to have it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35BE")

    label("loc_353C")


    ChrTalk(
        0xFE,
        (
            "The Archbishop\x01",
            "I feel a lot of responsibility\x01",
            "It looks like … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still,\x01",
            "Archbishop Ellardaに\x01",
            "I am willing to follow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BE")

    Jump("loc_4613")

    label("loc_35C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BC")

    ChrTalk(
        0xFE,
        (
            "Crossbell's national independence,\x01",
            "Great ripples in neighboring countries\x01",
            "It should spread out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially from the two major countries\x01",
            "From now on, even stronger pressure\x01",
            "It should have taken … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We, the people of Crossbell,\x01",
            "It will be better to survive it\x01",
            "Can we do it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_374E")

    label("loc_36BC")


    ChrTalk(
        0xFE,
        (
            "From now, from two major countries\x01",
            "Further strong pressure\x01",
            "It is supposed to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We, the people of Crossbell,\x01",
            "It will be better to survive it\x01",
            "Can we do it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374E")

    Jump("loc_4613")

    label("loc_3753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3836")

    ChrTalk(
        0xFE,
        (
            "In the previous attacks,\x01",
            "To the guard and the general public\x01",
            "Many damages came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A similar incident again\x01",
            "In order not to wake me up,\x01",
            "What shall I do …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell residents\x01",
            "If we do not think about it\x01",
            "I guess it will not be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38BC")

    label("loc_3836")


    ChrTalk(
        0xFE,
        (
            "A similar incident again\x01",
            "In order not to wake me up,\x01",
            "What shall I do …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell residents\x01",
            "If we do not think about it\x01",
            "I guess it will not be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BC")

    Jump("loc_4613")

    label("loc_38C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_394A")

    ChrTalk(
        0xFE,
        (
            "Residents of Mainz\x01",
            "What on earth have you done … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a job … …\x01",
            "Absolutely forgiving the goddess\x01",
            "It can not be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_394A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39CE")

    ChrTalk(
        0xFE,
        (
            "On the West Crossbell Highway I woke up yesterday\x01",
            "The derailment accident was such a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The dead did not come out\x01",
            "I was fortunate to be unhappy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A99")

    ChrTalk(
        0xFE,
        (
            "Trying to be correct at any time …\x01",
            "That is not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only to others, but also tough\x01",
            "律することができるArchbishop Ellardaは、\x01",
            "He is the most respected person for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B3C")

    ChrTalk(
        0xFE,
        (
            "The Archbishop is the commandment of the Seven Yigh Church\x01",
            "It is very strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although some people are obstinate,\x01",
            "I would rather say that to the archbishop\x01",
            "I respect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3BBF")

    ChrTalk(
        0xFE,
        (
            "Oh, the archbishop is no longer\x01",
            "Were you spoken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "HM……\x01",
            "It seems that it was cut up soon,\x01",
            "Did it happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3C57")

    ChrTalk(
        0xFE,
        (
            "These days, crossbells all over\x01",
            "Something like a mysterious thing is being witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was also a notice from the guard,\x01",
            "I would like to call attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_3C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1E")

    ChrTalk(
        0xFE,
        (
            "If you are an archbishop, now you are in the office\x01",
            "I am staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, Lease's\x01",
            "Recent actions here\x01",
            "It looks like I am investigating ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop and lease … …\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D55")

    label("loc_3D1E")


    ChrTalk(
        0xFE,
        (
            "If you are an archbishop, now you are in the office\x01",
            "I will keep you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D55")

    Jump("loc_4613")

    label("loc_3D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E38")

    ChrTalk(
        0xFE,
        (
            "High Priest Claudia,\x01",
            "It seems there is something like a sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that he was directed directly to Associate Yulia,\x01",
            "You have quite a good arm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it like saying this,\x01",
            "People do not depend on their appearance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EB6")

    label("loc_3E38")


    ChrTalk(
        0xFE,
        (
            "High Priest Claudia,\x01",
            "It seems there is something like a sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it like saying this,\x01",
            "People do not depend on their appearance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB6")

    Jump("loc_4613")

    label("loc_3EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA5")

    ChrTalk(
        0xFE,
        (
            "The future of the trade meeting\x01",
            "I am also anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The leaders of each country,\x01",
            "Each is a famous expert\x01",
            "Welcome you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of arrangements will be made,\x01",
            "As residents of Crossbell\x01",
            "I can not miss it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402E")

    label("loc_3FA5")


    ChrTalk(
        0xFE,
        (
            "The future of the trade meeting\x01",
            "I am also anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of arrangements will be made,\x01",
            "As residents of Crossbell\x01",
            "I can not miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402E")

    Jump("loc_4613")

    label("loc_4033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_418C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_411F")

    ChrTalk(
        0xFE,
        (
            "Archbishop and Professor Lago\x01",
            "There was a strong feud … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently it is a bit relieved,\x01",
            "Professor's letter is\x01",
            "You can now read it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the time I was throwing away without reading\x01",
            "The relationship has also improved considerably\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4187")

    label("loc_411F")


    ChrTalk(
        0xFE,
        (
            "Originally Professor Lago\x01",
            "A priest who studied under the archbishop … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among them, the feud between two people\x01",
            "I hope it will disappear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4187")

    Jump("loc_4613")

    label("loc_418C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4229")

    ChrTalk(
        0xFE,
        (
            "Today I'm free\x01",
            "I am cleaning the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is an old building … ….\x01",
            "I have to clean it regularly\x01",
            "Because it hurts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4613")

    label("loc_4229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_43CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431E")

    ChrTalk(
        0xFE,
        (
            "For senior class lessons,\x01",
            "More than younger classes\x01",
            "It should be getting harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keyaちゃんの理解力は\x01",
            "There are wonderful things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FErr …\x01",
            "I was praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, somehow I also have a high nose.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C6")

    label("loc_431E")


    ChrTalk(
        0xFE,
        (
            "Keyaちゃんは、ともすれば\x01",
            "Problems that even adults would consider\x01",
            "I will understand Sararito … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even without watching classes,\x01",
            "Just listening to that story\x01",
            "It's awesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C6")

    Jump("loc_4613")

    label("loc_43CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A7")

    ChrTalk(
        0xFE,
        (
            "Archbishop Ellardaは、\x01",
            "新しく来たSister · Leaseと\x01",
            "It seems they are visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I heard her name,\x01",
            "Archbishop was a little surprised\x01",
            "It seems like ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, well-known people\x01",
            "Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_451C")

    label("loc_44A7")


    ChrTalk(
        0xFE,
        (
            "Sister · Leaseの名前に、\x01",
            "Archbishop was a little surprised\x01",
            "It seems like ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, well-known people\x01",
            "Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451C")

    Jump("loc_4613")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")

    ChrTalk(
        0xFE,
        (
            "Regularly in the cathedral\x01",
            "Mass is being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Masses bear the goddess of the sky\x01",
            "Holy celebrations ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be held,\x01",
            "Please join us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4613")

    label("loc_45BF")


    ChrTalk(
        0xFE,
        (
            "Masses bear the goddess of the sky\x01",
            "Holy celebrations ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be held,\x01",
            "Please join us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4613")

    TalkEnd(0xFE)
    Return()

    # Function_15_3323 end

    def Function_16_4617(): pass

    label("Function_16_4617")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CA")

    ChrTalk(
        0xFE,
        (
            "With children outside the city,\x01",
            "Finally I was able to contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a while the business trip to Sunday school\x01",
            "Although it seems to be able to see the situation,\x01",
            "I am relieved for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4763")

    label("loc_46CA")


    ChrTalk(
        0xFE,
        (
            "You can contact the children outside the city,\x01",
            "I am relieved for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for the time Sunday school restarted\x01",
            "Sister Marbleと授業内容を\x01",
            "Should I consult with you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4763")

    Jump("loc_5A39")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480C")

    ChrTalk(
        0xFE,
        (
            "To children outside the city\x01",
            "While the situation is hard to keep in touch,\x01",
            "I wonder how this happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess ……\x01",
            "Please please protect people …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_483F")

    label("loc_480C")


    ChrTalk(
        0xFE,
        (
            "Oh, Goddess ……\x01",
            "Please please protect people …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_483F")

    Jump("loc_5A39")

    label("loc_4844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498E")

    ChrTalk(
        0xFE,
        (
            "先日、Sister · Leaseが\x01",
            "I left the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything from Alteria law country\x01",
            "It is said that there was an instruction to summon … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Erie, maybe this … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yeah, maybe \"Star Cup Knight\" as\x01",
            "I guess the instructions came down. )\x02\x03",
            "#00103F(Until what it is\x01",
            "I do not know exactly … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A04")

    label("loc_498E")


    ChrTalk(
        0xFE,
        (
            "先日、Sister · Leaseが\x01",
            "I left the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything from Alteria law country\x01",
            "It is said that there was an instruction to summon … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A04")

    Jump("loc_5A39")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A3B")
    Call(0, 54)
    Return()

    label("loc_4A3B")


    ChrTalk(
        0xFE,
        (
            "In this Mass, than usual\x01",
            "Quite a few people are visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the wounds owed by people in the raid incident,\x01",
            "It seems to be very big …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_4AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA5")

    ChrTalk(
        0xFE,
        (
            "Kimi-chan and Alek-kun … ….\x01",
            "I just met the day before yesterday.\x01",
            "It is getting caught up in such an incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There will be scary feelings … …\x01",
            "Oh goddess, please remember those children,\x01",
            "Please save Mainz ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C2A")

    label("loc_4BA5")


    ChrTalk(
        0xFE,
        (
            "To Mainz, the day before yesterday\x01",
            "I went to a Sunday school business trip\x01",
            "It is only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh goddess, please remember those children,\x01",
            "Please save Mainz ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C2A")

    Jump("loc_5A39")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C3D")
    Jump("loc_5A39")

    label("loc_4C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C4B")
    Jump("loc_5A39")

    label("loc_4C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C59")
    Jump("loc_5A39")

    label("loc_4C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_4D27")

    ChrTalk(
        0xFE,
        (
            "Senior class lessons as well\x01",
            "You seem to have finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am going tomorrow, the day after tomorrow\x01",
            "In Mainz, Almorica\x01",
            "I am going to a business trip on Sunday school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あとでSister Marbleに\x01",
            "I have to consult the lesson content.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_4D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_4E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E01")

    ChrTalk(
        0xFE,
        "Sister Marbleに御用ですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is back,\x01",
            "I am in the middle of an older class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今日はSister Juzyに\x01",
            "It seems to teach the way of teaching,\x01",
            "I may not be able to take my hand … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E96")

    label("loc_4E01")


    ChrTalk(
        0xFE,
        (
            "Sister Marbleはたった今、\x01",
            "I am in the middle of an older class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今日はSister Juzyの\x01",
            "Because it also serves as an education,\x01",
            "You may not be able to take your hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    Jump("loc_5A39")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_503F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC8")

    ChrTalk(
        0xFE,
        (
            "今日は、Sister Juzyが\x01",
            "Sister Marbleに授業のやり方を\x01",
            "It seems they are learning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During this time, a business trip to Mainz\x01",
            "Sister · Leaseに任せたことが\x01",
            "いい刺激になったLooks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although technology is scary,\x01",
            "I have a talent for children\x01",
            "I'm sure you will get better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_503A")

    label("loc_4FC8")


    ChrTalk(
        0xFE,
        (
            "Sister Juzyは\x01",
            "I have a talent for children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it is a Sunday school class,\x01",
            "I'm sure you will get better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503A")

    Jump("loc_5A39")

    label("loc_503F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_532F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5114")

    ChrTalk(
        0xFE,
        (
            "Sister · Leaseが\x01",
            "Earlier on Sunday school business trip\x01",
            "It seems they came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it was a bit late\x01",
            "I was worried, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you mean somewhere\x01",
            "Did you eat even rice?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5193")

    label("loc_5114")


    ChrTalk(
        0xFE,
        (
            "Sister · Leaseが\x01",
            "Earlier on Sunday school business trip\x01",
            "It seems they came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今はSister Marbleの所へ\x01",
            "I'm going to report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5193")

    Jump("loc_532A")

    label("loc_5198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A7")

    ChrTalk(
        0xFE,
        (
            "Sister · Leaseは今日、\x01",
            "Sunday school in the direction of Mainz\x01",
            "I'm going on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is quiet person, but\x01",
            "I am good at teaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, even if I come back soon\x01",
            "It's a good time, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps, you got over the bus.\x01",
            "I wonder if it has gone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_532A")

    label("loc_52A7")


    ChrTalk(
        0xFE,
        (
            "Sister · Lease、\x01",
            "Even if I come back from my business trip soon\x01",
            "It's a good time, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps, you got over the bus.\x01",
            "I wonder if it has gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_532A")

    Jump("loc_5A39")

    label("loc_532F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_534A")
    Call(0, 14)
    Jump("loc_53D9")

    label("loc_534A")


    ChrTalk(
        0xFE,
        (
            "Archbishop Ellarda……\x01",
            "以前からSister · Leaseのことを\x01",
            "It seems to be bothering to burn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even with circumstances unknown to us\x01",
            "Is there a reason …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D9")

    Jump("loc_5A39")

    label("loc_53DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_55E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5547")

    ChrTalk(
        0xFE,
        (
            "Mainz and children of Armorica,\x01",
            "Because the cathedral is far away, even Sunday school\x01",
            "I can not communicate easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, the children of the old city etc\x01",
            "Even on the day of classes the church\x01",
            "It does not come easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those children,\x01",
            "We visit Sister towns and villages\x01",
            "I am carrying out classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, today,\x01",
            "Sister · Leaseに旧市街へ\x01",
            "I'm having a business trip.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55DE")

    label("loc_5547")


    ChrTalk(
        0xFE,
        (
            "By the way, today,\x01",
            "Sister · Leaseに旧市街へ\x01",
            "I'm having a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are only a few habitable children over there,\x01",
            "Are they well done … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55DE")

    Jump("loc_5A39")

    label("loc_55E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_56A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FE")
    Call(0, 13)
    Jump("loc_56A0")

    label("loc_55FE")


    ChrTalk(
        0xFE,
        (
            "Sister · Leaseはとても\x01",
            "It is early to memorize the job ……\x01",
            "We have been helped a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Ellarda……\x01",
            "Anything to worry about her\x01",
            "Is it there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A0")

    Jump("loc_5A39")

    label("loc_56A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_572C")

    ChrTalk(
        0xFE,
        (
            "Mr. Lease\x01",
            "After the greeting to the archbishop,\x01",
            "It seems he went to the cemetery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From tomorrow on us\x01",
            "If you do not teach work variously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_59A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5917")

    ChrTalk(
        0xFE,
        (
            "Sister · Leaseは\x01",
            "It was kind of calm,\x01",
            "It is a very atmosphereful person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, from her\x01",
            "A very delicious smell\x01",
            "I did it, but that one ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fby the way……\x01",
            "Mr. Lease from honestly\x01",
            "Like the smell of bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FPerhaps, drop by a baker before coming\x01",
            "I wonder if you did some shopping.\x02\x03",
            "#00109FLeith is that slender\x01",
            "It is quite a snack food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWell, hey … is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, once you have a meal\x01",
            "You want to join us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59A4")

    label("loc_5917")


    ChrTalk(
        0xFE,
        (
            "Sister · Leaseは\x01",
            "It was kind of calm,\x01",
            "It is a very atmosphereful person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sister Juzyにとっても\x01",
            "It is going to be a nice stimulation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A4")

    Jump("loc_5A39")

    label("loc_59A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A39")

    ChrTalk(
        0xFE,
        (
            "Actually today, a new sister\x01",
            "From Alteria law country\x01",
            "It is scheduled to be dispatched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of person is coming ……\x01",
            "It is a little fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A39")

    TalkEnd(0xFE)
    Return()

    # Function_16_4617 end

    def Function_17_5A3D(): pass

    label("Function_17_5A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AC0")

    ChrTalk(
        0xC,
        (
            "People who seek salvation in the church\x01",
            "I will come across one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Prepare for us well\x01",
            "I have to welcome you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B2B")

    ChrTalk(
        0xC,
        (
            "To the serious thing in Crossbell City\x01",
            "It seems to be getting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I hope the citizens are safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1C")

    ChrTalk(
        0xC,
        (
            "Crossbell's national independence … ….\x01",
            "That's outrageous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Besides, bank freezing funding ……\x01",
            "As a human being of the Seven Yigh Church,\x01",
            "It 's not something you can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We also watched the situation for a while\x01",
            "It looks like it will …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5CAD")

    label("loc_5C1C")


    ChrTalk(
        0xC,
        (
            "Funds freezing of banks …\x01",
            "As a human being of the Seven Yigh Church,\x01",
            "It 's not something you can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We also watched the situation for a while\x01",
            "It looks like it will …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAD")

    Jump("loc_6A1E")

    label("loc_5CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D62")

    ChrTalk(
        0xC,
        (
            "Restoration of old city,\x01",
            "Testers' children\x01",
            "It seems that he takes the initiative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What are you thinking at first?\x01",
            "I thought I did not understand, but …\x01",
            "It seems that the roots were good children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DD6")

    ChrTalk(
        0xC,
        (
            "I do not think such an incident will happen\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "People in Mainz\x01",
            "I hope it is safe ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5E63")

    ChrTalk(
        0xC,
        (
            "Just a while ago,\x01",
            "I was stuck with climax to the grand scale\x01",
            "I have witnessed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, she is quite\x01",
            "I can not get rid of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5ED7")

    ChrTalk(
        0xC,
        (
            "This pedestal, for medicine etc.\x01",
            "It is commonly used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "More than other places\x01",
            "I have to clean it thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_5ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F9C")

    ChrTalk(
        0xC,
        (
            "Lease kun always uses the scriptures\x01",
            "You seem to be carrying around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have time to open books\x01",
            "You are reading\x01",
            "I often see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, I'm diligent.\x01",
            "It is quite good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6023")

    label("loc_5F9C")


    ChrTalk(
        0xC,
        (
            "Lease kun always uses the scriptures\x01",
            "You seem to be carrying around.\x01",
            "It seems I have read it if I have my free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, I'm diligent.\x01",
            "It is quite good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6023")

    Jump("loc_6A1E")

    label("loc_6028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_60A0")

    ChrTalk(
        0xC,
        (
            "Lease kun, from the streets\x01",
            "It seems they came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Where did you eat today.\x01",
            "I guess I'll ask you later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_60A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_6111")

    ChrTalk(
        0xC,
        "Well, cleaning is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a place everyone uses.\x01",
            "I have to keep it clean.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_6111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C5")

    ChrTalk(
        0xC,
        (
            "I was cleaning the office,\x01",
            "The archbishop comes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because there is something I want to examine\x01",
            "I was told to be alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "HM……\x01",
            "What on earth are you examining?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_622D")

    label("loc_61C5")


    ChrTalk(
        0xC,
        (
            "Lease as earlier,\x01",
            "Go to the town for lunch\x01",
            "It seems I got it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I suppose I will take a break, too.\x02",
    )

    CloseMessageWindow()

    label("loc_622D")

    Jump("loc_6A1E")

    label("loc_6232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_639F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6315")

    ChrTalk(
        0xC,
        (
            "His Highness Claudia,\x01",
            "Tension for today's plenary session\x01",
            "I thought he was doing it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, ridiculous,\x01",
            "I was very calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected, the next Queen of Libert ……\x01",
            "The liver is standing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_639A")

    label("loc_6315")


    ChrTalk(
        0xC,
        (
            "Before the plenary session,\x01",
            "Your Highness Claudia\x01",
            "I was quite calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected, the next Queen of Libert ……\x01",
            "The liver is standing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_639A")

    Jump("loc_6A1E")

    label("loc_639F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_652C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6486")

    ChrTalk(
        0xC,
        "I was surprised at the unveiling ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To be honest,\x01",
            "The 40th floor above ground is very\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To Haha, Mayor of Dieter,\x01",
            "Even when I came to worship this time\x01",
            "I have to apologize.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6527")

    label("loc_6486")


    ChrTalk(
        0xC,
        (
            "I was surprised at the unveiling ceremony.\x01",
            "No way, there are truly 40 floors … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To Haha, Mayor of Dieter,\x01",
            "Even when I came to worship this time\x01",
            "I have to apologize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6527")

    Jump("loc_6A1E")

    label("loc_652C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_66DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6643")

    ChrTalk(
        0xC,
        (
            "Archbishop Ellardaは\x01",
            "Because it is a very strict person,\x01",
            "There are many conflicts in the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Among them, the content of the activity is not clear\x01",
            "Regarding the human being of \"Seiyuu\"\x01",
            "Especially taking a tough attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks to the officials of the Seaplane Province\x01",
            "In the crossbell parish\x01",
            "It rarely comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_66D6")

    label("loc_6643")


    ChrTalk(
        0xC,
        (
            "Speaking of the Ministry of Construction\x01",
            "It is said to manage the goddess's sacrament\x01",
            "Although it is an institution in the church ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The content of that activity is also to the general clergy\x01",
            "I have not been told about it in detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66D6")

    Jump("loc_6A1E")

    label("loc_66DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C5")

    ChrTalk(
        0xC,
        (
            "Mr Lease, he seems to be adult\x01",
            "I was worried about being familiar with everyone … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yesterday's supper with Juju who is on duty\x01",
            "It seems that I was the first to openly understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Last night we talked about delicious shops in the city\x01",
            "It seems that it was very exciting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_684B")

    label("loc_67C5")


    ChrTalk(
        0xC,
        (
            "Mr. Lease, when it comes to food\x01",
            "Actively talking to the story, do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, passion for food is\x01",
            "There seems to be something strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684B")

    Jump("loc_6A1E")

    label("loc_6850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_68E9")

    ChrTalk(
        0xC,
        (
            "Archbishop, though the greeting is over\x01",
            "It was like thinking something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Something to Mr. Lease\x01",
            "I wonder whether it was also a problem.\x01",
            "I can not see that ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_68E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_698E")

    ChrTalk(
        0xC,
        (
            "Coming in newly\x01",
            "Regarding priests and sisters,\x01",
            "The archbishop gathers each person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A person who is ineligible as a priest\x01",
            "It can not be put in the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_698E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6A1E")

    ChrTalk(
        0xC,
        (
            "ここはArchbishop Ellardaの\x01",
            "I am in the office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Unusual medicinal herbs and precious books\x01",
            "Because it is kept,\x01",
            "Do not touch too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1E")

    TalkEnd(0xFE)
    Return()

    # Function_17_5A3D end

    def Function_18_6A22(): pass

    label("Function_18_6A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0F")

    ChrTalk(
        0xFE,
        (
            "Suddenly such a thing appeared,\x01",
            "Everyone in the business seems to be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But do not worry.\x01",
            "As long as I pray to the goddess\x01",
            "Absolutely fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, let 's pray for you too.\x01",
            "So everything goes\x01",
            "You should succeed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6B9F")

    label("loc_6B0F")


    ChrTalk(
        0xFE,
        (
            "No matter what happens,\x01",
            "As long as I pray to the goddess\x01",
            "Absolutely fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, let 's pray for you too.\x01",
            "So everything goes\x01",
            "You should succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9F")

    Jump("loc_8017")

    label("loc_6BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C58")

    ChrTalk(
        0xFE,
        (
            "Or while martial law enforcement is issued\x01",
            "If you come to pray secretly,\x01",
            "Such a thing has happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not go back to the city with this.\x01",
            "What am I supposed to do …?! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6CA0")

    label("loc_6C58")


    ChrTalk(
        0xFE,
        (
            "Anyway,\x01",
            "To make things happen soon\x01",
            "I have to pray for the goddess ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CA0")

    Jump("loc_8017")

    label("loc_6CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D9D")

    ChrTalk(
        0xFE,
        (
            "When the operation of the railroad stops,\x01",
            "From now on the work of trade\x01",
            "It is likely to become tough …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I am in the process of the world\x01",
            "I do not mean to go against it.\x01",
            "This is surely the intention of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nano, somehow.\x01",
            "I have to even forget the believing heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6E10")

    label("loc_6D9D")


    ChrTalk(
        0xFE,
        (
            "As long as I pray to the goddess\x01",
            "Surely, everything\x01",
            "It should work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you also pray.\x01",
            "It is a believing heart that matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E10")

    Jump("loc_8017")

    label("loc_6E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF8")

    ChrTalk(
        0xFE,
        (
            "Recently there is a prayer for the goddess\x01",
            "The business was going well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If a serious incident has occurred so far\x01",
            "To be honest, I am not happy with letting go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely, to make it profitable\x01",
            "There is no point in it.\x01",
            "I should pray for peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6F69")

    label("loc_6EF8")


    ChrTalk(
        0xFE,
        (
            "No matter how much money you make,\x01",
            "In this situation Crossbell\x01",
            "I can not rejoice with letting go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Peacefully,\x01",
            "I should pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F69")

    Jump("loc_8017")

    label("loc_6F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701C")

    ChrTalk(
        0xFE,
        (
            "Actually today, in Seoul in Mainz\x01",
            "I was going to buy it … ….\x01",
            "There is no way that such an incident happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "I have to pray to the goddess ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7084")

    label("loc_701C")


    ChrTalk(
        0xFE,
        (
            "Even though without business,\x01",
            "I am concerned about Mainz's situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O goddess, please let me know this incident\x01",
            "Lead to solve … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7084")

    Jump("loc_8017")

    label("loc_7089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714E")

    ChrTalk(
        0xFE,
        (
            "Actually yesterday, throughout the day\x01",
            "I feel a sinister feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ask later,\x01",
            "A derailment accident happened\x01",
            "Is not it so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I had no influence on my business negotiations … …\x01",
            "I was honest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_71D3")

    label("loc_714E")


    ChrTalk(
        0xFE,
        (
            "Actually yesterday, throughout the day\x01",
            "I feel a sinister feeling.\x01",
            "I was surprised at the story of a derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I had no influence on my business negotiations … …\x01",
            "I was honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71D3")

    Jump("loc_8017")

    label("loc_71D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727B")

    ChrTalk(
        0xFE,
        (
            "I was praying hard to the goddess … …\x01",
            "The shoelace has run out this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though we have business talks today …\x01",
            "Why is this also ominous! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_72F3")

    label("loc_727B")


    ChrTalk(
        0xFE,
        (
            "Kuroneko crosses the front,\x01",
            "The shoelace has broken ……\x01",
            "It is very ominous from this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope everything happens ….\x02",
    )

    CloseMessageWindow()

    label("loc_72F3")

    Jump("loc_8017")

    label("loc_72F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C4")

    ChrTalk(
        0xFE,
        (
            "…… Actually this morning,\x01",
            "A black cat is crossing me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, hee … …\x01",
            "Although I have business talks today\x01",
            "It is extremely ominous, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is more than usual\x01",
            "I have to pray carefully … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_7432")

    label("loc_73C4")


    ChrTalk(
        0xFE,
        (
            "Although it is a business talk today,\x01",
            "Black cats have crossed my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O goddess, please\x01",
            "Excuse a sinister sign … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7432")

    Jump("loc_8017")

    label("loc_7437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_74C5")

    ChrTalk(
        0xFE,
        (
            "…… Well, I often prayed\x01",
            "I guess I will go home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I still have not yet prayed.\x01",
            "Let's say I am here a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8017")

    label("loc_74C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_7641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A6")

    ChrTalk(
        0xFE,
        (
            "What I had come before\x01",
            "Sure, Professor Ian Grimewood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I was a bit tired … …\x01",
            "In the sacred air full of the chapel,\x01",
            "It must have been healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also prayed … …\x01",
            "It must be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_763C")

    label("loc_75A6")


    ChrTalk(
        0xFE,
        (
            "I am doing business as well\x01",
            "To Professor Grimwood\x01",
            "I often had my consultation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I was a bit tired,\x01",
            "I also prayed … …\x01",
            "It will be healed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763C")

    Jump("loc_8017")

    label("loc_7641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772C")

    ChrTalk(
        0xFE,
        (
            "For independent advocacy during this period,\x01",
            "It seems to be interesting also in other countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Foreign business associates, too,\x01",
            "Cross Bell Independence Complaints\x01",
            "I heard that they are discussing every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here comes the crowbar's attention\x01",
            "It seems to be even more increased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_77C6")

    label("loc_772C")


    ChrTalk(
        0xFE,
        (
            "There is also a referendum on inquiries about independence.\x01",
            "And the result is\x01",
            "The God Only knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O goddess.\x01",
            "For Cross Bell\x01",
            "It seems that the best choice will be made ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C6")

    Jump("loc_8017")

    label("loc_77CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_786E")

    ChrTalk(
        0xFE,
        (
            "Today's plenary session will be held by citizens\x01",
            "I hear that you can not listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sorry, but it can not be helped.\x01",
            "I am here to discuss the success of the meeting\x01",
            "Let's continue praying to the goddess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8017")

    label("loc_786E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_79BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7940")

    ChrTalk(
        0xFE,
        (
            "I also took the Orchis Tower\x01",
            "I went to see it … ….\x01",
            "It was a tremendous height.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From that rooftop,\x01",
            "We also pray for the empty goddess\x01",
            "It should be easier to reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, certainly\x01",
            "I would like to climb it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_79B9")

    label("loc_7940")


    ChrTalk(
        0xFE,
        (
            "From the rooftop of Orkis Tower,\x01",
            "We also pray for the empty goddess\x01",
            "It should be easier to reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I also want to\x01",
            "I would like to climb it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79B9")

    Jump("loc_8017")

    label("loc_79BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A75")

    ChrTalk(
        0xFE,
        (
            "At the commerce meeting from tomorrow,\x01",
            "About the arrangement of economic relations\x01",
            "It seems to be discussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on Crossbell\x01",
            "To me who is doing business,\x01",
            "It is a very interesting event.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7AD5")

    label("loc_7A75")


    ChrTalk(
        0xFE,
        (
            "Trade meeting as a merchant\x01",
            "I am very interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which, the success of the meeting\x01",
            "I have to pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD5")

    Jump("loc_8017")

    label("loc_7ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8D")

    ChrTalk(
        0xFE,
        (
            "Regardless of rain or typhoon,\x01",
            "Whether there are business talks early in the morning,\x01",
            "Never miss a daily prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that,\x01",
            "The condition of business is rising to the right.\x01",
            "Ha ha ha ha\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7BFD")

    label("loc_7B8D")


    ChrTalk(
        0xFE,
        (
            "No matter what I am,\x01",
            "Never miss a daily prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuation is power, you know.\x01",
            "Ha ha ha ha\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFD")

    Jump("loc_8017")

    label("loc_7C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_7DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5D")

    ChrTalk(
        0x153,
        (
            "#01105FOh, I always came praying\x01",
            "It is an orgy.\x02\x03",
            "#01109FIt seems that it came from the morning,\x01",
            "I was still there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I am on holiday,\x01",
            "To pray all day long\x01",
            "You are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pray also for your daughter.\x01",
            "If so, surely,\x01",
            "Everything will be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F…… Lloyd, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(… … even if asked by me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7DE3")

    label("loc_7D5D")


    ChrTalk(
        0xFE,
        (
            "I am on holiday,\x01",
            "To pray all day long\x01",
            "You are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pray for you guys as well.\x01",
            "If so, surely,\x01",
            "Everything will be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DE3")

    Jump("loc_8017")

    label("loc_7DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_7EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6C")

    ChrTalk(
        0xFE,
        (
            "What I am now is,\x01",
            "Thanks to the protection of the goddess ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With enough of gratitude,\x01",
            "I have to pray.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_7ED6")

    label("loc_7E6C")


    ChrTalk(
        0xFE,
        (
            "Oh, the goddess of the sky,\x01",
            "I am always grateful for your help……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By all means next business,\x01",
            "Please give me protection …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED6")

    Jump("loc_8017")

    label("loc_7EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F83")

    ChrTalk(
        0xFE,
        (
            "I am a trading trader.\x01",
            "To pray for business here,\x01",
            "よく来るようにYou are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come and I hope you guys are going to pray\x01",
            "I will recommend it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8017")

    label("loc_7F83")


    ChrTalk(
        0xFE,
        (
            "Even before, if you pray for successful business,\x01",
            "There was something that really worked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever you do, first pray to the goddess.\x01",
            "If you do that, it is no doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8017")

    TalkEnd(0xFE)
    Return()

    # Function_18_6A22 end

    def Function_19_801B(): pass

    label("Function_19_801B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_802C")
    Jump("loc_8ABB")

    label("loc_802C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8537")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_805E")
    Call(0, 56)
    Return()

    label("loc_805E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83BF")

    ChrTalk(
        0x101,
        (
            "#00000FMr. Lease,\x01",
            "I am helping Mass.\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FYes, that is the place.\x02\x03",
            "#04408F…… To this mass,\x01",
            "Especially many visitors\x01",
            "You seem to be visiting.\x02\x03",
            "My precious place was attacked,\x01",
            "Fearfulness to be hurt ……\x02\x03",
            "#04403F…… I also understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMr. Lease ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(… … Similar things to her a long time ago\x01",
            "It may have been there. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(Between ourselves……\x01",
            "In the influence of this incident \"Seiyu\"\x01",
            "I can not decide the future movement. )\x02\x03",
            "#04403F(… … While I am in Crossbell#13R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#,\x01",
            "I will collect information as much as possible. )\x02\x03",
            "#04400F(Lloyd's, too, in the direction of trends\x01",
            "Please be careful. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(While staying ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(……I understand.\x01",
            "Please also take care of Mr. Lease. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)
    Jump("loc_84B5")

    label("loc_83BF")


    ChrTalk(
        0xA,
        (
            "#04400F(Depending on the incident this time, \"Seiyuu Ministry\" also\x01",
            "I can not decide the future movement. )\x02\x03",
            "#04403F(… … While I was in Crossbell,\x01",
            "I will collect information as much as possible. )\x02\x03",
            "#04400F(Lloyd's, too, in the direction of trends\x01",
            "Please be careful. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84B5")

    Jump("loc_8532")

    label("loc_84BA")


    ChrTalk(
        0xA,
        (
            "#04400FI have been in a while for a while\x01",
            "Because there is massage help.\x02\x03",
            "#04404FWhen the program starts\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8532")

    Jump("loc_8ABB")

    label("loc_8537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8545")
    Jump("loc_8ABB")

    label("loc_8545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8886")

    ChrTalk(
        0xA,
        (
            "#04400FYesterday's derailment accident ……\x01",
            "A gigantic thing near the site\x01",
            "It looks like he was witnessed.\x02\x03",
            "Everyone,\x01",
            "What do I get in mind …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FWell, actually …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About yesterday's case\x01",
            "He explained it with care.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405F…… Knock's sea also\x01",
            "Prelimma grass ……\x02\x03",
            "#04408FAnd it again appeared in this place\x01",
            "\"Gnostic\" is … …\x02\x03",
            "#04403FThe problem is \"Who is Gnostic?\" …\x01",
            "Is that so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F… … In that way\x01",
            "You do not grab anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FI am unfortunate, but …\x01",
            "Information on religious relations including Gnostic\x01",
            "It is a situation where investigation has not progressed yet.\x02\x03",
            "#04403FAbout prelimb grass\x01",
            "Although I am recommending investigation,\x01",
            "It is still unknown why blooming … ….\x02\x03",
            "#04400FYou can sneak into this place\x01",
            "As I am the only one,\x01",
            "It seems to take time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so……\x02\x03",
            "#00000FThen, if you know something again\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04400FYeah … I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 1)
    Jump("loc_894C")

    label("loc_8886")


    ChrTalk(
        0xA,
        (
            "#04403FPrestige grass of Knox 's ocean ……\x01",
            "And it again appeared in this place\x01",
            "\"Gnostic\" … ….\x02\x03",
            "#04400FSometimes I can not stand out,\x01",
            "Although the investigation situation is not good …\x01",
            "I will report as soon as I know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894C")

    Jump("loc_8ABB")

    label("loc_8951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_895F")
    Jump("loc_8ABB")

    label("loc_895F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_896D")
    Jump("loc_8ABB")

    label("loc_896D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_897B")
    Jump("loc_8ABB")

    label("loc_897B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_8989")
    Jump("loc_8ABB")

    label("loc_8989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8997")
    Jump("loc_8ABB")

    label("loc_8997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8A37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89BE")
    Call(0, 21)
    Jump("loc_8A32")

    label("loc_89BE")


    ChrTalk(
        0xA,
        (
            "#04400F…… Everyone, thanks for today.\x01",
            "Thank you very much.\x02\x03",
            "#04403FIf there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A32")

    Jump("loc_8ABB")

    label("loc_8A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8A45")
    Jump("loc_8ABB")

    label("loc_8A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8A53")
    Jump("loc_8ABB")

    label("loc_8A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A6E")
    Call(0, 20)
    Jump("loc_8A91")

    label("loc_8A6E")


    ChrTalk(
        0xA,
        "#04403F(Rufina sister … …)\x02",
    )

    CloseMessageWindow()

    label("loc_8A91")

    Jump("loc_8ABB")

    label("loc_8A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_8AA4")
    Jump("loc_8ABB")

    label("loc_8AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_8AB2")
    Jump("loc_8ABB")

    label("loc_8AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8ABB")

    label("loc_8ABB")

    TalkEnd(0xFE)
    Return()

    # Function_19_801B end

    def Function_20_8ABF(): pass

    label("Function_20_8ABF")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04400F…… Indeed, this education\x01",
            "You seem to be quite moving.\x02\x03",
            "#04404FTruly cutting edge\x01",
            "近代都市Is that so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, indeed\x01",
            "It is a bit advanced though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter where you go\x01",
            "Children will not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04402FCertainly … maybe so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … By the way, Mr. Lease.\x01",
            "One thing that I care about\x01",
            "There is a … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you mean,\x01",
            "Rufina's sister … …\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#04405F…… Did you know your sister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, after all.\x01",
            "Since my last names are the same, I came in with a pin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In old days, variously\x01",
            "I was indebted to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FOh really……\x02\x03",
            "#04400Fあの、Sister Marble。\x01",
            "Will you do me a favor……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, you do not have to tell me.\x01",
            "Maybe you too#4R噵 噵#what do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was indebted to Mr. Rufina,\x01",
            "I will not tell Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… But is there only one thing I wonder?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Never, do not push yourself.\x01",
            "Even for your sister ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F……I understand.\x01",
            "Thank you for your thoughtfulness.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 3)
    Return()

    # Function_20_8ABF end

    def Function_21_8ED1(): pass

    label("Function_21_8ED1")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Mr. Lease,\x01",
            "It seems that it was a bit late\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, some monastic clothes\x01",
            "I have been advancing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FSorry for being late.\x02\x03",
            "#04400FActually, tramp on the way home\x01",
            "I have fallen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh no, Lease san\x01",
            "It is surprisingly scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… to say young,\x01",
            "Do not just try to overdo it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400F……Thank you for your concern.\x01",
            "I am changing clothes now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Marble teacher ……\x01",
            "To some extent what happened\x01",
            "It seems she is aware. )\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x2, 0)
    Return()

    # Function_21_8ED1 end

    def Function_22_90D6(): pass

    label("Function_22_90D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90F9")
    Call(0, 23)
    Jump("loc_90FC")

    label("loc_90F9")

    Call(0, 25)

    label("loc_90FC")

    Jump("loc_9104")

    label("loc_9101")

    Call(0, 23)

    label("loc_9104")

    Return()

    # Function_22_90D6 end

    def Function_23_9105(): pass

    label("Function_23_9105")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F9")

    ChrTalk(
        0x8,
        (
            "Lloyd, Erie …\x01",
            "I have something I want to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To that big tree … …\x01",
            "Keyaちゃんがいるのですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTeacher … Do you understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your\x01",
            "Looking at the anxious face,\x01",
            "Somehow my opinion came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… I do not know the circumstances in detail,\x01",
            "There is only one thing I can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keyaちゃんの保護者として、\x01",
            "Be sure to regain it in your hands.\x01",
            "……Sounds good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes … … sure!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 3)
    Jump("loc_9453")

    label("loc_92F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D8")

    ChrTalk(
        0x8,
        (
            "Regardless of circumstances,\x01",
            "Keyaちゃんには\x01",
            "We still need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keyaちゃんにとっても、\x01",
            "It should be the same …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, Ellie, and everyone.\x01",
            "Be sure to bring her to your hands\x01",
            "Take it back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9453")

    label("loc_93D8")


    ChrTalk(
        0x8,
        (
            "Regardless of circumstances,\x01",
            "Keyaちゃんには\x01",
            "We still need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be sure to bring her to your hands\x01",
            "Take it back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9453")

    Jump("loc_AE6D")

    label("loc_9458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_97B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Well, Ellie to Lloyd,\x01",
            "And everyone …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMarble teacher ……\x01",
            "It is safe and than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSorry to keep you worried.\x01",
            "We were sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, that's fine.\x01",
            "If you are okay\x01",
            "Because that's what's more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ところで……Keyaちゃんは、\x01",
            "I wonder if they are with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F……House.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FI know whereabouts … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is that so … I am worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, now\x01",
            "It is a situation not to be pulled in and out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You too\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 2)
    Jump("loc_97AE")

    label("loc_966A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_974E")

    ChrTalk(
        0x8,
        "Keyaちゃん……心配ですね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From the day of that independence declaration\x01",
            "Because I never see it,\x01",
            "I was also curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, now\x01",
            "It is a situation not to be pulled in and out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You too\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_97AE")

    label("loc_974E")


    ChrTalk(
        0x8,
        (
            "…… Anyway, now\x01",
            "It is a situation not to be pulled in and out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You too\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97AE")

    Jump("loc_AE6D")

    label("loc_97B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99BB")

    ChrTalk(
        0x8,
        (
            "Lloyd …\x01",
            "Keyaちゃんは大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently I did not have a Sunday school,\x01",
            "I am a little worried … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F…… That said so,\x01",
            "The situation was strange in the last few days\x01",
            "I feel like it.\x02\x03",
            "#00003FI guess I'm thinking somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FI see …\x01",
            "Even when we go out,\x01",
            "I guess I was very worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps this situation is\x01",
            "I wonder and it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, as a guardian\x01",
            "しっかりとKeyaちゃんを\x01",
            "I will watch over you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 4)
    Jump("loc_9A46")

    label("loc_99BB")


    ChrTalk(
        0x8,
        (
            "This situation of Crossbell …\x01",
            "I do not know what will happen in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, as a guardian\x01",
            "しっかりとKeyaちゃんを\x01",
            "I will watch over you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A46")

    Jump("loc_AE6D")

    label("loc_9A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9BD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A7D")
    Call(0, 55)
    Return()

    label("loc_9A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B48")

    ChrTalk(
        0x8,
        (
            "The children attending Sunday school,\x01",
            "I was able to confirm safe in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because this is the situation,\x01",
            "Classes are closed but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you resume, you will have a healthy smile again\x01",
            "I want you to show me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9BD3")

    label("loc_9B48")


    ChrTalk(
        0x8,
        (
            "Because this is the situation,\x01",
            "Sunday school classes for a while\x01",
            "I am on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you resume, you will have a healthy smile again\x01",
            "I want you to show me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD3")

    Jump("loc_AE6D")

    label("loc_9BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9C48")

    ChrTalk(
        0x8,
        (
            "Becoming a terrible situation\x01",
            "Oops I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "People in Mainz\x01",
            "I hope it is safe … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE6D")

    label("loc_9C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D21")

    ChrTalk(
        0x8,
        (
            "今日はSister Hatinaに、\x01",
            "Sunday school to Almorika village\x01",
            "I am going on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today in the whole crossbell\x01",
            "It is said that it is raining ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Become soaked\x01",
            "I hope not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9DB9")

    label("loc_9D21")


    ChrTalk(
        0x8,
        (
            "今日はSister Hatinaに、\x01",
            "Sunday school to Almorika village\x01",
            "I am going on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is raining,\x01",
            "Become soaked\x01",
            "I hope not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DB9")

    Jump("loc_AE6D")

    label("loc_9DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F28")

    ChrTalk(
        0x8,
        (
            "To Mr. Lease\x01",
            "There was a sister named Rufina,\x01",
            "I was also acquainted with myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She belongs to the \"Secretary of Construction\" of the Church,\x01",
            "With outstanding negotiation skills of various incidents\x01",
            "I was working on a solution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sometime called \"a thousand arms\" etc.,\x01",
            "It was famous in the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Unfortunately a few years ago,\x01",
            "It seems that he was martyred in an unhappy accident … …\x01",
            "I lost a regret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9FC0")

    label("loc_9F28")


    ChrTalk(
        0x8,
        (
            "To Mr. Rufina\x01",
            "I also long ago that I became indebted\x01",
            "It was there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To her again\x01",
            "I would like to thank you … …\x01",
            "I lost a regret.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC0")

    Jump("loc_AE6D")

    label("loc_9FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A1EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A166")

    ChrTalk(
        0x8,
        (
            "By the way, Lloyd … …\x01",
            "Yesterday visited me\x01",
            "I agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if you want to hear something\x01",
            "Were there any?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, as to that\x01",
            "It is for the time being all right now.\x02\x03",
            "#00003F(What is involved in \"Pleroma grass\"\x01",
            "Also contraindicated in church#4Rtaboo#It looks like ……\x01",
            "You should not tell the teacher. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is that so……\x01",
            "That's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehuu, it will be power anytime\x01",
            "Please do not hesitate to depend on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A1E6")

    label("loc_A166")


    ChrTalk(
        0x8,
        (
            "I, as much as possible, of Lloyd's\x01",
            "I would like to be of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehuu, it will be power anytime\x01",
            "Please do not hesitate to depend on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1E6")

    Jump("loc_AE6D")

    label("loc_A1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A2F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A206")
    Call(0, 27)
    Jump("loc_A2EC")

    label("loc_A206")


    ChrTalk(
        0x8,
        (
            "I say that the path of thousands of miles is also one step … …\x01",
            "You only have to remember one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(Archbishop's story,\x01",
            "That thing of the blue flower is\x01",
            "My teacher does not seem to know that … …)\x02\x03",
            "#00003F(Let's visit Mr. Lease again.\x01",
            "You should be in a dormitory in the chapel. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2EC")

    Jump("loc_AE6D")

    label("loc_A2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3BC")

    ChrTalk(
        0x8,
        (
            "In the crossbell autonomous state,\x01",
            "10 of tax revenue in the Empire and the Republic\x01",
            "There is a fixed rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is due to the two major powers as religious countries\x01",
            "Defined, since autonomous state was established\x01",
            "It is one of autonomous state law … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A45B")

    label("loc_A3BC")


    ChrTalk(
        0x8,
        (
            "That is, if independence is established\x01",
            "From these unfavorable rules\x01",
            "It will be released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course, never speaking\x01",
            "It's not easy, but ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A45B")

    Jump("loc_AE6D")

    label("loc_A460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A60A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A551")

    ChrTalk(
        0x8,
        (
            "Things that are hard work\x01",
            "It is transmitted from the front to the children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That way, even with difficult classes\x01",
            "It will listen eagerly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sister Juzyの授業は\x01",
            "Still, it is frustrating,\x01",
            "As for hard work, it is a passing score.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A605")

    label("loc_A551")


    ChrTalk(
        0x8,
        (
            "Sister Juzyの授業は\x01",
            "Still it is frustrating\x01",
            "As for hard work, it is a passing score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even the basic way of teaching\x01",
            "If you learn, surely a good lesson\x01",
            "You will be able to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A605")

    Jump("loc_AE6D")

    label("loc_A60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A87D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A6B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A631")
    Call(0, 21)
    Jump("loc_A6AF")

    label("loc_A631")


    ChrTalk(
        0x8,
        (
            "Mr. Lease's work,\x01",
            "I think it's useless … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Lloyd's also saying that they are young\x01",
            "Do not just try to overdo it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6AF")

    Jump("loc_A878")

    label("loc_A6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F7")

    ChrTalk(
        0x8,
        (
            "His Highness, Claudia,\x01",
            "Libert's strange thing a while ago\x01",
            "解決に貢献したI agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In such a serious incident,\x01",
            "She finishes the ceremonial ceremony\x01",
            "Became the next Queen of Libert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the time it reaches there\x01",
            "How much conflicts existed,\x01",
            "I can not seem to know but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though you are young, very strong core\x01",
            "I guess it's you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A878")

    label("loc_A7F7")


    ChrTalk(
        0x8,
        (
            "Your Highness Claudia\x01",
            "During the incident of Libert\x01",
            "I say I have finished the crown of the Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though you are young, very strong core\x01",
            "I guess it's you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A878")

    Jump("loc_AE6D")

    label("loc_A87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A9FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95D")

    ChrTalk(
        0x8,
        (
            "By the way, today,\x01",
            "It was the day of the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it becomes a building on the 40th floor above ground,\x01",
            "If the children look up\x01",
            "It will be powerful to reach heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, children are around this time\x01",
            "Where are we hungry?\x01",
            "I wonder if.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A9F5")

    label("loc_A95D")


    ChrTalk(
        0x8,
        (
            "If it becomes a building on the 40th floor above ground,\x01",
            "If the children look up\x01",
            "It will be powerful to reach heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, children are around this time\x01",
            "Where are we hungry?\x01",
            "I wonder if.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9F5")

    Jump("loc_AE6D")

    label("loc_A9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AB3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AACE")

    ChrTalk(
        0x8,
        (
            "The trade meeting finally\x01",
            "I approached tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It will be hard for you … …\x01",
            "You also do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes I will try my best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you,\x01",
            "Marble teacher.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AB3A")

    label("loc_AACE")


    ChrTalk(
        0x8,
        (
            "It will be hard for you … …\x01",
            "You also do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me cheer for your support\x01",
            "I will get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3A")

    Jump("loc_AE6D")

    label("loc_AB3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ABC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5A")
    Call(0, 20)
    Jump("loc_ABC2")

    label("loc_AB5A")


    ChrTalk(
        0x8,
        (
            "Oh, the Lloyd … …\x01",
            "I wonder if it will be on such a rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do not catch a cold\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC2")

    Jump("loc_AE6D")

    label("loc_ABC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_ADD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD4C")
    TurnDirection(0x8, 0x153, 0)

    ChrTalk(
        0x8,
        (
            "ふふ、Keyaちゃん。\x01",
            "Next senior class\x01",
            "We look forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This time a little more difficult question\x01",
            "I am preparing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYeah, I understand.\x01",
            "Keya、がんばって予習するね！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FWell, it is really amazing …\x01",
            "I admire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, of course we also\x01",
            "You may be overtaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, when that happens\x01",
            "As expected there is no stagnation ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_ADD3")

    label("loc_AD4C")


    ChrTalk(
        0x8,
        (
            "Keyaちゃんが来てから、\x01",
            "Also in senior class lessons\x01",
            "More vibrancy came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, other children\x01",
            "It sounds like a good stimulation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD3")

    Jump("loc_AE6D")

    label("loc_ADD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_ADE6")
    Jump("loc_AE6D")

    label("loc_ADE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AE6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE01")
    Call(0, 24)
    Jump("loc_AE6D")

    label("loc_AE01")


    ChrTalk(
        0x8,
        (
            "Huhu, then you guys.\x01",
            "I have a continuation of the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On another occasion\x01",
            "Please come and visit us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE6D")

    TalkEnd(0x8)
    Return()

    # Function_23_9105 end

    def Function_24_AE71(): pass

    label("Function_24_AE71")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1700, 16650, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27870, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x101, 153000, 200, 16800, 270)
    SetChrPos(0x102, 153300, 200, 17700, 270)
    SetChrPos(0x109, 154200, 200, 17580, 270)
    SetChrPos(0x105, 153900, 200, 16580, 270)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "Well, Lloyd's Erie ……\x01",
            "You came a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fお久しぶりです、Marble teacher.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105Flong time no see……\x01",
            "You are not surprised too much, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ふふ、さっきKeyaちゃんが\x01",
            "\"Came back~! \"\x01",
            "Because I was talking happily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSurely, Mr. Lloyd and Ellie 's,\x01",
            "Teacher from Sunday school days … was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I see.\x01",
            "You guys like that\x01",
            "It seems like a new member of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am Sister of the Seven Year Society,\x01",
            "I am Marble.\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, that's … …\x01",
            "Noel is a marble teacher\x01",
            "Did not you learn it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, at that time I was frank with me\x01",
            "Eastern Street class,\x01",
            "The father was in charge.\x02\x03",
            "#10103FNow for crossbell\x01",
            "I do not see you coming … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, the church priest\x01",
            "What I'm going to change\x01",
            "I guess it will remain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, in that sense\x01",
            "Reunion with Lloyd and Eli also\x01",
            "It was quite a fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Marble teacher ~,\x01",
            "Only with my older brothers\x01",
            "Let 's have classes without talking ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "もう、Ryuってば。\x01",
            "It seems like a reunited meeting\x01",
            "Let 's give it water.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh no, sorry.\x01",
            "I was pleased and told you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, then you guys,\x01",
            "I have a continuation of the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On another occasion\x01",
            "Please come and visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, sorry,\x01",
            "I interrupted the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell then, then\x01",
            "Excuse me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 2)
    EventEnd(0x5)
    Return()

    # Function_24_AE71 end

    def Function_25_B49E(): pass

    label("Function_25_B49E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B58E")

    ChrTalk(
        0xF,
        (
            "It is.\x01",
            "In short, it was done the other day\x01",
            "What is the trade meeting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "So-called\x01",
            "Economic relationship arrangements ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, a bit better\x01",
            "I do not understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "Well, well then, then,\x01",
            "Again from the beginning ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B604")

    label("loc_B58E")


    ChrTalk(
        0xF,
        (
            "(U, the task to deal with a bit\x01",
            "I wonder if it was too difficult ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(But, because it's important\x01",
            "I have to tell it firmly …! )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B604")

    TalkEnd(0xF)
    Return()

    # Function_25_B49E end

    def Function_26_B608(): pass

    label("Function_26_B608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B619")
    Jump("loc_BC33")

    label("loc_B619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B627")
    Jump("loc_BC33")

    label("loc_B627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B635")
    Jump("loc_BC33")

    label("loc_B635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B73C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6BD")

    ChrTalk(
        0xFE,
        (
            "On a rainy day\x01",
            "Because the floor is slippery\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. a while ago, I also slipped\x01",
            "Because I fell down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B737")

    label("loc_B6BD")


    ChrTalk(
        0xFE,
        (
            "Haha, today Sunday school is closed\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If such a scene was seen by children\x01",
            "Cha is more licked ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B737")

    Jump("loc_BC33")

    label("loc_B73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B74A")
    Jump("loc_BC33")

    label("loc_B74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B758")
    Jump("loc_BC33")

    label("loc_B758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_B7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B773")
    Call(0, 27)
    Jump("loc_B7E3")

    label("loc_B773")


    ChrTalk(
        0xFE,
        (
            "Sister Marbleの教えは\x01",
            "It really becomes study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someday, like her\x01",
            "I want to become a fine sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E3")

    Jump("loc_BC33")

    label("loc_B7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_B905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B892")

    ChrTalk(
        0xFE,
        (
            "やっぱりSister Marbleの授業は\x01",
            "It will be useless …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not go away.\x01",
            "Do not listen to classes regularly,\x01",
            "I need to refer …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B900")

    label("loc_B892")


    ChrTalk(
        0xFE,
        (
            "Sister Marbleの授業を見て\x01",
            "I am studying how to teach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, well\x01",
            "I listen to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B900")

    Jump("loc_BC33")

    label("loc_B905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9FB")

    ChrTalk(
        0xFE,
        (
            "It is.\x01",
            "In short, it was done the other day\x01",
            "What is the trade meeting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So-called\x01",
            "Economic relationship arrangements ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, a bit better\x01",
            "I do not understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, well then, then,\x01",
            "Again from the beginning ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BA71")

    label("loc_B9FB")


    ChrTalk(
        0xFE,
        (
            "(U, the task to deal with a bit\x01",
            "I wonder if it was too difficult ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(But, because it's important\x01",
            "I have to tell it firmly …! )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA71")

    Jump("loc_BC33")

    label("loc_BA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BA84")
    Jump("loc_BC33")

    label("loc_BA84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BA92")
    Jump("loc_BC33")

    label("loc_BA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BAA0")
    Jump("loc_BC33")

    label("loc_BAA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BC0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB87")

    ChrTalk(
        0xFE,
        (
            "Sister · Leaseって、\x01",
            "Several years in Alteria\x01",
            "シスターをやってたLooks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am about the same age,\x01",
            "I'm much more calm than I … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, he was trying to seniors in an era\x01",
            "I am ashamed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BC09")

    label("loc_BB87")


    ChrTalk(
        0xFE,
        (
            "はあ、まさかSister · Leaseが\x01",
            "I was a senior for years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was delighted to think that my juniors were able to do it,\x01",
            "It is embarrassing somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC09")

    Jump("loc_BC33")

    label("loc_BC0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_BC1C")
    Jump("loc_BC33")

    label("loc_BC1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_BC2A")
    Jump("loc_BC33")

    label("loc_BC2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BC33")

    label("loc_BC33")

    TalkEnd(0xFE)
    Return()

    # Function_26_B608 end

    def Function_27_BC37(): pass

    label("Function_27_BC37")

    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xF,
        (
            "Sister Marble。\x01",
            "Today I learned a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In that young class lesson\x01",
            "Show me a miserable place\x01",
            "I'm sorry but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huhuu, you do not have to worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I say that the path of thousands of miles is also one step … …\x01",
            "You only have to remember one by one.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_27_BC37 end

    def Function_28_BD3F(): pass

    label("Function_28_BD3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD54")
    Call(0, 50)
    Jump("loc_BDC8")

    label("loc_BD54")


    ChrTalk(
        0x11,
        (
            "#01100FKeya、日曜学校大好きだよ。\x02\x03",
            "#01109FI can study various things everyday,\x01",
            "RyuやHenryたちと\x01",
            "It is fun to see you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC8")

    TalkEnd(0xFE)
    Return()

    # Function_28_BD3F end

    def Function_29_BDCC(): pass

    label("Function_29_BDCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC0")

    ChrTalk(
        0xFE,
        (
            "Well, after all studying\x01",
            "Do not feel troubled … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Onii-chan, hey\x01",
            "Will you study for me instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell … … for myself, right?\x01",
            "You'd better do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chih, things like Dad\x01",
            "Saying that 's cancer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BEEB")

    label("loc_BEC0")


    ChrTalk(
        0xFE,
        (
            "Well, after all studying\x01",
            "I'm sorry to bother you\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEEB")

    TalkEnd(0xFE)
    Return()

    # Function_29_BDCC end

    def Function_30_BEEF(): pass

    label("Function_30_BEEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF94")
    SetChrSubChip(0x13, 0x1)
    Sleep(500)
    SetChrSubChip(0x12, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Ryu、ちゃんとしなよ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "このままじゃKeyaちゃんに\x01",
            "All I can do is put it in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Well, I know.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_BFFC")

    label("loc_BF94")


    ChrTalk(
        0xFE,
        (
            "僕も、Ryuのことばかり\x01",
            "I can not say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keyaちゃんに\x01",
            "I have to try not to lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFFC")

    TalkEnd(0xFE)
    Return()

    # Function_30_BEEF end

    def Function_31_C000(): pass

    label("Function_31_C000")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0ED")
    OP_63(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x14)

    ChrTalk(
        0xFE,
        "Well, uh … ….\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x14, 0x1)
    Sleep(500)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "ねえKeyaちゃん……\x01",
            "What should I do here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01100FWell, the calculation here is not …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(my mother……\x01",
            "It looks like they are doing good together. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C120")

    label("loc_C0ED")


    ChrTalk(
        0xFE,
        (
            "Is that so … ….\x01",
            "You can do it like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C120")

    TalkEnd(0xFE)
    Return()

    # Function_31_C000 end

    def Function_32_C124(): pass

    label("Function_32_C124")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3B4")

    ChrTalk(
        0x101,
        (
            "#00000Fやあ、Panceじゃないか。\x01",
            "Have you been doing fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, older brother\x01",
            "Wendy's big sister\x01",
            "You are a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, after a long absence,\x01",
            "I am indebted to Masu.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_END)), "loc_C26E")

    ChrTalk(
        0x105,
        "#10305FWendy is true, … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I just met you.\x01",
            "Officer of the oval store.\x02\x03",
            "#00109FHehe, it is childhood friend of Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2EE")

    label("loc_C26E")


    ChrTalk(
        0x105,
        "#10305FWendy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI am in the oval store\x01",
            "About the technician.\x02\x03",
            "#00109FHehe, it is childhood friend of Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2EE")


    ChrTalk(
        0xFE,
        (
            "So, that mechataka\x01",
            "It is my older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FWell, that's quite a word.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it is true.\x01",
            "Does your older brother think that, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(… surely, I will not deny it.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 1)
    Jump("loc_C423")

    label("loc_C3B4")


    ChrTalk(
        0xFE,
        (
            "My sister\x01",
            "Mecha-otaku turned out that,\x01",
            "It is influence of Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I absolutely must,\x01",
            "That's not going to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C423")

    TalkEnd(0xFE)
    Return()

    # Function_32_C124 end

    def Function_33_C427(): pass

    label("Function_33_C427")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C438")
    Jump("loc_C5F7")

    label("loc_C438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C4AF")

    ChrTalk(
        0xFE,
        "Today is a mass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are usually playing normally,\x01",
            "I should be bashful at such times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F7")

    label("loc_C4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C4BD")
    Jump("loc_C5F7")

    label("loc_C4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C4CB")
    Jump("loc_C5F7")

    label("loc_C4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C4D9")
    Jump("loc_C5F7")

    label("loc_C4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C4E7")
    Jump("loc_C5F7")

    label("loc_C4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_C4F5")
    Jump("loc_C5F7")

    label("loc_C4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_C503")
    Jump("loc_C5F7")

    label("loc_C503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C511")
    Jump("loc_C5F7")

    label("loc_C511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C51F")
    Jump("loc_C5F7")

    label("loc_C51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C52D")
    Jump("loc_C5F7")

    label("loc_C52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C53B")
    Jump("loc_C5F7")

    label("loc_C53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C549")
    Jump("loc_C5F7")

    label("loc_C549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_C557")
    Jump("loc_C5F7")

    label("loc_C557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_C565")
    Jump("loc_C5F7")

    label("loc_C565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C5F7")

    ChrTalk(
        0xFE,
        (
            "ちぇっ、Hamillのやつ\x01",
            "Keyaにいいトコ見せたいからって\x01",
            "Recently I'm tiny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm better than studying\x01",
            "I prefer to play outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5F7")

    TalkEnd(0xFE)
    Return()

    # Function_33_C427 end

    def Function_34_C5FB(): pass

    label("Function_34_C5FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C60C")
    Jump("loc_C7A2")

    label("loc_C60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C65A")

    ChrTalk(
        0xFE,
        (
            "Goddess……\x01",
            "Please make everyone in the city\x01",
            "Please turn it up … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7A2")

    label("loc_C65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C668")
    Jump("loc_C7A2")

    label("loc_C668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C676")
    Jump("loc_C7A2")

    label("loc_C676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C684")
    Jump("loc_C7A2")

    label("loc_C684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C692")
    Jump("loc_C7A2")

    label("loc_C692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_C6A0")
    Jump("loc_C7A2")

    label("loc_C6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_C6AE")
    Jump("loc_C7A2")

    label("loc_C6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C6BC")
    Jump("loc_C7A2")

    label("loc_C6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C6CA")
    Jump("loc_C7A2")

    label("loc_C6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C6D8")
    Jump("loc_C7A2")

    label("loc_C6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C6E6")
    Jump("loc_C7A2")

    label("loc_C6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C6F4")
    Jump("loc_C7A2")

    label("loc_C6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_C702")
    Jump("loc_C7A2")

    label("loc_C702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_C710")
    Jump("loc_C7A2")

    label("loc_C710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7A2")

    ChrTalk(
        0xFE,
        (
            "Ha ~ …\x01",
            "Keyaちゃん、かわいいなあ。\x01",
            "I am glad that I could study together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today I also raised my hands,\x01",
            "I have to answer the Banban problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A2")

    TalkEnd(0xFE)
    Return()

    # Function_34_C5FB end

    def Function_35_C7A6(): pass

    label("Function_35_C7A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83E")

    ChrTalk(
        0xFE,
        (
            "I like shopping,\x01",
            "To the economy\x01",
            "I am interested, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The matter of the commerce meeting during this time\x01",
            "It is still hard for us to guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C873")

    label("loc_C83E")


    ChrTalk(
        0xFE,
        (
            "About the trade meeting\x01",
            "It is still hard for us to guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C873")

    TalkEnd(0xFE)
    Return()

    # Function_35_C7A6 end

    def Function_36_C877(): pass

    label("Function_36_C877")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If this is Azelle-chan,\x01",
            "Do you understand ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time my older will come home\x01",
            "Let's listen.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_C877 end

    def Function_37_C8EA(): pass

    label("Function_37_C8EA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hmmmm … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I do not understand well after all.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_C8EA end

    def Function_38_C927(): pass

    label("Function_38_C927")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Fa\x01",
            "Studying makes me sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Sister is doing my best too\x01",
            "I have to listen properly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_C927 end

    def Function_39_C99A(): pass

    label("Function_39_C99A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA3E")

    ChrTalk(
        0xFE,
        (
            "Fuf, Humphre ……\x01",
            "Two Shaw Kigi ne ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This degree, common sense.\x01",
            "It's too simple to laugh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Ho, really?\x01",
            "Because I really understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_CAAC")

    label("loc_CA3E")


    ChrTalk(
        0xFE,
        (
            "Two shawaiigi is common sense.\x01",
            "Easy, easy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Already, go to that place!\x01",
            "Because I am studying!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAAC")

    TalkEnd(0xFE)
    Return()

    # Function_39_C99A end

    def Function_40_CAB0(): pass

    label("Function_40_CAB0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the future, even difficult things\x01",
            "I have to study neatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … Are your older doers studying?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_CAB0 end

    def Function_41_CB1A(): pass

    label("Function_41_CB1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CB67")

    ChrTalk(
        0xFE,
        "Hey, where will you go after this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess I am the department store?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBD0")

    label("loc_CB67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CBD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB82")
    Call(0, 42)
    Jump("loc_CBD0")

    label("loc_CB82")


    ChrTalk(
        0xFE,
        (
            "（Linally……\x01",
            "You are my fault and I\x01",
            "I got angry … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBD0")

    TalkEnd(0xFE)
    Return()

    # Function_41_CB1A end

    def Function_42_CBD4(): pass

    label("Function_42_CBD4")


    ChrTalk(
        0x1F,
        (
            "Sister,\x01",
            "Easy diet etc\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "You are in class\x01",
            "I am trying to hear stupid things\x01",
            "Please stop when you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "I can get mad again.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hehe, the second person there.\x01",
            "Quietly in class.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "Yes……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Ha, well …\x01",
            "(I got scolded by … …)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_42_CBD4 end

    def Function_43_CD03(): pass

    label("Function_43_CD03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CD3A")

    ChrTalk(
        0xFE,
        "I really do not get tired of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD6F")

    label("loc_CD3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CD6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD55")
    Call(0, 42)
    Jump("loc_CD6F")

    label("loc_CD55")


    ChrTalk(
        0xFE,
        "(Sorry, … …)\x02",
    )

    CloseMessageWindow()

    label("loc_CD6F")

    TalkEnd(0xFE)
    Return()

    # Function_43_CD03 end

    def Function_44_CD73(): pass

    label("Function_44_CD73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CDFA")

    ChrTalk(
        0xFE,
        (
            "No, Today about independence\x01",
            "It was nice to learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just read the Crossbell Times\x01",
            "There are things that do not come in sight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE54")

    label("loc_CDFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CE54")

    ChrTalk(
        0xFE,
        "I see, i see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The class of the marble teacher,\x01",
            "After all it is easy to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE54")

    TalkEnd(0xFE)
    Return()

    # Function_44_CD73 end

    def Function_45_CE58(): pass

    label("Function_45_CE58")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The senior class's lesson\x01",
            "After all it is difficult …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I had to pretend exactly.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_CE58 end

    def Function_46_CEAE(): pass

    label("Function_46_CEAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF7C")

    ChrTalk(
        0xFE,
        (
            "Well, today.\x01",
            "あのKeyaちゃんって子、\x01",
            "You have not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, that's right.\x01",
            "That child participates\x01",
            "Was it only natural science?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Check it, cute back look today\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_CFF3")

    label("loc_CF7C")


    ChrTalk(
        0xFE,
        (
            "いつもはKeyaちゃん、\x01",
            "I'm sitting in front of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cute head occipital\x01",
            "Watching classes while watching\x01",
            "It's quite fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFF3")

    TalkEnd(0xFE)
    Return()

    # Function_46_CEAE end

    def Function_47_CFF7(): pass

    label("Function_47_CFF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, everyone ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAunt\x01",
            "You were here.\x02\x03",
            "#00000FLater, Cecil elder sister\x01",
            "I have just come to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, it was.\x01",
            "I should go and see you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "Crossbell will be in the future\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… We, too,\x01",
            "Honestly I am perplexed … ….\x02\x03",
            "#00000FWhatever the form,\x01",
            "You are protecting the crossbells.\x01",
            "My feelings will not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F… Well, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200Fof course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWell, that kind of stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Huhu, you guys\x01",
            "I really became reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, thanks\x01",
            "I was a little anxious.\x01",
            "Thank you for calling out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 5)
    Jump("loc_D362")

    label("loc_D26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D326")

    ChrTalk(
        0xFE,
        (
            "I am here for a while\x01",
            "I will pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What will happen next?\x01",
            "I do not know but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is a goddess, surely we\x01",
            "It guides me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_D362")

    label("loc_D326")

    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "The goddess of the sky ……\x01",
            "Please protect us ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D362")

    TalkEnd(0xFE)
    Return()

    # Function_47_CFF7 end

    def Function_48_D366(): pass

    label("Function_48_D366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D378")
    Call(0, 49)
    Jump("loc_D414")

    label("loc_D378")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "部屋の中でSister · Leaseが\x01",
            "It seems that he is greeting the archbishop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F……ひとまずKeyaを迎えに行こう。\x01",
            "I should be in the classroom at Sunday school.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_D414")

    Return()

    # Function_48_D366 end

    def Function_49_D415(): pass

    label("Function_49_D415")

    EventBegin(0x0)
    Fade(500)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    SetChrPos(0x101, 49000, 0, 12340, 0)
    SetChrPos(0x102, 51000, 0, 12340, 0)
    SetChrPos(0x109, 49500, 0, 11330, 0)
    SetChrPos(0x105, 50500, 0, 11330, 0)
    SetChrFlags(0xC, 0x80)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#12P#00100FFor sure,\x01",
            "Archbishop Ellardaのお部屋よね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHmm……?\x01",
            "I can hear a voice from inside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xA, 0xFF)
    LoadChrToIndex("chr/ch11500.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    OP_68(100890, 1500, 8200, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#6P#13800F… So, from today\x01",
            "I will take care of you.\x02\x03",
            "#13803FAlthough it is a young person,\x01",
            "Hello my best regards … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P… … Wait.\x01",
            "Your name \"Argento\" is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCertainly from Alteria law country,\x01",
            "Although the appointment of a newcomer was informed,\x01",
            "No way ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#13803F……Something wrong\x01",
            "Were there any?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P………… No, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLet me be welcomed,\x01",
            "Sister · Lease。\x01",
            "Please do your best from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#13802FThank you very much.\x02\x03",
            "#13804FUnder the name of the goddess,\x01",
            "I will work diligently.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_4C(0xA, 0xFF)
    OP_D7(0x1E)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#6P#10105Fis this……\x01",
            "It is the voice of Mr. Reese earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FApparently, to the Archdiocese\x01",
            "It seems like you are greeting you as a poster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00103F……Everyone.\x01",
            "I do not like eavesdropping.\x02\x03",
            "#00100F今はKeyaちゃんを\x01",
            "Let's pick it up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#5P#00000FOh, that's right.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 50430, 0, 4030, 360)
    BeginChrThread(0xC, 0, 0, 3)
    SetScenarioFlags(0x134, 7)
    SetChrPos(0x0, 50280, 0, 12000, 180)
    EventEnd(0x5)
    Return()

    # Function_49_D415 end

    def Function_50_D912(): pass

    label("Function_50_D912")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1000, 8640, 0)
    MoveCamera(15, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(24640, 0)
    SetChrPos(0x101, 151610, 0, 8490, 90)
    SetChrPos(0x102, 151620, 0, 9490, 90)
    SetChrPos(0x109, 150550, 0, 7660, 90)
    SetChrPos(0x105, 150560, 0, 8880, 90)
    SetChrPos(0x11, 153620, 150, 9130, 270)
    SetChrSubChip(0x11, 0x1)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#11P#01105FOh, Lloyd ourselves.\x02\x03",
            "#01100FToday is class attendance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh, no way,\x01",
            "I do not mean that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FKeyaちゃん、\x01",
            "Are you studying hard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01110FYup!\x02\x03",
            "#01109FI can study various things everyday,\x01",
            "RyuやHenryたちと\x01",
            "It is fun to meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00102FHuhu, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, well qualified\x01",
            "You seem to be familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FOh, I was worried at first, but …\x01",
            "I think it was honest fear.\x02\x03",
            "#00000FKeya、しっかりがんばるんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01109FWell!\x01",
            "Lloyd's work too,\x01",
            "Do your best!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x135, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 151150, 0, 8870, 90)
    SetChrPos(0x11, 153620, 150, 9130, 0)
    SetChrSubChip(0x11, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_D912 end

    def Function_51_DBE9(): pass

    label("Function_51_DBE9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch20400.itc", 0x1E)
    SoundLoad(3598)
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9500, 0, 2500, 90)
    SetChrPos(0x102, 8750, 0, 2000, 90)
    SetChrPos(0x109, 8150, 0, 3200, 90)
    SetChrPos(0x105, 7350, 0, 2750, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5POh ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PNo, I still have lessons\x01",
            "It looks like I'm doing it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x52, 0xFF, 0xFF)
    SetChrPos(0x153, 151000, 200, 18000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 148500, 200, 18000, 90)
    OP_4B(0x8, 0xFF)
    OP_68(151000, 1600, 10500, 0)
    MoveCamera(324, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    OP_68(151000, 1600, 15500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x153,
        (
            "#01105F#5PWell, the expression here is\x01",
            "Because it becomes like this, …\x02\x03",
            "#01101F………………… (Karikari Rika)\x02\x03",
            "#01109FYes, the answer is\x01",
            "It is 512 sq. Ser!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(837, 0, 100, 0)
    SetChrName("Senior students")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4SHey!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#5PYes, it is correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PExpression development was unique, but\x01",
            "Did you think about yourself now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)

    ChrTalk(
        0x153,
        (
            "#01104F#11PWell, this way of doing\x01",
            "Because it was somewhat comfortable.\x02\x03",
            "#01110FKeya、まちがってた？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo problem.\x01",
            "It was a wonderful solution.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P── Everyone, the official is\x01",
            "To the end to draw the correct answer\x01",
            "It is only one of the guidelines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSometimes ingenuity, while enjoying\x01",
            "Please try to challenge the problem.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("Senior students")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4SYes!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9300, 0, 2200, 45)
    SetChrPos(0x102, 9100, 0, 2950, 90)
    SetChrPos(0x109, 9000, 0, 1400, 45)
    SetChrPos(0x105, 8400, 0, 2400, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F#5POh, that one ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PSunday school's\x01",
            "It's a senior class lesson …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PKeyaちゃん、凄い……\x02\x03",
            "#10106FThat problem, if I were you\x01",
            "It seems quite handy, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PIt is so-called secondary mathematics.\x02\x03",
            "#10302FHmm, pretty\x01",
            "Is not it a splendid solution?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5POh, indeed\x01",
            "うちのKeyaだよな……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5Pそうね、Keyaちゃんなら\x01",
            "Even if I could do that … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00011F#4S#1K─ ─ not!\x02",
    )


    ChrTalk(
        0x102,
        "#5P#00105F#4S#1K─ ─ not!\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWhew.\x01",
            "Be a little calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PAnd, for the time being, classes\x01",
            "Let's wait until it ends.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(151000, 1000, 13400, 0)
    MoveCamera(312, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(30000, 6000)
    SetChrPos(0x101, 147750, 0, 3750, 45)
    SetChrPos(0x102, 146400, 0, 4000, 45)
    SetChrPos(0x109, 146750, 0, 2850, 45)
    SetChrPos(0x105, 145500, 0, 3150, 45)
    SetChrPos(0x153, 151400, 0, 13400, 270)
    SetChrPos(0x8, 150600, 0, 13400, 90)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x1E, 0x4)
    ClearChrBattleFlags(0x1F, 0x4)
    ClearChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x1E, 0x17)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x18)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x1E, 150000, 0, 12000, 270)
    SetChrPos(0x1F, 150550, 0, 11100, 315)
    SetChrPos(0x20, 152000, 0, 11550, 180)
    Sleep(1000)
    FadeToBright(1000, 0)

    def lambda_E50D():
        OP_9B(0x0, 0x20, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_E50D)
    Sleep(1000)
    TurnDirection(0x1E, 0x1F, 500)
    Sleep(300)

    def lambda_E52F():
        OP_93(0x1F, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_E52F)
    Sleep(50)

    def lambda_E53F():
        OP_93(0x1E, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_E53F)
    WaitChrThread(0x1F, 2)

    def lambda_E550():
        OP_9B(0x0, 0x1F, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_E550)
    Sleep(50)
    WaitChrThread(0x1E, 2)

    def lambda_E56C():
        OP_9B(0x0, 0x1E, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_E56C)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x20, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "えっと、Keya？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_E5DC():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_E5DC)
    Sleep(50)

    def lambda_E5EC():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E5EC)
    OP_68(149000, 1000, 7700, 2000)
    MoveCamera(317, 22, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(35000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "Oh, you guys …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        (
            "#01105F#3598V#11P#30WWhy are you …?\x01",
            "Did everyone go?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0E)
    OP_C9(0x1, 0x80000000)
    OP_68(151000, 1000, 12400, 5000)
    MoveCamera(312, 25, 0, 5000)
    SetCameraDistance(30000, 5000)

    def lambda_E6B2():
        OP_95(0xFE, 151400, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6B2)
    Sleep(100)

    def lambda_E6CF():
        OP_95(0xFE, 150600, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E6CF)
    Sleep(500)

    def lambda_E6EC():
        OP_95(0xFE, 151400, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E6EC)
    Sleep(100)

    def lambda_E709():
        OP_95(0xFE, 150600, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E709)
    WaitChrThread(0x101, 1)

    def lambda_E727():
        OP_95(0xFE, 151400, 0, 11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E727)
    WaitChrThread(0x102, 1)

    def lambda_E745():
        OP_95(0xFE, 150600, 0, 11300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E745)
    WaitChrThread(0x109, 1)

    def lambda_E763():
        OP_95(0xFE, 151400, 0, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E763)
    WaitChrThread(0x105, 1)

    def lambda_E781():
        OP_95(0xFE, 150600, 0, 9800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E781)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6Pいや、Keyaが遅いから\x01",
            "I came to pick you up ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00102F#5Pそ、それよりKeyaちゃん。\x01",
            "Why are older class lessons?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#01112F#11PAh……\x02\x03",
            "#01108FEr, that 's right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PPossibly to Lloyd's\x01",
            "You do not talk about circumstances?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01106F#11P…………………… (Kokun)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PTo be aware, her academic ability is\x01",
            "It looks pretty expensive, is not it?\x02\x03",
            "#10300FFor older class lessons\x01",
            "As much as you can attach.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 350)

    ChrTalk(
        0x8,
        (
            "#11PYes, there is also hope of the principal\x01",
            "Somewhat older class from a while ago\x01",
            "I am asked to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven if it says, mathematics etc\x01",
            "I am limited to natural science.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PまさかKeyaちゃんが\x01",
            "I was smart so far … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01112F#11PEr …\x01",
            "Sorry to be sick … ….?\x02\x03",
            "#01106FKeya、まだコドモなのに\x01",
            "I studied mathematics … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PDo not you apologize, do you?\x02\x03",
            "#00002FKeyaが興味あるんだったら\x01",
            "I will not disagree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PWell … … Intellectual curiosity is\x01",
            "I want to extend it as it is.\x02\x03",
            "#00102FYes, I agree with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#11PHonto ー! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6Pただし、Ryuたちと一緒の\x01",
            "You will receive classes properly, right?\x02\x03",
            "#00000FWhat you can get at Sunday School\x01",
            "It's not just studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#11PYeah, I know!\x02\x03",
            "Ryuとpeachに、わからない所を\x01",
            "I also enjoy telling you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PWell, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#6PKeyaちゃん……\x01",
            "You are really smart, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHuhu, thanks to me too\x01",
            "It is about being helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PParticipation in senior classes\x01",
            "It is about once a week … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause I am also looking\x01",
            "Please rest assured.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x101,
        "#00002F#6PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PThank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#6PGiggle\x01",
            "It seems that the story has been settled.\x02\x03",
            "#10302FWell then before the sunset\x01",
            "Shall we return to the support section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, let's do that.\x02\x03",
            "#00000FMarble teacher.\x01",
            "Then, I will excuse you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PThank you very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0x153,
        "#01110F#12PSensei, if it is good!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PHehu, good bye.\x01",
            "Take care and return home.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x8, 150800, 200, 17500, 180)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 151000, 0, 11500, 0)
    SetScenarioFlags(0x128, 0)
    OP_29(0xA1, 0x1, 0xB)
    OP_1B(0x2, 0xFF, 0xFFFF)
    SetMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_51_DBE9 end

    def Function_52_EF84(): pass

    label("Function_52_EF84")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(150000, 1500, 10500, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    OP_68(150000, 1500, 13500, 3000)
    SetChrPos(0x101, 9300, 0, 2200, 90)
    SetChrPos(0x102, 9000, 0, 1300, 45)
    SetChrPos(0x103, 9150, 0, 3250, 135)
    SetChrPos(0x104, 8100, 0, 2700, 90)
    SetChrPos(0x109, 7250, 0, 2150, 90)
    SetChrPos(0x105, 7800, 0, 4250, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -2500, 0, 2500, 90)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(30000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005F#5PThis time is older class\x01",
            "Are there classes ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5P今日はKeyaは\x01",
            "I do not seem to have participated … …\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Dignified voice",
        "#4P─ ─ Are you guys something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_F1ED():

        label("loc_F1ED")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_F1ED")

    QueueWorkItem2(0x101, 2, lambda_F1ED)

    def lambda_F1FF():

        label("loc_F1FF")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_F1FF")

    QueueWorkItem2(0x102, 2, lambda_F1FF)

    def lambda_F211():

        label("loc_F211")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_F211")

    QueueWorkItem2(0x103, 2, lambda_F211)

    def lambda_F223():

        label("loc_F223")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_F223")

    QueueWorkItem2(0x104, 2, lambda_F223)

    def lambda_F235():

        label("loc_F235")

        TurnDirection(0x109, 0x9, 500)
        Yield()
        Jump("loc_F235")

    QueueWorkItem2(0x109, 2, lambda_F235)

    def lambda_F247():

        label("loc_F247")

        TurnDirection(0x105, 0x9, 500)
        Yield()
        Jump("loc_F247")

    QueueWorkItem2(0x105, 2, lambda_F247)
    Sleep(500)
    OP_68(7420, 1000, 2480, 4000)

    def lambda_F26D():
        OP_9B(0x0, 0x9, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_F26D)

    ChrTalk(
        0x101,
        "#00011F#12PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PArchbishop Ellarda……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PGood morning!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    ChrTalk(
        0x9,
        (
            "#5PYou guys are sure ……\x01",
            "I was a cross-border police officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PSister Marbleに用かね？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PYes.\x02\x03",
            "#00000FAbout that, plants\x01",
            "There was something I wanted to talk to.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PHm, is it a plant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PIs it medicinal herbs or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PNo, in that way\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PAnything may be listed in the scriptures\x01",
            "I can not talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHow is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHmm, if I can\x01",
            "You may listen instead instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAgain for herbs and plants in general\x01",
            "Because there is knowledge as it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F5C2")

    ChrTalk(
        0x101,
        (
            "#00002F#12POh, that's right ……\x01",
            "In the case of Lupine's grass\x01",
            "thank you for helping me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5EB")

    label("loc_F5C2")


    ChrTalk(
        0x101,
        "#00005F#12PWell, was that so?\x02",
    )

    CloseMessageWindow()

    label("loc_F5EB")


    ChrTalk(
        0x9,
        "#5PWell, if you guys are okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI am in the office.\x01",
            "You ought to call on if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(-9000, 1000, 2500, 6500)
    OP_9B(0x0, 0x9, 0x0, 0x3778, 0x8FC, 0x0)
    Sleep(250)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_F696():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_F696)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Sleep(250)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F#12PWell, hmm … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PAs usual\x01",
            "It seems to be strict … is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PBut it's no problem\x01",
            "Shall consult us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9000, 0, 2500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 6)
    OP_29(0xA6, 0x1, 0x7)
    OP_1B(0x2, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_52_EF84 end

    def Function_53_F804(): pass

    label("Function_53_F804")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    OP_68(100000, 1000, 10600, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 1500)
    SetChrPos(0x101, 100000, 0, 2500, 0)
    SetChrPos(0x102, 101200, 0, 2250, 0)
    SetChrPos(0x103, 99000, 0, 2250, 0)
    SetChrPos(0x104, 100000, 0, 500, 0)
    SetChrPos(0x109, 101000, 0, 1000, 0)
    SetChrPos(0x105, 98750, 0, 900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 100000, 100, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000F#2PExcuse me.\x01",
            "It is a person of the affairs support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh, get in.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(100000, 1000, 8500, 3000)
    MoveCamera(315, 22, 0, 3000)
    SetCameraDistance(30000, 3000)

    def lambda_F9A3():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F9A3)
    Sleep(100)

    def lambda_F9BB():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F9BB)
    Sleep(100)

    def lambda_F9D3():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F9D3)
    Sleep(100)

    def lambda_F9EB():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F9EB)
    Sleep(100)

    def lambda_FA03():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FA03)
    Sleep(100)

    def lambda_FA1B():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FA1B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11PHmm, shall we talk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt says in the scriptures\x01",
            "Do you mean plants?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo, as yet\x01",
            "Although it is not decided … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PFirst of all,\x01",
            "I will talk a little about circumstances.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(600)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#11P…… Time to empty, to feel the awareness\x01",
            "Wonderful devil … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PI reported on that before.\x01",
            "It is different from the tower and monster of the monastery … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(Oh, remember … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5P(I'd like to consult with the church before\x01",
            "You said that. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… That flower is\x01",
            "Do you have it now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, yes.\x01",
            "Light is lost … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    OP_0D()
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0x9,
        (
            "#11P#4SIt is! It is! It is!\x02\x03",
            "……this is………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001F#6PPossibly …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10107FAs I thought something! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P─ ─ ─ ─ No.\x02\x03",
            "Unfortunately, there is no idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PCome on!\x01",
            "That's it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PI do not know what you think\x01",
            "It was likely reaction, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThere is no thing without it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… What is invited from here\x01",
            "Would you wish to take over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThis is still a busy body.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PSounds like that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pああ、Sister Marbleに\x01",
            "It is useless where I heard it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven knowledgeable girl\x01",
            "You ought to know about that flower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConversely, if you know\x01",
            "It is somewhat problematic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6PWell, that is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6P…… Whatever you think\x01",
            "It is a remark of the premise you know, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo matter how I say it\x01",
            "My answer does not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven if the Guard's Sonja command\x01",
            "I will visit you directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PDamn\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(250)

    ChrTalk(
        0x102,
        (
            "#00106F#12P…… Lloyd, let's get rude.\x02\x03",
            "#00108FIt's no use asking more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P……I understood.\x02",
    )

    CloseMessageWindow()

    def lambda_101FF():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_101FF)
    Sleep(50)

    def lambda_1020F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1020F)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(200)

    ChrTalk(
        0x101,
        "#00003F#6PExcuse me, Archbishop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWell, please do not feel bad.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x6, 0x4)
    OP_68(50000, 1000, 13000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, 50000, 0, 14000, 180)
    SetChrPos(0x102, 50000, 0, 14000, 180)
    SetChrPos(0x103, 50000, 0, 14000, 180)
    SetChrPos(0x104, 50000, 0, 14000, 180)
    SetChrPos(0x109, 50000, 0, 14000, 180)
    SetChrPos(0x105, 50000, 0, 14000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 60000, 0, 3000, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_10398():
        OP_95(0x101, 50000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10398)

    def lambda_103B2():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_103B2)
    OP_68(49820, 1000, 3570, 7000)
    MoveCamera(315, 20, 0, 7000)
    OP_6E(300, 7000)
    SetCameraDistance(30000, 7000)
    Sleep(500)

    def lambda_103F4():
        OP_95(0x102, 48800, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_103F4)

    def lambda_1040E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1040E)
    Sleep(500)

    def lambda_10422():
        OP_95(0x103, 51000, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10422)

    def lambda_1043C():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1043C)
    Sleep(500)

    def lambda_10450():
        OP_95(0x104, 50000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10450)

    def lambda_1046A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_1046A)
    Sleep(500)

    def lambda_1047E():
        OP_95(0x109, 48750, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1047E)

    def lambda_10498():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10498)
    Sleep(500)

    def lambda_104AC():
        OP_95(0x105, 50000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104AC)

    def lambda_104C6():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_104C6)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x0, 0x1F4)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    def lambda_104FD():
        OP_95(0x105, 50750, 0, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104FD)
    WaitChrThread(0x101, 1)

    def lambda_1051B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1051B)
    WaitChrThread(0x102, 1)

    def lambda_1052C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1052C)
    WaitChrThread(0x103, 1)

    def lambda_1053D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1053D)
    WaitChrThread(0x104, 1)

    def lambda_1054E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1054E)
    WaitChrThread(0x109, 1)

    def lambda_1055F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1055F)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0x101, 500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#11POoooi …\x02\x03",
            "#00301FJust a little bit\x01",
            "You mean too mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PSenpai …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PBut, the atmosphere that makes you feel as though you're back\x01",
            "There was not anything in particular.\x02\x03",
            "#00208FIt is as if they hide us\x01",
            "It seems like it is right … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… probably somewhat\x01",
            "Contraindications#4Rtaboo#I wonder if there is.\x02\x03",
            "#00008FMr. Marble it, too\x01",
            "A contraindication that I do not know … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWell, as I said that way\x01",
            "I just want to know more.\x02\x03",
            "#10302FIn this way all the scriptures\x01",
            "Will you read it from scratch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBut when it comes to all the scriptures\x01",
            "It will be a huge number … …\x02\x03",
            "#00108F…… I read it a long time ago\x01",
            "I wonder which area was going down ……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    Sound(103, 0, 60, 0)

    NpcTalk(
        0xA,
        "Daughterの声",
        (
            "#1P#2S… … Maybe, in ordinary scriptures\x01",
            "Details should not be listed.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1083C():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1083C)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PHuh……\x02",
    )

    CloseMessageWindow()
    OP_68(52730, 1000, 3870, 2000)
    MoveCamera(326, 21, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)

    def lambda_1092A():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1092A)
    Sleep(0)

    def lambda_1093A():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1093A)
    Sleep(0)

    def lambda_1094A():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1094A)
    Sleep(0)

    def lambda_1095A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1095A)
    Sleep(0)

    def lambda_1096A():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1096A)
    Sleep(0)

    def lambda_1097A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1097A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_1099F():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1099F)
    OP_95(0xA, 56800, 0, 3000, 2000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5Pyou……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PRe, Lease - san …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F#12P(Shit, quietly … …)\x02\x03",
            "#04400F(… … leave the chapel as it is\x01",
            "Please come to the dormitory. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    OP_9B(0x0, 0xA, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_10A83():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_10A83)
    OP_9B(0x0, 0xA, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xA, 3)
    SetChrFlags(0xA, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(49820, 1000, 3570, 2000)
    MoveCamera(315, 20, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(300)

    def lambda_10B5D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10B5D)

    def lambda_10B6A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B6A)
    Sleep(50)

    def lambda_10B7A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10B7A)
    Sleep(50)

    def lambda_10B8A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10B8A)
    Sleep(50)

    def lambda_10B9A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10B9A)
    Sleep(50)

    def lambda_10BAA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10BAA)
    Sleep(50)

    def lambda_10BBA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10BBA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x109,
        "#10101F#5P(How, what will I do …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10CA9")

    ChrTalk(
        0x101,
        (
            "#00003F#6P(She is certainly the \"Star Cup Order\"\x01",
            "It's a story about the official … …)\x02\x03",
            "#00001F(Let's go anyhow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#5P(Yes, that is fine.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D44")

    label("loc_10CA9")


    ChrTalk(
        0x102,
        (
            "#00103F#5P(… she can trust her.\x02\x03",
            "#00101F(There seems to be something talking about\x01",
            "Let's go anyhow. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F#6P(… … Oh, I understand.\x02",
    )

    CloseMessageWindow()

    label("loc_10D44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 50000, 0, 2500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 7)
    OP_29(0xA6, 0x1, 0x8)
    OP_1B(0x4, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_53_F804 end

    def Function_54_10D89(): pass

    label("Function_54_10D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F1E")

    ChrTalk(
        0xD,
        (
            "Gee\x01",
            "It seems like you are in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Mysticon on \"Sister\" frame\x01",
            "Will you show up …? )\x02\x03",
            "#00000FExcuse me.\x01",
            "It is a little consultation … …\x02",
        )
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
        0xD,
        (
            "……Let me see……\x01",
            "No way that it takes invitation to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, I'm sorry.\x01",
            "There was work elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIs that so……\x01",
            "Then it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 2)
    Jump("loc_10F99")

    label("loc_10F1E")


    ChrTalk(
        0xD,
        (
            "I'm sorry, a bit more\x01",
            "I have a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The atmosphere called Miscon\x01",
            "I am not good at it a bit … ….\x01",
            "I refuse this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F99")

    TalkEnd(0xD)
    Return()

    # Function_54_10D89 end

    def Function_55_10F9D(): pass

    label("Function_55_10F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11217")

    ChrTalk(
        0x8,
        (
            "Gee\x01",
            "Everyone, what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Mr. Marble also\x01",
            "Sister, but …).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Surely\x01",
            "To Miscon\x01",
            "You can not invite me … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "… … Huh, perhaps … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Invite me to Miscon\x01",
            "Are you planning to give it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Such a thing\x01",
            "It is planned\x01",
            "There were rumors.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x101,
        (
            "#00012FEr, uh … ….\x01",
            "Did you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhufu, it is a joke.\x01",
            "Truly I am also old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please ask another sister.\x01",
            "I'm sure someone will help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FFuu …\x01",
            "To mr. marble\x01",
            "It does not come true.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 3)
    Jump("loc_112A0")

    label("loc_11217")


    ChrTalk(
        0x8,
        (
            "About Miscon\x01",
            "Ask another sister.\x01",
            "I'm sure someone will help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, if I am a little younger then\x01",
            "I ran for candidacy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112A0")

    TalkEnd(0x8)
    Return()

    # Function_55_10F9D end

    def Function_56_112A4(): pass

    label("Function_56_112A4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5600, 2000, 18210, 0)
    MoveCamera(339, 30, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -5140, 0, 19480, 315)
    SetChrPos(0x102, -5930, 0, 18250, 315)
    SetChrPos(0x103, -5840, 0, 17320, 315)
    SetChrPos(0x104, -5040, 0, 18120, 315)
    SetChrPos(0x109, -4230, 0, 18930, 315)
    SetChrPos(0x105, -4420, 0, 17290, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x87, 0x0)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_END)), "loc_11449")

    ChrTalk(
        0xA,
        (
            "#04405FAw, everyone.\x01",
            "Do you need something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Miscon's \"Sister\" frame … …\x01",
            "I wish she was not there? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(That's right … let's ask.)\x02\x03",
            "#00000FWell, I have consultation with Mr. Reese … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D9")

    label("loc_11449")


    ChrTalk(
        0x101,
        (
            "#00000FMr. Lease,\x01",
            "I am helping Mass.\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FYes, that is the place.\x02\x03",
            "#04400F…… To this mass,\x01",
            "Especially many visitors\x01",
            "You seem to be visiting.\x02\x03",
            "My precious place was attacked,\x01",
            "Fearfulness to be hurt ……\x02\x03",
            "#04403F…… I also understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMr. Lease ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(… … Similar things to her a long time ago\x01",
            "It may have been there. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(Between ourselves……\x01",
            "In the influence of this incident \"Seiyu\"\x01",
            "I can not decide the future movement. )\x02\x03",
            "#04403F(… … While I am in Crossbell#13R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#,\x01",
            "I will collect information as much as possible. )\x02\x03",
            "#04400F(Lloyd's, too, in the direction of trends\x01",
            "Please be careful. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(While staying ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(……I understand.\x01",
            "Please also take care of Mr. Lease. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04405Fby the way……\x01",
            "もしかしてDo you need something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FWell, well, well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Huff, it was a place to forget,\x01",
            "Miscon's \"Sister\" frame …\x01",
            "I wish she was not there? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(That's right ……\x01",
            "Let's go ask someone after we came. )\x02\x03",
            "#00000FWell, I have consultation with Mr. Reese … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)

    label("loc_118D9")

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
        (
            "#04405FMiscon … …?\x02\x03",
            "#04402FCharity event is\x01",
            "I think it's a very good thing … …\x01",
            "I am busy today.\x02\x03",
            "#04406FBesides, clerics like that\x01",
            "It is a bit of a thing to come out …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FWell, that's right, is not it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FChie, stand on stage\x01",
            "I wanted to see Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FWhatching\x01",
            "But the event itself\x01",
            "I think that it is very good.\x02\x03",
            "What other than misccon\x01",
            "Are they doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWell, other than Miscon is certain ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWith a piano concert,\x01",
            "It is a standing party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04403F…………………………\x01",
            "Everyone, in the same way with Miscon\x01",
            "May I participate?\x02",
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
        0x101,
        (
            "#00012FWell, well … it does not matter.\x02\x03",
            "#00004F(Have you been hungry for a party party …?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F(Ahaha, it looks like.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FWell, I will be back for a while\x01",
            "Because there is massage help.\x02\x03",
            "#04404FWhen the program starts\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DED")

    ChrTalk(
        0x101,
        (
            "#00003F─ ─ Now, at last\x01",
            "Participants' frame was filled.\x02\x03",
            "#00000FGo to the city hall\x01",
            "Let 's report to Roy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_11DED")

    SetScenarioFlags(0x199, 7)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5530, 0, 18650, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_56_112A4 end

    def Function_57_11E20(): pass

    label("Function_57_11E20")

    EventBegin(0x0)
    Fade(500)
    OP_68(860, 2190, 20270, 0)
    MoveCamera(319, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, -160, 500, 20710, 0)
    SetChrPos(0x102, -1330, 500, 20570, 0)
    SetChrPos(0x103, 1040, 500, 20540, 0)
    SetChrPos(0x104, -1100, 250, 19370, 0)
    SetChrPos(0x109, 60, 250, 19350, 0)
    SetChrPos(0x105, 1230, 250, 19340, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        "Oh … is it something for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you wish to preach\x01",
            "I will give you time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00005FNo.\x01",
            "そういうわけではI do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F(I wrote it on Kaito B's card\x01",
            "\"The light of the greatest goddess\" … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(570, 3200, 26250, 3000)
    MoveCamera(325, 24, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(31590, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#6P#N#00100F(Perhaps, this large\x01",
            "From stained glass\x01",
            "I think that it points to light. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#6P#N#00203F(If so, that light\x01",
            "\"Who bathes in his back\" is … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(860, 2190, 20270, 2000)
    MoveCamera(319, 24, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30010, 2000)
    Sleep(500)
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
    OP_6F(0x79)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "I do not know well what …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is something to say\x01",
            "Why do not you say it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FWell then, well then …\x02\x03",
            "#00000FArchbishop Ellarda。\x01",
            "Let me look under that teacher\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, do something suspicious\x01",
            "Do not worry because it does not do.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはArchbishop Ellardaに\x01",
            "I explained the circumstances and examined the teaching.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000Fthere were……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(470, 2000, 10610, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28510, 0)
    SetChrPos(0x101, -1250, 0, 11150, 0)
    SetChrPos(0x102, 150, 0, 11210, 315)
    SetChrPos(0x103, -2060, 0, 10100, 0)
    SetChrPos(0x104, -670, 0, 10170, 0)
    SetChrPos(0x109, 1000, 0, 10460, 315)
    SetChrPos(0x105, -1350, 0, 9170, 0)
    SetChrPos(0x9, 120, 0, 14230, 225)
    ClearMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1)
    SetChrPos(0x23, -1320, 150, 12580, 0)
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x2)
    SetChrFlags(0x23, 0x10)
    SetChrFlags(0x23, 0x20)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On the back of the trunk\x01",
            "There was a card attached.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The fourth cage is outside the city.\x01",
            "\"The western defense\x01",
            "Find a way of iron passing through your feet.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#6P#00100FThis is bell pretty\x01",
            "『ミステル』ってdollだったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHmm, it does not seem to be wrong.\x01",
            "…… Finally this is the 3 rd body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Unnoticed something like this\x01",
            "In such a place …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sometimes we had to remove the seat on demand\x01",
            "I do not think there was time to go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FTo be honest I am only a priest\x01",
            "There's no need to say it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FAlso, the person of the card\x01",
            "It looks as difficult as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F\"God#4RAiming#As you can see,\x01",
            "There should be a meaning \"a guard.\"\x02\x03",
            "#00103F\"To the west\"\x01",
            "\"The one who is in the west side of Crossbells\"\x01",
            "っていうことなんじゃI wonder if.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FAnd, that 's the \"guardian\"\x01",
            "\"Iron no Way\" passing through your feet … …?\x02\x03",
            "#10106FNo, I do not understand well yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FAlso, is it an analogy of something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, I guess that is probably the case.\x02\x03",
            "#00000FAnyway, collect this trunk\x01",
            "Let's go looking for the next one.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#11PKaito B ……\x01",
            "I was listening to the story\x01",
            "It seems to be a considerably unreasonable person.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1291C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1291C)
    Sleep(50)

    def lambda_1292C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1292C)

    ChrTalk(
        0x9,
        (
            "#11PAs a servant of a great goddess,\x01",
            "Please forgive such things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou guys, whatever\x01",
            "Please catch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FHowever, I will do my best.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iローゼンベルクdoll・Ｍ\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SetMapObjFlags(0x5, 0x4)
    SetChrFlags(0x23, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 180, 0, 10810, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, -210, 380, 23230, 180)
    OP_29(0x7A, 0x1, 0x4)
    SetScenarioFlags(0x157, 3)
    TalkEnd(0x9)
    EventEnd(0x5)
    Return()

    # Function_57_11E20 end

    SaveToFile()

Try(main)
