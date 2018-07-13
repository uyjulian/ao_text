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
        "Function_7_C5E",          # 07, 7
        "Function_8_D76",          # 08, 8
        "Function_9_1EB0",         # 09, 9
        "Function_10_1EB4",        # 0A, 10
        "Function_11_2EE4",        # 0B, 11
        "Function_12_2EE8",        # 0C, 12
        "Function_13_4415",        # 0D, 13
        "Function_14_5230",        # 0E, 14
        "Function_15_537B",        # 0F, 15
        "Function_16_614D",        # 10, 16
        "Function_17_74DC",        # 11, 17
        "Function_18_7FE6",        # 12, 18
        "Function_19_8076",        # 13, 19
        "Function_20_80E9",        # 14, 20
        "Function_21_839B",        # 15, 21
        "Function_22_8975",        # 16, 22
        "Function_23_8A1D",        # 17, 23
        "Function_24_8B33",        # 18, 24
        "Function_25_8C65",        # 19, 25
        "Function_26_99D8",        # 1A, 26
        "Function_27_9B79",        # 1B, 27
        "Function_28_9BB3",        # 1C, 28
        "Function_29_9BED",        # 1D, 29
        "Function_30_9E58",        # 1E, 30
        "Function_31_A243",        # 1F, 31
        "Function_32_A72F",        # 20, 32
        "Function_33_A91E",        # 21, 33
        "Function_34_AB04",        # 22, 34
        "Function_35_ABC7",        # 23, 35
        "Function_36_BB41",        # 24, 36
        "Function_37_BC4D",        # 25, 37
        "Function_38_BDF5",        # 26, 38
        "Function_39_CD61",        # 27, 39
        "Function_40_D100",        # 28, 40
        "Function_41_DDA4",        # 29, 41
        "Function_42_E2FF",        # 2A, 42
        "Function_43_E761",        # 2B, 43
        "Function_44_EC9A",        # 2C, 44
        "Function_45_F95A",        # 2D, 45
        "Function_46_10AB6",       # 2E, 46
        "Function_47_10AFF",       # 2F, 47
        "Function_48_10B48",       # 30, 48
        "Function_49_10B91",       # 31, 49
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
            "There is a car magazine, "Orbal Car Freak Vol.2".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x372, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5A")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Pop Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x372, 1)

    label("loc_C5A")

    TalkEnd(0xFF)
    Return()

    # Function_6_BA8 end

    def Function_7_C5E(): pass

    label("Function_7_C5E")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★Ash Tree Inn Recommended Dish★\x01",
            "　    ～　Chef's Omelet Rice　～\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Chef's Omelet Rice recipe is written down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_D72")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D72")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Chef's Omelet Rice"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D72")

    TalkEnd(0xFF)
    Return()

    # Function_7_C5E end

    def Function_8_D76(): pass

    label("Function_8_D76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA5")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFF")

    ChrTalk(
        0x8,
        (
            "With that unknown huge tree appearing,\x01",
            "I was worried that Jake would\x01",
            "have boggled up, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Harold's words, on the other hand,\x01",
            "seem to have exalted his motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For a trader, commercial spirit is the most\x01",
            "important thing... It's sprouted within Jake,\x01",
            "so I think he'll be alright from now on too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB2")

    label("loc_EFF")


    ChrTalk(
        0x8,
        (
            "For a trader, commercial spirit is the most\x01",
            "important thing... It's sprouted within Jake too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know what's going to happen to\x01",
            "Crossbell, but I've got no regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB2")

    Jump("loc_1EAC")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AD")

    ChrTalk(
        0x8,
        (
            "It seems Harold is\x01",
            "properly supporting his\x01",
            "family of Sophia and Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, if Jake had something\x01",
            "like that too, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even finding a genuine wife for\x01",
            "my grandchild might not be too\x01",
            "bad, after I retire.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113C")

    label("loc_10AD")


    ChrTalk(
        0x8,
        (
            "Hm, if I could find a\x01",
            "wife to support Jake in\x01",
            "public and private life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even finding a wife for my grandchild\x01",
            "might not be too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113C")

    Jump("loc_1EAC")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_12C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(
        0x8,
        (
            "Harold is negotiating for us\x01",
            "with the State Guard over\x01",
            "supplying us goods.\x02",
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
            "That Jake, if he could do\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C3")

    label("loc_1229")


    ChrTalk(
        0x8,
        (
            "That Jake, if he could\x01",
            "be a great trader\x01",
            "like Harold is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...No, I mustn't. He's gotten\x01",
            "some motivation recently. \x01",
            "I won't scold him too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C3")

    Jump("loc_1EAC")

    label("loc_12C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(
        0x8,
        (
            "Awhile ago, Jake got\x01",
            "motivation like he's\x01",
            "a different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though he's still\x01",
            "inexperienced, I\x01",
            "can finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to train him again\x01",
            "so I can put up the "Jake's\x01",
            "General Store" sign someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1453")

    label("loc_13BC")


    ChrTalk(
        0x8,
        (
            "Jake finally got\x01",
            "some motivation.\x01",
            "Now I can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to train him again\x01",
            "so I can put up the "Jake's\x01",
            "General Store" sign someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1453")

    Jump("loc_1EAC")

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151C")

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
            "But even so,\x01",
            "that Jake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He looks different\x01",
            "than usual today. Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1580")

    label("loc_151C")


    ChrTalk(
        0x8,
        (
            "That Jake... He looks\x01",
            "somehow different\x01",
            "than usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()

    label("loc_1580")

    Jump("loc_1EAC")

    label("loc_1585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_17EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1646")

    ChrTalk(
        0x8,
        (
            "It seems Mr. Minneth\x01",
            "is conducting his final\x01",
            "negotiations today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if his plan with\x01",
            "Derrick is finally starting.\x01",
            "Dear me, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_1646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1744")

    ChrTalk(
        0x8,
        (
            "When I casually looked out the window,\x01",
            "there were monsters in the public square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And from the looks of things,\x01",
            "that Mr. Minneth seemed\x01",
            "to be manipulating them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And in that shocking\x01",
            "moment, my back \x01",
            "hips gave out. Ouch...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17E9")

    label("loc_1744")


    ChrTalk(
        0x8,
        (
            "That Mr. Minneth was manipulating\x01",
            "the monsters that appeared in\x01",
            "the public square, wasn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And in that shocking\x01",
            "moment, my back \x01",
            "hips gave out. Ouch...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E9")

    Jump("loc_1EAC")

    label("loc_17EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1874")

    ChrTalk(
        0x8,
        (
            "I recently met a promising\x01",
            "man comparable to Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho, he's doing a lot\x01",
            "of good things for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190C")

    label("loc_1874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1883")
    Jump("loc_190C")

    label("loc_1883")


    ChrTalk(
        0x8,
        (
            "The man took a\x01",
            "liking to our\x01",
            "village's honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, hm, surely he's a trader\x01",
            "who's made a name for himself.\x01",
            "No mistake about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190C")

    Jump("loc_1EAC")

    label("loc_1911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(
        0x8,
        (
            "I'll retire soon, and I want to\x01",
            "leave the store to Jake, but...\x02",
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
            "Hm, I wish he had some\x01",
            "reason to want to...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A5D")

    label("loc_19DB")


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
            "I wonder if I could\x01",
            "give him some reason\x01",
            "to want to...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5D")

    Jump("loc_1EAC")

    label("loc_1A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4E")

    ChrTalk(
        0x8,
        (
            "My hips have been acting up lately.\x01",
            "I'm old too, you know.\x02",
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
            "No matter what I do, this grandchild\x01",
            "never wants to take it over.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BCF")

    label("loc_1B4E")


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
            "That guy has no motivation.\x01",
            "Things are looking grim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCF")

    Jump("loc_1EAC")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_1DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D09")

    ChrTalk(
        0x8,
        (
            "A red-headed stern man...\x01",
            "Yes, yes, indeed someone like him\x01",
            "came to the village with his friends recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were an imposing bunch, \x01",
            "but they bought a lot from my store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jake was scared of him, but he was a\x01",
            "very good customer in a long time.\x01",
            "Ho ho ho...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DC8")

    label("loc_1D09")


    ChrTalk(
        0x8,
        (
            "That redheaded stern man was a\x01",
            "very good customer in a long time.\x01",
            "Ho ho ho...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jake was scared of him, but one mustn't\x01",
            "judge customers by appearances.\x01",
            "That guy has a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC8")

    Jump("loc_1EAC")

    label("loc_1DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    ChrTalk(
        0x8,
        (
            "Harold came to do\x01",
            "business with us earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, he's a\x01",
            "promising trader..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish Jake would\x01",
            "follow his example.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EAC")

    label("loc_1E5E")


    ChrTalk(
        0x8,
        (
            "Harold is a\x01",
            "promising trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish Jake would\x01",
            "follow his example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAC")

    TalkEnd(0xFE)
    Return()

    # Function_8_D76 end

    def Function_9_1EB0(): pass

    label("Function_9_1EB0")

    Call(0, 10)
    Return()

    # Function_9_1EB0 end

    def Function_10_1EB4(): pass

    label("Function_10_1EB4")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F11")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1F11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F30")
    OP_AF(0x4F)
    Jump("loc_1F62")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F40")
    OP_AF(0x4E)
    Jump("loc_1F62")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F50")
    OP_AF(0x4D)
    Jump("loc_1F62")

    label("loc_1F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F60")
    OP_AF(0x4C)
    Jump("loc_1F62")

    label("loc_1F60")

    OP_AF(0x4B)

    label("loc_1F62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EDB")

    label("loc_1F71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F85")
    Jump("loc_2EDB")

    label("loc_1F85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F9D")
    TalkEnd(0x9)
    Return()

    label("loc_1F9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EDB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CB")

    ChrTalk(
        0x9,
        (
            "When Mr. Harold left, \x01",
            "he gave me some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            ""It's the mission of us traders to do\x01",
            "our best for everyone, especially\x01",
            "in times like these"...he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I can be of help to someone\x01",
            "by being a trader, I must do it\x01",
            "even if it kills me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2144")

    label("loc_20CB")


    ChrTalk(
        0x9,
        (
            "If I can be of help to someone\x01",
            "by being a trader, I must do it\x01",
            "even if it kills me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Alright... Let's do this!!\x02",
    )

    CloseMessageWindow()

    label("loc_2144")

    Jump("loc_2EDB")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2211")

    ChrTalk(
        0x9,
        (
            "I-I get the feeling grandpa is thinking about\x01",
            "something inappropriate for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because the times are like this, he should be\x01",
            "worried about the crops harvest decline.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EDB")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_23CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2339")

    ChrTalk(
        0x9,
        (
            "The other day, I saw Mr. Harold\x01",
            "negotiating with the State Guard and\x01",
            "I thought I still have a long way to go.\x02",
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
            "Since he's here, I was thinking\x01",
            "of asking Mr. Harold for advice...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C5")

    label("loc_2339")


    ChrTalk(
        0x9,
        (
            "I already know basically what my grandfather's\x01",
            "going to say by the look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I must become a fine\x01",
            "trader like Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C5")

    Jump("loc_2EDB")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245B")

    ChrTalk(
        0x9,
        (
            "Hello, and welcome to\x01",
            ""Reoir's General Store".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I recommend honey, our specialty.\x01",
            "Be sure to give it a look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24CF")

    label("loc_245B")


    ChrTalk(
        0x9,
        (
            "...How was that?\x01",
            "Pretty good, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe. I've got to learn this stuff\x01",
            "if I want to take over the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24CF")

    Jump("loc_2EDB")

    label("loc_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_265E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25CB")

    ChrTalk(
        0x9,
        (
            "Grandpa hurt his hips yesterday, \x01",
            "you see. He should take the day off...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But probably, he's worried because I'm\x01",
            "unreliable and can't leave the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...*sigh*, what am I doing.\x01",
            "I've got to try harder...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2659")

    label("loc_25CB")


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
            "I wonder if I could try harder,\x01",
            "so my grandpa won't worry, \x02",
        )
    )

    CloseMessageWindow()

    label("loc_2659")

    Jump("loc_2EDB")

    label("loc_265E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2783")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2703")

    ChrTalk(
        0x9,
        (
            "Everyone's talking\x01",
            "about village reform...\x01",
            "I wonder about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't really mind if\x01",
            "I live as I have up\x01",
            "until now. Carefree.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277E")

    label("loc_2703")


    ChrTalk(
        0x9,
        (
            "Grandpa hurt his hips\x01",
            "earlier. I wonder if\x01",
            "he's all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, that's right. I have\x01",
            "to bring him a compress...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_277E")

    Jump("loc_2EDB")

    label("loc_2783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286F")

    ChrTalk(
        0x9,
        (
            "I've been seeing a well-dressed\x01",
            "man often in the village lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That guy said to my grandpa,\x01",
            ""That's an able grandson you have",\x01",
            "and grandpa was delighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...As expected,\x01",
            "that was flattery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28D5")

    label("loc_286F")


    ChrTalk(
        0x9,
        (
            "Grandpa...\x01",
            "He looked happy hearing\x01",
            "compliments about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...As expected,\x01",
            "that was flattery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D5")

    Jump("loc_2EDB")

    label("loc_28DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D9")

    ChrTalk(
        0x9,
        (
            "Before long, I've got to tell grandpa\x01",
            "clearly that I've got no intention\x01",
            "of taking over the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, if I told him, he would\x01",
            "probably be dejected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, whatever. I'll continue\x01",
            "for awhile, just like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A91")

    label("loc_29D9")


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
            "...Well, whatever. I'll continue\x01",
            "for awhile, just like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A91")

    Jump("loc_2EDB")

    label("loc_2A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B53")

    ChrTalk(
        0x9,
        (
            "It seems grandpa wants me to\x01",
            "take over the general store, but... \x01",
            "Honestly, that's a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'll leave for\x01",
            "the city and strike it rich.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BC4")

    label("loc_2B53")


    ChrTalk(
        0x9,
        "I really don't want to take over the store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'll leave for\x01",
            "the city and strike it rich.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC4")

    Jump("loc_2EDB")

    label("loc_2BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_2D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF1")

    ChrTalk(
        0x9,
        (
            "A redheaded, large man? Oh yeah,\x01",
            "there was a man like that awhile\x01",
            "back who came with his friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Grandpa was happy\x01",
            "to turn a profit...\x01",
            "But I was somehow scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those guys weren't respectable. They were\x01",
            "planning something, no mistake about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D7F")

    label("loc_2CF1")


    ChrTalk(
        0x9,
        (
            "That large, redheaded man...\x01",
            "He wasn't respectable, \x01",
            "and I was scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...But the redheaded girl that\x01",
            "was with him was pretty cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")

    Jump("loc_2EDB")

    label("loc_2D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E56")

    ChrTalk(
        0x9,
        (
            "Hello, and welcome. \x01",
            "Have a look around... Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Here, we deal in honey, the village's\x01",
            "speciality product... Ladies and gentlemen.\x02",
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
    Jump("loc_2EDB")

    label("loc_2E56")


    ChrTalk(
        0x9,
        (
            "My grandpa says he wants me\x01",
            "to follow Mr. Harold's example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Comparing me to a veteran trader\x01",
            "is honestly too much to bear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDB")

    Jump("loc_1EC1")

    label("loc_2EE0")

    TalkEnd(0x9)
    Return()

    # Function_10_1EB4 end

    def Function_11_2EE4(): pass

    label("Function_11_2EE4")

    Call(0, 12)
    Return()

    # Function_11_2EE4 end

    def Function_12_2EE8(): pass

    label("Function_12_2EE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F31")
    Call(0, 40)
    Return()

    label("loc_2F31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5F")
    Call(0, 41)
    Return()

    label("loc_2F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8D")
    Call(0, 43)
    Return()

    label("loc_2F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FA4")
    Call(0, 44)
    Return()

    label("loc_2FA4")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4411")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3010")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3010")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3030")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_440C")

    label("loc_3030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3050")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_440C")

    label("loc_3050")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3064")
    Jump("loc_440C")

    label("loc_3064")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307C")
    TalkEnd(0xA)
    Return()

    label("loc_307C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_440C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_3133")

    ChrTalk(
        0xA,
        (
            "I'm somewhat embarrassed you'd\x01",
            "give us such high praise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha, by all means, please\x01",
            "make an article that will\x01",
            "drive business for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440C")

    label("loc_3133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_32FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3286")

    ChrTalk(
        0xA,
        (
            "The appearance of that pale azure\x01",
            "huge tree was quite surprising.\x02",
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
            "An exhausted  priest\x01",
            "and sister arrived\x01",
            "just some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got to bring them\x01",
            "too some coffee later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32F9")

    label("loc_3286")


    ChrTalk(
        0xA,
        (
            "An exhausted Father\x01",
            "and Sister arrived\x01",
            "just some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got to bring them\x01",
            "too some coffee later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F9")

    Jump("loc_440C")

    label("loc_32FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_352F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(
        0xA,
        (
            "The rumor of that declaration of\x01",
            "invalidity has reached this village too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We didn't have a very good impression of the\x01",
            "President in the village from the start, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Around now, the people in the\x01",
            "city too must sense the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to happen next...\x01",
            "Personally, I'm going to keep my eyes on things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_352A")

    label("loc_3470")


    ChrTalk(
        0xA,
        (
            "Around now, the people in the city too must\x01",
            "sense the problems with the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to happen next...\x01",
            "Personally, I'm going to keep my eyes on things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352A")

    Jump("loc_440C")

    label("loc_352F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3690")

    ChrTalk(
        0xA,
        (
            "Harold and his family are\x01",
            "staying in the large room on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, if Crossbell is in such a situation,\x01",
            "we probably won't be getting any new\x01",
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
    Jump("loc_373E")

    label("loc_3690")


    ChrTalk(
        0xA,
        (
            "Even so, it was a long\x01",
            "sought vacation for Harold.\x01",
            "How unlucky.\x02",
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

    label("loc_373E")

    Jump("loc_440C")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_393A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37E9")

    ChrTalk(
        0xA,
        (
            "I thought Mr. Geval came here\x01",
            "from the city because he\x01",
            "liked our food, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...I wonder where he's staying?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3935")

    label("loc_37E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C9")

    ChrTalk(
        0xA,
        (
            "The raid attack a few days ago\x01",
            "shook the peace throughout the\x01",
            "autonomous state of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tensions at the borders are\x01",
            "growing ever greater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what's going\x01",
            "to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3935")

    label("loc_38C9")


    ChrTalk(
        0xA,
        (
            "Tensions at the borders are\x01",
            "growing ever greater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what's going\x01",
            "to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3935")

    Jump("loc_440C")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0F")

    ChrTalk(
        0xA,
        (
            "Today, I'm lending out the large\x01",
            "room on 2F for Sunday School.\x02",
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
            "Sister also, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A87")

    label("loc_3A0F")


    ChrTalk(
        0xA,
        (
            "Sunday School is being held\x01",
            "today in the large room on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think I'll make\x01",
            "pudding for everyone\x01",
            "as a snack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A87")

    Jump("loc_440C")

    label("loc_3A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B39")

    ChrTalk(
        0xA,
        (
            "I heard in general what Derrick's\x01",
            "been doing lately away from\x01",
            "the Village Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, I wonder if it'll be\x01",
            "all right. A new business...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB8")

    label("loc_3B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C29")

    ChrTalk(
        0xA,
        (
            "I can't believe it... To think\x01",
            "that Mr. Minneth was a\x01",
            "crook... I never realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You could call him a\x01",
            "master of deceit. \x01",
            "What a frightening guy.\x02",
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
    Jump("loc_3CB8")

    label("loc_3C29")


    ChrTalk(
        0xA,
        (
            "Anyway, thank goodness Derrick was\x01",
            "able to reconcile with the Village Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That was a good way\x01",
            "to take advantage\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB8")

    Jump("loc_440C")

    label("loc_3CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D53")

    ChrTalk(
        0xA,
        (
            "*sigh*, I wonder when\x01",
            "Derrick will feel\x01",
            "like returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope he makes up with\x01",
            "the Village Chief soon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E08")

    label("loc_3D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D62")
    Jump("loc_3E08")

    label("loc_3D62")


    ChrTalk(
        0xA,
        (
            "I haven't had much contact\x01",
            "with Mr. Minneth, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like he's been meeting\x01",
            "with Derrick often lately... \x01",
            "I wonder what they're talking about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF2")

    ChrTalk(
        0x101,
        (
            "#00003F(Come to think of it, it\x01",
            "seems like we can get gourmet\x01",
            "guide coverage here, but...)\x02\x03",
            "#00001F(Now isn't the time. Let's not\x01",
            "forget to return here later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF2")

    Jump("loc_440C")

    label("loc_3EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_415D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A3")
    SetChrSubChip(0x12, 0x1)
    TurnDirection(0xA, 0x12, 0)

    ChrTalk(
        0xA,
        (
            "Derrick... It's not like the Village Chief\x01",
            "will reject it without listening\x01",
            "to what you have to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "No. I'm sure he'll think\x01",
            "it's no good because\x01",
            "it was my idea.\x02",
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
    Jump("loc_4158")

    label("loc_40A3")


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
            "treat him to a cup of\x01",
            "my special blend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4158")

    Jump("loc_440C")

    label("loc_415D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4279")

    ChrTalk(
        0xA,
        (
            "The heads of state from each\x01",
            "nation have come to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This event is unprecedented\x01",
            "in Crossbell history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They say Crossbell City's new mayor\x01",
            "was the one who proposed it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A bold idea. Just\x01",
            "what you'd expect\x01",
            "from the head of IBC.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4322")

    label("loc_4279")


    ChrTalk(
        0xA,
        (
            "The West Zemuria Trade Conference...\x01",
            "So it's finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The surrounding countries' interest in it seems high,\x01",
            "and I too am worried about how it will go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4322")

    Jump("loc_440C")

    label("loc_4327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_440C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433F")
    Jump("loc_440C")

    label("loc_433F")


    ChrTalk(
        0xA,
        (
            "The large redheaded man and his\x01",
            "friends didn't do anything especially\x01",
            "suspicious in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It looked like he had skilled men\x01",
            "and women with him... That's\x01",
            "just the kind of people they were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440C")

    Jump("loc_2FB1")

    label("loc_4411")

    TalkEnd(0xA)
    Return()

    # Function_12_2EE8 end

    def Function_13_4415(): pass

    label("Function_13_4415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44EB")

    ChrTalk(
        0xB,
        (
            "I didn't pay heed\x01",
            "to Keith, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh. He's quite manly.\x01",
            "I've changed my opinion\x01",
            "of him, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I unconsciously laughed earlier, \x01",
            "but I'll have to apologize later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4572")

    label("loc_44EB")


    ChrTalk(
        0xB,
        (
            "Keith is pretty manly. \x01",
            "I've changed my \x01",
            "opinion of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I unconsciously laughed earlier, \x01",
            "but I'll have to apologize later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4572")

    Jump("loc_522C")

    label("loc_4577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_46C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4636")

    ChrTalk(
        0xB,
        (
            "Mrs. Sophia is\x01",
            "a great cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's giving me cooking\x01",
            "lessons while she's staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, I'm going to\x01",
            "make a better omelet\x01",
            "rice than my father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46C3")

    label("loc_4636")


    ChrTalk(
        0xB,
        (
            "Mrs. Sophia is giving me cooking \x01",
            "lessons while she is staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, I'm going to\x01",
            "make a better omelet\x01",
            "rice than my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C3")

    Jump("loc_522C")

    label("loc_46C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_482C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479F")

    ChrTalk(
        0xB,
        (
            "Aah, Colin is\x01",
            "sooo cute㈱\x02",
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
            "As expected from the man I look up to,\x01",
            "Mr. Harold. I'm looking forward to\x01",
            "seeing how he turns out!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4827")

    label("loc_479F")


    ChrTalk(
        0xB,
        (
            "Aah, Colin is\x01",
            "sooo cute㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected from the man I look up to,\x01",
            "Mr. Harold. I'm looking forward to\x01",
            "seeing how he turns out!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4827")

    Jump("loc_522C")

    label("loc_482C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4925")

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
            "An armed group attacking a place\x01",
            "like that is unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like the police or CGF\x01",
            "to capture them somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49C5")

    label("loc_4925")


    ChrTalk(
        0xB,
        (
            "An attack on Crossbell City...\x01",
            "That armed group is unforgivable.\x02",
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

    label("loc_49C5")

    Jump("loc_522C")

    label("loc_49CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A72")

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
    Jump("loc_522C")

    label("loc_4A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C57")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B15")

    ChrTalk(
        0xB,
        (
            "Mr. Minneth came today to\x01",
            "talk about something important\x01",
            "to Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if the finale of\x01",
            "their plan is coming soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C52")

    label("loc_4B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD3")

    ChrTalk(
        0xB,
        (
            "That Minneth... He was\x01",
            "a despicable impostor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph. I thought he was\x01",
            "suspicious from the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The next time he shows up,\x01",
            "I'm going to let him have it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C52")

    label("loc_4BD3")


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
            "The next time he shows up,\x01",
            "I'm going to let him have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C52")

    Jump("loc_522C")

    label("loc_4C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D28")

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
            "Though I heard he is from a\x01",
            "famous foreign company,\x01",
            "he doesn't brag about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, there are men of\x01",
            "character in this world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DD4")

    label("loc_4D28")


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
            "famous company, he doesn't brag about it...\x01",
            "So there exist man of character too, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD4")

    Jump("loc_522C")

    label("loc_4DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF4")
    Call(0, 14)
    Jump("loc_4E8B")

    label("loc_4DF4")


    ChrTalk(
        0xB,
        (
            "I want to see Orchis Tower,\x01",
            "but there's the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you can down ten plates\x01",
            "of our omelet rice in an hour,\x01",
            "I could go on a date with you☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8B")

    Jump("loc_522C")

    label("loc_4E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_50B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8E")

    ChrTalk(
        0xB,
        (
            "Those Bracers\x01",
            "sure are strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though Mr. Arios draws the most\x01",
            "attention, those female Bracers\x01",
            "aren't too bad themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, you guys too, of course. Thanks\x01",
            "to you guys, everyone had a good time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5041")

    label("loc_4F8E")


    ChrTalk(
        0xB,
        (
            "Though Mr. Arios draws the most\x01",
            "attention, those female Bracers\x01",
            "aren't too bad themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, you guys too, of course. Thanks\x01",
            "to you guys, everyone had a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5041")

    Jump("loc_50AB")

    label("loc_5046")


    ChrTalk(
        0xB,
        (
            "The Bracers are here to\x01",
            "exterminate monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, I've got to give\x01",
            "them proper service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AB")

    Jump("loc_522C")

    label("loc_50B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_522C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A3")

    ChrTalk(
        0xB,
        (
            "Welcome. Please sit\x01",
            "at any seat you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all is said and done, I simply\x01",
            "must recommend our omelet rice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've recently improved it.\x01",
            "It tastes better than ever, so if\x01",
            "you like, please have some.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_522C")

    label("loc_51A3")


    ChrTalk(
        0xB,
        (
            "Mr. Harold is taking\x01",
            "the room on 2F today.\x02",
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

    label("loc_522C")

    TalkEnd(0xFE)
    Return()

    # Function_13_4415 end

    def Function_14_5230(): pass

    label("Function_14_5230")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Sealy, do you want to go to\x01",
            "the city with me next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Let's go see the\x01",
            "rumored Orchis Tower!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, but I have to\x01",
            "help with the store...\x02",
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
            "N-No, no... \x01",
            "That's obviously impossible.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_5230 end

    def Function_15_537B(): pass

    label("Function_15_537B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_54D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5478")

    ChrTalk(
        0xC,
        (
            "To be perfectly honest, this situation isn't\x01",
            "one that a guy like me can understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No matter what happens,\x01",
            "I have to protect Sealy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Though when I said this straight \x01",
            "to her face, she laughed... Tohoho.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54D3")

    label("loc_5478")


    ChrTalk(
        0xC,
        (
            "I was laughed at\x01",
            "by Sealy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No matter what\x01",
            "happens, I have\x01",
            "to protect her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54D3")

    Jump("loc_6149")

    label("loc_54D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_566D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CE")

    ChrTalk(
        0xC,
        (
            "Just between you and me, Sealy's\x01",
            "skill as a cook is...well, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was frankly scared when\x01",
            "she served me an omelet rice\x01",
            "that looked like cinders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Well, I forced myself and wolfed it down, though!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5668")

    label("loc_55CE")


    ChrTalk(
        0xC,
        (
            "Just between you and me, Sealy's\x01",
            "skill as a cook is...well, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, no matter what she serves,\x01",
            "I gotta force myself to fully eat it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5668")

    Jump("loc_6149")

    label("loc_566D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_57D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5753")

    ChrTalk(
        0xC,
        (
            "Those State Guards\x01",
            "are creepy.\x02",
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
            "Are the CGF really all that great, now\x01",
            "that they've become the State Guard?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_57D1")

    label("loc_5753")


    ChrTalk(
        0xC,
        (
            "Somehow those State\x01",
            "Guards make me mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are the CGF really all that great, now\x01",
            "that they've become the State Guard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D1")

    Jump("loc_6149")

    label("loc_57D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C6")

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
            "It's true that CGF patrols\x01",
            "have increased recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel like Crossbell's\x01",
            "turning into a\x01",
            "dangerous place...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5960")

    label("loc_58C6")


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
            "I feel like Crossbell's turning\x01",
            "into a dangerous place...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5960")

    Jump("loc_6149")

    label("loc_5965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A4B")

    ChrTalk(
        0xC,
        (
            "Oh, come to think of\x01",
            "it, that referendum\x01",
            "is fast approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a bit of a pain to go all the\x01",
            "way to the city to vote, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But this affects\x01",
            "the villagers too,\x01",
            "so I'll have to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5AD9")

    label("loc_5A4B")


    ChrTalk(
        0xC,
        (
            "The referendum on the question of\x01",
            "independence is fast approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a pain to go to the city and\x01",
            "vote, but... I'll have to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AD9")

    Jump("loc_6149")

    label("loc_5ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D2F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF4")

    ChrTalk(
        0xC,
        (
            "It seems Mr. Minneth and Derrick have\x01",
            "finished their discussions for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want to celebrate the rebirth of Armorica\x01",
            "Village and launch their effort with a bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. Sealy is fond of show,\x01",
            "so I'm sure she'd love it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5CA7")

    label("loc_5BF4")


    ChrTalk(
        0xC,
        (
            "It seems Mr. Minneth and Derrick have\x01",
            "finished their discussions for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want to launch their effort\x01",
            "with a bang, and celebrate\x01",
            "Armorica's rebirth with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA7")

    Jump("loc_5D2A")

    label("loc_5CAC")


    ChrTalk(
        0xC,
        (
            "What Mr. Minneth was talking about...\x01",
            "Could it all have been a lie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "*sigh*, that Derrick must\x01",
            "be quite depressed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2A")

    Jump("loc_6149")

    label("loc_5D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF1")

    ChrTalk(
        0xC,
        (
            "That foreigner man seems to have\x01",
            "a wealth of life experiences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He saw through that I\x01",
            "long for Sealy and he\x01",
            "encouraged me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Man, what a good guy...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E56")

    label("loc_5DF1")


    ChrTalk(
        0xC,
        (
            "That foreigner man...\x01",
            "I long for Sealy and he\x01",
            "encouraged me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Man, what a good guy...\x02",
    )

    CloseMessageWindow()

    label("loc_5E56")

    Jump("loc_6149")

    label("loc_5E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E76")
    Call(0, 14)
    Jump("loc_5EE6")

    label("loc_5E76")


    ChrTalk(
        0xC,
        (
            "Tohoho... And just when I'd worked\x01",
            "up the courage to invite her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Sealy can be pretty harsh sometimes.\x02",
    )

    CloseMessageWindow()

    label("loc_5EE6")

    Jump("loc_6149")

    label("loc_5EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FAD")

    ChrTalk(
        0xC,
        (
            "Actually, I want\x01",
            "to ask Sealy on a\x01",
            "date before long.\x02",
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
        "I'm sure she'll be ok with it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6023")

    label("loc_5FAD")


    ChrTalk(
        0xC,
        (
            "I plan to ask Sealy on\x01",
            "a date before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Alright. Today, I'll ready my heart...\x01",
            "And do the deed tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6023")

    Jump("loc_6149")

    label("loc_6028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CD")

    ChrTalk(
        0xC,
        (
            "I long for Sealy, the\x01",
            "poster girl for this store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can't get enough of her\x01",
            "smile that I end up staying\x01",
            "longer than I should...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6149")

    label("loc_60CD")


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
            "...Well, refills\x01",
            "aren't free, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6149")

    TalkEnd(0xFE)
    Return()

    # Function_15_537B end

    def Function_16_614D(): pass

    label("Function_16_614D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6164")
    Call(0, 44)
    Return()

    label("loc_6164")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_632B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627D")

    ChrTalk(
        0xD,
        (
            "A "Cryptid" is still here, that strange\x01",
            "huge tree appeared and highway\x01",
            "movement is restricted...\x02",
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
            "Yeah, that's Harold for you.\x01",
            "I eagerly await his return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6326")

    label("loc_627D")


    ChrTalk(
        0xD,
        (
            "Harold is wise, so\x01",
            "I'm sure he'll bring\x01",
            "me a book I like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...That said, the situation is\x01",
            "like this, so I want him to be as\x01",
            "careful as possible on the highway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6326")

    Jump("loc_74D8")

    label("loc_632B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_64F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6438")

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
            "finally took action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At this rate, things will improve.\x01",
            "I wonder if the barrier surrounding\x01",
            "the city will disappear too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64F4")

    label("loc_6438")


    ChrTalk(
        0xD,
        (
            "I wonder if at this rate, the barrier\x01",
            "surrounding the city will disappear too?\x02",
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

    label("loc_64F4")

    Jump("loc_74D8")

    label("loc_64F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_66B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6616")

    ChrTalk(
        0xD,
        (
            "With the "Cryptid" and the highway movement\x01",
            "restrictions, we can't do farm work, so I'd\x01",
            "like to read a book for a change of pace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But obviously I can't go to\x01",
            "the Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't you think that reading\x01",
            "really enriches life, hm?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66AB")

    label("loc_6616")


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
            "If such a life would last for years,\x01",
            "I could only call it a hell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66AB")

    Jump("loc_74D8")

    label("loc_66B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C8")

    ChrTalk(
        0xD,
        (
            "I already read the\x01",
            "Crossbell Times Extra\x01",
            "awhile back several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm concerned about the attack, but\x01",
            "the article about Ilya's serious injury\x01",
            "was the most shocking of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...As a citizen of Crossbell, I\x01",
            "pray she makes a full recovery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_684D")

    label("loc_67C8")


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
        "...I pray she makes a full recover.\x02",
    )

    CloseMessageWindow()

    label("loc_684D")

    Jump("loc_74D8")

    label("loc_6852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_69C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6938")

    ChrTalk(
        0xD,
        (
            "The pleasant sound of rain tapping on\x01",
            "the windows, warm coffee by my side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, rainy days make for\x01",
            "great reading weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is a good chance\x01",
            "to read all those\x01",
            "books I've piled up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69C1")

    label("loc_6938")


    ChrTalk(
        0xD,
        (
            "The pleasant sound of rain tapping on\x01",
            "the windows, warm coffee by my side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, rainy days make for\x01",
            "great reading weather.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C1")

    Jump("loc_74D8")

    label("loc_69C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6D06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB3")

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
            "I wonder if the Village Chief should\x01",
            "discard the old traditions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I at least understand that\x01",
            "Derrick wants reform.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6B30")

    label("loc_6AB3")


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
            "I at least understand that\x01",
            "Derrick wants reform.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B30")

    Jump("loc_6D01")

    label("loc_6B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C34")

    ChrTalk(
        0xD,
        (
            "It seems that Minneth did a nice\x01",
            "job winning over the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What another person wants...\x01",
            "His insight to see through that\x01",
            "was the real deal for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the end, he used that\x01",
            "rare talent for fraud...\x01",
            "He's beyond help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D01")

    label("loc_6C34")


    ChrTalk(
        0xD,
        (
            "That Minneth... If he didn't involved\x01",
            "himself in fraud, he might \x01",
            "have been very successful.\x02",
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

    label("loc_6D01")

    Jump("loc_74D8")

    label("loc_6D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E75")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "I borrowed "Ten Mysteries of Crossbell\x01",
            "that Really Exist" from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The story of the "Man Who Searches for\x01",
            "His Own Head"... Ooh, how chilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah, that one's really scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's lost his own head, \x01",
            "but cries out to find\x01",
            "it for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...That's not really\x01",
            "a scary part.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_6EF2")

    label("loc_6E75")


    ChrTalk(
        0xD,
        (
            "*sigh*, and just when\x01",
            "I was so scared,\x01",
            "Gｷfan ruined it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I must teach this guy how to\x01",
            "properly enjoy a ghost story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF2")

    Jump("loc_74D8")

    label("loc_6EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_727A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7044")

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
            "But it seems I\x01",
            "skipped a volume.\x02",
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

    label("loc_7044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F9")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "Today, I borrowed "Beauties\x01",
            "that Moved the Continent".\x01",
            "...It was quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a book that introduces you to the historic \x01",
            "achievements of women in each nation,\x01",
            "starting from "Walkｸre Lianne".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. Maybe originally, women\x01",
            "were the powerful ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I too am always hen-\x01",
            "pecked by my daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(I think that's just because\x01",
            "you're unreliable, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_7275")

    label("loc_71F9")


    ChrTalk(
        0xD,
        (
            ""Beauties that Moved the Continent"...\x01",
            "It's pretty interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why don't you guys try\x01",
            "to read it at the library?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7275")

    Jump("loc_74D8")

    label("loc_727A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_740F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7379")

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
            "traffic restrictions due to\x01",
            "the President's arrival.\x02",
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
    Jump("loc_740A")

    label("loc_7379")


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
            "I'll go to the library and\x01",
            "look for some book to read.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_740A")

    Jump("loc_74D8")

    label("loc_740F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_74D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7427")
    Jump("loc_74D8")

    label("loc_7427")


    ChrTalk(
        0xD,
        (
            "It looked like they bought\x01",
            "preserved food from Mr.\x01",
            "Reoir's general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. I wonder if they're going mountain climbing.\x01",
            "I've never seen a group like them, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D8")

    TalkEnd(0xFE)
    Return()

    # Function_16_614D end

    def Function_17_74DC(): pass

    label("Function_17_74DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_764F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7593")

    ChrTalk(
        0xE,
        (
            "Mr. Harold's family\x01",
            "returned to the city.\x02",
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
    Jump("loc_764A")

    label("loc_7593")


    ChrTalk(
        0xE,
        (
            "Mr. Harold's family was worried about\x01",
            "their neighborhood, so it's good\x01",
            "that they returned to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When Stefan and I return to the city,\x01",
            "I'll be sure to say hi to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764A")

    Jump("loc_7FE2")

    label("loc_764F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_765D")
    Jump("loc_7FE2")

    label("loc_765D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_77F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_775D")

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
            "Mr. Harold's family is worried\x01",
            "about the city too, but they're\x01",
            "doing all they can to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I've got to do what I can too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_77F3")

    label("loc_775D")


    ChrTalk(
        0xE,
        (
            "Mr. Harold's family is worried\x01",
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

    label("loc_77F3")

    Jump("loc_7FE2")

    label("loc_77F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D9")

    ChrTalk(
        0xE,
        (
            "*sigh*... A raid attack\x01",
            "on the city was\x01",
            "completely unexpected.\x02",
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
            "I hope something like\x01",
            "this never happens again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7952")

    label("loc_78D9")


    ChrTalk(
        0xE,
        (
            "*sigh*... A raid attack\x01",
            "on the city was\x01",
            "completely unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope something like\x01",
            "this never happens again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7952")

    Jump("loc_7FE2")

    label("loc_7957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A47")

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
            "It must be difficult, commuting\x01",
            "here from the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to be thankful to the sister\x01",
            "for coming all the way here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7ACB")

    label("loc_7A47")


    ChrTalk(
        0xE,
        (
            "It must be difficult, traveling\x01",
            "here from the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to be thankful to the sister\x01",
            "for coming all the way here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ACB")

    Jump("loc_7FE2")

    label("loc_7AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B93")

    ChrTalk(
        0xE,
        (
            "The Village Chief's son...\x01",
            "He's been tense ever since\x01",
            "he got back yesterday.\x02",
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
    Jump("loc_7C1A")

    label("loc_7B93")


    ChrTalk(
        0xE,
        (
            "Thank goodness Stefan and the village\x01",
            "children weren't attacked by monsters.\x02",
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

    label("loc_7C1A")

    Jump("loc_7FE2")

    label("loc_7C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CDC")

    ChrTalk(
        0xE,
        (
            "Hum huhuuum...\x01",
            "That does it for the sheets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I admired hotel maids before\x01",
            "I gave birth to Stefan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh, helping out at this\x01",
            "bar-inn is pretty fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7D5F")

    label("loc_7CDC")


    ChrTalk(
        0xE,
        (
            "Uh uh, helping out at this\x01",
            "bar-inn is pretty fun.\x02",
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

    label("loc_7D5F")

    Jump("loc_7FE2")

    label("loc_7D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7DE8")

    ChrTalk(
        0xE,
        (
            "Today I'm helping\x01",
            "clean the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They've supported Stefan\x01",
            "and I, so I want to help\x01",
            "them in any way I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FE2")

    label("loc_7DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E03")
    Call(0, 23)
    Jump("loc_7E87")

    label("loc_7E03")


    ChrTalk(
        0xE,
        (
            "My, can I really?\x01",
            "I will gladly accept, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh, I heard from Stefan\x01",
            "he had some before and I\x01",
            "wanted to try some too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E87")

    Jump("loc_7FE2")

    label("loc_7E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7FE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F53")

    ChrTalk(
        0xE,
        (
            "My son Stefan and I moved\x01",
            "here from Crossbell City \x01",
            "awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That child hated it at first,\x01",
            "but it seems he's gotten used to\x01",
            "life here. Uh uh, thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7FE2")

    label("loc_7F53")


    ChrTalk(
        0xE,
        (
            "By the way, Mr. Gｷfan\x01",
            "is renting us this room\x01",
            "cheap as a courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh, the people of this village\x01",
            "are warm and kind, aren't they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE2")

    TalkEnd(0xFE)
    Return()

    # Function_17_74DC end

    def Function_18_7FE6(): pass

    label("Function_18_7FE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8072")

    ChrTalk(
        0xF,
        (
            "The inn's old man will make\x01",
            "us snacks for recess during\x01",
            "today's Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Aww. I want it to be recess alreadyyy.\x02",
    )

    CloseMessageWindow()

    label("loc_8072")

    TalkEnd(0xFE)
    Return()

    # Function_18_7FE6 end

    def Function_19_8076(): pass

    label("Function_19_8076")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_80E5")

    ChrTalk(
        0x10,
        (
            "Pooley is\x01",
            "studying with\x01",
            "everyone todayyy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "She doesn't understand a single thing, though.\x02",
    )

    CloseMessageWindow()

    label("loc_80E5")

    TalkEnd(0xFE)
    Return()

    # Function_19_8076 end

    def Function_20_80E9(): pass

    label("Function_20_80E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81CF")

    ChrTalk(
        0x11,
        (
            "I went to check on things\x01",
            "in the city with my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "On all the friends and\x01",
            "neighbors I lived with\x01",
            "before, everyone was safe.\x02",
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
    Jump("loc_8271")

    label("loc_81CF")


    ChrTalk(
        0x11,
        (
            "Until yesterday, I was with my mom\x01",
            "checking on things in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "All the friends and neighbors\x01",
            "I lived with before were safe.\x01",
            "Really, thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8271")

    Jump("loc_8397")

    label("loc_8276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_832B")

    ChrTalk(
        0x11,
        (
            "I used to go to the cathedral\x01",
            "when I lived in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But now that I live\x01",
            "in the village, the\x01",
            "Sister comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "...That's a little easier.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8397")

    label("loc_832B")


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
        "...Now it's a little easier.\x02",
    )

    CloseMessageWindow()

    label("loc_8397")

    TalkEnd(0xFE)
    Return()

    # Function_20_80E9 end

    def Function_21_839B(): pass

    label("Function_21_839B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_83F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83F0")

    ChrTalk(
        0x12,
        (
            "...I have an important\x01",
            "visitor today. Get out\x01",
            "of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F0")

    Jump("loc_8971")

    label("loc_83F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8756")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8751")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86AE")

    ChrTalk(
        0x12,
        "...Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMr. Derrick... \x01",
            "Umm, if possible, I'd like you to \x01",
            "talk once more with your father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...Hmph. I've already\x01",
            "spoken with him many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But the Village Chief is a staunch\x01",
            "conservative. He doesn't approve of\x01",
            "my reforms, no even a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I was just about to give up on\x01",
            "reform, when Mr. Minneth\x01",
            "came and gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My father can't be trusted...\x01",
            "The two of us will reform\x01",
            "Armorica Village splendidly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...There's suspicious points about Minneth.\x01",
            "I'd like him to rethink this if possible, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(We've insufficient evidence at present.\x01",
            "He'll be difficult to persuade...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8751")

    label("loc_86AE")


    ChrTalk(
        0x12,
        (
            "I had given up on village\x01",
            "reform, but Mr. Minneth\x01",
            "gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My father can't be trusted...\x01",
            "The two of us will reform\x01",
            "Armorica Village splendidly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8751")

    Jump("loc_8971")

    label("loc_8756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88DE")

    ChrTalk(
        0x12,
        (
            "My father, the Village Chief... No matter\x01",
            "what kind of reform proposals I give him,\x01",
            "he stubbornly refuses to approve them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "He always repeats the same things. "How the village\x01",
            "should be" and "Don't lose sight of reality", he says...\x02",
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
        (
            "...*sigh*,\x01",
            "somehow I'm tired.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8971")

    label("loc_88DE")


    ChrTalk(
        0x12,
        (
            "If the Village Chief won't accept them,\x01",
            "reforms can't proceed. It's just a\x01",
            "matter of time before we're ruined...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...Somehow\x01",
            "I got tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8971")

    TalkEnd(0xFE)
    Return()

    # Function_21_839B end

    def Function_22_8975(): pass

    label("Function_22_8975")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8A19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8993")
    Call(0, 23)
    Jump("loc_8A19")

    label("loc_8993")


    ChrTalk(
        0x13,
        (
            "Oh, right, today I came to\x01",
            "share some of this with you.\x02",
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

    label("loc_8A19")

    TalkEnd(0xFE)
    Return()

    # Function_22_8975 end

    def Function_23_8A1D(): pass

    label("Function_23_8A1D")

    OP_4B(0xE, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Then, you've been staying\x01",
            "in this room for awhile?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes. He offered, and I\x01",
            "thought to take him up on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In return, I'm\x01",
            "thinking of helping\x01",
            "out with the store.\x02",
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

    # Function_23_8A1D end

    def Function_24_8B33(): pass

    label("Function_24_8B33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD3")

    ChrTalk(
        0x14,
        (
            "On my way here today, \x01",
            "I noticed giant cat\x01",
            "footprints here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I wonder what happened\x01",
            "In this village yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8C61")

    label("loc_8BD3")


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
            "In this village yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C61")

    TalkEnd(0xFE)
    Return()

    # Function_24_8B33 end

    def Function_25_8C65(): pass

    label("Function_25_8C65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8C76")
    Jump("loc_99D4")

    label("loc_8C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_90B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9007")

    ChrTalk(
        0x15,
        (
            "#03600FOh, everyone...!\x01",
            "Thank goodness you're safe.\x02\x03",
            "#03603FI heard the rumors of Chairman\x01",
            "MacDowell's independence\x01",
            "declaration of invalidity.\x02\x03",
            "#03605FCould you have been...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, we've been busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHas there been any changes\x01",
            "at Amorica Village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FNo, not as of yet...\x02\x03",
            "#03600FIt's just, the State Guard\x01",
            "seemed confused during my\x01",
            "negotiations with them just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAs expected, it seems the influence \x01",
            "on the village is small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if pushed, I'd say the\x01",
            "influence on the city is greater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FYes. I'm worried about my\x01",
            "neighbors, as well as my friends\x01",
            "at Mainz and St. Ursula Hospital.\x02\x03",
            "#03608FI'd go visit them if I\x01",
            "could move freely, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Anyway, I can't say the situation has\x01",
            "completely changed for the better yet.\x02\x03",
            "#00000FPlease be careful,\x01",
            "Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#03600FYes, you guys be careful too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 5)
    Jump("loc_90B1")

    label("loc_9007")


    ChrTalk(
        0x15,
        (
            "#03603FI'm worried about my neighbors in\x01",
            "the city, and my friends in Mainz\x01",
            "and St. Ursula Hospital as well.\x02\x03",
            "#03608FI'd go visit them if I\x01",
            "could move freely, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90B1")

    Jump("loc_99D4")

    label("loc_90B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D1")
    Call(0, 26)
    Jump("loc_918D")

    label("loc_90D1")


    ChrTalk(
        0x15,
        (
            "#03600FAt the moment, I'm assembling goods the\x01",
            "villagers need for the next negotiations\x01",
            "with the State Guard.\x02\x03",
            "#03603FEveryone, please. Do be careful.\x01",
            "...May the Goddess protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_918D")

    Jump("loc_99D4")

    label("loc_9192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_926B")
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
            "#1K◆[Fraud Case Day 2]? (Debug)\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not cleared]\x01",      # 2
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
        (0, "loc_9252"),
        (1, "loc_9257"),
        (2, "loc_9261"),
        (SWITCH_DEFAULT, "loc_926B"),
    )


    label("loc_9252")

    Jump("loc_926B")

    label("loc_9257")

    OP_29(0x87, 0x4, 0x10)
    Jump("loc_926B")

    label("loc_9261")

    OP_29(0x87, 0x3, 0x10)
    Jump("loc_926B")

    label("loc_926B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_938D")

    ChrTalk(
        0x15,
        (
            "#03600FI received an invitation\x01",
            "from the Village Chief to come.\x02\x03",
            "#03603FAlthough it seems Pete\x01",
            "declined his invitation for\x01",
            "helping with the fraud case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThat case with Minneth...\x01",
            "So that's what happened.\x02\x03",
            "#00003FThank goodness Pete\x01",
            "didn't get involved...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9488")

    label("loc_938D")


    ChrTalk(
        0x15,
        (
            "#03600FI received an invitation\x01",
            "from the Village Chief to come.\x02\x03",
            "#03603FIt seems Pete declined the\x01",
            "invitation for helping with\x01",
            "a certain case, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSo that's what happened, huh.\x02\x03",
            "#00003FThank goodness Pete\x01",
            "didn't get involved...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9488")


    ChrTalk(
        0x15,
        "#03600FYes, I feel the same.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_954F")

    label("loc_94B2")


    ChrTalk(
        0x15,
        (
            "#03600FThe Resistance force was sighted at\x01",
            "the Ancient Battlefield. The entrance\x01",
            "is in midway alongf the Old Road.\x02\x03",
            "#03603FEveryone, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954F")

    Jump("loc_99D4")

    label("loc_9554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_99D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9813")

    ChrTalk(
        0x101,
        (
            "#00000FAh...Mr. Harold.\x01",
            "So you're here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03605FOh, it's the Special Support Section. \x01",
            "Fancy meeting you here.\x02\x03",
            "#03600FYes, I'm here for business\x01",
            "negotiations today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, you're\x01",
            "doing your honest\x01",
            "trades as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609FHa ha. Thankfully\x01",
            "I got some good\x01",
            "deals today.\x02\x03",
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
            " x10 received.\x02",
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
            "#03600FYes. Actually, it's a little something\x01",
            "extra I got in one of my deals.\x02\x03",
            "#03609FWe can't eat them all,\x01",
            "so I hope they'll\x01",
            "be useful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUmm, then...\x01",
            "We gladly accept.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 6)
    Jump("loc_99D4")

    label("loc_9813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_992C")

    ChrTalk(
        0x15,
        (
            "#03604FThankfully, I\x01",
            "got some good\x01",
            "deals today.\x02\x03",
            "#03608FIt's just, lately, the Village Chief and Derrick's\x01",
            "arguments show no sign of stopping. \x01",
            "It's a very worrying state of affairs.\x02\x03",
            "#03603FThe relationship between a father\x01",
            "and son must be a difficult one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_99D4")

    label("loc_992C")


    ChrTalk(
        0x15,
        (
            "#03603FThe Village Chief and Derrick...\x01",
            "They both want to protect\x01",
            "their village, but...\x02\x03",
            "#03608FThe relationship between a father\x01",
            "and son must be a difficult one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99D4")

    TalkEnd(0xFE)
    Return()

    # Function_25_8C65 end

    def Function_26_99D8(): pass

    label("Function_26_99D8")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#03608FMr. Reoir's lumbago medicine...\x01",
            "and Mrs. Ange's supply of\x01",
            "band-aids are running short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700FThe innkeeper is\x01",
            "running low of some\x01",
            "seasoning too.\x02\x03",
            "#03708FSome of them are spices you can\x01",
            "only get at the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FHmm... I'll make do with\x01",
            "the band-aids, but I'll\x01",
            "need the other things.\x02\x03",
            "#03600FThank you, Sophia. Please rest,\x01",
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

    # Function_26_99D8 end

    def Function_27_9B79(): pass

    label("Function_27_9B79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA8")
    Call(0, 38)
    Return()

    label("loc_9BA8")

    Call(0, 39)
    Return()

    label("loc_9BAC")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_27_9B79 end

    def Function_28_9BB3(): pass

    label("Function_28_9BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BE2")
    Call(0, 38)
    Return()

    label("loc_9BE2")

    Call(0, 39)
    Return()

    label("loc_9BE6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_28_9BB3 end

    def Function_29_9BED(): pass

    label("Function_29_9BED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9BFE")
    Jump("loc_9E54")

    label("loc_9BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9C0C")
    Jump("loc_9E54")

    label("loc_9C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C27")
    Call(0, 26)
    Jump("loc_9CA7")

    label("loc_9C27")


    ChrTalk(
        0x16,
        (
            "#03700FAs my husband's partner, I help him,\x01",
            "even though I'm not good at it.\x02\x03",
            "I hope I can be of some\x01",
            "use to the villagers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA7")

    Jump("loc_9E54")

    label("loc_9CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DD1")

    ChrTalk(
        0x16,
        (
            "#03708FThe other members of the Support\x01",
            "Section... How worrying.\x02\x03",
            "#03700FI pray that you're able to\x01",
            "reunite with them safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHu hu, thank you madame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FNow that things have come to this, we must\x01",
            "do whatever it takes to meet up with them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_9E54")

    label("loc_9DD1")


    ChrTalk(
        0x16,
        (
            "#03708FThe other members of the Support\x01",
            "Section... How worrying.\x02\x03",
            "#03700FI pray that you're able to\x01",
            "reunite with them safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E54")

    TalkEnd(0xFE)
    Return()

    # Function_29_9BED end

    def Function_30_9E58(): pass

    label("Function_30_9E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E69")
    Jump("loc_A23F")

    label("loc_9E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9E77")
    Jump("loc_A23F")

    label("loc_9E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9EF9")

    ChrTalk(
        0x17,
        (
            "#03805FHmm, it looks like papa\x01",
            "and mama are working...\x02\x03",
            "#03800FShould I go play with\x01",
            "Camille and the otheeers?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A23F")

    label("loc_9EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A23F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A10C")
    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F9D")
    Jump("loc_9FE7")

    label("loc_9F9D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FBD")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FE7")

    label("loc_9FBD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FDD")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FE7")

    label("loc_9FDD")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9FE7")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEhehe, doggy.\x01",
            "Let's play agaaain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3CHm, if time will allow it.\x02\x03",
            "#01203F...Still, since I've joined the\x01",
            "Support Section, little kids have\x01",
            "become very attached to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FUh uh, that is one of your\x01",
            "good points, Zeit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_A23A")

    label("loc_A10C")

    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A19D")
    Jump("loc_A1E7")

    label("loc_A19D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1BD")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E7")

    label("loc_A1BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1DD")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E7")

    label("loc_A1DD")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1E7")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEhehe, doggy.\x01",
            "Let's play agaaain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A23A")

    ClearChrFlags(0x17, 0x10)

    label("loc_A23F")

    TalkEnd(0xFE)
    Return()

    # Function_30_9E58 end

    def Function_31_A243(): pass

    label("Function_31_A243")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A259")
    SetScenarioFlags(0x2, 2)

    label("loc_A259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A68D")

    ChrTalk(
        0x18,
        (
            "#04303F#30WOur Merkabah won't be\x01",
            "too useful for awhile...\x02\x03",
            "#04300FWhen it's fixed, we'll back\x01",
            "you up as best we can.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_A3F1")
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x105, 0)
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A37D")
    Jump("loc_A3C7")

    label("loc_A37D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A39D")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3C7")

    label("loc_A39D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3BD")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3C7")

    label("loc_A3BD")

    OP_52(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3C7")

    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x10)

    label("loc_A3F1")


    ChrTalk(
        0x18,
        (
            "#04308F#30W──Wazy. Don't do anything\x01",
            "too crazy. You hear?\x02\x03",
            "#04301FIf you squander your powers like me,\x01",
            "it'll turn deadly when it counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403FYeah... I'll keep\x01",
            "that in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A688")
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#04300F#30WOh yeah... I almost\x01",
            "forgot. Lloyd, take this.\x02",
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
        "#00305FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSome kind of fragment...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#04303F#30WIt was where the Aion\x01",
            "crashed... It's probably\x01",
            "one of its parts.\x02\x03",
            "#04300FThinking you might find a \x01",
            "way to put it to good use,\x01",
            "I've picked it up.\x02\x03",
            "#04311FWell, just take it with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen...\x01",
            "I'll gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A688")

    Jump("loc_A72B")

    label("loc_A68D")


    ChrTalk(
        0x18,
        (
            "#04303F#30WOur Merkabah won't be\x01",
            "too useful for awhile...\x02\x03",
            "#04300FWhen it's fixed, we'll back\x01",
            "you up as best we can.\x02\x03",
            "#04302FAnyway, do your best, guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A72B")

    TalkEnd(0xFE)
    Return()

    # Function_31_A243 end

    def Function_32_A72F(): pass

    label("Function_32_A72F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A884")

    ChrTalk(
        0x19,
        (
            "#13808FWhen KeA was coming to Sunday School,\x01",
            "she was talking about the fun times\x01",
            "she had with you all.\x02\x03",
            "#13804F...As a Knight of the Gralsritter, I\x01",
            "won't say anything inappropriate, but...\x02\x03",
            "#13802FI think getting her smile back is\x01",
            "the most important thing of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FMiss Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F...Acknowledged.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A91A")

    label("loc_A884")


    ChrTalk(
        0x19,
        (
            "#13808FWhen KeA was coming to Sunday School,\x01",
            "she was talking about the fun times\x01",
            "she had with you all.\x02\x03",
            "#13804F...Please, take back \x01",
            "that smile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A91A")

    TalkEnd(0xFE)
    Return()

    # Function_32_A72F end

    def Function_33_A91E(): pass

    label("Function_33_A91E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA55")

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
            "I'm concerned about the rocky relationship\x01",
            "between Derrick and the Village Chief, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't interfere, though. Bracers\x01",
            "must remain neutral at all times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_AB00")

    label("loc_AA55")


    ChrTalk(
        0xFE,
        (
            "I'm concerned about the rocky relationship\x01",
            "between Derrick and the Village Chief, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't interfere, though. Bracers\x01",
            "must remain neutral at all times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB00")

    TalkEnd(0xFE)
    Return()

    # Function_33_A91E end

    def Function_34_AB04(): pass

    label("Function_34_AB04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB84")

    ChrTalk(
        0xFE,
        (
            "I saw a well-dressed\x01",
            "man crossing the\x01",
            "bridge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. I have\x01",
            "no interest in humans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_ABC3")

    label("loc_AB84")


    ChrTalk(
        0xFE,
        "*munch, munch*...\x02",
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

    label("loc_ABC3")

    TalkEnd(0xFE)
    Return()

    # Function_34_AB04 end

    def Function_35_ABC7(): pass

    label("Function_35_ABC7")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC66")
    BeginChrThread(0x109, 1, 0, 36)
    WaitChrThread(0x109, 1)

    label("loc_AC66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC80")
    BeginChrThread(0x105, 1, 0, 36)
    WaitChrThread(0x105, 1)

    label("loc_AC80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC9A")
    BeginChrThread(0x106, 1, 0, 36)
    WaitChrThread(0x106, 1)

    label("loc_AC9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACB4")
    BeginChrThread(0x10A, 1, 0, 36)
    WaitChrThread(0x10A, 1)

    label("loc_ACB4")

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

    def lambda_AD98():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AD98)
    Sleep(50)

    def lambda_ADA8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_ADA8)
    Sleep(50)

    def lambda_ADB8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_ADB8)
    Sleep(50)

    def lambda_ADC8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_ADC8)
    Sleep(50)

    def lambda_ADD8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_ADD8)
    Sleep(50)

    def lambda_ADE8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_ADE8)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMiss Ries...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE56")

    ChrTalk(
        0x105,
        "#10402FSo this is where you were.\x02",
    )

    CloseMessageWindow()

    label("loc_AE56")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AED5")

    ChrTalk(
        0x18,
        (
            "#11P#04300F#30WOh... If it isn't Wazy,\x01",
            "Lloyd and friends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEFE")

    label("loc_AED5")


    ChrTalk(
        0x18,
        "#11P#04300F#30WOh... You guys, huh.\x02",
    )

    CloseMessageWindow()

    label("loc_AEFE")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFDE")
    BeginChrThread(0x109, 1, 0, 37)
    WaitChrThread(0x109, 1)

    label("loc_AFDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFF8")
    BeginChrThread(0x105, 1, 0, 37)
    WaitChrThread(0x105, 1)

    label("loc_AFF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B012")
    BeginChrThread(0x106, 1, 0, 37)
    WaitChrThread(0x106, 1)

    label("loc_B012")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B02C")
    BeginChrThread(0x10A, 1, 0, 37)
    WaitChrThread(0x10A, 1)

    label("loc_B02C")

    WaitChrThread(0x104, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00000FWe have something to ask the both of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FYou shot down that absurd\x01",
            "flyin' doll, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00104FThat was really good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04302F#30WHa ha... I took a lot of\x01",
            "damage on my end too, though.\x02\x03",
            "#04306FUnfortunately, I've used up all my\x01",
            "power and now I'm resting...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2AF")

    ChrTalk(
        0x103,
        (
            "#6P#00205FAccording to Mr. Abbas,\x01",
            "using quite a dangerous "power"\x01",
            "puts you in a grave situation...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FYeah. You used the "Stigma"'s\x01",
            "power together with the Merkabah,\x01",
            "releasing it all at once, right?\x02\x03",
            "#10402FHow reckless. You might have gone to\x01",
            "see the Goddess if you were careless.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B318")

    label("loc_B2AF")


    ChrTalk(
        0x103,
        (
            "#6P#00205FAccording to Mr. Abbas,\x01",
            "using quite a dangerous "power"\x01",
            "puts you in a grave situation...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B318")


    ChrTalk(
        0x101,
        "#6P#00005FI-Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13800FYes, by nature, the "Stigma" is a\x01",
            "source of forbidden power which\x01",
            "is too much for the human body...\x02\x03",
            "#13808FThere is a limit to how much power\x01",
            "you can recklessly release.\x02\x03",
            "#13803FI can't help but say it was really careless for\x01",
            "one in the responsible position of "Dominion".\x02",
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
            "#11P#04306F#30W...*sigh*, Ries. Give\x01",
            "me a break already.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B594")

    ChrTalk(
        0x105,
        (
            "#12P#10409FHa ha. It looks like\x01",
            "you're being henpecked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62F")

    label("loc_B594")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5E8")

    ChrTalk(
        0x109,
        (
            "#12P#10109F(I-It sure looks like\x01",
            "he's being dominated...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62F")

    label("loc_B5E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B62F")

    ChrTalk(
        0x106,
        (
            "#12P#10702F(Uh uh. Looks like\x01",
            "he's outmatched...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B69B")

    ChrTalk(
        0x10A,
        (
            "#12P#00603F(Gralsritter Dominions...\x01",
            "They sure are quite different than I heard.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B765")

    label("loc_B69B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B707")

    ChrTalk(
        0x106,
        (
            "#12P#10704F(Gralsritter Dominions... They are\x01",
            "quite different than what I heard.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B765")

    label("loc_B707")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B765")

    ChrTalk(
        0x109,
        (
            "#12P#10106F*sigh*. I think you too should\x01",
            "listen to what Mr. Abbas says.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B765")


    ChrTalk(
        0x18,
        (
            "#11P#04303F#30WBy the way...\x02\x03",
            "#04308FOne hell of a thing has\x01",
            "appeared for sure, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13801FThe "Tree of Azure"... A miracle\x01",
            "brought forth from human tenacity.\x02\x03",
            "#13803FTo think something like that could appear \x01",
            "from someone aside the Goddess...\x02\x03",
            "#13808FAnd what's more, from Miss KeA's power...\x02",
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
            "can fully believe it yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F──However, I absolutely intend to\x01",
            "solve this case with our hands.\x02\x03",
            "#00001FAs the "Special Support Section"...\x01",
            "And above all else, as her guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04304F#30WI see... Looks like you decided\x01",
            "on that a long time ago.\x02\x03",
            "#04300FOur Merkabah won't be\x01",
            "too useful for awhile...\x02\x03",
            "When it's fixed, we'll back\x01",
            "you up as best we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13802F...May the Goddess protect you.\x01",
            "Please, be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FThanks, dear Ries.\x02",
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

    # Function_35_ABC7 end

    def Function_36_BB41(): pass

    label("Function_36_BB41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB70")
    SetChrPos(0xFE, 77230, 0, -2080, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC4C")

    label("loc_BB70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9F")
    SetChrPos(0xFE, 78370, 0, -1940, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC4C")

    label("loc_BB9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBCE")
    SetChrPos(0xFE, 79550, 0, -2100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC4C")

    label("loc_BBCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBFD")
    SetChrPos(0xFE, 77200, 0, -3170, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC4C")

    label("loc_BBFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC2C")
    SetChrPos(0xFE, 78370, 0, -3110, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC4C")

    label("loc_BC2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC4C")
    SetChrPos(0xFE, 79550, 0, -3200, 0)

    label("loc_BC4C")

    Return()

    # Function_36_BB41 end

    def Function_37_BC4D(): pass

    label("Function_37_BC4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC96")
    SetChrPos(0xFE, 78700, 0, -1050, 270)

    def lambda_BC72():
        OP_95(0xFE, 71150, 0, -1050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BC72)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BC96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCDF")
    SetChrPos(0xFE, 78650, 0, 0, 270)

    def lambda_BCBB():
        OP_95(0xFE, 71150, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BCBB)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BCDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD28")
    SetChrPos(0xFE, 79740, 0, -1220, 270)

    def lambda_BD04():
        OP_95(0xFE, 72240, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD04)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BD28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD71")
    SetChrPos(0xFE, 79740, 0, -40, 270)

    def lambda_BD4D():
        OP_95(0xFE, 72240, 0, -40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD4D)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BD71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDBA")
    SetChrPos(0xFE, 80780, 0, -1100, 270)

    def lambda_BD96():
        OP_95(0xFE, 73280, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD96)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BDBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDF4")
    SetChrPos(0xFE, 80780, 0, 20, 270)

    def lambda_BDDF():
        OP_95(0xFE, 73280, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BDDF)

    label("loc_BDF4")

    Return()

    # Function_37_BC4D end

    def Function_38_BDF5(): pass

    label("Function_38_BDF5")

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
            "#5PLittle Tio!\x01",
            "...She's not with you yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5P*sigh*, that lowers the tension a bit.\x02",
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
        (
            "#5PNo... \x01",
            "WE are sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FBut Miss Eolia... \x01",
            "You're as lovely as ever.\x02\x03",
            "#00304FWhy not take this opportunity to\x01",
            "give up on peTiote and switch to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PNo, I'll pass㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FAw, right through the heart!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FS-Senior Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHu hu, nice suicide attack.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FKnock it off,\x01",
            "both of you.\x02\x03",
            "#00100FSorry Miss Ling.\x01",
            "Now, about your\x01",
            "request...\x02",
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
            "#5PWhat we'd like you to do with us is nothing\x01",
            "other than take our own personal training...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIn short, I want to have\x01",
            "a match with you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FA match... You must mean\x01",
            "real fighting training, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBut, why such a\x01",
            "request now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWeren't you guys a little\x01",
            "too green awhile back?\x02",
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
        "#12P#00012FI can't really argue with that, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FYes, you hit us where it hurts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHa ha, well don't worry about that\x01",
            "too much. Think of this match as\x01",
            "a test of your abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PI think you'll learn a\x01",
            "lot from this experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PUnderstand that Ling and\x01",
            "my free times overlap,\x01",
            "so it has to be now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PIt's too bad we have to leave\x01",
            "Scott and Wenzel out, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha. If those two were here,\x01",
            "this fight would be even more\x01",
            "impossible than it already is.\x02\x03",
            "#00000FBut you're right. There's\x01",
            "not many chances like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FYeah! I always wanted to practice\x01",
            "with someone who's more experienced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FMore experienced, huh?\x02\x03",
            "#10304FWhen Randy says that, it seems like\x01",
            "it has a whole different meaning.\x02",
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
            "#10114FAh.\x02",
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
            "#6P#00111FWazy... Please don't stir up any more\x01",
            "trouble than you already have, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHa ha. It seems your new members\x01",
            "will make us have some fun too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PYeah, yeah. From what I can see,\x01",
            "both of them look quite capable.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x12C, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10102FI-I'm not quite sure how\x01",
            "good my own abilities are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, I'm honored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHow about it then?\x01",
            "Do you accept?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYes... If possible, we'd\x01",
            "like to have a match.\x02\x03",
            "#00000FWhere're we doing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWell, it has to be a wide open area\x01",
            "that won't interfere with daily life.\x01",
            "So I was thinking the village entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWe got the Village Chief's permission,\x01",
            "so we can use it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIf you're ready now, we can\x01",
            "begin immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PHow are your equipment and supplies?\x01",
            "We'll wait if you need to get ready.\x02",
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
            "[All Set, Fight Now]\x01",      # 0
            "[Quit]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB7")

    ChrTalk(
        0x101,
        (
            "#12P#00000FSince we're all set, can\x01",
            "we move there now?\x02\x03",
            "#00004FWe officially accept\x01",
            "your challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PUh uh, now you're talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PAlright then, let's the training begin now!\x02",
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
            "Quest [Taking Part in Bracer Training]\x07\x00",
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
    Jump("loc_CD09")

    label("loc_CBB7")


    ChrTalk(
        0x101,
        (
            "#12P#00000FWe'd like to prepare.\x01",
            "Can you wait for us?\x02",
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
            "#5PAnd if you've got other\x01",
            "business, I don't mind\x01",
            "if it takes priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWe were just looking for a way\x01",
            "to use our free time, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PDon't worry about us, we'll\x01",
            "wait for you here patiently.\x02",
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

    label("loc_CD09")

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

    # Function_38_BDF5 end

    def Function_39_CD61(): pass

    label("Function_39_CD61")

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
            "#5PDo you accept\x01",
            "our challenge?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[All Set, Fight Now]\x01",      # 0
            "[Quit]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFD0")

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, we're all set.\x01",
            "Shall we get going, then?\x02\x03",
            "We officially accept\x01",
            "your challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PUh uh, now you're talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PAlright then, let's the training begin now!\x02",
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
            "Quest [Taking Part in Bracer Training]\x07\x00",
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
    Jump("loc_D0AB")

    label("loc_CFD0")


    ChrTalk(
        0x101,
        (
            "#12P#00006FSorry... It seems we'll need\x01",
            "a little more time.\x02",
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
            "#5PWell, if you've got other business, \x01",
            "that takes precedence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PDon't worry\x01",
            "about us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D0AB")

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

    # Function_39_CD61 end

    def Function_40_D100(): pass

    label("Function_40_D100")

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
            "Hey, it's the Support Section.\x01",
            "Welcome to "Ash Tree".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Want to eat something\x01",
            "today? Or rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, we came here\x01",
            "for work today...\x02",
        )
    )

    CloseMessageWindow()
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
        0xA,
        (
            "Ah, so it's about that.\x01",
            "I heard about it from the\x01",
            "Crossbell News Service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright then, allow\x01",
            "me to treat you to my\x01",
            "Chef's Omelet Rice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, if you please, Master.\x02",
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
            "Lloyd and the others ate the Chef's Omelet Rice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00104F*chomp chomp*... \x01",
            "Hmm, this omelet rice\x01",
            "sure is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes. I think it is superb.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe chicken, rice and ketchup\x01",
            "flavors wrapped in fluffy egg\x01",
            "is somehow simple and good.\x02\x03",
            "#00004FAnd I think Armorica Village\x01",
            "is in a nice location,\x01",
            "surrounded by mother nature...\x02\x03",
            "#00009FI don't think anyone should leave\x01",
            "Armorica without having this first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha, I'm embarrassed you'd\x01",
            "say that much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHa ha. It looks like you're partial\x01",
            "to this omelet rice, Mr. Lloyd...\x02\x03",
            "I think we can leave writing\x01",
            "the guide article to you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00306FWell, it's also got the Master's personality.\x01",
            "We can recommend it wholeheartedly.\x02\x03",
            "#00300FWe also ate this other times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'll be responsible\x01",
            "for writing this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha ha, by all means, please\x01",
            "make an article that will\x01",
            "drive business for us.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_DA6E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_DA8B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_DA9E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DA9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_DAB1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_DACE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_DAE1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_DAFE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DAFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_DB11")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_DB2E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_DB41")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_DB5E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DB5E")

    OP_29(0x80, 0x1, 0x7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC86")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DC7D")

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

    label("loc_DC7D")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_DC86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD6A")
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

    label("loc_DD6A")

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

    # Function_40_D100 end

    def Function_41_DDA4(): pass

    label("Function_41_DDA4")

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
            "#00000FExcuse me, I'd like to ask\x01",
            "you a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner who has\x01",
            "been visiting the village recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Oh, the guy who's been staying\x01",
            "here off and on lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, he was very\x01",
            "polite and pleasant.\x02",
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
            "#00105FThat's right...\x01",
            "Do you happen to\x01",
            "know his name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Umm... "Minneth",\x01",
            "I think it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least that's how he signed\x01",
            "his name in our guest register.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F"Minneth", huh...\x01",
            "Hu hu, at least we\x01",
            "have his name now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FAnd, do you know anything\x01",
            "about this Mr. Minneth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, well he didn't really talk much.\x01",
            "I can't really tell you anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although, he called Derrick to his room and\x01",
            "they talked. This happened several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That's all I can tell you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Those must be the secret talks\x01",
            "with the Village Chief's son...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah... Anyway,\x01",
            "we got some\x01",
            "good info.)\x02\x03",
            "#00000FThank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No problem. It was my pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Incidentally, since you're here, it would\x01",
            "make me happy if you ordered something.\x02",
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

    # Function_41_DDA4 end

    def Function_42_E2FF(): pass

    label("Function_42_E2FF")

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
            "#00000FExcuse me, I'd like to ask\x01",
            "you a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner who has\x01",
            "been visiting the village recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, him. \x01",
            "He's quite perceptive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F...What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that he's taken\x01",
            "quite a liking to our honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""I'll widespread this across the\x01",
            "entire continent for sure!"...\x01",
            "That's what he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FWidespread... ?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FFrom the way he said it... \x01",
            "I guess he's some kind of trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I didn't ask him the details,\x01",
            "but it seems that he his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With such a discerning eye, he's\x01",
            "surely made a name for himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, I'd like my grandson\x01",
            "to follow his example.\x02",
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
            "#00303FAnyway, he seemed like\x01",
            "a skilled trader, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see...\x01",
            "We came to know a lot.\x02\x03",
            "#00004FThank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hm, come again anytime.\x02",
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

    # Function_42_E2FF end

    def Function_43_E761(): pass

    label("Function_43_E761")

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
        "We've got rooms free, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(That's right, if Mr.\x01",
            "Geval really did come\x01",
            "to Armorica Village...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(It is likely he\x01",
            "came to the inn.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUm, can we ask\x01",
            "you something...?\x02\x03",
            "Is there a man by the name\x01",
            "of Geval staying here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, Mr. Geval, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's been coming here to\x01",
            "eat every so often lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FJust to eat...?\x02\x03",
            "He's not staying\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, he isn't. I don't\x01",
            "remember checking him in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He likes our food, so\x01",
            "I thought he was coming\x01",
            "here from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm... I don't\x01",
            "think that's what's\x01",
            "goin' on here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FCould he have a\x01",
            "relative here\x01",
            "in Armorica?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIf that was the case,\x01",
            "Alm and Aerie would know\x01",
            "where he is immediately...\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_END)), "loc_EBCD")

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
            "#00001F...Let's try speaking with the Village\x01",
            "Chief. He may know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_EC40")

    label("loc_EBCD")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#00003FFor now, let's have a look around.\x02\x03",
            "#00000FIt's possible\x01",
            "he's in a good\x01",
            "hiding place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC40")

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

    # Function_43_E761 end

    def Function_44_EC9A(): pass

    label("Function_44_EC9A")

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
            "#11POh, it's you guys...\x01",
            "The police's um... Special\x01",
            "Support Section, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PThanks for all your help back then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_EEF7")

    ChrTalk(
        0xD,
        (
            "#5PYeah, I remember when you saved those\x01",
            "tourists at the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PAnd now that I think about it,\x01",
            "I caused you some trouble\x01",
            "due to a library book...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, don't\x01",
            "worry about it.\x02\x03",
            "#00000FHas there been any\x01",
            "strange incidents recently?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFA4")

    label("loc_EEF7")


    ChrTalk(
        0xD,
        (
            "#5PYeah, I remember when you saved those\x01",
            "tourists at the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, it has been a long time.\x02\x03",
            "Has there been any\x01",
            "strange incidents recently?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFA4")


    ChrTalk(
        0xA,
        (
            "#11PHmm, this village has\x01",
            "been pretty peaceful\x01",
            "lately, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI'm compelled to say though, there\x01",
            "have been some unfamiliar faces\x01",
            "visiting this village recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PYeah, that giant red-haired man and his pals...\x02",
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
            "#6P#00301F...By any chance,\x01",
            "was his hair color\x01",
            "the same as mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh, now that you mention it,\x01",
            "it's pretty similar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThat giant red-haired guy, he had\x01",
            "with him a lively young girl who\x01",
            "also had the same shade of hair.\x02",
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
            "#00001F...Uhmm, if possible, do you have any\x01",
            "specific details about why they were\x01",
            "here... Or what they were doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PSorry to tell you but, I wasn't\x01",
            "really keeping an eye on them.\x02",
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
            "...Now that you mention it, I did see them\x01",
            "purchase some goods at the general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For some reason, they were buying large\x01",
            "quantities of cheese, bacon, and bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Old man Reoir was pretty happy about\x01",
            "making such a big profit that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIs that so...?\x02",
    )

    CloseMessageWindow()

    def lambda_F46F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F46F)
    Sleep(50)

    def lambda_F47F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F47F)
    Sleep(50)

    def lambda_F48F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F48F)
    Sleep(50)
    OP_93(0x109, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00001F...... So the "Red Constellation" came\x01",
            "to visit Armorica Village, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAll we know now is that they came\x01",
            "to stock up on food supplies.\x02\x03",
            "#10103FAnd they seemed to have only purchased\x01",
            "the cheap, cost-effective foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...For jaeger corps, the ability to\x01",
            "maintain a healthy supply of food is\x01",
            "one of our most fundamental skills.\x02\x03",
            "A battle could break out at any time,\x01",
            "so we have to always be prepared.\x02\x03",
            "#00301FAnd since those guys are veteran\x01",
            "jaegers, they've probably already\x01",
            "mapped out this entire area as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHu hu, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut is that really\x01",
            "why they were here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F...... For now, let's\x01",
            "just make a mental note\x01",
            "of this and move on.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F77A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F77A)
    Sleep(50)

    def lambda_F78A():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F78A)
    Sleep(50)

    def lambda_F79A():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F79A)
    Sleep(50)

    def lambda_F7AA():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F7AA)
    Sleep(50)

    def lambda_F7BA():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F7BA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00004F...Thank yoy very much for \x01",
            "your valuable information.\x02\x03",
            "#00000FPlease contact us \x01",
            "if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHm, not sure what's going on exactly,\x01",
            "but you guys seem pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell, stop by again whenever you want\x01",
            "and I'll be sure to prepare some\x01",
            "delicious omelet rice for you, okay?\x02",
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

    # Function_44_EC9A end

    def Function_45_F95A(): pass

    label("Function_45_F95A")

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
        "Wow, that's a big doggy!\x02",
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

    def lambda_FC29():
        OP_93(0x15, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_FC29)
    Sleep(50)

    def lambda_FC39():
        OP_93(0x16, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_FC39)
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
        "Everyone...!\x02",
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
            "Oh... Mr. Lloyd!\x02\x03",
            "Thank goodness...\x01",
            "You're safe!\x02",
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
            "#00002F#12PIt's been awhile,\x01",
            "Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#12P#3C..."Big doggy"...\x01",
            "Could he be referring to myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PUh uh, I think it is a nice naming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10409F#12PAhaha, even a Divine Wolf can be cute.\x02",
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
            "#03600FI heard that you are a\x01",
            "wanted escapee, but...\x01",
            "I'm glad you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha... \x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03708F#11PUmm, what happened to the\x01",
            "other Support Section members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Unfortunately,\x01",
            "we got separated.\x02\x03",
            "#00208FWe don't even know\x01",
            "where they are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#03710F#11PI see... That's worrying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PIt seems like you and your\x01",
            "family were visiting right\x01",
            "when the accident occurred?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYes... \x01",
            "We didn't have the slightest\x01",
            "idea about what was going on.\x02\x03",
            "#03608FThen, highway movement\x01",
            "restrictions were put in place and\x01",
            "we couldn't get back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700F#11PBut, we're very grateful\x01",
            "to the villagers.\x02\x03",
            "The innkeeper said we could stay\x01",
            "until the situation dies down.\x02\x03",
            "#03709FAnd it looks like Colin has made friends\x01",
            "with the children of the village, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#03809F#5PCamille and Pooley\x01",
            "play with me a lot!\x02\x03",
            "Play with us too next time, doggy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#6P#3CHu hu, I shall consider it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609F#11PHa ha...thank you very much.\x02\x03",
            "#03600FAnd so, to repay the\x01",
            "villagers, I have been\x01",
            "helping them out.\x02\x03",
            "#03604FAlthough, I'm only responsible\x01",
            "for negotiating with the\x01",
            "periodic State Guard patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PNo, that is an important role,\x01",
            "given the situation.\x02\x03",
            "#00202FWith a veteran trader like you,\x01",
            "Mr. Harold, those negotiations\x01",
            "will probably go smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600F#11PHa ha. It's really\x01",
            "no big deal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x15)

    ChrTalk(
        0x15,
        (
            "#03605F#11POh, but I heard something interesting during\x01",
            "my discussions with the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PSomething interesting...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYes. They said an\x01",
            "unknown rebel force is\x01",
            "lurking in this area.\x02\x03",
            "#03601FThey said it has attacked State\x01",
            "Guard units several times.\x02",
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
            "#10402F#6PWow... I can't believe there could be\x01",
            "anyone like that, given the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PWe don't know who they're, but... \x01",
            "I think it is good intelligence all the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, we should look into it.\x02\x03",
            "#00001FMr. Harold, do you know of any\x01",
            "sightings of the rebel force?\x02",
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
            "during a regular patrol, but...\x01",
            "I didn't hear the outcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CThe Armorica Ancient Battlefield... A cursed\x01",
            "place where blood was spilled countless times,\x01",
            "and where the Cult built its stronghold.\x02\x03",
            "#01201FThere are many hidden passages within\x01",
            "those ruins. If the rebel force is hiding,\x01",
            "that would be a suitable location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PWe don't know what's waiting for us out there...\x01",
            "Let's make sure our gear is in order before we go.\x02",
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

    # Function_45_F95A end

    def Function_46_10AB6(): pass

    label("Function_46_10AB6")


    def lambda_10ABB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10ABB)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 73000, 0, -500, 2000, 0x0)
    Return()

    # Function_46_10AB6 end

    def Function_47_10AFF(): pass

    label("Function_47_10AFF")


    def lambda_10B04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10B04)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -1000, 2000, 0x0)
    OP_95(0xFE, 73750, 0, -1000, 2000, 0x0)
    Return()

    # Function_47_10AFF end

    def Function_48_10B48(): pass

    label("Function_48_10B48")


    def lambda_10B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10B4D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 75000, 0, -500, 2000, 0x0)
    Return()

    # Function_48_10B48 end

    def Function_49_10B91(): pass

    label("Function_49_10B91")


    def lambda_10B96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10B96)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
    OP_95(0xFE, 74250, 0, 0, 2000, 0x0)
    Return()

    # Function_49_10B91 end

    SaveToFile()

Try(main)
