from ScenarioHelper import *

def main():
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
        "Role old man",           # 1
        "Jake",               # 2
        "Gofan",             # 3
        "Cry",               # 4
        "Keith",                 # 5
        "Alfred",           # 6
        "Aretha",                 # 7
        "Camille",               # 8
        "pulley",               # 9
        "Stephane",             # 10
        "Derrick",               # 11
        "Angers",               # 12
        "Sister Hatina",     # 13
        "Harold",               # 14
        "Sofia",               # 15
        "Choline",                 # 16
        "Father Kevin",             # 17
        "Sister · Lease",       # 18
        "Zookoist Rin",             # 19
        "Friend Aolia",         # 20
        "Mushroute Scott",         # 21
        "Chiluru",                 # 22
        "cuisine",                   # 23
        "cuisine",                   # 24
        "cuisine",                   # 25
        "cuisine",                   # 26
        "cuisine",                   # 27
        "cuisine",                   # 28
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
        "Function_7_C50",          # 07, 7
        "Function_8_D4C",          # 08, 8
        "Function_9_1DBD",         # 09, 9
        "Function_10_1DC1",        # 0A, 10
        "Function_11_2C66",        # 0B, 11
        "Function_12_2C6A",        # 0C, 12
        "Function_13_3F1E",        # 0D, 13
        "Function_14_4C68",        # 0E, 14
        "Function_15_4D9A",        # 0F, 15
        "Function_16_5A78",        # 10, 16
        "Function_17_6C7D",        # 11, 17
        "Function_18_76BD",        # 12, 18
        "Function_19_7749",        # 13, 19
        "Function_20_77BF",        # 14, 20
        "Function_21_7A36",        # 15, 21
        "Function_22_7F2A",        # 16, 22
        "Function_23_7FC9",        # 17, 23
        "Function_24_80E7",        # 18, 24
        "Function_25_8207",        # 19, 25
        "Function_26_8F28",        # 1A, 26
        "Function_27_90D5",        # 1B, 27
        "Function_28_910F",        # 1C, 28
        "Function_29_9149",        # 1D, 29
        "Function_30_9369",        # 1E, 30
        "Function_31_973D",        # 1F, 31
        "Function_32_9C6A",        # 20, 32
        "Function_33_9E2A",        # 21, 33
        "Function_34_9FD1",        # 22, 34
        "Function_35_A096",        # 23, 35
        "Function_36_AF10",        # 24, 36
        "Function_37_B01C",        # 25, 37
        "Function_38_B1C4",        # 26, 38
        "Function_39_C036",        # 27, 39
        "Function_40_C406",        # 28, 40
        "Function_41_D002",        # 29, 41
        "Function_42_D514",        # 2A, 42
        "Function_43_D941",        # 2B, 43
        "Function_44_DE9F",        # 2C, 44
        "Function_45_E9A2",        # 2D, 45
        "Function_46_FA0E",        # 2E, 46
        "Function_47_FA57",        # 2F, 47
        "Function_48_FAA0",        # 30, 48
        "Function_49_FAE9",        # 31, 49
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
            "There is a car magazine \"Drifting Car Freak vol.2\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('轻快色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Pop color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('轻快色彩', 1)

    label("loc_C4C")

    TalkEnd(0xFF)
    Return()

    # Function_6_BA8 end

    def Function_7_C50(): pass

    label("Function_7_C50")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★トネリコ亭・おすすめcuisine★\x01",
            "~ Takumi Omu Rice ~\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The recipe of Takumi style omelette is written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_D48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Takumi style omelette\"\x07\x00",
            "のレシピI learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D48")

    TalkEnd(0xFF)
    Return()

    # Function_7_C50 end

    def Function_8_D4C(): pass

    label("Function_8_D4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7B")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E83")

    ChrTalk(
        0x8,
        (
            "A big tree of an object appears,\x01",
            "Jakeが萎縮してしまわんか\x01",
            "I was worried … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haroldくんの一言で\x01",
            "On the contrary it seems to have demonstrated motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The most important commercial spirit for merchants …\x01",
            "それが芽生えたJakeは\x01",
            "I'm sure I'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F15")

    label("loc_E83")


    ChrTalk(
        0x8,
        (
            "The most important commercial spirit for merchants …\x01",
            "Jakeにもそれが芽生えおった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter what the crossbell will be like this time,\x01",
            "There is nothing to remember on a scoop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F15")

    Jump("loc_1DB9")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101A")

    ChrTalk(
        0x8,
        (
            "Haroldくんは、Sofia殿や\x01",
            "Cholineくんという家族の存在に\x01",
            "It seems to be supported firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ふむ、Jakeにもそのような\x01",
            "Or if there exists …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once retired, in earnest\x01",
            "It is also to search grandchild's bride\x01",
            "It may not be bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_108D")

    label("loc_101A")


    ChrTalk(
        0x8,
        (
            "ふむ、Jakeにも\x01",
            "We support both public and private\x01",
            "If a bride is found ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is also to search grandchild's bride\x01",
            "It may not be bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108D")

    Jump("loc_1DB9")

    label("loc_1092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(
        0x8,
        (
            "Haroldくんは、\x01",
            "Regarding supply of supplies from the Defense Army\x01",
            "We are negotiating a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How much self-sufficiency is established\x01",
            "With this village, medicines etc.\x01",
            "It's getting pretty much necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jakeのやつも、あれくらい\x01",
            "I wish it would be possible ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1252")

    label("loc_11A6")


    ChrTalk(
        0x8,
        (
            "Jakeのやつも、\x01",
            "Haroldくん位の商人に\x01",
            "I wish it would be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… I do not know recently\x01",
            "You are motivating people.\x01",
            "Do not say too few words.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1252")

    Jump("loc_1DB9")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1354")

    ChrTalk(
        0x8,
        (
            "少し前から、Jakeが\x01",
            "Just as people have changed\x01",
            "It is for the first time to motivate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is still immature,\x01",
            "I can finally be relieved\x01",
            "That's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いつか《Jake雑貨店》の\x01",
            "To put up a signboard,\x01",
            "I have to tell you again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FA")

    label("loc_1354")


    ChrTalk(
        0x8,
        (
            "Jakeがようやく\x01",
            "It motivated me.\x01",
            "わしも安心できるThat's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いつか《Jake雑貨店》の\x01",
            "To put up a signboard,\x01",
            "I have to tell you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1DB9")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(
        0x8,
        (
            "Kosi hurt yesterday\x01",
            "It is still bad.\x01",
            "I am also years old …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, even so\x01",
            "Jakeの奴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today somehow and always\x01",
            "Looks like the situation is different.\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1525")

    label("loc_14C9")


    ChrTalk(
        0x8,
        (
            "Jakeの奴……\x01",
            "Today somehow and always\x01",
            "Looks like the situation is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Did something happen?\x02",
    )

    CloseMessageWindow()

    label("loc_1525")

    Jump("loc_1DB9")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1739")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D3")

    ChrTalk(
        0x8,
        (
            "Apparently today,\x01",
            "Minneshu makes the last negotiation\x01",
            "She seems to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いよいよDerrickとの計画が\x01",
            "To start it.\x01",
            "No, it is fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1734")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A8")

    ChrTalk(
        0x8,
        (
            "When I looked outside the window,\x01",
            "There are monsters in the plaza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Moreover, as long as you see the situation,\x01",
            "That Minneshita handles it\x01",
            "It seems like you did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the surprised rhythm,\x01",
            "I'm sorry to hurt Koshi.\x01",
            "Warmth ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1734")

    label("loc_16A8")


    ChrTalk(
        0x8,
        (
            "The monsters that appeared in the plaza,\x01",
            "That Minneshita handles it\x01",
            "It seems like you did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the surprised rhythm,\x01",
            "I'm sorry to hurt Koshi.\x01",
            "Warmth ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1734")

    Jump("loc_1DB9")

    label("loc_1739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B9")

    ChrTalk(
        0x8,
        (
            "最近、Haroldくんに次いで\x01",
            "I met a prospective man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Cuddly, doing a lot and well\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183C")

    label("loc_17B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C8")
    Jump("loc_183C")

    label("loc_17C8")


    ChrTalk(
        0x8,
        (
            "That man,\x01",
            "Very village honey very much\x01",
            "You liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, Well,\x01",
            "To a nice merchant\x01",
            "Not the difference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183C")

    Jump("loc_1DB9")

    label("loc_1841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_199D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(
        0x8,
        (
            "I retied soon,\x01",
            "店をJakeに任せたいが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Appreciably\x01",
            "You will be motivated.\x01",
            "I am always in danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, even if it's some opportunity\x01",
            "I wish I had it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1998")

    label("loc_1916")


    ChrTalk(
        0x8,
        (
            "Jakeの奴は、\x01",
            "I feel like I truly follow the shop\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something motivated\x01",
            "As long as it's a chance\x01",
            "Does not sound okay … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    Jump("loc_1DB9")

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A70")

    ChrTalk(
        0x8,
        (
            "Recently, Koshi is bad.\x01",
            "I am too old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nevertheless, in the near future\x01",
            "Jakeに店を任せて\x01",
            "I would like to retire … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How can this grandson\x01",
            "I will motivate you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AEF")

    label("loc_1A70")


    ChrTalk(
        0x8,
        (
            "I am too old, soon\x01",
            "Jakeに店を任せて\x01",
            "I would like to retire … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not feel motivated by himself.\x01",
            "It is a tough trip.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEF")

    Jump("loc_1DB9")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_1CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    ChrTalk(
        0x8,
        (
            "A strict man with red hair …\x01",
            "Ooooo, indeed recently\x01",
            "Such a man came with a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was a staggering variety of people,\x01",
            "He bought a lot of my items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jakeのやつは怯えておったが、\x01",
            "He is a superior of Hisabisa.\x01",
            "Ho Ho Ho …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CA5")

    label("loc_1C01")


    ChrTalk(
        0x8,
        (
            "A strict man with red hair,\x01",
            "He is a superior of Hisabisa.\x01",
            "Ho Ho Ho …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jakeのやつは怯えておったが、\x01",
            "Do not judge customers by appearance.\x01",
            "There are still a few treats.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA5")

    Jump("loc_1DB9")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D59")

    ChrTalk(
        0x8,
        (
            "先ほど、Haroldくんが\x01",
            "I came to deal with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, he is\x01",
            "It is a promising merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jakeのやつに\x01",
            "I want to make drink by decoiling nails.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB9")

    label("loc_1D59")


    ChrTalk(
        0x8,
        (
            "Haroldくんは\x01",
            "It is a promising merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jakeのやつに\x01",
            "I want to make drink by decoiling nails.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB9")

    TalkEnd(0xFE)
    Return()

    # Function_8_D4C end

    def Function_9_1DBD(): pass

    label("Function_9_1DBD")

    Call(0, 10)
    Return()

    # Function_9_1DBD end

    def Function_10_1DC1(): pass

    label("Function_10_1DC1")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C62")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E4B")
    OP_AF(0x4F)
    Jump("loc_1E7D")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E5B")
    OP_AF(0x4E)
    Jump("loc_1E7D")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E6B")
    OP_AF(0x4D)
    Jump("loc_1E7D")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E7B")
    OP_AF(0x4C)
    Jump("loc_1E7D")

    label("loc_1E7B")

    OP_AF(0x4B)

    label("loc_1E7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C5D")

    label("loc_1E8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA0")
    Jump("loc_2C5D")

    label("loc_1EA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB8")
    TalkEnd(0x9)
    Return()

    label("loc_1EB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC9")

    ChrTalk(
        0x9,
        (
            "Haroldさんが帰り際に、\x01",
            "You gave me advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "\"At such times, for everyone\x01",
            "It is our mission to do our best in business. \"\x01",
            "… ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By doing business with me\x01",
            "If someone's help,\x01",
            "I have to try it with the feeling of dying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2031")

    label("loc_1FC9")


    ChrTalk(
        0x9,
        (
            "By doing business with me\x01",
            "If someone's help,\x01",
            "I have to try it with the feeling of dying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Alright …… Yurts! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_2031")

    Jump("loc_2C5D")

    label("loc_2036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(
        0x9,
        (
            "Something like Grandpa\x01",
            "I feel like I'm planning a disturbing thing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is such a time, and the harvest of agricultural crops\x01",
            "Worry about being depressed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5D")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_223D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(
        0x9,
        (
            "この間、Haroldさんが\x01",
            "Looking at negotiating with Defense Forces,\x01",
            "I thought it was still too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I intended to succeed the store,\x01",
            "Ah, that's true.\x01",
            "I wish I could not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "折角だし、Haroldさんに\x01",
            "I would like to receive advice ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2238")

    label("loc_21C6")


    ChrTalk(
        0x9,
        (
            "What he wants to say is\x01",
            "You can understand roughly if you look at the face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "俺もHaroldさんみたいな\x01",
            "You must be a fine merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2238")

    Jump("loc_2C5D")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")

    ChrTalk(
        0x9,
        (
            "Welcome party,\x01",
            "Welcome to \"Role General Store\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Recommendation is honey of special products.\x01",
            "Please take a look there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2330")

    label("loc_22CC")


    ChrTalk(
        0x9,
        (
            "…. How are you, pretty?\x01",
            "It's becoming a summer, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To, in earnest to succeed the store\x01",
            "Let 's think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2330")

    Jump("loc_2C5D")

    label("loc_2335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2416")

    ChrTalk(
        0x9,
        (
            "Yesterday my grandfather\x01",
            "I was hurting my back.\x01",
            "I wish I could take a day off ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But maybe I will not depend on it\x01",
            "I wonder if I do not go to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Ha, what are you doing me, okay?\x01",
            "I have to do my best more …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24AB")

    label("loc_2416")


    ChrTalk(
        0x9,
        (
            "To inherit a general store,\x01",
            "I do not care much,\x01",
            "I was not motivated, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order not to worry about Grandpa,\x01",
            "Let 's try harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AB")

    Jump("loc_2C5D")

    label("loc_24B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255D")

    ChrTalk(
        0x9,
        (
            "I am referring to Armorica's reform\x01",
            "It seems that there is a talk ….\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Besides, as usual,\x01",
            "I do not mind it.\x01",
            "It is easy and fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D0")

    label("loc_255D")


    ChrTalk(
        0x9,
        (
            "Grandpa,\x01",
            "My back seemed to have been pain for a little while ago\x01",
            "Is it alright……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, that's it. Put a poultice from the back\x01",
            "Bring me and ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D0")

    Jump("loc_2C5D")

    label("loc_25D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C0")

    ChrTalk(
        0x9,
        (
            "I often see it in the village recently\x01",
            "I have a good person … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, Grandpa, that person\x01",
            "\"Have a nice-made grandchild\" or\x01",
            "It seems they are pleased to be told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… As flattering as a flattery\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272B")

    label("loc_26C0")


    ChrTalk(
        0x9,
        (
            "Grandpa,\x01",
            "Praised me\x01",
            "It seems they are pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… As flattering as a flattery\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272B")

    Jump("loc_2C5D")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2805")

    ChrTalk(
        0x9,
        (
            "It is almost time for Grandpa\x01",
            "\"I do not mean to take over the store\"\x01",
            "I have to say clearly, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "でも、言うとGrandpa,\x01",
            "I wonder I'm disappointed …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……whatever,\x01",
            "As it is for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2886")

    label("loc_2805")


    ChrTalk(
        0x9,
        (
            "I get salary, I am not busy … …\x01",
            "If you think it is a part-time job\x01",
            "It is nice to have breakfast at sundry shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……whatever,\x01",
            "As it is for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2886")

    Jump("loc_2C5D")

    label("loc_288B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2927")

    ChrTalk(
        0x9,
        (
            "Grandpa to me\x01",
            "It seems I'm going to take over the store … …\x01",
            "To be honest, it is troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future go out into town,\x01",
            "I want to hit a mountain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_297C")

    label("loc_2927")


    ChrTalk(
        0x9,
        "I'm honest I am sorry to succeed the store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future go out into town,\x01",
            "I want to hit a mountain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_297C")

    Jump("loc_2C5D")

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_END)), "loc_2B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A78")

    ChrTalk(
        0x9,
        (
            "A redhead giant ……?\x01",
            "Well, a while ago\x01",
            "I guess such a man came with a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He told me he was profitable.\x01",
            "I was pleased, but …\x01",
            "I was scared somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They are absolutely not a formal thing.\x01",
            "There is no difference in planning something ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AFF")

    label("loc_2A78")


    ChrTalk(
        0x9,
        (
            "A redhead giant ……\x01",
            "It is not an absolute form,\x01",
            "I was scared somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… But the redhead girl who was with me\x01",
            "I was a little cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFF")

    Jump("loc_2C5D")

    label("loc_2B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD5")

    ChrTalk(
        0x9,
        (
            "Welcome, thank you.\x01",
            "Take me as you like … … Kudasai.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also the honey which is a special product of the village\x01",
            "I'm caught up here … Masuyo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Well, polite wording\x01",
            "After all it was a bit hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C5D")

    label("loc_2BD5")


    ChrTalk(
        0x9,
        (
            "My grandfather, put it on something\x01",
            "Haroldさんを見習えって言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With such a veteran merchant\x01",
            "Even when compared, the honest load is heavy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5D")

    Jump("loc_1DCE")

    label("loc_2C62")

    TalkEnd(0x9)
    Return()

    # Function_10_1DC1 end

    def Function_11_2C66(): pass

    label("Function_11_2C66")

    Call(0, 12)
    Return()

    # Function_11_2C66 end

    def Function_12_2C6A(): pass

    label("Function_12_2C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB3")
    Call(0, 40)
    Return()

    label("loc_2CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CE1")
    Call(0, 41)
    Return()

    label("loc_2CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D0F")
    Call(0, 43)
    Return()

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D26")
    Call(0, 44)
    Return()

    label("loc_2D26")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DA6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2DA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC6")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F15")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE6")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F15")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFA")
    Jump("loc_3F15")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E12")
    TalkEnd(0xA)
    Return()

    label("loc_2E12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F15")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_2EB8")

    ChrTalk(
        0xA,
        (
            "When it is acclaimed to that extent\x01",
            "I wonder why I'm embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hello, everyone\x01",
            "An article that will thrive\x01",
            "I have asked for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F15")

    label("loc_2EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_306B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE1")

    ChrTalk(
        0xA,
        (
            "To the appearance of that pale huge tree\x01",
            "It was pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a ridiculous situation ….\x01",
            "In such a case,\x01",
            "It is also important to take a break once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I just got tired of myself a while ago\x01",
            "Father and sister have\x01",
            "I just came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Later for them, even coffee\x01",
            "I have to take it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3066")

    label("loc_2FE1")


    ChrTalk(
        0xA,
        (
            "About a while ago, I was exhausted\x01",
            "Father and sister have\x01",
            "I just came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Later for them, even coffee\x01",
            "I have to take it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3066")

    Jump("loc_3F15")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_31F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3172")

    ChrTalk(
        0xA,
        (
            "Rumors of the invalid declaration of the example,\x01",
            "This village has arrived too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Originally to the president in the village\x01",
            "I did not have a good impression … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "People in town as well as trekking this time,\x01",
            "I wonder if you felt doubtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What will be the future development …\x01",
            "Personally I can not keep an eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31F2")

    label("loc_3172")


    ChrTalk(
        0xA,
        (
            "People in town as well as President\x01",
            "I guess they felt doubtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What will be the future development …\x01",
            "Personally I can not keep an eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F2")

    Jump("loc_3F15")

    label("loc_31F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_33B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3307")

    ChrTalk(
        0xA,
        (
            "Harold君とご家族は、\x01",
            "I'm staying in the big room on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, in this situation Crossbell\x01",
            "A new customer will not come.\x01",
            "When you are in trouble, you are mutually exclusive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I also help a lot with the village,\x01",
            "I just lent a room\x01",
            "I'm sorry but.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33AD")

    label("loc_3307")


    ChrTalk(
        0xA,
        (
            "それにしても、Harold君も\x01",
            "Although it is a pleasant vacation,\x01",
            "I was lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a big help as a village ….\x01",
            "I can not go back to the city\x01",
            "I guess it is quite uneasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AD")

    Jump("loc_3F15")

    label("loc_33B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3599")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3468")

    ChrTalk(
        0xA,
        (
            "Mr. Gebal likes my taste\x01",
            "I was going from the city\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "…… Where are you staying now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3594")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352C")

    ChrTalk(
        0xA,
        (
            "In the meantime,\x01",
            "Crossbell Autonomous state as a whole\x01",
            "It is a matter of shaking peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tension of the border is also\x01",
            "It is said that it is strengthening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell is united,\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3594")

    label("loc_352C")


    ChrTalk(
        0xA,
        (
            "Tension of the border is also\x01",
            "It is said that it is strengthening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell is united,\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3594")

    Jump("loc_3F15")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365E")

    ChrTalk(
        0xA,
        (
            "Today for Sunday school,\x01",
            "I am renting a large room on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, for the children\x01",
            "Even with a snack of pudding\x01",
            "I might as well make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oops, of course\x01",
            "Sister's minutes too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36D1")

    label("loc_365E")


    ChrTalk(
        0xA,
        (
            "Today in the big room on the second floor\x01",
            "I am doing Sunday school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For everyone,\x01",
            "Even with a snack of pudding\x01",
            "I might as well make it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D1")

    Jump("loc_3F15")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377A")

    ChrTalk(
        0xA,
        (
            "Derrick君に、ここ最近\x01",
            "What was doing away from the mayor?\x01",
            "I could listen to it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But I wonder if it's okay.\x01",
            "It's a new business …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E7")

    label("loc_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3860")

    ChrTalk(
        0xA,
        (
            "No way, Mr. Minnes\x01",
            "He said he was a con artist … …\x01",
            "I did not notice at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sissame, deceive others\x01",
            "Should I call it a professional?\x01",
            "It's a horrible man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems to be wanted,\x01",
            "As soon as you are arrested\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38E7")

    label("loc_3860")


    ChrTalk(
        0xA,
        (
            "ともあれ、Derrick君が\x01",
            "It was nice to have reconciled with the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In that sense,\x01",
            "This incident was a good start\x01",
            "Maybe it has become.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E7")

    Jump("loc_3F15")

    label("loc_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3971")

    ChrTalk(
        0xA,
        (
            "ふう、Derrick君は\x01",
            "When will you come\x01",
            "I wonder if I am going home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As soon as the village head\x01",
            "I would like you to reconcile ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A09")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3980")
    Jump("loc_3A09")

    label("loc_3980")


    ChrTalk(
        0xA,
        (
            "I am with Mr. Minnes,\x01",
            "There is not much contact with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "なにやら最近Derrick君と\x01",
            "Although it seems to be meeting well … …\x01",
            "What kind of story are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADF")

    ChrTalk(
        0x101,
        (
            "#00003F(by the way,\x01",
            "Gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00001F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADF")

    Jump("loc_3F15")

    label("loc_3AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3F")
    SetChrSubChip(0x12, 0x1)
    TurnDirection(0xA, 0x12, 0)

    ChrTalk(
        0xA,
        (
            "Derrick君……\x01",
            "Even the mayor mayor\x01",
            "I mean denying you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "No, my father surely ……\x01",
            "My idea itself\x01",
            "I do not like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Otherwise,\x01",
            "The current situation of the village\x01",
            "There is no way I can keep silent …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… I know that it is difficult in various ways.\x01",
            "But sometimes I drink coffee,\x01",
            "It is important to calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    TurnDirection(0xA, 0x0, 0)
    SetChrSubChip(0x12, 0x0)
    Jump("loc_3CE1")

    label("loc_3C3F")


    ChrTalk(
        0xA,
        (
            "Derrick君も、\x01",
            "It is like a villageman who has a strong sense of responsibility.\x01",
            "There seems to be many things to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I came all the way,\x01",
            "Even with a cup of blend\x01",
            "I'd like to serve you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE1")

    Jump("loc_3F15")

    label("loc_3CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE8")

    ChrTalk(
        0xA,
        (
            "The leaders of each country\x01",
            "Gather in the crossbell …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This is also in the history of Crossbell\x01",
            "Unprecedented, it is hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I advocated Cross Bell City\x01",
            "I mean that it is a new mayor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, as expected\x01",
            "There is only IBC's top,\x01",
            "You will have a bold idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E60")

    label("loc_3DE8")


    ChrTalk(
        0xA,
        (
            "Western Zemria Trade Council ……\x01",
            "It is finally beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that the interests of neighboring countries are also high,\x01",
            "I am also interested in trends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_3F15")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")
    Jump("loc_3F15")

    label("loc_3E7D")


    ChrTalk(
        0xA,
        (
            "The redhead giants,\x01",
            "Especially the suspicious thing in the village\x01",
            "It seems I did not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "People who are likely to have arms\x01",
            "It seems they were all together ….\x01",
            "I wonder who they are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F15")

    Jump("loc_2D33")

    label("loc_3F1A")

    TalkEnd(0xA)
    Return()

    # Function_12_2C6A end

    def Function_13_3F1E(): pass

    label("Function_13_3F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFC")

    ChrTalk(
        0xB,
        (
            "あたし、Keith君のことは\x01",
            "I did not care about it though … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, with that\x01",
            "There is a man 's feeling.\x01",
            "Somehow I have reviewed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although I laughed a little while ago,\x01",
            "I need to apologize later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4081")

    label("loc_3FFC")


    ChrTalk(
        0xB,
        (
            "Keithくんもなかなか\x01",
            "There is a man 's feeling.\x01",
            "Somehow I have reviewed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although I laughed a little while ago,\x01",
            "I need to apologize later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4081")

    Jump("loc_4C64")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_41F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415D")

    ChrTalk(
        0xB,
        (
            "Sofiaさん、とっても\x01",
            "cuisineが上手なのよね〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While staying,\x01",
            "私もおcuisineを習っとこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, better than your father\x01",
            "To make omelet rice\x01",
            "Become it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41F0")

    label("loc_415D")


    ChrTalk(
        0xB,
        (
            "SofiaさんがWhile staying,\x01",
            "おcuisineを習っとこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, better than your father\x01",
            "To make omelet rice\x01",
            "Become it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F0")

    Jump("loc_4C64")

    label("loc_41F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BC")

    ChrTalk(
        0xB,
        (
            "あ〜、Cholineくんは\x01",
            "Really cute I wish ~\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Grinning your eyes,\x01",
            "Very friendly and …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected it is my yearning.\x01",
            "Haroldさんの子供だわ。\x01",
            "The future will be fun! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_432F")

    label("loc_42BC")


    ChrTalk(
        0xB,
        (
            "あ〜、Cholineくんは\x01",
            "Really cute I wish ~\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected it is my yearning.\x01",
            "Haroldさんの子供だわ。\x01",
            "The future will be fun! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432F")

    Jump("loc_4C64")

    label("loc_4334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4409")

    ChrTalk(
        0xB,
        (
            "To Crossbell City\x01",
            "I went when I was at a memorial festival ….\x01",
            "Very beautiful and lovely city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To attack such a place,\x01",
            "Armed group, I will forgive you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To the police and guards,\x01",
            "I want you to catch it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_448C")

    label("loc_4409")


    ChrTalk(
        0xB,
        (
            "To attack the city of Crossbell,\x01",
            "I will forgive the armed group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This time Minneshi and say,\x01",
            "Why is a bad person\x01",
            "I wonder if there is so much ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448C")

    Jump("loc_4C64")

    label("loc_4491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_452F")

    ChrTalk(
        0xB,
        (
            "Haha, on rainy days\x01",
            "It's damp and it's crisp.\x01",
            "It is also hard to clean the floor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At the very least,\x01",
            "From dross at the shop\x01",
            "I want you to come in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C64")

    label("loc_452F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_470A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C1")

    ChrTalk(
        0xB,
        (
            "Today, Mr. Minnes\x01",
            "Derrickさんに大事な話を\x01",
            "It seems to come to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Finally the plan\x01",
            "I wonder if it gets stuck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4705")

    label("loc_45C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4682")

    ChrTalk(
        0xB,
        (
            "That kind of minnes ……\x01",
            "It was a terrible food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhun, I started from the beginning\x01",
            "I thought it was suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I will show you this time\x01",
            "Because I do it all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4705")

    label("loc_4682")


    ChrTalk(
        0xB,
        (
            "That kind of minnes ……\x01",
            "I started from the beginning\x01",
            "I thought it was doubtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I will show you this time\x01",
            "Because I do it all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4705")

    Jump("loc_4C64")

    label("loc_470A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E1")

    ChrTalk(
        0xB,
        (
            "Recently, it looks very gentle\x01",
            "My uncle often comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To a famous foreign company\x01",
            "I heard that I am working,\x01",
            "I do not do that at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, in the world\x01",
            "It is what you can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_486E")

    label("loc_47E1")


    ChrTalk(
        0xB,
        (
            "Recently, it looks very gentle\x01",
            "My uncle often comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am working for a famous company in a foreign country\x01",
            "I do not win at all at all ……\x01",
            "It is what you can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486E")

    Jump("loc_4C64")

    label("loc_4873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488E")
    Call(0, 14)
    Jump("loc_491D")

    label("loc_488E")


    ChrTalk(
        0xB,
        (
            "What is Orkistower?\x01",
            "I'd like to see it, but I do have a shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Make my omelet rice\x01",
            "If you can finish 10 dishes in 1 hour,\x01",
            "You may as well date it, but ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491D")

    Jump("loc_4C64")

    label("loc_4922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B1C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A15")

    ChrTalk(
        0xB,
        (
            "What are the hypocrite men?\x01",
            "It is really strong, is not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Arios only\x01",
            "It tends to attract attention,\x01",
            "That women prime minister is also good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh, of course you also.\x01",
            "Thanks to you I had a good time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AB0")

    label("loc_4A15")


    ChrTalk(
        0xB,
        (
            "Arios only\x01",
            "It tends to attract attention,\x01",
            "That women prime minister is also good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh, of course you also.\x01",
            "Thanks to you I had a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB0")

    Jump("loc_4B17")

    label("loc_4AB5")


    ChrTalk(
        0xB,
        (
            "The hittermen,\x01",
            "He came to destroy demonic beasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, seriously serving\x01",
            "I gotta give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B17")

    Jump("loc_4C64")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE7")

    ChrTalk(
        0xB,
        (
            "welcome.\x01",
            "Please go to your favorite seat ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "うちのオススメcuisineは、\x01",
            "Anyway it's omurice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently improved\x01",
            "Because it became more delicious,\x01",
            "If it's okay, eat it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C64")

    label("loc_4BE7")


    ChrTalk(
        0xB,
        (
            "今日はHaroldさんが\x01",
            "I am taking a room on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The business negotiation seems to have ended,\x01",
            "Take some coffee\x01",
            "I wonder if I should give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C64")

    TalkEnd(0xFE)
    Return()

    # Function_13_3F1E end

    def Function_14_4C68(): pass

    label("Function_14_4C68")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Cryちゃん、\x01",
            "Will not you go to the city with me next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With the rumored Orkis Tower\x01",
            "Let's go see it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well,\x01",
            "But there is a store help … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I see\x01",
            "Our omurice in 10 hours in an hour\x01",
            "If I can finish it, you can go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, no …\x01",
            "Well that's unbelievable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_4C68 end

    def Function_15_4D9A(): pass

    label("Function_15_4D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E75")

    ChrTalk(
        0xC,
        (
            "To be honest, for me\x01",
            "I do not understand the translation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Absolutely, whatever happens\x01",
            "俺がCryちゃんをI'll protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "… … When I tell him to face\x01",
            "I was laughed but …. Hiho.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EE2")

    label("loc_4E75")


    ChrTalk(
        0xC,
        (
            "Cryちゃんには\x01",
            "I was laughed but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Absolutely, whatever happens\x01",
            "俺がCryちゃんを\x01",
            "I'll protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE2")

    Jump("loc_5A74")

    label("loc_4EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_504A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC1")

    ChrTalk(
        0xC,
        (
            "ここだけの話、Cryちゃんの\x01",
            "cuisineの腕って……アレなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It looks like an eraser\x01",
            "When omelette was served,\x01",
            "Truly I also got scolded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "… … Well, I forcibly finished it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5045")

    label("loc_4FC1")


    ChrTalk(
        0xC,
        (
            "ここだけの話、Cryちゃんの\x01",
            "cuisineの腕って……アレなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "… Well, what will come out\x01",
            "I just forcibly finish it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5045")

    Jump("loc_5A74")

    label("loc_504A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5123")

    ChrTalk(
        0xC,
        (
            "Defense Forces men,\x01",
            "It is not good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To the habit of stopping in the village,\x01",
            "It's like \"I protect you\"\x01",
            "I feel sorry for lack of atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Became a defense army from the guard,\x01",
            "Is not it soaring?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_518B")

    label("loc_5123")


    ChrTalk(
        0xC,
        (
            "For the defense army people\x01",
            "Somehow you get angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Became a defense army from the guard,\x01",
            "Is not it soaring?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518B")

    Jump("loc_5A74")

    label("loc_5190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5286")

    ChrTalk(
        0xC,
        (
            "The main criminal of the recent raid incident,\x01",
            "I'm still hiding in crossbell\x01",
            "There is a high possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Recently, the guard's patrol has increased\x01",
            "I wonder what it is like …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Somehow the crossbell,\x01",
            "I got to a noisy place\x01",
            "It's alright …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5311")

    label("loc_5286")


    ChrTalk(
        0xC,
        (
            "The main criminal of the recent raid incident,\x01",
            "I'm still hiding in crossbell\x01",
            "There is a high possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Somehow the crossbell,\x01",
            "It became a noisy place ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5311")

    Jump("loc_5A74")

    label("loc_5316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E8")

    ChrTalk(
        0xC,
        (
            "Oh, I see.\x01",
            "An example of a referendum is\x01",
            "You are approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Going to vote to the city is\x01",
            "It's a little troublesome ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We also to the villagers\x01",
            "It is relevant,\x01",
            "You had better go properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5464")

    label("loc_53E8")


    ChrTalk(
        0xC,
        (
            "I ask the question of independence\x01",
            "The referendum is approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is troublesome to go to the vote to the city ….\x01",
            "You had better go properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5464")

    Jump("loc_5A74")

    label("loc_5469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5667")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5558")

    ChrTalk(
        0xC,
        (
            "Today, with Mr. Minnes\x01",
            "Derrickの商談が終わるらしい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Celebrating the reincarnation of Almorika village,\x01",
            "I want to do it even with the launch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "へへ、Cryちゃんも派手好きだし、\x01",
            "I'm sure you will be pleased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55E7")

    label("loc_5558")


    ChrTalk(
        0xC,
        (
            "Today, with Mr. Minnes\x01",
            "Derrickの商談が終わるらしい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even doing the launch with the parts,\x01",
            "A new origination of Almorika village\x01",
            "I hope to celebrate with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E7")

    Jump("loc_5662")

    label("loc_55EC")


    ChrTalk(
        0xC,
        (
            "Mr. Minnes's story ……\x01",
            "Perhaps, were they all lying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "あー、Derrickの奴も\x01",
            "I wonder if he is considerably worried …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5662")

    Jump("loc_5A74")

    label("loc_5667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_579C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5725")

    ChrTalk(
        0xC,
        (
            "That foreigner Osassu,\x01",
            "I would like to have plenty of life experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "俺がCryちゃんに\x01",
            "Through seeing what I long for,\x01",
            "He encouraged me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, he's a nice person ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5797")

    label("loc_5725")


    ChrTalk(
        0xC,
        (
            "That foreigner 's Osan,\x01",
            "Cryちゃんに憧れている俺を\x01",
            "He encouraged me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, he's a nice person ……\x02",
    )

    CloseMessageWindow()

    label("loc_5797")

    Jump("loc_5A74")

    label("loc_579C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_580D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B7")
    Call(0, 14)
    Jump("loc_5808")

    label("loc_57B7")


    ChrTalk(
        0xC,
        (
            "About …\x01",
            "You must have been brave and invited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Cryちゃんは手厳しいぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_5808")

    Jump("loc_5A74")

    label("loc_580D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E0")

    ChrTalk(
        0xC,
        (
            "Actually, soon\x01",
            "Cryちゃんをデートに\x01",
            "I was planning to invite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyday as far as I can say\x01",
            "Come to the shop, both of you\x01",
            "I became very familiar … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It should surely OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5950")

    label("loc_58E0")


    ChrTalk(
        0xC,
        (
            "近いうちにCryちゃんを\x01",
            "I am planning to invite him to a date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Okay, prepare your mind for today … …\x01",
            "The decision will be tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5950")

    Jump("loc_5A74")

    label("loc_5955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EF")

    ChrTalk(
        0xC,
        (
            "The signboard girl of this store,\x01",
            "Cryちゃんは俺の憧れなんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway,\x01",
            "I can not accept that smile!\x01",
            "I'll be there a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A74")

    label("loc_59EF")


    ChrTalk(
        0xC,
        (
            "Cryちゃんの笑顔の為なら、\x01",
            "No matter how many times I changed coffee\x01",
            "I want to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wait … are you again?\x01",
            "It is not free though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A74")

    TalkEnd(0xFE)
    Return()

    # Function_15_4D9A end

    def Function_16_5A78(): pass

    label("Function_16_5A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8F")
    Call(0, 44)
    Return()

    label("loc_5A8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9C")

    ChrTalk(
        0xD,
        (
            "There is still \"Phantom beast\"\x01",
            "With the advent of an unknown big tree\x01",
            "Although the movement of the highway is restricted … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "街に戻ったHarold君が、\x01",
            "Some books that I like\x01",
            "I heard you bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "ああ、流石はHarold君だ。\x01",
            "I can not wait for his return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C3C")

    label("loc_5B9C")


    ChrTalk(
        0xD,
        (
            "聡明なHarold君のことだ、\x01",
            "I'm sure you like my favorite book\x01",
            "I am sure you will bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… It is such a situation though.\x01",
            "Also enough for moving the highway\x01",
            "I would like you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3C")

    Jump("loc_6C79")

    label("loc_5C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D29")

    ChrTalk(
        0xD,
        (
            "Due to movement restrictions on the highway,\x01",
            "I can not go to the library freely\x01",
            "I was going on … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "McDaely's chairman\x01",
            "You finally did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The situation improved as it was,\x01",
            "The barrier that wraps around the city\x01",
            "Does it disappear and disappears?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DBC")

    label("loc_5D29")


    ChrTalk(
        0xD,
        (
            "このままThe barrier that wraps around the city\x01",
            "Does it disappear and disappears?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Everything is restored,\x01",
            "To go to the library freely\x01",
            "I hope I can do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBC")

    Jump("loc_6C79")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB8")

    ChrTalk(
        0xD,
        (
            "With \"Phantom beast\" and movement restrictions on the highway\x01",
            "Agriculture never goes well, I feel like changing\x01",
            "I would like to read even a new book ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Also in the library in Crosbell City\x01",
            "Of course you can not go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Although reading is a moisture of life,\x01",
            "Do not you think it is too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F4D")

    label("loc_5EB8")


    ChrTalk(
        0xD,
        (
            "To the library in Crosbell City\x01",
            "I can not go …\x01",
            "I can not read new books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If I had this kind of life for years\x01",
            "I can only say hell … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4D")

    Jump("loc_6C79")

    label("loc_5F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_60C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604C")

    ChrTalk(
        0xD,
        (
            "I left a while ago.\x01",
            "Special issue of Crossbell Times,\x01",
            "I will read over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I am also worried about the attacks,\x01",
            "An article in which Iria was seriously injured\x01",
            "Shocking than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… As residents of Crossbell,\x01",
            "I just pray for her recovery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60BE")

    label("loc_604C")


    ChrTalk(
        0xD,
        (
            "Always on the crossbell\x01",
            "Iria who kept giving life,\x01",
            "What does it mean to meet such an eye …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "… … I just pray for recovery.\x02",
    )

    CloseMessageWindow()

    label("loc_60BE")

    Jump("loc_6C79")

    label("loc_60C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_618E")

    ChrTalk(
        0xD,
        (
            "Sound of comfortable rain striking the window,\x01",
            "Warm coffee besides … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For me on a rainy day,\x01",
            "It's the best reading day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because it's no problem\x01",
            "A book that had been collected at once\x01",
            "Shall I read it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_61FC")

    label("loc_618E")


    ChrTalk(
        0xD,
        (
            "Sound of comfortable rain striking the window,\x01",
            "Warm coffee besides … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For me on a rainy day,\x01",
            "It's the best reading day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61FC")

    Jump("loc_6C79")

    label("loc_6201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_650D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D9")

    ChrTalk(
        0xD,
        (
            "The era changes,\x01",
            "The problem that this village has is\x01",
            "I think it has increased more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The village chief should abandon tradition\x01",
            "Although not saying ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Derrick君が改革を望むのも\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6354")

    label("loc_62D9")


    ChrTalk(
        0xD,
        (
            "The era changes,\x01",
            "The problem that this village has is\x01",
            "I think it has increased more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Derrick君が改革を望むのも\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6354")

    Jump("loc_6508")

    label("loc_6359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6458")

    ChrTalk(
        0xD,
        (
            "That man, Minnesh,\x01",
            "It seems that you were successfully embracing the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What other people want … …\x01",
            "The insight to figure it out,\x01",
            "I definitely would have been real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Talent for talent, fraud etc.\x01",
            "It means that I used it\x01",
            "It is a story that I can not save.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6508")

    label("loc_6458")


    ChrTalk(
        0xD,
        (
            "That man named Minnes … …\x01",
            "If you do not dress hands like fraud,\x01",
            "You may have been Taisei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… Well, as far as I can talk\x01",
            "There seems to be quite a few preparations,\x01",
            "I do not have any room for sympathy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6508")

    Jump("loc_6C79")

    label("loc_650D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6672")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "\"There really was a crossbell monster\"\x01",
            "I borrowed a book from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The story of this \"man seeking his head …\"\x01",
            "No, the spine does not freeze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, it is certainly frightening ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I should not have my head,\x01",
            "I do not know where to \"look for\"\x01",
            "I gave a groan voice ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… There is not much\x01",
            "It's not a scary part.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_66F5")

    label("loc_6672")


    ChrTalk(
        0xD,
        (
            "Funky\x01",
            "I was immersed in fear\x01",
            "Gofanのせいで台無しだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is how to enjoy ghost stories\x01",
            "I have to teach it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6C79")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685A")

    ChrTalk(
        0xD,
        (
            "As I went to the library,\x01",
            "I have been enjoying reading recently\x01",
            "I bought a novel of a continuation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Apparently, skip the number of turns\x01",
            "It seems I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I accidentally read it\x01",
            "I want to avoid being spoiled ……\x01",
            "I am sorry but I wonder if they will get it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝５卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝５卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 4)
    TalkEnd(0xFE)
    SetChrFlags(0xD, 0x10)
    Return()

    label("loc_685A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D8")
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xD,
        (
            "I borrowed it at the library today.\x01",
            "\"Beauties who moved the continents\" … …\x01",
            "It's quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With \"War Otome Rianu\" as the lead,\x01",
            "A woman who formed historical feat of each country\x01",
            "It was a book that I was introducing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, after all women\x01",
            "Originally it may be a strong existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To my daughter as well\x01",
            "I am leaning to the buttocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(That is you\x01",
            "I think that I'm just not going to rely … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    Jump("loc_6A3E")

    label("loc_69D8")


    ChrTalk(
        0xD,
        (
            "\"Beauties who moved the continents\" … …\x01",
            "It's quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You guys also at the library\x01",
            "Why do not you read it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A3E")

    Jump("loc_6C79")

    label("loc_6A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4C")

    ChrTalk(
        0xD,
        (
            "I like reading.\x01",
            "I went to the city library this morning\x01",
            "I intended to go ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With President's Cross Bell\x01",
            "Traffic is regulated by traffic,\x01",
            "I had completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thanks and good news\x01",
            "I spent the morning.\x01",
            "Whew, it's unbelievable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BC7")

    label("loc_6B4C")


    ChrTalk(
        0xD,
        (
            "Traffic regulation of the road now is also\x01",
            "It seems that it is canceled … ….\x01",
            "I wonder if I will go to the city later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Go to the library,\x01",
            "I have to find something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BC7")

    Jump("loc_6C79")

    label("loc_6BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE4")
    Jump("loc_6C79")

    label("loc_6BE4")


    ChrTalk(
        0xD,
        (
            "They, at the miscellaneous goods store of Mr. Leol\x01",
            "Save foods that you can save\x01",
            "It seems they bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I wonder if I can go climbing.\x01",
            "I could not see such a gathering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C79")

    TalkEnd(0xFE)
    Return()

    # Function_16_5A78 end

    def Function_17_6C7D(): pass

    label("Function_17_6C7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D20")

    ChrTalk(
        0xE,
        (
            "Haroldさん一家は、\x01",
            "I got back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because I became friends\x01",
            "I am somewhat lonely but ….\x01",
            "This is the situation and it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6DBF")

    label("loc_6D20")


    ChrTalk(
        0xE,
        (
            "Haroldさん一家は、\x01",
            "I was worried about my neighbors,\x01",
            "You had better go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "私とStephaneも里帰りする時には、\x01",
            "You have to go to a greeting by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DBF")

    Jump("loc_76B9")

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6DD2")
    Jump("loc_76B9")

    label("loc_6DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBF")

    ChrTalk(
        0xE,
        (
            "It has become such a thing,\x01",
            "I am in Crossbell City\x01",
            "I am worried about my old neighborhood … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haroldさんたちは、\x01",
            "While worrying about the city but properly\x01",
            "You are doing what you should do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I have to do something, something I can do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F50")

    label("loc_6EBF")


    ChrTalk(
        0xE,
        (
            "Haroldさんたちは、\x01",
            "While worrying about the city but properly\x01",
            "You are doing what you should do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I am not only worried,\x01",
            "I have to do something I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F50")

    Jump("loc_76B9")

    label("loc_6F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7025")

    ChrTalk(
        0xE,
        (
            "Ha\x01",
            "I wish for the city to be attacked\x01",
            "I did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Fortunately, you know\x01",
            "It looks like it was safe ….\x01",
            "There seems to have been many victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This is already\x01",
            "I hope it will not happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7090")

    label("loc_7025")


    ChrTalk(
        0xE,
        (
            "Ha\x01",
            "I wish for the city to be attacked\x01",
            "I did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This is already\x01",
            "I hope it will not happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7090")

    Jump("loc_76B9")

    label("loc_7095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7180")

    ChrTalk(
        0xE,
        (
            "Until moving to the village,\x01",
            "Although I have a business trip on Sunday school\x01",
            "You did not know even existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To let the village go to the cathedral\x01",
            "I thought it was hard … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You are coming from a distant place\x01",
            "I must thank Sister for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_71F0")

    label("loc_7180")


    ChrTalk(
        0xE,
        (
            "From here to the cathedral\x01",
            "It is hard to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You are coming from a distant place\x01",
            "I must thank Sister for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71F0")

    Jump("loc_76B9")

    label("loc_71F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_731B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7298")

    ChrTalk(
        0xE,
        (
            "Son of a village mayor … …\x01",
            "Since I came back yesterday\x01",
            "It looks like he's tingling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The future of the village in today's negotiations\x01",
            "What is taking … …\x01",
            "Of course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7316")

    label("loc_7298")


    ChrTalk(
        0xE,
        (
            "Stephaneや村の子供たちが\x01",
            "I'm glad I did not get attacked by demons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Indeed, if you come with that cheat … …\x01",
            "I will never forgive them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7316")

    Jump("loc_76B9")

    label("loc_731B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D3")

    ChrTalk(
        0xE,
        (
            "Hmmm … ___ ___ 0\x01",
            "The sheets are OK with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "私、Stephaneを産む前は\x01",
            "I was longing for the maid of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, help at the hotel tavern\x01",
            "It is quite fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_744C")

    label("loc_73D3")


    ChrTalk(
        0xE,
        (
            "Huhu, help at the hotel tavern\x01",
            "It is quite fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stephaneも友達と\x01",
            "It seems they are doing good friends,\x01",
            "Every day is fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_744C")

    Jump("loc_76B9")

    label("loc_7451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74D6")

    ChrTalk(
        0xE,
        (
            "Today I helped with the store\x01",
            "I am doing the cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "私もStephaneも\x01",
            "I am indebted to you,\x01",
            "You should use even a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B9")

    label("loc_74D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_757D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F1")
    Call(0, 23)
    Jump("loc_7578")

    label("loc_74F1")


    ChrTalk(
        0xE,
        (
            "Well, is it okay?\x01",
            "You will appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "ふふ、Stephaneが前に\x01",
            "Listening to the treat,\x01",
            "I also wanted to try it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7578")

    Jump("loc_76B9")

    label("loc_757D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_76B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7632")

    ChrTalk(
        0xE,
        (
            "私と息子のStephaneは、\x01",
            "A little while ago from the crossbell\x01",
            "I have migrated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "At first I was also hating that girl,\x01",
            "I seem to have got used to the village.\x01",
            "Hehe, it was good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_76B9")

    label("loc_7632")


    ChrTalk(
        0xE,
        (
            "By the way,\x01",
            "Gofanさんのご好意で\x01",
            "I had you let me borrow it cheaply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, people in this village\x01",
            "It's warm and gentle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B9")

    TalkEnd(0xFE)
    Return()

    # Function_17_6C7D end

    def Function_18_76BD(): pass

    label("Function_18_76BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7745")

    ChrTalk(
        0xF,
        (
            "On Sunday School Day,\x01",
            "On vacation time an innkeeper told me\x01",
            "You bring me a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh, I wonder if it will be a holiday time soon.\x02",
    )

    CloseMessageWindow()

    label("loc_7745")

    TalkEnd(0xFE)
    Return()

    # Function_18_76BD end

    def Function_19_7749(): pass

    label("Function_19_7749")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77BB")

    ChrTalk(
        0x10,
        (
            "pulleyね、\x01",
            "Today with my girls\x01",
            "He is a student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I do not even understand one though.\x02",
    )

    CloseMessageWindow()

    label("loc_77BB")

    TalkEnd(0xFE)
    Return()

    # Function_19_7749 end

    def Function_20_77BF(): pass

    label("Function_20_77BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_792A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_789C")

    ChrTalk(
        0x11,
        (
            "With my mother\x01",
            "I was going to see the state of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The neighborhood where I lived before\x01",
            "My friends and neighbors.\x01",
            "Everyone seems to have been safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Mom, I was worried for a long time\x01",
            "It looks like … ….\x01",
            "Really, it was good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7925")

    label("loc_789C")


    ChrTalk(
        0x11,
        (
            "昨日まで、With my mother\x01",
            "I was going to see the state of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Previous friends and neighbors,\x01",
            "Everyone seems to have been safe.\x01",
            "Really, it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7925")

    Jump("loc_7A32")

    label("loc_792A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D4")

    ChrTalk(
        0x11,
        (
            "When I was in town I went to the cathedral\x01",
            "I was passing though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "When I live in a village\x01",
            "From the sister\x01",
            "You are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "…… It might be a little rakin.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7A32")

    label("loc_79D4")


    ChrTalk(
        0x11,
        (
            "When I was in town,\x01",
            "To the Sunday school to the cathedral\x01",
            "I was passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "…… It may be a little late now.\x02",
    )

    CloseMessageWindow()

    label("loc_7A32")

    TalkEnd(0xFE)
    Return()

    # Function_20_77BF end

    def Function_21_7A36(): pass

    label("Function_21_7A36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7A8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A89")

    ChrTalk(
        0x12,
        (
            "……today,\x01",
            "There is an important customer.\x01",
            "Get out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A89")

    Jump("loc_7F26")

    label("loc_7A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE1")

    ChrTalk(
        0x12,
        "… …. You guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FDerrickさん……\x01",
            "Ah, preferably once more\x01",
            "Try talking with the village head … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…… Hun.\x01",
            "Talk etc. I've done it many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However, the village mayor is only concerned about maintenance,\x01",
            "There is nothing but my reform plan\x01",
            "I did not try to admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Meanwhile, Mr. Minnes\x01",
            "To me who was giving up reform of the village\x01",
            "It gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I do not depend on my father anymore …\x01",
            "We two people, Almorika village\x01",
            "I do good reform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(…… Minneshi has a suspicious point.\x01",
            "If possible we would like you to think again … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(There is insufficient evidence at this time.\x01",
            "Persuasion will be difficult, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D7D")

    label("loc_7CE1")


    ChrTalk(
        0x12,
        (
            "Mr. Minnes\x01",
            "To me who was giving up reform of the village\x01",
            "It gave me a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I do not depend on my father anymore …\x01",
            "We two people, Almorika village\x01",
            "I do good reform.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7D")

    Jump("loc_7F26")

    label("loc_7D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EAB")

    ChrTalk(
        0x12,
        (
            "Father …… The village mayor,\x01",
            "No matter what reform plan is issued\x01",
            "I will not admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The second phrase is \"the figure that the village should be\"\x01",
            "\"Do not lose sight of the essence\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However, to such things without such a form\x01",
            "Even though I hold on to the village\x01",
            "Only quietly being destroyed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…… Fuu, I do not know what\x01",
            "I got tired.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7F26")

    label("loc_7EAB")


    ChrTalk(
        0x12,
        (
            "Since village mayor does not approve,\x01",
            "Village reform will not be done.\x01",
            "Only wait for the ruin … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…… I do not know what\x01",
            "I got tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F26")

    TalkEnd(0xFE)
    Return()

    # Function_21_7A36 end

    def Function_22_7F2A(): pass

    label("Function_22_7F2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F48")
    Call(0, 23)
    Jump("loc_7FC5")

    label("loc_7F48")


    ChrTalk(
        0x13,
        (
            "Oh yes, today\x01",
            "I came to shovel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Look, my good at\x01",
            "Homemade made carbonara sauce.\x01",
            "Eat with pasta.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC5")

    TalkEnd(0xFE)
    Return()

    # Function_22_7F2A end

    def Function_23_7FC9(): pass

    label("Function_23_7FC9")

    OP_4B(0xE, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Well then, for a while\x01",
            "Are you staying in this room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah, because it's your pleasure\x01",
            "I thought about letting me amenable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Instead, a little\x01",
            "Trying to help the shop\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That's good.\x01",
            "Up to now I've been cutting out with two people,\x01",
            "It will be pleased if more people are added.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0xE, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_23_7FC9 end

    def Function_24_80E7(): pass

    label("Function_24_80E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818E")

    ChrTalk(
        0x14,
        (
            "Today, I noticed something going on\x01",
            "Some places in the village\x01",
            "There are footprints like big cats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Yesterday in this village\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8203")

    label("loc_818E")


    ChrTalk(
        0x14,
        (
            "Some places in the village\x01",
            "Footprints like big cats\x01",
            "It looks like it is on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Yesterday in this village\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8203")

    TalkEnd(0xFE)
    Return()

    # Function_24_80E7 end

    def Function_25_8207(): pass

    label("Function_25_8207")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8218")
    Jump("loc_8F24")

    label("loc_8218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_863E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8590")

    ChrTalk(
        0x15,
        (
            "#03600FOh, everyone …!\x01",
            "It is safe and above all.\x02\x03",
            "#03603FBy McDowell\x01",
            "When an invalid declaration of an independent country was made\x01",
            "I heard rumors.\x02\x03",
            "#03605FPerhaps, everyone … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWell, it was a lot of hard work … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSomething in Almorika village,\x01",
            "Have there been changes in the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FNo, for now …\x02\x03",
            "#03600FHowever, just during negotiations with the Defense Forces\x01",
            "It was contacted,\x01",
            "They seemed to be panicking too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAfter all the impact on the village\x01",
            "It seems to be insignificant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if anything\x01",
            "The influence on the city will be great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FYes, everyone in the neighborhood is worried\x01",
            "Mainz and Ursula hospital as well\x01",
            "I am interested.\x02\x03",
            "#03608FIf I managed to move freely\x01",
            "I'd like to visit each area … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Anyway, the situation is still\x01",
            "It can not be said that it completely improved.\x02\x03",
            "#00000FHaroldさんの方も\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#03600FWell, please take care of everyone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 5)
    Jump("loc_8639")

    label("loc_8590")


    ChrTalk(
        0x15,
        (
            "#03603FI am also worried about the neighborhood in the city\x01",
            "Mainz and Ursula hospital as well\x01",
            "I am interested.\x02\x03",
            "#03608FIf I managed to move freely\x01",
            "I'd like to visit each area … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8639")

    Jump("loc_8F24")

    label("loc_863E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_86F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8659")
    Call(0, 26)
    Jump("loc_86F4")

    label("loc_8659")


    ChrTalk(
        0x15,
        (
            "#03600FFor negotiations with the next Defense Forces,\x01",
            "Materials that everyone in the village needs\x01",
            "It is a place to summarize.\x02\x03",
            "#03603FEveryone, please take care.\x01",
            "…… Protecting the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86F4")

    Jump("loc_8F24")

    label("loc_86F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87EE")
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
            "#1K◆ \"Fraud case 2nd day\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",            # 0
            "【I am clearing】\x01",        # 1
            "【Not clear】\x01",      # 2
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
        (0, "loc_87D5"),
        (1, "loc_87DA"),
        (2, "loc_87E4"),
        (SWITCH_DEFAULT, "loc_87EE"),
    )


    label("loc_87D5")

    Jump("loc_87EE")

    label("loc_87DA")

    OP_29(0x87, 0x4, 0x10)
    Jump("loc_87EE")

    label("loc_87E4")

    OP_29(0x87, 0x3, 0x10)
    Jump("loc_87EE")

    label("loc_87EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8910")

    ChrTalk(
        0x15,
        (
            "#03600FFrom the village head to Armorica\x01",
            "I received an invitation.\x02\x03",
            "#03603FTo the gratitude of the matter of the case of the fraud case\x01",
            "Pete who was invited with him\x01",
            "It seems I thought I refrained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FIn that Minnes incident ……\x01",
            "Is that so.\x02\x03",
            "#00003FI can not get caught up to Pete\x01",
            "Should I say good?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A08")

    label("loc_8910")


    ChrTalk(
        0x15,
        (
            "#03600FFrom the village head to Armorica\x01",
            "I received an invitation.\x02\x03",
            "#03603FTo thank you for helping a case\x01",
            "Pete who was invited with him\x01",
            "It seems I thought I refrained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so.\x02\x03",
            "#00003FI can not get caught up to Pete\x01",
            "Should I say good?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A08")


    ChrTalk(
        0x15,
        "#03600FYes, I really think so.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8AB9")

    label("loc_8A37")


    ChrTalk(
        0x15,
        (
            "#03600FResistance forces are in the middle of the old road\x01",
            "In the vicinity of the Almora Battlefield\x01",
            "It seems to have been witnessed.\x02\x03",
            "#03603FEveryone, please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AB9")

    Jump("loc_8F24")

    label("loc_8ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9D")

    ChrTalk(
        0x101,
        (
            "#00000Fあ……Haroldさん。\x01",
            "I came here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03605FOh, everyone in the support department.\x01",
            "It is strange to see him in such a place.\x02\x03",
            "#03600FYeah, today we will negotiate\x01",
            "I was just about to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, as usual\x01",
            "I am doing business in good faith\x01",
            "You look like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609FThanks to you.\x01",
            "Good deal today\x01",
            "I was allowed to.\x02\x03",
            "#03600FThat's right, everyone …\x01",
            "Please accept this if you do not mind.\x01",
            "Can I get it?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蜂蜜糖浆', 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x104,
        "#00305FHow old are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FYeah, in fact at the time of trading\x01",
            "I got it extra.\x02\x03",
            "#03609FI can not finish eating with my house,\x01",
            "If you do not mind, everyone's\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWell then, then …\x01",
            "Thankfully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 6)
    Jump("loc_8F24")

    label("loc_8D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E91")

    ChrTalk(
        0x15,
        (
            "#03604FThanks to you\x01",
            "Good deal today\x01",
            "I was allowed to.\x02\x03",
            "#03608Fただ最近、村長はDerrickくんと\x01",
            "Dispute#2RSomething#It seems that it does not go out continuously,\x01",
            "It was quite troubling.\x02\x03",
            "#03603F…… Parents and children are\x01",
            "It is still difficult, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8F24")

    label("loc_8E91")


    ChrTalk(
        0x15,
        (
            "#03603F村長とDerrickくん……\x01",
            "The feeling of wanting to protect the village is\x01",
            "It should be there with each other … …\x02\x03",
            "#03608F…… Parents and children are\x01",
            "It is still difficult, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F24")

    TalkEnd(0xFE)
    Return()

    # Function_25_8207 end

    def Function_26_8F28(): pass

    label("Function_26_8F28")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#03608FReol's low back pain medicine ……\x01",
            "それにAngersさんの家では\x01",
            "Is the bandage missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700FThe owner of this inn also,\x01",
            "Some of the seasoning is running out\x01",
            "It looked like I was in trouble.\x02\x03",
            "#03708FThat spice is only in department stores\x01",
            "I think it was something I did not put in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03603FHmm …… bandage plaster\x01",
            "It seems to be managed somehow,\x01",
            "Others seem to need to negotiate.\x02\x03",
            "#03600Fありがとう、Sofia。\x01",
            "Leave it to me and rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_26_8F28 end

    def Function_27_90D5(): pass

    label("Function_27_90D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9104")
    Call(0, 38)
    Return()

    label("loc_9104")

    Call(0, 39)
    Return()

    label("loc_9108")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_27_90D5 end

    def Function_28_910F(): pass

    label("Function_28_910F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913E")
    Call(0, 38)
    Return()

    label("loc_913E")

    Call(0, 39)
    Return()

    label("loc_9142")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_28_910F end

    def Function_29_9149(): pass

    label("Function_29_9149")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_915A")
    Jump("loc_9365")

    label("loc_915A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9168")
    Jump("loc_9365")

    label("loc_9168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9183")
    Call(0, 26)
    Jump("loc_9200")

    label("loc_9183")


    ChrTalk(
        0x16,
        (
            "#03700FAs my partner's partner,\x01",
            "I am helping it while it is very powerful.\x02\x03",
            "Even a little, everyone in the village\x01",
            "I hope it helps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9200")

    Jump("loc_9365")

    label("loc_9205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F5")

    ChrTalk(
        0x16,
        (
            "#03708FEveryone else in the support section …\x01",
            "Makes you worry, right.\x02\x03",
            "#03700FI hope that you can merge safely\x01",
            "I pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FThanks Muff, Huff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIn any case,\x01",
            "I have to join them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_9365")

    label("loc_92F5")


    ChrTalk(
        0x16,
        (
            "#03708FEveryone else in the support section …\x01",
            "Makes you worry, right.\x02\x03",
            "#03700FThings that you can join safely\x01",
            "I pray.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9365")

    TalkEnd(0xFE)
    Return()

    # Function_29_9149 end

    def Function_30_9369(): pass

    label("Function_30_9369")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_937A")
    Jump("loc_9739")

    label("loc_937A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9388")
    Jump("loc_9739")

    label("loc_9388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_940C")

    ChrTalk(
        0x17,
        (
            "#03805FWell, my parents\x01",
            "It looks like he's doing a job … …\x02\x03",
            "#03800FCamilleくんたちのところに\x01",
            "Maybe I should go to play?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9739")

    label("loc_940C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9602")
    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94B0")
    Jump("loc_94FA")

    label("loc_94B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_94D0")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94FA")

    label("loc_94D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94F0")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94FA")

    label("loc_94F0")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_94FA")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEh, my dog.\x01",
            "Let's play again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3CWell, time is allowed.\x02\x03",
            "#01203F…… However, at the support department\x01",
            "Since entering,\x01",
            "It is nostalgic for young children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHuhu,\x01",
            "Whether it is a good place for Zeit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_9734")

    label("loc_9602")

    OP_52(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x107, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9693")
    Jump("loc_96DD")

    label("loc_9693")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96B3")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96DD")

    label("loc_96B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96D3")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96DD")

    label("loc_96D3")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96DD")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(
        0x17,
        (
            "#03809FEh, my dog.\x01",
            "Let's play again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9734")

    ClearChrFlags(0x17, 0x10)

    label("loc_9739")

    TalkEnd(0xFE)
    Return()

    # Function_30_9369 end

    def Function_31_973D(): pass

    label("Function_31_973D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9753")
    SetScenarioFlags(0x2, 2)

    label("loc_9753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA9")

    ChrTalk(
        0x18,
        (
            "#04303F#30WThis is Mercapa\x01",
            "If it is usable for a while … …\x02\x03",
            "#04300FAs soon as we recover, we as much as we can\x01",
            "I'm going to have a backup.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_9905")
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x105, 0)
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9891")
    Jump("loc_98DB")

    label("loc_9891")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98B1")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98DB")

    label("loc_98B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98D1")
    OP_52(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98DB")

    label("loc_98D1")

    OP_52(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98DB")

    OP_52(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x10)

    label("loc_9905")


    ChrTalk(
        0x18,
        (
            "#04308F#30W── Wadi.\x01",
            "Do not you feel unhappy?\x02\x03",
            "#04301FIf I run out of force like me\x01",
            "Do not get stolen at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403FAh……\x01",
            "I will keep it at the best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA4")
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#04300F#30WWell … I did a place to forget.\x01",
            "Lloyd, hand out.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 2)

    ChrTalk(
        0x104,
        "#00305FThis guy……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs there a piece of something …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#04303F#30WIron is\x01",
            "It fell to the place where it crashed … …\x01",
            "Perhaps, something of a guy or something.\x02\x03",
            "#04300FLloyd's guys after all\x01",
            "I thought there might be something to use,\x01",
            "It was a monkey picked up.\x02\x03",
            "#04311FWell, I'll come back from the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then……\x01",
            "I will appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BA4")

    Jump("loc_9C66")

    label("loc_9BA9")


    ChrTalk(
        0x18,
        (
            "#04303F#30WThis is Mercapa\x01",
            "If it is usable for a while … …\x02\x03",
            "#04300FAs soon as we recover, we as much as we can\x01",
            "I'm going to have a backup.\x02\x03",
            "#04302FAnyway I feel bored, Lloyd guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C66")

    TalkEnd(0xFE)
    Return()

    # Function_31_973D end

    def Function_32_9C6A(): pass

    label("Function_32_9C6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D95")

    ChrTalk(
        0x19,
        (
            "#13808FMr. Kiya who came to Sunday school\x01",
            "Always doing something about you\x01",
            "I was talking happily.\x02\x03",
            "#13804F… As a knight of the star cup\x01",
            "It might be a disagreeable remark … …\x02\x03",
            "#13802FTo regain that smile is\x01",
            "I think that it is worth more than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FMr. Lease ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F… … The point of consent is understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E26")

    label("loc_9D95")


    ChrTalk(
        0x19,
        (
            "#13808FMr. Kiya who came to Sunday school\x01",
            "Always doing something about you\x01",
            "I was talking happily.\x02\x03",
            "#13804F… …. Please keep that smile\x01",
            "Please regain it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E26")

    TalkEnd(0xFE)
    Return()

    # Function_32_9C6A end

    def Function_33_9E2A(): pass

    label("Function_33_9E2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F35")

    ChrTalk(
        0xFE,
        (
            "For the plenary sessions, we requested\x01",
            "I'm about to look around the country,\x01",
            "This neighborhood is peace itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村長さんとDerrick君の関係が\x01",
            "I'm worried about getting somewhat bad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's not something I will talk out.\x01",
            "You do not have to be neutral to the last.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_9FCD")

    label("loc_9F35")


    ChrTalk(
        0xFE,
        (
            "村長さんとDerrick君の関係が\x01",
            "I'm worried about getting somewhat bad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's not something I will talk out.\x01",
            "You do not have to be neutral to the last.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FCD")

    TalkEnd(0xFE)
    Return()

    # Function_33_9E2A end

    def Function_34_9FD1(): pass

    label("Function_34_9FD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A057")

    ChrTalk(
        0xFE,
        (
            "At the crossing bridge,\x01",
            "A good old man\x01",
            "It looks like ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……whatever.\x01",
            "I am not interested in humans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_A092")

    label("loc_A057")


    ChrTalk(
        0xFE,
        "Munching …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The omelet rice here,\x01",
            "favorite……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A092")

    TalkEnd(0xFE)
    Return()

    # Function_34_9FD1 end

    def Function_35_A096(): pass

    label("Function_35_A096")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A135")
    BeginChrThread(0x109, 1, 0, 36)
    WaitChrThread(0x109, 1)

    label("loc_A135")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14F")
    BeginChrThread(0x105, 1, 0, 36)
    WaitChrThread(0x105, 1)

    label("loc_A14F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A169")
    BeginChrThread(0x106, 1, 0, 36)
    WaitChrThread(0x106, 1)

    label("loc_A169")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A183")
    BeginChrThread(0x10A, 1, 0, 36)
    WaitChrThread(0x10A, 1)

    label("loc_A183")

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

    def lambda_A267():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A267)
    Sleep(50)

    def lambda_A277():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A277)
    Sleep(50)

    def lambda_A287():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A287)
    Sleep(50)

    def lambda_A297():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A297)
    Sleep(50)

    def lambda_A2A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_A2A7)
    Sleep(50)

    def lambda_A2B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_A2B7)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMr. Lease …! Is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A328")

    ChrTalk(
        0x105,
        "#10402FWhat, were you here?\x02",
    )

    CloseMessageWindow()

    label("loc_A328")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetChrSubChip(0x18, 0x1)
    OP_93(0x19, 0x5A, 0x1F4)

    ChrTalk(
        0x19,
        "#13805Feveryone……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A39B")

    ChrTalk(
        0x18,
        (
            "#11P#04300F#30WAh……\x01",
            "Widely the Lloyd guys you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C0")

    label("loc_A39B")


    ChrTalk(
        0x18,
        "#11P#04300F#30WOh … you guys?\x02",
    )

    CloseMessageWindow()

    label("loc_A3C0")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4A0")
    BeginChrThread(0x109, 1, 0, 37)
    WaitChrThread(0x109, 1)

    label("loc_A4A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4BA")
    BeginChrThread(0x105, 1, 0, 37)
    WaitChrThread(0x105, 1)

    label("loc_A4BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4D4")
    BeginChrThread(0x106, 1, 0, 37)
    WaitChrThread(0x106, 1)

    label("loc_A4D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4EE")
    BeginChrThread(0x10A, 1, 0, 37)
    WaitChrThread(0x10A, 1)

    label("loc_A4EE")

    WaitChrThread(0x104, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00000FBoth of us both asked the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FThat unexpected flying doll\x01",
            "It seems that it was brilliant, shot down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00104FI really appreciate your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04302F#30WHa ha …\x01",
            "The damage of Kotch is also enormous.\x02\x03",
            "#04306FTo utterly exhaust the power\x01",
            "It's a place to have a rest, but ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A721")

    ChrTalk(
        0x103,
        (
            "#6P#00205FAccording to Mr. Abbas\x01",
            "Using a rather dangerous \"power\"\x01",
            "Did you say that it was in danger? …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FOh, with the power of \"Stigmata\" and Mercava\x01",
            "You linked and released it all at once?\x02\x03",
            "#10402FIt is totally unreasonable.\x01",
            "If you are not good at goddess#4REidos#I think I will go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A77B")

    label("loc_A721")


    ChrTalk(
        0x103,
        (
            "#6P#00205FAccording to Mr. Abbas\x01",
            "Using a rather dangerous \"power\"\x01",
            "Did you say that it was in danger? …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A77B")


    ChrTalk(
        0x101,
        "#6P#00005FWell, maybe … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13800FYeah, \"Stigmata\" originally,\x01",
            "Source of surplus forbidden power to human beings ……\x02\x03",
            "#13808FFree it unlimitedly\x01",
            "There is recklessly there.\x02\x03",
            "#13803FAs a responsible \"guardian knight\" position\x01",
            "I can not help to say that it is too low grade.\x02",
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
            "#11P#04306F#30W…… Ha, lease.\x01",
            "Please forgive me soon.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9AE")

    ChrTalk(
        0x105,
        (
            "#12P#10409FHaha, feel good\x01",
            "You seem to be spreading in the buttocks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA5B")

    label("loc_A9AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA05")

    ChrTalk(
        0x109,
        (
            "#12P#10109F(No, somewhat in the ass\x01",
            "It looks like being laid … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA5B")

    label("loc_AA05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA5B")

    ChrTalk(
        0x106,
        (
            "#12P#10702F(Huhu, apparently my head\x01",
            "It does not seem to rise …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAB6")

    ChrTalk(
        0x10A,
        (
            "#12P#00603F(Guardian Knight of the Star Cup ……\x01",
            "It is quite different from the information heard. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB79")

    label("loc_AAB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB13")

    ChrTalk(
        0x106,
        (
            "#12P#10704F(Guardian Knight of the Star Cup ……\x01",
            "It is quite different from what I heard. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB79")

    label("loc_AB13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB79")

    ChrTalk(
        0x109,
        (
            "#12P#10106FWell, you also say what Abbas says\x01",
            "I think I should listen more properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB79")


    ChrTalk(
        0x18,
        (
            "#11P#04303F#30WThat's … …\x02\x03",
            "#04308FBut well, ridiculous Mong\x01",
            "I guess it has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13801F\"A big blue tree\" ……\x01",
            "Is it a miracle that people's obsession created?\x02\x03",
            "#13803FNo way except by goddess hands\x01",
            "It seems that such things will appear … …\x02\x03",
            "#13808FMoreover, with the power of Mr. Kea … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F… …. Yeah ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FTo be honest, we also\x01",
            "I have not realized yet … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F── But, only this case\x01",
            "We will definitely solve it with ours.\x02\x03",
            "#00001FAs a \"Special Affairs Support Division\" ……\x01",
            "More than anything as a guardian of that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#04304F#30WI see……\x01",
            "It seems like he was prepared for a long time.\x02\x03",
            "#04300FThis is Mercapa\x01",
            "If it is usable for a while … …\x02\x03",
            "As soon as we recover, we as much as we can\x01",
            "I'm going to have a backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#13802F…… Protecting the goddess.\x01",
            "Please be careful again.\x02",
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
        "#12P#00100FWell then I'll be back.\x02",
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

    # Function_35_A096 end

    def Function_36_AF10(): pass

    label("Function_36_AF10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3F")
    SetChrPos(0xFE, 77230, 0, -2080, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF6E")
    SetChrPos(0xFE, 78370, 0, -1940, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9D")
    SetChrPos(0xFE, 79550, 0, -2100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AF9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFCC")
    SetChrPos(0xFE, 77200, 0, -3170, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AFCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFFB")
    SetChrPos(0xFE, 78370, 0, -3110, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01B")

    label("loc_AFFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01B")
    SetChrPos(0xFE, 79550, 0, -3200, 0)

    label("loc_B01B")

    Return()

    # Function_36_AF10 end

    def Function_37_B01C(): pass

    label("Function_37_B01C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B065")
    SetChrPos(0xFE, 78700, 0, -1050, 270)

    def lambda_B041():
        OP_95(0xFE, 71150, 0, -1050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B041)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0AE")
    SetChrPos(0xFE, 78650, 0, 0, 270)

    def lambda_B08A():
        OP_95(0xFE, 71150, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B08A)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B0AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F7")
    SetChrPos(0xFE, 79740, 0, -1220, 270)

    def lambda_B0D3():
        OP_95(0xFE, 72240, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0D3)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B0F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B140")
    SetChrPos(0xFE, 79740, 0, -40, 270)

    def lambda_B11C():
        OP_95(0xFE, 72240, 0, -40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B11C)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B140")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B189")
    SetChrPos(0xFE, 80780, 0, -1100, 270)

    def lambda_B165():
        OP_95(0xFE, 73280, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B165)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1C3")

    label("loc_B189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C3")
    SetChrPos(0xFE, 80780, 0, 20, 270)

    def lambda_B1AE():
        OP_95(0xFE, 73280, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B1AE)

    label("loc_B1C3")

    Return()

    # Function_37_B01C end

    def Function_38_B1C4(): pass

    label("Function_38_B1C4")

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
        "#5PHello, I came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PTio!\x01",
            "…… I have not gotten it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PHaha, I am going down the tension.\x02",
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
        "#12P#00006FSorry, something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PDisagreeable……\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FBut, Mr. Eoria ……\x01",
            "Nice as ever.\x02\x03",
            "#00304FAt this time, Tiio is giving up\x01",
            "Do not you change to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PNo, I'm feeling downright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FGosh ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FLa, Randy-senior … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHuh, it's a superb honorable crushing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FRandy is already\x01",
            "Learn freely.\x02\x03",
            "#00100FSorry, Mr. Lin.\x01",
            "I will talk about the request immediately\x01",
            "I'd like to ask …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5POh, let me explain.\x01",
            "It is a simple story though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWhat I would like to go out with\x01",
            "Our own training that is nothing else -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIn other words, with us and you\x01",
            "I want to make arrangements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWhat is meant to be …?\x01",
            "Is it fighting in the actual battle format?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBut why\x01",
            "Do you ask such a request now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5POh yeah, a while ago\x01",
            "It was because Hiyokko passed away?\x02",
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
        "#12P#00012FThere is no word to return indeed … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FYes, I'm getting stuck in my chest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWell, is not it okay?\x01",
            "Instead, now\x01",
            "I admit the power of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PThat's what we do\x01",
            "To the extent that you want to feel with your skin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PJust me and Rin's free time\x01",
            "Knowing overlapping\x01",
            "I thought it was only now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PTo Scott and Wenzel\x01",
            "It's bad, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, if I had two of them\x01",
            "More ridiculously\x01",
            "It seems to be getting.\x02\x03",
            "#00000FBut surely.\x01",
            "There are rare occasions like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FOw!\x01",
            "I definitely want to borrow your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWant to borrow yourself …?\x02\x03",
            "#10304FRandy says\x01",
            "I could seem to have another meaning though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10100FWhat does that mean … …\x02\x03",
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
            "#6P#00111FWajima …… no more\x01",
            "Can you avoid scratching?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHaha, apparently a new facebook\x01",
            "It seems to entertain me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PYeah yeah, I saw it\x01",
            "It seems that both of us can cope.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x12C, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10102FWell, whether it is equivalent or not\x01",
            "I do not have confidence indeed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHuh, it is a real honor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PSo, what do you do.\x01",
            "Can you accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah ….\x01",
            "I will do so if I can.\x02\x03",
            "#00000FHow are you going to place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5POh, as wide as it is\x01",
            "Do not get in the way of life\x01",
            "I am considering the entrance of the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PI also have permission from the village headowner\x01",
            "You can use it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PIf you are already ready\x01",
            "I want to start it even soon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PIs equipment and shopping okay?\x01",
            "I will wait for preparation if necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FI agree……\x02",
    )

    CloseMessageWindow()
    OP_29(0x75, 0x1, 0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Prepared, doing a matching]\x01",      # 0
            "【I will stop it】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE9A")

    ChrTalk(
        0x101,
        (
            "#12P#00000FBecause I am ready\x01",
            "Can I move at once?\x02\x03",
            "#00004FMeeting with two people,\x01",
            "I will be officially accepted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PHuhu, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PWell then, start training!\x02",
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
            "Quest 【Request for participation in hypocritical person training】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_BFDE")

    label("loc_BE9A")


    ChrTalk(
        0x101,
        (
            "#12P#00000FBecause there is something I want to prepare,\x01",
            "Can I have you wait?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5POh, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PAlso, if there is any other business\x01",
            "Even if you prioritize it separately\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5POriginally we also have free time\x01",
            "I only use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PAt that time, do not mind here\x01",
            "Because it will be slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOk, got it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BFDE")

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

    # Function_38_B1C4 end

    def Function_39_C036(): pass

    label("Function_39_C036")

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
        "#5PHi, Are you ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PMatching with us,\x01",
            "Can you accept it?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Prepared, doing a matching]\x01",      # 0
            "【I will stop it】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C2")

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, it's patched.\x01",
            "Can I move at once?\x02\x03",
            "Meeting with two people,\x01",
            "I will be officially accepted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PHuhu, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PWell then, start training!\x02",
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
            "Quest 【Request for participation in hypocritical person training】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C3B1")

    label("loc_C2C2")


    ChrTalk(
        0x101,
        (
            "#12P#00006FExcuse me……\x01",
            "It looks like it will take a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5POh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWell, if there are other things to do\x01",
            "Give priority to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PApart from us\x01",
            "You do not have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C3B1")

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

    # Function_39_C036 end

    def Function_40_C406(): pass

    label("Function_40_C406")

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
            "Hi guys, the support department.\x01",
            "Welcome to \"Tonrikotei\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Would you like to eat something today?\x01",
            "Or is it staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, today I am at work\x01",
            "I came ….\x02",
        )
    )

    CloseMessageWindow()
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
        0xA,
        (
            "Oh, that?\x01",
            "From Crossbell Communication Company\x01",
            "I have heard the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, immediately to you guys\x01",
            "My \"masterful omelet rice\"\x01",
            "I will treat you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, I'm counting on you master.\x02",
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
            "Lloyds ate takumi style omelet rice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00104FPu …\x01",
            "Well, after all this\x01",
            "Omurice is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, I think that it is really superb.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI was wrapped in fluffy eggs\x01",
            "Chicken rice's ketchup taste,\x01",
            "What is simple and nice.\x02\x03",
            "#00004FSurrounded by this wilderness\x01",
            "In Almorika village\x01",
            "I think it's a nice location … ….\x02\x03",
            "#00009FIf you come to Almorika village\x01",
            "I can not go back without eating this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, if you are told so far\x01",
            "I wonder why I'm embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHehe, the omelette here\x01",
            "It seems to be Lloyd's favorite … …\x02\x03",
            "You seem to be leaving the guide articles.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00306FWell, here also including the character of Master\x01",
            "I have to push it firmly.\x02\x03",
            "#00300FEven before I had a feast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I have responsibility\x01",
            "I will write it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hello, everyone\x01",
            "An article that will thrive\x01",
            "I have asked for you.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_CD04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_CD21")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_CD34")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_CD47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_CD64")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_CD77")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_CD94")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_CDA7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_CDC4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_CDD7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_CDF4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDF4")

    OP_29(0x80, 0x1, 0x7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEF7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEEE")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CEEE")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_CEF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFC8")
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

    label("loc_CFC8")

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

    # Function_40_C406 end

    def Function_41_D002(): pass

    label("Function_41_D002")

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
            "#00000FUm, I asked a little.\x01",
            "I'd like to ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Recently I am visiting the village\x01",
            "I asked about foreigners.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Oh, recently occasionally\x01",
            "That person who comes to stay at my place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, very polite\x01",
            "It is a person who can be likable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FPolite, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105Fby the way……\x01",
            "That person's name etc.\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, certainly ….\x01",
            "Was it \"Minnesity\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the guest list\x01",
            "It looks like he was signing that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F\"Minnesh\" or …\x01",
            "Huhu, tentatively the name is\x01",
            "It became obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FSo, about Mr. Minnes\x01",
            "Do you have anything to know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, what I talked a lot\x01",
            "Because there is nothing, I wonder if I can say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "ただ、部屋にDerrickくんを呼んで\x01",
            "It seems they are talking a couple of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I wonder what it is about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(With the son of the village head of the example\x01",
            "It seems like talking about talk … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Oh …… Anyway,\x01",
            "There is little information\x01",
            "It seems I got it. )\x02\x03",
            "#00000FThanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No problem, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Incidentally\x01",
            "I'm glad if you order me.\x02",
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

    # Function_41_D002 end

    def Function_42_D514(): pass

    label("Function_42_D514")

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
            "#00000FUm, I asked a little.\x01",
            "I'd like to ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Recently I am visiting the village\x01",
            "I asked about foreigners.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, that man?\x01",
            "It is a man with pretty eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F… …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everything, village honey\x01",
            "It seems that he liked it very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "'I surely,\x01",
            "I can pass in the continent! \"\x01",
            "… and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs it usual …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FTo tell from a conversation,\x01",
            "Is it a merchant or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I did not ask in detail\x01",
            "Probably not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As long as that owner of the eyes\x01",
            "You must be a man with a name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To my grandson at all\x01",
            "I would like to emulate him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FMake your arms feel anyway\x01",
            "I feel like a businessman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see……\x01",
            "I understood a lot.\x02\x03",
            "#00004FThanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, whenever you come again, yeah.\x02",
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

    # Function_42_D514 end

    def Function_43_D941(): pass

    label("Function_43_D941")

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
            "Gee\x01",
            "Did you mean lodging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "The room is now available.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Yes, if Mr. Gebal is\x01",
            "In Almorika village\x01",
            "If it is coming … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(The possibility that you are coming to the hotel tavern\x01",
            "It might be expensive. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUm, a bit\x01",
            "I'd like to ask …\x02\x03",
            "Here, a person called Gabaru\x01",
            "Have you not stayed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, Mr. Gebal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Recently I occasionally eat\x01",
            "You are a visiting customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FSometimes for a meal … ….?\x02\x03",
            "I am staying here\x01",
            "Is not that why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, that can not be.\x01",
            "I do not remember receiving it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I like my taste,\x01",
            "I was going from the city\x01",
            "I thought that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm……\x01",
            "It is realistic for fluke stone.\x01",
            "I feel like I will not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FOr …\x01",
            "Even relatives in Almorika village\x01",
            "Do you have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300Fif so,\x01",
            "Alm's already\x01",
            "It seems to be investigated, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_END)), "loc_DDCE")

    ChrTalk(
        0x101,
        "#00003Fperhaps……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#00001F…… Let's consult with the mayor once.\x01",
            "You might know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_DE45")

    label("loc_DDCE")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#00003FLet's investigate once.\x02\x03",
            "#00000FMaybe\x01",
            "There are places where you might hide yourself\x01",
            "It may be there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE45")

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

    # Function_43_D941 end

    def Function_44_DE9F(): pass

    label("Function_44_DE9F")

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
            "#11PGee\x01",
            "You guys are certainly the police\x01",
            "Was it a mission support section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PIt used to take care of me before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_E0CB")

    ChrTalk(
        0xD,
        (
            "#5POh, sure I wander into the old battlefield.\x01",
            "Were you looking for tourists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PSpeaking of which,\x01",
            "Even in the case of library books\x01",
            "You bothered me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012Fmy mother……\x01",
            "No, I do not care.\x02\x03",
            "#00000FRecently, what has changed\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E163")

    label("loc_E0CB")


    ChrTalk(
        0xD,
        (
            "#5POh, sure I wander into the old battlefield.\x01",
            "Were you looking for tourists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, I have noticed a long time ago.\x02\x03",
            "Recently, what has changed\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E163")


    ChrTalk(
        0xA,
        (
            "#11PThat's right.\x01",
            "This village is cheap\x01",
            "It's a peaceful thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIn the meantime,\x01",
            "Unfamiliar people\x01",
            "I guess I visited the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5POh, that red - grown big guy ……\x02",
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
        "#00105FA big red haired ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FDid you mean …\x01",
            "That redhead is\x01",
            "Is it the same color as my hair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh, that's right.\x01",
            "You certainly feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWith that red giant giant,\x01",
            "An active lady who was together with her\x01",
            "I think it was such a color of hair.\x02",
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
            "#00001F… … Um, let me hear it in detail\x01",
            "I'd like to ……\x01",
            "What are they doing in this village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PNo, ~ I always watched\x01",
            "It is because it is not.\x02",
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
            "Oh, by the grocery store\x01",
            "I saw you were shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Somehow, cheese, bacon, black bread or something\x01",
            "I seem to have bought a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That day it was a profit making\x01",
            "The old man in the rain was delighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIs that so……\x02",
    )

    CloseMessageWindow()

    def lambda_E58A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E58A)
    Sleep(50)

    def lambda_E59A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E59A)
    Sleep(50)

    def lambda_E5AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E5AA)
    Sleep(50)
    OP_93(0x109, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00001F…… \"Red constellation\"\x01",
            "I heard you were visiting Almorika village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAs far as I can talk\x01",
            "You seem to have come for food procurement.\x02\x03",
            "#10103FOnly things that seem to be effective for preservation\x01",
            "It seems I was buying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F… … For hunters,\x01",
            "Because securing food is the basis in the basics.\x02\x03",
            "When battles can happen,\x01",
            "Always maintain a perfect system …\x02\x03",
            "#00301FYatsu et al. Who are battle-ring hunters,\x01",
            "You should be thorough about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHuh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut the aim is really\x01",
            "I wonder if that is all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F… for the moment,\x01",
            "It is better to keep in mind\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E7F6():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E7F6)
    Sleep(50)

    def lambda_E806():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E806)
    Sleep(50)

    def lambda_E816():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E816)
    Sleep(50)

    def lambda_E826():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E826)
    Sleep(50)

    def lambda_E836():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E836)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00004F…… precious story\x01",
            "Thank you very much.\x02\x03",
            "#00000FIf there is something again\x01",
            "Please contact the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHmm, I do not understand somewhat\x01",
            "You also seem to be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell, come back at any time again.\x01",
            "Prepare delicious omelet rice\x01",
            "I'll be waiting.\x02",
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

    # Function_44_DE9F end

    def Function_45_E9A2(): pass

    label("Function_45_E9A2")

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
        "Oh, it's a big dog ~!\x02",
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

    def lambda_EC77():
        OP_93(0x15, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_EC77)
    Sleep(50)

    def lambda_EC87():
        OP_93(0x16, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_EC87)
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
        "everyone is……!\x02",
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
            "Oh …… Lloyd!\x02\x03",
            "Was good……\x01",
            "It was safe!\x02",
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
            "#00002F#12P……Haroldさん、\x01",
            "It is long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#12P#3C…… What is \"big dog\"?\x01",
            "Could it be about me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PHuhu, that's a nice name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10409F#12PAhaha, god wolves are also missing.\x02",
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
            "#03610F#11PLloyd's\x01",
            "Listen to the rumor that he was arrested\x01",
            "I was really worried.\x02\x03",
            "#03600FAs for anything as a deserter\x01",
            "I heard he was wanted, but …\x01",
            "It looks like it 's safe and it was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6Pmy mother……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03708F#11PUm, everyone at the other support department\x01",
            "How did it go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P……Unfortunately,\x01",
            "It is separated.\x02\x03",
            "#00208FAlso a detailed location\x01",
            "I do not know ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#03710F#11PIs that so … I am worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6P……Haroldさんたちは\x01",
            "When you are in a change, just village\x01",
            "You seem to have been visiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYeah ….\x01",
            "At first I wonder what happened,\x01",
            "I could not get your idea.\x02\x03",
            "#03608FI do not know the reason\x01",
            "Restrictions on movement of the highway are issued,\x01",
            "I can not go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#03700F#11PBut, to the people of the village really\x01",
            "I am indebted to you.\x02\x03",
            "The owner of the inn, until the blooms cool\x01",
            "Please tell me to stay … …\x02\x03",
            "#03709FCholineも、村の子供達と\x01",
            "It seems I got along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#03809F#5PCamilleくんやpulleyちゃんが\x01",
            "It plays a lot.\x02\x03",
            "Let's play dogs together next time ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#6P#3CHuh, I'll think about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03609F#11Pはは……Thank you very much.\x02\x03",
            "#03600FWell, that's why\x01",
            "I also help the village to give back\x01",
            "I am allowed to do it.\x02\x03",
            "#03604FHowever, sometimes it comes\x01",
            "Negotiations with Defense Forces\x01",
            "I will accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PNo, under this situation\x01",
            "It is a very important role.\x02\x03",
            "#00202FHaroldさんのような\x01",
            "If you are a veteran merchant, you also negotiate\x01",
            "I'm pretty accustomed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600F#11PWell, really a big deal\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x15)

    ChrTalk(
        0x15,
        (
            "#03605F#11PYes, while negotiating with the Defense Forces\x01",
            "I heard a story about it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAn interesting story …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PYes, anything around here\x01",
            "Unknown resistance force is\x01",
            "I heard he is lurking.\x02\x03",
            "#03601FThe troops of the defense force several times\x01",
            "It seems that it is on the raid.\x02",
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
        "#00011F#6PIs it true? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6POh … under this situation\x01",
            "Is there a human being who does such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PI do not know who it is … …\x01",
            "It is very useful information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6POh, it seems necessary to make sure.\x02\x03",
            "#00001FHaroldさん、抵抗勢力というのは\x01",
            "Where are you being witnessed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03610F#11PApparently, it is in the middle of the old road\x01",
            "In the vicinity of the Almora Battlefield\x01",
            "It seems to have been witnessed.\x02\x03",
            "#03601FDefense forces regularly\x01",
            "It seems to be patrolling … …\x01",
            "成果は上がっていないYou look like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CArmorika Battlefield ……\x01",
            "Once blood was blown several times,\x01",
            "Is the ground of the dressing that the cult has established as the headquarters?\x02\x03",
            "#01201FThere are also many hidden passageways in that ruin.\x01",
            "How to resist hidden resistance and power\x01",
            "It will be suitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PI do not know what is waiting ….\x01",
            "Are you ready to go and go?\x02",
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

    # Function_45_E9A2 end

    def Function_46_FA0E(): pass

    label("Function_46_FA0E")


    def lambda_FA13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FA13)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 73000, 0, -500, 2000, 0x0)
    Return()

    # Function_46_FA0E end

    def Function_47_FA57(): pass

    label("Function_47_FA57")


    def lambda_FA5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FA5C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -1000, 2000, 0x0)
    OP_95(0xFE, 73750, 0, -1000, 2000, 0x0)
    Return()

    # Function_47_FA57 end

    def Function_48_FAA0(): pass

    label("Function_48_FAA0")


    def lambda_FAA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FAA5)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, -500, 2000, 0x0)
    OP_95(0xFE, 75000, 0, -500, 2000, 0x0)
    Return()

    # Function_48_FAA0 end

    def Function_49_FAE9(): pass

    label("Function_49_FAE9")


    def lambda_FAEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FAEE)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
    OP_95(0xFE, 74250, 0, 0, 2000, 0x0)
    Return()

    # Function_49_FAE9 end

    SaveToFile()

Try(main)
