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
        "Function_11_2FA0",        # 0B, 11
        "Function_12_30B5",        # 0C, 12
        "Function_13_34A7",        # 0D, 13
        "Function_14_35B5",        # 0E, 14
        "Function_15_378D",        # 0F, 15
        "Function_16_4CB3",        # 10, 16
        "Function_17_61EA",        # 11, 17
        "Function_18_73F7",        # 12, 18
        "Function_19_8E17",        # 13, 19
        "Function_20_98A9",        # 14, 20
        "Function_21_9C80",        # 15, 21
        "Function_22_9E8F",        # 16, 22
        "Function_23_9EBE",        # 17, 23
        "Function_24_BE71",        # 18, 24
        "Function_25_C464",        # 19, 25
        "Function_26_C601",        # 1A, 26
        "Function_27_CCA3",        # 1B, 27
        "Function_28_CDAA",        # 1C, 28
        "Function_29_CE4B",        # 1D, 29
        "Function_30_CF76",        # 1E, 30
        "Function_31_D069",        # 1F, 31
        "Function_32_D163",        # 20, 32
        "Function_33_D435",        # 21, 33
        "Function_34_D615",        # 22, 34
        "Function_35_D7D6",        # 23, 35
        "Function_36_D8A4",        # 24, 36
        "Function_37_D931",        # 25, 37
        "Function_38_D976",        # 26, 38
        "Function_39_D9F5",        # 27, 39
        "Function_40_DB07",        # 28, 40
        "Function_41_DB81",        # 29, 41
        "Function_42_DC3A",        # 2A, 42
        "Function_43_DD68",        # 2B, 43
        "Function_44_DDCC",        # 2C, 44
        "Function_45_DEBC",        # 2D, 45
        "Function_46_DF1D",        # 2E, 46
        "Function_47_E066",        # 2F, 47
        "Function_48_E3D5",        # 30, 48
        "Function_49_E491",        # 31, 49
        "Function_50_E955",        # 32, 50
        "Function_51_EC22",        # 33, 51
        "Function_52_FF9F",        # 34, 52
        "Function_53_10863",       # 35, 53
        "Function_54_11F77",       # 36, 54
        "Function_55_12195",       # 37, 55
        "Function_56_124D1",       # 38, 56
        "Function_57_12FEB",       # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_114A")
    Call(0, 12)
    Jump("loc_114D")

    label("loc_114A")

    Call(0, 11)

    label("loc_114D")

    Jump("loc_1413")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1350")

    ChrTalk(
        0x9,
        (
            "The Large Tree that appeared in the\x01",
            "Marshlands... Nothing of the sort is recorded\x01",
            "in the Testaments of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be some sort of\x01",
            "man made thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1317")

    ChrTalk(
        0x105,
        (
            "#10400FWell, just leave it to us\x01",
            "for now.\x02\x03",
            "#10404FIf we manage the situation,\x01",
            "I'd love to request your\x01",
            "cooperation from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I will think about\x01",
            "it. If it is for\x01",
            "Crosbell's sake, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "May the Goddess'\x01",
            "protection be with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1348")

    label("loc_1317")


    ChrTalk(
        0x9,
        (
            "...May the Goddess'\x01",
            "protection be with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1348")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1413")

    label("loc_1350")


    ChrTalk(
        0x9,
        (
            "As for that Large Tree, there is\x01",
            "no record of it in Testaments of\x01",
            "the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be some sort of man made\x01",
            "thing. However... Let us pray to\x01",
            "the Goddess for her protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1413")

    Jump("loc_2F9C")

    label("loc_1418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_168B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1443")
    Call(0, 12)
    Jump("loc_1446")

    label("loc_1443")

    Call(0, 11)

    label("loc_1446")

    Jump("loc_1686")

    label("loc_144B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(
        0x9,
        (
            "The present situation in Crossbell... I am also one\x01",
            "of the causes for having continually rejected the\x01",
            "intervention of the Congregation for the Sacraments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I had accepted their aid, it is\x01",
            "possible that the situation would\x01",
            "have not reached this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears I need to\x01",
            "cool my anger and take a\x01",
            "good look inside myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1686")

    label("loc_15B0")


    ChrTalk(
        0x9,
        (
            "If I had accepted aid from the Congregation\x01",
            "for the Sacraments, it is possible that the\x01",
            "situation would have not reached this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears I need to\x01",
            "cool my anger and take a\x01",
            "good look inside myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1686")

    Jump("loc_2F9C")

    label("loc_168B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E1")

    ChrTalk(
        0x9,
        (
            "Sister Ries has returned\x01",
            "to HQ in Arteria, hm...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...It seems the Congregation\x01",
            "for the Sacraments has started\x01",
            "to intervene in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Crossbell is entering\x01",
            "troubled times... That\x01",
            "could be an omen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that I too, as leader\x01",
            "of Crossbell parish, must think\x01",
            "about what to do from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D3")

    label("loc_17E1")


    ChrTalk(
        0x9,
        (
            "Even the Congregation for the Sacraments has\x01",
            "started to act in earnest... Crossbell seems\x01",
            "to be on the verge of entering troubled times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that I too, as leader\x01",
            "of Crossbell parish, must think\x01",
            "about what to do from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D3")

    Jump("loc_2F9C")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7C")

    ChrTalk(
        0x9,
        (
            "...A little while ago,\x01",
            "information came in from the\x01",
            "Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It said that the Pope himself had\x01",
            "approved the Congregation for the\x01",
            "Sacraments' intervention in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be that the present situation\x01",
            "where an attack and so on happened\x01",
            "could not have been helped...\x02",
        )
    )


    ChrTalk(
        0x9,
        (
            "However, even so... I\x01",
            "cannot approve of them, who\x01",
            "conduct illegal activities.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B4C")

    label("loc_1A7C")


    ChrTalk(
        0x9,
        (
            "Information came in saying the Pope\x01",
            "Himself had approved the Congregation for\x01",
            "the Sacraments intervention in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, even so... I\x01",
            "cannot approve of them, who\x01",
            "conduct illegal activities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4C")

    Jump("loc_2F9C")

    label("loc_1B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1A")

    ChrTalk(
        0x9,
        (
            "Even now, many CGF members\x01",
            "are being exposed to danger\x01",
            "on Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "O Great Goddess of the\x01",
            "Sky, I beg you to\x01",
            "protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And drive away evil...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C74")

    label("loc_1C1A")


    ChrTalk(
        0x9,
        (
            "O Great Goddess of the\x01",
            "Sky, I beg you to\x01",
            "protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And drive away evil...\x02",
    )

    CloseMessageWindow()

    label("loc_1C74")

    Jump("loc_2F9C")

    label("loc_1C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D43")

    ChrTalk(
        0x9,
        (
            "Just now, a bracer came to\x01",
            "get information. Eolia and\x01",
            "Ling appear to be missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Unfortunately, they didn't\x01",
            "come to the cathedral. Hmm,\x01",
            "I hope they are all right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DD6")

    label("loc_1D43")


    ChrTalk(
        0x9,
        (
            "I am indebted to them for many things,\x01",
            "like supplying medicinal ingredients,\x01",
            "guarding my priests and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope they are all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD6")

    Jump("loc_2F9C")

    label("loc_1DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EA6")

    ChrTalk(
        0x9,
        (
            "Well then... I have to\x01",
            "schedule the next mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Following cult incident, incidents are still\x01",
            "continuing... I have to provide peace of mind\x01",
            "to the citizens who participate in mass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9C")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_204B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA3")

    ChrTalk(
        0x9,
        (
            "...About the matter of\x01",
            "yesterday's flower, are\x01",
            "you still snooping around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In this vast continent, you\x01",
            "sometimes run across worlds you\x01",
            "should not come into contact with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...You must not delve\x01",
            "too deeply into it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2046")

    label("loc_1FA3")


    ChrTalk(
        0x9,
        (
            "In this vast continent, you\x01",
            "sometimes run across worlds you\x01",
            "should not come into contact with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You must not delve too\x01",
            "deeply into it. Bear\x01",
            "that in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2046")

    Jump("loc_2F9C")

    label("loc_204B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_22DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220C")

    ChrTalk(
        0x9,
        (
            "There is nothing I can\x01",
            "say about those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even others within the church...\x01",
            "such as Sister Marble, for example,\x01",
            "should have no knowledge of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now leave me. I am a\x01",
            "busy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(As I thought, it seems\x01",
            "the Archbishop won't\x01",
            "tell us...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Ries seemed to want to\x01",
            "speak to us, so... Let's\x01",
            "try going to her for now.)\x02\x03",
            "(She should be waiting at\x01",
            "the dormitory, just\x01",
            "outside the chapel.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22DA")

    label("loc_220C")


    ChrTalk(
        0x9,
        (
            "There is nothing I can\x01",
            "say about those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now leave me. I am a\x01",
            "busy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Miss Ries should be waiting at the\x01",
            "dormitory just outside the chapel...\x01",
            "Anyway, let's try going there.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DA")

    Jump("loc_2F9C")

    label("loc_22DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_23F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B1")

    ChrTalk(
        0x9,
        (
            "Ries Argent... As I\x01",
            "suspected, I am sure she\x01",
            "is her younger sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph... that lot. What\x01",
            "in the world are they\x01",
            "scheming...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It seems he's in deep\x01",
            "thought...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23F0")

    label("loc_23B1")


    ChrTalk(
        0x9,
        (
            "...That damn lot. What\x01",
            "in the world are they\x01",
            "scheming...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F0")

    Jump("loc_2F9C")

    label("loc_23F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2525")

    ChrTalk(
        0x9,
        (
            "The very day of the trade conference's\x01",
            "main session... Sister Ries' business\x01",
            "trip took an awfully long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And also, there are\x01",
            "those ruins in the Mainz\x01",
            "area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I see. I do not know what she\x01",
            "was doing, but... As I suspected,\x01",
            "it seems there is no doubt.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_258F")

    label("loc_2525")


    ChrTalk(
        0x9,
        (
            "...Oh, what could you\x01",
            "want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am researching something\x01",
            "now. Do not enter the room\x01",
            "indiscreetly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258F")

    Jump("loc_2F9C")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2916")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D0")
    Call(0, 57)
    Return()

    label("loc_25D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(
        0x9,
        (
            "Phantom Thief B... To think\x01",
            "he hid stolen goods in the\x01",
            "sacred Crossbell Cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I heard stories about\x01",
            "him. He seems to be\x01",
            "quite the scoundrel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As a servant of the\x01",
            "Great Goddess, I cannot\x01",
            "forgive such a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ladies and gentlemen,\x01",
            "please. Do whatever it\x01",
            "takes to capture him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27AD")

    label("loc_270D")


    ChrTalk(
        0x9,
        (
            "Phantom Thief B... As a\x01",
            "servant of the Great Goddess,\x01",
            "I cannot forgive such a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ladies and gentlemen,\x01",
            "please. Do whatever it\x01",
            "takes to capture him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AD")

    TalkEnd(0x9)
    Return()

    label("loc_27B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287D")

    ChrTalk(
        0x9,
        (
            "Crown Princess Klaudia\x01",
            "came to greet me some\x01",
            "time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though young, she\x01",
            "possesses a sophisticated\x01",
            "way of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of Liberl\x01",
            "Kingdom could be bright\x01",
            "indeed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2911")

    label("loc_287D")


    ChrTalk(
        0x9,
        (
            "Crown Princess Klaudia...\x01",
            "Though young, she possess a\x01",
            "sophisticated way of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The future of Liberl\x01",
            "Kingdom could be bright\x01",
            "indeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2911")

    Jump("loc_2F9C")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_29D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2931")
    Call(0, 14)
    Jump("loc_29CF")

    label("loc_2931")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "A business trip to\x01",
            "Mainz...? I somewhat\x01",
            "worried, but all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Regarding that girl,\x01",
            "report to me if\x01",
            "something happens again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_29CF")

    Jump("loc_2F9C")

    label("loc_29D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B06")

    ChrTalk(
        0x9,
        (
            "I received a letter from\x01",
            "Professor Ragot of St.\x01",
            "Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "His study using the Lupinus Grass medical\x01",
            "herb I gave him before produced results...\x01",
            "And so on, that's what it said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Although that is outside\x01",
            "my area of expertise, I can\x01",
            "at least say "Well done."\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BC8")

    label("loc_2B06")


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
            "...Although that is outside\x01",
            "my area of expertise, I can\x01",
            "at least say "Well done."\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC8")

    Jump("loc_2F9C")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE8")
    Call(0, 13)
    Jump("loc_2C74")

    label("loc_2BE8")

    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ries Argent, hmm...?\x01",
            "Well, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sister Hatina. Teach her\x01",
            "the job very well for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, please leave it to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_2C74")

    Jump("loc_2F9C")

    label("loc_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA8")

    ChrTalk(
        0x9,
        (
            "...Ries Argent... That\x01",
            "young girl is...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x153,
        (
            "#01111FArchbishop, what's\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FRies is that sister,\x01",
            "right?\x02\x03",
            "#10304FHehe, is there something\x01",
            "you're worried about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "...It has nothing to do\x01",
            "with all of you. Pay it\x01",
            "no mind.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E53")

    label("loc_2DA8")


    ChrTalk(
        0x9,
        (
            "...Ries Argent... That\x01",
            "young girl is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01100FIf you tummy hurts, just\x01",
            "say so. KeA will go get\x01",
            "the first aid kit for you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x153, 500)

    ChrTalk(
        0x9,
        (
            "Y-Yes. ...Pay it no\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E53")

    Jump("loc_2F9C")

    label("loc_2E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2E66")
    Jump("loc_2F9C")

    label("loc_2E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F23")

    ChrTalk(
        0x9,
        (
            "Welcome to the Crossbell\x01",
            "Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aidios will surely reach\x01",
            "out to all those who seek\x01",
            "relief with a pious heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "May the Goddess guide\x01",
            "you all...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F9C")

    label("loc_2F23")


    ChrTalk(
        0x9,
        (
            "Aidios will surely reach\x01",
            "out to all those who seek\x01",
            "relief with a pious heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "May the Goddess guide\x01",
            "you all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9C")

    TalkEnd(0x9)
    Return()

    # Function_10_111C end

    def Function_11_2FA0(): pass

    label("Function_11_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3052")

    ChrTalk(
        0x9,
        (
            "...To think that the\x01",
            "situation has reached\x01",
            "this point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps it is my responsibility\x01",
            "for having refused "their"\x01",
            "intervention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_30B4")

    label("loc_3052")


    ChrTalk(
        0x9,
        (
            "Perhaps it is my responsibility\x01",
            "for having refused "their"\x01",
            "intervention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()

    label("loc_30B4")

    Return()

    # Function_11_2FA0 end

    def Function_12_30B5(): pass

    label("Function_12_30B5")

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
            "#10400FHi there, Archbishop\x01",
            "Eralda. Long time no\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...So that's how it is,\x01",
            "hm? Wazy Hemisphere, you\x01",
            "really are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My eyes were thoroughly\x01",
            "deceived by Sister Ries'\x01",
            "deception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...It is truly something\x01",
            "the Congregation for the\x01",
            "Sacraments would think of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FHehe. Regarding that,\x01",
            "allow me to apologize\x01",
            "officially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In the current matter, I am also\x01",
            "at fault for having stubbornly\x01",
            "refused to allow your intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For this reason, you\x01",
            "have no need to\x01",
            "apologize.\x02",
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
        "#00306FA strict man as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FWell, considering your\x01",
            "position, I think it's\x01",
            "unavoidable.\x02\x03",
            "#10400FHehe. But I'd be happy if you\x01",
            "could take a little less notice\x01",
            "of our activities from now on.\x02",
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
        (
            "#00211FThat's too blunt of a\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I cannot give you an\x01",
            "immediate reply. However,\x01",
            "I will consider it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears I need to\x01",
            "cool my anger and take a\x01",
            "good look inside myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 1)
    Return()

    # Function_12_30B5 end

    def Function_13_34A7(): pass

    label("Function_13_34A7")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "...It appears that she\x01",
            "is assisting Sister\x01",
            "Marble.\x02",
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
            "Yes. She's very quick in\x01",
            "learning the job... She's\x01",
            "a great help to all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, I see...\x02",
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

    # Function_13_34A7 end

    def Function_14_35B5(): pass

    label("Function_14_35B5")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hm... You entrusted Sister\x01",
            "Ries with tomorrow's\x01",
            "Sunday School trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. It seems she hasn't\x01",
            "started Sunday School\x01",
            "lessons yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Excuse me, Archbishop.\x01",
            "Is there something about\x01",
            "Sister Ries...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It seems you've been\x01",
            "very worried about her\x01",
            "recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...No, it is nothing so\x01",
            "important. I am just a little\x01",
            "worried about the way she works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Regarding that girl,\x01",
            "report to me if\x01",
            "something happens again.\x02",
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

    # Function_14_35B5 end

    def Function_15_378D(): pass

    label("Function_15_378D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387B")

    ChrTalk(
        0xFE,
        (
            "Although the President has been arrested,\x01",
            "the situation surrounding Crossbell can\x01",
            "hardly be said to be optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The day when this land will\x01",
            "be dragged into war once\x01",
            "again could be not far off...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38ED")

    label("loc_387B")


    ChrTalk(
        0xFE,
        (
            "The day when Crossbell is\x01",
            "again dragged into war\x01",
            "could not so far off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let us pray, to the\x01",
            "Goddess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38ED")

    Jump("loc_4CAF")

    label("loc_38F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D6")

    ChrTalk(
        0xFE,
        (
            "It seems the Archbishop\x01",
            "feels partly responsible\x01",
            "for this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder. He's\x01",
            "strict even towards\x01",
            "himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly why I'd\x01",
            "like him to guide us as\x01",
            "he has until now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A50")

    label("loc_39D6")


    ChrTalk(
        0xFE,
        (
            "The Archbishop feels\x01",
            "partly responsible for\x01",
            "this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, we intend to\x01",
            "stand by Archbishop\x01",
            "Eralda.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A50")

    Jump("loc_4CAF")

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7A")

    ChrTalk(
        0xFE,
        (
            "Crossbell State independence should\x01",
            "be causing big repercussions in the\x01",
            "neighboring countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In particular, even stronger\x01",
            "pressure should be coming from\x01",
            "the major powers from now on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens\x01",
            "of Crossbell will be\x01",
            "able to endure it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C0C")

    label("loc_3B7A")


    ChrTalk(
        0xFE,
        (
            "From now on, increased\x01",
            "pressure should be coming\x01",
            "from the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens\x01",
            "of Crossbell will be\x01",
            "able to endure it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0C")

    Jump("loc_4CAF")

    label("loc_3C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D03")

    ChrTalk(
        0xFE,
        (
            "Due to the previous attack,\x01",
            "the CGF and townsfolk\x01",
            "suffered a lot of damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What should we do so\x01",
            "that the same thing\x01",
            "doesn't happen again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The citizens of\x01",
            "Crossbell must think\x01",
            "about that together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D89")

    label("loc_3D03")


    ChrTalk(
        0xFE,
        (
            "What should we do so\x01",
            "that the same thing\x01",
            "doesn't happen again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The citizens of\x01",
            "Crossbell must think\x01",
            "about that together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D89")

    Jump("loc_4CAF")

    label("loc_3D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E1C")

    ChrTalk(
        0xFE,
        (
            "I wonder what has become\x01",
            "of the citizens of\x01",
            "Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such an act... There's\x01",
            "no way the Goddess could\x01",
            "ever forgive it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_3E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EBC")

    ChrTalk(
        0xFE,
        (
            "I'm told the derailment\x01",
            "accident yesterday along West\x01",
            "Crossbell Highway was awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that there were\x01",
            "no dead is a silver\x01",
            "lining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_3EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0xFE,
        (
            "Doing the right thing in\x01",
            "sunshine or rain... It's\x01",
            "easier said than done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda, who can strictly\x01",
            "measure not only others, but also himself,\x01",
            "is the most respectable person to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4052")

    ChrTalk(
        0xFE,
        (
            "The Archbishop is very\x01",
            "rigorous towards the precepts\x01",
            "of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are people who say he's a\x01",
            "bigot, but, instead, I respect\x01",
            "that side of the Archbishop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_4052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_40DA")

    ChrTalk(
        0xFE,
        (
            "Oh, have you already\x01",
            "spoken to the\x01",
            "Archbishop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... It seems it ended\x01",
            "rather quickly... Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_40DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_41A6")

    ChrTalk(
        0xFE,
        (
            "Recently, I'm told that mysterious\x01",
            "monster appearances have been\x01",
            "witnessed throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's also been a notice\x01",
            "from the CGF. I'd really like\x01",
            "to call for caution here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_41A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4273")

    ChrTalk(
        0xFE,
        (
            "At present, the\x01",
            "Archbishop is holed up\x01",
            "in his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears he is\x01",
            "researching Ries' latest\x01",
            "activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Archbishop and\x01",
            "Ries... Could something\x01",
            "be wrong?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42A2")

    label("loc_4273")


    ChrTalk(
        0xFE,
        (
            "The Archbishop is holed\x01",
            "up in his office.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A2")

    Jump("loc_4CAF")

    label("loc_42A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B0")

    ChrTalk(
        0xFE,
        (
            "It appears Crown\x01",
            "Princess Klaudia is well\x01",
            "versed in the sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she was taught\x01",
            "directly by Captain Julia, and\x01",
            "they say she is quite capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shouldn't say this, but\x01",
            "you can't judge a person\x01",
            "by their appearance...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4443")

    label("loc_43B0")


    ChrTalk(
        0xFE,
        (
            "It appears Crown\x01",
            "Princess Klaudia is well\x01",
            "versed in the sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shouldn't say this, but\x01",
            "you can't judge a person\x01",
            "by their appearance...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4443")

    Jump("loc_4CAF")

    label("loc_4448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_45D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4543")

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "trade conference results\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for the countries' heads\x01",
            "of state, each of them is a\x01",
            "well-known intellectual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen, I\x01",
            "can't overlook whatever\x01",
            "decisions will be made.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45CB")

    label("loc_4543")


    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "trade conference results\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen, I\x01",
            "can't overlook whatever\x01",
            "decisions will be made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CB")

    Jump("loc_4CAF")

    label("loc_45D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471D")

    ChrTalk(
        0xFE,
        (
            "There was strong discord\x01",
            "between the Archbishop and\x01",
            "Professor Ragot, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It has softened up a little\x01",
            "recently and he became able to at\x01",
            "least read the professor's letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears their relationship has\x01",
            "improved considerably from the times when\x01",
            "he threw them away without reading them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47B1")

    label("loc_471D")


    ChrTalk(
        0xFE,
        (
            "Originally, Professor Ragot\x01",
            "was a priest studying under\x01",
            "the Archbishop like myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that, in time,\x01",
            "their discord will\x01",
            "disappear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B1")

    Jump("loc_4CAF")

    label("loc_47B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4866")

    ChrTalk(
        0xFE,
        (
            "Today I'm cleaning the\x01",
            "cathedral with the staff\x01",
            "who are free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it's an old building...\x01",
            "If it's not periodically cleaned,\x01",
            "it will get damaged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAF")

    label("loc_4866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_4A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4963")

    ChrTalk(
        0xFE,
        (
            "Senior class lessons should\x01",
            "be quite a lot more difficult\x01",
            "than the junior classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "KeA's reasoning skills\x01",
            "are amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FEhehe... KeA got\x01",
            "praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, that makes me\x01",
            "proud too for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A19")

    label("loc_4963")


    ChrTalk(
        0xFE,
        (
            "KeA ends up smoothly\x01",
            "solving problems that would\x01",
            "even make an adult think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I don't observe her\x01",
            "lessons, just by hearing that I\x01",
            "can understand how amazing she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A19")

    Jump("loc_4CAF")

    label("loc_4A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AFB")

    ChrTalk(
        0xFE,
        (
            "It seems Archbishop Eralda\x01",
            "is interviewing our new\x01",
            "sister, Sister Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When he heard her name,\x01",
            "the Archbishop seemed a\x01",
            "little surprised, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, could she be\x01",
            "someone famous?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B78")

    label("loc_4AFB")


    ChrTalk(
        0xFE,
        (
            "It seems the Archbishop was\x01",
            "a little surprised upon\x01",
            "hearing Sister Ries' name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, could she be\x01",
            "someone famous?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B78")

    Jump("loc_4CAF")

    label("loc_4B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3C")

    ChrTalk(
        0xFE,
        (
            "Mass is held\x01",
            "periodically at the\x01",
            "cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mass is a holy function\x01",
            "to revere the Goddess of\x01",
            "the Sky...\x02",
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
    Jump("loc_4CAF")

    label("loc_4C3C")


    ChrTalk(
        0xFE,
        (
            "Mass is a holy function\x01",
            "to revere the Goddess of\x01",
            "the Sky...\x02",
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

    label("loc_4CAF")

    TalkEnd(0xFE)
    Return()

    # Function_15_378D end

    def Function_16_4CB3(): pass

    label("Function_16_4CB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D88")

    ChrTalk(
        0xFE,
        (
            "I was finally able to\x01",
            "contact the children in\x01",
            "the city.\x02",
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
    Jump("loc_4E44")

    label("loc_4D88")


    ChrTalk(
        0xFE,
        (
            "I was able to contact the\x01",
            "children in the city and\x01",
            "for now I'm relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I think I'll consult with\x01",
            "Sister Marble about lesson contact\x01",
            "for when Sunday School restarts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E44")

    Jump("loc_61E6")

    label("loc_4E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F02")

    ChrTalk(
        0xFE,
        (
            "For such a thing to happen when we're\x01",
            "still having a hard time contacting\x01",
            "the children in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, o Goddess... Please\x01",
            "protect the people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F35")

    label("loc_4F02")


    ChrTalk(
        0xFE,
        (
            "Ah, o Goddess... Please\x01",
            "protect the people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F35")

    Jump("loc_61E6")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5102")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5082")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Sister Ries\x01",
            "left Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears she received a\x01",
            "recall order from the\x01",
            "Holy Nation of Arteria...\x02",
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
            "#00101F(Yes, she probably\x01",
            "received orders as a\x01",
            "Gralsritter.)\x02\x03",
            "#00103F(Although, as you might\x01",
            "imagine, I don't know\x01",
            "what they could be...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50FD")

    label("loc_5082")


    ChrTalk(
        0xFE,
        (
            "Yesterday, Sister Ries\x01",
            "left Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears she received a\x01",
            "recall order from the\x01",
            "Holy Nation of Arteria...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FD")

    Jump("loc_61E6")

    label("loc_5102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5134")
    Call(0, 54)
    Return()

    label("loc_5134")


    ChrTalk(
        0xFE,
        (
            "At this mass we were\x01",
            "visited by a lot more\x01",
            "people than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the scars the\x01",
            "people received in the attack\x01",
            "seems to have been great...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E6")

    label("loc_51D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D1")

    ChrTalk(
        0xFE,
        (
            "Kimmy and Alec... I just met them the\x01",
            "day before yesterday and yet they got\x01",
            "involved in such an incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure they're having a frightening\x01",
            "experience... Aah, Goddess, please\x01",
            "save those children, save Mainz...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5350")

    label("loc_52D1")


    ChrTalk(
        0xFE,
        (
            "I just went to Mainz two\x01",
            "days ago for Sunday\x01",
            "School lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, Goddess, please\x01",
            "save those children,\x01",
            "save Mainz...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5350")

    Jump("loc_61E6")

    label("loc_5355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5363")
    Jump("loc_61E6")

    label("loc_5363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5371")
    Jump("loc_61E6")

    label("loc_5371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_537F")
    Jump("loc_61E6")

    label("loc_537F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_5468")

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
            "I'm also leaving tomorrow and\x01",
            "the day after to teach Sunday\x01",
            "School in Mainz and Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to consult\x01",
            "with Sister Marble later\x01",
            "about lesson content.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E6")

    label("loc_5468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_55CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5534")

    ChrTalk(
        0xFE,
        (
            "Do you need Sister\x01",
            "Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is currently in the\x01",
            "middle of senior\x01",
            "classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she is teaching\x01",
            "Sister Juju how to do lessons,\x01",
            "so she might be very busy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55C6")

    label("loc_5534")


    ChrTalk(
        0xFE,
        (
            "Right now, Sister Marble\x01",
            "is in the middle of\x01",
            "senior classes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since she is training Sister\x01",
            "Juju's today as well, she\x01",
            "might be very busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55C6")

    Jump("loc_61E6")

    label("loc_55CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571B")

    ChrTalk(
        0xFE,
        (
            "I heard Sister Juju is\x01",
            "learning how to hold a lesson\x01",
            "from Sister Marble today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that trusting Sister\x01",
            "Ries with the Mainz lessons has\x01",
            "been a good stimulus for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is clumsy, but I'm sure she'll be\x01",
            "good at it eventually, since she has the\x01",
            "innate talent of being liked by children.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_57AE")

    label("loc_571B")


    ChrTalk(
        0xFE,
        (
            "Sister Juju has the\x01",
            "innate talent of being\x01",
            "liked by children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure she'll even be\x01",
            "good at holding Sunday\x01",
            "School lessons, eventually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57AE")

    Jump("loc_61E6")

    label("loc_57B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_592F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A3")

    ChrTalk(
        0xFE,
        (
            "It seems Sister Ries has\x01",
            "just returned from her trip\x01",
            "to hold Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was worried since she\x01",
            "was a little late,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be that she was\x01",
            "having something to eat\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_592A")

    label("loc_58A3")


    ChrTalk(
        0xFE,
        (
            "It seems Sister Ries has\x01",
            "just returned from her trip\x01",
            "to hold Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's reporting in to\x01",
            "Sister Marble's right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_592A")

    Jump("loc_5A8C")

    label("loc_592F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A2C")

    ChrTalk(
        0xFE,
        (
            "Sister Ries is going on a\x01",
            "trip to Mainz to hold Sunday\x01",
            "School lessons today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's calm, but she's\x01",
            "good at teaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about\x01",
            "it, she should be back\x01",
            "by now, but...\x02",
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
    Jump("loc_5A8C")

    label("loc_5A2C")


    ChrTalk(
        0xFE,
        (
            "Sister Ries... She\x01",
            "should be back by now,\x01",
            "but...\x02",
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

    label("loc_5A8C")

    Jump("loc_61E6")

    label("loc_5A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAC")
    Call(0, 14)
    Jump("loc_5B48")

    label("loc_5AAC")


    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda... It appears\x01",
            "he's been concerned about\x01",
            "Sister Ries for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if there's some\x01",
            "circumstance we're not\x01",
            "aware of...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B48")

    Jump("loc_61E6")

    label("loc_5B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CCC")

    ChrTalk(
        0xFE,
        (
            "Since the cathedral is far from the\x01",
            "children of Mainz and Armorica,\x01",
            "they can't attend Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, the Downtown kids don't\x01",
            "come to church at all, even when\x01",
            "it's the day for their lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We sisters go to the city\x01",
            "and villages to hold lessons\x01",
            "targeted at those children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, Sister\x01",
            "Ries went to Downtown\x01",
            "for us today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D5F")

    label("loc_5CCC")


    ChrTalk(
        0xFE,
        (
            "Incidentally, Sister\x01",
            "Ries went to Downtown\x01",
            "for us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the kids there are\x01",
            "strange. I wonder if she's\x01",
            "doing the lesson all right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5F")

    Jump("loc_61E6")

    label("loc_5D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7F")
    Call(0, 13)
    Jump("loc_5E29")

    label("loc_5D7F")


    ChrTalk(
        0xFE,
        (
            "Sister Ries was very quick to\x01",
            "learn the job... She's been a\x01",
            "great help to all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda... I\x01",
            "wonder if he's concerned\x01",
            "about her for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E29")

    Jump("loc_61E6")

    label("loc_5E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_5ED6")

    ChrTalk(
        0xFE,
        (
            "Ries appears to have gone\x01",
            "to the graveyard after\x01",
            "greeting the Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Starting tomorrow, we'll\x01",
            "have to teach her many\x01",
            "things about the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E6")

    label("loc_5ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_612E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B6")

    ChrTalk(
        0xFE,
        (
            "Sister Ries is calm and\x01",
            "has a certain air about\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, a very delicious\x01",
            "smell was coming from her...\x01",
            "What ever could that mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNow that you mention it... A\x01",
            "slight breadlike fragrance\x01",
            "was coming from Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMaybe she'd been\x01",
            "shopping at a bakery\x01",
            "before coming?\x02\x03",
            "#00109FAlthough slender, Ries\x01",
            "is quite the glutton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FY-Yes... You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, I'd like to have a\x01",
            "meal with her once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6129")

    label("loc_60B6")


    ChrTalk(
        0xFE,
        (
            "Sister Ries is calm and\x01",
            "has a certain air about\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she'll be a\x01",
            "good stimulus for Sister\x01",
            "Juju.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6129")

    Jump("loc_61E6")

    label("loc_612E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_61E6")

    ChrTalk(
        0xFE,
        (
            "Actually, a new sister from\x01",
            "the Holy Nation of Arteria is\x01",
            "scheduled to arrive today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of person\x01",
            "she will be... I'm slightly\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E6")

    TalkEnd(0xFE)
    Return()

    # Function_16_4CB3 end

    def Function_17_61EA(): pass

    label("Function_17_61EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_627E")

    ChrTalk(
        0xC,
        (
            "People who seek help in the\x01",
            "Church are going to keep\x01",
            "coming one after the next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have to be prepared\x01",
            "and show them in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_627E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_62F0")

    ChrTalk(
        0xC,
        (
            "It seems terrible things\x01",
            "are happening in\x01",
            "Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope the citizens are\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_62F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63FE")

    ChrTalk(
        0xC,
        (
            "Crossbell independence...\x01",
            "It's become something\x01",
            "unimaginable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Moreover, a bank asset freeze...\x01",
            "As a man of the Septian Church,\x01",
            "it's not something I can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We'll have to monitor\x01",
            "the situation ourselves\x01",
            "for a little while...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_64A4")

    label("loc_63FE")


    ChrTalk(
        0xC,
        (
            "A bank asset freeze... As a man\x01",
            "of the Septian Church, it's not\x01",
            "something I can defend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We'll have to monitor\x01",
            "the situation ourselves\x01",
            "for a little while...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64A4")

    Jump("loc_73F3")

    label("loc_64A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6570")

    ChrTalk(
        0xC,
        (
            "It seems the Testaments\x01",
            "kids took the initiative\x01",
            "to repair Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At first I didn't understand what\x01",
            "they were thinking, but... It seems\x01",
            "that, deep down, they're good kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_6570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_65E7")

    ChrTalk(
        0xC,
        (
            "It's incredible to think\x01",
            "such an incident could\x01",
            "happen.\x02",
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
    Jump("loc_73F3")

    label("loc_65E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_666F")

    ChrTalk(
        0xC,
        (
            "I witnessed Juju\x01",
            "magnificently falling on\x01",
            "her bottom earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My my, she can't quite\x01",
            "get rid of her\x01",
            "clumsiness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_666F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_66EB")

    ChrTalk(
        0xC,
        (
            "This pedestal is often\x01",
            "used for dosing and the\x01",
            "like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must clean it more\x01",
            "carefully than\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_66EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6858")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BA")

    ChrTalk(
        0xC,
        (
            "It appears Ries is\x01",
            "always walking with\x01",
            "Testaments in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I often see her with her\x01",
            "nose in a book whenever\x01",
            "she's free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How diligent. It's a\x01",
            "good thing to be doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6853")

    label("loc_67BA")


    ChrTalk(
        0xC,
        (
            "Ries always walks around carrying\x01",
            "Testaments with her. It seems she\x01",
            "reads them when she has time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How diligent. It's a\x01",
            "good thing to be doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6853")

    Jump("loc_73F3")

    label("loc_6858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_68DC")

    ChrTalk(
        0xC,
        (
            "It appears Ries has\x01",
            "returned from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder where she went\x01",
            "to eat today. Maybe I'll\x01",
            "ask her later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_68DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_696E")

    ChrTalk(
        0xC,
        (
            "Hmm, I think this just\x01",
            "about does it for the\x01",
            "cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is a place everyone\x01",
            "uses. It must be kept\x01",
            "clean at all times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_696E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3F")

    ChrTalk(
        0xC,
        (
            "While I was cleaning the\x01",
            "office, the Archbishop\x01",
            "came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He told me to leave him\x01",
            "alone since he is\x01",
            "researching something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hm... I wonder what he\x01",
            "could be researching?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6AA4")

    label("loc_6A3F")


    ChrTalk(
        0xC,
        (
            "It appears Ries went to\x01",
            "the city to have lunch\x01",
            "just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe I'll take a break\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AA4")

    Jump("loc_73F3")

    label("loc_6AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA1")

    ChrTalk(
        0xC,
        (
            "I thought that Crown Princess\x01",
            "Klaudia would've been tense\x01",
            "heading into today's conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was surprised.\x01",
            "Instead, she was very\x01",
            "calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected from the\x01",
            "next Queen of Liberl...\x01",
            "She has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6C30")

    label("loc_6BA1")


    ChrTalk(
        0xC,
        (
            "Crown Princess Klaudia\x01",
            "quite calm heading into\x01",
            "the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected from the\x01",
            "next Queen of Liberl...\x01",
            "She has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C30")

    Jump("loc_73F3")

    label("loc_6C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D48")

    ChrTalk(
        0xC,
        (
            "I was taken aback at the\x01",
            "ceremony as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To be quite honest, a building\x01",
            "stretching 40 floors above ground\x01",
            "is something really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. I'll have to give President\x01",
            "Dieter my compliments the next\x01",
            "time he comes to worship.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6DFF")

    label("loc_6D48")


    ChrTalk(
        0xC,
        (
            "I was taken aback at the\x01",
            "ceremony as well. To think\x01",
            "there are really 40 floors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. I'll have to give President\x01",
            "Dieter my compliments the next\x01",
            "time he comes to worship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DFF")

    Jump("loc_73F3")

    label("loc_6E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_703C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F64")

    ChrTalk(
        0xC,
        (
            "Because Archbishop Eralda\x01",
            "is so strict, he has many\x01",
            "antagonists in the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Among them, he is particularly strict\x01",
            "towards those of the Congregation for the\x01",
            "Sacraments, whose activities are unclear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank goodness it's so rare for people\x01",
            "from the Congregation for the\x01",
            "Sacraments to come to Crossbell parish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7037")

    label("loc_6F64")


    ChrTalk(
        0xC,
        (
            "The Congregation for the Sacraments... It\x01",
            "is an organization within the Church said\x01",
            "to manage the Goddess' sacraments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Their activities in detail\x01",
            "are not made known even to\x01",
            "us common clergymen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7037")

    Jump("loc_73F3")

    label("loc_703C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_71DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7177")

    ChrTalk(
        0xC,
        (
            "SInce Miss Ries is docile-looking,\x01",
            "I was worried about her becoming\x01",
            "friends with everyone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "During yesterday's evening meal\x01",
            "duty, it seems she hit it off\x01",
            "with Sister Juju right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It appears they had a lot of\x01",
            "fun last night chatting about\x01",
            "good stores in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_71D7")

    label("loc_7177")


    ChrTalk(
        0xC,
        (
            "Ries just loves talking\x01",
            "about food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, it seems she has\x01",
            "an amazing passion for\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71D7")

    Jump("loc_73F3")

    label("loc_71DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_72A5")

    ChrTalk(
        0xC,
        (
            "The Archbishop... After the\x01",
            "greetings ended, it seems he's been\x01",
            "in deep thought about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder if there's been\x01",
            "some problem with Ries. It\x01",
            "doesn't seem so, however...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_72A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_7352")

    ChrTalk(
        0xC,
        (
            "The Archbishop interviews\x01",
            "each and every new priest\x01",
            "and sister who comes here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As clergymen, we can't\x01",
            "put unfit persons in the\x01",
            "cathedral, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73F3")

    label("loc_7352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73F3")

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
            "valuable books are kept here, do not\x01",
            "go around touching things at random.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F3")

    TalkEnd(0xFE)
    Return()

    # Function_17_61EA end

    def Function_18_73F7(): pass

    label("Function_18_73F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_75D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751F")

    ChrTalk(
        0xFE,
        (
            "That thing appeared all of a\x01",
            "sudden and me and my trader\x01",
            "friends are all shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But don't worry. If we just\x01",
            "pray to the Goddess,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come now, why don't you pray\x01",
            "too? By doing that, just about\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_75D3")

    label("loc_751F")


    ChrTalk(
        0xFE,
        (
            "Whatever happens, if we just\x01",
            "pray to the Goddess,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come now, why don't you pray\x01",
            "too? By doing that, just about\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D3")

    Jump("loc_8E13")

    label("loc_75D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_76EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768A")

    ChrTalk(
        0xFE,
        (
            "I snuck out in secret under\x01",
            "m-martial law to come pray and\x01",
            "something like this happens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't go back to the\x01",
            "city. What should I\x01",
            "do...!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_76E5")

    label("loc_768A")


    ChrTalk(
        0xFE,
        (
            "A-At any rate, I have to pray\x01",
            "to the Goddess that the\x01",
            "situation calms down quickly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E5")

    Jump("loc_8E13")

    label("loc_76EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_78C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7829")

    ChrTalk(
        0xFE,
        (
            "With rail service halted, it\x01",
            "seems being a trader is going\x01",
            "to get harder from now on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I don't intend to go\x01",
            "against the flow of society. I'm\x01",
            "sure this too is the Goddess' will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, we'll manage somehow.\x01",
            "As long as you don't forget to\x01",
            "have a believing heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_78BB")

    label("loc_7829")


    ChrTalk(
        0xFE,
        (
            "If you pray to the Goddess,\x01",
            "I'm sure that everything\x01",
            "will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all should pray too.\x01",
            "What's important is a\x01",
            "believing heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78BB")

    Jump("loc_8E13")

    label("loc_78C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79CC")

    ChrTalk(
        0xFE,
        (
            "Recently my business was\x01",
            "going well due to praying\x01",
            "to the Goddess, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After such a serious\x01",
            "incident happened, frankly,\x01",
            "I can't openly be glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Praying for my profits is\x01",
            "surely meaningless. I have\x01",
            "to pray for peace itself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7A69")

    label("loc_79CC")


    ChrTalk(
        0xFE,
        (
            "No matter how much I profit,\x01",
            "with the situation in Crossbell,\x01",
            "I can't openly be glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Peace itself, that's\x01",
            "what I have to pray to\x01",
            "the Goddess for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A69")

    Jump("loc_8E13")

    label("loc_7A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B41")

    ChrTalk(
        0xFE,
        (
            "Actually, I planned to stock up\x01",
            "on septium at Mainz today... To\x01",
            "think such a thing happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-That's right, I have to\x01",
            "pray to the Goddess for the\x01",
            "incident to be resolved...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7BD7")

    label("loc_7B41")


    ChrTalk(
        0xFE,
        (
            "Forget about my business,\x01",
            "I'm worried about the\x01",
            "situation in Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, please show\x01",
            "everyone the way to\x01",
            "resolving this incident...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BD7")

    Jump("loc_8E13")

    label("loc_7BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD8")

    ChrTalk(
        0xFE,
        (
            "Actually, I felt an ill\x01",
            "omen throughout the day\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I asked later,\x01",
            "hadn't a derailment\x01",
            "accident occurred?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It had no influence on my\x01",
            "business negotiations, but...\x01",
            "Honestly, that was frightening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7DA7")

    label("loc_7CD8")


    ChrTalk(
        0xFE,
        (
            "Actually, I felt an ill omen throughout\x01",
            "the day yesterday. I was shocked at\x01",
            "news of the derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It had no influence on my\x01",
            "business negotiations, but...\x01",
            "Honestly, that was frightening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DA7")

    Jump("loc_8E13")

    label("loc_7DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6A")

    ChrTalk(
        0xFE,
        (
            "I had been fervently praying\x01",
            "to the Goddess, but... I\x01",
            "snapped a shoelace just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a business\x01",
            "negotiation today... Why\x01",
            "must I be so unfortunate!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7EF5")

    label("loc_7E6A")


    ChrTalk(
        0xFE,
        (
            "A black cat crossed my path, a\x01",
            "shoelace snapped... It's been\x01",
            "nothing but ill omens since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope nothing happens,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF5")

    Jump("loc_8E13")

    label("loc_7EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8000")

    ChrTalk(
        0xFE,
        (
            "...Actually, this black\x01",
            "cat crossed my path this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, damn... I have a business\x01",
            "negotiation today. Isn't that\x01",
            "an extremely bad omen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This requires me to be\x01",
            "more conscientious in my\x01",
            "prayer than usual...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_8091")

    label("loc_8000")


    ChrTalk(
        0xFE,
        (
            "Even though I have a business\x01",
            "negotiation today, a black cat\x01",
            "crossed right in front of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O Goddess, please\x01",
            "exorcise this bad\x01",
            "omen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8091")

    Jump("loc_8E13")

    label("loc_8096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_8136")

    ChrTalk(
        0xFE,
        (
            "...Yes. I prayed a lot,\x01",
            "so I guess it's time to\x01",
            "head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or perhaps it's not\x01",
            "enough prayer. I think I'll\x01",
            "stay here a while longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E13")

    label("loc_8136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_82BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_822A")

    ChrTalk(
        0xFE,
        (
            "I'm positive Ian\x01",
            "Grimwood came here not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looked a little tired, but... I'm\x01",
            "sure he was healed by the holy air\x01",
            "which fills this place of worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He prayed as well... I'm\x01",
            "sure he'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_82BA")

    label("loc_822A")


    ChrTalk(
        0xFE,
        (
            "I've often consulted\x01",
            "with Mr. Grimwood for my\x01",
            "trade deals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looked a little tired,\x01",
            "but he prayed too, so...\x01",
            "I'm sure he was healed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82BA")

    Jump("loc_8E13")

    label("loc_82BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_848E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83DA")

    ChrTalk(
        0xFE,
        (
            "Foreign nations seem to be\x01",
            "taking a growing interest in the\x01",
            "recent independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear my foreign trader\x01",
            "friends discussing Crossbell\x01",
            "independence on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, Crossbell's\x01",
            "visibility seems to have\x01",
            "grown even more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8489")

    label("loc_83DA")


    ChrTalk(
        0xFE,
        (
            "The referendum on the question of\x01",
            "independence draws close. Only\x01",
            "the Goddess knows its result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess. Please,\x01",
            "make the result the best\x01",
            "choice for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8489")

    Jump("loc_8E13")

    label("loc_848E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8554")

    ChrTalk(
        0xFE,
        (
            "They said that citizens\x01",
            "cannot attend today's\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a pity, but... It can't be helped.\x01",
            "I'll remain here, praying to the Goddess\x01",
            "for the success of the conference.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E13")

    label("loc_8554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_86FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8651")

    ChrTalk(
        0xFE,
        (
            "I went to see Orchis\x01",
            "Tower myself... It was\x01",
            "ridiculously tall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I prayed from the rooftop, it\x01",
            "would be a lot easier for my prayers\x01",
            "to reach the Goddess of the Sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'd really like to\x01",
            "go up there one day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_86F6")

    label("loc_8651")


    ChrTalk(
        0xFE,
        (
            "If it was from the Orchis Tower rooftop,\x01",
            "it would be much easier for prayers to\x01",
            "reach the Goddess of the Sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'd really like to\x01",
            "go up there one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86F6")

    Jump("loc_8E13")

    label("loc_86FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_886F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87DB")

    ChrTalk(
        0xFE,
        (
            "They say that, starting tomorrow,\x01",
            "economic relations are going to be\x01",
            "discussed at the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To me, whose business is\x01",
            "based out of Crossbell, it's\x01",
            "an event of extreme concern.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_886A")

    label("loc_87DB")


    ChrTalk(
        0xFE,
        (
            "To us traders, the trade\x01",
            "conference is very\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, I'll have to\x01",
            "pray the Goddess for the\x01",
            "success of the conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_886A")

    Jump("loc_8E13")

    label("loc_886F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_89B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893C")

    ChrTalk(
        0xFE,
        (
            "No matter if it rains, no matter if\x01",
            "there's a typhoon, I pray every day I have\x01",
            "an early morning business negotiation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, my\x01",
            "business is booming.\x01",
            "Hahaha...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_89B0")

    label("loc_893C")


    ChrTalk(
        0xFE,
        (
            "No matter what happens,\x01",
            "I never fail to pray\x01",
            "daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Little and often fills\x01",
            "the purse, they say.\x01",
            "Hahaha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89B0")

    Jump("loc_8E13")

    label("loc_89B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_8B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B10")

    ChrTalk(
        0x153,
        (
            "#01105FAh, it's the old man who\x01",
            "always comes to pray.\x02\x03",
            "#01109FYou came this morning,\x01",
            "but you're still here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. I decided to offer\x01",
            "prayers all day on my\x01",
            "day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You pray too, little miss.\x01",
            "If you do that, everything\x01",
            "will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F...Lloyd, is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(...Heck if I know.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8B97")

    label("loc_8B10")


    ChrTalk(
        0xFE,
        (
            "I decided to offer my\x01",
            "prayers all day on my\x01",
            "day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please pray as well,\x01",
            "everyone. If you do,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B97")

    Jump("loc_8E13")

    label("loc_8B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_8CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C2E")

    ChrTalk(
        0xFE,
        (
            "What I have now is\x01",
            "thanks to the Goddess'\x01",
            "blessing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must put feelings of\x01",
            "gratitude into my\x01",
            "prayers.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_8CAB")

    label("loc_8C2E")


    ChrTalk(
        0xFE,
        (
            "Ah, o Goddess of the\x01",
            "Sky, thank you for\x01",
            "everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I beg you for to bless\x01",
            "my business in the\x01",
            "future as well...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CAB")

    Jump("loc_8E13")

    label("loc_8CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5E")

    ChrTalk(
        0xFE,
        (
            "I'm a trader, you see. I try\x01",
            "to come here often to pray for\x01",
            "the success of my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I strongly suggest that\x01",
            "all of you pray as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8E13")

    label("loc_8D5E")


    ChrTalk(
        0xFE,
        (
            "When I prayed for the success of\x01",
            "my business before, it really\x01",
            "happened that it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When doing anything, first\x01",
            "pray to the Goddess. If you\x01",
            "do that, you won't fail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E13")

    TalkEnd(0xFE)
    Return()

    # Function_18_73F7 end

    def Function_19_8E17(): pass

    label("Function_19_8E17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E28")
    Jump("loc_98A5")

    label("loc_8E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_92ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E5A")
    Call(0, 56)
    Return()

    label("loc_8E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_927B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_917A")

    ChrTalk(
        0x101,
        (
            "#00000FRies, it looks like\x01",
            "you're helping with\x01",
            "mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FIndeed I am.\x02\x03",
            "#04408FThere's an especially\x01",
            "large number of visitors\x01",
            "for today's mass.\x02\x03",
            "Their homes have been\x01",
            "attacked, and they fear\x01",
            "for their lives...\x02\x03",
            "#04403FI myself understand how\x01",
            "they feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FRies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(...Maybe something like\x01",
            "this happened to Ries\x01",
            "long ago.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(This is just between you and me...\x01",
            "Due to the effects of this incident,\x01",
            "mobilization of the Congregation for\x01",
            "the Sacraments has been confirmed.)\x02\x03",
            "#04403F(...While I'm in Crossbell, I intend\x01",
            "to gather as much intelligence as I\x01",
            "can.)\x02\x03",
            "#04400F(You all should act carefully.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(While in Crossbell...\x01",
            "you say?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Understood. Take care\x01",
            "of yourself as well,\x01",
            "Ries.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)
    Jump("loc_9276")

    label("loc_917A")


    ChrTalk(
        0xA,
        (
            "#04400F(Due to the effects of this incident,\x01",
            "the Congregation for the Sacraments\x01",
            "has not yet decided its next move.)\x02\x03",
            "#04403F(...While I am in Crossbell, I intend\x01",
            "to gather as much information as\x01",
            "possible.)\x02\x03",
            "#04400F(You all should act carefully.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9276")

    Jump("loc_92E8")

    label("loc_927B")


    ChrTalk(
        0xA,
        (
            "#04400FI have to help with mass\x01",
            "for a while longer.\x02\x03",
            "#04404FWhen the program starts,\x01",
            "please contact me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92E8")

    Jump("loc_98A5")

    label("loc_92ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_92FB")
    Jump("loc_98A5")

    label("loc_92FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966E")

    ChrTalk(
        0xA,
        (
            "#04400FYesterday's derailment\x01",
            "accident... They say a giant\x01",
            "monster was seen near the site.\x02\x03",
            "Everyone, do you have any\x01",
            "idea...?\x02",
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
            "Briefly explained\x01",
            "yesterday's accident.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405F...Pleroma Grass in Knox\x01",
            "Woodlands too...\x02\x03",
            "#04408FAlso, Gnosis appeared\x01",
            "again in this land...?\x02\x03",
            "#04403FI think the problem is\x01",
            ""Who gave him Gnosis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F...Did you figure out\x01",
            "anything on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FI am sorry, but... I haven't made\x01",
            "any progress on cult-related\x01",
            "information, Gnosis included.\x02\x03",
            "#04403FAs for Pleroma Grass, my research\x01",
            "is progressing, but what causes\x01",
            "it to bloom is still unknown...\x02\x03",
            "#04400FSince I was the only one who\x01",
            "could infiltrate this land, it's\x01",
            "taking this long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so...\x02\x03",
            "#00000FThen, if you figure out\x01",
            "anything else, please\x01",
            "contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04400FYes... Understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 1)
    Jump("loc_9743")

    label("loc_966E")


    ChrTalk(
        0xA,
        (
            "#04403FPleroma Grass in Knox Woodlands... Also,\x01",
            "Gnosis appeared again in this land...\x02\x03",
            "#04400FSince I can't act publicly, the\x01",
            "investigation isn't going well, but...\x01",
            "I'll report to you if I do find something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9743")

    Jump("loc_98A5")

    label("loc_9748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9756")
    Jump("loc_98A5")

    label("loc_9756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9764")
    Jump("loc_98A5")

    label("loc_9764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_9772")
    Jump("loc_98A5")

    label("loc_9772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_9780")
    Jump("loc_98A5")

    label("loc_9780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_978E")
    Jump("loc_98A5")

    label("loc_978E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_982C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B5")
    Call(0, 21)
    Jump("loc_9827")

    label("loc_97B5")


    ChrTalk(
        0xA,
        (
            "#04400F...Everyone, thank you\x01",
            "very much for today.\x02\x03",
            "#04403FI'll be counting on you\x01",
            "if anything else\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9827")

    Jump("loc_98A5")

    label("loc_982C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_983A")
    Jump("loc_98A5")

    label("loc_983A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9848")
    Jump("loc_98A5")

    label("loc_9848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9863")
    Call(0, 20)
    Jump("loc_987B")

    label("loc_9863")


    ChrTalk(
        0xA,
        "#04403F(Rufina...)\x02",
    )

    CloseMessageWindow()

    label("loc_987B")

    Jump("loc_98A5")

    label("loc_9880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_988E")
    Jump("loc_98A5")

    label("loc_988E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_989C")
    Jump("loc_98A5")

    label("loc_989C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_98A5")

    label("loc_98A5")

    TalkEnd(0xFE)
    Return()

    # Function_19_8E17 end

    def Function_20_98A9(): pass

    label("Function_20_98A9")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04400F...I see. It appears\x01",
            "that education here is\x01",
            "proceeding well.\x02\x03",
            "#04404FAs expected of a modern\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. It is indeed\x01",
            "progressing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter where you go,\x01",
            "children are the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FThat could very well be\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...By the way, Ries.\x01",
            "There's one thing that's\x01",
            "been on my mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if you're the\x01",
            "younger sister of\x01",
            "Rufina.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#04405F...You knew my sister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I knew it. It's\x01",
            "because you have the\x01",
            "same last name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She helped me with many\x01",
            "things a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FI see...\x02\x03",
            "#04400FUmm, Sister Marble? I\x01",
            "have a favor I'd like to\x01",
            "ask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. You don't have to say\x01",
            "anything. You're probably\x01",
            "the same as her, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I owe Rufina a great\x01",
            "deal, so I won't inform\x01",
            "the archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...But, can I ask one\x01",
            "thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Don't overdo it. For\x01",
            "Rufina's sake as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F...I understand. Thank\x01",
            "you for your concern.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 3)
    Return()

    # Function_20_98A9 end

    def Function_21_9C80(): pass

    label("Function_21_9C80")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Miss Ries, you're a\x01",
            "little late... Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, your habit is\x01",
            "stained here and\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403FI'm very sorry for being\x01",
            "late.\x02\x03",
            "#04400FActually, I tripped and\x01",
            "fell on my way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My, my. You're\x01",
            "unexpectedly clumsy,\x01",
            "Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Just because you're\x01",
            "young, you don't have to\x01",
            "overdo it all the time, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400F...Thank you for the\x01",
            "advice. I'll go change\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Miss Marble... She seemed to\x01",
            "have noticed that something\x01",
            "may have happened.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x2, 0)
    Return()

    # Function_21_9C80 end

    def Function_22_9E8F(): pass

    label("Function_22_9E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EB2")
    Call(0, 23)
    Jump("loc_9EB5")

    label("loc_9EB2")

    Call(0, 25)

    label("loc_9EB5")

    Jump("loc_9EBD")

    label("loc_9EBA")

    Call(0, 23)

    label("loc_9EBD")

    Return()

    # Function_22_9E8F end

    def Function_23_9EBE(): pass

    label("Function_23_9EBE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A1BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A098")

    ChrTalk(
        0x8,
        (
            "Lloyd, Elie... There's\x01",
            "something I want to ask\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "KeA is... Inside that\x01",
            "tree, right?\x02",
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
        "#00005FTeacher... Can you tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Looking at your\x01",
            "worried faces, I just\x01",
            "assumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I don't know the\x01",
            "details, but there's only\x01",
            "one thing I can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As KeA's guardians, you\x01",
            "must absolutely take her\x01",
            "back. ...Are we clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes... Absolutely!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 3)
    Jump("loc_A1B5")

    label("loc_A098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A156")

    ChrTalk(
        0x8,
        (
            "No matter the\x01",
            "circumstances, KeA still\x01",
            "needs you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And I'm sure KeA feels\x01",
            "the same about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, Elie, and\x01",
            "everyone. You absolutely\x01",
            "must take her back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A1B5")

    label("loc_A156")


    ChrTalk(
        0x8,
        (
            "No matter the\x01",
            "circumstances, KeA still\x01",
            "needs you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You absolutely must take\x01",
            "her back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1B5")

    Jump("loc_BE6D")

    label("loc_A1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A4E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A39A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "My, it's Lloyd, Elie and\x01",
            "everyone...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMiss Marble... I'm glad\x01",
            "you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe're sorry to have made\x01",
            "you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, it's all right. The\x01",
            "most important thing is\x01",
            "that you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way... Is KeA\x01",
            "with you?\x02",
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
        (
            "#00306FWe know where she is,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see... I'm worried\x01",
            "about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...At any rate, this is\x01",
            "a difficult situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be very careful,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 2)
    Jump("loc_A4DE")

    label("loc_A39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A48A")

    ChrTalk(
        0x8,
        (
            "KeA... I'm worried about\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't seen her even once since\x01",
            "the day independence was declared,\x01",
            "and that is weighing on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...At any rate, this is\x01",
            "a difficult situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be very careful,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A4DE")

    label("loc_A48A")


    ChrTalk(
        0x8,
        (
            "...At any rate, this is\x01",
            "a difficult situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be very careful,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4DE")

    Jump("loc_BE6D")

    label("loc_A4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A724")

    ChrTalk(
        0x8,
        (
            "Lloyd... Is KeA all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We haven't had Sunday\x01",
            "School recently, so I'm\x01",
            "a little worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...Now that you mention it,\x01",
            "I feel like she's acting\x01",
            "strange the past few days.\x02\x03",
            "#00003FLike she's brooding over\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYou're right... Every time we\x01",
            "left, it seemed like she was\x01",
            "very worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's most likely uneasy about\x01",
            "this situation, but there's\x01",
            "nothing to be done about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As her guardian, Lloyd,\x01",
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
    Jump("loc_A7BB")

    label("loc_A724")


    ChrTalk(
        0x8,
        (
            "This situation Crossbell is\x01",
            "in... We don't know what\x01",
            "will happen in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As her guardian, Lloyd,\x01",
            "you have to properly\x01",
            "watch over her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7BB")

    Jump("loc_BE6D")

    label("loc_A7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A996")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7F2")
    Call(0, 55)
    Return()

    label("loc_A7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8F7")

    ChrTalk(
        0x8,
        (
            "I was able to confirm that, for\x01",
            "the time being, the children\x01",
            "attending Sunday School are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The situation being what\x01",
            "it is, lessons are\x01",
            "suspended, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When we restart them, I\x01",
            "would like to see smiles\x01",
            "full of energy again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A991")

    label("loc_A8F7")


    ChrTalk(
        0x8,
        (
            "The situation being what\x01",
            "it is, the Sunday School\x01",
            "lessons are suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When we restart them, I\x01",
            "would like to see smiles\x01",
            "full of energy again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A991")

    Jump("loc_BE6D")

    label("loc_A996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_AA00")

    ChrTalk(
        0x8,
        (
            "What a terrible\x01",
            "situation this has\x01",
            "become.\x02",
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
    Jump("loc_BE6D")

    label("loc_AA00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AACE")

    ChrTalk(
        0x8,
        (
            "Today, I had Sister Hatina\x01",
            "go teach Sunday School in\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears there's rain\x01",
            "today across all of\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope she doesn't get\x01",
            "soaking wet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AB57")

    label("loc_AACE")


    ChrTalk(
        0x8,
        (
            "Today, I had Sister Hatina\x01",
            "go teach Sunday School in\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's raining too... I\x01",
            "hope she doesn't get\x01",
            "soaking wet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB57")

    Jump("loc_BE6D")

    label("loc_AB5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ADD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2A")

    ChrTalk(
        0x8,
        (
            "Ries had an older sister\x01",
            "named Rufina. She was an\x01",
            "acquaintance of mine as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She belonged to the Congregation for the\x01",
            "Sacraments and solved many different incidents\x01",
            "with her excellent negotiation skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In time she was called\x01",
            ""Thousand Arms" and became\x01",
            "famous in the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Sadly, it appears she was martyred in an\x01",
            "unfortunate accident several years ago... It's\x01",
            "a shame that such a good person passed away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_ADD0")

    label("loc_AD2A")


    ChrTalk(
        0x8,
        (
            "I've been indebted to\x01",
            "Rufina for a long time\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wanted to express my thanks to her\x01",
            "once again, but... It's a shame that\x01",
            "such a good person passed away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD0")

    Jump("loc_BE6D")

    label("loc_ADD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8D")

    ChrTalk(
        0x8,
        (
            "Now that I think about it,\x01",
            "Lloyd... It appears that you\x01",
            "came to visit me yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Was there something you\x01",
            "wanted to ask me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, we're good regarding that for now.\x02\x03",
            "#00003F(It appears there's a taboo in the\x01",
            "Church regarding Pleroma Grass... It's\x01",
            "best not to tell Miss Marble about it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is that so...? All\x01",
            "right, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I'll help you\x01",
            "anytime, so please don't\x01",
            "hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B002")

    label("loc_AF8D")


    ChrTalk(
        0x8,
        (
            "I too want to help you\x01",
            "all as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I'll help you\x01",
            "anytime, so please don't\x01",
            "hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B002")

    Jump("loc_BE6D")

    label("loc_B007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_B15A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B022")
    Call(0, 27)
    Jump("loc_B155")

    label("loc_B022")


    ChrTalk(
        0x8,
        (
            "A journey of a thousand miles\x01",
            "begins with a single step... You\x01",
            "should learn things one at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(According to what the Archbishop\x01",
            "said, even Miss Marble doesn't\x01",
            "know about those azure flowers...)\x02\x03",
            "#00003F(Let's pay a visit to Miss Ries.\x01",
            "She should be at the dorm in front\x01",
            "of the chapel.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B155")

    Jump("loc_BE6D")

    label("loc_B15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_B2FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B242")

    ChrTalk(
        0x8,
        (
            "In Crossbell State we pay 10%\x01",
            "of our tax revenue to both\x01",
            "the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This rule has been in place since\x01",
            "formation of the state, as decided by\x01",
            "the major powers, our suzerain states...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B2F8")

    label("loc_B242")


    ChrTalk(
        0x8,
        (
            "In other words, if the independence is\x01",
            "successful, Crossbell will be freed from\x01",
            "unfair decisions like that going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course, it's far\x01",
            "easier said than done,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F8")

    Jump("loc_BE6D")

    label("loc_B2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B4BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3FE")

    ChrTalk(
        0x8,
        (
            "I deliver lessons\x01",
            "honestly to the children\x01",
            "with "utmost effort".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I do that, they will\x01",
            "listen even to difficult\x01",
            "lessons with passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sister Juju's lessons are\x01",
            "still awkward, but as for\x01",
            "utmost effort, she passes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B4B9")

    label("loc_B3FE")


    ChrTalk(
        0x8,
        (
            "Sister Juju's lessons are\x01",
            "still awkward, but as for\x01",
            "utmost effort, she passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If she adds some basic teaching\x01",
            "methods, I'm sure she'll be able\x01",
            "to hold good lessons in no time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4B9")

    Jump("loc_BE6D")

    label("loc_B4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B7E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B5A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E5")
    Call(0, 21)
    Jump("loc_B5A0")

    label("loc_B4E5")


    ChrTalk(
        0x8,
        (
            "I think that Ries' way\x01",
            "of working can't be\x01",
            "helped, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I think this applies to all of you as\x01",
            "well. Just because you're young, don't\x01",
            "overdo things all the time, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A0")

    Jump("loc_B7E3")

    label("loc_B5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B741")

    ChrTalk(
        0x8,
        (
            "Princess Klaudia seems to have contributed\x01",
            "to the resolution of the Liberl phenomenon\x01",
            "that happened some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the midst of such a terrible incident, the\x01",
            "crowning ceremony was held and she became the\x01",
            "next queen in line for the Liberl throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't fathom what kind\x01",
            "of conflict brought her\x01",
            "to that point, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though young, I think\x01",
            "she has a very strong\x01",
            "backbone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B7E3")

    label("loc_B741")


    ChrTalk(
        0x8,
        (
            "They say the crowning ceremony\x01",
            "for Princess Klaudia was held in\x01",
            "the midst of a terrible incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though young, I think\x01",
            "she has a very strong\x01",
            "backbone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E3")

    Jump("loc_BE6D")

    label("loc_B7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B9BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B902")

    ChrTalk(
        0x8,
        (
            "Come to think of it,\x01",
            "today was the day of the\x01",
            "unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On a building 40 floors above ground,\x01",
            "the children will feel like they can\x01",
            "reach the sky when they look up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I wonder if the\x01",
            "children are having a\x01",
            "good time around now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B9BA")

    label("loc_B902")


    ChrTalk(
        0x8,
        (
            "On a building 40 floors above ground,\x01",
            "the children will feel like they can\x01",
            "reach the sky when they look up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I wonder if the\x01",
            "children are having a\x01",
            "good time around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9BA")

    Jump("loc_BE6D")

    label("loc_B9BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BB1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA9E")

    ChrTalk(
        0x8,
        (
            "Finally, the trade\x01",
            "conference will be held\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It will be hard in many\x01",
            "ways, but... Everyone,\x01",
            "do your best.\x02",
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
            "Miss Marble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BB16")

    label("loc_BA9E")


    ChrTalk(
        0x8,
        (
            "It will be hard in many\x01",
            "ways, but... Everyone,\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will be cheering for\x01",
            "you all from the\x01",
            "shadows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB16")

    Jump("loc_BE6D")

    label("loc_BB1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BBA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB36")
    Call(0, 20)
    Jump("loc_BBA0")

    label("loc_BB36")


    ChrTalk(
        0x8,
        (
            "Oh, Lloyd and everyone...\x01",
            "Are you going out on such\x01",
            "a rainy day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Take care to not catch a\x01",
            "cold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA0")

    Jump("loc_BE6D")

    label("loc_BBA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_BDD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD3E")
    TurnDirection(0x8, 0x153, 0)

    ChrTalk(
        0x8,
        (
            "Haha, KeA. I'm looking\x01",
            "forward to the next\x01",
            "senior class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will prepare some\x01",
            "slightly more difficult\x01",
            "problems for next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FYeah, all right. KeA\x01",
            "will do her best to be\x01",
            "ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FHmm, she's really\x01",
            "amazing... I admire her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. She might surpass\x01",
            "us all, eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHmm. If that happens,\x01",
            "it'll surely be\x01",
            "embarrassing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BDD1")

    label("loc_BD3E")


    ChrTalk(
        0x8,
        (
            "After KeA came, the\x01",
            "senior class lessons\x01",
            "became more lively too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. She seems to have\x01",
            "a good influence on the\x01",
            "other children as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDD1")

    Jump("loc_BE6D")

    label("loc_BDD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_BDE4")
    Jump("loc_BE6D")

    label("loc_BDE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BE6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDFF")
    Call(0, 24)
    Jump("loc_BE6D")

    label("loc_BDFF")


    ChrTalk(
        0x8,
        (
            "Haha. In that case\x01",
            "everyone... I have to\x01",
            "continue the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come visit again\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6D")

    TalkEnd(0x8)
    Return()

    # Function_23_9EBE end

    def Function_24_BE71(): pass

    label("Function_24_BE71")

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
        (
            "#00000FLong time no see, Miss\x01",
            "Marble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIt's been a long time...\x01",
            "Wait, you're not\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. It's because KeA\x01",
            "said "They're baaack!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYou were Lloyd and\x01",
            "Elie's Sunday School\x01",
            "teacher, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, that's right. And you\x01",
            "two appear to be the new\x01",
            "Support Section members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am Marble, Septian\x01",
            "Church sister. Pleased to\x01",
            "make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNow that you mention it...\x01",
            "You didn't study under\x01",
            "Miss Marble, did you Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FNo. The East Street class\x01",
            "Fran and I attended was\x01",
            "taught by a father.\x02\x03",
            "#10103FI think he left Crossbell\x01",
            "at some point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, priest\x01",
            "reassignments do happen\x01",
            "every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I suppose it's quite\x01",
            "lucky I was able to reunite\x01",
            "with Lloyd and Elie like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Miss Marbleee. Don't\x01",
            "just talk to them all\x01",
            "day. Do the lessooon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Ryｹ!! It's their long-awaited\x01",
            "reunion! You don't have to throw\x01",
            "cold water on it so quickly!\x02",
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
            "My, I am sorry. It seems\x01",
            "I got lost in\x01",
            "conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, everyone. I\x01",
            "do need to be getting\x01",
            "back to my lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please visit again if\x01",
            "you have another chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FS-Sorry to disturb your\x01",
            "lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FUmm, excuse us, then.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 2)
    EventEnd(0x5)
    Return()

    # Function_24_BE71 end

    def Function_25_C464(): pass

    label("Function_25_C464")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57F")

    ChrTalk(
        0xF,
        (
            "Sooo... In short, about\x01",
            "the trade conference that\x01",
            "was held the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It was about they call\x01",
            "business\x01",
            "relationships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, I don't really\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "H-Huh? Then, I'll\x01",
            "explain it from the\x01",
            "beginning again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C5FD")

    label("loc_C57F")


    ChrTalk(
        0xF,
        (
            "(Ooh, this could be too\x01",
            "difficult a problem to\x01",
            "deal with...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(B-But it's important,\x01",
            "so I must teach them\x01",
            "properly!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5FD")

    TalkEnd(0xF)
    Return()

    # Function_25_C464 end

    def Function_26_C601(): pass

    label("Function_26_C601")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C612")
    Jump("loc_CC9F")

    label("loc_C612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C620")
    Jump("loc_CC9F")

    label("loc_C620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C62E")
    Jump("loc_CC9F")

    label("loc_C62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B7")

    ChrTalk(
        0xFE,
        (
            "On rainy days it's easy\x01",
            "to slip on floors, so\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I just slipped and\x01",
            "fell myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C740")

    label("loc_C6B7")


    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm really glad\x01",
            "that today Sunday School\x01",
            "is off today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the children had seen\x01",
            "that, they'd make fun of\x01",
            "me even more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C740")

    Jump("loc_CC9F")

    label("loc_C745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C753")
    Jump("loc_CC9F")

    label("loc_C753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C761")
    Jump("loc_CC9F")

    label("loc_C761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_C7ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C77C")
    Call(0, 27)
    Jump("loc_C7E8")

    label("loc_C77C")


    ChrTalk(
        0xFE,
        (
            "Sister Marble's\x01",
            "teachings are very\x01",
            "useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One day, I want to\x01",
            "become a splendid\x01",
            "teacher like her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7E8")

    Jump("loc_CC9F")

    label("loc_C7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_C925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C89A")

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
            "Ah, no, I mustn't. I must use\x01",
            "her lessons as reference, not\x01",
            "to listen to them normally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C920")

    label("loc_C89A")


    ChrTalk(
        0xFE,
        (
            "I'm learning how to\x01",
            "teach by observing\x01",
            "Sister Marble's lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I\x01",
            "unintentionally end up\x01",
            "getting absorbed in them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C920")

    Jump("loc_CC9F")

    label("loc_C925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CAC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA46")

    ChrTalk(
        0xFE,
        (
            "Sooo... In short, about\x01",
            "the trade conference that\x01",
            "was held the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was about they call\x01",
            "business\x01",
            "relationships...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Teacher, I don't really\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "H-Huh? Then, I'll\x01",
            "explain it from the\x01",
            "beginning again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CAC4")

    label("loc_CA46")


    ChrTalk(
        0xFE,
        (
            "(Ooh, this could be too\x01",
            "difficult a problem to\x01",
            "deal with...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(B-But it's important,\x01",
            "so I must teach them\x01",
            "properly!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAC4")

    Jump("loc_CC9F")

    label("loc_CAC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CAD7")
    Jump("loc_CC9F")

    label("loc_CAD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CAE5")
    Jump("loc_CC9F")

    label("loc_CAE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CAF3")
    Jump("loc_CC9F")

    label("loc_CAF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CC7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBE4")

    ChrTalk(
        0xFE,
        (
            "It seems Ries has been a\x01",
            "sister in Arteria for\x01",
            "many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She seems to be about my\x01",
            "age, but she's much\x01",
            "calmer than I am...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm ashamed to\x01",
            "have tried to act like an\x01",
            "important-looking senior.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CC75")

    label("loc_CBE4")


    ChrTalk(
        0xFE,
        (
            "*sigh*, who could have\x01",
            "thought that Sister Ries\x01",
            "was my senior...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel ashamed somehow\x01",
            "for rejoicing, thinking\x01",
            "I had gotten a junior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC75")

    Jump("loc_CC9F")

    label("loc_CC7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_CC88")
    Jump("loc_CC9F")

    label("loc_CC88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_CC96")
    Jump("loc_CC9F")

    label("loc_CC96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CC9F")

    label("loc_CC9F")

    TalkEnd(0xFE)
    Return()

    # Function_26_C601 end

    def Function_27_CCA3(): pass

    label("Function_27_CCA3")

    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xF,
        (
            "Sister Marble, I learned\x01",
            "so much today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Umm, my senior class\x01",
            "lesson was pathetic,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, don't worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A journey of a thousand miles\x01",
            "begins with a single step... You\x01",
            "should learn things one at a time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_27_CCA3 end

    def Function_28_CDAA(): pass

    label("Function_28_CDAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDBF")
    Call(0, 50)
    Jump("loc_CE47")

    label("loc_CDBF")


    ChrTalk(
        0x11,
        (
            "#01100FKeA loves Sunday School.\x02\x03",
            "#01109FKeA studies lots things every\x01",
            "day, and doing it with Ryｹ,\x01",
            "Henri and the others is fun too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE47")

    TalkEnd(0xFE)
    Return()

    # Function_28_CDAA end

    def Function_29_CE4B(): pass

    label("Function_29_CE4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF4D")

    ChrTalk(
        0xFE,
        (
            "Ugh, studying is such a\x01",
            "pain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mister, won't you take\x01",
            "my place and study for\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNow look here... Studying is for\x01",
            "your own sake, you hear? You should\x01",
            "do it properly, by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, you're just like my\x01",
            "dad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CF72")

    label("loc_CF4D")


    ChrTalk(
        0xFE,
        (
            "Ugh, studying is such a\x01",
            "pain...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF72")

    TalkEnd(0xFE)
    Return()

    # Function_29_CE4B end

    def Function_30_CF76(): pass

    label("Function_30_CF76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D00F")
    SetChrSubChip(0x13, 0x1)
    Sleep(500)
    SetChrSubChip(0x12, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Do it properly, Ryｹ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, KeA will\x01",
            "leave you in the dust.\x02",
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
    Jump("loc_D065")

    label("loc_D00F")


    ChrTalk(
        0xFE,
        (
            "I can't just think about\x01",
            "Ryｹ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to do my best to\x01",
            "keep up with KeA too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D065")

    TalkEnd(0xFE)
    Return()

    # Function_30_CF76 end

    def Function_31_D069(): pass

    label("Function_31_D069")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D13E")
    OP_63(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x14)

    ChrTalk(
        0xFE,
        "Umm, ahh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x14, 0x1)
    Sleep(500)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Hey KeA... What do you\x01",
            "do here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01100FLet's see, to calculate\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha... Looks like\x01",
            "they're getting along.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_D15F")

    label("loc_D13E")


    ChrTalk(
        0xFE,
        (
            "I-I see... Like this,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D15F")

    TalkEnd(0xFE)
    Return()

    # Function_31_D069 end

    def Function_32_D163(): pass

    label("Function_32_D163")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3CD")

    ChrTalk(
        0x101,
        (
            "#00000FHi Pinset. How have you\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, you're Wendy's\x01",
            "friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Long time no see. Thank\x01",
            "you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_END)), "loc_D29B")

    ChrTalk(
        0x105,
        "#10305FWendy, huh. Isn't she...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, she's the engineer\x01",
            "we just met at the orbal\x01",
            "store.\x02\x03",
            "#00109FHaha. She's Lloyd's\x01",
            "childhood friend, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D313")

    label("loc_D29B")


    ChrTalk(
        0x105,
        "#10305FWendy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe engineer at the\x01",
            "orbal store.\x02\x03",
            "#00109FHaha. She's Lloyd's\x01",
            "childhood friend, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D313")


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
        (
            "#10112FT-That's one way to put\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's true! You think\x01",
            "so too, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(...It is true. I can't\x01",
            "deny it.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 1)
    Jump("loc_D431")

    label("loc_D3CD")


    ChrTalk(
        0xFE,
        (
            "It was father's\x01",
            "influence that turned\x01",
            "her into a mecha geek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll never end up like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D431")

    TalkEnd(0xFE)
    Return()

    # Function_32_D163 end

    def Function_33_D435(): pass

    label("Function_33_D435")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D446")
    Jump("loc_D611")

    label("loc_D446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D4BC")

    ChrTalk(
        0xFE,
        (
            "They're holding mass\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We do nothing but play\x01",
            "around, we must behave\x01",
            "in times like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D611")

    label("loc_D4BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D4CA")
    Jump("loc_D611")

    label("loc_D4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D4D8")
    Jump("loc_D611")

    label("loc_D4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D4E6")
    Jump("loc_D611")

    label("loc_D4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D4F4")
    Jump("loc_D611")

    label("loc_D4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_D502")
    Jump("loc_D611")

    label("loc_D502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_D510")
    Jump("loc_D611")

    label("loc_D510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D51E")
    Jump("loc_D611")

    label("loc_D51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D52C")
    Jump("loc_D611")

    label("loc_D52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D53A")
    Jump("loc_D611")

    label("loc_D53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D548")
    Jump("loc_D611")

    label("loc_D548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D556")
    Jump("loc_D611")

    label("loc_D556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_D564")
    Jump("loc_D611")

    label("loc_D564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_D572")
    Jump("loc_D611")

    label("loc_D572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D611")

    ChrTalk(
        0xFE,
        (
            "Tch, that Hamil. He recently got\x01",
            "fired up, saying that he wanted\x01",
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

    label("loc_D611")

    TalkEnd(0xFE)
    Return()

    # Function_33_D435 end

    def Function_34_D615(): pass

    label("Function_34_D615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D626")
    Jump("loc_D7D2")

    label("loc_D626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D67D")

    ChrTalk(
        0xFE,
        (
            "Goddess... Please keep\x01",
            "all the people of the\x01",
            "city in good health...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7D2")

    label("loc_D67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D68B")
    Jump("loc_D7D2")

    label("loc_D68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D699")
    Jump("loc_D7D2")

    label("loc_D699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D6A7")
    Jump("loc_D7D2")

    label("loc_D6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D6B5")
    Jump("loc_D7D2")

    label("loc_D6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_D6C3")
    Jump("loc_D7D2")

    label("loc_D6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_D6D1")
    Jump("loc_D7D2")

    label("loc_D6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D6DF")
    Jump("loc_D7D2")

    label("loc_D6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D6ED")
    Jump("loc_D7D2")

    label("loc_D6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D6FB")
    Jump("loc_D7D2")

    label("loc_D6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D709")
    Jump("loc_D7D2")

    label("loc_D709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D717")
    Jump("loc_D7D2")

    label("loc_D717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_D725")
    Jump("loc_D7D2")

    label("loc_D725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_D733")
    Jump("loc_D7D2")

    label("loc_D733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D7D2")

    ChrTalk(
        0xFE,
        (
            "*sigh*... KeA is cute...\x01",
            "I'm happy I get to study\x01",
            "with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, I'll have to raise my\x01",
            "hand a lot and answer one\x01",
            "question after the next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7D2")

    TalkEnd(0xFE)
    Return()

    # Function_34_D615 end

    def Function_35_D7D6(): pass

    label("Function_35_D7D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D86B")

    ChrTalk(
        0xFE,
        (
            "I like shopping and an\x01",
            "interest in economics,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The recent trade conference\x01",
            "is still something\x01",
            "difficult for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D8A0")

    label("loc_D86B")


    ChrTalk(
        0xFE,
        (
            "The trade conference is\x01",
            "still difficult for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8A0")

    TalkEnd(0xFE)
    Return()

    # Function_35_D7D6 end

    def Function_36_D8A4(): pass

    label("Function_36_D8A4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder if big brother\x01",
            "Azel would understand\x01",
            "this conversation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll try asking\x01",
            "him the next time he\x01",
            "comes home.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_D8A4 end

    def Function_37_D931(): pass

    label("Function_37_D931")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Yes, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...As I thought, I don't\x01",
            "really get it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_D931 end

    def Function_38_D976(): pass

    label("Function_38_D976")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*yaaawn*... When I study\x01",
            "I get sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the sister is doing\x01",
            "her best, so I have to\x01",
            "listen to her properly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_D976 end

    def Function_39_D9F5(): pass

    label("Function_39_D9F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA95")

    ChrTalk(
        0xFE,
        (
            "H-Hmm... The trade\x01",
            "conference, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just common sense.\x01",
            "It's so easy it's\x01",
            "laughable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...R-Really? You really\x01",
            "get it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_DB03")

    label("loc_DA95")


    ChrTalk(
        0xFE,
        (
            "Trade conferences are\x01",
            "just common sense. Easy\x01",
            "stuff, easy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Enough, go away! I'm\x01",
            "studying here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB03")

    TalkEnd(0xFE)
    Return()

    # Function_39_D9F5 end

    def Function_40_DB07(): pass

    label("Function_40_DB07")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the sake of your future,\x01",
            "you must study even\x01",
            "complicated things properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Boys, are you\x01",
            "studying?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_DB07 end

    def Function_41_DB81(): pass

    label("Function_41_DB81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_DBD7")

    ChrTalk(
        0xFE,
        "Say, where do we go now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the department store\x01",
            "as usual?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC36")

    label("loc_DBD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_DC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF2")
    Call(0, 42)
    Jump("loc_DC36")

    label("loc_DBF2")


    ChrTalk(
        0xFE,
        (
            "(Lenalee... Didn't she\x01",
            "got mad at me too\x01",
            "because of youuu...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC36")

    TalkEnd(0xFE)
    Return()

    # Function_41_DB81 end

    def Function_42_DC3A(): pass

    label("Function_42_DC3A")


    ChrTalk(
        0x1F,
        (
            "I wonder if the sister\x01",
            "knows a simple diet or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Hey, quit asking me\x01",
            "stupid things during\x01",
            "lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "She'll get mad at us\x01",
            "again, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Haha, you two there. Be\x01",
            "quiet during lessons.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "Okaaay....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "O-Okaaay... (She got mad\x01",
            "at me too...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_42_DC3A end

    def Function_43_DD68(): pass

    label("Function_43_DD68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_DD9B")

    ChrTalk(
        0xFE,
        (
            "We aren't really tired,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC8")

    label("loc_DD9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_DDC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDB6")
    Call(0, 42)
    Jump("loc_DDC8")

    label("loc_DDB6")


    ChrTalk(
        0xFE,
        "(S-Sorry...)\x02",
    )

    CloseMessageWindow()

    label("loc_DDC8")

    TalkEnd(0xFE)
    Return()

    # Function_43_DD68 end

    def Function_44_DDCC(): pass

    label("Function_44_DDCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_DE60")

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad learned\x01",
            "about independence\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess there are things\x01",
            "you can't get just by\x01",
            "reading Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEB8")

    label("loc_DE60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_DEB8")

    ChrTalk(
        0xFE,
        "I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Marble's lessons\x01",
            "are really easy to\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEB8")

    TalkEnd(0xFE)
    Return()

    # Function_44_DDCC end

    def Function_45_DEBC(): pass

    label("Function_45_DEBC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "As expected, senior\x01",
            "class lessons are\x01",
            "difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should've prepared\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_DEBC end

    def Function_46_DF1D(): pass

    label("Function_46_DF1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFEA")

    ChrTalk(
        0xFE,
        (
            "Oh, that KeA kid isn't\x01",
            "coming today, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, come to think of\x01",
            "it, she attends only\x01",
            "natural sciences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, I wanted to gaze at\x01",
            "her cute figure from\x01",
            "behind today too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E062")

    label("loc_DFEA")


    ChrTalk(
        0xFE,
        (
            "KeA always sits in front\x01",
            "of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking classes while gazing\x01",
            "at the cute back of her\x01",
            "head is pretty enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E062")

    TalkEnd(0xFE)
    Return()

    # Function_46_DF1D end

    def Function_47_E066(): pass

    label("Function_47_E066")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2E5")
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
            "#00005FAunt... So this is where\x01",
            "you were.\x02\x03",
            "#00000FCecil came to the\x01",
            "Support Section just\x01",
            "moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, is that so? I must\x01",
            "go see her later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I wonder what\x01",
            "will happen to Crossbell\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Honestly, we're lost, but...\x02\x03",
            "#00000FWhatever shape Crossbell takes,\x01",
            "it won't change the feeling of\x01",
            "wanting to protect it.\x02",
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
        "#00300FWell, you said it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Haha. You've all\x01",
            "become so dependable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, thanks to you, I feel\x01",
            "a little relieved. Thank\x01",
            "you for speaking with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 5)
    Jump("loc_E3D1")

    label("loc_E2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E394")

    ChrTalk(
        0xFE,
        (
            "I am going to stay here\x01",
            "a while longer to pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what will\x01",
            "happen in the future,\x01",
            "but...\x02",
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
    Jump("loc_E3D1")

    label("loc_E394")

    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "O Goddess of the Sky...\x01",
            "Please protect us all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3D1")

    TalkEnd(0xFE)
    Return()

    # Function_47_E066 end

    def Function_48_E3D5(): pass

    label("Function_48_E3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3E7")
    Call(0, 49)
    Jump("loc_E490")

    label("loc_E3E7")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sister Ries appears to\x01",
            "be greeting the\x01",
            "Archbishop inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F...Let's go pick up KeA for\x01",
            "now. She should be in the\x01",
            "Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_E490")

    Return()

    # Function_48_E3D5 end

    def Function_49_E491(): pass

    label("Function_49_E491")

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
            "#12P#00100FThis is Archbishop\x01",
            "Eralda's room, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHmm? I hear voices\x01",
            "inside.\x02",
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
            "#6P#13800F...And so, starting\x01",
            "today, I will be in your\x01",
            "care.\x02\x03",
            "#13803FI may be inexperienced,\x01",
            "but I am looking forward\x01",
            "to your support...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Wait. Your surname,\x01",
            ""Argent"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PArteria did contact us saying\x01",
            "a novice would be coming, but\x01",
            "who could have thought...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#13803F...Is there any problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...No, nevermind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI welcome you, Sister\x01",
            "Ries. Please do your\x01",
            "best from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#13802FThank you very much.\x02\x03",
            "#13804FI shall work humbly, in\x01",
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
            "#6P#10105FThat's... Ries' voice.\x01",
            "We just met her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIt looks like she's\x01",
            "introducing herself to\x01",
            "the archbishop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00103F...Everyone. It's not ok\x01",
            "to eavesdrop.\x02\x03",
            "#00100FLet's go pick up KeA.\x02",
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

    # Function_49_E491 end

    def Function_50_E955(): pass

    label("Function_50_E955")

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
        "#6P#00000FAh, no, that's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FKeA, are you doing your\x01",
            "best studying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01110FYeah!\x02\x03",
            "#01109FKeA studies lots things every\x01",
            "day, and doing it with Ryｹ,\x01",
            "Henri and the others is fun too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00102FHaha. I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHmm, she seems to have\x01",
            "fit right in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FYes, we were worried at\x01",
            "first, but... I guess we\x01",
            "didn't need to.\x02\x03",
            "#00000FKeep doing your best,\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#01109FYeah! Do your best too,\x01",
            "ok guys!?\x02",
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

    # Function_50_E955 end

    def Function_51_EC22(): pass

    label("Function_51_EC22")

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
        "#00005F#5PHuh?\x02",
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
            "#00008F#5PWell, class is still in\x01",
            "session...\x02",
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
            "#01105F#5PUmm, so this formula\x01",
            "becomes this, and after\x01",
            "that...\x02\x03",
            "#01101FHmm... (*scribble\x01",
            "scribble*)\x02\x03",
            "#01109FYes! The answer is 512\x01",
            "square selge!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(837, 0, 100, 0)
    SetChrName("Senior Students")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4SWoah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#5PYes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe formula you used was\x01",
            "unique, though. Did you\x01",
            "come up with that yourself?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)

    ChrTalk(
        0x153,
        (
            "#01104F#11PEhehe, doing it this way\x01",
            "felt better somehow.\x02\x03",
            "#01110FWas KeA wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, no. That was a\x01",
            "wonderful solution.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P...Everyone, an official formula\x01",
            "is just one guideline to derive\x01",
            "the correct solution, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PChallenge yourselves to come\x01",
            "up with unique solutions\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("Senior Students")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4SYes ma'am!\x02",
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
            "#00108F#5PA senior Sunday School\x01",
            "class, isn't it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PKeA is amazing...\x02\x03",
            "#10106FI don't even think I\x01",
            "could solve a problem\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PIt's mid-level math.\x02\x03",
            "#10302FHmm. That's quite the\x01",
            "splendid solution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, that's our KeA for\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PRight, that level of\x01",
            "math is nothing for\x01",
            "KeA...\x02",
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
        "#6P#00011F#4S#1K─That's not it!\x02",
    )


    ChrTalk(
        0x102,
        "#5P#00105F#4S#1K─That's not it!\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x105,
        "#10306F#5PJeez. Calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PF-For now, let's wait\x01",
            "until the end of KeA's\x01",
            "lesson.\x02",
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

    def lambda_F540():
        OP_9B(0x0, 0x20, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_F540)
    Sleep(1000)
    TurnDirection(0x1E, 0x1F, 500)
    Sleep(300)

    def lambda_F562():
        OP_93(0x1F, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_F562)
    Sleep(50)

    def lambda_F572():
        OP_93(0x1E, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_F572)
    WaitChrThread(0x1F, 2)

    def lambda_F583():
        OP_9B(0x0, 0x1F, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_F583)
    Sleep(50)
    WaitChrThread(0x1E, 2)

    def lambda_F59F():
        OP_9B(0x0, 0x1E, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_F59F)
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
        "Umm, KeA?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_F608():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_F608)
    Sleep(50)

    def lambda_F618():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F618)
    OP_68(149000, 1000, 7700, 2000)
    MoveCamera(317, 22, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(35000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "My, it's all of you...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        (
            "#01105F#3598V#11P#30WHuuuh? Why is everyone\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0E)
    OP_C9(0x1, 0x80000000)
    OP_68(151000, 1000, 12400, 5000)
    MoveCamera(312, 25, 0, 5000)
    SetCameraDistance(30000, 5000)

    def lambda_F6DF():
        OP_95(0xFE, 151400, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6DF)
    Sleep(100)

    def lambda_F6FC():
        OP_95(0xFE, 150600, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6FC)
    Sleep(500)

    def lambda_F719():
        OP_95(0xFE, 151400, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F719)
    Sleep(100)

    def lambda_F736():
        OP_95(0xFE, 150600, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F736)
    WaitChrThread(0x101, 1)

    def lambda_F754():
        OP_95(0xFE, 151400, 0, 11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F754)
    WaitChrThread(0x102, 1)

    def lambda_F772():
        OP_95(0xFE, 150600, 0, 11300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F772)
    WaitChrThread(0x109, 1)

    def lambda_F790():
        OP_95(0xFE, 151400, 0, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F790)
    WaitChrThread(0x105, 1)

    def lambda_F7AE():
        OP_95(0xFE, 150600, 0, 9800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F7AE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, we came to get you\x01",
            "because you were late,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00102F#5PM-More importantly, KeA.\x01",
            "Why are you in a senior\x01",
            "class?\x02",
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
            "#01108FUmm, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PCould it be that you\x01",
            "haven't told Lloyd and\x01",
            "the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01106F#11P......(*nods*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PLooks like she's an\x01",
            "excellent student.\x02\x03",
            "#10300FSo much that she can\x01",
            "keep up with a senior\x01",
            "class.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 350)

    ChrTalk(
        0x8,
        (
            "#11PYes. She said she wanted to, so I've\x01",
            "been having her join the senior\x01",
            "class for a little while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POnly for math and\x01",
            "natural sciences,\x01",
            "though.\x02",
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
            "#00103F#5PTo think that KeA is\x01",
            "that smart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01112F#11PUmm... Sorry for not\x01",
            "telling you...?\x02\x03",
            "#01106FEven though KeA's still\x01",
            "a kid she studies math\x01",
            "and stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha. That's nothing to\x01",
            "apologize for, you know?\x02\x03",
            "#00002FIf you're interested in\x01",
            "that stuff, I won't\x01",
            "object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PRight... I'd like her to\x01",
            "grow her intellectual\x01",
            "curiosity.\x02\x03",
            "#00102FHmm. I'm in favor as\x01",
            "well.\x02",
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
            "#00004F#6PBut you have to take\x01",
            "classes with Ryu and the\x01",
            "others too, ok?\x02\x03",
            "#00000FSunday School isn't just\x01",
            "for studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#11PYeah, I know!\x02\x03",
            "It's also fun to teach\x01",
            "Ryｹ and Momo what they\x01",
            "don't get!\x02",
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
        "#10102F#6PKeA, you're so smart!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHaha. She's even helping\x01",
            "me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PShe joins the senior\x01",
            "class about once a\x01",
            "week...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll keep an eye on her\x01",
            "too, so please don't\x01",
            "worry.\x02",
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
        (
            "#00104F#6PThanks for all your\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#6PHaha... Well that's\x01",
            "settled then.\x02\x03",
            "#10302FThen, should we return\x01",
            "to the Support Section\x01",
            "before the sun sets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, let's.\x02\x03",
            "#00000FMiss Marble, please\x01",
            "excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PThank you for your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0x153,
        "#01110F#12PBye, Miss Marble!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    ChrTalk(
        0x8,
        (
            "#5PHaha, goodbye KeA.\x01",
            "Careful on your way\x01",
            "home.\x02",
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

    # Function_51_EC22 end

    def Function_52_FF9F(): pass

    label("Function_52_FF9F")

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
            "#00005F#5PThere's senior class\x01",
            "lessons at this hour,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5PIt seems that KeA is not\x01",
            "attending today...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Majestic Voice",
        (
            "#4P─Do you all need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_10218():

        label("loc_10218")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_10218")

    QueueWorkItem2(0x101, 2, lambda_10218)

    def lambda_1022A():

        label("loc_1022A")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_1022A")

    QueueWorkItem2(0x102, 2, lambda_1022A)

    def lambda_1023C():

        label("loc_1023C")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_1023C")

    QueueWorkItem2(0x103, 2, lambda_1023C)

    def lambda_1024E():

        label("loc_1024E")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_1024E")

    QueueWorkItem2(0x104, 2, lambda_1024E)

    def lambda_10260():

        label("loc_10260")

        TurnDirection(0x109, 0x9, 500)
        Yield()
        Jump("loc_10260")

    QueueWorkItem2(0x109, 2, lambda_10260)

    def lambda_10272():

        label("loc_10272")

        TurnDirection(0x105, 0x9, 500)
        Yield()
        Jump("loc_10272")

    QueueWorkItem2(0x105, 2, lambda_10272)
    Sleep(500)
    OP_68(7420, 1000, 2480, 4000)

    def lambda_10298():
        OP_9B(0x0, 0x9, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10298)

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
            "#5PIf I remember\x01",
            "correctly... You're from\x01",
            "the Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PDo you need Sister\x01",
            "Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PY-Yes.\x02\x03",
            "#00000FUmm, we'd like to\x01",
            "consult with her about a\x01",
            "certain plant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PHm, a plant, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIs it a medicinal herb\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PNo, that's not the case,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PWe heard it might appear\x01",
            "in the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHmm. In that case, you\x01",
            "can ask me about it\x01",
            "instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI may not look it, but I'm\x01",
            "knowledgeable about medicinal\x01",
            "herbs and plants in general.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10639")

    ChrTalk(
        0x101,
        (
            "#00002F#12PAh, now that you mention it...\x01",
            "You really helped us out with\x01",
            "the Lupinus Grass case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1065B")

    label("loc_10639")


    ChrTalk(
        0x101,
        "#00005F#12POh, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_1065B")


    ChrTalk(
        0x9,
        (
            "#5PWell, if you like, that\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI'm retiring to my\x01",
            "office. Come visit, if\x01",
            "you like.\x02",
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

    def lambda_10705():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10705)
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
        "#00001F#12PH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PStrict as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PBut since we're here,\x01",
            "why don't we try\x01",
            "consulting with him?\x02",
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

    # Function_52_FF9F end

    def Function_53_10863(): pass

    label("Function_53_10863")

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
            "#00000F#2P─Pardon us. We're from\x01",
            "the Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, do come in.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(100000, 1000, 8500, 3000)
    MoveCamera(315, 22, 0, 3000)
    SetCameraDistance(30000, 3000)

    def lambda_10A0F():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10A0F)
    Sleep(100)

    def lambda_10A27():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10A27)
    Sleep(100)

    def lambda_10A3F():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10A3F)
    Sleep(100)

    def lambda_10A57():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10A57)
    Sleep(100)

    def lambda_10A6F():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10A6F)
    Sleep(100)

    def lambda_10A87():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10A87)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11PHmph. Let's hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA plant that appears in\x01",
            "the Testaments, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, we're still not\x01",
            "certain, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PFirst, we'll tell you\x01",
            "what has happened thus\x01",
            "far.\x02",
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
            "#11P...The presence of time,\x01",
            "space and mirage elements\x01",
            "and mysterious monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PAnd they're different from the\x01",
            "monsters at the tower and temple\x01",
            "that were previously reported...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#5P(Ah, come to think of\x01",
            "it...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5P(She said that they\x01",
            "tried to consult with\x01",
            "the Church before.)\x02",
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
            "#11P...Those flowers. Do you\x01",
            "have them with you now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAh, yes. They lost their\x01",
            "light, but...\x02",
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
        (
            "#10107FAs we thought, you know\x01",
            "something!?\x02",
        )
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
            "#11P─No.\x02\x03",
            "Unfortunately, I have no\x01",
            "idea.\x02",
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
        "#00011F#6PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PHey now! How come!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PNo matter how you think about\x01",
            "it, that reaction says you do\x01",
            "have some idea about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI said, I don't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough I was the one who\x01",
            "called you, I'll ask you\x01",
            "to leave now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt may not look it, but\x01",
            "I am busy.\x02",
        )
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
            "#11POh, and asking Sister\x01",
            "Marble is useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlthough she is extremely\x01",
            "knowledgeable, she probably\x01",
            "won't know about those flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConversely, if she did know\x01",
            "about them, that would be a\x01",
            "bit of a problem.\x02",
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
            "#10302F#6PIf you think about it, you\x01",
            "could only make that statement\x01",
            "if you did know them, no?\x02",
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
            "#11PEven if Commander Sonya\x01",
            "of the CGF came here in\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PTch...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(250)

    ChrTalk(
        0x102,
        (
            "#00106F#12P...Lloyd, let's excuse\x01",
            "ourselves.\x02\x03",
            "#00108FFurther questioning is\x01",
            "pointless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...Understood.\x02",
    )

    CloseMessageWindow()

    def lambda_1133C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1133C)
    Sleep(50)

    def lambda_1134C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1134C)
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
        (
            "#11PYes, do not think ill of\x01",
            "me.\x02",
        )
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

    def lambda_114D9():
        OP_95(0x101, 50000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_114D9)

    def lambda_114F3():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_114F3)
    OP_68(49820, 1000, 3570, 7000)
    MoveCamera(315, 20, 0, 7000)
    OP_6E(300, 7000)
    SetCameraDistance(30000, 7000)
    Sleep(500)

    def lambda_11535():
        OP_95(0x102, 48800, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11535)

    def lambda_1154F():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1154F)
    Sleep(500)

    def lambda_11563():
        OP_95(0x103, 51000, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11563)

    def lambda_1157D():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1157D)
    Sleep(500)

    def lambda_11591():
        OP_95(0x104, 50000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11591)

    def lambda_115AB():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_115AB)
    Sleep(500)

    def lambda_115BF():
        OP_95(0x109, 48750, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_115BF)

    def lambda_115D9():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_115D9)
    Sleep(500)

    def lambda_115ED():
        OP_95(0x105, 50000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_115ED)

    def lambda_11607():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_11607)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x0, 0x1F4)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    def lambda_1163E():
        OP_95(0x105, 50750, 0, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1163E)
    WaitChrThread(0x101, 1)

    def lambda_1165C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1165C)
    WaitChrThread(0x102, 1)

    def lambda_1166D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1166D)
    WaitChrThread(0x103, 1)

    def lambda_1167E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1167E)
    WaitChrThread(0x104, 1)

    def lambda_1168F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1168F)
    WaitChrThread(0x109, 1)

    def lambda_116A0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_116A0)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0x101, 500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#11PWait just a second\x01",
            "here...\x02\x03",
            "#00301FWasn't he just a tiny\x01",
            "bit too mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PR-Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PHowever, it didn't seem there\x01",
            "was anything he felt\x01",
            "especially guilty about.\x02\x03",
            "#00208FIt was like he thought hiding\x01",
            "something from us was the\x01",
            "correct course of action...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Most likely there's\x01",
            "some kind of taboo.\x02\x03",
            "#00008FOne so great, even Miss\x01",
            "Marble doesn't know\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11POh man. When you put it that way,\x01",
            "it just makes me want to know it\x01",
            "that much more, you know.\x02\x03",
            "#10302FIf it's come to this, should we\x01",
            "read the entire Testaments start\x01",
            "to finish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBut if you consider the\x01",
            "entire Testaments, they're\x01",
            "extensive...\x02\x03",
            "#00108FI read them a long time\x01",
            "ago, so I don't know where\x01",
            "that passage would be...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    Sound(103, 0, 60, 0)

    NpcTalk(
        0xA,
        "Girl's Voice",
        (
            "#1P#2S...Those details\x01",
            "probably won't appear in\x01",
            "any normal Testaments.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11A24():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_11A24)
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

    def lambda_11B12():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11B12)
    Sleep(0)

    def lambda_11B22():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11B22)
    Sleep(0)

    def lambda_11B32():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11B32)
    Sleep(0)

    def lambda_11B42():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11B42)
    Sleep(0)

    def lambda_11B52():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11B52)
    Sleep(0)

    def lambda_11B62():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11B62)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_11B87():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_11B87)
    OP_95(0xA, 56800, 0, 3000, 2000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5PYou're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PR-Ries...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F#12P(*shh*, quiet down...)\x02\x03",
            "#04400F(...Leave the chapel and\x01",
            "come to the dormitory.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    OP_9B(0x0, 0xA, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_11C57():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_11C57)
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

    def lambda_11D31():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11D31)

    def lambda_11D3E():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11D3E)
    Sleep(50)

    def lambda_11D4E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11D4E)
    Sleep(50)

    def lambda_11D5E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11D5E)
    Sleep(50)

    def lambda_11D6E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11D6E)
    Sleep(50)

    def lambda_11D7E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11D7E)
    Sleep(50)

    def lambda_11D8E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11D8E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x109,
        "#10101F#5P(W-What do we do?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11E8A")

    ChrTalk(
        0x101,
        (
            "#00003F#6P(If I recall, she said\x01",
            "she's a member of the\x01",
            ""Gralsritter"...)\x02\x03",
            "#00001F(Anyway, let's try going\x01",
            "there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5P(Yes, I think that's\x01",
            "alright.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F32")

    label("loc_11E8A")


    ChrTalk(
        0x102,
        (
            "#00103F#5P(...We can trust her.)\x02\x03",
            "#00101F(Anyway, it seems she has\x01",
            "something to say to us, so\x01",
            "let's try going there.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F#6P(...Yeah, understood.)\x02",
    )

    CloseMessageWindow()

    label("loc_11F32")

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

    # Function_53_10863 end

    def Function_54_11F77(): pass

    label("Function_54_11F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12114")

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
            "#00003F(I wonder if she'd be\x01",
            "our sister for the\x01",
            "pageant...?)\x02\x03",
            "#00000FUmm, excuse me. I'd like\x01",
            "to ask you something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Sister Hatina to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            "...U-Umm... To think I'd\x01",
            "be invited...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, I'm sorry. I\x01",
            "have another job to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see... Then, it can't\x01",
            "be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 2)
    Jump("loc_12191")

    label("loc_12114")


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
            "I dislike the air of a\x01",
            "beauty pageants, so... I'll\x01",
            "have to refuse, this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12191")

    TalkEnd(0xD)
    Return()

    # Function_54_11F77 end

    def Function_55_12195(): pass

    label("Function_55_12195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1242A")

    ChrTalk(
        0x8,
        (
            "Oh... Everyone, is\x01",
            "something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Miss Marble is a sister\x01",
            "too, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(A-As you can imagine, we\x01",
            "can't invite her to\x01",
            "something like a pageant...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Haha, could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That you intend to\x01",
            "invite me to the\x01",
            "pageant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a rumor going\x01",
            "around that such a thing\x01",
            "is being planned.\x02",
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
        "#00012FU-Umm... So you knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu, I'm joking. I\x01",
            "have a certain age, you\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Try asking the other\x01",
            "sisters. I'm sure\x01",
            "someone will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F*sigh*... We're no match\x01",
            "for you, Miss Marble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 3)
    Jump("loc_124CD")

    label("loc_1242A")


    ChrTalk(
        0x8,
        (
            "Try asking the other sisters\x01",
            "about the pageant... I'm\x01",
            "sure someone will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. If only I were a\x01",
            "little younger, I would've\x01",
            "participated though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124CD")

    TalkEnd(0x8)
    Return()

    # Function_55_12195 end

    def Function_56_124D1(): pass

    label("Function_56_124D1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_END)), "loc_12682")

    ChrTalk(
        0xA,
        (
            "#04405FOh, everyone. Did you\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(A "sister" for the\x01",
            "pageant... Wouldn't she\x01",
            "be fine?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(You're right... Let's\x01",
            "try asking her.)\x02\x03",
            "#00000FThere's something I'd\x01",
            "like to discuss with\x01",
            "you, Ries...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AC7")

    label("loc_12682")


    ChrTalk(
        0x101,
        (
            "#00000FRies, it looks like\x01",
            "you're helping with\x01",
            "mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04400FIndeed I am.\x02\x03",
            "#04400FThere's an especially\x01",
            "large number of visitors\x01",
            "for today's mass.\x02\x03",
            "Their homes have been\x01",
            "attacked, and they fear\x01",
            "for their lives...\x02\x03",
            "#04403FI myself understand how\x01",
            "they feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FRies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(...Maybe something like\x01",
            "this happened to Ries\x01",
            "long ago.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04400F(This is just between you and me...\x01",
            "Due to the effects of this incident,\x01",
            "mobilization of the Congregation for\x01",
            "the Sacraments has been confirmed.)\x02\x03",
            "#04403F(...While I'm in Crossbell, I intend\x01",
            "to gather as much intelligence as I\x01",
            "can.)\x02\x03",
            "#04400F(You all should act carefully.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(While in Crossbell...\x01",
            "you say?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Understood. Take care\x01",
            "of yourself as well,\x01",
            "Ries.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04405FBy the way... Did you\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FU-Umm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Haha, I almost forgot.\x01",
            "Wouldn't she make a good\x01",
            "sister for the pageant?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(You're right... Since\x01",
            "we're here, let's try\x01",
            "asking her.)\x02\x03",
            "#00000FThere's something I'd\x01",
            "like to discuss with\x01",
            "you, Ries...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)

    label("loc_12AC7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Sister Ries to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405FA pageant...is it?\x02\x03",
            "#04402FI think the charity event\x01",
            "is great, but... I'm\x01",
            "rather busy today.\x02\x03",
            "#04406FAnd, for a clergyman to\x01",
            "participate to such an\x01",
            "event would be a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FW-Well, that's also\x01",
            "true...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTch, and I wanted to see\x01",
            "dear Ries standin' on\x01",
            "the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FHaha... But, I think the\x01",
            "event itself is great.\x02\x03",
            "Aside from the pageant,\x01",
            "what other things are\x01",
            "being done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, aside from that\x01",
            "there's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FA piano concert and a\x01",
            "buffet party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#04403F...Everyone, can I ask\x01",
            "you to let me take part\x01",
            "in that pageant?\x02",
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
            "#00012FU-Umm... I don't mind.\x02\x03",
            "#00004F(Was she reeled in by\x01",
            "the buffet party?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F(Ahaha, looks that way.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04402FThen, I have to help\x01",
            "with mass for a while\x01",
            "longer.\x02\x03",
            "#04404FWhen the program starts,\x01",
            "please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we understand.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FB8")

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

    label("loc_12FB8")

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

    # Function_56_124D1 end

    def Function_57_12FEB(): pass

    label("Function_57_12FEB")

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
        (
            "Oh... Do you need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you'd like a sermon,\x01",
            "I can make time for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#00005FN-No. That's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F(The "light of the\x01",
            "greatest Goddess" from\x01",
            "Phantom Thief B's card...)\x02",
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
            "#6P#N#00100F(It's probably referring\x01",
            "to the light from this\x01",
            "stained-glass window.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#6P#N#00203F(In that case, "he whose\x01",
            "back basks" in that\x01",
            "light is...)\x02",
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
        (
            "I'm not sure what's\x01",
            "going on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have something to\x01",
            "say, how about saying it\x01",
            "clearly, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FU-Umm, then...\x02\x03",
            "#00000FArchbishop Eralda. May\x01",
            "we search under that\x01",
            "podium?\x02",
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
            "#6P#10300FDon't worry. We won't do\x01",
            "anything suspicious.\x02",
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
            "Lloyd and the others explained\x01",
            "the situation to Archbishop\x01",
            "Eralda and searched the podium.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FThere it is!\x02",
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
            "A card was affixed to\x01",
            "the back of the trunk.\x07\x00\x02",
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
            "Search the "iron road that runs under\x01",
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
            "#6P#00100FThis one is "Mistel".\x01",
            "Bell loves this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FNo doubt. ...With this,\x01",
            "we finally have three of\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just when did such a\x01",
            "thing get under there!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sometimes I'm not here\x01",
            "due to business, but not\x01",
            "for that long, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHonestly speaking, I can\x01",
            "only say it's an act of\x01",
            "the Goddess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FThe card seems difficult\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FAs for "protectors", it has\x01",
            "the meaning of "guardians",\x01",
            "just like the characters say.\x02\x03",
            "#00103FAnd regarding "western", he\x01",
            "might mean those who protect\x01",
            "the western side of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FThen there's the "iron road"\x01",
            "that runs under the feet of\x01",
            "the "guardians", huh.\x02\x03",
            "#10106FHmm, I still don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt might be another\x01",
            "metaphor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, that's probably\x01",
            "it.\x02\x03",
            "#00000FAnyhow, let's retrieve\x01",
            "this trunk and search\x01",
            "for the next one.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#11PPhantom Thief B, you say? I've\x01",
            "heard the name, but I had no\x01",
            "idea he was such a scoundrel.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13B5A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13B5A)
    Sleep(50)

    def lambda_13B6A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13B6A)

    ChrTalk(
        0x9,
        (
            "#11PAs a servant of the\x01",
            "Great Goddess, I cannot\x01",
            "forgive such a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLadies and gentlemen,\x01",
            "please. Do whatever it\x01",
            "takes to capture him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FWe'll do our best.\x02",
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

    # Function_57_12FEB end

    SaveToFile()

Try(main)
