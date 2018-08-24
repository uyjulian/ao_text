from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0020.bin",                # FileName
        "t0020",                    # MapName
        "t0020",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0020",                  # 0
        "Old Man Reoir",          # 1
        "Jake",                   # 2
        "Gｷfan",                 # 3
        "Sealy",                  # 4
        "Keith",                  # 5
        "Alfred",                 # 6
        "Aretha",                 # 7
        "Camille",                # 8
        "Pooley",                 # 9
        "Stefan",                 # 10
        "Derrick",                # 11
        "Ange",                   # 12
        "Sister Hatina",          # 13
        "Harold",                 # 14
        "Sophia",                 # 15
        "Colin",                  # 16
        "Father Kevin",           # 17
        "Sister Ries",            # 18
        "Bracer Ling",            # 19
        "Bracer Eolia",           # 20
        "Bracer Scott",           # 21
        "Chiruru",                # 22
        "Food",                   # 23
        "Food",                   # 24
        "Food",                   # 25
        "Food",                   # 26
        "Food",                   # 27
        "Food",                   # 28
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch25200.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch24402.itc",                   # 04
        "chr/ch21002.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch22702.itc",                   # 07
        "chr/ch24600.itc",                   # 08
        "chr/ch24700.itc",                   # 09
        "chr/ch20600.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch32302.itc",                   # 0C
        "chr/ch24300.itc",                   # 0D
        "chr/ch25500.itc",                   # 0E
        "chr/ch09300.itc",                   # 0F
        "chr/ch32002.itc",                   # 10
        "chr/ch32102.itc",                   # 11
        "chr/ch09400.itc",                   # 12
        "chr/ch09402.itc",                   # 13
        "chr/ch07202.itc",                   # 14
        "chr/ch09302.itc",                   # 15
        "chr/ch11402.itc",                   # 16
        "chr/ch11500.itc",                   # 17
        "chr/ch27202.itc",                   # 18
        "chr/ch20502.itc",                   # 19
    ))

    DeclNpc(4294926767, 0,       3470,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294918936, 0,       769,     90,   261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294967257, 0,       6039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(699,     0,       2049,    90,   261,  0x0, 0,   3,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(7849,    180,     2460,    0,    261,  0x0, 0,   4,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294965237, 180,     4000,    0,    261,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(139320,  500,     360,     180,  261,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(78019,   0,       4294966926, 0,    389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(79169,   0,       4294967167, 315,  389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(76849,   0,       4294967126, 90,   389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(112559,  0,       4294966787, 270,  389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(141600,  0,       4294966296, 180,  389,  0x0, 0,   13,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(78000,   189,     1500,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(112559,  0,       4294966787, 270,  389,  0x0, 0,   15,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(71449,   0,       4294965696, 0,    389,  0x0, 0,   18,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(74000,   100,     4294965546, 0,    388,  0x0, 0,   20,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(69290,   500,     790,     180,  452,  0x0, 0,   22,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(69379,   0,       4294966106, 0,    453,  0x0, 0,   23,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(4294964787, 180,     1179,    270,  389,  0x0, 0,   16,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(4294963916, 189,     4294966486, 0,    389,  0x0, 0,   17,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(4294964787, 180,     1179,    270,  452,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(3549,    180,     4294965296, 70,   452,  0x0, 0,   25,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(4294963796, 800,     4294966947, 0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294962577, 800,     289,     0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294963106, 800,     1519,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294964146, 800,     699,     0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294962916, 800,     4294966947, 0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294962557, 800,     1000,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(270,     0,       4460,    1000,    4294967256, 1500,    6040,    0x007E, 0,  11, 0x0000)
    DeclActor(4294920936, 0,       30,      1000,    4294918936, 1500,    770,     0x007E, 0,  9,  0x0000)
    DeclActor(86250,   0,       2050,    1200,    86250,   2500,    2050,    0x007C, 0,  6,  0x0000)
    DeclActor(6400,    0,       8900,    1200,    6400,    1700,    8900,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1380, 0)                                       # 0

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_6CD",          # 02, 2
        "Function_3_6F8",          # 03, 3
        "Function_4_723",          # 04, 4
        "Function_5_B30",          # 05, 5
        "Function_6_BA8",          # 06, 6
        "Function_7_C56",          # 07, 7
        "Function_8_D6A",          # 08, 8
        "Function_9_1DEF",         # 09, 9
        "Function_10_1DF3",        # 0A, 10
        "Function_11_2DC2",        # 0B, 11
        "Function_12_2DC6",        # 0C, 12
        "Function_13_4254",        # 0D, 13
        "Function_14_5010",        # 0E, 14
        "Function_15_5149",        # 0F, 15
        "Function_16_5E9D",        # 10, 16
        "Function_17_71E6",        # 11, 17
        "Function_18_7CD0",        # 12, 18
        "Function_19_7D5A",        # 13, 19
        "Function_20_7DC8",        # 14, 20
        "Function_21_8078",        # 15, 21
        "Function_22_8600",        # 16, 22
        "Function_23_86A6",        # 17, 23
        "Function_24_87BE",        # 18, 24
        "Function_25_88EF",        # 19, 25
        "Function_26_95D1",        # 1A, 26
        "Function_27_9761",        # 1B, 27
        "Function_28_979B",        # 1C, 28
        "Function_29_97D5",        # 1D, 29
        "Function_30_9A40",        # 1E, 30
        "Function_31_9E02",        # 1F, 31
        "Function_32_A2E6",        # 20, 32
        "Function_33_A4C7",        # 21, 33
        "Function_34_A69D",        # 22, 34
        "Function_35_A761",        # 23, 35
        "Function_36_B675",        # 24, 36
        "Function_37_B781",        # 25, 37
        "Function_38_B929",        # 26, 38
        "Function_39_C81A",        # 27, 39
        "Function_40_CBAF",        # 28, 40
        "Function_41_D819",        # 29, 41
        "Function_42_DD65",        # 2A, 42
        "Function_43_E1C4",        # 2B, 43
        "Function_44_E6DA",        # 2C, 44
        "Function_45_F383",        # 2D, 45
        "Function_46_104BD",       # 2E, 46
        "Function_47_10506",       # 2F, 47
        "Function_48_1054F",       # 30, 48
        "Function_49_10598",       # 31, 49
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CC")
    OP_95(0xFE, 700, 0, 2050, 2000, 0x0)
    OP_95(0xFE, 6210, 0, 2640, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 2810, 0, 1030, 2000, 0x0)
    OP_95(0xFE, 3120, 0, -560, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -2050, 0, -820, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    Jump("Function_1_61C")

    label("loc_6CC")

    Return()

    # Function_1_61C end

    def Function_2_6CD(): pass

    label("Function_2_6CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F7")
    OP_94(0xFE, 0x229CA, 0xFFFFF754, 0x23212, 0xFFFFFF9C, 0x3E8)
    Sleep(250)
    Jump("Function_2_6CD")

    label("loc_6F7")

    Return()

    # Function_2_6CD end

    def Function_3_6F8(): pass

    label("Function_3_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_722")
    OP_94(0xFE, 0x8AAC, 0x3E8, 0xB5A4, 0xFFFFFC7C, 0x7D0)
    Sleep(250)
    Jump("Function_3_6F8")

    label("loc_722")

    Return()

    # Function_3_6F8 end

    def Function_4_723(): pass

    label("Function_4_723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76B")
    SetChrChipByIndex(0x1A, 0x10)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0x11)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_76B")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0x17, 0x14)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7D8")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x16)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_B15")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_801")
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 78010, 0, 2060, 0)
    Jump("loc_B15")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_887")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x15, 0x15)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 82040, 180, -1400, 45)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 81720, 0, 220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C")
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)

    label("loc_86C")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 73950, 400, 800, 180)
    Jump("loc_B15")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8E8")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 71500, 0, 0, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 73950, 400, 800, 180)
    Jump("loc_B15")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_923")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 142940, 0, -770, 180)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_B15")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_931")
    Jump("loc_B15")

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_964")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_B15")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_B15")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9A9")
    SetChrPos(0xE, 41000, 0, 0, 180)
    BeginChrThread(0xE, 0, 0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A4")
    ClearChrFlags(0x12, 0x80)

    label("loc_9A4")

    Jump("loc_B15")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9E8")
    SetChrPos(0xE, 73600, 0, -960, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2")
    SetChrFlags(0xD, 0x10)

    label("loc_9D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9E3")
    ClearChrFlags(0x12, 0x80)

    label("loc_9E3")

    Jump("loc_B15")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A9E")
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x18)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x19)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    SetChrPos(0xE, 41000, 0, 0, 180)
    BeginChrThread(0xE, 0, 0, 3)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 7850, 0, 5660, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A72")
    SetChrFlags(0xD, 0x10)

    label("loc_A72")

    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1920, 180, 4000, 0)
    SetChrChipByIndex(0x12, 0xC)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_B15")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_AAC")
    Jump("loc_B15")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ADA")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0xE, 141600, 0, -2000, 0)
    SetChrFlags(0xE, 0x10)
    Jump("loc_B15")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AFE")
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_B15")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B0C")
    Jump("loc_B15")

    label("loc_B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B15")

    label("loc_B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2F")
    Event(0, 45)

    label("loc_B2F")

    Return()

    # Function_4_723 end

    def Function_5_B30(): pass

    label("Function_5_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B42")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B68")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_B68")

    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B94")
    SetMapObjFrame(0xFF, "tuika00", 0x1, 0x1)

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA7")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_BA7")

    Return()

    # Function_5_B30 end

    def Function_6_BA8(): pass

    label("Function_6_BA8")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a car magazine,\x01",
            ""Orbal Car Freak vol.2".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x372, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C52")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Pop\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x372, 1)

    label("loc_C52")

    TalkEnd(0xFF)
    Return()

    # Function_6_BA8 end

    def Function_7_C56(): pass

    label("Function_7_C56")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★Ash Tree Inn Recommended Dish★\x01",
            "    ～　Chef's Omelet Rice　～\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Chef's Omelet Rice\x01",
            "recipe is written here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_D66")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Chef's\x01",
            "Omelet Rice"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D66")

    TalkEnd(0xFF)
    Return()

    # Function_7_C56 end

    def Function_8_D6A(): pass

    label("Function_8_D6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D99")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDC")

    ChrTalk(
        0x8,
        (
            "That mysterious huge tree\x01",
            "appeared, and I'm worried\x01",
            "Jake will wither away, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Harold's comments, on\x01",
            "the other hand, showed\x01",
            "his determination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To a trader, the spirit of commerce is the\x01",
            "most important thing... It's sprouted within\x01",
            "Jake, so I think he'll be alright from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F85")

    label("loc_EDC")


    ChrTalk(
        0x8,
        (
            "To a merchant, the most\x01",
            "important thing is spirit...\x01",
            "It's sprouted within Jake too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know what's going\x01",
            "to happen to Crossbell,\x01",
            "but I've got no regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F85")

    Jump("loc_1DEB")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105C")

    ChrTalk(
        0x8,
        (
            "It seems Harold is properly\x01",
            "supporting his family of\x01",
            "Sophia and Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, Jake is that to\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I retire, finding a\x01",
            "wife for my grandchild\x01",
            "might not be too bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E7")

    label("loc_105C")


    ChrTalk(
        0x8,
        (
            "Hmm, if I could find a\x01",
            "wife to support Jake in\x01",
            "public and private life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Finding a wife for my\x01",
            "grandchild might not be\x01",
            "too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E7")

    Jump("loc_1DEB")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_125A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CA")

    ChrTalk(
        0x8,
        (
            "Harold is negotiating\x01",
            "over supplying the State\x01",
            "Guard with goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if we are self-\x01",
            "sufficient, we still\x01",
            "need a lot of medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That Jake, if he could\x01",
            "do something like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1255")

    label("loc_11CA")


    ChrTalk(
        0x8,
        (
            "That Jake, if he could\x01",
            "be a merchant like\x01",
            "Harold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...No, no. He's gotten some\x01",
            "motivation recently. I\x01",
            "won't scold him too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1255")

    Jump("loc_1DEB")

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0x8,
        (
            "A while back, Jake got\x01",
            "motivation like he's a\x01",
            "different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though he's still\x01",
            "inexperienced, I can\x01",
            "finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to train him again\x01",
            "so I can put up the Jake's\x01",
            "General Store sign someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13E3")

    label("loc_134E")


    ChrTalk(
        0x8,
        (
            "Jake finally got some\x01",
            "motivation. Now I can\x01",
            "rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to train him again\x01",
            "so I can put up the Jake's\x01",
            "General Store sign someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E3")

    Jump("loc_1DEB")

    label("loc_13E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AC")

    ChrTalk(
        0x8,
        (
            "I hurt my lower back\x01",
            "yesterday and it's still\x01",
            "not better. I'm old...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But even so, that\x01",
            "Jake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He looks different than\x01",
            "usual today. Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1510")

    label("loc_14AC")


    ChrTalk(
        0x8,
        (
            "That Jake... He looks\x01",
            "somehow different than\x01",
            "usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if something\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1510")

    Jump("loc_1DEB")

    label("loc_1515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1763")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CF")

    ChrTalk(
        0x8,
        (
            "It seems Minneth is\x01",
            "conducting his final\x01",
            "negotiations today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if his plan with\x01",
            "Derrick is finally starting.\x01",
            "Haha, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C3")

    ChrTalk(
        0x8,
        (
            "When I casually looked out the\x01",
            "window, there were monsters in\x01",
            "the public square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And from the looks of\x01",
            "things, that Minneth seemed\x01",
            "to be manipulating them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And in that shocking\x01",
            "moment, my back gave\x01",
            "out. Ouch...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_175E")

    label("loc_16C3")


    ChrTalk(
        0x8,
        (
            "That Minneth was manipulating\x01",
            "the monsters that appeared in\x01",
            "the public square, wasn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And in that shocking\x01",
            "moment, my back gave\x01",
            "out. Ouch...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175E")

    Jump("loc_1DEB")

    label("loc_1763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_187B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DF")

    ChrTalk(
        0x8,
        (
            "I recently met a man as\x01",
            "promising as Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho, he did a number of\x01",
            "good things for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_17DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17EE")
    Jump("loc_1876")

    label("loc_17EE")


    ChrTalk(
        0x8,
        (
            "The man took a liking to\x01",
            "our village's honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. Surely he's a merchant\x01",
            "who's made a name for\x01",
            "himself. No mistake about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_1DEB")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1946")

    ChrTalk(
        0x8,
        (
            "I'll retire soon, and I\x01",
            "want to leave the store\x01",
            "to Jake, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That guy has no\x01",
            "motivation. He never\x01",
            "does anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. I wish he had some\x01",
            "reason to want to...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19C8")

    label("loc_1946")


    ChrTalk(
        0x8,
        (
            "I wonder if that Jake\x01",
            "has any interest in\x01",
            "taking over the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if I could give\x01",
            "him some reason to want\x01",
            "to...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C8")

    Jump("loc_1DEB")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC0")

    ChrTalk(
        0x8,
        (
            "My back has been acting\x01",
            "up lately. It's about\x01",
            "that time in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to retire and\x01",
            "leave the store to Jake\x01",
            "before too long, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter what I do,\x01",
            "this grandson never\x01",
            "wants to take it over.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B41")

    label("loc_1AC0")


    ChrTalk(
        0x8,
        (
            "Given my age, I want to\x01",
            "leave to store to Jake\x01",
            "and retire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That guy has no\x01",
            "motivation. Things are\x01",
            "looking grim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B41")

    Jump("loc_1DEB")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_1D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(
        0x8,
        (
            "A red-headed stern man...\x01",
            "Oh, I've become friends\x01",
            "with him recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're a strict bunch,\x01",
            "but they bought a lot\x01",
            "from my store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jake was scared of them, but\x01",
            "maybe it's because we don't\x01",
            "have guests too often. Hohoho.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D04")

    label("loc_1C53")


    ChrTalk(
        0x8,
        (
            "The redheaded stern man\x01",
            "was our customer a while\x01",
            "ago. Hohoho...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jake was scared of him, but one mustn't\x01",
            "judge customers by appearances. That\x01",
            "guy has a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D04")

    Jump("loc_1DEB")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(
        0x8,
        (
            "Harold came to do\x01",
            "business with us\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, he's a promising\x01",
            "merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish Jake would follow\x01",
            "his example.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DEB")

    label("loc_1D9B")


    ChrTalk(
        0x8,
        (
            "Harold is a promising\x01",
            "merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish Jake would follow\x01",
            "his example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEB")

    TalkEnd(0xFE)
    Return()

    # Function_8_D6A end

    def Function_9_1DEF(): pass

    label("Function_9_1DEF")

    Call(0, 10)
    Return()

    # Function_9_1DEF end

    def Function_10_1DF3(): pass

    label("Function_10_1DF3")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E52")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E71")
    OP_AF(0x4F)
    Jump("loc_1EA3")

    label("loc_1E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E81")
    OP_AF(0x4E)
    Jump("loc_1EA3")

    label("loc_1E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E91")
    OP_AF(0x4D)
    Jump("loc_1EA3")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EA1")
    OP_AF(0x4C)
    Jump("loc_1EA3")

    label("loc_1EA1")

    OP_AF(0x4B)

    label("loc_1EA3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DB9")

    label("loc_1EB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC6")
    Jump("loc_2DB9")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDE")
    TalkEnd(0x9)
    Return()

    label("loc_1EDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_208A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(
        0x9,
        (
            "When Harold left, he\x01",
            "gave me some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            ""It's the mission of us traders to\x01",
            "do our best for everyone, especially\x01",
            "in times like these", he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I can be of help to someone\x01",
            "by being a merchant, I must do\x01",
            "it, even if it kills me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2085")

    label("loc_2009")


    ChrTalk(
        0x9,
        (
            "If I can be of help to someone\x01",
            "by being a merchant, I must do\x01",
            "it, even if it kills me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Alright... Let's do\x01",
            "this!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2085")

    Jump("loc_2DB9")

    label("loc_208A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_213B")

    ChrTalk(
        0x9,
        (
            "I get the feeling grandpa is\x01",
            "thinking about something\x01",
            "inappropriate for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of times like\x01",
            "these, I'm worried about\x01",
            "the harvest slump.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_213B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_22D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(
        0x9,
        (
            "The other day, I saw Harold\x01",
            "negotiating with the State\x01",
            "Guard. I have a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I'm going to inherit the\x01",
            "store, I need to be able to\x01",
            "do things like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since he's here, I was\x01",
            "thinking of asking\x01",
            "Harold for advice...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22CC")

    label("loc_2248")


    ChrTalk(
        0x9,
        (
            "I already know basically\x01",
            "what my father's going to\x01",
            "say by the look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to be a fine\x01",
            "merchant like Harold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CC")

    Jump("loc_2DB9")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(
        0x9,
        (
            "Hello, and welcome to\x01",
            "Reoir's General Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I recommend honey, our\x01",
            "specialty. I can show\x01",
            "you some, if you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23DB")

    label("loc_2367")


    ChrTalk(
        0x9,
        (
            "...How was that? Pretty\x01",
            "good, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe. I've got to learn\x01",
            "this stuff if I want to\x01",
            "take over the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DB")

    Jump("loc_2DB9")

    label("loc_23E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D2")

    ChrTalk(
        0x9,
        (
            "Grandpa hurt his back\x01",
            "yesterday, see. He should\x01",
            "take the day off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But probably, he's worried\x01",
            "because I'm unreliable and\x01",
            "can't leave the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...*sigh*, what have I\x01",
            "done. I've got to try\x01",
            "harder...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_255F")

    label("loc_24D2")


    ChrTalk(
        0x9,
        (
            "I have no interest or\x01",
            "motivation to take over\x01",
            "the general store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So my grandpa won't\x01",
            "worry, I wonder if I\x01",
            "could try harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255F")

    Jump("loc_2DB9")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2689")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2609")

    ChrTalk(
        0x9,
        (
            "Everyone's talking about\x01",
            "village reform... I\x01",
            "wonder about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't really mind if I\x01",
            "live as I have up until\x01",
            "now. Carefree.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2684")

    label("loc_2609")


    ChrTalk(
        0x9,
        (
            "Grandpa hurt his back\x01",
            "earlier. I wonder if\x01",
            "he's all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, that's right. I have\x01",
            "to bring him a\x01",
            "compress...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2684")

    Jump("loc_2DB9")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2770")

    ChrTalk(
        0x9,
        (
            "I've been seeing a well-\x01",
            "dressed man often in the\x01",
            "village lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That guy said to my grandpa,\x01",
            ""That's an able grandson you\x01",
            "have" and grandpa was delighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected, that's\x01",
            "flattery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27C0")

    label("loc_2770")


    ChrTalk(
        0x9,
        (
            "Grandpa, I'd love it if\x01",
            "you praised me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected, that's\x01",
            "flattery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C0")

    Jump("loc_2DB9")

    label("loc_27C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_297C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BD")

    ChrTalk(
        0x9,
        (
            "Before long, I've got to tell\x01",
            "grandpa clearly. "I've no intention\x01",
            "of taking over the store."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, if I tell him,\x01",
            "he'll probably be\x01",
            "dejected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, whatever. We'll\x01",
            "continue for a while,\x01",
            "just like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2977")

    label("loc_28BD")


    ChrTalk(
        0x9,
        (
            "I get a salary, it's not too busy...\x01",
            "Thinking about part time jobs, the\x01",
            "general store has to be one of the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, whatever. We'll\x01",
            "continue for a while,\x01",
            "just like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2977")

    Jump("loc_2DB9")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A37")

    ChrTalk(
        0x9,
        (
            "It seems Grandpa wants me to\x01",
            "take over the general store,\x01",
            "but... Honestly, it's troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'll\x01",
            "leave for the city and\x01",
            "strike it rich.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AAB")

    label("loc_2A37")


    ChrTalk(
        0x9,
        (
            "Honestly, I'll decline\x01",
            "to take over the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'll\x01",
            "leave for the city and\x01",
            "strike it rich.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAB")

    Jump("loc_2DB9")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_2C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD0")

    ChrTalk(
        0x9,
        (
            "A redheaded, large man? Oh yeah,\x01",
            "there was a man like that a while\x01",
            "back, who brought his friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Grandpa was happy to\x01",
            "turn a profit... But I\x01",
            "was scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those guys weren't respectable.\x01",
            "They were planning something,\x01",
            "no mistake about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C60")

    label("loc_2BD0")


    ChrTalk(
        0x9,
        (
            "That large, red-haired man...\x01",
            "He wasn't respectable, and I\x01",
            "was scared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...But the redheaded\x01",
            "girl that was with him\x01",
            "was pretty cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C60")

    Jump("loc_2DB9")

    label("loc_2C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")

    ChrTalk(
        0x9,
        (
            "Hello, and welcome. Have\x01",
            "a look around... please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Here, we deal in honey, the\x01",
            "village's speciality product...\x01",
            "ladies and gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...*sigh*. I'm really\x01",
            "bad at polite speech.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DB9")

    label("loc_2D36")


    ChrTalk(
        0x9,
        (
            "My grandpa says he wants\x01",
            "me to follow Harold's\x01",
            "example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Comparing me to a veteran\x01",
            "merchant is honestly too\x01",
            "much to bear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB9")

    Jump("loc_1E00")

    label("loc_2DBE")

    TalkEnd(0x9)
    Return()

    # Function_10_1DF3 end

    def Function_11_2DC2(): pass

    label("Function_11_2DC2")

    Call(0, 12)
    Return()

    # Function_11_2DC2 end

    def Function_12_2DC6(): pass

    label("Function_12_2DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0F")
    Call(0, 40)
    Return()

    label("loc_2E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E3D")
    Call(0, 41)
    Return()

    label("loc_2E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E6B")
    Call(0, 43)
    Return()

    label("loc_2E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E82")
    Call(0, 44)
    Return()

    label("loc_2E82")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4250")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EF0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F10")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_424B")

    label("loc_2F10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F30")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_424B")

    label("loc_2F30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F44")
    Jump("loc_424B")

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5C")
    TalkEnd(0xA)
    Return()

    label("loc_2F5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_3004")

    ChrTalk(
        0xA,
        (
            "I'm embarrassed you'd\x01",
            "give us such high\x01",
            "praise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By all means, please write\x01",
            "an article that will drive\x01",
            "business for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_424B")

    label("loc_3004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314C")

    ChrTalk(
        0xA,
        (
            "The appearance of that\x01",
            "bluish-white huge tree\x01",
            "was quite surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's an unthinkable situation, but...\x01",
            "It's especially in times like these that\x01",
            "it's important to take breaks sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Earlier, an exhausted\x01",
            "priest and sister came\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got to bring them\x01",
            "some coffee later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31B3")

    label("loc_314C")


    ChrTalk(
        0xA,
        (
            "Earlier, an exhausted\x01",
            "priest and sister came\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got to bring them\x01",
            "some coffee later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B3")

    Jump("loc_424B")

    label("loc_31B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_33E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3323")

    ChrTalk(
        0xA,
        (
            "The rumor of that\x01",
            "invalidity declaration\x01",
            "has reached this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We didn't have a very good\x01",
            "impression of the President in this\x01",
            "village from the start, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Around now, the people\x01",
            "in the city must sense\x01",
            "the problem too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to\x01",
            "happen next... Personally, I'm\x01",
            "going to keep an eye on things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33DC")

    label("loc_3323")


    ChrTalk(
        0xA,
        (
            "Around now, the people in\x01",
            "the city too must sense the\x01",
            "problems with the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to\x01",
            "happen next... Personally, I'm\x01",
            "going to keep an eye on things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DC")

    Jump("loc_424B")

    label("loc_33E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_35D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3538")

    ChrTalk(
        0xA,
        (
            "Harold and his family\x01",
            "are staying in the large\x01",
            "room on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, if Crossbell is like this, we\x01",
            "probably won't be getting any new\x01",
            "guests, huh. We're both in dire straits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's helping out with various things around\x01",
            "the village, and lending him the room is the\x01",
            "least I can do to thank him for his help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35D4")

    label("loc_3538")


    ChrTalk(
        0xA,
        (
            "Even so, it's Harold's\x01",
            "vacation. How unlucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He is a big help to our village,\x01",
            "but... It's unsettling to think he\x01",
            "can't return to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D4")

    Jump("loc_424B")

    label("loc_35D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_37B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_367B")

    ChrTalk(
        0xA,
        (
            "I thought Geval came here\x01",
            "from the city because he\x01",
            "liked our food, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I wonder where he's\x01",
            "staying?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B0")

    label("loc_367B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(
        0xA,
        (
            "The attack a few days ago\x01",
            "shook the peace throughout\x01",
            "Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tensions at the borders\x01",
            "are growing ever\x01",
            "greater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what's going to\x01",
            "happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37B0")

    label("loc_3744")


    ChrTalk(
        0xA,
        (
            "Tensions at the borders\x01",
            "are growing ever\x01",
            "greater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what's going to\x01",
            "happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B0")

    Jump("loc_424B")

    label("loc_37B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3889")

    ChrTalk(
        0xA,
        (
            "Today, I'm lending out\x01",
            "the large room on 2F for\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now then, I think I'll\x01",
            "make the kids some\x01",
            "pudding for a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, and some for the\x01",
            "sister too, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3901")

    label("loc_3889")


    ChrTalk(
        0xA,
        (
            "Sunday School is being\x01",
            "held today in the large\x01",
            "room on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think I'll make\x01",
            "pudding for everyone as\x01",
            "a snack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3901")

    Jump("loc_424B")

    label("loc_3906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A0")

    ChrTalk(
        0xA,
        (
            "I heard what Derrick's\x01",
            "been doing lately away\x01",
            "from the chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, I wonder if it'll\x01",
            "be all right. A new\x01",
            "business...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0B")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A84")

    ChrTalk(
        0xA,
        (
            "I don't believe it! To\x01",
            "think Minneth was a\x01",
            "crook... I never realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You could call him a\x01",
            "master of deceit. What a\x01",
            "frightening guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's a wanted man now,\x01",
            "so I hope he's captured\x01",
            "before long...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B0B")

    label("loc_3A84")


    ChrTalk(
        0xA,
        (
            "Anyway, thank goodness\x01",
            "Derrick was able to\x01",
            "reconcile with the chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That was a good way to\x01",
            "take advantage of the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0B")

    Jump("loc_424B")

    label("loc_3B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9E")

    ChrTalk(
        0xA,
        (
            "*sigh*, I wonder when\x01",
            "Derrick will feel like\x01",
            "returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope he makes up with\x01",
            "the chief soon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4E")

    label("loc_3B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BAD")
    Jump("loc_3C4E")

    label("loc_3BAD")


    ChrTalk(
        0xA,
        (
            "I haven't had much\x01",
            "contact with Minneth,\x01",
            "personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like he's been meeting\x01",
            "with Derrick often lately... I\x01",
            "wonder what they're talking about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D34")

    ChrTalk(
        0x101,
        (
            "#00003F(Come to think of it, it\x01",
            "seems like we can get gourmet\x01",
            "guide coverage here, but...)\x02\x03",
            "#00001F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D34")

    Jump("loc_424B")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDD")
    SetChrSubChip(0x12, 0x1)
    TurnDirection(0xA, 0x12, 0)

    ChrTalk(
        0xA,
        (
            "Derrick... It's not like the chief\x01",
            "is rejecting you without listening\x01",
            "to what you have to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "No. I'm sure he thinks\x01",
            "it's no good because it\x01",
            "was my idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or else, he wouldn't just\x01",
            "silently watch the current\x01",
            "situation of the village...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I understand things are difficult.\x01",
            "But it's important to have a coffee\x01",
            "and calm down every now and then too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    TurnDirection(0xA, 0x0, 0)
    SetChrSubChip(0x12, 0x0)
    Jump("loc_3F92")

    label("loc_3EDD")


    ChrTalk(
        0xA,
        (
            "Derrick feels responsible for the\x01",
            "village, just like the chief. I'm sure\x01",
            "he's worried about a lot of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since he's here, I'll\x01",
            "treat him to a cup of my\x01",
            "special blend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F92")

    Jump("loc_424B")

    label("loc_3F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B5")

    ChrTalk(
        0xA,
        (
            "The heads of state from\x01",
            "each nation have come to\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This event is\x01",
            "unprecedented in\x01",
            "Crossbell's history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They say Crossbell\x01",
            "City's new mayor was the\x01",
            "one who proposed it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A bold idea. Just what\x01",
            "you'd expect from the\x01",
            "head of IBC.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_415D")

    label("loc_40B5")


    ChrTalk(
        0xA,
        (
            "The West Zemuria Trade\x01",
            "Conference... So it's\x01",
            "finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The surrounding countries'\x01",
            "interest in it is high, and I like\x01",
            "to pay attention to these things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_415D")

    Jump("loc_424B")

    label("loc_4162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_424B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417A")
    Jump("loc_424B")

    label("loc_417A")


    ChrTalk(
        0xA,
        (
            "The large red-haired man and his\x01",
            "friend didn't do anything especially\x01",
            "suspicious in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It looked like he had able-bodied\x01",
            "men and women with him... That's\x01",
            "just the kind of people they were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_424B")

    Jump("loc_2E8F")

    label("loc_4250")

    TalkEnd(0xA)
    Return()

    # Function_12_2DC6 end

    def Function_13_4254(): pass

    label("Function_13_4254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_43A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431B")

    ChrTalk(
        0xB,
        (
            "I didn't pay attention\x01",
            "to Keith, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. He's an honorable\x01",
            "man. I've changed my\x01",
            "opinion of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I laughed earlier, but\x01",
            "I'll have to apologize\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_439B")

    label("loc_431B")


    ChrTalk(
        0xB,
        (
            "Keith is a pretty\x01",
            "honorable man. I've\x01",
            "changed my opinion of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I laughed earlier, but\x01",
            "I'll have to apologize\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439B")

    Jump("loc_500C")

    label("loc_43A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_44E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4459")

    ChrTalk(
        0xB,
        "Sophia is a great cook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's giving me cooking\x01",
            "lessons while she's\x01",
            "staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I'm going to make\x01",
            "a better omelet rice\x01",
            "than my father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44DF")

    label("loc_4459")


    ChrTalk(
        0xB,
        (
            "Sophia is giving me\x01",
            "cooking lessons while\x01",
            "she is staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I'm going to make\x01",
            "a better omelet rice\x01",
            "than my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DF")

    Jump("loc_500C")

    label("loc_44E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_463C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B5")

    ChrTalk(
        0xB,
        (
            "Ah~, Colin is sooo\x01",
            "cute~㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "His eyes are so round,\x01",
            "and he's so friendly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I look up to Harold. As expected\x01",
            "his child. I'm looking forward\x01",
            "to seeing how he turns out!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4637")

    label("loc_45B5")


    ChrTalk(
        0xB,
        (
            "Ah~, Colin is sooo\x01",
            "cute~㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I look up to Harold. As expected\x01",
            "his child. I'm looking forward\x01",
            "to seeing how he turns out!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4637")

    Jump("loc_500C")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4735")

    ChrTalk(
        0xB,
        (
            "I went to Crossbell City for the\x01",
            "Anniversary Festival... It's a\x01",
            "very beautiful and nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "An armed group attacking\x01",
            "a place like that is\x01",
            "unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like the police or\x01",
            "CGF to capture them\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47D3")

    label("loc_4735")


    ChrTalk(
        0xB,
        (
            "An attack on Crossbell\x01",
            "City? That armed group\x01",
            "is unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Setting Minneth from the\x01",
            "other day aside, I wonder why\x01",
            "there's so many bad people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D3")

    Jump("loc_500C")

    label("loc_47D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4880")

    ChrTalk(
        0xB,
        (
            "*sigh*, rainy days are wet\x01",
            "and I hate them. It's a\x01",
            "pain cleaning the floors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just wish the\x01",
            "customers wouldn't track\x01",
            "mud all over the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500C")

    label("loc_4880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A60")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_491C")

    ChrTalk(
        0xB,
        (
            "Minneth and Derrick came\x01",
            "today to talk about\x01",
            "something important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if the finale\x01",
            "of their plan is coming\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5B")

    label("loc_491C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49DC")

    ChrTalk(
        0xB,
        (
            "That Minneth... He was\x01",
            "an unthinkable impostor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph. I thought he was\x01",
            "suspicious from the\x01",
            "beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The next time he shows\x01",
            "up, I'm going to let him\x01",
            "have it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A5B")

    label("loc_49DC")


    ChrTalk(
        0xB,
        (
            "That Minneth... I thought\x01",
            "he was suspicious from\x01",
            "the start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The next time he shows\x01",
            "up, I'm going to let him\x01",
            "have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A5B")

    Jump("loc_500C")

    label("loc_4A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4BCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2C")

    ChrTalk(
        0xB,
        (
            "A nice man has been\x01",
            "coming here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though I heard he is from\x01",
            "a famous foreign firm, he\x01",
            "doesn't brag about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, there are capable\x01",
            "people in this world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4BC9")

    label("loc_4B2C")


    ChrTalk(
        0xB,
        (
            "A nice man has been\x01",
            "coming here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even though he works for a foreign\x01",
            "famous firm, he doesn't brag about\x01",
            "it... He must be a capable person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC9")

    Jump("loc_500C")

    label("loc_4BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE9")
    Call(0, 14)
    Jump("loc_4C78")

    label("loc_4BE9")


    ChrTalk(
        0xB,
        (
            "I want to see Orchis\x01",
            "Tower, but there's the\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you can down ten plates\x01",
            "of our omelet rice in an\x01",
            "hour, I'll date you, though☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C78")

    Jump("loc_500C")

    label("loc_4C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E92")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D76")

    ChrTalk(
        0xB,
        (
            "Those bracers sure are\x01",
            "strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though Arios draws the most\x01",
            "attention, those female bracers\x01",
            "aren't too bad themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, you guys too, of\x01",
            "course. Thanks to you guys,\x01",
            "everyone had a good time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E24")

    label("loc_4D76")


    ChrTalk(
        0xB,
        (
            "Though Arios draws the most\x01",
            "attention, those female bracers\x01",
            "aren't too bad themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, you guys too, of\x01",
            "course. Thanks to you guys,\x01",
            "everyone had a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E24")

    Jump("loc_4E8D")

    label("loc_4E29")


    ChrTalk(
        0xB,
        (
            "The bracers are here to\x01",
            "exterminate monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I've got to give\x01",
            "them proper service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8D")

    Jump("loc_500C")

    label("loc_4E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_500C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F85")

    ChrTalk(
        0xB,
        (
            "Welcome. Please sit at\x01",
            "any seat you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all is said and\x01",
            "done, I simply must\x01",
            "recommend our omelet rice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've recently improved it. It\x01",
            "tastes better than ever, so if\x01",
            "you like, please have some.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_500C")

    label("loc_4F85")


    ChrTalk(
        0xB,
        (
            "Mr. Harold is taking a\x01",
            "room on 2F today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems his business\x01",
            "negotiations are over, so I think\x01",
            "I'll bring him some coffee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500C")

    TalkEnd(0xFE)
    Return()

    # Function_13_4254 end

    def Function_14_5010(): pass

    label("Function_14_5010")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Sealy, want to go to the\x01",
            "city with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Let's go see the rumored\x01",
            "Orchis Tower!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, but I have to help\x01",
            "with the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...How about this?☆ If you can\x01",
            "down ten plates of our omelet rice\x01",
            "in an hour, I'll go with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "N-No, no... That's\x01",
            "obviously impossible.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_5010 end

    def Function_15_5149(): pass

    label("Function_15_5149")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5230")

    ChrTalk(
        0xC,
        (
            "To be perfectly honest, this\x01",
            "situation isn't one that a\x01",
            "guy like me can understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No matter what happens,\x01",
            "I have to protect her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...When we met face-to-\x01",
            "face, she laughed...\x01",
            "Tohoho.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_528B")

    label("loc_5230")


    ChrTalk(
        0xC,
        (
            "I was laughed at by\x01",
            "Sealy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No matter what happens,\x01",
            "I have to protect her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_528B")

    Jump("loc_5E99")

    label("loc_5290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536F")

    ChrTalk(
        0xC,
        (
            "Just between you and me,\x01",
            "Sealy's skill as a\x01",
            "cook... is like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was frankly scared when\x01",
            "she served me omelet rice\x01",
            "that looked like cinders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, I guess I gotta\x01",
            "eat it all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53FF")

    label("loc_536F")


    ChrTalk(
        0xC,
        (
            "Just between you and me,\x01",
            "Sealy's skill as a\x01",
            "cook... is like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, no matter what\x01",
            "she serves, I gotta\x01",
            "force myself to eat it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FF")

    Jump("loc_5E99")

    label("loc_5404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E9")

    ChrTalk(
        0xC,
        (
            "Those State Guard are\x01",
            "creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Whenever they stop by the\x01",
            "village, they give off a "we\x01",
            "are protecting you" vibe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are the CGF really all that\x01",
            "great, now that they've\x01",
            "become the State Guard?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_555F")

    label("loc_54E9")


    ChrTalk(
        0xC,
        (
            "I'm furious at the State\x01",
            "Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are the CGF really all that\x01",
            "great, now that they've\x01",
            "become the State Guard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_555F")

    Jump("loc_5E99")

    label("loc_5564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5654")

    ChrTalk(
        0xC,
        (
            "It's likely the attackers from\x01",
            "the other day are still hiding\x01",
            "somewhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's true that CGF\x01",
            "patrols have increased\x01",
            "recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel like Crossbell's\x01",
            "turning into a dangerous\x01",
            "place...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56EE")

    label("loc_5654")


    ChrTalk(
        0xC,
        (
            "It's likely the attackers from\x01",
            "the other day are still hiding\x01",
            "somewhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel like Crossbell's\x01",
            "turning into a dangerous\x01",
            "place...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56EE")

    Jump("loc_5E99")

    label("loc_56F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D6")

    ChrTalk(
        0xC,
        (
            "Oh, come to think of it,\x01",
            "that referendum is fast\x01",
            "approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a bit of a pain to\x01",
            "go all the way to the\x01",
            "city to vote, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But this affects the\x01",
            "villagers, so we'll have\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5864")

    label("loc_57D6")


    ChrTalk(
        0xC,
        (
            "The referendum on the\x01",
            "question of independence\x01",
            "is fast approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a pain to go to the\x01",
            "city and vote, but...\x01",
            "I'll have to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5864")

    Jump("loc_5E99")

    label("loc_5869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5979")

    ChrTalk(
        0xC,
        (
            "It seems Minneth and\x01",
            "Derrick have finished their\x01",
            "discussions for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want to celebrate the rebirth\x01",
            "of Armorica Village and launch\x01",
            "their effort with a bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. Sealy loves\x01",
            "attention. I'm sure\x01",
            "she'll love it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A28")

    label("loc_5979")


    ChrTalk(
        0xC,
        (
            "It seems Minneth and\x01",
            "Derrick have finished their\x01",
            "discussions for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want to launch their effort\x01",
            "with a band, and celebrate\x01",
            "Armorica's rebirth with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A28")

    Jump("loc_5A99")

    label("loc_5A2D")


    ChrTalk(
        0xC,
        (
            "What Minneth was talking\x01",
            "about... Could it all\x01",
            "have been a lie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That Derrick must be\x01",
            "depressed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A99")

    Jump("loc_5E99")

    label("loc_5A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B54")

    ChrTalk(
        0xC,
        (
            "That foreigner seems to\x01",
            "have a wealth of life\x01",
            "experiences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I know Sealy looks up to\x01",
            "him, so I want to cheer\x01",
            "him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Man, what a good guy...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BBA")

    label("loc_5B54")


    ChrTalk(
        0xC,
        (
            "I know Sealy looks up to\x01",
            "that foreigner, so I\x01",
            "want to cheer him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Man, what a good guy...\x02",
    )

    CloseMessageWindow()

    label("loc_5BBA")

    Jump("loc_5E99")

    label("loc_5BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BDA")
    Call(0, 14)
    Jump("loc_5C3C")

    label("loc_5BDA")


    ChrTalk(
        0xC,
        (
            "Tohoho... And just when\x01",
            "I'd worked up the\x01",
            "courage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sealy can be pretty\x01",
            "harsh sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3C")

    Jump("loc_5E99")

    label("loc_5C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D03")

    ChrTalk(
        0xC,
        (
            "Actually, I want to ask\x01",
            "Sealy on a date before\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've been coming here\x01",
            "almost daily, and we've\x01",
            "become quite close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sure she'll be ok\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D79")

    label("loc_5D03")


    ChrTalk(
        0xC,
        (
            "I plan to ask Sealy on a\x01",
            "date before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Alright. Today, I'll\x01",
            "ready my heart... And do\x01",
            "the deed tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D79")

    Jump("loc_5E99")

    label("loc_5D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1D")

    ChrTalk(
        0xC,
        (
            "I long for Sealy, the\x01",
            "poster girl for this\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can't get enough of her\x01",
            "smile! I end up staying\x01",
            "longer than I should.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E99")

    label("loc_5E1D")


    ChrTalk(
        0xC,
        (
            "I wonder how many times\x01",
            "I've ordered coffee refills\x01",
            "just to get more of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, refills are\x01",
            "normal, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E99")

    TalkEnd(0xFE)
    Return()

    # Function_15_5149 end

    def Function_16_5E9D(): pass

    label("Function_16_5E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB4")
    Call(0, 44)
    Return()

    label("loc_5EB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_607E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD0")

    ChrTalk(
        0xD,
        (
            "A Cryptid is still here, that strange\x01",
            "huge tree appeared and highway\x01",
            "movement is restricted, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Harold returned to the city,\x01",
            "but he agreed to bring me a\x01",
            "book he thinks I'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, that's Harold for\x01",
            "you. I eagerly await his\x01",
            "return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6079")

    label("loc_5FD0")


    ChrTalk(
        0xD,
        (
            "Harold is wise, so I'm\x01",
            "sure he'll bring me a\x01",
            "book I'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Even though the situation is\x01",
            "like this. I want him to be as\x01",
            "careful as possible on the highway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6079")

    Jump("loc_71E2")

    label("loc_607E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_622A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6179")

    ChrTalk(
        0xD,
        (
            "I'm sunk. Because of the\x01",
            "highway movement restrictions,\x01",
            "I can't go to the library...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Chairman MacDowell's\x01",
            "finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At this rate, things will improve.\x01",
            "The barrier around Crossbell City\x01",
            "disappeared, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6225")

    label("loc_6179")


    ChrTalk(
        0xD,
        (
            "At this rate, the\x01",
            "barrier surrounding the\x01",
            "city will disappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I just want everything to go back\x01",
            "to the way it used to be, when I\x01",
            "could go to the library freely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6225")

    Jump("loc_71E2")

    label("loc_622A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_63E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634C")

    ChrTalk(
        0xD,
        (
            "With the Cryptid and the highway movement\x01",
            "restrictions, we can't do farm work, so I'll\x01",
            "try reading a book for a change of pace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But obviously I can't go\x01",
            "to the Crossbell City\x01",
            "Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Would saying that\x01",
            "readers live rich lives\x01",
            "be saying too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63DF")

    label("loc_634C")


    ChrTalk(
        0xD,
        (
            "I can't go to Crossbell\x01",
            "City Library... so I\x01",
            "can't read any new books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If a life like this\x01",
            "lasts many years, it can\x01",
            "only be called hell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63DF")

    Jump("loc_71E2")

    label("loc_63E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F8")

    ChrTalk(
        0xD,
        (
            "I've read the Crossbell\x01",
            "Times Extra a while back\x01",
            "several times already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm concerned about the attack, but\x01",
            "the article about Ilya's injury was\x01",
            "the most shocking of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...As a citizen of\x01",
            "Crossbell, I pray she\x01",
            "makes a full recovery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_657D")

    label("loc_64F8")


    ChrTalk(
        0xD,
        (
            "For something like this to\x01",
            "happen to Ilya, who is always\x01",
            "giving energy to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I pray she makes a\x01",
            "full recover.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_657D")

    Jump("loc_71E2")

    label("loc_6582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6668")

    ChrTalk(
        0xD,
        (
            "The pleasant sound of rain\x01",
            "tapping on the windows,\x01",
            "warm coffee by my side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, rainy days make\x01",
            "for great reading\x01",
            "weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is a good chance to\x01",
            "read all those books\x01",
            "I've piled up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66F1")

    label("loc_6668")


    ChrTalk(
        0xD,
        (
            "The pleasant sound of rain\x01",
            "tapping on the windows,\x01",
            "warm coffee by my side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, rainy days make\x01",
            "for great reading\x01",
            "weather.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F1")

    Jump("loc_71E2")

    label("loc_66F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A05")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67DB")

    ChrTalk(
        0xD,
        (
            "I feel the problems of\x01",
            "the village grow with\x01",
            "each passing season.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wonder if the chief\x01",
            "should discard the old\x01",
            "traditions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I at least understand\x01",
            "that Derrick wants\x01",
            "reform.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6858")

    label("loc_67DB")


    ChrTalk(
        0xD,
        (
            "I feel the problems of\x01",
            "the village grow with\x01",
            "each passing season.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I at least understand\x01",
            "that Derrick wants\x01",
            "reform.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6858")

    Jump("loc_6A00")

    label("loc_685D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694C")

    ChrTalk(
        0xD,
        (
            "It seems that Minneth\x01",
            "did a nice job winning\x01",
            "over the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't know what he wants...\x01",
            "But your insight to see\x01",
            "through it is the real thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If he would use his\x01",
            "talents for fraud, he's\x01",
            "beyond help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A00")

    label("loc_694C")


    ChrTalk(
        0xD,
        (
            "That Minneth... If he's\x01",
            "involved in fraud, he\x01",
            "might have succeeded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Well, based on what I've heard,\x01",
            "he has quite the criminal record,\x01",
            "so there's no room for sympathy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A00")

    Jump("loc_71E2")

    label("loc_6A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B77")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "I borrowed "Ten Mysteries\x01",
            "of Crossbell that Really\x01",
            "Exist" from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The story of the "Man Who\x01",
            "Searches for His Own\x01",
            "Head"... Ooh, how chilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, that one's really\x01",
            "scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's lost its own head,\x01",
            "but cries out, "Find it\x01",
            "for me."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...And that's not even\x01",
            "the scariest part.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_6BF8")

    label("loc_6B77")


    ChrTalk(
        0xD,
        (
            "*sigh*, and just when\x01",
            "when I was so scared, you\x01",
            "ruined it for me, Gｷfan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You've got to tell ghost\x01",
            "story fans properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF8")

    Jump("loc_71E2")

    label("loc_6BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D4A")

    ChrTalk(
        0xD,
        (
            "While I was at the library, I\x01",
            "bought the latest serial novel\x01",
            "I've been enjoying lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But it seems I skipped a\x01",
            "volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'd like to avoid inadvertently\x01",
            "spoiling myself... Sorry, but\x01",
            "could you please take it?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F2, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 4)
    TalkEnd(0xFE)
    SetChrFlags(0xD, 0x10)
    Return()

    label("loc_6D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F08")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "Today, I borrowed "Beauties\x01",
            "that Moved the Continent.\x01",
            "...It was quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a book that introduces you to the\x01",
            "historic achievements of women in each\x01",
            "nation, starting with "Walkｸre Lianne".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. Maybe originally,\x01",
            "women were the powerful\x01",
            "ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My daughter is always\x01",
            "giving me a hard time,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(I think that's just\x01",
            "because you're\x01",
            "unreliable, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_6F7F")

    label("loc_6F08")


    ChrTalk(
        0xD,
        (
            ""Beauties that Moved the\x01",
            "Continent"... It's\x01",
            "pretty interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why don't you guys try\x01",
            "going to the library?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F7F")

    Jump("loc_71E2")

    label("loc_6F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_711D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7087")

    ChrTalk(
        0xD,
        (
            "I love reading. I planned\x01",
            "to go to the library this\x01",
            "morning, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I completely forgot about\x01",
            "the traffic restrictions due\x01",
            "to the President's arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thanks to that, I spent\x01",
            "the morning doing\x01",
            "nothing. How miserable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7118")

    label("loc_7087")


    ChrTalk(
        0xD,
        (
            "The traffic restrictions\x01",
            "have been lifted... I think\x01",
            "I'll go to the city later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'll go to the library\x01",
            "and look for some book\x01",
            "to read.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7118")

    Jump("loc_71E2")

    label("loc_711D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_71E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7135")
    Jump("loc_71E2")

    label("loc_7135")


    ChrTalk(
        0xD,
        (
            "It looked like they bought\x01",
            "preserved food from\x01",
            "Reoir's general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. I wonder if they're going\x01",
            "mountain climbing. I've never\x01",
            "seen a group like them, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71E2")

    TalkEnd(0xFE)
    Return()

    # Function_16_5E9D end

    def Function_17_71E6(): pass

    label("Function_17_71E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7299")

    ChrTalk(
        0xE,
        (
            "Harold's family returned\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm a little sad. I was just getting\x01",
            "to know them. But in a situation\x01",
            "like this, it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_734C")

    label("loc_7299")


    ChrTalk(
        0xE,
        (
            "Harold's family was worried about\x01",
            "their neighborhood, so it's good\x01",
            "that they returned to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When Stefan and I return\x01",
            "to the city, I'll be\x01",
            "sure to say hi to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_734C")

    Jump("loc_7CCC")

    label("loc_7351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_735F")
    Jump("loc_7CCC")

    label("loc_735F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_74F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_745B")

    ChrTalk(
        0xE,
        (
            "Because the situation is like\x01",
            "this, I'm worried about my old\x01",
            "neighbors in Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Harold's family is worried\x01",
            "about the city too, but they're\x01",
            "doing all they can to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've got to do what I\x01",
            "can too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_74ED")

    label("loc_745B")


    ChrTalk(
        0xE,
        (
            "Harold's family is worried\x01",
            "about the city too, but they're\x01",
            "doing all they can to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't just be scared.\x01",
            "I have to do what I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74ED")

    Jump("loc_7CCC")

    label("loc_74F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75CC")

    ChrTalk(
        0xE,
        (
            "*sigh*... An attack on\x01",
            "the city was completely\x01",
            "unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Thankfully my friends are\x01",
            "safe, but... It seems\x01",
            "there are many victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope nothing like this\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_763E")

    label("loc_75CC")


    ChrTalk(
        0xE,
        (
            "*sigh*... An attack on\x01",
            "the city was completely\x01",
            "unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope nothing like this\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763E")

    Jump("loc_7CCC")

    label("loc_7643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7733")

    ChrTalk(
        0xE,
        (
            "Until I moved here, I\x01",
            "didn't know about traveling\x01",
            "Sunday School teachers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It must be difficult,\x01",
            "commuting here from the\x01",
            "cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to be thankful to\x01",
            "the sister for coming\x01",
            "all the way here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_77B7")

    label("loc_7733")


    ChrTalk(
        0xE,
        (
            "It must be difficult,\x01",
            "traveling here from the\x01",
            "cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to be thankful to\x01",
            "the sister for coming\x01",
            "all the way here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B7")

    Jump("loc_7CCC")

    label("loc_77BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7903")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7877")

    ChrTalk(
        0xE,
        (
            "The chief's son... He's\x01",
            "been tense ever since he\x01",
            "got back yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Today's negotiations involved\x01",
            "the future of the village...\x01",
            "That much is certain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FE")

    label("loc_7877")


    ChrTalk(
        0xE,
        (
            "Thank goodness Stefan and\x01",
            "the village children weren't\x01",
            "attacked by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Goodness. That crook...\x01",
            "I'll never forgive him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78FE")

    Jump("loc_7CCC")

    label("loc_7903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79BC")

    ChrTalk(
        0xE,
        (
            "Hmhmhmm~... That does it\x01",
            "for the sheets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I admired hotel maids\x01",
            "before I gave birth to\x01",
            "Stefan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, helping out at\x01",
            "this bar-inn is pretty\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A3E")

    label("loc_79BC")


    ChrTalk(
        0xE,
        (
            "Haha, helping out at\x01",
            "this bar-inn is pretty\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stefan has become close\x01",
            "with his friends, and\x01",
            "every day is fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A3E")

    Jump("loc_7CCC")

    label("loc_7A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7AC8")

    ChrTalk(
        0xE,
        (
            "Today I'm helping clean\x01",
            "the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They've supported me and\x01",
            "Stefan, so I want to help\x01",
            "them in any way I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CCC")

    label("loc_7AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE3")
    Call(0, 23)
    Jump("loc_7B61")

    label("loc_7AE3")


    ChrTalk(
        0xE,
        (
            "Well, isn't that fine?\x01",
            "I'll accept it\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. They treated\x01",
            "Stefan earlier, and I\x01",
            "wanted to have some too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B61")

    Jump("loc_7CCC")

    label("loc_7B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C42")

    ChrTalk(
        0xE,
        (
            "My son Stefan and I moved here\x01",
            "from Crossbell City a while\x01",
            "back. Haha, thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That child hated it at first,\x01",
            "but it seems he's gotten used to\x01",
            "life here. Haha, thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7CCC")

    label("loc_7C42")


    ChrTalk(
        0xE,
        (
            "By the way, Gｷfan is\x01",
            "renting us this room\x01",
            "cheap as a courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. The people of this\x01",
            "village are warm and\x01",
            "kind, aren't they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CCC")

    TalkEnd(0xFE)
    Return()

    # Function_17_71E6 end

    def Function_18_7CD0(): pass

    label("Function_18_7CD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7D56")

    ChrTalk(
        0xF,
        (
            "The inn's old man made us\x01",
            "snacks for recess during\x01",
            "today's Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Aww. I want it to be\x01",
            "recess already~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D56")

    TalkEnd(0xFE)
    Return()

    # Function_18_7CD0 end

    def Function_19_7D5A(): pass

    label("Function_19_7D5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7DC4")

    ChrTalk(
        0x10,
        (
            "Pooley is studying with\x01",
            "everyone today~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't understand a\x01",
            "single thing, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DC4")

    TalkEnd(0xFE)
    Return()

    # Function_19_7D5A end

    def Function_20_7DC8(): pass

    label("Function_20_7DC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EAE")

    ChrTalk(
        0x11,
        (
            "I went to check on\x01",
            "things in the city with\x01",
            "my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "On all the friends and\x01",
            "neighbors I lived with\x01",
            "before. Everyone was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "My mom was worried the\x01",
            "whole time... Really,\x01",
            "thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7F50")

    label("loc_7EAE")


    ChrTalk(
        0x11,
        (
            "Until yesterday, I was\x01",
            "with my mom checking on\x01",
            "things in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "All the friends and neighbors\x01",
            "I lived with before were\x01",
            "safe. Really, thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F50")

    Jump("loc_8074")

    label("loc_7F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800A")

    ChrTalk(
        0x11,
        (
            "I used to go to the\x01",
            "cathedral when I lived\x01",
            "in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But now that I live in\x01",
            "the village, the sister\x01",
            "comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...That's a little\x01",
            "easier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8074")

    label("loc_800A")


    ChrTalk(
        0x11,
        (
            "When I lived in the city,\x01",
            "I went to the cathedral\x01",
            "for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Now is a little\x01",
            "easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8074")

    TalkEnd(0xFE)
    Return()

    # Function_20_7DC8 end

    def Function_21_8078(): pass

    label("Function_21_8078")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_80D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80CD")

    ChrTalk(
        0x12,
        (
            "...I have an important\x01",
            "visitor today. Get out\x01",
            "of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80CD")

    Jump("loc_85FC")

    label("loc_80D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8403")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_83FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_836E")

    ChrTalk(
        0x12,
        "...Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FDerrick... Umm, if possible,\x01",
            "I'd like you to talk once\x01",
            "more with your father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...Hmph. I've already\x01",
            "spoken with him many\x01",
            "times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But my father is a staunch\x01",
            "conservative. He doesn't approve of\x01",
            "my reforms, no even a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I was just about to give\x01",
            "up on reform, when Minneth\x01",
            "came and gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My father can't be trusted...\x01",
            "The two of us will reform\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...There's suspicious points\x01",
            "about Minneth. I'd like him to\x01",
            "rethink this if possible, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(We've insufficient evidence\x01",
            "at present. He'll be\x01",
            "difficult to persuade...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_83FE")

    label("loc_836E")


    ChrTalk(
        0x12,
        (
            "I had given up on\x01",
            "village reform. Minneth\x01",
            "gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My father can't be trusted...\x01",
            "The two of us will reform\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83FE")

    Jump("loc_85FC")

    label("loc_8403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_85FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857B")

    ChrTalk(
        0x12,
        (
            "My father, the chief... No matter what\x01",
            "kind of reform proposals I give him,\x01",
            "he stubbornly refuses to approve them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "He always repeats the same things.\x01",
            ""How the village should be" and "Don't\x01",
            "lose sight of reality", he says...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But if we cling to those things\x01",
            "without form, the village will\x01",
            "quietly go under...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...*sigh*, I'm tired.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_85FC")

    label("loc_857B")


    ChrTalk(
        0x12,
        (
            "If the chief won't accept them,\x01",
            "reforms can't proceed. It's just a\x01",
            "matter of time before we're ruined...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...I'm tired.\x02",
    )

    CloseMessageWindow()

    label("loc_85FC")

    TalkEnd(0xFE)
    Return()

    # Function_21_8078 end

    def Function_22_8600(): pass

    label("Function_22_8600")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_86A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_861E")
    Call(0, 23)
    Jump("loc_86A2")

    label("loc_861E")


    ChrTalk(
        0x13,
        (
            "That's right, our share\x01",
            "of the profits came in\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Look, it's my special\x01",
            "homemade carbonara sauce.\x01",
            "It goes with pasta.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A2")

    TalkEnd(0xFE)
    Return()

    # Function_22_8600 end

    def Function_23_86A6(): pass

    label("Function_23_86A6")

    OP_4B(0xE, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Then, you've been\x01",
            "staying in this room for\x01",
            "a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes. He offered, and I\x01",
            "thought I'd take him up\x01",
            "on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In return, I'm thinking\x01",
            "of helping out with the\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That's a good idea. It'll\x01",
            "be easier to manage this\x01",
            "place with an extra person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0xE, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_23_86A6 end

    def Function_24_87BE(): pass

    label("Function_24_87BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_88EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885D")

    ChrTalk(
        0x14,
        (
            "On my way here today, I\x01",
            "noticed giant cat\x01",
            "footprints here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I wonder what happened\x01",
            "in this village\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_88EB")

    label("loc_885D")


    ChrTalk(
        0x14,
        (
            "On my way to the village,\x01",
            "there seemed to be giant cat\x01",
            "footprints here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I wonder what happened\x01",
            "in this village\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88EB")

    TalkEnd(0xFE)
    Return()

    # Function_24_87BE end

    def Function_25_88EF(): pass

    label("Function_25_88EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8900")
    Jump("loc_95CD")

    label("loc_8900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5C")

    ChrTalk(
        0x15,
        (
            "#03600FOh, everyone! Thank goodness\x01",
            "you're safe.\x02\x03",
            "#03603FI heard the rumors of Chairman\x01",
            "MacDowell's independence\x01",
            "invalidity declaration.\x02\x03",
            "#03605FCould you all have...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, we've been busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHave there been any\x01",
            "changes at Amorica\x01",
            "Village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FNo, none as of yet...\x02\x03",
            "#03600FIt's just, the State Guard\x01",
            "seemed confused during my\x01",
            "negotiations with them just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThe village's influence\x01",
            "must seem small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if pushed, I'd say\x01",
            "their influence on the\x01",
            "city is greater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FYes. I'm worried about my\x01",
            "neighbors, as well as my friends\x01",
            "at Mainz and St. Ursula Hospital.\x02\x03",
            "#03608FI'd go visit them if I could move\x01",
            "freely, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Anyway, I can't say\x01",
            "the situation any better\x01",
            "yet.\x02\x03",
            "#00000FPlease be careful,\x01",
            "Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FAlright. You guys be\x01",
            "careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 5)
    Jump("loc_8D06")

    label("loc_8C5C")


    ChrTalk(
        0x15,
        (
            "#03603FI'm worried about my neighbors in\x01",
            "the city, and my friends in Mainz\x01",
            "and St. Ursula Hospital as well.\x02\x03",
            "#03608FI'd go visit them if I could move\x01",
            "freely, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D06")

    Jump("loc_95CD")

    label("loc_8D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_8DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D26")
    Call(0, 26)
    Jump("loc_8DCF")

    label("loc_8D26")


    ChrTalk(
        0x15,
        (
            "#03600FAt the moment, I'm assembling\x01",
            "goods for the next negotiations\x01",
            "with the state guard.\x02\x03",
            "#03603FEveryone, please. Do be\x01",
            "careful. ...May the Goddess\x01",
            "protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DCF")

    Jump("loc_95CD")

    label("loc_8DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_916E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EAD")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆[Fraud Case] Day 2?\x01",
            "(debug)\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not Cleared]\x01",      # 2
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
        (0, "loc_8E94"),
        (1, "loc_8E99"),
        (2, "loc_8EA3"),
        (SWITCH_DEFAULT, "loc_8EAD"),
    )


    label("loc_8E94")

    Jump("loc_8EAD")

    label("loc_8E99")

    OP_29(0x87, 0x4, 0x10)
    Jump("loc_8EAD")

    label("loc_8EA3")

    OP_29(0x87, 0x3, 0x10)
    Jump("loc_8EAD")

    label("loc_8EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8FC2")

    ChrTalk(
        0x15,
        (
            "#03600FWe received an invitation from\x01",
            "the chief to come.\x02\x03",
            "#03603FAlthough it seems Pete\x01",
            "declined his invitation for\x01",
            "helping with the fraud case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThe Minneth case... So\x01",
            "that's what happened.\x02\x03",
            "#00003FThank goodness Pete\x01",
            "didn't get involved...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90AA")

    label("loc_8FC2")


    ChrTalk(
        0x15,
        (
            "#03600FWe received an invitation\x01",
            "from the chief to come.\x02\x03",
            "#03603FIt seems Pete declined the\x01",
            "invitation for helping in\x01",
            "the case, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSo that's how it is,\x01",
            "huh.\x02\x03",
            "#00003FThank goodness Pete\x01",
            "didn't get involved...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90AA")


    ChrTalk(
        0x15,
        "#03600FYes, I agree.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9169")

    label("loc_90CC")


    ChrTalk(
        0x15,
        (
            "#03600FThe resistance force was sighted at\x01",
            "the Ancient Battlefield. The entrance\x01",
            "is in the middle of the Old Path.\x02\x03",
            "#03603FEveryone, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9169")

    Jump("loc_95CD")

    label("loc_916E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_95CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9421")

    ChrTalk(
        0x101,
        (
            "#00000FAh, Harold. So you're\x01",
            "here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03605FOh, it's the Special\x01",
            "Support Section. Fancy\x01",
            "meeting you here.\x02\x03",
            "#03600FYes, I'm here for\x01",
            "business negotiations\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. You're the same\x01",
            "honest merchant as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609FHaha. Thankfully I got\x01",
            "some good deals today.\x02\x03",
            "#03600FThat's right everyone...\x01",
            "If you like, would you\x01",
            "take these?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "x10 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13C, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x104,
        "#00305FOh, is it all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FYes. Actually, it's a\x01",
            "little something extra I\x01",
            "got in one of my deals.\x02\x03",
            "#03609FWe can't eat them, so I\x01",
            "hope they'll be useful\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUmm, then... We\x01",
            "gratefully accept.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 6)
    Jump("loc_95CD")

    label("loc_9421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_952F")

    ChrTalk(
        0x15,
        (
            "#03604FThankfully, I got some good deals today.\x02\x03",
            "#03608FIt's just, lately, the chief and Derrick's\x01",
            "arguments show no sign of stopping. It's a\x01",
            "very worrying state of affairs.\x02\x03",
            "#03603FThe relationship between a father and son\x01",
            "must be difficult one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_95CD")

    label("loc_952F")


    ChrTalk(
        0x15,
        (
            "#03603FThe chief and Derrick...\x01",
            "They both want to protect\x01",
            "their village, but...\x02\x03",
            "#03608FThe relationship between\x01",
            "a father and son must be\x01",
            "difficult one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95CD")

    TalkEnd(0xFE)
    Return()

    # Function_25_88EF end

    def Function_26_95D1(): pass

    label("Function_26_95D1")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#03608FReoir's back medicine...\x01",
            "and Ange's supply of\x01",
            "bandages are running short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700FThe innkeeper is running\x01",
            "low of seasoning too.\x02\x03",
            "#03708FSome of them are spices\x01",
            "you can only get at the\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FHmm... We'll make do without\x01",
            "the bandages, but we'll need\x01",
            "the other things.\x02\x03",
            "#03600FThanks, Sophia. Please rest,\x01",
            "and leave the rest to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_26_95D1 end

    def Function_27_9761(): pass

    label("Function_27_9761")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9790")
    Call(0, 38)
    Return()

    label("loc_9790")

    Call(0, 39)
    Return()

    label("loc_9794")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_27_9761 end

    def Function_28_979B(): pass

    label("Function_28_979B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97CA")
    Call(0, 38)
    Return()

    label("loc_97CA")

    Call(0, 39)
    Return()

    label("loc_97CE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_28_979B end

    def Function_29_97D5(): pass

    label("Function_29_97D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_97E6")
    Jump("loc_9A3C")

    label("loc_97E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_97F4")
    Jump("loc_9A3C")

    label("loc_97F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980F")
    Call(0, 26)
    Jump("loc_988F")

    label("loc_980F")


    ChrTalk(
        0x16,
        (
            "#03700FAs my husband's partner,\x01",
            "I help him, even though\x01",
            "I'm not good at it.\x02\x03",
            "I hope I can be of some\x01",
            "use to the villagers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_988F")

    Jump("loc_9A3C")

    label("loc_9894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9A3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99AF")

    ChrTalk(
        0x16,
        (
            "#03708FThe other members of the\x01",
            "Support Section... I'm\x01",
            "worried about them.\x02\x03",
            "#03700FI pray that you're able\x01",
            "to reunite with them\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHaha, thank you madam.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIf it's like this, we'll\x01",
            "do whatever it takes to\x01",
            "meet up with them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_9A3C")

    label("loc_99AF")


    ChrTalk(
        0x16,
        (
            "#03708FThe other members of the\x01",
            "Support Section... I'm\x01",
            "worried about them.\x02\x03",
            "#03700FI pray that you're able\x01",
            "to reunite with them\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A3C")

    TalkEnd(0xFE)
    Return()

    # Function_29_97D5 end

    def Function_30_9A40(): pass

    label("Function_30_9A40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9A51")
    Jump("loc_9DFE")

    label("loc_9A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9A5F")
    Jump("loc_9DFE")

    label("loc_9A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9AD4")

    ChrTalk(
        0x17,
        (
            "#03805FHmm, it looks like dad's\x01",
            "working...\x02\x03",
            "#03800FShould I go play with\x01",
            "Camille and the others~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DFE")

    label("loc_9AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CCC")
    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B78")
    Jump("loc_9BC2")

    label("loc_9B78")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B98")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BC2")

    label("loc_9B98")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BB8")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BC2")

    label("loc_9BB8")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BC2")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEhehe, doggy. Let's play\x01",
            "again~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3CYes, I will allow it.\x02\x03",
            "#01203F...But he is not a member of\x01",
            "the Support Section, so I\x01",
            "shall not grow too attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHaha. I love that about\x01",
            "you, Zeit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_9DF9")

    label("loc_9CCC")

    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D5D")
    Jump("loc_9DA7")

    label("loc_9D5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D7D")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DA7")

    label("loc_9D7D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D9D")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DA7")

    label("loc_9D9D")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DA7")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEhehe, doggy. Let's play\x01",
            "again~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF9")

    ClearChrFlags(0x17, 0x10)

    label("loc_9DFE")

    TalkEnd(0xFE)
    Return()

    # Function_30_9A40 end

    def Function_31_9E02(): pass

    label("Function_31_9E02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E18")
    SetScenarioFlags(0x2, 2)

    label("loc_9E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A244")

    ChrTalk(
        0x18,
        (
            "#04303F#30WMy Merkabah won't be too\x01",
            "useful for a while...\x02\x03",
            "#04300FWhen it's fixed, we'll\x01",
            "back you up as best we\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_9FB0")
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x105, 0)
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F3C")
    Jump("loc_9F86")

    label("loc_9F3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F5C")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F86")

    label("loc_9F5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F7C")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F86")

    label("loc_9F7C")

    OP_52(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F86")

    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x10)

    label("loc_9FB0")


    ChrTalk(
        0x18,
        (
            "#04308F#30W─Wazy. Don't do anything\x01",
            "too crazy. You hear?\x02\x03",
            "#04301FIf you squander your\x01",
            "powers like me, it'll turn\x01",
            "deadly when it counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403FYeah... I'll keep that\x01",
            "in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A23F")
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#04300F#30WOh yeah... I almost\x01",
            "forgot. Lloyd, take\x01",
            "this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 2)

    ChrTalk(
        0x104,
        "#00305FThis guy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FSome kind of\x01",
            "fragment...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#04303F#30WIt was where the Aion\x01",
            "crashed... It's probably\x01",
            "one of its parts.\x02\x03",
            "#04300FYou might find a way to\x01",
            "put it to good use, so I\x01",
            "want you to have it.\x02\x03",
            "#04311FWell, all of you, I\x01",
            "mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen... We gratefully\x01",
            "accept.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A23F")

    Jump("loc_A2E2")

    label("loc_A244")


    ChrTalk(
        0x18,
        (
            "#04303F#30WMy Merkabah won't be too\x01",
            "useful for a while...\x02\x03",
            "#04300FWhen it's fixed, we'll\x01",
            "back you up as best we\x01",
            "can.\x02\x03",
            "#04302FAnyway, do your best,\x01",
            "guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2E2")

    TalkEnd(0xFE)
    Return()

    # Function_31_9E02 end

    def Function_32_A2E6(): pass

    label("Function_32_A2E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42B")

    ChrTalk(
        0x19,
        (
            "#13808FWhen KeA came to Sunday School,\x01",
            "she talked about the fun times\x01",
            "she had with you all.\x02\x03",
            "#13804F...As a knight of the\x01",
            "Gralsritter, I won't say\x01",
            "anything inappropriate, but...\x02\x03",
            "#13802FI think getting her smile back\x01",
            "is the most important thing of\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FRies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F...Acknowledged.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4C3")

    label("loc_A42B")


    ChrTalk(
        0x19,
        (
            "#13808FWhen KeA came to Sunday School,\x01",
            "she talked about the fun times\x01",
            "she had with you all.\x02\x03",
            "#13804F...Please, take back that smile\x01",
            "for all of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4C3")

    TalkEnd(0xFE)
    Return()

    # Function_32_A2E6 end

    def Function_33_A4C7(): pass

    label("Function_33_A4C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F6")

    ChrTalk(
        0xFE,
        (
            "Heading into the main session, we're\x01",
            "patrolling while taking care of requests.\x01",
            "Things seem peaceful here, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm concerned about the rocky\x01",
            "relationship between Derrick\x01",
            "and the chief, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't interfere, though.\x01",
            "Bracers must remain\x01",
            "neutral at all times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_A699")

    label("loc_A5F6")


    ChrTalk(
        0xFE,
        (
            "I'm concerned about the rocky\x01",
            "relationship between Derrick\x01",
            "and the chief, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't interfere, though.\x01",
            "Bracers must remain\x01",
            "neutral at all times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A699")

    TalkEnd(0xFE)
    Return()

    # Function_33_A4C7 end

    def Function_34_A69D(): pass

    label("Function_34_A69D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A71D")

    ChrTalk(
        0xFE,
        (
            "I saw a well-dressed man\x01",
            "crossing the bridge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. I\x01",
            "have no interest in\x01",
            "humans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_A75D")

    label("loc_A71D")


    ChrTalk(
        0xFE,
        "*crunch, munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love this place's\x01",
            "omelet rice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A75D")

    TalkEnd(0xFE)
    Return()

    # Function_34_A69D end

    def Function_35_A761(): pass

    label("Function_35_A761")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(78100, 1500, -3470, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x19, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 36)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x102, 1, 0, 36)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x103, 1, 0, 36)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x104, 1, 0, 36)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A800")
    BeginChrThread(0x109, 1, 0, 36)
    WaitChrThread(0x109, 1)

    label("loc_A800")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A81A")
    BeginChrThread(0x105, 1, 0, 36)
    WaitChrThread(0x105, 1)

    label("loc_A81A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A834")
    BeginChrThread(0x106, 1, 0, 36)
    WaitChrThread(0x106, 1)

    label("loc_A834")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A84E")
    BeginChrThread(0x10A, 1, 0, 36)
    WaitChrThread(0x10A, 1)

    label("loc_A84E")

    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0xFA0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(70310, 1500, -240, 3000)
    MoveCamera(313, 27, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_A932():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A932)
    Sleep(50)

    def lambda_A942():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A942)
    Sleep(50)

    def lambda_A952():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A952)
    Sleep(50)

    def lambda_A962():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A962)
    Sleep(50)

    def lambda_A972():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_A972)
    Sleep(50)

    def lambda_A982():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_A982)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FRies!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9E8")

    ChrTalk(
        0x105,
        (
            "#10402FSo this is where you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E8")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetChrSubChip(0x18, 0x1)
    OP_93(0x19, 0x5A, 0x1F4)

    ChrTalk(
        0x19,
        "#13805FEveryone...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA5E")

    ChrTalk(
        0x18,
        (
            "#11P#04300F#30WOh... If it isn't Wazy\x01",
            "and Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA87")

    label("loc_AA5E")


    ChrTalk(
        0x18,
        "#11P#04300F#30WOh... You guys, huh.\x02",
    )

    CloseMessageWindow()

    label("loc_AA87")

    SetChrPos(0x0, 85600, 0, -1570, 0)
    SetChrPos(0x1, 85600, 0, -1570, 0)
    SetChrPos(0x2, 85600, 0, -1570, 0)
    SetChrPos(0x3, 85600, 0, -1570, 0)
    SetChrPos(0x4, 85600, 0, -1570, 0)
    SetChrPos(0x5, 85600, 0, -1570, 0)
    OP_68(70310, 1200, -240, 3000)
    MoveCamera(310, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(24880, 3000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 37)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x102, 1, 0, 37)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x103, 1, 0, 37)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x104, 1, 0, 37)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB67")
    BeginChrThread(0x109, 1, 0, 37)
    WaitChrThread(0x109, 1)

    label("loc_AB67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB81")
    BeginChrThread(0x105, 1, 0, 37)
    WaitChrThread(0x105, 1)

    label("loc_AB81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB9B")
    BeginChrThread(0x106, 1, 0, 37)
    WaitChrThread(0x106, 1)

    label("loc_AB9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABB5")
    BeginChrThread(0x10A, 1, 0, 37)
    WaitChrThread(0x10A, 1)

    label("loc_ABB5")

    WaitChrThread(0x104, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe have something to ask\x01",
            "the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FYou shot down that\x01",
            "unthinkable flying doll,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FThat was really good\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04302F#30WHaha... I took a lot of\x01",
            "damage on my end too,\x01",
            "though.\x02\x03",
            "#04306FYou guys are pathetic,\x01",
            "making me use up all my\x01",
            "power like that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3D")

    ChrTalk(
        0x103,
        (
            "#6P#00205FAre you like that because you\x01",
            "used the dangerous "power"\x01",
            "Abbas warned you about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FYeah. When you use the Stigma's power\x01",
            "together with the Merkabah, you can\x01",
            "release it all at once, right?\x02\x03",
            "#10402FHow reckless. You might have gone to\x01",
            "see the Goddess if you were careless.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE9D")

    label("loc_AE3D")


    ChrTalk(
        0x103,
        (
            "#6P#00205FAre you like that because you\x01",
            "used the dangerous "power"\x01",
            "Abbas warned you about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE9D")


    ChrTalk(
        0x101,
        "#6P#00005FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13800FYes. The very nature of the\x01",
            "Stigma is that its power is\x01",
            "too much for the body...\x02\x03",
            "#13808FAnd it is reckless to\x01",
            "release that power without\x01",
            "limit.\x02\x03",
            "#13803FI can't help but say it's\x01",
            "reckless for one in the\x01",
            "position of Dominion.\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#11P#04306F#30W...*sigh*, Ries. Give me\x01",
            "a break already.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0DD")

    ChrTalk(
        0x105,
        (
            "#12P#10409FHaha. Looks like you're\x01",
            "being henpecked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B177")

    label("loc_B0DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B131")

    ChrTalk(
        0x109,
        (
            "#12P#10109F(I-It sure looks like\x01",
            "he's being dominated...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B177")

    label("loc_B131")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B177")

    ChrTalk(
        0x106,
        (
            "#12P#10702F(Fufu. Looks like he's\x01",
            "outmatched...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B177")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1F2")

    ChrTalk(
        0x10A,
        (
            "#12P#00603F(Gralsritter Dominions...\x01",
            "They're quite different from\x01",
            "what I've heard, aren't they.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2BB")

    label("loc_B1F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B265")

    ChrTalk(
        0x106,
        (
            "#12P#10704F(Gralsritter Dominions...\x01",
            "They're quite different\x01",
            "from what what I've heard.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2BB")

    label("loc_B265")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2BB")

    ChrTalk(
        0x109,
        (
            "#12P#10106F*sigh*. I think you\x01",
            "should listen to what\x01",
            "Abbas says.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2BB")


    ChrTalk(
        0x18,
        (
            "#11P#04303F#30WThere is that...\x02\x03",
            "#04308FBut, well, that\x01",
            "unthinkable thing\x01",
            "appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13801FThe Azure Tree... A\x01",
            "miracle brought forth\x01",
            "from human tenacity.\x02\x03",
            "#13803FOnly by the hand of a\x01",
            "goddess could something\x01",
            "like that appear...\x02\x03",
            "#13808FAnd what's more, KeA's\x01",
            "power is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F...Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FTo be honest, none of us\x01",
            "have experienced it\x01",
            "personally, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F─However, if we solve\x01",
            "any case, it will be\x01",
            "this one.\x02\x03",
            "#00001FAs the Special Support\x01",
            "Section... And above all\x01",
            "else, as her guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04304F#30WI see... Looks like you\x01",
            "decided on that a long\x01",
            "time ago.\x02\x03",
            "#04300FMy Merkabah won't be too\x01",
            "useful for a while...\x02\x03",
            "When it's fixed, we'll\x01",
            "back you up as best we\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13802F...May the Goddess\x01",
            "protect you. Please, be\x01",
            "extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FThanks, Ries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FWe'll be going, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x18, 0x0)
    OP_93(0x19, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7563", 0)
    SetChrPos(0x0, 71500, 0, -610, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_1B(0x3, 0xFF, 0xFFFF)
    SetScenarioFlags(0x1CE, 0)
    EventEnd(0x5)
    Return()

    # Function_35_A761 end

    def Function_36_B675(): pass

    label("Function_36_B675")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6A4")
    SetChrPos(0xFE, 77230, 0, -2080, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B780")

    label("loc_B6A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6D3")
    SetChrPos(0xFE, 78370, 0, -1940, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B780")

    label("loc_B6D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B702")
    SetChrPos(0xFE, 79550, 0, -2100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B780")

    label("loc_B702")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B731")
    SetChrPos(0xFE, 77200, 0, -3170, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B780")

    label("loc_B731")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B760")
    SetChrPos(0xFE, 78370, 0, -3110, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B780")

    label("loc_B760")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B780")
    SetChrPos(0xFE, 79550, 0, -3200, 0)

    label("loc_B780")

    Return()

    # Function_36_B675 end

    def Function_37_B781(): pass

    label("Function_37_B781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7CA")
    SetChrPos(0xFE, 78700, 0, -1050, 270)

    def lambda_B7A6():
        OP_95(0xFE, 71150, 0, -1050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7A6)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B928")

    label("loc_B7CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B813")
    SetChrPos(0xFE, 78650, 0, 0, 270)

    def lambda_B7EF():
        OP_95(0xFE, 71150, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7EF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B928")

    label("loc_B813")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B85C")
    SetChrPos(0xFE, 79740, 0, -1220, 270)

    def lambda_B838():
        OP_95(0xFE, 72240, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B838)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B928")

    label("loc_B85C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A5")
    SetChrPos(0xFE, 79740, 0, -40, 270)

    def lambda_B881():
        OP_95(0xFE, 72240, 0, -40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B881)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B928")

    label("loc_B8A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8EE")
    SetChrPos(0xFE, 80780, 0, -1100, 270)

    def lambda_B8CA():
        OP_95(0xFE, 73280, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B8CA)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B928")

    label("loc_B8EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B928")
    SetChrPos(0xFE, 80780, 0, 20, 270)

    def lambda_B913():
        OP_95(0xFE, 73280, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B913)

    label("loc_B928")

    Return()

    # Function_37_B781 end

    def Function_38_B929(): pass

    label("Function_38_B929")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1240, 1700, -2210, 0)
    MoveCamera(340, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -700, 0, -550, 300)
    SetChrPos(0x102, -1350, 0, -1680, 300)
    SetChrPos(0x104, -670, 0, -2990, 300)
    SetChrPos(0x109, 860, 0, -380, 270)
    SetChrPos(0x105, 350, 0, -1860, 300)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2340, 180, 910, 135)
    SetChrPos(0x1B, -3100, 190, -1070, 135)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x1A,
        "#5POh, you came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PTio! ...Still isn't\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5P*sigh*, that lowers the\x01",
            "tension a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00006FS-Sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PUmm... We're sorry too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FBut Eolia... You're\x01",
            "lovely as ever.\x02\x03",
            "#00304FWhy not take this\x01",
            "opportunity to give up on\x01",
            "PeTiote and change to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PHmm... I'll pass㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FAw, right through the\x01",
            "heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FR-Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHehe. Nice try, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FKnock it off already,\x01",
            "Randy.\x02\x03",
            "#00100FSorry Ling. Now about\x01",
            "that training...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PYeah, let me explain.\x01",
            "It's super simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWhat we'd like you to do with\x01",
            "us is nothing other than take\x01",
            "our own personal training...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIn short, I want to duel\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FDuel you say... You must\x01",
            "mean fighting in combat\x01",
            "form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FBut, why now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWeren't you guys a\x01",
            "little too green a while\x01",
            "back?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FI can't really argue\x01",
            "with that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FWow, another stake\x01",
            "through the heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHaha, well don't worry about that\x01",
            "too much. Think of this duel as a\x01",
            "test of your abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PI think you'll learn a\x01",
            "lot from this\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PUnderstand that Ling and I\x01",
            "have built up some free\x01",
            "time, so it has to be now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PIt's too bad we have to\x01",
            "leave Scott and Wenzel\x01",
            "out of this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha. If those two were here,\x01",
            "this fight would be even more\x01",
            "impossible than it already is.\x02\x03",
            "#00000FBut you're right. There's not\x01",
            "many chances like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FYeah! I always wanted to\x01",
            "practice with someone\x01",
            "who's more experienced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FMore experienced, huh?\x02\x03",
            "#10304FWhen Randy says that, it\x01",
            "seems like it has a\x01",
            "whole different meaning.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10100FWhat do you mean by...\x02\x03",
            "#10114FOh.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)
    TurnDirection(0x102, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00111FWazy... Please don't\x01",
            "stir up any more trouble\x01",
            "than you already have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHaha. It seems your new\x01",
            "members are enjoying\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PYeah, yeah. From what I\x01",
            "can see, both of them\x01",
            "look quite capable.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x12C, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10102FI-I'm not quite sure how\x01",
            "good my own abilities\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHehe, I'm honored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHow 'bout it then? Do\x01",
            "you accept?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYes... If possible, we'd\x01",
            "like to duel.\x02\x03",
            "#00000FWhere are we dueling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PYeah, it has to be a wide open area\x01",
            "that won't interfere with daily life.\x01",
            "So I was thinking the village entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWe got the elder's\x01",
            "permission, so we can\x01",
            "use it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIf you're ready now, we\x01",
            "can begin immediately,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PHow are your equipment\x01",
            "and supplies? We'll wait\x01",
            "if you need to get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FRight...\x02",
    )

    CloseMessageWindow()
    OP_29(0x75, 0x1, 0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Let's Duel!]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C687")

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're all set. Let's get\x01",
            "started.\x02\x03",
            "#00004FWe officially accept\x01",
            "your challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHaha, now you're\x01",
            "talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PAlright then. To the\x01",
            "training ground!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Training with the\x01",
            "Bracers]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C7C2")

    label("loc_C687")


    ChrTalk(
        0x101,
        (
            "#12P#00000FWe'd like to prepare for\x01",
            "a bit. Can you wait for\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PYeah, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PAnd if you've other\x01",
            "business, I don't mind\x01",
            "if it takes priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWe were just looking for\x01",
            "a way to use our free\x01",
            "time, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWe'll just wait here,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C7C2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -70, 0, -3430, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x155, 7)
    SetChrPos(0x1A, -2510, 180, 1180, 270)
    SetChrPos(0x1B, -3380, 190, -810, 0)
    EventEnd(0x5)
    Return()

    # Function_38_B929 end

    def Function_39_C81A(): pass

    label("Function_39_C81A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1240, 1700, -2210, 0)
    MoveCamera(340, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -700, 0, -550, 300)
    SetChrPos(0x102, -1350, 0, -1680, 300)
    SetChrPos(0x104, -670, 0, -2990, 300)
    SetChrPos(0x109, 860, 0, -380, 270)
    SetChrPos(0x105, 350, 0, -1860, 300)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2340, 180, 910, 135)
    SetChrPos(0x1B, -3100, 190, -1070, 135)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x1A,
        "#5PHey, you guys ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PDo you accept our\x01",
            "challenge?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Let's Duel!]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA78")

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, we're all set.\x01",
            "Shall we get going,\x01",
            "then?\x02\x03",
            "We officially accept\x01",
            "your challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHaha, now you're\x01",
            "talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PAlright then. To the\x01",
            "training ground!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Training with the\x01",
            "Bracers]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_CB5A")

    label("loc_CA78")


    ChrTalk(
        0x101,
        (
            "#12P#00006FSorry... It seems it'll\x01",
            "take a little too much\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5POh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWell, if you've got\x01",
            "other business, that\x01",
            "takes precedence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PDon't worry about us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CB5A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -70, 0, -3430, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1A, -2510, 180, 1180, 270)
    SetChrPos(0x1B, -3380, 190, -810, 0)
    EventEnd(0x5)
    Return()

    # Function_39_C81A end

    def Function_40_CBAF(): pass

    label("Function_40_CBAF")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xA, 0xB4, 0x0)
    OP_68(410, 1500, 3290, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Hey, it's the Support\x01",
            "Section. Welcome to Ash\x01",
            "Tree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Want to eat somethin'\x01",
            "today? Or a rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, we're here for work\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()
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
        0xA,
        (
            "Ah, so that's what it\x01",
            "was. I heard about it\x01",
            "from Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright then, allow me\x01",
            "to treat you to my "Chef\x01",
            "Omelet Rice".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, if you please,\x01",
            "master.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x103, -2490, 200, 950, 245)
    SetChrPos(0x101, -4490, 200, 2190, 175)
    SetChrPos(0x104, -5400, 200, 1100, 126)
    SetChrPos(0x102, -5210, 200, -110, 65)
    SetChrPos(0x109, -4380, 200, -1100, 30)
    SetChrPos(0x105, -3410, 200, -1000, 0)
    SetChrPos(0xA, -3130, 200, 3130, 180)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_68(-4100, 1600, 580, 0)
    MoveCamera(310, 33, 0, 0)
    OP_6E(330, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate\x01",
            "the Chef Omelet Rice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00104F*eating*... Hmm, this\x01",
            "omelet rice sure is\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. I think it's\x01",
            "superb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe chicken, rice and ketchup\x01",
            "flavors wrapped in fluffy egg\x01",
            "are quite simple and good.\x02\x03",
            "#00004FAnd I think Armorica Village\x01",
            "is in a nice location,\x01",
            "surrounded by mother nature...\x02\x03",
            "#00009FI don't think anyone should\x01",
            "leave Armorica without having\x01",
            "this first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, I'm embarrassed\x01",
            "you'd say that much\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHaha. It looks like\x01",
            "you're partial to this\x01",
            "omelet rice, Lloyd...\x02\x03",
            "I think we can leave\x01",
            "writing the guide\x01",
            "article to you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00306FWell, this omelet rice has\x01",
            "character. We can recommend\x01",
            "it wholeheartedly.\x02\x03",
            "#00300FWe've had this in the past\x01",
            "many times too, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'll be\x01",
            "responsible for writing\x01",
            "this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By all means, please write\x01",
            "an article that will drive\x01",
            "business for us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -600, 0, 3900, 0)
    SetChrPos(0x102, 600, 0, 3900, 0)
    SetChrPos(0x103, -600, 0, 2700, 0)
    SetChrPos(0x109, 600, 0, 2700, 0)
    SetChrPos(0x104, -600, 0, 1500, 0)
    SetChrPos(0x105, 600, 0, 1500, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
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
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_68(590, 2000, 2950, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(330, 0)
    SetCameraDistance(25000, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x172, 7)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_D4F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_D513")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_D526")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_D539")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_D556")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_D569")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_D586")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_D599")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_D5B6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_D5C9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_D5E6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D5E6")

    OP_29(0x80, 0x1, 0x7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6F1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D6E8")

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

    label("loc_D6E8")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_D6F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7DF")
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

    label("loc_D7DF")

    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -250, 0, -920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_40_CBAF end

    def Function_41_D819(): pass

    label("Function_41_D819")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    OP_68(730, 1500, 2190, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, I'd like to ask you\x01",
            "a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner\x01",
            "who's been visiting the\x01",
            "village recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Oh, the guy who's been\x01",
            "saying at our place off\x01",
            "and on lately, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, he was very polite\x01",
            "and pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FPolite, you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThat's right... Do you\x01",
            "happen to know his name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Umm... "Minneth", I\x01",
            "think it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least that's how he\x01",
            "signed his name in our\x01",
            "guest register.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FMinneth, huh... Well at\x01",
            "least we have his name\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FAnd, do you know\x01",
            "anything about this\x01",
            "Minneth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, well he didn't\x01",
            "really talk much. I can't\x01",
            "really tell you anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although, he called Derrick\x01",
            "to his room and they talked.\x01",
            "This happened several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's all I can tell\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Those must be the\x01",
            "secret discussions with\x01",
            "the chief's son...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah... Anyway, we got\x01",
            "some good info.)\x02\x03",
            "#00000FThank you very much for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No problem. It was my\x01",
            "pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Let me know if you want\x01",
            "to order anything while\x01",
            "you're here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 700, 0, 2050, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4C(0xA, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x174, 1)
    OP_29(0x82, 0x1, 0x1)
    SetChrPos(0x0, 120, 0, 1520, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_D819 end

    def Function_42_DD65(): pass

    label("Function_42_DD65")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-40910, 1500, 2430, 0)
    MoveCamera(345, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -41240, 0, 2080, 45)
    SetChrPos(0x102, -42090, 0, 3420, 90)
    SetChrPos(0x103, -40430, 0, 960, 0)
    SetChrPos(0x104, -41790, 0, 470, 45)
    SetChrPos(0x109, -42790, 0, 1440, 450)
    SetChrPos(0x105, -43210, 0, 2600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, I'd like to ask you\x01",
            "a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner\x01",
            "who's been visiting the\x01",
            "village recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, him. He's got quite\x01",
            "the discerning eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWhat do you mean by\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that he's taken\x01",
            "quite a liking to our\x01",
            "honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""I'll spread this across the\x01",
            "entire continent for sure!"...\x01",
            "That's what he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FSpread, was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FFrom the way he said\x01",
            "it... I guess he's some\x01",
            "kind of merchant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I didn't ask him\x01",
            "the details, but it\x01",
            "seems that he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With such a discerning\x01",
            "eye, he's surely made a\x01",
            "name for himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want my grandkids for\x01",
            "follow his example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAnyway, he seemed like a\x01",
            "skilled merchant, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... That helps.\x02\x03",
            "#00004FThank you very much for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure. Come again\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 2)
    OP_29(0x82, 0x1, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41240, 0, 2080, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_42_DD65 end

    def Function_43_E1C4(): pass

    label("Function_43_E1C4")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xA, 0xB4, 0x0)
    OP_68(410, 1500, 3290, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -510, 0, 3060, 0)
    SetChrPos(0x102, 940, 0, 2410, 0)
    SetChrPos(0x103, -1310, 0, 2160, 0)
    SetChrPos(0x104, 120, 0, 1520, 0)
    SetChrPos(0x109, -980, 0, 540, 0)
    SetChrPos(0x105, 920, 0, 440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Oh... Are you staying\x01",
            "with us tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've got rooms free,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(That's right. If Geval\x01",
            "really did come to\x01",
            "Armorica...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(He likely came to this\x01",
            "inn.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUm, can we ask you\x01",
            "something?\x02\x03",
            "Is there a man by the\x01",
            "name of Geval staying\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, Geval eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's been coming here to\x01",
            "eat every so often\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FJust to eat?\x02\x03",
            "He's not staying with\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, I don't think so. I\x01",
            "don't remember checking\x01",
            "him in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He likes our food, so I\x01",
            "think he's coming here\x01",
            "from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm... I don't think\x01",
            "that's what's going on\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FCould he have a relative\x01",
            "here in Armorica?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIf that were the case,\x01",
            "Alm and Aerie would know\x01",
            "where he is immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_END)), "loc_E60D")

    ChrTalk(
        0x101,
        "#00003FCould it be...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#00001F...Let's try speaking\x01",
            "with the chief. He may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_E680")

    label("loc_E60D")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#00003FFor now, let's have a\x01",
            "look around.\x02\x03",
            "#00000FIt's possible he's in a\x01",
            "good hiding place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E680")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 700, 0, 2050, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x19B, 2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 120, 0, 1520, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_43_E1C4 end

    def Function_44_E6DA(): pass

    label("Function_44_E6DA")

    EventBegin(0x0)
    Fade(500)
    OP_68(-580, 1200, 2920, 0)
    MoveCamera(308, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0xD, -1420, 180, 3810, 90)
    SetChrSubChip(0xD, 0x2)
    SetChrPos(0x101, -470, 0, 2360, 0)
    SetChrPos(0x102, -1200, 0, 1520, 0)
    SetChrPos(0x104, 880, 0, 1830, 0)
    SetChrPos(0x109, 80, 0, 1070, 0)
    SetChrPos(0x105, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_93(0xA, 0xB4, 0x0)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#11POh, it's you guys... The\x01",
            "police's um... Special\x01",
            "Support Section, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThanks for all your help\x01",
            "back then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_E948")

    ChrTalk(
        0xD,
        (
            "#5PYeah, I remember when you\x01",
            "saved those tourists at\x01",
            "the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PAnd you also bothered to help\x01",
            "me find the missing passage\x01",
            "of that library book, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha, don't worry about\x01",
            "it.\x02\x03",
            "#00000FBut anyway, have there\x01",
            "been any strange\x01",
            "incidents recently?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA02")

    label("loc_E948")


    ChrTalk(
        0xD,
        (
            "#5PYeah, I remember when you\x01",
            "saved those tourists at\x01",
            "the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, it has been a long\x01",
            "time.\x02\x03",
            "But anyway, have there\x01",
            "been any strange\x01",
            "incidents recently?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA02")


    ChrTalk(
        0xA,
        (
            "#11PHmm, this village has\x01",
            "been pretty peaceful\x01",
            "lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PBut if I had to say, some\x01",
            "unfamiliar faces visited\x01",
            "this town recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PYeah, that giant red-\x01",
            "haired man and his\x01",
            "pals...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FGiant red-haired man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301F...By any chance, was\x01",
            "his hair color the same\x01",
            "as mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh, now that you mention\x01",
            "it, yours is pretty\x01",
            "similar to his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThat giant red-haired guy had\x01",
            "with him a lively young girl\x01",
            "who had the same shade of hair.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#00001F...Uh, if possible, do you have any\x01",
            "specific details about why they were\x01",
            "here... Or what they were doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAh, I'm sorry to say,\x01",
            "but I wasn't really\x01",
            "keeping an eye on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHow about you, Alf?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Now that you mention it,\x01",
            "I did see them purchase some\x01",
            "goods at the general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For some reason, they were\x01",
            "buying large quantities of\x01",
            "cheese, bacon, and bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Old man Reoir was pretty\x01",
            "happy about making such\x01",
            "a large profit that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIs that so...\x02",
    )

    CloseMessageWindow()

    def lambda_EEAD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EEAD)
    Sleep(50)

    def lambda_EEBD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EEBD)
    Sleep(50)

    def lambda_EECD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EECD)
    Sleep(50)
    OP_93(0x109, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00001F...... So Red Constellation\x01",
            "came to visit Armorica\x01",
            "Village, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAll we know now is that\x01",
            "they came to stock up on\x01",
            "food supplies.\x02\x03",
            "#10103FAnd they seemed to have\x01",
            "only purchased cheap,\x01",
            "cost-effective foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...For a jaeger corps, securing a\x01",
            "food supply is one of their most\x01",
            "fundamental skills.\x02\x03",
            "A battle could break out at any\x01",
            "time, so we have to always be ready.\x02\x03",
            "#00301FAnd since those guys are veteran\x01",
            "jaegers, they've probably already\x01",
            "mapped out this entire area as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHehe, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut, is that really the\x01",
            "only reason they were\x01",
            "here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F...For now, let's just\x01",
            "make a mental note of\x01",
            "this and move on.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F19D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F19D)
    Sleep(50)

    def lambda_F1AD():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F1AD)
    Sleep(50)

    def lambda_F1BD():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F1BD)
    Sleep(50)

    def lambda_F1CD():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F1CD)
    Sleep(50)

    def lambda_F1DD():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F1DD)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00004F...And thanks, guys. You\x01",
            "really helped us gain some\x01",
            "valuable information.\x02\x03",
            "#00000FPlease contact us if you\x01",
            "ever need anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHmm, not sure what's\x01",
            "going on exactly, but you\x01",
            "guys seem pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell, stop by again and I'll be\x01",
            "sure to prepare some delicious\x01",
            "omelet rice for you, okay?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xD, -2060, 180, 4000, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0x14F, 0)
    OP_29(0xA3, 0x1, 0x1)
    SetChrPos(0x0, -470, 0, 2360, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_E6DA end

    def Function_45_F383(): pass

    label("Function_45_F383")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07200.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03700.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03600.itp")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 77920, 0, -5350, 0)
    SetChrPos(0x103, 77920, 0, -5350, 0)
    SetChrPos(0x105, 77920, 0, -5350, 0)
    SetChrPos(0x107, 77920, 0, -5350, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    SetChrPos(0x15, 71500, 0, 0, 180)
    SetChrPos(0x17, 73950, 400, 800, 180)
    OP_68(77910, 700, -5350, 0)
    MoveCamera(320, 30, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_68(72500, 1000, -500, 5000)
    MoveCamera(315, 25, 0, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x101, 1, 0, 46)
    Sleep(750)
    BeginChrThread(0x107, 1, 0, 49)
    Sleep(750)
    BeginChrThread(0x103, 1, 0, 47)
    Sleep(750)
    BeginChrThread(0x105, 1, 0, 48)
    OP_0D()
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x17, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x17,
        "Wah, that's a huge puppy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F653():
        OP_93(0x15, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_F653)
    Sleep(50)

    def lambda_F663():
        OP_93(0x16, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_F663)
    Sleep(50)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x16, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x16,
        "You all are...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x15,
        (
            "Oh... It's you!\x02\x03",
            "Thank goodness you're safe!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PIt's been a while,\x01",
            "Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#12P#3C..."Huge puppy", you\x01",
            "said. Could you be\x01",
            "referring to myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PHaha, I think he likes\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#12PAhaha, even divine\x01",
            "wolves can be cute.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x1)
    SetChrPos(0x15, 78650, 0, 1000, 180)
    SetChrPos(0x16, 77650, 0, 1000, 180)
    SetChrPos(0x17, 74900, 0, -150, 135)
    SetChrPos(0x101, 78650, 0, -1000, 0)
    SetChrPos(0x103, 77650, 0, -1000, 0)
    SetChrPos(0x105, 78650, 0, -2250, 0)
    SetChrPos(0x107, 77650, 0, -2750, 0)
    OP_68(77650, 1200, -110, 0)
    MoveCamera(324, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24250, 0)
    SetCameraDistance(23750, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#03610F#11PI was really worried when\x01",
            "I heard the rumor that\x01",
            "you all were arrested.\x02\x03",
            "#03600FI heard that you are all\x01",
            "wanted escapees, but...\x01",
            "I'm glad you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03708F#11PUmm, what happened to\x01",
            "the other Support\x01",
            "Section members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Unfortunately, we got\x01",
            "separated.\x02\x03",
            "#00208FWe don't even know where\x01",
            "they are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03710F#11PI see... That's\x01",
            "worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PIt seems like you and your\x01",
            "family were visiting right\x01",
            "when the phenomenon occurred?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYes... I had no idea what was\x01",
            "happening at first.\x02\x03",
            "#03608FThen, highway movement\x01",
            "restrictions were put in place and\x01",
            "we couldn't get back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700F#11PBut, we're very grateful to\x01",
            "the villagers.\x02\x03",
            "The innkeeper said we could\x01",
            "stay until the situation dies\x01",
            "down.\x02\x03",
            "#03709FAnd it looks like Colin has\x01",
            "made friends with the\x01",
            "children of the village, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#03809F#5PCamille and Pooley play\x01",
            "with me a lot!\x02\x03",
            "Play with us next time,\x01",
            "okay puppy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CHehe, I shall consider\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609F#11PHaha... Thank you very much.\x02\x03",
            "#03600FAnd so, to repay the\x01",
            "villagers, I have been\x01",
            "helping them out.\x02\x03",
            "#03604FAlthough, I'm responsible\x01",
            "only for negotiating with the\x01",
            "periodic State Guard patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PNo, that's an important role,\x01",
            "given the situation.\x02\x03",
            "#00202FWith a veteran merchant like\x01",
            "you, Harold, those negotiations\x01",
            "probably go smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600F#11PHaha. It's really no big\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x15)

    ChrTalk(
        0x15,
        (
            "#03605F#11POh, but I heard something\x01",
            "interesting during my discussions\x01",
            "with the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PSomething interesting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYes. They said an\x01",
            "unknown rebel force is\x01",
            "lurking in this area.\x02\x03",
            "#03601FThey said it has\x01",
            "attacked State Guard\x01",
            "units several times.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PWow... I can't believe\x01",
            "there could be anyone like\x01",
            "that, given the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PWe don't know who it is\x01",
            "but... I think it's good\x01",
            "intelligence all the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, we should look\x01",
            "into it.\x02\x03",
            "#00001FHarold, do you know of\x01",
            "any sightings of the\x01",
            "rebel force?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PIt seems they were sighted on the\x01",
            "Ancient Battlefield. The entrance\x01",
            "is midway down Armorica Old Road.\x02\x03",
            "#03601FThey said they were attacked\x01",
            "during a regular patrol, but... I\x01",
            "didn't hear the outcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CThe Armorica Ancient Battlefield... A cursed\x01",
            "place where blood was spilled countless times,\x01",
            "and where the cult built its stronghold.\x02\x03",
            "#01201FThere are many hidden passages within those\x01",
            "ruins. If the rebel force is hiding, that\x01",
            "would be a suitable location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PWe don't know what's waiting for\x01",
            "us out there... Let's make sure\x01",
            "our gear is in order before we go.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x17, 0x14)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x1)
    OP_49()
    OP_D7(0x1E)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    SetChrPos(0x16, 71500, 0, -1000, 0)
    SetChrPos(0x15, 71500, 0, 0, 180)
    SetChrPos(0x17, 73950, 400, 800, 180)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    BeginChrThread(0x15, 0, 0, 0)
    BeginChrThread(0x16, 0, 0, 0)
    SetChrPos(0x0, 76660, 0, -1410, 135)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 4)
    OP_29(0xAF, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_45_F383 end

    def Function_46_104BD(): pass

    label("Function_46_104BD")


    def lambda_104C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_104C2)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 73000, 0, -500, 2000, 0x0)
    Return()

    # Function_46_104BD end

    def Function_47_10506(): pass

    label("Function_47_10506")


    def lambda_1050B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1050B)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -1000, 2000, 0x0)
    OP_95(0xFE, 73750, 0, -1000, 2000, 0x0)
    Return()

    # Function_47_10506 end

    def Function_48_1054F(): pass

    label("Function_48_1054F")


    def lambda_10554():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10554)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 75000, 0, -500, 2000, 0x0)
    Return()

    # Function_48_1054F end

    def Function_49_10598(): pass

    label("Function_49_10598")


    def lambda_1059D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1059D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
    OP_95(0xFE, 74250, 0, 0, 2000, 0x0)
    Return()

    # Function_49_10598 end

    SaveToFile()

Try(main)
