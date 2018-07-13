from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Sister Marble",          # 1
        "Archbishop Eralda",      # 2
        "Sister Ries",            # 3
        "Priest Genus",           # 4
        "Priest Renton",          # 5
        "Sister Hatina",          # 6
        "Trader Morgio",          # 7
        "Sister Juju",            # 8
        "Leyte",                  # 9
        "KeA",                    # 10
        "Ryｹ",                   # 11
        "Henri",                  # 12
        "Momo",                   # 13
        "Pinset",                 # 14
        "Tamil",                  # 15
        "Hamil",                  # 16
        "Coutaz",                 # 17
        "Hugott",                 # 18
        "Boy",                    # 19
        "Boy",                    # 20
        "Girl",                   # 21
        "Girl",                   # 22
        "Pluna",                  # 23
        "Lenalee",                # 24
        "Burick",                 # 25
        "Young Man",              # 26
        "Girl",                   # 27
        "Doll",                   # 28
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
        "Function_11_2FEF",        # 0B, 11
        "Function_12_3102",        # 0C, 12
        "Function_13_3500",        # 0D, 13
        "Function_14_3613",        # 0E, 14
        "Function_15_37ED",        # 0F, 15
        "Function_16_4D94",        # 10, 16
        "Function_17_63AD",        # 11, 17
        "Function_18_7644",        # 12, 18
        "Function_19_90FF",        # 13, 19
        "Function_20_9C27",        # 14, 20
        "Function_21_A07B",        # 15, 21
        "Function_22_A2AC",        # 16, 22
        "Function_23_A2DB",        # 17, 23
        "Function_24_C366",        # 18, 24
        "Function_25_C9CC",        # 19, 25
        "Function_26_CB7B",        # 1A, 26
        "Function_27_D24D",        # 1B, 27
        "Function_28_D378",        # 1C, 28
        "Function_29_D415",        # 1D, 29
        "Function_30_D533",        # 1E, 30
        "Function_31_D621",        # 1F, 31
        "Function_32_D733",        # 20, 32
        "Function_33_DA2C",        # 21, 33
        "Function_34_DC0F",        # 22, 34
        "Function_35_DDC7",        # 23, 35
        "Function_36_DEA7",        # 24, 36
        "Function_37_DF34",        # 25, 37
        "Function_38_DF79",        # 26, 38
        "Function_39_DFF8",        # 27, 39
        "Function_40_E117",        # 28, 40
        "Function_41_E18B",        # 29, 41
        "Function_42_E246",        # 2A, 42
        "Function_43_E373",        # 2B, 43
        "Function_44_E3D6",        # 2C, 44
        "Function_45_E4CF",        # 2D, 45
        "Function_46_E532",        # 2E, 46
        "Function_47_E692",        # 2F, 47
        "Function_48_EA15",        # 30, 48
        "Function_49_EADF",        # 31, 49
        "Function_50_F00A",        # 32, 50
        "Function_51_F309",        # 33, 51
        "Function_52_10758",       # 34, 52
        "Function_53_1102C",       # 35, 53
        "Function_54_12723",       # 36, 54
        "Function_55_12961",       # 37, 55
        "Function_56_12CA8",       # 38, 56
        "Function_57_13885",       # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_114A")
    Call(0, 12)
    Jump("loc_114D")

    label("loc_114A")

    Call(0, 11)

    label("loc_114D")

    Jump("loc_1422")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1364")

    ChrTalk(
        0x9,
        (
            "The "huge tree" that has appeared in the Marshlands...\x01",
            "In the Septian Church Testaments,\x01",
            "nothing of the sort is reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be some sort\x01",
            "of man made thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_132C")

    ChrTalk(
        0x105,
        (
            "#10400FWell, just leave it\x01",
            "to us for now.\x02\x03",
            "#10404FIn the case we solve the situation,\x01",
            "I'd absolutely like to request your\x01",
            "cooperation from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I will think about that, if that\x01",
            "is for Crosbell's sake, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "May the Goddess protection be with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_135C")

    label("loc_132C")


    ChrTalk(
        0x9,
        (
            "...May the Goddess\x01",
            "protection be with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135C")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1422")

    label("loc_1364")


    ChrTalk(
        0x9,
        (
            "As for that "huge tree", there is no report\x01",
            "of it in the Septian Church Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be some sort of\x01",
            "man made thing, however...\x01",
            "Let us pray the Goddess for Her protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1422")

    Jump("loc_2FEB")

    label("loc_1427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_16AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1452")
    Call(0, 12)
    Jump("loc_1455")

    label("loc_1452")

    Call(0, 11)

    label("loc_1455")

    Jump("loc_16A6")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(
        0x9,
        (
            "The present situation in Crossbell...\x01",
            "I am also one of the causes for having kept rejecting the\x01",
            "intervention of the "Congregation for the Sacraments".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I had accepted their aid,\x01",
            "it is possible that the situation\x01",
            "would have not reached this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that I too need\x01",
            "to cool down my anger and\x01",
            "take another good look at me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A6")

    label("loc_15C7")


    ChrTalk(
        0x9,
        (
            "If I had accepted the "Congregation for the Sacraments"\x01",
            "aid, it is possible that the situation would have\x01",
            "not reached this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that I too need\x01",
            "to cool down my anger and\x01",
            "take another good look at me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A6")

    Jump("loc_2FEB")

    label("loc_16AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1843")

    ChrTalk(
        0x9,
        (
            "Sister Ries has returned to\x01",
            "Arteria headquarters, hm...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...It seems that the Congregation for the Sacraments\x01",
            "too have started to move to intervene in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That could be a presage that...\x01",
            "Crossbell is on the verge of\x01",
            "embarking on troubled times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that I too, as the leader of the\x01",
            "parish of Crossbell, have to think about\x01",
            "what to do from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1943")

    label("loc_1843")


    ChrTalk(
        0x9,
        (
            "Even the Congregation for the Sacraments started\x01",
            "to move in earnest... Crossbell seem to be\x01",
            "on the verge of embarking on troubled times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that I too, as the leader of the\x01",
            "parish of Crossbell, have to think about\x01",
            "what to do from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1943")

    Jump("loc_2FEB")

    label("loc_1948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(
        0x9,
        (
            "...A little while ago, information came\x01",
            "from the Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It said that it seems the Pope Himself had approved the\x01",
            "Congregation for the Sacraments Crossbell intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be that it cannot be helped in the present\x01",
            "situation where a raid incident and so on happened...\x02",
        )
    )


    ChrTalk(
        0x9,
        (
            "However, even so...\x01",
            "I cannot approve of them,\x01",
            "who do illegal activities.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC9")

    label("loc_1AEB")


    ChrTalk(
        0x9,
        (
            "Information came saying that it seems the\x01",
            "Pope Himself had approved the Congregation for\x01",
            "the Sacraments Crossbell intervention, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, even so...\x01",
            "I cannot approve of them,\x01",
            "who do illegal activities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC9")

    Jump("loc_2FEB")

    label("loc_1BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9B")

    ChrTalk(
        0x9,
        (
            "Even now, many CGF members are being\x01",
            "exposed to danger on the Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "O Great Goddess of the Sky,\x01",
            "I beg you to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And drive back evil...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CF5")

    label("loc_1C9B")


    ChrTalk(
        0x9,
        (
            "O Great Goddess of the Sky,\x01",
            "I beg you to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And drive back evil...\x02",
    )

    CloseMessageWindow()

    label("loc_1CF5")

    Jump("loc_2FEB")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(
        0x9,
        (
            "Just a while ago, a Bracer came to get information.\x01",
            "It appears that Eolia and the other one are missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Unfortunately, they didn't come to the Cathedral.\x01",
            "Hm, I hope they are fine...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E69")

    label("loc_1DD6")


    ChrTalk(
        0x9,
        (
            "I am indebted to them for many things,\x01",
            "like supplying medicinal ingredients,\x01",
            "bodyguarding for priests and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope they are fine...\x02",
    )

    CloseMessageWindow()

    label("loc_1E69")

    Jump("loc_2FEB")

    label("loc_1E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F33")

    ChrTalk(
        0x9,
        (
            "Well then...\x01",
            "I have to program the next mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After that Cult incident, incidents are continuing...\x01",
            "I have to provide peace of mind to the\x01",
            "citizens who participate to mass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEB")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2020")

    ChrTalk(
        0x9,
        (
            "...About yesterday's flower matter,\x01",
            "I you still nosing around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In this vast continent,\x01",
            "there exist worlds that sometimes\x01",
            "you should not come in contact with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...You must not go too deep into it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20C1")

    label("loc_2020")


    ChrTalk(
        0x9,
        (
            "In this vast continent,\x01",
            "there exist worlds that sometimes\x01",
            "you should not come in contact with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You must not go too deep into it.\x01",
            "Bear that it in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C1")

    Jump("loc_2FEB")

    label("loc_20C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_2368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228E")

    ChrTalk(
        0x9,
        (
            "I have nothing I can say\x01",
            "about those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even other people in the Church...\x01",
            "Like Sister Marble, for instance,\x01",
            "should have no knowledge of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now retire.\x01",
            "I too am a busy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(As I thought, it seems the\x01",
            "Archbishop won't tell us...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Miss Ries seemed to want\x01",
            "to speak to us, so...\x01",
            "Let's try going to her for now.)\x02\x03",
            "(She should be waiting at the\x01",
            "dormitory, just out of the chapel.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2363")

    label("loc_228E")


    ChrTalk(
        0x9,
        (
            "I have nothing I can say\x01",
            "about those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now retire.\x01",
            "I too am a busy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Miss Ries should be waiting at the\x01",
            "dormitory just out of the chapel...\x01",
            "At any rate, let's try to go there.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2363")

    Jump("loc_2FEB")

    label("loc_2368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243F")

    ChrTalk(
        0x9,
        (
            "Ries Argent...\x01",
            "As I suspected, I am sure she is her younger sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph...that lot.\x01",
            "What in the world are they scheming...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(It seems he's in some deep thinking...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_247E")

    label("loc_243F")


    ChrTalk(
        0x9,
        (
            "...That damn lot.\x01",
            "What in the world are they scheming...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247E")

    Jump("loc_2FEB")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_262B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(
        0x9,
        (
            "The very day of the Trade Conference \x01",
            "plenary session... Sister Ries' business\x01",
            "trip took an awful lot of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And also, in the Mainz area\x01",
            "there are those ruins...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I understand.\x01",
            "I do not know what she was doing, but...\x01",
            "As I suspected, it seems there is no doubt.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2626")

    label("loc_25BC")


    ChrTalk(
        0x9,
        "...Oh, what could you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am researching something now.\x01",
            "Do not enter the room indiscreetly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2626")

    Jump("loc_2FEB")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2986")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2667")
    Call(0, 57)
    Return()

    label("loc_2667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2795")

    ChrTalk(
        0x9,
        (
            "Phantom Thief B... To think he hid a stolen\x01",
            "good in the sacred Crossbell Cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I heard stories about him.\x01",
            "It seems to be quite the scoundrel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As a servant of the Great Goddess,\x01",
            "I cannot forgive such a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ladies and gentlemen,\x01",
            "catch him no matter what.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2825")

    label("loc_2795")


    ChrTalk(
        0x9,
        (
            "Phantom Thief B...\x01",
            "As a servant of the Great Goddess,\x01",
            "I cannot forgive such a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ladies and gentlemen,\x01",
            "catch him no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2825")

    TalkEnd(0x9)
    Return()

    label("loc_2829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F0")

    ChrTalk(
        0x9,
        (
            "Crown Princess Klaudia came\x01",
            "to greet me some time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although young, she seems\x01",
            "to think sophisticatedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of Liberl Kingdom\x01",
            "could be said to be bright.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2981")

    label("loc_28F0")


    ChrTalk(
        0x9,
        (
            "Crown Princess Klaudia...\x01",
            "Although young, she seems\x01",
            "to think sophisticatedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of Liberl Kingdom\x01",
            "could be said to be bright.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2981")

    Jump("loc_2FEB")

    label("loc_2986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A1")
    Call(0, 14)
    Jump("loc_2A4B")

    label("loc_29A1")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "A business trip to the Mainz area...?\x01",
            "I am worried somewhat, but all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Regarding that girl, report to\x01",
            "me if something happens again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_2A4B")

    Jump("loc_2FEB")

    label("loc_2A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B71")

    ChrTalk(
        0x9,
        (
            "I received a letter from Professor\x01",
            "Ragot of St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He had results in the study which used the\x01",
            "Lupinus Grass medical herb I gave him before...\x01",
            "And so on, that's what was written in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...For all I know, I can\x01",
            "only say a "well done".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C12")

    label("loc_2B71")


    ChrTalk(
        0x9,
        (
            "I received a report from Professor\x01",
            "Ragot of St. Ursula Hospital about\x01",
            "the study I helped with before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...For all I know, I can\x01",
            "only say a "well done".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C12")

    Jump("loc_2FEB")

    label("loc_2C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C32")
    Call(0, 13)
    Jump("loc_2CB6")

    label("loc_2C32")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ries Argent, hm...?\x01",
            "Well, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sister Hatina.\x01",
            "Teach her the\x01",
            "job very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, please leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_2CB6")

    Jump("loc_2FEB")

    label("loc_2CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E00")

    ChrTalk(
        0x9,
        (
            "...Ries Argent...\x01",
            "That young girl is...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x153,
        "#01111FMr. Archbishop, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F"Ries" is that\x01",
            "Sister, right?\x02\x03",
            "#10304FHu hu, is there something you're worried about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "...It is something that has nothing to do with you all.\x01",
            "Do not mind it.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2EAA")

    label("loc_2E00")


    ChrTalk(
        0x9,
        (
            "...Ries Argent...\x01",
            "That young girl is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FIf you tummy hurts, just say it.\x01",
            "KeA will go get the emergency box for you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x153, 500)

    ChrTalk(
        0x9,
        (
            "H-Hm.\x01",
            "...Do not mind it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAA")

    Jump("loc_2FEB")

    label("loc_2EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2EBD")
    Jump("loc_2FEB")

    label("loc_2EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F76")

    ChrTalk(
        0x9,
        (
            "Welcome to the\x01",
            "Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aidios will surely reach out to those\x01",
            "who seek relief with a pious heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "May the Goddess guide you all...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2FEB")

    label("loc_2F76")


    ChrTalk(
        0x9,
        (
            "Aidios will surely reach out to those\x01",
            "who seek relief with a pious heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "May the Goddess guide you all...\x02",
    )

    CloseMessageWindow()

    label("loc_2FEB")

    TalkEnd(0x9)
    Return()

    # Function_10_111C end

    def Function_11_2FEF(): pass

    label("Function_11_2FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A1")

    ChrTalk(
        0x9,
        (
            "...To think that the situation\x01",
            "has reached such a point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe it is my responsibility for\x01",
            "having refused "their" intervention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3101")

    label("loc_30A1")


    ChrTalk(
        0x9,
        (
            "Maybe it is my responsibility for\x01",
            "having refused "their" intervention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()

    label("loc_3101")

    Return()

    # Function_11_2FEF end

    def Function_12_3102(): pass

    label("Function_12_3102")

    TurnDirection(0x9, 0x105, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "You are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FHi there, Archbishop Eralda.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...So that is how it is, hm?\x01",
            "Wazy Hemisphere,\x01",
            "you really are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Covering Sister Ries,\x01",
            "my eyes were nicely\x01",
            "deceived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Something the "Congregation\x01",
            "for the Sacraments" would think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FHu hu, regarding that matter,\x01",
            "let me apologize officially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In the matter at hand, I am\x01",
            "also at fault for having stubbornly\x01",
            "kept refusing your intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since I say that, you have\x01",
            "no reason to apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FArchbishop...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FA strict person as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FWell, considering your position,\x01",
            "I think it's unavoidable.\x02\x03",
            "#10400FHu hu, but I'll be happy if you could\x01",
            "turn a little blind eye towards out\x01",
            "activities from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FH-Hey now, Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FThat's too blunt of a request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I cannot give you an immediate reply.\x01",
            "However, I will considerate it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that I too need\x01",
            "to cool down my anger and\x01",
            "take another good look at me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 1)
    Return()

    # Function_12_3102 end

    def Function_13_3500(): pass

    label("Function_13_3500")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "...It appears that she is\x01",
            "helping out Sister Marble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Do you mean Sister Ries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, she's very quick\x01",
            "in learning the job...\x01",
            "We're being helped a lot too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm, I understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "(...Well, fine then.)\x02",
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

    # Function_13_3500 end

    def Function_14_3613(): pass

    label("Function_14_3613")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hm...\x01",
            "You entrusted Sister Ries\x01",
            "with tomorrow's business trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, it seems she hasn't started\x01",
            "Sunday School lessons yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Excuse me, Archbishop.\x01",
            "Is there something about Sister Ries...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It seems that you have been very\x01",
            "worried about her recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...No, it is nothing so important.\x01",
            "I am just worried a little\x01",
            "about the way she works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Regarding that girl, report to\x01",
            "me if something happens again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_14_3613 end

    def Function_15_37ED(): pass

    label("Function_15_37ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D8")

    ChrTalk(
        0xFE,
        (
            "Although the President has been restrained,\x01",
            "the situation surrounding Crossbell can\x01",
            "hardly be said to be optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The day when this land will be dragged\x01",
            "into war again, could be not so far...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3950")

    label("loc_38D8")


    ChrTalk(
        0xFE,
        (
            "The day when Crossbell \x01",
            "will be dragged into war\x01",
            "again, could be not so far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let us pray, to the Goddess...\x02",
    )

    CloseMessageWindow()

    label("loc_3950")

    Jump("loc_4D90")

    label("loc_3955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4D")

    ChrTalk(
        0xFE,
        (
            "The Archbishop seems to\x01",
            "feel considerably responsible\x01",
            "for this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder, since\x01",
            "he's a strict person\x01",
            "even towards himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly why I'd\x01",
            "like him to guide us as\x01",
            "he did until now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AD5")

    label("loc_3A4D")


    ChrTalk(
        0xFE,
        (
            "The Archbishop seems to\x01",
            "feel considerably responsible\x01",
            "for this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, we intend\x01",
            "to stand by Archbishop\x01",
            "Eralda.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD5")

    Jump("loc_4D90")

    label("loc_3ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0B")

    ChrTalk(
        0xFE,
        (
            "The Crossbell State independence\x01",
            "should be causing big repercussions\x01",
            "on the neighboring countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In particular, even stronger pressure\x01",
            "should be coming from the two\x01",
            "major powers from now on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will we citizens of Crossbell\x01",
            "be able to go through that,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CAB")

    label("loc_3C0B")


    ChrTalk(
        0xFE,
        (
            "From now on, further strong\x01",
            "pressure should be coming \x01",
            "from the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will we citizens of Crossbell\x01",
            "be able to go through that,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAB")

    Jump("loc_4D90")

    label("loc_3CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB2")

    ChrTalk(
        0xFE,
        (
            "Due to the previous raid attack, \x01",
            "the CGF and the townsfolk\x01",
            "suffered a lot of damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What should we do so that\x01",
            "the same incident does\x01",
            "not happen once again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell citizens\x01",
            "must think about\x01",
            "that all together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E3E")

    label("loc_3DB2")


    ChrTalk(
        0xFE,
        (
            "What should we do so that\x01",
            "the same incident does\x01",
            "not happen once again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell citizens\x01",
            "must think about\x01",
            "that all together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3E")

    Jump("loc_4D90")

    label("loc_3E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(
        0xFE,
        (
            "I wonder what has happened\x01",
            "to the citizens of Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such deed...\x01",
            "There's no way the Goddess\x01",
            "could ever forgive it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F97")

    ChrTalk(
        0xFE,
        (
            "I'm told the state of the derailment accident\x01",
            "that happened yesterday at the West \x01",
            "Crossbell Highway was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that there was no dead\x01",
            "is a blessing in disguise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_3F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4070")

    ChrTalk(
        0xFE,
        (
            "Doing the right thing in sunshine or rain...\x01",
            "It's easier said than done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda, who can strictly measure\x01",
            "not only the others, but himself too,\x01",
            "is the most respectable person to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_412A")

    ChrTalk(
        0xFE,
        (
            "The Archbishop is very rigorous towards\x01",
            "the Septian Church precepts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There're persons who say he's\x01",
            "a bigot, but, instead, I respect \x01",
            "that side of the Archbishop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_412A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_41AE")

    ChrTalk(
        0xFE,
        (
            "Oh, have you already\x01",
            "spoken to the Archbishop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm...\x01",
            "It seems it ended quite fast...\x01",
            "Has anything happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_41AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_427D")

    ChrTalk(
        0xFE,
        (
            "Recently, I'm told there have been witnesses\x01",
            "of mysterious monsters in all Crossbell lands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There has also been a notification from the CGF.\x01",
            "I'd really want to call out for an alert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_427D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435E")

    ChrTalk(
        0xFE,
        (
            "At present, the Archbishop\x01",
            "is holed up in his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that he is\x01",
            "researching Miss Ries\x01",
            "latest activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Archbishop and Miss Ries...\x01",
            "Could there be something wrong?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_438D")

    label("loc_435E")


    ChrTalk(
        0xFE,
        (
            "The Archbishop is\x01",
            "holed up in his office.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438D")

    Jump("loc_4D90")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A9")

    ChrTalk(
        0xFE,
        (
            "It appears that Crown Princess Klaudia\x01",
            "is well versed in the sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it was directly transmitted to her by\x01",
            "Captain Julia, and they say she is quite capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shouldn't say this, but you can't\x01",
            "judge a person by his appearance...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_453F")

    label("loc_44A9")


    ChrTalk(
        0xFE,
        (
            "It appears that Crown Princess Klaudia\x01",
            "is well versed in the sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shouldn't say this, but you can't\x01",
            "judge a person by his appearance...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453F")

    Jump("loc_4D90")

    label("loc_4544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_46C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463A")

    ChrTalk(
        0xFE,
        (
            "About the Trade Conference\x01",
            "result, I'm worried too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for the countries VIPs,\x01",
            "each one of them is a well-\x01",
            "known intellectual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen, I\x01",
            "can't overlook whatever\x01",
            "decisions will be taken.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46C3")

    label("loc_463A")


    ChrTalk(
        0xFE,
        (
            "About the Trade Conference\x01",
            "result, I'm worried too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen, I\x01",
            "can't overlook whatever\x01",
            "decisions will be taken.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C3")

    Jump("loc_4D90")

    label("loc_46C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_489F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480F")

    ChrTalk(
        0xFE,
        (
            "There was a strong discord between\x01",
            "the Archbishop and Professor Ragot, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently that too softened up a\x01",
            "little and he became able to read\x01",
            "at least the professor's letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears their relationships has\x01",
            "improved quite a lot from the times\x01",
            "he threw them away without reading.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_489A")

    label("loc_480F")


    ChrTalk(
        0xFE,
        (
            "Originally, Professor Ragot too was\x01",
            "a priest studying under the Archbishop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that in time, their\x01",
            "discord will disappear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_489A")

    Jump("loc_4D90")

    label("loc_489F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_494D")

    ChrTalk(
        0xFE,
        (
            "Today I'm cleaning the Cathedral\x01",
            "with the persons who are free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it's an old building...\x01",
            "If it's not periodically cleaned,\x01",
            "it gets damaged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D90")

    label("loc_494D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_4B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A53")

    ChrTalk(
        0xFE,
        (
            "senior class lessons should\x01",
            "be becoming a lot more difficult\x01",
            "than the junior class ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "KeA's understanding\x01",
            "faculties are amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FEheheh...\x01",
            "KeA's got praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, somehow that makes me proud too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B01")

    label("loc_4A53")


    ChrTalk(
        0xFE,
        (
            "KeA ends up solving smoothly\x01",
            "even problems that would\x01",
            "make an adult think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I don't watch the lessons,\x01",
            "just by hearing that I can feel\x01",
            "how amazing she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B01")

    Jump("loc_4D90")

    label("loc_4B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE8")

    ChrTalk(
        0xFE,
        (
            "It seems that Archbishop\x01",
            "Eralda is interviewing the\x01",
            "newly arrived Sister Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When he heard her name,\x01",
            "the Archbishop seemed\x01",
            "a little surprised, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, could she be\x01",
            "anyone famous?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C59")

    label("loc_4BE8")


    ChrTalk(
        0xFE,
        (
            "It seems the Archbishop\x01",
            "was a little surprised at\x01",
            "Sister Ries' name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, could she be\x01",
            "anyone famous?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C59")

    Jump("loc_4D90")

    label("loc_4C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1D")

    ChrTalk(
        0xFE,
        (
            "Mass is held periodically\x01",
            "at the Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mass is a holy function to\x01",
            "revere the Goddess of the Sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you will attend\x01",
            "when it's being held.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D90")

    label("loc_4D1D")


    ChrTalk(
        0xFE,
        (
            "Mass is a holy function to\x01",
            "revere the Goddess of the Sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you will attend\x01",
            "when it's being held.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D90")

    TalkEnd(0xFE)
    Return()

    # Function_15_37ED end

    def Function_16_4D94(): pass

    label("Function_16_4D94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E63")

    ChrTalk(
        0xFE,
        (
            "I could finally contact the\x01",
            "children in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems we'll have to monitor the\x01",
            "situation for a while for Sunday School\x01",
            "business trips, but for now I'm relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F2A")

    label("loc_4E63")


    ChrTalk(
        0xFE,
        (
            "I was able to contact the children in\x01",
            "the city and for now I'm relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I think that I will consult\x01",
            "with Sister Marble about the lessons\x01",
            "content for when Sunday School restart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F2A")

    Jump("loc_63A9")

    label("loc_4F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF8")

    ChrTalk(
        0xFE,
        (
            "For such a thing to happen while\x01",
            "we're still in a difficult situation for\x01",
            "contacting the children in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, o Goddess...\x01",
            "Please protect all the people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5030")

    label("loc_4FF8")


    ChrTalk(
        0xFE,
        (
            "Aah, o Goddess...\x01",
            "Please protect all the people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5030")

    Jump("loc_63A9")

    label("loc_5035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5179")

    ChrTalk(
        0xFE,
        (
            "Yesterday Sister Ries\x01",
            "left Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears she received a recall order\x01",
            "from the Holy Nation of Arteria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Elie, could it be...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yes, she probably received\x01",
            "orders as a "Gralsritter".)\x02\x03",
            "#00103F(As you can imagine though,\x01",
            "I don't know what could they be...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51F3")

    label("loc_5179")


    ChrTalk(
        0xFE,
        (
            "Yesterday Sister Ries\x01",
            "left Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears she received a recall order\x01",
            "from the Holy Nation of Arteria...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F3")

    Jump("loc_63A9")

    label("loc_51F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_522A")
    Call(0, 54)
    Return()

    label("loc_522A")


    ChrTalk(
        0xFE,
        (
            "At this mass we were visited by\x01",
            "quite many persons than usually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the scars the people received\x01",
            "during the raid seems to be very great...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63A9")

    label("loc_52CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D1")

    ChrTalk(
        0xFE,
        (
            "Kimmy and Alec...\x01",
            "I had just met them the day before yesterday\x01",
            "and yet they got involved in such an incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure they're having a frightening experience...\x01",
            "Aah, my Goddess, please save\x01",
            "those children, save Mainz...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5462")

    label("loc_53D1")


    ChrTalk(
        0xFE,
        (
            "I had just gone to Mainz\x01",
            "two days ago on a business\x01",
            "trip for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, my Goddess, please save\x01",
            "those children, save Mainz...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5462")

    Jump("loc_63A9")

    label("loc_5467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5475")
    Jump("loc_63A9")

    label("loc_5475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5483")
    Jump("loc_63A9")

    label("loc_5483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5491")
    Jump("loc_63A9")

    label("loc_5491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_558B")

    ChrTalk(
        0xFE,
        (
            "It seems that the senior\x01",
            "class has ended too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm also going on a business trip for \x01",
            "Sunday School tomorrow and the\x01",
            "next day to Mainz and Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to consult with Sister Marble\x01",
            "later about the lessons content.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63A9")

    label("loc_558B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_5707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5665")

    ChrTalk(
        0xFE,
        "Do you need Sister Marble?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is currently right in\x01",
            "the middle of senior class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today it seems she is teaching\x01",
            "Sister Juju how to do a lesson,\x01",
            "so maybe she'll be very busy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5702")

    label("loc_5665")


    ChrTalk(
        0xFE,
        (
            "Right now, Sister Marble is in\x01",
            "the middle of senior class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since today that is adding up\x01",
            "to Sister Juju's training too,\x01",
            "maybe she'll be very busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5702")

    Jump("loc_63A9")

    label("loc_5707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5861")

    ChrTalk(
        0xFE,
        (
            "Today it seems that Sister\x01",
            "Juju is learning how to hold\x01",
            "a lesson from Sister Marble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that having entrusted\x01",
            "Sister Ries with a business trip to\x01",
            "Mainz has been a good stimulus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her skills are clumsy, but I'm sure\x01",
            "she'll become good at it, since she has\x01",
            "the inner talent to be liked by children.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_58E0")

    label("loc_5861")


    ChrTalk(
        0xFE,
        (
            "Sister Juju has the inner talent\x01",
            "to be liked by children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure she'll become good\x01",
            "even at Sunday School lessons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E0")

    Jump("loc_63A9")

    label("loc_58E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59DD")

    ChrTalk(
        0xFE,
        (
            "Sister Ries seems to have just\x01",
            "come back from a business\x01",
            "trip for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was worried since it\x01",
            "she was a little late, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be that she was having\x01",
            "something to eat somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A6C")

    label("loc_59DD")


    ChrTalk(
        0xFE,
        (
            "Sister Ries seems to have just\x01",
            "come back from a business\x01",
            "trip for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's making a report at\x01",
            "Sister Marble's place now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6C")

    Jump("loc_5BDD")

    label("loc_5A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B77")

    ChrTalk(
        0xFE,
        (
            "Sister Ries is going on a\x01",
            "Sunday School business\x01",
            "trip to Mainz today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a calm person, but\x01",
            "she's good at teaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, it should \x01",
            "be time she came back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she missed\x01",
            "her bus stop?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BDD")

    label("loc_5B77")


    ChrTalk(
        0xFE,
        (
            "Sister Ries...\x01",
            "It should be time\x01",
            "she came back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she missed\x01",
            "her bus stop?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BDD")

    Jump("loc_63A9")

    label("loc_5BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BFD")
    Call(0, 14)
    Jump("loc_5CA6")

    label("loc_5BFD")


    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda...\x01",
            "It appears he's been very concerned\x01",
            "about Sister Ries since some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if there're some circumstances\x01",
            "we're not aware of...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA6")

    Jump("loc_63A9")

    label("loc_5CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E31")

    ChrTalk(
        0xFE,
        (
            "Since for the children of Mainz\x01",
            "and Armorica the cathedral is far,\x01",
            "they can't attend Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, the Downtown kids don't\x01",
            "come to church at all even\x01",
            "when it is lessons day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We Sisters go out to town\x01",
            "and villages to hold lessons\x01",
            "targeted at such children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, today Sister Ries\x01",
            "has gone on a business trip\x01",
            "to Downtown for us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5ECD")

    label("loc_5E31")


    ChrTalk(
        0xFE,
        (
            "Incidentally, today Sister Ries\x01",
            "has gone on a business trip\x01",
            "to Downtown for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only peculiar children are there.\x01",
            "I wonder if she's doing fine...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ECD")

    Jump("loc_63A9")

    label("loc_5ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EED")
    Call(0, 13)
    Jump("loc_5F98")

    label("loc_5EED")


    ChrTalk(
        0xFE,
        (
            "Sister Ries is very quick\x01",
            "in learning about the job...\x01",
            "She's a great help for us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda...\x01",
            "I wonder if he's concerned\x01",
            "about her for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F98")

    Jump("loc_63A9")

    label("loc_5F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_6059")

    ChrTalk(
        0xFE,
        (
            "Miss Ries appears to have\x01",
            "gone to the graveyard after\x01",
            "finishing to greet the Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Starting from tomorrow, we'll have\x01",
            "to teach her many things about the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63A9")

    label("loc_6059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_62E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6264")

    ChrTalk(
        0xFE,
        (
            "Sister Ries is a very\x01",
            "calm person with a\x01",
            "certain air about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, a very tasty-like \x01",
            "smell was coming from her...\x01",
            "What could that ever mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNow that you mention it...\x01",
            "It seemed like a bread fragrance\x01",
            "was slightly coming from Miss Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMaybe before coming here she\x01",
            "had been shopping at a bakery?\x02\x03",
            "#00109FAlthough slender, Miss\x01",
            "Ries is quite the glutton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FY-Yes...you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, I'd like to have\x01",
            "a meal with her once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62E4")

    label("loc_6264")


    ChrTalk(
        0xFE,
        (
            "Sister Ries is a very\x01",
            "calm person with a\x01",
            "certain air about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she will be a good\x01",
            "stimulus for Sister Juju.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E4")

    Jump("loc_63A9")

    label("loc_62E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_63A9")

    ChrTalk(
        0xFE,
        (
            "Actually, today a new Sister\x01",
            "is scheduled to be sent from \x01",
            "the Holy Nation of Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of person is going to come...?\x01",
            "I'm looking forward to it a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A9")

    TalkEnd(0xFE)
    Return()

    # Function_16_4D94 end

    def Function_17_63AD(): pass

    label("Function_17_63AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_644E")

    ChrTalk(
        0xC,
        (
            "People who seek help in the Church too\x01",
            "are going to keep coming one after the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have to be firmly prepared\x01",
            "and usher them in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_644E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64C5")

    ChrTalk(
        0xC,
        (
            "It seems that terrible things are\x01",
            "happening in Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I hope the citizens are safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_64C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_668B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65DE")

    ChrTalk(
        0xC,
        (
            "Crossbell national independence...\x01",
            "It's become something unimaginable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Moreover, a bank freezing of funds...\x01",
            "As a man of the Septian Church,\x01",
            "it's not something I can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We too we'll have to monitor\x01",
            "the situation for a little while...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6686")

    label("loc_65DE")


    ChrTalk(
        0xC,
        (
            "A bank freezing of funds...\x01",
            "As a man of the Septian Church,\x01",
            "it's not something I can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We too we'll have to monitor\x01",
            "the situation for a little while...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6686")

    Jump("loc_7640")

    label("loc_668B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_674C")

    ChrTalk(
        0xC,
        (
            "It seems the Testaments\x01",
            "kids took the initiative to\x01",
            "repair Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At first I didn't understand\x01",
            "what they were thinking, but...\x01",
            "It seems that deep down are good kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_674C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_67C7")

    ChrTalk(
        0xC,
        (
            "The thought that such an incident\x01",
            "can happen is incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope the people of\x01",
            "Mainz are safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_67C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6857")

    ChrTalk(
        0xC,
        (
            "Just before I eyewitnessed \x01",
            "Juju magnificently falling\x01",
            "on her bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My my, she can't quite get\x01",
            "rid of her clumsiness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_6857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_68D2")

    ChrTalk(
        0xC,
        (
            "This pedestal is often\x01",
            "used for dose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must clean it with scrupulous\x01",
            "care more than other places.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_68D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B3")

    ChrTalk(
        0xC,
        (
            "It appears that Ries is always\x01",
            "walking with the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I often happen to see her\x01",
            "with her nose in the book\x01",
            "whenever she's free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, how diligent.\x01",
            "It's a very well thing to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6A48")

    label("loc_69B3")


    ChrTalk(
        0xC,
        (
            "Ries always walk carrying\x01",
            "the Testaments with her.\x01",
            "It seems she reads when she has time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, how diligent.\x01",
            "It's a very well thing to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A48")

    Jump("loc_7640")

    label("loc_6A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_6AD7")

    ChrTalk(
        0xC,
        (
            "It appears that Ries has\x01",
            "come back from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder where she went to eat today.\x01",
            "Maybe I'll ask her later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_6AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_6B56")

    ChrTalk(
        0xC,
        "Hm, I think this can do for the cleanings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a place everyone uses.\x01",
            "It must be kept steadily clean.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_6B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C28")

    ChrTalk(
        0xC,
        (
            "While I was cleaning the office,\x01",
            "the Archbishop came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was told to leave him alone\x01",
            "since he has to research something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hm...\x01",
            "I wonder what could he be researching?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6C99")

    label("loc_6C28")


    ChrTalk(
        0xC,
        (
            "It appears that Ries too\x01",
            "has gone to the city to\x01",
            "have lunch just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Maybe I'll take some rest too.\x02",
    )

    CloseMessageWindow()

    label("loc_6C99")

    Jump("loc_7640")

    label("loc_6C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA0")

    ChrTalk(
        0xC,
        (
            "I thought that Crown Princess Klaudia\x01",
            "too would've been tense heading to\x01",
            "today's conference, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, what a surprise,\x01",
            "she was very calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected from the next Queen of Liberl...\x01",
            "She has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6E2F")

    label("loc_6DA0")


    ChrTalk(
        0xC,
        (
            "Before the conference,\x01",
            "Crown Princess Klaudia\x01",
            "was surely calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected from the next Queen of Liberl...\x01",
            "She has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2F")

    Jump("loc_7640")

    label("loc_6E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F39")

    ChrTalk(
        0xC,
        "I too was taken aback at the ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Frankly speaking, a 40 floors\x01",
            "building above ground is\x01",
            "something really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha, the next time he comes\x01",
            "to worship, I'll have to give \x01",
            "President Dieter my compliments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6FF3")

    label("loc_6F39")


    ChrTalk(
        0xC,
        (
            "I too was taken aback at the ceremony.\x01",
            "To think that there're really 40 floors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha, the next time he comes\x01",
            "to worship, I'll have to give \x01",
            "President Dieter my compliments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF3")

    Jump("loc_7640")

    label("loc_6FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7180")

    ChrTalk(
        0xC,
        (
            "Because Archbishop Eralda\x01",
            "is a very strict person, he has\x01",
            "many antagonists in the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Above all, he has a particular severe attitude \x01",
            "concerning the men of the "Congregation for\x01",
            "the Sacraments" whose activities are not clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank goodness it is rare for persons connected\x01",
            "to the Congregation for the Sacraments\x01",
            "to come to the Crossbell parish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_725B")

    label("loc_7180")


    ChrTalk(
        0xC,
        (
            "The Congregation for the Sacraments...\x01",
            "It is an organ inside the Church said to\x01",
            "manage the Goddess' sacraments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The content of their activities are not made known\x01",
            "in detail even to us common clergymen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_725B")

    Jump("loc_7640")

    label("loc_7260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7396")

    ChrTalk(
        0xC,
        (
            "SInce Miss Ries is docile-looking, I was worried\x01",
            "about her becoming familiar with everyone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems she was talking friendly\x01",
            "with Juju at yesterday's dinner turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It appears that last night they were having a lot\x01",
            "of fun chatting about good stores in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7422")

    label("loc_7396")


    ChrTalk(
        0xC,
        (
            "When it comes down to food, it seems\x01",
            "that Miss Ries talks proactively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha, it appears she has an\x01",
            "amazing passion towards food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7422")

    Jump("loc_7640")

    label("loc_7427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_74F1")

    ChrTalk(
        0xC,
        (
            "The Archbishop...after the greetings ended,\x01",
            "it seems he's been deep thinking about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder if there has been any\x01",
            "problem with Miss Ries...?\x01",
            "I doesn't seem, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_74F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_75A3")

    ChrTalk(
        0xC,
        (
            "The Archbishop interviews one\x01",
            "by one all the new priests and\x01",
            "sisters who come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As clergymen, we can't put unfit\x01",
            "persons in the cathedral, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7640")

    label("loc_75A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7640")

    ChrTalk(
        0xC,
        (
            "This is Archbishop\x01",
            "Eralda's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because rare medical plants and\x01",
            "valuable books are safekept here,\x01",
            "do not go around touching too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7640")

    TalkEnd(0xFE)
    Return()

    # Function_17_63AD end

    def Function_18_7644(): pass

    label("Function_18_7644")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_782A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7770")

    ChrTalk(
        0xFE,
        (
            "That thing appeared all of a sudden and it seems\x01",
            "my trader comrades too are all shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But no worry.\x01",
            "If we just pray to the Goddess,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come now, why don't you pray too?\x01",
            "By doing that, just about\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7825")

    label("loc_7770")


    ChrTalk(
        0xFE,
        (
            "Whatever may come,\x01",
            "if we just pray to the Goddess,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come now, why don't you pray too?\x01",
            "By doing that, just about\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7825")

    Jump("loc_90FB")

    label("loc_782A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78DA")

    ChrTalk(
        0xFE,
        (
            "I sneaked out in secret under\x01",
            "m-martial law to come to pray\x01",
            "and such a thing happens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't go back to the city.\x01",
            "What should I do...!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7933")

    label("loc_78DA")


    ChrTalk(
        0xFE,
        (
            "A-At any rate, I have to\x01",
            "pray the Goddess so that\x01",
            "the situation calms down quick...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7933")

    Jump("loc_90FB")

    label("loc_7938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A85")

    ChrTalk(
        0xFE,
        (
            "With the railway service halted,\x01",
            "it seems that the trade job is going\x01",
            "to become harder from now on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I don't intend to\x01",
            "go against the flow of society.\x01",
            "I'm sure this too is the Goddess' will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, we'll manage somehow.\x01",
            "As long as you don't forget to have a believing heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7B1E")

    label("loc_7A85")


    ChrTalk(
        0xFE,
        (
            "If you pray to the Goddess,\x01",
            "I'm sure that everything\x01",
            "is going to be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all should pray too.\x01",
            "What's important is a believing heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B1E")

    Jump("loc_90FB")

    label("loc_7B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C32")

    ChrTalk(
        0xFE,
        (
            "Recently my business was going well\x01",
            "even due to praying to the Goddess, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After such a serious incident happened,\x01",
            "frankly, I can't openly be glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Praying for my profits\x01",
            "sure is meaningless.\x01",
            "I have to pray for peace itself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7CD0")

    label("loc_7C32")


    ChrTalk(
        0xFE,
        (
            "No matter how much I profit,\x01",
            "in the situation Crossbell is in,\x01",
            "I can't openly be glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Peace itself, that's what I have\x01",
            "to pray to the Goddess for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CD0")

    Jump("loc_90FB")

    label("loc_7CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DAD")

    ChrTalk(
        0xFE,
        (
            "Actually, today I had plans to\x01",
            "stock up on Septium at Mainz...\x01",
            "To think that such a thing happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-That's right, I have to pray to the\x01",
            "Goddess for the incident to be solved...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7E31")

    label("loc_7DAD")


    ChrTalk(
        0xFE,
        (
            "No matter my business,\x01",
            "I'm worried about Mainz situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, please show the way\x01",
            "to this incident resolution...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E31")

    Jump("loc_90FB")

    label("loc_7E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_800A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F38")

    ChrTalk(
        0xFE,
        (
            "Actually, yesterday I was feeling\x01",
            "an ill omen throughout the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An when I tried to ask later,\x01",
            "hadn't a derailment\x01",
            "accident occurred?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It had no influence on my business\x01",
            "negotiations, but...honestly, that was scary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8005")

    label("loc_7F38")


    ChrTalk(
        0xFE,
        (
            "Actually, yesterday I was feeling\x01",
            "an ill omen throughout the day.\x01",
            "I was shocked at the derailment accident story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It had no influence on my business\x01",
            "negotiations, but...honestly, that was scary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8005")

    Jump("loc_90FB")

    label("loc_800A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80CA")

    ChrTalk(
        0xFE,
        (
            "I had been fervently praying to the Goddess, but...\x01",
            "Now I snapped a shoelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I have a business negotiation today...\x01",
            "Why am I be so unfortunate!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_815E")

    label("loc_80CA")


    ChrTalk(
        0xFE,
        (
            "A black cat traversed in front of me,\x01",
            "a shoelace snapped...\x01",
            "It's been nothing but ill omens since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope nothing happens, but...\x02",
    )

    CloseMessageWindow()

    label("loc_815E")

    Jump("loc_90FB")

    label("loc_8163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_830C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8270")

    ChrTalk(
        0xFE,
        (
            "...Actually, this morning a\x01",
            "black cat traversed in front of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, damn...\x01",
            "Although I have a business negotiation today,\x01",
            "isn't that an extreme bad omen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This requires to be praying more\x01",
            "conscientiously than usual...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_8307")

    label("loc_8270")


    ChrTalk(
        0xFE,
        (
            "Although I have a business negotiation today,\x01",
            "a black cat traversed in front of my eyes,\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, please exorcise\x01",
            "this bad presentiment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8307")

    Jump("loc_90FB")

    label("loc_830C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_83AF")

    ChrTalk(
        0xFE,
        (
            "...Hm, I prayed a lot, so I\x01",
            "guess it's time to go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or as I think, that's not enough praying.\x01",
            "I think I'll stay here a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FB")

    label("loc_83AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_8546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84A6")

    ChrTalk(
        0xFE,
        (
            "I'm sure that Ian Grimwood\x01",
            "came here just a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looked a little tired, but...\x01",
            "I'm sure he was healed by the holy\x01",
            "air which fills this place of worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He prayed too...\x01",
            "I'm sure he will be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8541")

    label("loc_84A6")


    ChrTalk(
        0xFE,
        (
            "I too during my trades have\x01",
            "often consulted with\x01",
            "Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked to be a little tired,\x01",
            "but he even prayed, so...\x01",
            "I'm sure he was healed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8541")

    Jump("loc_90FB")

    label("loc_8546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8689")

    ChrTalk(
        0xFE,
        (
            "All foreign countries seem to have been taking a\x01",
            "growing interest in the recent independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that my foreign trade comrades\x01",
            "too are discussing Crossbell independence\x01",
            "pros and cons on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, Crossbell visibility\x01",
            "seems to have grown even more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8743")

    label("loc_8689")


    ChrTalk(
        0xFE,
        (
            "The referendum to question the propriety\x01",
            "of the independence is upon us. \x01",
            "Also, only the Goddess knows its result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, Goddess.\x01",
            "Please, grant the best\x01",
            "choice for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8743")

    Jump("loc_90FB")

    label("loc_8748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8808")

    ChrTalk(
        0xFE,
        (
            "They say that in today's conference\x01",
            "the citizens can't attend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a pity, but...it can't be helped.\x01",
            "I'll keep praying to the Goddess\x01",
            "for the conference success here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FB")

    label("loc_8808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_89C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8907")

    ChrTalk(
        0xFE,
        (
            "I too went to see\x01",
            "Orchis Tower...\x01",
            "It was unreasonably high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's from that rooftop, it would be\x01",
            "way easier for the prayers to the\x01",
            "Goddess of the Sky to reach her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, that's something I'd\x01",
            "really want to climb.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_89BE")

    label("loc_8907")


    ChrTalk(
        0xFE,
        (
            "If it's from the Orchis Tower rooftop, it\x01",
            "would be way easier for the prayers to\x01",
            "the Goddess of the Sky to reach her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, that's something I too\x01",
            "would really want to climb.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89BE")

    Jump("loc_90FB")

    label("loc_89C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA2")

    ChrTalk(
        0xFE,
        (
            "They say that starting tomorrow,\x01",
            "economic relations are going to be\x01",
            "discusses at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To me, whose business has\x01",
            "got Crossbell as base, it's an\x01",
            "event of extreme concern.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8B29")

    label("loc_8AA2")


    ChrTalk(
        0xFE,
        (
            "For a trader, the Trade\x01",
            "Conference is very interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, I'll have to pray the\x01",
            "Goddess for the conference success,\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B29")

    Jump("loc_90FB")

    label("loc_8B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8C8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C09")

    ChrTalk(
        0xFE,
        (
            "No matter if it rains, if there's a typhoon,\x01",
            "if I have a business negotiation early in\x01",
            "the morning, every day I pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, my business\x01",
            "condition is soaring.\x01",
            "Hah hah ha...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8C85")

    label("loc_8C09")


    ChrTalk(
        0xFE,
        (
            "No matter what happens,\x01",
            "I never miss to pray every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Little and often fills the purse, they say.\x01",
            "Hah hah ha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C85")

    Jump("loc_90FB")

    label("loc_8C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_8E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF8")

    ChrTalk(
        0x153,
        (
            "#01105FAh, it's the old mister who\x01",
            "always come to pray.\x02\x03",
            "#01109FIt seems you came in the morning,\x01",
            "but you're still here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, I decided to offer\x01",
            "my prayers all day\x01",
            "during my day of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pray too, little Miss.\x01",
            "If you do that,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F...Lloyd, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(...No use asking me.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8E80")

    label("loc_8DF8")


    ChrTalk(
        0xFE,
        (
            "I decided to offer\x01",
            "my prayers all day\x01",
            "during my day of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pray too, you all.\x01",
            "If you do that,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E80")

    Jump("loc_90FB")

    label("loc_8E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_8FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F1C")

    ChrTalk(
        0xFE,
        (
            "What I have now is thanks\x01",
            "to the Goddess' blessing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must pray putting in a\x01",
            "lot of feelings of gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_8F9B")

    label("loc_8F1C")


    ChrTalk(
        0xFE,
        (
            "Aah, o Goddess of the Sky,\x01",
            "thank you for all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I beg you for your blessing\x01",
            "for the future business too...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F9B")

    Jump("loc_90FB")

    label("loc_8FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_90FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9042")

    ChrTalk(
        0xFE,
        (
            "I'm a trader, you see.\x01",
            "I try to come often here to pray\x01",
            "for the sake of my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I strongly suggest you\x01",
            "all to pray too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_90FB")

    label("loc_9042")


    ChrTalk(
        0xFE,
        (
            "Even when I prayed for business success\x01",
            "before, it really happened that it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In doing anything, first of all, pray to the\x01",
            "Goddess. If you do that, you won't mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FB")

    TalkEnd(0xFE)
    Return()

    # Function_18_7644 end

    def Function_19_90FF(): pass

    label("Function_19_90FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9110")
    Jump("loc_9C23")

    label("loc_9110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9636")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9142")
    Call(0, 56)
    Return()

    label("loc_9142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9499")

    ChrTalk(
        0x101,
        (
            "#00000FMiss Ries, it seems\x01",
            "you're helping out\x01",
            "with mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FYes, it's as you say.\x02\x03",
            "#04408F...It seems that at this\x01",
            "mass there're a great\x01",
            "many worship-visitors.\x02\x03",
            "Having your precious place attacked,\x01",
            "the fear of being injured...\x02\x03",
            "#04403F...I understand those feelings too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMiss Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(...Maybe something similar\x01",
            "happened to her too in the past.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(Just between you and me... Due to\x01",
            "the effects of this incident, the\x01",
            "Congregation for the Sacraments too\x01",
            "has not decided how to move next.)\x02\x03",
            "#04403F(...While I can stay in Crossbell, I intend to\x01",
            "gather as much information as possible.)\x02\x03",
            "#04400F(Lloyd and you all too, please\x01",
            "be careful about how you move.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(While in Crossbell...you say?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...Understood.\x01",
            "Miss Ries, be careful too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)
    Jump("loc_95B9")

    label("loc_9499")


    ChrTalk(
        0xA,
        (
            "#04400F(Due to the effects of this incident,\x01",
            "the "Congregation for the Sacraments"\x01",
            "too has not decided how to move next.)\x02\x03",
            "#04403F(...While I am in Crossbell, I intend to\x01",
            "gather as much information as possible.)\x02\x03",
            "#04400F(Lloyd and you all too, please\x01",
            "be careful about how you move.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B9")

    Jump("loc_9631")

    label("loc_95BE")


    ChrTalk(
        0xA,
        (
            "#04400FI have to help with mass\x01",
            "for a little while more.\x02\x03",
            "#04404FWhen the program starts, \x01",
            "please contact me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9631")

    Jump("loc_9C23")

    label("loc_9636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9644")
    Jump("loc_9C23")

    label("loc_9644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99D4")

    ChrTalk(
        0xA,
        (
            "#04400FYesterday's derailment accident...\x01",
            "They say a giant monster\x01",
            "was seen nearby the site.\x02\x03",
            "Everyone, do you\x01",
            "have any clue...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained in brief about\x01",
            "yesterday's accident.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405F...Pleroma Grass in\x01",
            "Knox Woodlands too...\x02\x03",
            "#04408FAlso, "Gnosis" appeared\x01",
            "again in this land...?\x02\x03",
            "#04403FI think the problem is \x01",
            ""Who gave him Gnosis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F...Didn't you figure out\x01",
            "anything on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FI am sorry, but...\x01",
            "Information related to the Cult that include\x01",
            "Gnosis haven't progressed since before.\x02\x03",
            "#04403FAs for Pleroma Grass, my\x01",
            "research is progressing, but what\x01",
            "causes it to bloom is still unknown...\x02\x03",
            "#04400FSince I was the only one who\x01",
            "could infiltrate in this land,\x01",
            "it's taking this much time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00000FThen, if you figure out anything\x01",
            "again, please contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04400FYes...understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 1)
    Jump("loc_9AB2")

    label("loc_99D4")


    ChrTalk(
        0xA,
        (
            "#04403FPleroma Grass in Knox Woodlands...\x01",
            "Also, "Gnosis" appeared\x01",
            "again in this land...\x02\x03",
            "#04400FSince I can't act in public, the\x01",
            "investigation state is unfavorable, but...\x01",
            "I'll report to you in case I find something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AB2")

    Jump("loc_9C23")

    label("loc_9AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9AC5")
    Jump("loc_9C23")

    label("loc_9AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9AD3")
    Jump("loc_9C23")

    label("loc_9AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_9AE1")
    Jump("loc_9C23")

    label("loc_9AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_9AEF")
    Jump("loc_9C23")

    label("loc_9AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9AFD")
    Jump("loc_9C23")

    label("loc_9AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9B9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B24")
    Call(0, 21)
    Jump("loc_9B9A")

    label("loc_9B24")


    ChrTalk(
        0xA,
        (
            "#04400F...Everyone, thank you\x01",
            "very much for today.\x02\x03",
            "#04403FIf something comes up again,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B9A")

    Jump("loc_9C23")

    label("loc_9B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9BAD")
    Jump("loc_9C23")

    label("loc_9BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9BBB")
    Jump("loc_9C23")

    label("loc_9BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9BFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BD6")
    Call(0, 20)
    Jump("loc_9BF9")

    label("loc_9BD6")


    ChrTalk(
        0xA,
        "#04403F(Big sister Rufina...)\x02",
    )

    CloseMessageWindow()

    label("loc_9BF9")

    Jump("loc_9C23")

    label("loc_9BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_9C0C")
    Jump("loc_9C23")

    label("loc_9C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_9C1A")
    Jump("loc_9C23")

    label("loc_9C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9C23")

    label("loc_9C23")

    TalkEnd(0xFE)
    Return()

    # Function_19_90FF end

    def Function_20_9C27(): pass

    label("Function_20_9C27")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04400F...I see, it appears that education\x01",
            "here is quite progressing.\x02\x03",
            "#04404FI think it's to be expected from\x01",
            "the most modern city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, it's true that\x01",
            "it's progressing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Children are the\x01",
            "same everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04402FRight...that could be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...By the way, Miss Ries.\x01",
            "I have one thing that has\x01",
            "been on my mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By any chance,\x01",
            "could you be Miss...\x01",
            "Rufina's younger sister?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#04405F...Did you now my big sister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, as I thought. I guessed it right\x01",
            "because you have the same surname.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the past, she helped\x01",
            "me with so many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FWas that so...?\x02\x03",
            "#04400FUhhm, SIster Marble.\x01",
            "I have a favor I'd like to ask you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, you don't have to say anything.\x01",
            "You probably are the same as her too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am indebted to Miss Rufina so\x01",
            "I won't inform the Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...However, can I suggest you only one thing?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Never overdo things, all right?\x01",
            "Even for the sake of your older sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F...I understand.\x01",
            "Thank you for your concern.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 3)
    Return()

    # Function_20_9C27 end

    def Function_21_A07B(): pass

    label("Function_21_A07B")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Miss Ries, you're a little late...\x01",
            "Could something have happened?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, your habit is\x01",
            "stained here and there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FI'm very sorry for being late.\x02\x03",
            "#04400FActually, I tripped and fell down\x01",
            "while I was coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My my, oh Miss Ries, you're\x01",
            "unexpectedly clumsy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Just because you're young, you\x01",
            "don't have to always overdo it, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400F...Thank you for your advice.\x01",
            "I'll go change now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Teacher Marble...\x01",
            "She seemed to have noticed to a certain \x01",
            "degree that something's happened.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x2, 0)
    Return()

    # Function_21_A07B end

    def Function_22_A2AC(): pass

    label("Function_22_A2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2CF")
    Call(0, 23)
    Jump("loc_A2D2")

    label("loc_A2CF")

    Call(0, 25)

    label("loc_A2D2")

    Jump("loc_A2DA")

    label("loc_A2D7")

    Call(0, 23)

    label("loc_A2DA")

    Return()

    # Function_22_A2AC end

    def Function_23_A2DB(): pass

    label("Function_23_A2DB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A5D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B4")

    ChrTalk(
        0x8,
        (
            "Lloyd, Elie...\x01",
            "There's something I want to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "KeA is...\x01",
            "Inside that tree, right?\x02",
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
        "#00005FTeacher...can you tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I presumed it by\x01",
            "looking at your\x01",
            "worried faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I don't know the details, but\x01",
            "there's just one thing I can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As KeA's guardians, you\x01",
            "must absolutely take her back.\x01",
            "...Are we clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes...absolutely!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 3)
    Jump("loc_A5CD")

    label("loc_A4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A56D")

    ChrTalk(
        0x8,
        (
            "No matter the circumstances,\x01",
            "KeA still needs you.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And it's the same\x01",
            "about KeA for you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, Elie, and everyone.\x01",
            "You must absolutely\x01",
            "take her back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A5CD")

    label("loc_A56D")


    ChrTalk(
        0x8,
        (
            "No matter the circumstances,\x01",
            "KeA still needs you.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You must absolutely\x01",
            "take her back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5CD")

    Jump("loc_C362")

    label("loc_A5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7BC")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "My, Lloyd, Elie\x01",
            "and everyone...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FTeacher Marble...\x01",
            "I'm glad you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe're very sorry to\x01",
            "have made you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, it's all right.\x01",
            "The most important thing\x01",
            "is that you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way...is KeA\x01",
            "together with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWe know where she's, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I see...I'm worried about her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...At any rate, now it's\x01",
            "a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all too, be\x01",
            "very careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 2)
    Jump("loc_A911")

    label("loc_A7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8BC")

    ChrTalk(
        0x8,
        "KeA...I'm worried about her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't seen her even once since the\x01",
            "day of that independence declaration,\x01",
            "so I've been troubling my heart too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...At any rate, now it's\x01",
            "a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all too, be\x01",
            "very careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A911")

    label("loc_A8BC")


    ChrTalk(
        0x8,
        (
            "...At any rate, now it's\x01",
            "a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all too, be\x01",
            "very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A911")

    Jump("loc_C362")

    label("loc_A916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ABEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB54")

    ChrTalk(
        0x8,
        (
            "Lloyd...\x01",
            "Is KeA all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently we haven't had Sunday School,\x01",
            "so I've become a little worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...Now that you mention it,\x01",
            "I feel like she's been a little \x01",
            "strange during the last few days.\x02\x03",
            "#00003FLike she's brooding over something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYou're right...\x01",
            "It seemed she's been very worried\x01",
            "even when we go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's probably uneasy about this situation, \x01",
            "nothing that can be done about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, as her guardian,\x01",
            "you have to properly\x01",
            "watch over her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 4)
    Jump("loc_ABE9")

    label("loc_AB54")


    ChrTalk(
        0x8,
        (
            "This situation Crossbell is in...\x01",
            "Something could be happening in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, as her guardian,\x01",
            "you have to properly\x01",
            "watch over her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABE9")

    Jump("loc_C362")

    label("loc_ABEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ADD0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC20")
    Call(0, 55)
    Return()

    label("loc_AC20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD29")

    ChrTalk(
        0x8,
        (
            "I was able to confirm that, for the time being,\x01",
            "the children who attend Sunday School are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the situation is like this,\x01",
            "lessons are on holiday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When we restart them, I would like\x01",
            "to see smiles full of energy again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_ADCB")

    label("loc_AD29")


    ChrTalk(
        0x8,
        (
            "Since the situation is like this,\x01",
            "even the Sunday School lessons\x01",
            "are on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When we restart them, I would like\x01",
            "to see smiles full of energy again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADCB")

    Jump("loc_C362")

    label("loc_ADD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_AE38")

    ChrTalk(
        0x8,
        (
            "What a terrible situation\x01",
            "it has become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope the people of\x01",
            "Mainz are safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C362")

    label("loc_AE38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AFAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF12")

    ChrTalk(
        0x8,
        (
            "Today, I had Sister Hatina go\x01",
            "for a Sunday School business\x01",
            "trip to Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that today is\x01",
            "raining on all of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope she doesn't\x01",
            "get soaked wet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AFA9")

    label("loc_AF12")


    ChrTalk(
        0x8,
        (
            "Today, I had Sister Hatina go\x01",
            "for a Sunday School business\x01",
            "trip to Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's also raining...\x01",
            "I hope she doesn't\x01",
            "get soaked wet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFA9")

    Jump("loc_C362")

    label("loc_AFAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B195")

    ChrTalk(
        0x8,
        (
            "Miss Ries had an older sister\x01",
            "called Rufina. She was an\x01",
            "acquaintance of mine too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She belonged to the "Congregation for the Sacraments" \x01",
            "and brought a solution to many different\x01",
            "incidents with her excellent negotiation skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In time she was called "Thousand Arms"\x01",
            "and became a famous person in the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Sadly, it appears that several years ago\x01",
            "she died a martyr in an unfortunate accident...\x01",
            "It's a shame a good person passed away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B233")

    label("loc_B195")


    ChrTalk(
        0x8,
        (
            "I had been indebted\x01",
            "to Miss Rufina too\x01",
            "in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wanted to express my thanks\x01",
            "to her once again, but...\x01",
            "It's a shame a good person passed away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B233")

    Jump("loc_C362")

    label("loc_B238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3FB")

    ChrTalk(
        0x8,
        (
            "Now that I think about it, Lloyd...\x01",
            "It appears that you came to\x01",
            "visit me yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you have something\x01",
            "you wanted to ask me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, regarding that we're\x01",
            "already fine.\x02\x03",
            "#00003F(It appears there's a taboo in the\x01",
            "Church regarding "Pleroma Grass"...\x01",
            "It's better not speaking about it to teacher.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is that so...?\x01",
            "All right, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I can help you any time,\x01",
            "so please, don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B480")

    label("loc_B3FB")


    ChrTalk(
        0x8,
        (
            "I too want to help out you all,\x01",
            "Lloyd, as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I can help you any time,\x01",
            "so please, don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B480")

    Jump("loc_C362")

    label("loc_B485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_B5F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4A0")
    Call(0, 27)
    Jump("loc_B5F2")

    label("loc_B4A0")


    ChrTalk(
        0x8,
        (
            "A journey of a thousand miles begins with a single step...\x01",
            "You should learn one thing at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(According to what the Archbishop\x01",
            "told us, it seems that even teacher\x01",
            "doesn't know about those Azure Flowers...)\x02\x03",
            "#00003F(As I thought, let's pay a visit\x01",
            "to Miss Ries. She should be at the\x01",
            "dormitory in front of the chapel.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5F2")

    Jump("loc_C362")

    label("loc_B5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_B7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B730")

    ChrTalk(
        0x8,
        (
            "In the autonomous state of Crossbell\x01",
            "we have a regulation that has us pay 10%\x01",
            "of revenues to the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is one of the state rules we had had since the\x01",
            "beginning of the autonomous state formation, decided \x01",
            "by the two major powers that are suzerain states...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B7E1")

    label("loc_B730")


    ChrTalk(
        0x8,
        (
            "In other words, if the independence\x01",
            "is successful, Crossbell will be freed\x01",
            "from unfair decisions from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course, it's absolutely\x01",
            "easier said than done, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E1")

    Jump("loc_C362")

    label("loc_B7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B9AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8ED")

    ChrTalk(
        0x8,
        (
            "I transmit with honesty to the children\x01",
            "what is called "utmost effort".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I do that, they will listen even to\x01",
            "difficult lessons with passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sister Juju's lessons are\x01",
            "still clumsy, but as for\x01",
            "utmost effort, she passes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B9A7")

    label("loc_B8ED")


    ChrTalk(
        0x8,
        (
            "Sister Juju's lessons are\x01",
            "still clumsy, but as for\x01",
            "utmost effort, she passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, if she adds some basic\x01",
            "teaching methods, I'm sure she'll\x01",
            "be able to make some good lessons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9A7")

    Jump("loc_C362")

    label("loc_B9AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BCE1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BA7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9D3")
    Call(0, 21)
    Jump("loc_BA76")

    label("loc_B9D3")


    ChrTalk(
        0x8,
        (
            "I think that Miss Ries' way of\x01",
            "working can't be helped, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Lloyd and you all too, just because you're\x01",
            "young, don't only overdo things, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA76")

    Jump("loc_BCDC")

    label("loc_BA7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC22")

    ChrTalk(
        0x8,
        (
            "Her Highness Klaudia seems to have \x01",
            "contributed to the resolution of the Liberl \x01",
            "phenomenon that happened a little time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the midst of such a terrible incident,\x01",
            "she held the crown princess ceremony\x01",
            "and became the next Liberl queen in line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't perceive how much\x01",
            "of a conflict brought her\x01",
            "to that point, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although young, I think she's a\x01",
            "person with an immense backbone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BCDC")

    label("loc_BC22")


    ChrTalk(
        0x8,
        (
            "It's said that Her Highness Klaudia\x01",
            "held the crown princess ceremony\x01",
            "in the midst of such a terrible incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although young, I think she's a\x01",
            "person with an immense backbone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCDC")

    Jump("loc_C362")

    label("loc_BCE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BEC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE03")

    ChrTalk(
        0x8,
        (
            "Now that I think about it, today\x01",
            "was the unveiling ceremony day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you're on a 40 floors above ground\x01",
            "structure, the children, when they look up,\x01",
            "will feel like they can reach the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I wonder if the\x01",
            "children are in high\x01",
            "spirits by now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BEC4")

    label("loc_BE03")


    ChrTalk(
        0x8,
        (
            "When you're on a 40 floors above ground\x01",
            "structure, the children, when they look up,\x01",
            "will feel like they can reach the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I wonder if the\x01",
            "children are in high\x01",
            "spirits by now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEC4")

    Jump("loc_C362")

    label("loc_BEC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C02A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB0")

    ChrTalk(
        0x8,
        (
            "Finally, the Trade Conference\x01",
            "is going to be tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It will be hard in many ways, but...\x01",
            "You all too, do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you very much,\x01",
            "teacher Marble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_C025")

    label("loc_BFB0")


    ChrTalk(
        0x8,
        (
            "It will be hard in many ways, but...\x01",
            "You all too, do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I too will cheer for\x01",
            "you from the shadows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C025")

    Jump("loc_C362")

    label("loc_C02A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C0B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C045")
    Call(0, 20)
    Jump("loc_C0AF")

    label("loc_C045")


    ChrTalk(
        0x8,
        (
            "Oh, Lloyd and you all...\x01",
            "Are you going out on such a rainy day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be careful to not\x01",
            "catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0AF")

    Jump("loc_C362")

    label("loc_C0B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_C2D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C239")
    TurnDirection(0x8, 0x153, 0)

    ChrTalk(
        0x8,
        (
            "Uh uh, KeA.\x01",
            "Look forward to the\x01",
            "next senior class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will prepare some little\x01",
            "complex problems next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYes, all right. KeA will do\x01",
            "her best and prepare!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FUuhm, she's really amazing...\x01",
            "I admire her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, eventually, she\x01",
            "could surpass us all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FUhhm, if that happens,\x01",
            "we would really lose face...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_C2CF")

    label("loc_C239")


    ChrTalk(
        0x8,
        (
            "After KeA came, the\x01",
            "senior class lessons\x01",
            "too became more lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, it appears she's having a good\x01",
            "influence on the other children too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2CF")

    Jump("loc_C362")

    label("loc_C2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_C2E2")
    Jump("loc_C362")

    label("loc_C2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2FD")
    Call(0, 24)
    Jump("loc_C362")

    label("loc_C2FD")


    ChrTalk(
        0x8,
        (
            "Uh uh, then...\x01",
            "I have to continue the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come visit again\x01",
            "on another occasion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C362")

    TalkEnd(0x8)
    Return()

    # Function_23_A2DB end

    def Function_24_C366(): pass

    label("Function_24_C366")

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
            "My, Lloyd and Elie...\x01",
            "I'm glad you came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see, teacher Marble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIt's been a long time...\x01",
            "Wait, you aren't surprised that much...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, it's because some \x01",
            "time ago KeA happily said \x01",
            ""They're baaack!".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FIf I remember correctly, you're a teacher from\x01",
            "Mr. Lloyd and Miss Elie Sunday School time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, that's right.\x01",
            "And you two seem to be the\x01",
            "new Support Section members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am a Septian Church Sister,\x01",
            "my name is Marble.\x01",
            "Nice to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, now that I think about it...\x01",
            "Noｱl, you didn't study\x01",
            "under teacher Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FNo. The East Street class \x01",
            "Fran and I attended at that\x01",
            "time was held by a Father.\x02\x03",
            "#10103FIt seems that he's\x01",
            "not in Crossbell now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, the Church priests\x01",
            "being changed is a\x01",
            "common fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, in that sense,\x01",
            "even Lloyd and Elie\x01",
            "reunion was quite lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Teacher Marbleee...\x01",
            "Don't just talk to the guys, \x01",
            "let's do the lessooon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, Ryｹ.\x01",
            "It seems they haven't seen each other\x01",
            "in time, so don't throw them a wet blanket.\x02",
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
            "My my, I'm sorry. I was happy and without\x01",
            "noticing I got caught up in the conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, then, I have to\x01",
            "continue the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come visit again\x01",
            "on another occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FW-We're sorry to have\x01",
            "disturbed your lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEehm, then,\x01",
            "excuse us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 2)
    EventEnd(0x5)
    Return()

    # Function_24_C366 end

    def Function_25_C9CC(): pass

    label("Function_25_C9CC")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAEE")

    ChrTalk(
        0xF,
        (
            "Sooo...\x01",
            "In short, about the Trade Conference\x01",
            "that was held the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It was about what they are\x01",
            "called business relationships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, I don't\x01",
            "really understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "E-Eeh, then, I'll explain\x01",
            "it from the start again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CB77")

    label("loc_CAEE")


    ChrTalk(
        0xF,
        (
            "(Uuh, this could be too complex\x01",
            "of a problem to deal with...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(B-But it's an important thing,\x01",
            "so I must teach it properly...!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB77")

    TalkEnd(0xF)
    Return()

    # Function_25_C9CC end

    def Function_26_CB7B(): pass

    label("Function_26_CB7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CB8C")
    Jump("loc_D249")

    label("loc_CB8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CB9A")
    Jump("loc_D249")

    label("loc_CB9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CBA8")
    Jump("loc_D249")

    label("loc_CBA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CCCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC32")

    ChrTalk(
        0xFE,
        (
            "On rainy days it's easy\x01",
            "to slip on the floors, so\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I just slipped\x01",
            "and fell too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CCCA")

    label("loc_CC32")


    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm really glad that today\x01",
            "Sunday School is on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the children had seen that scene,\x01",
            "I would've been made light of even more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCCA")

    Jump("loc_D249")

    label("loc_CCCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CCDD")
    Jump("loc_D249")

    label("loc_CCDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CCEB")
    Jump("loc_D249")

    label("loc_CCEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_CD79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD06")
    Call(0, 27)
    Jump("loc_CD74")

    label("loc_CD06")


    ChrTalk(
        0xFE,
        (
            "Sister Marble's teachings\x01",
            "are really useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One day, I want to become a\x01",
            "splendid teacher like her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD74")

    Jump("loc_D249")

    label("loc_CD79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_CEAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE26")

    ChrTalk(
        0xFE,
        (
            "Sister Marble's lessons\x01",
            "are very instructive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, no, I mustn't.\x01",
            "I must use her lessons as reference,\x01",
            "not to listen to them normally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CEA8")

    label("loc_CE26")


    ChrTalk(
        0xFE,
        (
            "I'm learning how to teach by\x01",
            "observing Sister Marble lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I involuntarily end\x01",
            "up getting absorbed in them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEA8")

    Jump("loc_D249")

    label("loc_CEAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFD5")

    ChrTalk(
        0xFE,
        (
            "Sooo...\x01",
            "In short, about the Trade Conference\x01",
            "that was held the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was about what they are\x01",
            "called business relationships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, I don't\x01",
            "really understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "E-Eeh, then, I'll explain\x01",
            "it from the start again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D05E")

    label("loc_CFD5")


    ChrTalk(
        0xFE,
        (
            "(Uuh, this could be too complex\x01",
            "of a problem to deal with...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(B-But it's an important thing,\x01",
            "so I must teach it properly...!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D05E")

    Jump("loc_D249")

    label("loc_D063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D071")
    Jump("loc_D249")

    label("loc_D071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D07F")
    Jump("loc_D249")

    label("loc_D07F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D08D")
    Jump("loc_D249")

    label("loc_D08D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D18A")

    ChrTalk(
        0xFE,
        (
            "It seems that Sister Ries\x01",
            "has been a Sister in \x01",
            "Arteria for some years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She seems to be about my age,\x01",
            "but she's a lot calmer than me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm ashamed to have tried to\x01",
            "act like an important-looking senior.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D21F")

    label("loc_D18A")


    ChrTalk(
        0xFE,
        (
            "*sigh*, who could have thought that\x01",
            "Sister Ries was a senior...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow I feel ashamed for having\x01",
            "rejoiced thinking I had gotten a junior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D21F")

    Jump("loc_D249")

    label("loc_D224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_D232")
    Jump("loc_D249")

    label("loc_D232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_D240")
    Jump("loc_D249")

    label("loc_D240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D249")

    label("loc_D249")

    TalkEnd(0xFE)
    Return()

    # Function_26_CB7B end

    def Function_27_D24D(): pass

    label("Function_27_D24D")

    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xF,
        (
            "Sister Marble, today\x01",
            "I learned so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Uuhm, I ended up showing\x01",
            "something pathetic during\x01",
            "senior class lesson, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, do not be worried about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A journey of a thousand miles begins with a single step...\x01",
            "You should learn one thing at a time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_27_D24D end

    def Function_28_D378(): pass

    label("Function_28_D378")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38D")
    Call(0, 50)
    Jump("loc_D411")

    label("loc_D38D")


    ChrTalk(
        0x11,
        (
            "#01100FKeA likes Sunday School a lot.\x02\x03",
            "#01109FEvery day KeA can study many things,\x01",
            "and meeting with Ryｹ and Henri is fun too.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D411")

    TalkEnd(0xFE)
    Return()

    # Function_28_D378 end

    def Function_29_D415(): pass

    label("Function_29_D415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D508")

    ChrTalk(
        0xFE,
        (
            "Uuh, studying is\x01",
            "really a pain, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Big bro, won't you study\x01",
            "instead of me for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FListen now...it's for your sake, right?\x01",
            "You should do it diligently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, you say stuff\x01",
            "like my dad does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D52F")

    label("loc_D508")


    ChrTalk(
        0xFE,
        (
            "Uuh, studying is\x01",
            "really a pain...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D52F")

    TalkEnd(0xFE)
    Return()

    # Function_29_D415 end

    def Function_30_D533(): pass

    label("Function_30_D533")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5CF")
    SetChrSubChip(0x13, 0x1)
    Sleep(500)
    SetChrSubChip(0x12, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Ryｹ, do it properly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, you'll just\x01",
            "be left behind by KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I-I know that already.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_D61D")

    label("loc_D5CF")


    ChrTalk(
        0xFE,
        (
            "I too can't only\x01",
            "tell on Ryｹ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must do my best\x01",
            "to not lose to KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D61D")

    TalkEnd(0xFE)
    Return()

    # Function_30_D533 end

    def Function_31_D621(): pass

    label("Function_31_D621")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D708")
    OP_63(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x14)

    ChrTalk(
        0xFE,
        "Uhhm, eehm...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x14, 0x1)
    Sleep(500)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Say, KeA...\x01",
            "What should I do in this point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01100FLet's see, to calculate this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha...\x01",
            "It seems they're getting along well.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_D72F")

    label("loc_D708")


    ChrTalk(
        0xFE,
        (
            "I-I see...\x01",
            "I should do like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D72F")

    TalkEnd(0xFE)
    Return()

    # Function_31_D621 end

    def Function_32_D733(): pass

    label("Function_32_D733")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9C0")

    ChrTalk(
        0x101,
        (
            "#00000FHi Pinset.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, you're bis\x01",
            "sis Wendy's\x01",
            "friend, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Long time no see, thank you\x01",
            "for all the hard work you do.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_END)), "loc_D881")

    ChrTalk(
        0x105,
        "#10305FWendy? Isn't she...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, she's the orbal store engineer\x01",
            "who we met some time ago.\x02\x03",
            "#00109F*giggle*, she's Lloyd childhood friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8F4")

    label("loc_D881")


    ChrTalk(
        0x105,
        "#10305FWendy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe engineer at\x01",
            "the orbal store.\x02\x03",
            "#00109F*giggle*, she's Lloyd childhood friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8F4")


    ChrTalk(
        0xFE,
        (
            "Right, that mecha geek\x01",
            "is my big sis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FT-That's quite the way to speak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that's true.\x01",
            "Big brother here thinks that too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(...It's true, I can't deny it.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 1)
    Jump("loc_DA28")

    label("loc_D9C0")


    ChrTalk(
        0xFE,
        (
            "It was father's influence\x01",
            "that turned big sis into a\x01",
            "mecha geek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll never end\x01",
            "up like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA28")

    TalkEnd(0xFE)
    Return()

    # Function_32_D733 end

    def Function_33_DA2C(): pass

    label("Function_33_DA2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DA3D")
    Jump("loc_DC0B")

    label("loc_DA3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DAB7")

    ChrTalk(
        0xFE,
        "Today there's mass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We too do nothing but playing around,\x01",
            "but at times like this, we must behave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC0B")

    label("loc_DAB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DAC5")
    Jump("loc_DC0B")

    label("loc_DAC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DAD3")
    Jump("loc_DC0B")

    label("loc_DAD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DAE1")
    Jump("loc_DC0B")

    label("loc_DAE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DAEF")
    Jump("loc_DC0B")

    label("loc_DAEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_DAFD")
    Jump("loc_DC0B")

    label("loc_DAFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_DB0B")
    Jump("loc_DC0B")

    label("loc_DB0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DB19")
    Jump("loc_DC0B")

    label("loc_DB19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DB27")
    Jump("loc_DC0B")

    label("loc_DB27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DB35")
    Jump("loc_DC0B")

    label("loc_DB35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DB43")
    Jump("loc_DC0B")

    label("loc_DB43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DB51")
    Jump("loc_DC0B")

    label("loc_DB51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_DB5F")
    Jump("loc_DC0B")

    label("loc_DB5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_DB6D")
    Jump("loc_DC0B")

    label("loc_DB6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DC0B")

    ChrTalk(
        0xFE,
        (
            "Tch, that Hamil, recently he was\x01",
            "fired up saying that he wanted\x01",
            "to show KeA how good he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I prefer playing outside\x01",
            "rather than studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC0B")

    TalkEnd(0xFE)
    Return()

    # Function_33_DA2C end

    def Function_34_DC0F(): pass

    label("Function_34_DC0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DC20")
    Jump("loc_DDC3")

    label("loc_DC20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DC72")

    ChrTalk(
        0xFE,
        (
            "Goddess...\x01",
            "Please keep in health\x01",
            "all the people of the city...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC3")

    label("loc_DC72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DC80")
    Jump("loc_DDC3")

    label("loc_DC80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DC8E")
    Jump("loc_DDC3")

    label("loc_DC8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DC9C")
    Jump("loc_DDC3")

    label("loc_DC9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DCAA")
    Jump("loc_DDC3")

    label("loc_DCAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_DCB8")
    Jump("loc_DDC3")

    label("loc_DCB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_DCC6")
    Jump("loc_DDC3")

    label("loc_DCC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DCD4")
    Jump("loc_DDC3")

    label("loc_DCD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DCE2")
    Jump("loc_DDC3")

    label("loc_DCE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DCF0")
    Jump("loc_DDC3")

    label("loc_DCF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DCFE")
    Jump("loc_DDC3")

    label("loc_DCFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DD0C")
    Jump("loc_DDC3")

    label("loc_DD0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_DD1A")
    Jump("loc_DDC3")

    label("loc_DD1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_DD28")
    Jump("loc_DDC3")

    label("loc_DD28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DDC3")

    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "KeA is cute...\x01",
            "I'm happy I can study with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, I'll have to raise my hand a lot\x01",
            "and answer a question after the other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC3")

    TalkEnd(0xFE)
    Return()

    # Function_34_DC0F end

    def Function_35_DDC7(): pass

    label("Function_35_DDC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE64")

    ChrTalk(
        0xFE,
        (
            "I like shopping and\x01",
            "I have a interest into\x01",
            "economics, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The recent Trade Conference\x01",
            "is still something difficult for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DEA3")

    label("loc_DE64")


    ChrTalk(
        0xFE,
        (
            "The Trade Conference is\x01",
            "still something difficult for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEA3")

    TalkEnd(0xFE)
    Return()

    # Function_35_DDC7 end

    def Function_36_DEA7(): pass

    label("Function_36_DEA7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder if big brother Azel would\x01",
            "understand this conversation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll try asking him\x01",
            "the next time he comes home.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_DEA7 end

    def Function_37_DF34(): pass

    label("Function_37_DF34")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Yes, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...As I thought, I don't really get it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_DF34 end

    def Function_38_DF79(): pass

    label("Function_38_DF79")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*yaaawn*...\x01",
            "When I study I get sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the Sister is doing her best,\x01",
            "so I have to listen to her properly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_DF79 end

    def Function_39_DFF8(): pass

    label("Function_39_DFF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E09A")

    ChrTalk(
        0xFE,
        (
            "H-Hmm...\x01",
            "Trade Conference, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This thing is common sense.\x01",
            "It's too easy that's laughable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...R-Really?\x01",
            "You really get it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E113")

    label("loc_E09A")


    ChrTalk(
        0xFE,
        (
            "Something like a Trade Conference\x01",
            "is common sense. Easy stuff, easy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Enough, get away!\x01",
            "I'm studying here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E113")

    TalkEnd(0xFE)
    Return()

    # Function_39_DFF8 end

    def Function_40_E117(): pass

    label("Function_40_E117")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For your future's sake, you must study\x01",
            "properly even complicated things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Misters, are studying?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_E117 end

    def Function_41_E18B(): pass

    label("Function_41_E18B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_E1E3")

    ChrTalk(
        0xFE,
        "Say, where do we go now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To the department store like usual?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E242")

    label("loc_E1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_E242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1FE")
    Call(0, 42)
    Jump("loc_E242")

    label("loc_E1FE")


    ChrTalk(
        0xFE,
        (
            "(Lenalee...\x01",
            "Didn't she got mad at me\x01",
            "too because of youuu...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E242")

    TalkEnd(0xFE)
    Return()

    # Function_41_E18B end

    def Function_42_E246(): pass

    label("Function_42_E246")


    ChrTalk(
        0x1F,
        (
            "I wonder if the Sister\x01",
            "knows a simple diet\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Hey, quit asking me\x01",
            "stupid things\x01",
            "during lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "She'll get mad at us again, you know?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Uh uh, you two there.\x01",
            "Be quiet during lessons.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "Yeees....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Y-Yeees...\x01",
            "(She got mad at me too...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_42_E246 end

    def Function_43_E373(): pass

    label("Function_43_E373")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_E3A5")

    ChrTalk(
        0xFE,
        "We aren't really tired, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3D2")

    label("loc_E3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_E3D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C0")
    Call(0, 42)
    Jump("loc_E3D2")

    label("loc_E3C0")


    ChrTalk(
        0xFE,
        "(S-Sorry...)\x02",
    )

    CloseMessageWindow()

    label("loc_E3D2")

    TalkEnd(0xFE)
    Return()

    # Function_43_E373 end

    def Function_44_E3D6(): pass

    label("Function_44_E3D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_E470")

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad that today we\x01",
            "learned about "independence".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There're even things you can't get\x01",
            "by only reading Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4CB")

    label("loc_E470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_E4CB")

    ChrTalk(
        0xFE,
        "I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Teacher Marble's lessons\x01",
            "are really easy to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4CB")

    TalkEnd(0xFE)
    Return()

    # Function_44_E3D6 end

    def Function_45_E4CF(): pass

    label("Function_45_E4CF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "As expected, senior class\x01",
            "lessons are difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should've prepared decently.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_E4CF end

    def Function_46_E532(): pass

    label("Function_46_E532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E616")

    ChrTalk(
        0xFE,
        (
            "Oh, that child called\x01",
            "KeA is not coming\x01",
            "today, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aah, now that I think about\x01",
            "it, that child only attends\x01",
            "natural sciences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, I wanted to gaze at her cute\x01",
            "figure from behind today too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E68E")

    label("loc_E616")


    ChrTalk(
        0xFE,
        (
            "KeA always sits\x01",
            "in front of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking classes while gazing\x01",
            "at her cute back of the head\x01",
            "is pretty enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E68E")

    TalkEnd(0xFE)
    Return()

    # Function_46_E532 end

    def Function_47_E692(): pass

    label("Function_47_E692")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E921")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAunt...\x01",
            "You were here?\x02\x03",
            "#00000FSister Cecil just came to the\x01",
            "Support Section moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, is that so?\x01",
            "I must go see her later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "I wonder what will be of\x01",
            "Crossbell from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Honestly speaking,\x01",
            "we too are at sea, but...\x02\x03",
            "#00000FWhatever shape Crossbell\x01",
            "will take, it doesn't change\x01",
            "the feeling of protecting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F...Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FNaturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWell, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Uh uh, you all have become\x01",
            "really dependable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, thanks to you, I'm\x01",
            "feeling a little bit relieved.\x01",
            "Thank you for talking to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 5)
    Jump("loc_EA11")

    label("loc_E921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9D4")

    ChrTalk(
        0xFE,
        (
            "I am going to stay here for\x01",
            "a little longer to pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't now what will\x01",
            "happen in the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure that the\x01",
            "Goddess will guide us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_EA11")

    label("loc_E9D4")

    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "O Goddess of the Sky...\x01",
            "Please protect us all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA11")

    TalkEnd(0xFE)
    Return()

    # Function_47_E692 end

    def Function_48_EA15(): pass

    label("Function_48_EA15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA27")
    Call(0, 49)
    Jump("loc_EADE")

    label("loc_EA27")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears that Sister Ries is greeting\x01",
            "the Archbishop inside the room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F...Let's go pick up KeA for now.\x01",
            "She should be in the Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_EADE")

    Return()

    # Function_48_EA15 end

    def Function_49_EADF(): pass

    label("Function_49_EADF")

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
            "#12P#00100FIf I remember correctly, this place\x01",
            "is Archbishop Eralda's room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHm...?\x01",
            "You can hear voices coming from inside.\x02",
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
            "#6P#13800F...And so, starting today,\x01",
            "I will be in your care.\x02\x03",
            "#13803FI may be inexperienced, but I am \x01",
            "looking forward to your support...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Wait.\x01",
            "Your surname, "Argent"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's true that it was by the Holy Nation\x01",
            "of Arteria that a newcomer had been\x01",
            "appointed, but who could have thought...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#13803F...Is there any\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...No, there's no one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLet me welcome you,\x01",
            "Sister Ries.\x01",
            "Do your best from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#13802FThank you very much.\x02\x03",
            "#13804FI will work responsibly under\x01",
            "the name of the Goddess.\x02",
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
            "#6P#10105FThat's... Miss Ries' voice.\x01",
            "We met her some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIt appears she's making her\x01",
            "greetings to the Archbishop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00103F...Everyone.\x01",
            "Eavesdropping is not nice.\x02\x03",
            "#00100FLet's go pick\x01",
            "up KeA now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#5P#00000FYeah, you're right.\x02",
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

    # Function_49_EADF end

    def Function_50_F00A(): pass

    label("Function_50_F00A")

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
            "#11P#01105FAh, guys.\x02\x03",
            "#01100FWas today parents' day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh, no,\x01",
            "that's not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FKeA, are you doing\x01",
            "your best studying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01110FYes!\x02\x03",
            "#01109FEvery day KeA can study many things,\x01",
            "and meeting with Ryｹ, Henri and the\x01",
            "others is fun too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00102F*giggle*, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHmm, she seems to be\x01",
            "quite familiar here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FYes, we were worried at first, but...\x01",
            "Honestly, I think it was a needless anxiety.\x02\x03",
            "#00000FKeA, continue to do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01109FYes!\x01",
            "You all do your best with\x01",
            "your work too, Lloyd!\x02",
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

    # Function_50_F00A end

    def Function_51_F309(): pass

    label("Function_51_F309")

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
        "#00005F#5POh...?\x02",
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
            "#00008F#5PWell, they're still\x01",
            "holding classes──\x02",
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
            "#01105F#5PEehm, so this formula becomes\x01",
            "like this, and after that...\x02\x03",
            "#01101F............(*scrib scrib scrib*)\x02\x03",
            "#01109FHere it is, the answer\x01",
            "is 512 square selge!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(837, 0, 100, 0)
    SetChrName("Seniors")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4SOooh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#5PYes, it's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe formula development was unique though,\x01",
            "did you think about it yourself now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)

    ChrTalk(
        0x153,
        (
            "#01104F#11PEheheh, somehow I felt that\x01",
            "doing it this way was good.\x02\x03",
            "#01110FWas KeA wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, no.\x01",
            "That was a very amazing way to solve it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P──Everyone, an official formula\x01",
            "is just one guideline to derive\x01",
            "the correct solution, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAt times, please try to devise something\x01",
            "and challenge problems while having fun.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("Seniors")
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
        "#00001F#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PA Sunday School lesson\x01",
            "of senior class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PKeA is amazing...\x02\x03",
            "#10106FIf it had been me, I would've had\x01",
            "much trouble with that problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PThat's what they call second grade math.\x02\x03",
            "#10302FThat's quite the splendid\x01",
            "way to solve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, nothing less expected\x01",
            "from our KeA, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PRight, that level of math\x01",
            "is nothing for KeA...\x02",
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
        "#6P#00011F#4S#1K──That's not it!\x02",
    )


    ChrTalk(
        0x102,
        "#5P#00105F#4S#1K──That's not it!\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10306F#5POh boy.\x01",
            "Calm down a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PI-In any case, let's wait\x01",
            "for the lesson to be over.\x02",
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

    def lambda_FC8F():
        OP_9B(0x0, 0x20, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_FC8F)
    Sleep(1000)
    TurnDirection(0x1E, 0x1F, 500)
    Sleep(300)

    def lambda_FCB1():
        OP_93(0x1F, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_FCB1)
    Sleep(50)

    def lambda_FCC1():
        OP_93(0x1E, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_FCC1)
    WaitChrThread(0x1F, 2)

    def lambda_FCD2():
        OP_9B(0x0, 0x1F, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_FCD2)
    Sleep(50)
    WaitChrThread(0x1E, 2)

    def lambda_FCEE():
        OP_9B(0x0, 0x1E, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_FCEE)
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
        "Ehm, KeA?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_FD57():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_FD57)
    Sleep(50)

    def lambda_FD67():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FD67)
    OP_68(149000, 1000, 7700, 2000)
    MoveCamera(317, 22, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(35000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        (
            "#01105F#3598V#11P#30WOh...?\x01",
            "What's wrong guys?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0E)
    OP_C9(0x1, 0x80000000)
    OP_68(151000, 1000, 12400, 5000)
    MoveCamera(312, 25, 0, 5000)
    SetCameraDistance(30000, 5000)

    def lambda_FE24():
        OP_95(0xFE, 151400, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE24)
    Sleep(100)

    def lambda_FE41():
        OP_95(0xFE, 150600, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE41)
    Sleep(500)

    def lambda_FE5E():
        OP_95(0xFE, 151400, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FE5E)
    Sleep(100)

    def lambda_FE7B():
        OP_95(0xFE, 150600, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FE7B)
    WaitChrThread(0x101, 1)

    def lambda_FE99():
        OP_95(0xFE, 151400, 0, 11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE99)
    WaitChrThread(0x102, 1)

    def lambda_FEB7():
        OP_95(0xFE, 150600, 0, 11300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEB7)
    WaitChrThread(0x109, 1)

    def lambda_FED5():
        OP_95(0xFE, 151400, 0, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FED5)
    WaitChrThread(0x105, 1)

    def lambda_FEF3():
        OP_95(0xFE, 150600, 0, 9800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FEF3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, since you were late\x01",
            "we came to pick you up, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00102F#5PM-More importantly, KeA.\x01",
            "Why are you in a senior class lesson?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#01112F#11PAh...\x02\x03",
            "#01108FEhm, well...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PCould it be that you haven't told\x01",
            "about it to Lloyd and the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01106F#11P............(*nod*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PI presume that her scholarship\x01",
            "is pretty high, eh?\x02\x03",
            "#10300FSo much she can keep up\x01",
            "with senior class lessons.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 350)

    ChrTalk(
        0x8,
        (
            "#11PYes, she wanted to so I've\x01",
            "been letting her attend senior\x01",
            "class too since a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAlthough limited to mathematics\x01",
            "and natural sciences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PTo think that KeA\x01",
            "was that smart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01112F#11PEhm...\x01",
            "Sorry for not telling you...?\x02\x03",
            "#01106FKeA is still a child and yet\x01",
            "she studies math and so on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, there's nothing to apologize for, you know?\x02\x03",
            "#00002FIf you have an interest for those,\x01",
            "I won't be contrary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PRight... I'd like you to grow your\x01",
            "intellectual curiosity like that.\x02\x03",
            "#00102FYes, I agree too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#11PReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHowever, you have to properly take the\x01",
            "classes with Ryｹ and the others too, ok?\x02\x03",
            "#00000FWhat you acquire in Sunday School\x01",
            "is not only knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#11PYes, I know!\x02\x03",
            "It's also fun to teach Ryｹand Momo what they don't get!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#6PKeA...\x01",
            "She's really smart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUh uh, thanks to her,\x01",
            "I am being helped too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PShe will take senior\x01",
            "class once a week...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI will be watching over her\x01",
            "too, so please don't worry.\x02",
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
        "#00104F#6PPlease take care of her.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#6PHu hu... I'm glad an\x01",
            "agreement was reached.\x02\x03",
            "#10302FThen, should be go back to the Support\x01",
            "Section at once before the sun sets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, let's.\x02\x03",
            "#00000FTeacher Marble.\x01",
            "Please excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PThank you for all your efforts.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0x153,
        "#01110F#12PTeacher, byyye!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PUh uh, goodbye.\x01",
            "Be careful on the way back.\x02",
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

    # Function_51_F309 end

    def Function_52_10758(): pass

    label("Function_52_10758")

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
            "#00005F#5PIs there senior class \x01",
            "lessons at this hour...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5PIt seems that KeA is\x01",
            "not attending today...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Majestic Voice",
        "#4P──You all, do you need something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_109D6():

        label("loc_109D6")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_109D6")

    QueueWorkItem2(0x101, 2, lambda_109D6)

    def lambda_109E8():

        label("loc_109E8")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_109E8")

    QueueWorkItem2(0x102, 2, lambda_109E8)

    def lambda_109FA():

        label("loc_109FA")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_109FA")

    QueueWorkItem2(0x103, 2, lambda_109FA)

    def lambda_10A0C():

        label("loc_10A0C")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_10A0C")

    QueueWorkItem2(0x104, 2, lambda_10A0C)

    def lambda_10A1E():

        label("loc_10A1E")

        TurnDirection(0x109, 0x9, 500)
        Yield()
        Jump("loc_10A1E")

    QueueWorkItem2(0x109, 2, lambda_10A1E)

    def lambda_10A30():

        label("loc_10A30")

        TurnDirection(0x105, 0x9, 500)
        Yield()
        Jump("loc_10A30")

    QueueWorkItem2(0x105, 2, lambda_10A30)
    Sleep(500)
    OP_68(7420, 1000, 2480, 4000)

    def lambda_10A56():
        OP_9B(0x0, 0x9, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10A56)

    ChrTalk(
        0x101,
        "#00011F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PArchbishop Eralda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PG-Good evening!\x02",
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
            "#5PIf I remember correctly...\x01",
            "You're from the Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PDo you need Sister Marble?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PY-Yes.\x02\x03",
            "#00000FUhhm, we would like to consult\x01",
            "with her about a certain plant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PHm, a plant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PIs that a medical herb?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PNo, it's not\x01",
            "the case, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PIt appears that plant could be\x01",
            "showing up in the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POoh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHm, then you can ask\x01",
            "me in her stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI may not look like it, but I'm knowledgeable\x01",
            "about medical herbs and plants in general.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10DED")

    ChrTalk(
        0x101,
        (
            "#00002F#12PAh, now that you mention it...\x01",
            "You really helped us out\x01",
            "with the Lupinus Grass case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E0B")

    label("loc_10DED")


    ChrTalk(
        0x101,
        "#00005F#12PI-Is that so?\x02",
    )

    CloseMessageWindow()

    label("loc_10E0B")


    ChrTalk(
        0x9,
        "#5PWell, if you want, that is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI'll be retiring in my office.\x01",
            "If you like, come visit me.\x02",
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

    def lambda_10EBC():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10EBC)
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
        "#00001F#12PU-Uhhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PA strict-looking person\x01",
            "as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PBut since we're here, why don't\x01",
            "we try consulting with him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#11P............\x02",
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

    # Function_52_10758 end

    def Function_53_1102C(): pass

    label("Function_53_1102C")

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
            "#00000F#2P──Pardon us. We're from the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PAah, come in.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(100000, 1000, 8500, 3000)
    MoveCamera(315, 22, 0, 3000)
    SetCameraDistance(30000, 3000)

    def lambda_111D7():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_111D7)
    Sleep(100)

    def lambda_111EF():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_111EF)
    Sleep(100)

    def lambda_11207():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11207)
    Sleep(100)

    def lambda_1121F():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1121F)
    Sleep(100)

    def lambda_11237():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11237)
    Sleep(100)

    def lambda_1124F():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1124F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11PHm, so let's hear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAbout that plant that\x01",
            "appears in the Testaments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo, that's not\x01",
            "confirmed yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PFirst, we'll tell you what\x01",
            "has happened up to now.\x02",
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
            "#11P...Mysterious monsters\x01",
            "familiar with time and space...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PThey're also different from the monsters of the \x01",
            "Tower and Temple we previously reported about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(Ah, now that she mentions it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5P(She said that they tried to\x01",
            "consult with the Church before.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Those "flowers"...\x01",
            "Do you have them with you now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAh, yes.\x01",
            "They lost their light, but...\x02",
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
            "#11P#4S!!!\x02\x03",
            "...These are...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001F#6PCould it be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10107FAs we thought, do you know something!?\x02",
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
            "#11P──No.\x02\x03",
            "Unfortunately, I have no idea.\x02",
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
        "#00011F#6PEeh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey now!\x01",
            "How come!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PNo matter how we consider that reaction,\x01",
            "it seemed you had some clue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI don't have any.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...I was the one who called you,\x01",
            "but I'll ask you to leave now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PEven if it doesn't seem, I'm a busy person.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PN-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAh, it will also be useless\x01",
            "asking Sister Marble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlthough an extremely knowledgeable woman, \x01",
            "she probably won't know those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConversely, if she knew about them,\x01",
            "that could be somewhat of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6PY-You mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6P...That's a statement that presumes\x01",
            "you know about them, you see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo matter what you say,\x01",
            "my answer won't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven if Commander Sonya of the\x01",
            "CGF would come here in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PKh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(250)

    ChrTalk(
        0x102,
        (
            "#00106F#12P...Lloyd, let's excuse us.\x02\x03",
            "#00108FIt's useless asking more than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...Understood.\x02",
    )

    CloseMessageWindow()

    def lambda_11AEC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11AEC)
    Sleep(50)

    def lambda_11AFC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11AFC)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(200)

    ChrTalk(
        0x101,
        "#00003F#6PExcuse us, Archbishop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHm, no hard feelings.\x02",
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

    def lambda_11C82():
        OP_95(0x101, 50000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C82)

    def lambda_11C9C():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11C9C)
    OP_68(49820, 1000, 3570, 7000)
    MoveCamera(315, 20, 0, 7000)
    OP_6E(300, 7000)
    SetCameraDistance(30000, 7000)
    Sleep(500)

    def lambda_11CDE():
        OP_95(0x102, 48800, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11CDE)

    def lambda_11CF8():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_11CF8)
    Sleep(500)

    def lambda_11D0C():
        OP_95(0x103, 51000, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11D0C)

    def lambda_11D26():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_11D26)
    Sleep(500)

    def lambda_11D3A():
        OP_95(0x104, 50000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11D3A)

    def lambda_11D54():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_11D54)
    Sleep(500)

    def lambda_11D68():
        OP_95(0x109, 48750, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11D68)

    def lambda_11D82():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_11D82)
    Sleep(500)

    def lambda_11D96():
        OP_95(0x105, 50000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11D96)

    def lambda_11DB0():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_11DB0)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x0, 0x1F4)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    def lambda_11DE7():
        OP_95(0x105, 50750, 0, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11DE7)
    WaitChrThread(0x101, 1)

    def lambda_11E05():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11E05)
    WaitChrThread(0x102, 1)

    def lambda_11E16():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11E16)
    WaitChrThread(0x103, 1)

    def lambda_11E27():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11E27)
    WaitChrThread(0x104, 1)

    def lambda_11E38():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11E38)
    WaitChrThread(0x109, 1)

    def lambda_11E49():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11E49)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0x101, 500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#11PHey hey hey...\x02\x03",
            "#00301FWasn't he just a tiny\x01",
            "bit too ill-natured?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PS-Senior...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PHowever, there was no particular\x01",
            "guilty atmosphere there.\x02\x03",
            "#00208FIt was like he was thinking that it was\x01",
            "correct to hide something from us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Maybe there's some\x01",
            "kind of taboo...\x02\x03",
            "#00008FAnd also, a taboo that even\x01",
            "teacher Marble doesn't know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11POh boy, being told like that only makes\x01",
            "me want to know much more about them.\x02\x03",
            "#10302FSince things are like this, should we try looking\x01",
            "for it reading the Testaments from start to finish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBut if you consider the entire\x01",
            "Testaments, they're extensive...\x02\x03",
            "#00108F...I read them in the past so I\x01",
            "don't know in which passage...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    Sound(103, 0, 60, 0)

    NpcTalk(
        0xA,
        "Girl's Voice",
        (
            "#1P#2S...Maybe they won't appear\x01",
            "in the common Testaments.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_121A3():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_121A3)
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
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()
    OP_68(52730, 1000, 3870, 2000)
    MoveCamera(326, 21, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)

    def lambda_12291():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12291)
    Sleep(0)

    def lambda_122A1():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_122A1)
    Sleep(0)

    def lambda_122B1():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_122B1)
    Sleep(0)

    def lambda_122C1():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_122C1)
    Sleep(0)

    def lambda_122D1():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_122D1)
    Sleep(0)

    def lambda_122E1():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_122E1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_12306():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_12306)
    OP_95(0xA, 56800, 0, 3000, 2000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5PYou're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PM-Miss Ries...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F#12P(*shh*, quiet down...)\x02\x03",
            "#04400F(...Leave from the chapel like you're \x01",
            "doing and please come to the dormitory.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    OP_9B(0x0, 0xA, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_123FA():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_123FA)
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

    def lambda_124D4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_124D4)

    def lambda_124E1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_124E1)
    Sleep(50)

    def lambda_124F1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_124F1)
    Sleep(50)

    def lambda_12501():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12501)
    Sleep(50)

    def lambda_12511():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12511)
    Sleep(50)

    def lambda_12521():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12521)
    Sleep(50)

    def lambda_12531():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12531)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x109,
        "#10101F#5P(W-What do we do...?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1263B")

    ChrTalk(
        0x101,
        (
            "#00003F#6P(She's someone related to the\x01",
            ""Gralsritter" if I remember correctly...)\x02\x03",
            "#00001F(At any rate, let's try to go there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#5P(Yes, I think that's okay.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_126DE")

    label("loc_1263B")


    ChrTalk(
        0x102,
        (
            "#00103F#5P(...We can trust her.)\x02\x03",
            "#00101F(It seems she has something to talk\x01",
            "with us, so let's try to go there.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F#6P(...Yeah, understood.)\x02",
    )

    CloseMessageWindow()

    label("loc_126DE")

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

    # Function_53_1102C end

    def Function_54_12723(): pass

    label("Function_54_12723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128D4")

    ChrTalk(
        0xD,
        (
            "Oh... You seem to be\x01",
            "worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I wonder if she would appear as \x01",
            "the "Sister" entry in the pageant...?)\x02\x03",
            "#00000FUhhm, excuse me.\x01",
            "I'd like to consult with you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            "...U-Uhhm...\x01",
            "To think that I'd be invited...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, I'm sorry.\x01",
            "I have another job to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see...\x01",
            "Then, it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 2)
    Jump("loc_1295D")

    label("loc_128D4")


    ChrTalk(
        0xD,
        (
            "I'm sorry, I have\x01",
            "another job to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm also not good with the\x01",
            "air of a beauty contest, so...\x01",
            "I'll have to refuse, this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1295D")

    TalkEnd(0xD)
    Return()

    # Function_54_12723 end

    def Function_55_12961(): pass

    label("Function_55_12961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C00")

    ChrTalk(
        0x8,
        (
            "Oh...\x01",
            "Everyone, is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Teacher Marble is\x01",
            "a Sister too, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(A-As you can imagine, we\x01",
            "can't invite her to something\x01",
            "like a pageant...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Uh uh, could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That you intend to invite\x01",
            "me at the pageant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a rumor going\x01",
            "around that such a\x01",
            "thing is being planned.\x02",
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
            "#00012FE-Eeehm...\x01",
            "Did you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu, I'm joking.\x01",
            "I have a certain age, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Try asking the other Sisters.\x01",
            "I'm sure someone will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F*sigh*...\x01",
            "We're no match for\x01",
            "you, teacher Marble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 3)
    Jump("loc_12CA4")

    label("loc_12C00")


    ChrTalk(
        0x8,
        (
            "Try asking the other Sisters \x01",
            "about the pageant..\x01",
            "I'm sure someone will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, if only I were a little younger,\x01",
            "I would've participated though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CA4")

    TalkEnd(0x8)
    Return()

    # Function_55_12961 end

    def Function_56_12CA8(): pass

    label("Function_56_12CA8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_END)), "loc_12E63")

    ChrTalk(
        0xA,
        (
            "#04405FOh, everyone.\x01",
            "Do you need anything from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(A "Sister" for the pageant...\x01",
            "Wouldn't she be fine?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(You're right...let's try asking her.)\x02\x03",
            "#00000FMiss Ries, there's something \x01",
            "we'd like to have advice on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13304")

    label("loc_12E63")


    ChrTalk(
        0x101,
        (
            "#00000FMiss Ries, it seems\x01",
            "you're helping out\x01",
            "with mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FYes, it's as you say.\x02\x03",
            "#04400F...It seems that at this\x01",
            "mass there're a great\x01",
            "many worship-visitors.\x02\x03",
            "Having your precious place attacked,\x01",
            "the fear of being injured...\x02\x03",
            "#04403F...I understand those feelings too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMiss Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(...Maybe something similar\x01",
            "happened to her too in the past.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(Just between you and me... Due to\x01",
            "the effects of this incident, the\x01",
            "Congregation for the Sacraments too\x01",
            "has not decided how to move next.)\x02\x03",
            "#04403F(...While I can stay in Crossbell, I intend to\x01",
            "gather as much information as possible.)\x02\x03",
            "#04400F(Lloyd and you all too, please\x01",
            "be careful about how you move.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(While in Crossbell...you say?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...Understood.\x01",
            "Miss Ries, be careful too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04405FBy the way...\x01",
            "Could you be needing anything from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FE-Eehm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hu hu, I was almost forgetting,\x01",
            "but a "Sister" for the pageant...\x01",
            "Wouldn't she be fine?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(You're right...\x01",
            "Since we're here, let's try asking her.)\x02\x03",
            "#00000FMiss Ries, there's something \x01",
            "we'd like to have advice on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)

    label("loc_13304")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405FA pageant...is it?\x02\x03",
            "#04402FI think that a charity event\x01",
            "is something really nice, but...\x01",
            "Today I'm busy with many things.\x02\x03",
            "#04406FAlso, for a clergyman to participate\x01",
            "to such an event would be a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FW-Well, that's also true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTch, and I wanted to see dear\x01",
            "Ries standin' on the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FUh uh...\x01",
            "However, I think that the event\x01",
            "itself is something really nice.\x02\x03",
            "Aside from the pageant, what\x01",
            "other things are being done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FUhhm, aside from that there're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FA piano concert and\x01",
            "a buffet party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04403F............\x01",
            "Everyone, can I ask you to\x01",
            "let me take part in that pageant?\x02",
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
            "#00012FE-Eehm...we don't mind.\x02\x03",
            "#00004F(Was she reeled in by the buffet party...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F(Ahaha, seems so.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FThen, I have to help with mass\x01",
            "for a little while more.\x02\x03",
            "#04404FWhen the program starts, \x01",
            "please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13852")

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

    label("loc_13852")

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

    # Function_56_12CA8 end

    def Function_57_13885(): pass

    label("Function_57_13885")

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
        "Oh...do you need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you wish for a sermon,\x01",
            "I could make time for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00005FN-No.\x01",
            "It's not for that motive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F("The light of the greatest Goddess" that\x01",
            "was written on Phantom Thief B card...)\x02",
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
            "#6P#N#00100F(Maybe it indicates the\x01",
            "light from this big\x01",
            "stained glass...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#6P#N#00203F(In that case, "Who has the \x01",
            "light poured on his back" is...)\x02",
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
        "I don't understand, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have something to say,\x01",
            "what about saying it clearly, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FE-Eehm, then...\x02\x03",
            "#00000FArchbishop Eralda.\x01",
            "Could you do us the favor to let\x01",
            "us look under that platform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, we won't do anything suspicious,\x01",
            "so you can rest easy.\x02",
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
            "Lloyd and the others explained the situation to\x01",
            "Archbishop Eralda and searched the platform.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FFound it...!\x02",
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
            "On the reverse side of the trunk\x01",
            "there was a card attached.\x07\x00\x02",
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
            "The fourth cell is outside the city.\x01",
            "Find "The iron road that runs under\x01",
            "the feet of the western protectors".\x07\x00\x02",
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
            "#6P#00100FThis should be "Mistel",\x01",
            "a doll Bell really loved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHm, no doubt.\x01",
            "...And with this, we have three at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When on earth did a thing like\x01",
            "that end up in such a place...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sometimes I leave due to business,\x01",
            "but not for that much time, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FFrankly speakin', I could\x01",
            "only say that's divine work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FAlso, the card seems\x01",
            "difficult as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FAccording to the "protectors" word,\x01",
            "it could also stay for "guardians".\x02\x03",
            "#00103FIf we add the "western" part to it, we have\x01",
            ""the guardians of the west side of Crossbell".\x01",
            "That's what it could mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FThen there's that "iron road" that runs\x01",
            "under the feet of the "guardians"...eh?\x02\x03",
            "#10106FUuuhm, I still don't really get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FCould it be another figure of speech?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, I think it could be it.\x02\x03",
            "#00000FAt any rate, let's retrieve this trunk\x01",
            "and head on the next search.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#11PPhantom Thief B, hm...?\x01",
            "I heard stories about him.\x01",
            "It seems to be quite the scoundrel.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14488():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14488)
    Sleep(50)

    def lambda_14498():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14498)

    ChrTalk(
        0x9,
        (
            "#11PAs a servant of the Great Goddess,\x01",
            "I cannot forgive such a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLadies and gentlemen,\x01",
            "catch him no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FW-We'll do our best.\x02",
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
            "#16IRosenberg Doll M\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x337, 1)
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

    # Function_57_13885 end

    SaveToFile()

Try(main)
