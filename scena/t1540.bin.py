from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1540.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1540",                  # 0
        "Cecil",                 # 1
        "Nurse Philia",         # 2
        "Martha director",             # 3
        "Nurse Shillon",           # 4
        "Nurse machine",         # 5
        "Doctor Doctor",       # 6
        "Professor Seyland",         # 7
        "hospitalized patient",               # 8
        "hospitalized patient",               # 9
        "hospitalized patient",               # 10
        "hospitalized patient",               # 11
        "hospitalized patient",               # 12
        "hospitalized patient",               # 13
        "hospitalized patient",               # 14
        "hospitalized patient",               # 15
        "hospitalized patient",               # 16
        "hospitalized patient",               # 17
        "hospitalized patient",               # 18
        "hospitalized patient",               # 19
        "Policeman",                   # 20
        "policewoman",                   # 21
        "Policeman",                   # 22
        "Policeman",                   # 23
        "Luganoff",               # 24
        "Jed",                 # 25
        "Huey",               # 26
        "Slash",             # 27
        "Dyson official",         # 28
        "Trainee Litton",         # 29
        "Trainee Nguyen",           # 30
        "hospitalized patient",               # 31
        "hospitalized patient",               # 32
        "hospitalized patient",               # 33
        "hospitalized patient",               # 34
        "hospitalized patient",               # 35
        "hospitalized patient",               # 36
        "hospitalized patient",               # 37
        "hospitalized patient",               # 38
    ))

    AddCharChip((
        "chr/ch05300.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "chr/ch29600.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch29300.itc",                   # 04
        "chr/ch44800.itc",                   # 05
        "apl/ch50133.itc",                   # 06
        "apl/ch50141.itc",                   # 07
        "apl/ch50135.itc",                   # 08
        "apl/ch50137.itc",                   # 09
        "apl/ch50139.itc",                   # 0A
        "apl/ch50143.itc",                   # 0B
        "apl/ch50132.itc",                   # 0C
        "apl/ch50141.itc",                   # 0D
        "apl/ch51538.itc",                   # 0E
        "apl/ch51540.itc",                   # 0F
        "chr/ch20200.itc",                   # 10
        "chr/ch29400.itc",                   # 11
        "chr/ch29500.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(110709,  0,       4294962976, 90,   389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(24610,   0,       680,     225,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(108930,  0,       1450,    45,   261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(110709,  0,       4294961657, 0,    261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(110709,  0,       4294962976, 90,   261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(110720,  0,       4294963057, 180,  261,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4294963296, 699,     52029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(4849,    699,     4294910326, 270,  453,  0x0, 0,   8,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(4294963146, 699,     4294910326, 270,  453,  0x0, 0,   9,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   10,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(4849,    699,     4294915236, 270,  453,  0x0, 0,   8,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(4294963146, 699,     4294915236, 270,  453,  0x0, 0,   11,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294963296, 699,     57029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(4294963296, 699,     52029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(4294963186, 400,     4294910326, 0,    469,  0x0, 0,   12,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(4849,    699,     4294910326, 270,  453,  0x0, 0,   10,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(4294963296, 699,     57029,   270,  453,  0x0, 0,   11,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(4294963296, 699,     52029,   270,  453,  0x0, 0,   13,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(4809,    400,     4294915337, 0,    469,  0x0, 0,   14,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(4809,    400,     4294910326, 0,    469,  0x0, 0,   15,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(4294963186, 400,     4294915236, 0,    469,  0x0, 0,   15,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(4294963186, 400,     4294910326, 0,    469,  0x0, 0,   14,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(103349,  0,       0,       90,   389,  0x0, 0,   16,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   43,  255,  0)
    DeclNpc(4294963296, 699,     52029,   270,  453,  0x0, 0,   9,   0,   255, 255, 0,   44,  255,  0)
    DeclNpc(4849,    699,     4294910326, 270,  453,  0x0, 0,   8,   0,   255, 255, 0,   45,  255,  0)
    DeclNpc(4294963146, 699,     4294910326, 270,  453,  0x0, 0,   7,   0,   255, 255, 0,   46,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  453,  0x0, 0,   7,   0,   255, 255, 0,   47,  255,  0)
    DeclNpc(4294963296, 699,     57029,   270,  453,  0x0, 0,   6,   0,   255, 255, 0,   48,  255,  0)
    DeclNpc(4849,    699,     4294910326, 270,  453,  0x0, 0,   10,  0,   255, 255, 0,   49,  255,  0)
    DeclNpc(4294963146, 699,     4294915236, 270,  453,  0x0, 0,   9,   0,   255, 255, 0,   50,  255,  0)

    DeclEvent(0x0000, 0, 53,  8.779999732971191,     5.800000190734863,     -1.0,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -2.926666736602783,    -2.9000000953674316,   0.20000001788139343,   1.0])

    DeclActor(23500,   0,       4294966466, 1500,    24610,   1500,    680,     0x007E, 0,  5,  0x0000)

    ChipFrameInfo(1684, 0)                                       # 0

    ScpFunction((
        "Function_0_694",          # 00, 0
        "Function_1_744",          # 01, 1
        "Function_2_DF4",          # 02, 2
        "Function_3_133B",         # 03, 3
        "Function_4_1801",         # 04, 4
        "Function_5_1CCA",         # 05, 5
        "Function_6_1CCE",         # 06, 6
        "Function_7_2C3A",         # 07, 7
        "Function_8_3DC6",         # 08, 8
        "Function_9_3ECD",         # 09, 9
        "Function_10_3F82",        # 0A, 10
        "Function_11_4464",        # 0B, 11
        "Function_12_45F4",        # 0C, 12
        "Function_13_47EE",        # 0D, 13
        "Function_14_4BE9",        # 0E, 14
        "Function_15_5675",        # 0F, 15
        "Function_16_5759",        # 10, 16
        "Function_17_5ACB",        # 11, 17
        "Function_18_5C54",        # 12, 18
        "Function_19_5D5E",        # 13, 19
        "Function_20_5FAD",        # 14, 20
        "Function_21_6195",        # 15, 21
        "Function_22_63FB",        # 16, 22
        "Function_23_668B",        # 17, 23
        "Function_24_6816",        # 18, 24
        "Function_25_6B36",        # 19, 25
        "Function_26_6BA5",        # 1A, 26
        "Function_27_6C19",        # 1B, 27
        "Function_28_6C64",        # 1C, 28
        "Function_29_6D05",        # 1D, 29
        "Function_30_6E62",        # 1E, 30
        "Function_31_6FA1",        # 1F, 31
        "Function_32_70C8",        # 20, 32
        "Function_33_715A",        # 21, 33
        "Function_34_71D8",        # 22, 34
        "Function_35_72F7",        # 23, 35
        "Function_36_74A1",        # 24, 36
        "Function_37_74E4",        # 25, 37
        "Function_38_756B",        # 26, 38
        "Function_39_78C4",        # 27, 39
        "Function_40_79C1",        # 28, 40
        "Function_41_7AB8",        # 29, 41
        "Function_42_7D09",        # 2A, 42
        "Function_43_802E",        # 2B, 43
        "Function_44_80C3",        # 2C, 44
        "Function_45_81F5",        # 2D, 45
        "Function_46_8305",        # 2E, 46
        "Function_47_84CD",        # 2F, 47
        "Function_48_85DA",        # 30, 48
        "Function_49_86C4",        # 31, 49
        "Function_50_87A7",        # 32, 50
        "Function_51_88C4",        # 33, 51
        "Function_52_88CB",        # 34, 52
        "Function_53_9805",        # 35, 53
        "Function_54_9868",        # 36, 54
    ))


    def Function_0_694(): pass

    label("Function_0_694")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6CC"),
        (1, "loc_6D8"),
        (2, "loc_6E4"),
        (3, "loc_6F0"),
        (4, "loc_6FC"),
        (5, "loc_708"),
        (6, "loc_714"),
        (SWITCH_DEFAULT, "loc_720"),
    )


    label("loc_6CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_6FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_708")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_714")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_720")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_743")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_72C")

    label("loc_743")

    Return()

    # Function_0_694 end

    def Function_1_744(): pass

    label("Function_1_744")

    SetChrChipByIndex(0xF, 0x6)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x6)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0x8)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrChipByIndex(0x16, 0xB)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x9)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrChipByIndex(0x18, 0x7)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrChipByIndex(0x19, 0xC)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0xA)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0x7)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1C, 0xB)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1D, 0x9)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    SetChrChipByIndex(0x1E, 0xD)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x26, 0x6)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    SetChrChipByIndex(0x27, 0x9)
    SetChrSubChip(0x27, 0x0)
    EndChrThread(0x27, 0x0)
    SetChrBattleFlags(0x27, 0x4)
    SetChrChipByIndex(0x28, 0x8)
    SetChrSubChip(0x28, 0x0)
    EndChrThread(0x28, 0x0)
    SetChrBattleFlags(0x28, 0x4)
    SetChrChipByIndex(0x29, 0x7)
    SetChrSubChip(0x29, 0x0)
    EndChrThread(0x29, 0x0)
    SetChrBattleFlags(0x29, 0x4)
    SetChrChipByIndex(0x2A, 0x7)
    SetChrSubChip(0x2A, 0x0)
    EndChrThread(0x2A, 0x0)
    SetChrBattleFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2B, 0x6)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    SetChrChipByIndex(0x2C, 0xA)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    SetChrChipByIndex(0x2D, 0x9)
    SetChrSubChip(0x2D, 0x0)
    EndChrThread(0x2D, 0x0)
    SetChrBattleFlags(0x2D, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_92A")
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_DDB")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9D3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 102790, 0, 3080, 0)
    SetChrPos(0xA, 23790, 0, 1610, 135)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, 24610, 0, 680, 315)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_995")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_995")

    SetChrPos(0xD, 3970, 0, -55460, 135)
    ClearChrFlags(0x2C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x2C, 0x10)

    label("loc_9BF")

    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_DDB")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A30")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 24840, 0, -17230, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 24830, 0, -18620, 0)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    Jump("loc_DDB")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A97")
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 3490, 0, 55460, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    SetChrFlags(0x24, 0x10)
    SetChrFlags(0x26, 0x10)

    label("loc_A63")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    Jump("loc_DDB")

    label("loc_A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 110700, 0, -3400, 90)

    label("loc_AC7")

    SetChrPos(0xD, -3950, 0, -55500, 180)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -10, 0, 53970, 0)
    Jump("loc_DDB")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BA5")
    SetChrPos(0xA, -4100, 0, 55470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B44")
    SetChrFlags(0xA, 0x10)

    label("loc_B44")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, -3950, 0, -55500, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    SetChrFlags(0x17, 0x10)

    label("loc_B8C")

    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_DDB")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C66")
    SetChrPos(0xA, 110710, 0, -4320, 180)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xB, 110710, 0, -5640, 0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 1390, 0, 52480, 315)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C24")
    ClearChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    ClearChrFlags(0xB, 0x10)

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    SetChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x1)

    label("loc_C37")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 3490, 0, -53570, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C61")
    SetChrFlags(0x24, 0x10)

    label("loc_C61")

    Jump("loc_DDB")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CCF")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 110650, 0, -5010, 90)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 26640, 0, -19370, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 6700, 0, 4970, 180)
    Jump("loc_DDB")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D3A")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -540, 0, 53560, 315)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    SetChrPos(0x24, -3940, 0, -55480, 180)
    Jump("loc_DDB")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D95")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, 24930, 0, -26050, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D90")
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 30220, 0, -21990, 315)

    label("loc_D90")

    Jump("loc_DDB")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrPos(0xB, -3950, 0, 53530, 180)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_DDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF3")
    ClearScenarioFlags(0x25, 1)
    Call(0, 51)

    label("loc_DF3")

    Return()

    # Function_1_744 end

    def Function_2_DF4(): pass

    label("Function_2_DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E06")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FE4")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1026")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1068")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10AA")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_10AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1120")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1196")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11D8")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_11D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_121A")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_125C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_129E")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_12DB")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12DB")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1317")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1317")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133A")
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x4, 0x0, 0x36)

    label("loc_133A")

    Return()

    # Function_2_DF4 end

    def Function_3_133B(): pass

    label("Function_3_133B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1359")
    Call(0, 4)
    Jump("loc_1494")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140A")

    ChrTalk(
        0x8,
        (
            "#01304FMembers of the Special Affairs Support Division\x01",
            "Now it's all together, surely\x01",
            "You should be able to solve a series of incidents.\x02\x03",
            "#01300FI will be cheering here.\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1494")

    label("loc_140A")


    ChrTalk(
        0x8,
        (
            "#01304FHuhu, if you decide so\x01",
            "I have to work hard at the hospital work too.\x02\x03",
            "#01300FSurely the goddess is watching.\x01",
            "Good luck with you too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_17FD")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_153C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(
        0x8,
        (
            "#01300FTo the section chief and Kaea,\x01",
            "Please say hello to me.\x02\x03",
            "It's a tough situation ….\x01",
            "Let's keep on each other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_1537")

    Jump("loc_17FD")

    label("loc_153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_154A")
    Jump("loc_17FD")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1558")
    Jump("loc_17FD")

    label("loc_1558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1756")

    ChrTalk(
        0x8,
        (
            "#01308FIn the case of Shizuku's surgery,\x01",
            "The atmosphere inside the hospital is very\x01",
            "It's getting dark.\x02\x03",
            "#01300FBut this is the time\x01",
            "Our nurse smile\x01",
            "I have to show it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSurely, that's right.\x01",
            "We also have a smile on Ka'a\x01",
            "I feel like being saved … ….\x02\x03",
            "#00009FIf Cecil's older sister smiles\x01",
            "Patients will be readily available\x01",
            "I think I'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, I'm sure I am anxious\x01",
            "It will be blown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01309FHehe, Thank you.\x02\x03",
            "#01300FShizuoka is also positive.\x01",
            "We have to be firm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D3")

    label("loc_1756")


    ChrTalk(
        0x8,
        (
            "#01300FWhen it is dark,\x01",
            "You have to show me a smile.\x02\x03",
            "It also helps to relieve the patient's anxiety\x01",
            "It is our duty as a nurse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_17FD")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17E6")
    Jump("loc_17FD")

    label("loc_17E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17F4")
    Jump("loc_17FD")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_17FD")

    label("loc_17FD")

    TalkEnd(0xFE)
    Return()

    # Function_3_133B end

    def Function_4_1801(): pass

    label("Function_4_1801")

    EventBegin(0x0)
    Fade(500)
    OP_68(102280, 1100, 1850, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18970, 0)
    SetChrPos(0x101, 102320, 0, 1060, 356)
    SetChrPos(0x102, 103040, 0, 420, 356)
    SetChrPos(0x103, 101120, 0, 850, 41)
    SetChrPos(0x104, 104270, 0, 1230, 311)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18B8")
    SetChrPos(0x109, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_18E3")

    label("loc_18B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18E3")
    SetChrPos(0x105, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_18E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_194C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1921")
    SetChrPos(0x105, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_194C")

    label("loc_1921")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_194C")
    SetChrPos(0x109, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_194C")

    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P#01305FWell, Lloyd's … …!\x02\x03",
            "#01309FHuhu, members of the Special Affairs Support Division\x01",
            "Everyone seems to have got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, at last.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A21")

    ChrTalk(
        0x105,
        (
            "#12P#10402FHuh, your older sister\x01",
            "Thanks for your support.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A21")


    ChrTalk(
        0x102,
        (
            "#12P#00100FI'm sorry to cause you\x01",
            "Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01300FEllie … …. Everyone\x01",
            "It seems I had a lot of hardship.\x02\x03",
            "#01304FHuhu, but why?\x02\x03",
            "#01302FYour bonds are better than before\x01",
            "I feel deepening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, to finish this far\x01",
            "It's been a tough time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FA sense of accomplishment as well.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BB2")

    ChrTalk(
        0x109,
        (
            "#12P#10112FHaha ……\x01",
            "There are still a lot of things to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")


    ChrTalk(
        0x8,
        (
            "#5P#01304FIt seems that there will still be hard times to continue ……\x02\x03",
            "#01300FIf you guys surely,\x01",
            "You should be able to solve this series of incidents.\x02\x03",
            "#01309FHuhu, do your best, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAh……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1AC, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 102700, 0, 940, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1CA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CBC")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1CBC")

    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_4_1801 end

    def Function_5_1CCA(): pass

    label("Function_5_1CCA")

    Call(0, 6)
    Return()

    # Function_5_1CCA end

    def Function_6_1CCE(): pass

    label("Function_6_1CCE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC9")

    ChrTalk(
        0x9,
        (
            "To make such a tree appear,\x01",
            "And unexpectedly\x01",
            "It has become … ~ ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From the president to the patient\x01",
            "Keep calm so as not to give you anxiety\x01",
            "It is said that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha, not very, but\x01",
            "I can not calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4E")

    label("loc_1DC9")


    ChrTalk(
        0x9,
        (
            "Oh, Cecil-senpai\x01",
            "To see that big tree\x01",
            "I went to a rest area in the premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha, seniors calm down\x01",
            "It's awesome ~ is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4E")

    Jump("loc_2C36")

    label("loc_1E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F00")

    ChrTalk(
        0x9,
        (
            "I can not get back to the city\x01",
            "To hospitalized patients and outpatients\x01",
            "It is where I correspond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As this happened in the city,\x01",
            "It seems that this situation will continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C36")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF2")

    ChrTalk(
        0x9,
        (
            "Donovan's recovery\x01",
            "It is pretty good and soon\x01",
            "I think that you can also leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, Mr. Ilya\x01",
            "Even with strong patient rehab\x01",
            "I do not know whether to cure it completely ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do your best.\x01",
            "I hope I can resurrect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2094")

    label("loc_1FF2")


    ChrTalk(
        0x9,
        (
            "Mr. Ilya\x01",
            "Even with strong patient rehab\x01",
            "I do not know if I will recover … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Still, hope that may be nice\x01",
            "It makes me feel\x01",
            "It is terrible place of Mr. Iria.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2094")

    Jump("loc_2C36")

    label("loc_2099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_219A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0x9,
        (
            "Iria and Mr. Donovan's\x01",
            "Consciousness came back ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Recently just something noisy\x01",
            "To be honest, I was depressed, but ….\x01",
            "It was nice to have a bright topic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2195")

    label("loc_214F")


    ChrTalk(
        0x9,
        (
            "Iria and Mr. Donovan's\x01",
            "Consciousness is back,\x01",
            "It was really good ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2195")

    Jump("loc_2C36")

    label("loc_219A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    ChrTalk(
        0x9,
        (
            "The intensive care unit in the research building\x01",
            "The guards are housed\x01",
            "I am there but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was hurt by harsh injuries,\x01",
            "It will take time to discharge from the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Up to now, various patients\x01",
            "I have been hospitalized,\x01",
            "Indeed I want to cover my eyes ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2335")

    label("loc_22A6")


    ChrTalk(
        0x9,
        (
            "Up to now, various patients\x01",
            "I have been hospitalized but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am in an intensive care unit\x01",
            "For injuries of the guards,\x01",
            "Indeed I want to cover my eyes ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_2C36")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_245E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")

    ChrTalk(
        0x9,
        (
            "Also correspondence of yesterday's train accident\x01",
            "It finally calmed down\x01",
            "Is not it feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "(Kuuuuu … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……by the way,\x01",
            "I did not eat it at Roku.\x01",
            "I'm hungry now ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2459")

    label("loc_23F5")


    ChrTalk(
        0x9,
        (
            "I am busy,\x01",
            "I did not eat it at Roku.\x01",
            "I'm hungry now ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Later I'm going to have lunch.\x02",
    )

    CloseMessageWindow()

    label("loc_2459")

    Jump("loc_2C36")

    label("loc_245E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2591")

    ChrTalk(
        0x9,
        (
            "Professor Seyland,\x01",
            "A technique to cure Shizuku's eyes\x01",
            "It seems that he is rethinking newly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At first I thought I was depressed\x01",
            "It was hard to make a voice ……\x01",
            "You already switched your head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cool at all times\x01",
            "Mental power that can act reasonably …\x01",
            "As expected, I feel like a professor ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263B")

    label("loc_2591")


    ChrTalk(
        0x9,
        (
            "When it did not go well,\x01",
            "It's time to change your head soon.\x01",
            "It is surprisingly difficult, is not it ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cool at all times\x01",
            "Mental power that can act reasonably …\x01",
            "It is truly Professor Seyland ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263B")

    Jump("loc_2C36")

    label("loc_2640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2742")

    ChrTalk(
        0x9,
        (
            "By the operation of Shizuku-chan\x01",
            "When I was down, suddenly to the chief\x01",
            "I was beat up on the buttocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haa ~ I was surprised … …\x01",
            "I'm still burning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But thanks, sort of\x01",
            "Dark feelings blew away.\x01",
            "I hope it does not work today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F0")

    label("loc_2742")


    ChrTalk(
        0x9,
        (
            "Thanks to being beaten up, somehow\x01",
            "Dark feelings blew away.\x01",
            "As expected it is the president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… But a little more\x01",
            "Even though I could have done it.\x01",
            "The buttocks will tickle still ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F0")

    Jump("loc_2C36")

    label("loc_27F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(
        0x9,
        (
            "I am happy to leave Michael's discharge,\x01",
            "I'm getting sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Especially Shizuku-chan\x01",
            "My age is close and I am a good friend,\x01",
            "I guess I'm lonely alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C36")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2978")

    ChrTalk(
        0x9,
        (
            "The unveiling ceremony of today's Orkis Tower,\x01",
            "I also wanted to go see it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, recently it is quite\x01",
            "I can not take a day off ~ …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have no choice but to be busy,\x01",
            "I want to go to play soon ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A11")

    label("loc_2978")


    ChrTalk(
        0x9,
        (
            "Also this time the alkane shell performance,\x01",
            "Do you arrange tickets for buying?\x01",
            "Even I am doubtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have no choice but to be busy,\x01",
            "I want to go to play soon ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A11")

    Jump("loc_2C36")

    label("loc_2A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDA")

    ChrTalk(
        0x9,
        (
            "Hello, this is\x01",
            "It's a nurse station ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Oh!\x01",
            "Randy to your brother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FFather, Philia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Flong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is true!\x01",
            "Hehe, but she looks fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Randy, sometime soon\x01",
            "I will leave the schedule open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOkay Okay,\x01",
            "Let's do it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSenior, that kind of thing again\x01",
            "I feel like I promised … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FHa, boy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 5)
    Jump("loc_2C36")

    label("loc_2BDA")


    ChrTalk(
        0x9,
        (
            "Someday, everyone\x01",
            "It is something you want to do jointly ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At that time my brother,\x01",
            "You are coming!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C36")

    TalkEnd(0x9)
    Return()

    # Function_6_1CCE end

    def Function_7_2C3A(): pass

    label("Function_7_2C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C63")
    Call(0, 52)
    Return()

    label("loc_2C63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D28")

    ChrTalk(
        0xFE,
        (
            "Outpatient resumed,\x01",
            "I have been busy for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it was not accepted so far,\x01",
            "It seems that a lot of outpatient visits have come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, put your fight\x01",
            "I suppose that I will encourage work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DAC")

    label("loc_2D28")


    ChrTalk(
        0xFE,
        (
            "Mr. Harold's missing supplies\x01",
            "I asked for it,\x01",
            "Patient acceptance system is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm supposed to put in a spirit and encourage my work.\x02",
    )

    CloseMessageWindow()

    label("loc_2DAC")

    Jump("loc_3DC2")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2E68")

    ChrTalk(
        0xFE,
        (
            "I am at the accommodation\x01",
            "Because I will go to a foreign guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then Philia,\x01",
            "An explanation to hospitalized patients\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        "Yes, I understand~.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_3DC2")

    label("loc_2E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F76")

    ChrTalk(
        0xFE,
        (
            "However, only seriously ill / seriously injured\x01",
            "I can not convey it to the hospital,\x01",
            "It's a no-brainer rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand from the appearance\x01",
            "It is natural that there are injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Patients who can be helped by early treatment\x01",
            "If you can not help it,\x01",
            "I really do not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FF9")

    label("loc_2F76")


    ChrTalk(
        0xFE,
        (
            "Only seriously ill / seriously injured\x01",
            "I can not convey it to the hospital,\x01",
            "It's a no-brainer rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter\x01",
            "Do you know the place there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF9")

    Jump("loc_3DC2")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318F")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio-chan ……\x01",
            "You are leaving the hospital, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes … Martha,\x01",
            "Thank you for everything.\x02\x03",
            "#00204FIn the past, when returning when hospitalized\x01",
            "I wish I could have done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, it's an old story, and such a thing\x01",
            "You do not have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can come and visit us any time ……\x01",
            "Please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHuhu, yes.\x01",
            "I certainly will.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_323C")

    label("loc_318F")


    ChrTalk(
        0xFE,
        (
            "To Tio is the machine of the hospital\x01",
            "I had a lot of help,\x01",
            "I enjoyed talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can come and visit us any time ……\x01",
            "Please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    Jump("loc_3DC2")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A9")

    ChrTalk(
        0xFE,
        (
            "We, medical staff,\x01",
            "The opportunity to see people's death\x01",
            "It is natural as a matter of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, like me and the professors\x01",
            "As long as I do it, to each person's death\x01",
            "I do not even have tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this raid incident ……\x01",
            "Thinking of the many victims,\x01",
            "An angry man will come up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To lightly steal people's lives ……\x01",
            "It is absolutely unacceptable behavior.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_342E")

    label("loc_33A9")


    ChrTalk(
        0xFE,
        (
            "While doctors help many lives,\x01",
            "Take a person's life lightly\x01",
            "There are guys like hunters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… People say,\x01",
            "It is a really deep creature.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342E")

    Jump("loc_3DC2")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344E")
    Call(0, 8)
    Jump("loc_34CE")

    label("loc_344E")


    ChrTalk(
        0xFE,
        (
            "Well, also seeing the performance of the alkane shell\x01",
            "It is the race of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanking the goddess for saving,\x01",
            "I have to get rid of my injuries right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CE")

    Jump("loc_3DC2")

    label("loc_34D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_361C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F8")
    Call(0, 9)
    Jump("loc_3553")

    label("loc_34F8")


    ChrTalk(
        0xFE,
        "Even if I say such a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking of your mistakes so far\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3553")

    Jump("loc_3617")

    label("loc_3558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")

    ChrTalk(
        0xFE,
        (
            "You bother, bother me\x01",
            "I was saved because they came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am this child\x01",
            "Because I have to preach,\x01",
            "See you next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3617")

    label("loc_35DD")


    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "Looking after Shiron\x01",
            "It's really tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3617")

    Jump("loc_3DC2")

    label("loc_361C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3757")

    ChrTalk(
        0xFE,
        (
            "Everyone, this guy as well\x01",
            "Their spirit is missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's because of that Shizuku-chan\x01",
            "I fully understand your feelings.\x01",
            "Everyone seems to be depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, to us\x01",
            "I have a depressed face,\x01",
            "Other patients will be worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must show my energy when I do like this.\x01",
            "I think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D5")

    label("loc_3757")


    ChrTalk(
        0xFE,
        (
            "Everyone, this guy as well\x01",
            "You can not feel depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm fine with fine sky.\x01",
            "See, you are doing well!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_3DC2")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Somewhat so ……!\x01",
            "What is there\x01",
            "Is not it Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is after a long absence!\x01",
            "Have you made doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FTio is\x01",
            "You know him, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, when I was in the hospital long ago\x01",
            "I had something to take care of with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, as a nurse\x01",
            "I do not do anything serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police 's job will be hard work,\x01",
            "Take care of yourself\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FYes, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 4)
    Jump("loc_3A5E")

    label("loc_39CA")


    ChrTalk(
        0xFE,
        (
            "As I said before,\x01",
            "Tio really\x01",
            "I became a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police 's job will be hard work,\x01",
            "Take care of yourself\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5E")

    Jump("loc_3DC2")

    label("loc_3A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7E")

    ChrTalk(
        0xFE,
        (
            "Cecil against any opponent\x01",
            "Divided, with consideration\x01",
            "You can touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems normal,\x01",
            "There are not many people that can do it.\x01",
            "I think that it is a good talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, that girl\x01",
            "I went to the nurse's way\x01",
            "It may be a goddess' s thoughts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C1C")

    label("loc_3B7E")


    ChrTalk(
        0xFE,
        (
            "Compassion for the patients\x01",
            "I can give you peace of mind.\x01",
            "Cecil's good talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, that girl\x01",
            "I went to the nurse's way\x01",
            "It may be a goddess' s thoughts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1C")

    Jump("loc_3DC2")

    label("loc_3C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D54")

    ChrTalk(
        0xFE,
        (
            "Professor Seyland,\x01",
            "It's pretty much in Remiferia\x01",
            "A well-known person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having a doctorate in the field of medicine,\x01",
            "It is said that it is also deeply connected with the great public building.\x01",
            "Well, you can say that the identity is certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More than that, Athaa\x01",
            "I liked the attitude of the spirit.\x01",
            "The woman at this time must be ah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DC2")

    label("loc_3D54")


    ChrTalk(
        0xFE,
        (
            "Well, Professor Seyland\x01",
            "He plays the ball\x01",
            "I like the attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The woman at this time must be ah.\x02",
    )

    CloseMessageWindow()

    label("loc_3DC2")

    TalkEnd(0xFE)
    Return()

    # Function_7_2C3A end

    def Function_8_3DC6(): pass

    label("Function_8_3DC6")

    OP_4B(0xA, 0xFF)
    OP_4B(0x17, 0xFF)

    ChrTalk(
        0x17,
        (
            "Practice alkane shell\x01",
            "Although I came to see it,\x01",
            "There are train accidents and the like …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Wow, that's too bad ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, by the way, tomorrow\x01",
            "It was a renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, it is the kind of living thing.\x01",
            "To the goddess that I was saved\x01",
            "I must thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x17, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x17, 0xFF)
    Return()

    # Function_8_3DC6 end

    def Function_9_3ECD(): pass

    label("Function_9_3ECD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Totally you are a child … …\x01",
            "How many times make the same mistake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, that's why\x01",
            "I told you to do ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The mistake is happening\x01",
            "It is a mistake!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_3ECD end

    def Function_10_3F82(): pass

    label("Function_10_3F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FAB")
    Call(0, 52)
    Return()

    label("loc_3FAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC9")
    Call(0, 12)
    Jump("loc_400E")

    label("loc_3FC9")


    ChrTalk(
        0xFE,
        (
            "Hey, I made a mistake because it looked like.\x01",
            "When you look closely it is not the same size.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400E")

    Jump("loc_4460")

    label("loc_4013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402E")
    Call(0, 12)
    Jump("loc_4070")

    label("loc_402E")


    ChrTalk(
        0xFE,
        (
            "Bagio in the city and\x01",
            "Dad, mothers are\x01",
            "I wonder if it will be okay ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4070")

    Jump("loc_4460")

    label("loc_4075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4083")
    Jump("loc_4460")

    label("loc_4083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4091")
    Jump("loc_4460")

    label("loc_4091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417C")

    ChrTalk(
        0xFE,
        (
            "…… So much patient\x01",
            "It is the first time I saw that it was brought in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone looks so painful …\x01",
            "Ever since that I'm kind of alone\x01",
            "I got scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today too for mefa-chan\x01",
            "Let's stay together …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4211")

    label("loc_417C")


    ChrTalk(
        0xFE,
        (
            "…… So much patient\x01",
            "It was the first time I saw that it was brought in,\x01",
            "I got scared somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today too for mefa-chan\x01",
            "Let's stay together …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4211")

    Jump("loc_4460")

    label("loc_4216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4224")
    Jump("loc_4460")

    label("loc_4224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_442A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4249")
    Call(0, 9)
    Jump("loc_429C")

    label("loc_4249")


    ChrTalk(
        0xFE,
        (
            "So, surely something\x01",
            "It is a mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hin, please believe ~!\x02",
    )

    CloseMessageWindow()

    label("loc_429C")

    Jump("loc_4425")

    label("loc_42A1")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AB")

    ChrTalk(
        0xFE,
        (
            "Fly, a strap of a basket of ….\x01",
            "It was nice to receive ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FBagger is good, is not it?\x01",
            "I am also a favorite.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I see\x01",
            "Right ~, it's cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "…… Kolat, are you listening? Is it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TurnDirection(0xFE, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_4421")

    label("loc_43AB")


    ChrTalk(
        0xFE,
        (
            "Mr. Martha is also a horror,\x01",
            "Please look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bag with straps,\x01",
            "It is cute ~ is it ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Do you know?\x02",
    )

    CloseMessageWindow()

    label("loc_4421")

    OP_4C(0xA, 0xFF)

    label("loc_4425")

    Jump("loc_4460")

    label("loc_442A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4438")
    Jump("loc_4460")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4446")
    Jump("loc_4460")

    label("loc_4446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4454")
    Jump("loc_4460")

    label("loc_4454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4460")
    Call(0, 11)

    label("loc_4460")

    TalkEnd(0xFE)
    Return()

    # Function_10_3F82 end

    def Function_11_4464(): pass

    label("Function_11_4464")

    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x10, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459C")

    ChrTalk(
        0xB,
        "Huh, let's get dripin ~ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Mr. nurse,\x01",
            "I wonder if it will be OK today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I also made a mistake in stabbing place,\x01",
            "When puff and blood comes out ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh dear, what we are going through\x01",
            "I just got crazy at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, please feel at ease.\x01",
            "Probably absolutely OK!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "(Fu, I am too anxious … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_45EB")

    label("loc_459C")


    ChrTalk(
        0xB,
        (
            "……that?\x01",
            "I seem to have forgotten the injection needle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Okay, I will ask you a nurse ……\x02",
    )

    CloseMessageWindow()

    label("loc_45EB")

    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_11_4464 end

    def Function_12_45F4(): pass

    label("Function_12_45F4")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46EE")

    ChrTalk(
        0xC,
        (
            "Then Shirone, hand it out\x01",
            "I'm going to inspect the hospitalized patients!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeah, Meifa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I have a thermometer! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha ♪ I'm here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Soret you have,\x01",
            "It's not a thermometer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "… … Huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E2")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_47E2")

    ChrTalk(
        0xB,
        (
            "Meifa,\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I am a bit scared ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It seems like there was a big movement in town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But do not worry.\x01",
            "Now what we can do\x01",
            "Because you only have to do with chitin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, yeah …!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_47E2")

    SetScenarioFlags(0x3, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_45F4 end

    def Function_13_47EE(): pass

    label("Function_13_47EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_484E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480C")
    Call(0, 12)
    Jump("loc_4849")

    label("loc_480C")


    ChrTalk(
        0xFE,
        (
            "Everything is different at all!\x01",
            "…… Completely, this girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4849")

    Jump("loc_4BE5")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_48DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4869")
    Call(0, 12)
    Jump("loc_48D5")

    label("loc_4869")


    ChrTalk(
        0xFE,
        (
            "There was a big movement\x01",
            "I certainly would like to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now what we can do\x01",
            "It is important to do with chitin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D5")

    Jump("loc_4BE5")

    label("loc_48DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_48E8")
    Jump("loc_4BE5")

    label("loc_48E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_48F6")
    Jump("loc_4BE5")

    label("loc_48F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C4")

    ChrTalk(
        0xFE,
        (
            "Children put in room 202,\x01",
            "At first I was very strong,\x01",
            "After a while I feel depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it is not only due to injury,\x01",
            "I wonder what happened in the town …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A38")

    label("loc_49C4")


    ChrTalk(
        0xFE,
        (
            "By the way, recently, Shiron is what\x01",
            "She seems to be frightened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, we are going\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A38")

    Jump("loc_4BE5")

    label("loc_4A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A4B")
    Jump("loc_4BE5")

    label("loc_4A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A59")
    Jump("loc_4BE5")

    label("loc_4A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A67")
    Jump("loc_4BE5")

    label("loc_4A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A75")
    Jump("loc_4BE5")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B54")

    ChrTalk(
        0xFE,
        (
            "Shilon's guy, during this\x01",
            "It was sunny on the rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Moreover, on the dried sheets\x01",
            "I looked happy to wrap up … …\x01",
            "It is impossible really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, I do not feel pretty.\x01",
            "Do the same thing again … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BD7")

    label("loc_4B54")


    ChrTalk(
        0xFE,
        (
            "Shilon's guy, during this\x01",
            "It was sunny on the rooftop.\x01",
            "Sheets will also get dirty ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… just in case, later\x01",
            "Do you go to see the state?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    Jump("loc_4BE5")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BE5")

    label("loc_4BE5")

    TalkEnd(0xFE)
    Return()

    # Function_13_47EE end

    def Function_14_4BE9(): pass

    label("Function_14_4BE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CDD")

    ChrTalk(
        0xFE,
        (
            "After going round once a while\x01",
            "Surgery is also included.\x01",
            "…… Hello, I'm busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, no matter where,\x01",
            "What we should do is not changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Helping the patient in front of me … …\x01",
            "That is the job of a doctor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D63")

    label("loc_4CDD")


    ChrTalk(
        0xFE,
        (
            "Whatever happens, no matter where,\x01",
            "What we should do is not changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Helping the patient in front of me … …\x01",
            "That is the job of a doctor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D63")

    Jump("loc_5671")

    label("loc_4D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D83")
    Call(0, 15)
    Jump("loc_4DBE")

    label("loc_4D83")


    ChrTalk(
        0xFE,
        (
            "Our hospital staff is excellent.\x01",
            "Please do not worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBE")

    Jump("loc_5671")

    label("loc_4DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4DD4")
    Call(0, 41)
    Jump("loc_5671")

    label("loc_4DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF7")

    ChrTalk(
        0xFE,
        (
            "Police officers who were hospitalized\x01",
            "Young people in the bad group,\x01",
            "He was already discharged from the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Originally, for a while after discharge\x01",
            "I'd like to see a hospital visit ……\x01",
            "I can not do it under the travel restrictions of the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Irresponsible conduct as a doctor\x01",
            "This situation that will be forced … …\x01",
            "You can not help feeling a doubt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4FAB")

    label("loc_4EF7")


    ChrTalk(
        0xFE,
        (
            "Originally, patients who were discharged from the hospital\x01",
            "It is necessary to see the progress for a while,\x01",
            "I can not do it under the travel restrictions of the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Irresponsible conduct as a doctor\x01",
            "This situation that will be forced … …\x01",
            "You can not help feeling a doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAB")

    Jump("loc_5671")

    label("loc_4FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5104")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5091")

    ChrTalk(
        0xFE,
        (
            "They are more hearted than the body\x01",
            "It seems that the damage damaged is large.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Illness and injury are cured by the patient's mind.\x01",
            "With a desperate feeling\x01",
            "The healing will also be delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you manage to recover\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_50FF")

    label("loc_5091")


    ChrTalk(
        0xFE,
        (
            "They are more hearted than the body\x01",
            "It seems that the damage damaged is large.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you manage to recover\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FF")

    Jump("loc_5671")

    label("loc_5104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5172")

    ChrTalk(
        0xFE,
        (
            "…… Fracture of the foot\x01",
            "I have already taken action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is not injuries like dying,\x01",
            "calm down please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5671")

    label("loc_5172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527C")

    ChrTalk(
        0xFE,
        (
            "Originally when surgery was born,\x01",
            "\"Punctuation such as cutting human body\"\x01",
            "It's been said a while … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, its understanding\x01",
            "It feels like I'm getting deeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great procurement has a success\x01",
            "Thanks for showing usability.\x01",
            "I must thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_530B")

    label("loc_527C")


    ChrTalk(
        0xFE,
        (
            "Recently, understanding of surgery is also done\x01",
            "It feels like I'm getting deeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great procurement has a success\x01",
            "Thanks for showing usability.\x01",
            "I must thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_530B")

    Jump("loc_5671")

    label("loc_5310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_550F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5486")

    ChrTalk(
        0xFE,
        (
            "Symptoms of Shizuku-\x01",
            "Surgery · internal medicine · neurology problems\x01",
            "It interfered complicatedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said that Kanji is difficult,\x01",
            "It is not completely blindness\x01",
            "It is said that there is a slight hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Looking for a little hope\x01",
            "In a sense, rather than give up\x01",
            "It can be said that it is painful and painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless I will never give up\x01",
            "To that parent and child, I will respect it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_550A")

    label("loc_5486")


    ChrTalk(
        0xFE,
        (
            "To ask for little hope\x01",
            "In a sense, it is painful and painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless I will never give up\x01",
            "To that parent and child, I will respect it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550A")

    Jump("loc_5671")

    label("loc_550F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551D")
    Jump("loc_5671")

    label("loc_551D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E9")

    ChrTalk(
        0xFE,
        (
            "In the matter of Joachim\x01",
            "Hospital credit fell temporarily, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our doctor's work,\x01",
            "It is all to help the patient seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you keep showing that attitude,\x01",
            "You will be able to regain credibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5663")

    label("loc_55E9")


    ChrTalk(
        0xFE,
        (
            "Our doctor's work,\x01",
            "It is all to help the patient seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you keep showing that attitude,\x01",
            "You will definitely get back the lost credit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5663")

    Jump("loc_5671")

    label("loc_5668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5671")

    label("loc_5671")

    TalkEnd(0xFE)
    Return()

    # Function_14_4BE9 end

    def Function_15_5675(): pass

    label("Function_15_5675")

    OP_4B(0xD, 0xFF)
    OP_4B(0x2C, 0xFF)

    ChrTalk(
        0x2C,
        (
            "Teacher … kind of medicine\x01",
            "I heard that it is not enough,\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Now I managed to manage it at the hospital as a whole\x01",
            "I am in the process of devising measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our hospital staff is excellent.\x01",
            "Please do not worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x2C, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x2C, 0xFF)
    Return()

    # Function_15_5675 end

    def Function_16_5759(): pass

    label("Function_16_5759")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_576A")
    Jump("loc_5AC7")

    label("loc_576A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5778")
    Jump("loc_5AC7")

    label("loc_5778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5786")
    Jump("loc_5AC7")

    label("loc_5786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5794")
    Jump("loc_5AC7")

    label("loc_5794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F9")

    ChrTalk(
        0xFE,
        (
            "Litton's 202 round visit,\x01",
            "Is it 1 minute 14 seconds over now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I said that it was already over,\x01",
            "…… There are still a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I thought about it before ….\x01",
            "Professors are unusual\x01",
            "It is tough on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One minute and one second affects life and death … …\x01",
            "A medical scene is such a world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To help more people's lives,\x01",
            "Strict observance of the time and movement as planned is\x01",
            "It is quite common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200Fsurely……\x01",
            "To say anything\x01",
            "It might be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, the technology\x01",
            "It should not be incomplete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I work quickly and perfectly.\x01",
            "…… For future young doctors\x01",
            "I want you to do so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5AAB")

    label("loc_59F9")


    ChrTalk(
        0xFE,
        (
            "To help more people's lives\x01",
            "Strict observance of the time and movement as planned is\x01",
            "It is quite common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I work quickly and perfectly.\x01",
            "…… For future young doctors\x01",
            "I want you to do so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AAB")

    Jump("loc_5AC7")

    label("loc_5AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5ABE")
    Jump("loc_5AC7")

    label("loc_5ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5AC7")

    label("loc_5AC7")

    TalkEnd(0xFE)
    Return()

    # Function_16_5759 end

    def Function_17_5ACB(): pass

    label("Function_17_5ACB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B51")

    ChrTalk(
        0xFE,
        (
            "Mr. Seyland,\x01",
            "He is a very respectable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wording is severe,\x01",
            "That consultation is compassionate\x01",
            "It is because it is overflowing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C50")

    label("loc_5B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BD2")

    ChrTalk(
        0xFE,
        (
            "The hospital food here,\x01",
            "The balance of nutrition\x01",
            "It is well thought out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is somewhat postoperative\x01",
            "I feel like healing well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C50")

    label("loc_5BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C50")

    ChrTalk(
        0xFE,
        (
            "In this hospital,\x01",
            "Nurses and teachers\x01",
            "You did it very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, quite.\x01",
            "I like my hospitalization.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C50")

    TalkEnd(0xFE)
    Return()

    # Function_17_5ACB end

    def Function_18_5C54(): pass

    label("Function_18_5C54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CE5")

    ChrTalk(
        0xFE,
        (
            "That female doctor, what kind of\x01",
            "It's okay I'm okay …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm staring at you when I'm complaining,\x01",
            "It seems to be quiet until he left the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5A")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D4E")

    ChrTalk(
        0xFE,
        "Oh, I'd like to leave the hospital early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also have plenty of simple meals.\x01",
            "Let's eat beef tea or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5A")

    label("loc_5D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D5A")
    Call(0, 11)

    label("loc_5D5A")

    TalkEnd(0xFE)
    Return()

    # Function_18_5C54 end

    def Function_19_5D5E(): pass

    label("Function_19_5D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DEE")

    ChrTalk(
        0xFE,
        (
            "Sholi shorisho …\x01",
            "My grandchild gave me\x01",
            "You are peeling the apples.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, if you do not mind\x01",
            "Would you like to join us as well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EAA")

    ChrTalk(
        0xFE,
        (
            "Today, for sure, in the city\x01",
            "There was an unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the rumored Orkis Tower\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after I left the hospital\x01",
            "Shall I look forward to it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F18")

    label("loc_5EAA")


    ChrTalk(
        0xFE,
        (
            "With the rumored Orkis Tower\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after I left the hospital\x01",
            "Shall I look forward to it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F18")

    Jump("loc_5FA9")

    label("loc_5F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FA9")

    ChrTalk(
        0xFE,
        (
            "Previously the hospital teacher\x01",
            "Due to causing a major incident\x01",
            "I was making a fuss, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a very good hospital.\x01",
            "I was worried about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA9")

    TalkEnd(0xFE)
    Return()

    # Function_19_5D5E end

    def Function_20_5FAD(): pass

    label("Function_20_5FAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6010")

    ChrTalk(
        0xFE,
        "Oh, is it true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm relieved.\x01",
            "Cure it quickly and get to work\x01",
            "I have to return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6191")

    label("loc_6010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CC")

    ChrTalk(
        0xFE,
        (
            "While my colleague is busy,\x01",
            "Please come visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not worry about work,\x01",
            "You are devoted to curing injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, in this case\x01",
            "Do you forget about work?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6120")

    label("loc_60CC")


    ChrTalk(
        0xFE,
        (
            "At this time, about work\x01",
            "Let's forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now to cure the injury\x01",
            "I have to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6120")

    Jump("loc_6191")

    label("loc_6125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6191")

    ChrTalk(
        0xFE,
        (
            "In a traffic accident, foot bones\x01",
            "Please break it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew.\x01",
            "I also have important work\x01",
            "Do not go over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_20_5FAD end

    def Function_21_6195(): pass

    label("Function_21_6195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_621F")

    ChrTalk(
        0xFE,
        (
            "The bed in the hospital room, too,\x01",
            "It was buried at a stroke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it was a big accident,\x01",
            "There are no dead people coming out\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F7")

    label("loc_621F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_62CD")

    ChrTalk(
        0xFE,
        (
            "The husband who left at home,\x01",
            "Are you letting the children eat properly\x01",
            "I was worried … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To that person, somehow\x01",
            "It looks like I'm challenging cooking.\x01",
            "I was relieved for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F7")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_63F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6391")

    ChrTalk(
        0xFE,
        (
            "Because I am an operation that is not a big deal\x01",
            "It seems that hospital admission is also short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But when you leave your house\x01",
            "After all the family is worried …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Husband and children\x01",
            "I wonder if you are eating properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_63F7")

    label("loc_6391")


    ChrTalk(
        0xFE,
        (
            "When you leave your house\x01",
            "After all the family is worried …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Husband and children\x01",
            "I wonder if you are eating properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F7")

    TalkEnd(0xFE)
    Return()

    # Function_21_6195 end

    def Function_22_63FB(): pass

    label("Function_22_63FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6473")

    ChrTalk(
        0xFE,
        (
            "No way, the train's\x01",
            "What is derailment accident ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, in a row\x01",
            "The incident is happening.\x01",
            "A monster who is noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6687")

    label("loc_6473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_661A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6574")

    ChrTalk(
        0xFE,
        (
            "To a distraction during hospitalization,\x01",
            "Cross the Bell Times this year\x01",
            "I read it from No. 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Attack of assassination of former Mayor of Mcdael,\x01",
            "Founding memorial festival, and that cult affair ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, for half a year\x01",
            "There really was various things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6615")

    label("loc_6574")


    ChrTalk(
        0xFE,
        (
            "Former Mayor's assassination attempted incident,\x01",
            "Civil affair, by terrorists\x01",
            "Raid incident at the Orchis Tower ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, for half a year\x01",
            "There are really various incidents occurring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6615")

    Jump("loc_6687")

    label("loc_661A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6687")

    ChrTalk(
        0xFE,
        (
            "Just while in hospital\x01",
            "I will spare my leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even books that were collected\x01",
            "Shall I read it at once?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6687")

    TalkEnd(0xFE)
    Return()

    # Function_22_63FB end

    def Function_23_668B(): pass

    label("Function_23_668B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_671F")

    ChrTalk(
        0xFE,
        (
            "This is just patient\x01",
            "To cure it safely,\x01",
            "As expected, the teachers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as there is Ursula Hospital,\x01",
            "Crossbell residents are safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6812")

    label("loc_671F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_673A")
    Call(0, 39)
    Jump("loc_679C")

    label("loc_673A")


    ChrTalk(
        0xFE,
        (
            "Because I am young, I am a bit worried\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Litton also\x01",
            "It is quite dependable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_679C")

    Jump("loc_6812")

    label("loc_67A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6812")

    ChrTalk(
        0xFE,
        (
            "Dr. Verdain's examination\x01",
            "Very polite and nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was taken care of by skilled teachers,\x01",
            "I am happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6812")

    TalkEnd(0xFE)
    Return()

    # Function_23_668B end

    def Function_24_6816(): pass

    label("Function_24_6816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_694B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C7")

    ChrTalk(
        0xFE,
        (
            "To be hospitalized for a train accident,\x01",
            "I am really sorry ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was hospitalized with a gikkuri waist\x01",
            "It is as poor as you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… What, that\x01",
            "Something that I said.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6946")

    label("loc_68C7")


    ChrTalk(
        0xFE,
        (
            "To be hospitalized for a train accident,\x01",
            "I was hospitalized with a gikkuri waist\x01",
            "It is as poor as you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… What, that\x01",
            "The face that he said something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6946")

    Jump("loc_6B32")

    label("loc_694B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A17")

    ChrTalk(
        0xFE,
        "…… My friend came to visit me yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be hospitalized at a gikkuri waist,\x01",
            "Because it's bad, everyone\x01",
            "I did not say that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely my mother rose.\x01",
            "Terrible …… It's too terrible ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6A9A")

    label("loc_6A17")


    ChrTalk(
        0xFE,
        (
            "To be hospitalized at a gikkuri waist,\x01",
            "Because it's bad, everyone\x01",
            "I did not say that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the happiness itself was a pleasure,\x01",
            "Oh well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A9A")

    Jump("loc_6B32")

    label("loc_6A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6B32")

    ChrTalk(
        0xFE,
        (
            "Oh, this is my motherfucker maiden,\x01",
            "I have to get in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Moreover,\x01",
            "Cool bad … … It is bad cool … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B32")

    TalkEnd(0xFE)
    Return()

    # Function_24_6816 end

    def Function_25_6B36(): pass

    label("Function_25_6B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B54")
    Call(0, 8)
    Jump("loc_6BA1")

    label("loc_6B54")


    ChrTalk(
        0xFE,
        (
            "Although it was saved,\x01",
            "The alkane shell at the … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, that's too bad ……\x02",
    )

    CloseMessageWindow()

    label("loc_6BA1")

    TalkEnd(0xFE)
    Return()

    # Function_25_6B36 end

    def Function_26_6BA5(): pass

    label("Function_26_6BA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C15")

    ChrTalk(
        0xFE,
        (
            "When the train rolled over,\x01",
            "I thought it was no good … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being,\x01",
            "I do not want to use the railroad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C15")

    TalkEnd(0xFE)
    Return()

    # Function_26_6BA5 end

    def Function_27_6C19(): pass

    label("Function_27_6C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C60")

    ChrTalk(
        0xFE,
        (
            "I was hurt … …!\x01",
            "And then die! It will be dead … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C60")

    TalkEnd(0xFE)
    Return()

    # Function_27_6C19 end

    def Function_28_6C64(): pass

    label("Function_28_6C64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D01")

    ChrTalk(
        0xFE,
        (
            "…… People across the house, opposite man\x01",
            "Gagher noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way\x01",
            "Because I was able to survive from the accident,\x01",
            "I have to put up with a bit of pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D01")

    TalkEnd(0xFE)
    Return()

    # Function_28_6C64 end

    def Function_29_6D05(): pass

    label("Function_29_6D05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD7")

    ChrTalk(
        0xFE,
        (
            "To the fighting power of \"red constellation\"\x01",
            "We can say that at all\x01",
            "I could not compete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A big unease to citizens\x01",
            "I should have given it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is the police for ……\x01",
            "I feel bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6E5E")

    label("loc_6DD7")


    ChrTalk(
        0xFE,
        (
            "To the fighting power of \"red constellation\"\x01",
            "We can say that at all\x01",
            "I could not compete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Donovan police also managed to\x01",
            "I hope to recover …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5E")

    TalkEnd(0xFE)
    Return()

    # Function_29_6D05 end

    def Function_30_6E62(): pass

    label("Function_30_6E62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F32")

    ChrTalk(
        0xFE,
        (
            "As Mr. Fran is in reception,\x01",
            "Our cops so far\x01",
            "It was extremely encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She regained consciousness,\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F……Thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6F9D")

    label("loc_6F32")


    ChrTalk(
        0xFE,
        (
            "Mr. Fran\x01",
            "It regains consciousness,\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as you get well\x01",
            "Sounds good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9D")

    TalkEnd(0xFE)
    Return()

    # Function_30_6E62 end

    def Function_31_6FA1(): pass

    label("Function_31_6FA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7034")

    ChrTalk(
        0xFE,
        (
            "Up to Fran.\x01",
            "I got a serious injury … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it …!\x01",
            "For what we are\x01",
            "I trained at the police school ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_70C4")

    label("loc_7034")


    ChrTalk(
        0xFE,
        (
            "Damn it …!\x01",
            "For what we are\x01",
            "I trained at the police school ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Mr. Fran\x01",
            "To make a serious injury,\x01",
            "I can not help being miserable … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C4")

    TalkEnd(0xFE)
    Return()

    # Function_31_6FA1 end

    def Function_32_70C8(): pass

    label("Function_32_70C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7156")

    ChrTalk(
        0xFE,
        (
            "The devil managed by that hunter,\x01",
            "It was frighteningly trained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once those assaults attack,\x01",
            "I will be given up this time …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7156")

    TalkEnd(0xFE)
    Return()

    # Function_32_70C8 end

    def Function_33_715A(): pass

    label("Function_33_715A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_71D4")

    ChrTalk(
        0xFE,
        (
            "Mr. Waldo ……\x01",
            "Until that will be that way\x01",
            "Did you want to become strong …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Damn, I do not mind, hey … …\x02",
    )

    CloseMessageWindow()

    label("loc_71D4")

    TalkEnd(0xFE)
    Return()

    # Function_33_715A end

    def Function_34_71D8(): pass

    label("Function_34_71D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_72F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7287")

    ChrTalk(
        0xFE,
        (
            "Whatever conflict was … ….\x01",
            "Anyhow, such a person\x01",
            "I can not do anything with the head any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tsuka, Saber Viper ……\x01",
            "This may be the end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_72F3")

    label("loc_7287")


    ChrTalk(
        0xFE,
        (
            "Such a guy ……\x01",
            "I can not do anything with the head any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tsuka, Saber Viper ……\x01",
            "This may be the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72F3")

    TalkEnd(0xFE)
    Return()

    # Function_34_71D8 end

    def Function_35_72F7(): pass

    label("Function_35_72F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_749D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741C")

    ChrTalk(
        0xFE,
        (
            "We just finished with bone fracture … …\x01",
            "He is a serious injury.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as I arrive at the hospital\x01",
            "Brought to an intensive care room ……\x01",
            "I am receiving treatment at the research building right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, still consciousness\x01",
            "It's a story that I will not recover ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fucking, why is this\x01",
            "I got it … …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_749D")

    label("loc_741C")


    ChrTalk(
        0xFE,
        (
            "The slash guy as well\x01",
            "Fully scare me.\x01",
            "I can not talk to Lok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fucking, why is this\x01",
            "I got it … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_749D")

    TalkEnd(0xFE)
    Return()

    # Function_35_72F7 end

    def Function_36_74A1(): pass

    label("Function_36_74A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_74E0")

    ChrTalk(
        0xFE,
        (
            "Buzz blinking ……\x01",
            "Then, a thing … … a thing attacked … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E0")

    TalkEnd(0xFE)
    Return()

    # Function_36_74A1 end

    def Function_37_74E4(): pass

    label("Function_37_74E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7567")

    ChrTalk(
        0xFE,
        (
            "Well, now\x01",
            "Nurse station's\x01",
            "I will clean it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Because it is a garden of women.\x01",
            "I'm getting nervous very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7567")

    TalkEnd(0xFE)
    Return()

    # Function_37_74E4 end

    def Function_38_756B(): pass

    label("Function_38_756B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_757C")
    Jump("loc_78C0")

    label("loc_757C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_758A")
    Jump("loc_78C0")

    label("loc_758A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_759B")
    Call(0, 41)
    Jump("loc_78C0")

    label("loc_759B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_765D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B6")
    Call(0, 40)
    Jump("loc_7658")

    label("loc_75B6")


    ChrTalk(
        0xFE,
        (
            "A patient who can leave the hospital\x01",
            "It is free to return to the city\x01",
            "I can not take it for granted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the \"Phantom Beast\" on the Highway\x01",
            "I guess there's also vigilance,\x01",
            "It feels like being too strict as expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7658")

    Jump("loc_78C0")

    label("loc_765D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_77C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7711")

    ChrTalk(
        0xFE,
        (
            "This room in my room\x01",
            "Police officers are in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apart from Mr. Kanbe of the second section\x01",
            "It is not an injury so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The duration of hospitalization to that extent\x01",
            "I do not think it will be long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_77BB")

    label("loc_7711")


    ChrTalk(
        0xFE,
        (
            "Mr. Kanbe of the second division ……\x01",
            "Although consciousness has not come back yet,\x01",
            "For a while Yama has overcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In Room 302 of the 3rd floor\x01",
            "I think I was in the hospital.\x01",
            "You ought to visit me if you do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77BB")

    Jump("loc_78C0")

    label("loc_77C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77CE")
    Jump("loc_78C0")

    label("loc_77CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7825")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E9")
    Call(0, 39)
    Jump("loc_7820")

    label("loc_77E9")


    ChrTalk(
        0xFE,
        (
            "Litton \"Teacher\" ……\x01",
            "Well, I heard a good sound …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7820")

    Jump("loc_78C0")

    label("loc_7825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7833")
    Jump("loc_78C0")

    label("loc_7833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78A9")

    ChrTalk(
        0xFE,
        (
            "Oh, the bones are pretty much\x01",
            "It seems they have stuck together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have a bit more patience\x01",
            "I will be able to walk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78C0")

    label("loc_78A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78B7")
    Jump("loc_78C0")

    label("loc_78B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_78C0")

    label("loc_78C0")

    TalkEnd(0xFE)
    Return()

    # Function_38_756B end

    def Function_39_78C4(): pass

    label("Function_39_78C4")

    OP_4B(0x24, 0xFF)

    ChrTalk(
        0x24,
        (
            "Yeah, the course is going well.\x01",
            "Even so soon\x01",
            "I think that you can leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Oh yeah that's right,\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Huhu, Mr. Litton also\x01",
            "There is some dependency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Well, is that so?\x01",
            "Well … I'm embarrassed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 0)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x24, 0xFF)
    Return()

    # Function_39_78C4 end

    def Function_40_79C1(): pass

    label("Function_40_79C1")

    OP_4B(0x24, 0xFF)
    OP_4B(0x26, 0xFF)

    ChrTalk(
        0x24,
        "Yes, the postoperative course is going well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Even if it is true\x01",
            "I hope to leave the hospital ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Oh, by the way, to and from the highway\x01",
            "There was a limitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Whew, for a while\x01",
            "It seems to be only hospitalized.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 3)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x10)
    OP_4C(0x24, 0xFF)
    OP_4C(0x26, 0xFF)
    Return()

    # Function_40_79C1 end

    def Function_41_7AB8(): pass

    label("Function_41_7AB8")

    OP_4B(0x24, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5A")

    ChrTalk(
        0xD,
        (
            "The hospital is set up by the President\x01",
            "Although I am receiving assistance ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Again, anxiety spreading to patients\x01",
            "It looks like a pretty thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Yeah, I went back and forth in an ambulance\x01",
            "It is quite limited and ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Maybe it's like me\x01",
            "The patient feels anxiety the resident is feeling\x01",
            "It may be transmitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In this case, even if you are not a resident\x01",
            "You should feel insecure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "……anyway,\x01",
            "People can feel relieved\x01",
            "Consideration is necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 2)
    Jump("loc_7D00")

    label("loc_7C5A")


    ChrTalk(
        0x24,
        (
            "Even Professor Verdyne\x01",
            "I do not feel anxious\x01",
            "There are things ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Everyone feels like anxiety.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "……anyway,\x01",
            "People can feel relieved\x01",
            "Consideration is necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D00")

    OP_4C(0x24, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_41_7AB8 end

    def Function_42_7D09(): pass

    label("Function_42_7D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D1A")
    Jump("loc_802A")

    label("loc_7D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7D28")
    Jump("loc_802A")

    label("loc_7D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7D36")
    Jump("loc_802A")

    label("loc_7D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E38")

    ChrTalk(
        0xFE,
        (
            "As a result of Shizuku's surgery\x01",
            "I think there are pros and cons, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could not recover at all\x01",
            "I could improve the function of the eye even a little\x01",
            "I think that's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally to treatment\x01",
            "I started the first step.\x01",
            "I have to work hard at the whole hospital.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_7ED3")

    label("loc_7E38")


    ChrTalk(
        0xFE,
        (
            "Suzuku finally got into treatment\x01",
            "I was able to take the first step.\x01",
            "I think that's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But, if you try it for the patient himself\x01",
            "After all it is uneasy …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED3")

    Jump("loc_802A")

    label("loc_7ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EE6")
    Jump("loc_802A")

    label("loc_7EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA5")

    ChrTalk(
        0xFE,
        (
            "Professor Seyland,\x01",
            "Even though I am young\x01",
            "It is very stately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm asking for a \"female doctor\"\x01",
            "The ideal image is exactly her … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me firmly study\x01",
            "I have to get it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_801C")

    label("loc_7FA5")


    ChrTalk(
        0xFE,
        (
            "Professor Seyland,\x01",
            "I'm asking for a \"female doctor\"\x01",
            "It is perfect for the ideal image.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me firmly study\x01",
            "I have to get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801C")

    Jump("loc_802A")

    label("loc_8021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_802A")

    label("loc_802A")

    TalkEnd(0xFE)
    Return()

    # Function_42_7D09 end

    def Function_43_802E(): pass

    label("Function_43_802E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8065")

    ChrTalk(
        0xFE,
        "Ha, I want to leave the hospital …\x02",
    )

    CloseMessageWindow()
    Jump("loc_80BF")

    label("loc_8065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_80BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8080")
    Call(0, 40)
    Jump("loc_80BF")

    label("loc_8080")


    ChrTalk(
        0xFE,
        (
            "Whew, for a while\x01",
            "It seems to be only hospitalized.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BF")

    TalkEnd(0xFE)
    Return()

    # Function_43_802E end

    def Function_44_80C3(): pass

    label("Function_44_80C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8159")

    ChrTalk(
        0xFE,
        (
            "Once the application has passed,\x01",
            "I was supposed to be able to return … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time the defense army comes\x01",
            "It seems a bit ahead.\x01",
            "Whether to wait patiently ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F1")

    label("loc_8159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_81F1")

    ChrTalk(
        0xFE,
        (
            "You leave the hospital and return to the city\x01",
            "I need a cumbersome application.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Defense forces are visiting on a tour\x01",
            "I can only return timing ……\x01",
            "This is going to be offended.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F1")

    TalkEnd(0xFE)
    Return()

    # Function_44_80C3 end

    def Function_45_81F5(): pass

    label("Function_45_81F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8261")

    ChrTalk(
        0xFE,
        (
            "Dissatisfaction with the president,\x01",
            "It can not be helped to say it already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess it is time to endure now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8301")

    label("loc_8261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8301")

    ChrTalk(
        0xFE,
        (
            "So then, to the president\x01",
            "There are many complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, when I complained\x01",
            "I am independent,\x01",
            "It can not be helped to some extent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8301")

    TalkEnd(0xFE)
    Return()

    # Function_45_81F5 end

    def Function_46_8305(): pass

    label("Function_46_8305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_83C8")

    ChrTalk(
        0xFE,
        (
            "Although I did not meet and talk directly,\x01",
            "In the figure of Iria who is doing his best in rehabilitation\x01",
            "I was really encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After a while, when I can return to the town,\x01",
            "Iria's hard work for everyone\x01",
            "I want to tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84C9")

    label("loc_83C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_84C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84A5")

    ChrTalk(
        0xFE,
        (
            "Ilia is hospitalized in the hospital\x01",
            "I might be able to meet you.\x01",
            "I also had a pale expectation ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rehabilitation with amazing features\x01",
            "If you see it working hard,\x01",
            "The soul of Meehae was miserable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I want you to keep up.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 1)
    Jump("loc_84C9")

    label("loc_84A5")


    ChrTalk(
        0xFE,
        "Iria … I hope you do your best.\x02",
    )

    CloseMessageWindow()

    label("loc_84C9")

    TalkEnd(0xFE)
    Return()

    # Function_46_8305 end

    def Function_47_84CD(): pass

    label("Function_47_84CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8542")

    ChrTalk(
        0xFE,
        (
            "Oh, it's a crowd.\x01",
            "Hospitals also have hot shots\x01",
            "I can not read it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if anyone will come to see me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85D6")

    label("loc_8542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_85D6")

    ChrTalk(
        0xFE,
        (
            "I just made a complicated fracture\x01",
            "I was taken to a hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it improved considerably,\x01",
            "It seems quite troublesome to return to the city\x01",
            "I will get bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D6")

    TalkEnd(0xFE)
    Return()

    # Function_47_84CD end

    def Function_48_85DA(): pass

    label("Function_48_85DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8647")

    ChrTalk(
        0xFE,
        (
            "It looks to the east sky\x01",
            "That pale tree is united …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O goddess.\x01",
            "Please save ourselves …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86C0")

    label("loc_8647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_86C0")

    ChrTalk(
        0xFE,
        (
            "What happens to the crossbell ……\x01",
            "Only the goddess knows it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, the way of salvation to us\x01",
            "To show things ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86C0")

    TalkEnd(0xFE)
    Return()

    # Function_48_85DA end

    def Function_49_86C4(): pass

    label("Function_49_86C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_874F")

    ChrTalk(
        0xFE,
        (
            "I am supposed to be able to leave the hospital today.\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside is such a situation ……\x01",
            "I want to go home and reassure my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A3")

    label("loc_874F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_87A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_876A")
    Call(0, 15)
    Jump("loc_87A3")

    label("loc_876A")


    ChrTalk(
        0xFE,
        (
            "If the teacher says so\x01",
            "I guess it's OK though …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A3")

    TalkEnd(0xFE)
    Return()

    # Function_49_86C4 end

    def Function_50_87A7(): pass

    label("Function_50_87A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8825")

    ChrTalk(
        0xFE,
        "It seems that teachers at rounds are also busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that outpatients are on the rise.\x01",
            "I'd like you to keep doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88C0")

    label("loc_8825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_88C0")

    ChrTalk(
        0xFE,
        (
            "There seems to be various problems at the hospital,\x01",
            "Teachers seem to be doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected it should be called Ursula Hospital ……\x01",
            "We can be hospitalized with confidence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88C0")

    TalkEnd(0xFE)
    Return()

    # Function_50_87A7 end

    def Function_51_88C4(): pass

    label("Function_51_88C4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_51_88C4 end

    def Function_52_88CB(): pass

    label("Function_52_88CB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110440, 1000, -3360, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 109780, 0, -3000, 135)
    SetChrPos(0x102, 110740, 0, -3020, 180)
    SetChrPos(0x103, 109190, 0, -4120, 135)
    SetChrPos(0x109, 109950, 0, -1880, 180)
    SetChrPos(0x104, 110150, 0, -580, 180)
    SetChrPos(0x105, 108940, 0, -1070, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "Seriously, that kid\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "About the mistake of ordering orders\x01",
            "I have to lose it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeah, seriously\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When writing an order sheet,\x01",
            "Meifa is tight\x01",
            "I was watching and spraying\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Still about 20 times\x01",
            "I misplaced the digits, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Ha, Mayfa's\x01",
            "I know the hardship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fthat……\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "Oh it's you guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, this child\x01",
            "Order medical supplies\x01",
            "I leave it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As I received the package,\x01",
            "Inside a boring doll\x01",
            "I was in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This girl, even before\x01",
            "Miscellaneous goods which do not understand Wake\x01",
            "I ordered it by mistake … Hey ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, please believe.\x01",
            "I said I should have done it properly this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLloyd, as we thought\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, looks like it\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FActually…\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's luggage misallocation\x01",
            "I explained that there was.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "No misunderstanding …\x01",
            "Was that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FNow, by ourselves\x01",
            "I am in the midst of redelivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWhat is the baggage for the hospital?\x01",
            "Is this about that?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '沉重货物'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('沉重货物', 1)

    ChrTalk(
        0xA,
        (
            "Hmm … … this surely\x01",
            "It's a medical device I ordered from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I bother delivering it\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "Also …\x01",
            "I'm sorry, Shillon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This time is my\x01",
            "It seems that it was quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhufu, that's fine.\x01",
            "I do not mind at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, that's right.\x01",
            "I wonder if that is also in ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Shillong is behind the baggage\x01",
            "I put my hands and furled right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Oh, happy!\x01",
            "\"Kagemalu\" strap spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "On the order,\x01",
            "I asked them together.\x01",
            "Uhufu, you are cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Shillon, you all\x01",
            "It is a sermon afterwards.\x02",
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
        0x101,
        (
            "#00006FUhhh\x02\x03",
            "#00000FI'm sorry, but it was misplaced\x01",
            "Even if you let me take your luggage\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Oh, that's right.\x01",
            "Give me a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Here it is.\x01",
            "I have asked for you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '小箱子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('小箱子', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThank you \x02\x03",
            "#00003FWell, from Aaron\x01",
            "According to the received slip ……\x02\x03",
            "#00000FNext is the house in the residential district\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92D7)
    Sleep(50)

    def lambda_92E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92E7)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FIf you reach it\x01",
            "It is a sunny request, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FSpeaking of residential areas,\x01",
            "McDaill's Chairman's House also\x01",
            "You are in a corner of a residential area.\x02\x03",
            "#10300FEly, this address is\x01",
            "Which is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_93A4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93A4)
    Sleep(50)

    def lambda_93B4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93B4)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FUhh, right\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FOh this is\x02\x03",
            "Campbell's House of Congress\x01",
            "It is not a vacant house next door.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95CC")
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
            "A vacant house in a residential area? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                        # 0
            "【Kaito B entered with quest】\x01",            # 1
            "【I studied in the prequel lacking dwelling quest】\x01",      # 2
            "I have not examined it]\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95B2")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x1, 0x2)
    Jump("loc_95CC")

    label("loc_95B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95CC")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x2, 0x2)

    label("loc_95CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9650")

    ChrTalk(
        0x101,
        (
            "#00005FCertainly ten years ago\x01",
            "Haunted House\x01",
            "It was being made a noise … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes, that's him\x02",
    )

    CloseMessageWindow()
    Jump("loc_96F4")

    label("loc_9650")


    ChrTalk(
        0x101,
        (
            "#00005FIs that certain?\x01",
            "I wonder if it was the name of a Republican senator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYeah ….\x01",
            "There is a mansion on the north side of the residential area.\x02\x03",
            "#00101FNext door, over ten years\x01",
            "It should have been a vacant house ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96F4")


    ChrTalk(
        0x104,
        (
            "#00305FWhat's going on?\x02\x03",
            "#00300FRecently\x01",
            "Was it also a tenant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FWell I don't really know\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F……Anyways,\x01",
            "Let's go once to deliver the package.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    SetScenarioFlags(0x176, 0)
    OP_29(0x85, 0x1, 0x3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 109780, 0, -3000, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_88CB end

    def Function_53_9805(): pass

    label("Function_53_9805")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room was room 301.\x01",
            "Let's go to see the situation as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 8600, 0, 3680, 180)
    EventEnd(0x4)
    Return()

    # Function_53_9805 end

    def Function_54_9868(): pass

    label("Function_54_9868")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room was room 301.\x01",
            "Let's go to see the situation as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26800, 0, -25170, 0)
    EventEnd(0x4)
    Return()

    # Function_54_9868 end

    SaveToFile()

Try(main)
