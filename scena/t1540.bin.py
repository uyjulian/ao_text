from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Cecil",                  # 1
        "Nurse Filia",            # 2
        "Head Nurse Martha",      # 3
        "Nurse Xilun",            # 4
        "Nurse Meihua",           # 5
        "Doctor Belldine",        # 6
        "Professor Seiland",      # 7
        "Inpatient",              # 8
        "Inpatient",              # 9
        "Inpatient",              # 10
        "Inpatient",              # 11
        "Inpatient",              # 12
        "Inpatient",              # 13
        "Inpatient",              # 14
        "Inpatient",              # 15
        "Inpatient",              # 16
        "Inpatient",              # 17
        "Inpatient",              # 18
        "Inpatient",              # 19
        "Policeman",              # 20
        "Policewoman",            # 21
        "Policeman",              # 22
        "Policeman",              # 23
        "Luganov",                # 24
        "Jed",                    # 25
        "Huey",                   # 26
        "Slash",                  # 27
        "Janitor Dyson",          # 28
        "Medical Intern Lytton",  # 29
        "Medical Intern Gwen",    # 30
        "Inpatient",              # 31
        "Inpatient",              # 32
        "Inpatient",              # 33
        "Inpatient",              # 34
        "Inpatient",              # 35
        "Inpatient",              # 36
        "Inpatient",              # 37
        "Inpatient",              # 38
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
        "Function_4_1836",         # 04, 4
        "Function_5_1D69",         # 05, 5
        "Function_6_1D6D",         # 06, 6
        "Function_7_2F39",         # 07, 7
        "Function_8_43DF",         # 08, 8
        "Function_9_4525",         # 09, 9
        "Function_10_45E4",        # 0A, 10
        "Function_11_4AE4",        # 0B, 11
        "Function_12_4CA1",        # 0C, 12
        "Function_13_4EAE",        # 0D, 13
        "Function_14_5365",        # 0E, 14
        "Function_15_60FD",        # 0F, 15
        "Function_16_6213",        # 10, 16
        "Function_17_663B",        # 11, 17
        "Function_18_67E6",        # 12, 18
        "Function_19_692F",        # 13, 19
        "Function_20_6C06",        # 14, 20
        "Function_21_6E26",        # 15, 21
        "Function_22_7111",        # 16, 22
        "Function_23_7490",        # 17, 23
        "Function_24_7654",        # 18, 24
        "Function_25_79E2",        # 19, 25
        "Function_26_7A54",        # 1A, 26
        "Function_27_7AEE",        # 1B, 27
        "Function_28_7B34",        # 1C, 28
        "Function_29_7BF0",        # 1D, 29
        "Function_30_7D93",        # 1E, 30
        "Function_31_7ECE",        # 1F, 31
        "Function_32_8031",        # 20, 32
        "Function_33_80EB",        # 21, 33
        "Function_34_817E",        # 22, 34
        "Function_35_828A",        # 23, 35
        "Function_36_847D",        # 24, 36
        "Function_37_84D3",        # 25, 37
        "Function_38_8573",        # 26, 38
        "Function_39_8949",        # 27, 39
        "Function_40_8A4B",        # 28, 40
        "Function_41_8B88",        # 29, 41
        "Function_42_8E51",        # 2A, 42
        "Function_43_9215",        # 2B, 43
        "Function_44_92BC",        # 2C, 44
        "Function_45_9442",        # 2D, 45
        "Function_46_9582",        # 2E, 46
        "Function_47_97A7",        # 2F, 47
        "Function_48_98DF",        # 30, 48
        "Function_49_99E7",        # 31, 49
        "Function_50_9B08",        # 32, 50
        "Function_51_9C9F",        # 33, 51
        "Function_52_9CA6",        # 34, 52
        "Function_53_AD76",        # 35, 53
        "Function_54_ADD6",        # 36, 54
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1359")
    Call(0, 4)
    Jump("loc_14C8")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")

    ChrTalk(
        0x8,
        (
            "#01304FNow that all the SSS members\x01",
            "are together, I am sure you will be\x01",
            "able to solve the chain of incidents.\x02\x03",
            "#01300FI will cheer for you from here.\x01",
            "Please do your best, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C8")

    label("loc_141F")


    ChrTalk(
        0x8,
        (
            "#01304FUh uh, being this the case,\x01",
            "I must do my best too with the hospital work.\x02\x03",
            "#01300FI am sure the venerable Goddess is watching.\x01",
            "You too, please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C8")

    Jump("loc_1832")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155D")

    ChrTalk(
        0x8,
        (
            "#01300FPlease say hello to your\x01",
            "Chief and KeA too.\x02\x03",
            "It is a tough situation, but...\x01",
            "Let's both do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155D")

    label("loc_155D")

    Jump("loc_1832")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1570")
    Jump("loc_1832")

    label("loc_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_157E")
    Jump("loc_1832")

    label("loc_157E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_180D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(
        0x8,
        (
            "#01308FDue to the matter of Shizuku's\x01",
            "surgery, the mood in the hospital\x01",
            "has become very gloomy.\x02\x03",
            "#01300FHowever, it is right in times\x01",
            "like this that we nurses\x01",
            "must show a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's indeed true.\x01",
            "We too have been helped\x01",
            "by KeA's smile, so...\x02\x03",
            "#00009FI think that the patients too\x01",
            "will feel better if you smile,\x01",
            "sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm sure their worries\x01",
            "will be blown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01309FUh uh, thank you.\x02\x03",
            "#01300FShizuku too is looking forward.\x01",
            "We must get our act together too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1808")

    label("loc_1795")


    ChrTalk(
        0x8,
        (
            "#01300FRight in gloomy times we\x01",
            "must show a smile.\x02\x03",
            "It is us nurses' duty to relieve\x01",
            "a patient's worries too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1808")

    Jump("loc_1832")

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_181B")
    Jump("loc_1832")

    label("loc_181B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1829")
    Jump("loc_1832")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1832")

    label("loc_1832")

    TalkEnd(0xFE)
    Return()

    # Function_3_133B end

    def Function_4_1836(): pass

    label("Function_4_1836")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1918")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18ED")
    SetChrPos(0x109, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_1918")

    label("loc_18ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1918")
    SetChrPos(0x105, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1918")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1981")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1956")
    SetChrPos(0x105, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_1981")

    label("loc_1956")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1981")
    SetChrPos(0x109, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1981")

    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P#01305FOh, Lloyd, guys...!\x02\x03",
            "#01309FUh uh, it seems the SSS\x01",
            "members are all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, at last.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A4D")

    ChrTalk(
        0x105,
        (
            "#12P#10402FHu hu, it's thanks\x01",
            "to your support.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4D")


    ChrTalk(
        0x102,
        (
            "#12P#00100FSorry to have worried you,\x01",
            "Miss Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01300FMiss Elie...and everyone too,\x01",
            "you seem to have gone through a lot.\x02\x03",
            "#01304FUh uh, but I wonder why...\x02\x03",
            "#01302FTo me, it seems like your bonds\x01",
            "have depended more than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, although we managed to reach\x01",
            "this point, there were a lot of hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FThe sense of accomplishment is all the more.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C2D")

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha...\x01",
            "There're still a heap of things to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2D")


    ChrTalk(
        0x8,
        (
            "#5P#01304FIt seems the hard times will still go on, but...\x02\x03",
            "#01300FI am sure that, if it is you all, you will\x01",
            "be able to solve this chain of incidents.\x02\x03",
            "#01309FUh uh, please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1AC, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 102700, 0, 940, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D43")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1D43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5B")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1D5B")

    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_4_1836 end

    def Function_5_1D69(): pass

    label("Function_5_1D69")

    Call(0, 6)
    Return()

    # Function_5_1D69 end

    def Function_6_1D6D(): pass

    label("Function_6_1D6D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E51")

    ChrTalk(
        0x9,
        (
            "Such a tree appearing...\x01",
            "T-Things have really\x01",
            "become serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The Head Nurse told me to\x01",
            "keep my composure to not\x01",
            "make the patients worry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, I can't really\x01",
            "stay calm...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EF9")

    label("loc_1E51")


    ChrTalk(
        0x9,
        (
            "Oh, if you're looking for senior Cecil,\x01",
            "after she saw that big tree she went\x01",
            "to the lounge area in the premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, senior is cool\x01",
            "being calm and all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF9")

    Jump("loc_2F35")

    label("loc_1EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1FC9")

    ChrTalk(
        0x9,
        (
            "I'm dealing with the inpatients\x01",
            "and the outpatients who can't\x01",
            "return to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since in the city a thing like that happened, it\x01",
            "seems that situation will continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F35")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_21EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2115")

    ChrTalk(
        0x9,
        (
            "Mr. Donovan's recovery is\x01",
            "progressing pretty well, so I think\x01",
            "he'll be able to be discharged soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, they say that even if Miss Ilya \x01",
            "undergoes an intense rehabilitation,\x01",
            "they don't know if she'll fully heal or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow I hope she does her best\x01",
            "and manages to make a comeback.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E7")

    label("loc_2115")


    ChrTalk(
        0x9,
        (
            "They say that even if Miss Ilya\x01",
            "undergoes an intense rehabilitation,\x01",
            "they don't know if she'll fully heal or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, making us feel an\x01",
            "indescribable hope is one of\x01",
            "Miss Ilya's amazing traits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E7")

    Jump("loc_2F35")

    label("loc_21EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D3")

    ChrTalk(
        0x9,
        (
            "Miss Ilya and Mr. Donovan\x01",
            "have regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately it's been only talks of bad things and\x01",
            "honestly, I was feeling down, but... I'm glad\x01",
            "a cheerful topic of conversation has appeared.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2324")

    label("loc_22D3")


    ChrTalk(
        0x9,
        (
            "I'm really glad that Miss\x01",
            "Ilya and Mr. Donovan\x01",
            "have regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2324")

    Jump("loc_2F35")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2463")

    ChrTalk(
        0x9,
        (
            "The people of the CGF were \x01",
            "accommodated in the ICU in\x01",
            "the research building, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone has received severe injuries from the jaegers \x01",
            "and they say it'll take time to be discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Many patients have been \x01",
            "hospitalised until now, but...\x01",
            "I really averted my eyes...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2504")

    label("loc_2463")


    ChrTalk(
        0x9,
        (
            "Many patients have been \x01",
            "hospitalised until now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I really averted my eyes from\x01",
            "the injuries of the people of the\x01",
            "CGF who were put in the ICU...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2504")

    Jump("loc_2F35")

    label("loc_2509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E4")

    ChrTalk(
        0x9,
        (
            "It seems things have finally\x01",
            "calmed down with dealing with\x01",
            "yesterday's derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "(*grooowl*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Now that I think about it,\x01",
            "I haven't eaten enough.\x01",
            "I'm hungry now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263C")

    label("loc_25E4")


    ChrTalk(
        0x9,
        (
            "Being busy I haven't\x01",
            "eaten enough.\x01",
            "I'm hungry now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'll go have a meal later.\x02",
    )

    CloseMessageWindow()

    label("loc_263C")

    Jump("loc_2F35")

    label("loc_2641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_289D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B9")

    ChrTalk(
        0x9,
        (
            "It seems that Professor Seiland\x01",
            "will work over again a surgery\x01",
            "for healing Shizuku's eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At first, I thought she was feeling down\x01",
            "and it was hard to talk to her, but...\x01",
            "She has already changed her way of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A force of will that can act calmly and\x01",
            "rationally no matter the circumstances...\x01",
            "That's really who the professor is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2898")

    label("loc_27B9")


    ChrTalk(
        0x9,
        (
            "Immediately changing your way of\x01",
            "thinking when things don't go well\x01",
            "is unexpectedly difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A force of will that can act calmly and\x01",
            "rationally no matter the circumstances...\x01",
            "That's really who the professor is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2898")

    Jump("loc_2F35")

    label("loc_289D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BF")

    ChrTalk(
        0x9,
        (
            "When I was feeling down due to\x01",
            "Shizuku's surgery, the Head Nurse\x01",
            "suddenly slapped my butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, that surprised me...\x01",
            "It's still tingling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, thanks to that, somehow my\x01",
            "gloomy feelings have been blown off.\x01",
            "I must do my best today too, yes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A94")

    label("loc_29BF")


    ChrTalk(
        0x9,
        (
            "Thanks to having been slapped, somehow\x01",
            "my gloomy feelings have been blown off.\x01",
            "That's the Head Nurse for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, I would've liked she\x01",
            "had restrained herself a little.\x01",
            "My butt is still tingling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A94")

    Jump("loc_2F35")

    label("loc_2A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B62")

    ChrTalk(
        0x9,
        (
            "I'm happy Mihail is leaving the hospital,\x01",
            "however we'll feel lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Especially Shizuku, I guess she'll\x01",
            "be the most lonely because they are\x01",
            "also close in age and great friends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F35")

    label("loc_2B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C39")

    ChrTalk(
        0x9,
        (
            "I too wanted to go see the Orchis\x01",
            "Tower unveiling today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, lately I can't\x01",
            "get a lot of days off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can't be helped being busy, but\x01",
            "I'd like to have some fun soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CF4")

    label("loc_2C39")


    ChrTalk(
        0x9,
        (
            "I even doubt if I'll be able to stand\x01",
            "in line to buy the ticket for the \x01",
            "next Arc-en-ciel public performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can't be helped being busy, but\x01",
            "I'd like to have some fun soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF4")

    Jump("loc_2F35")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB0")

    ChrTalk(
        0x9,
        (
            "Good morniiing, this\x01",
            "is the nurse station...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Wait, aah!\x01",
            "The younger brother and Mr. Randyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHey there, dear Filia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It really iiis!\x01",
            "Uh uh, but you look well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Mr. Randy, soon my\x01",
            "schedule will be open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOkay, okay, let's do\x01",
            "another group date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSenior, you still promise\x01",
            "those things easily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F*sigh*, my oh my.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 5)
    Jump("loc_2F35")

    label("loc_2EB0")


    ChrTalk(
        0x9,
        (
            "I want to go on a group date\x01",
            "with everyone one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Younger brother, you'll have to come\x01",
            "absolutely too when that happens!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F35")

    TalkEnd(0x9)
    Return()

    # Function_6_1D6D end

    def Function_7_2F39(): pass

    label("Function_7_2F39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F62")
    Call(0, 52)
    Return()

    label("loc_2F62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3088")

    ChrTalk(
        0xFE,
        (
            "After we have been accepting outpatients again,\x01",
            "the place has become busy in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that a lot of outpatients have come as \x01",
            "if to make up for all we couldn't accept until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I'll give it my all and\x01",
            "be zealous with my work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3127")

    label("loc_3088")


    ChrTalk(
        0xFE,
        (
            "I asked Mr. Harold to bring the\x01",
            "goods we're lacking. The patients'\x01",
            "acceptance system is perfect now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll give it my all and be zealous with my job.\x02",
    )

    CloseMessageWindow()

    label("loc_3127")

    Jump("loc_43DB")

    label("loc_312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_31E0")

    ChrTalk(
        0xFE,
        (
            "I'm going to the outpatients'\x01",
            "visitors at the boarding house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, Filia, I leave the\x01",
            "explanations to the\x01",
            "inpatients to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_43DB")

    label("loc_31E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335E")

    ChrTalk(
        0xFE,
        (
            "Anyway, the fact that only patients\x01",
            "with serious illnesses or injuries can be\x01",
            "carried in the hospital is an absurd rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's natural that there're also illnesses and wounds\x01",
            "that can't be understood just by their appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be too horrible to look at if\x01",
            "we couldn't save even patients who we\x01",
            "could have by using early treatments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3401")

    label("loc_335E")


    ChrTalk(
        0xFE,
        (
            "Only patients with serious illnesses or\x01",
            "injuries can get carried in the hospital...\x01",
            "That's an absurd rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if President\x01",
            "Dieter gets that point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3401")

    Jump("loc_43DB")

    label("loc_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_366D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B8")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio...\x01",
            "I'm told you're leaving the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes... Head Nurse Martha,\x01",
            "thank you for all you did for me.\x02\x03",
            "#00204FI hope I was able to repay you for when\x01",
            "I was hospitalised in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, jeez, it's in the past, so you\x01",
            "don't have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come again to see me whenever you want...\x01",
            "And please, be careful out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FUh uh, yes.\x01",
            "I'll do that for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3668")

    label("loc_35B8")


    ChrTalk(
        0xFE,
        (
            "Tio helped in many ways with\x01",
            "the hospital's machines and I\x01",
            "had fun chatting with her too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come again to see me whenever you want...\x01",
            "And please, be careful out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3668")

    Jump("loc_43DB")

    label("loc_366D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382C")

    ChrTalk(
        0xFE,
        (
            "As a matter of course, we medical\x01",
            "personnel have many chances to\x01",
            "be present when a person dies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why when people like the professors\x01",
            "and me do this job for a long time we end up\x01",
            "not even shedding tears for each person's death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this raid incident...\x01",
            "When I think about the many victims,\x01",
            "anger starts boiling within me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carelessly taking away people's lives...\x01",
            "It's an unforgivable act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38D0")

    label("loc_382C")


    ChrTalk(
        0xFE,
        (
            "There're people like doctors who\x01",
            "save many lives and, on the other hand,\x01",
            "jaegers who carelessly take them away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "..."Man" is really a\x01",
            "sinful living being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D0")

    Jump("loc_43DB")

    label("loc_38D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F0")
    Call(0, 8)
    Jump("loc_39B4")

    label("loc_38F0")


    ChrTalk(
        0xFE,
        (
            "Well, even watching the Arc-en-ciel public\x01",
            "performance, while there's life, there's hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have to be grateful to the Goddess that you're\x01",
            "safe and focus on healing your injuries now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B4")

    Jump("loc_43DB")

    label("loc_39B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DE")
    Call(0, 9)
    Jump("loc_3A54")

    label("loc_39DE")


    ChrTalk(
        0xFE,
        "You can't even say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I think about the mistakes you've\x01",
            "made until now, you're really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A54")

    Jump("loc_3B15")

    label("loc_3A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD7")

    ChrTalk(
        0xFE,
        (
            "Thank you for having\x01",
            "come on purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to lecture\x01",
            "this girl here, so\x01",
            "see you later, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B15")

    label("loc_3AD7")


    ChrTalk(
        0xFE,
        (
            "Goodness gracious...\x01",
            "Looking after Xilun\x01",
            "is really hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B15")

    Jump("loc_43DB")

    label("loc_3B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7D")

    ChrTalk(
        0xFE,
        (
            "Honestly, all of them\x01",
            "seem to be spent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get very well how they feel since\x01",
            "it's about the matter with Shizuku.\x01",
            "Everyone would feel down like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if even us make\x01",
            "a depressed face, the other\x01",
            "patients would become uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is right in times like this we must\x01",
            "show cheeriness. That's what I think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D28")

    label("loc_3C7D")


    ChrTalk(
        0xFE,
        (
            "Honestly, it's not good that all\x01",
            "of them are feeling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it's a put-on cheeriness, cheeriness is the\x01",
            "most important thing. Come on, you too, cheer up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D28")

    Jump("loc_43DB")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F20")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "My my my...!\x01",
            "Isn't that Tio?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, long time no see!\x01",
            "Have been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, I have.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FTio, are you an acquaintance\x01",
            "of the Head Nurse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. When I was hospitalised in the past,\x01",
            "it happened that she looked after me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahaha, as a nurse, I didn't\x01",
            "do anything special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The policeman job has many hardships\x01",
            "too, but you have to pay attention to\x01",
            "your health and do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FYes...thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 4)
    Jump("loc_3FD3")

    label("loc_3F20")


    ChrTalk(
        0xFE,
        (
            "I've said it before too,\x01",
            "but Tio has become\x01",
            "a real beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The policeman job has many hardships\x01",
            "too, but you have to pay attention to\x01",
            "your health and do your very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD3")

    Jump("loc_43DB")

    label("loc_3FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413A")

    ChrTalk(
        0xFE,
        (
            "No matter the person, Cecil doesn't \x01",
            "discriminate and can connect\x01",
            "considerately with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There aren't that many people who can\x01",
            "do something like that as it were normal.\x01",
            "I think she has a magnificent talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, maybe it was the will of\x01",
            "the venerable Goddess that made\x01",
            "her advance on the path to be a nurse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4211")

    label("loc_413A")


    ChrTalk(
        0xFE,
        (
            "Consideration is something that can\x01",
            "give peace of mind to the patients.\x01",
            "It's Cecil's splendid talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, maybe it was the will of\x01",
            "the venerable Goddess that made\x01",
            "her advance on the path to be a nurse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4211")

    Jump("loc_43DB")

    label("loc_4216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4374")

    ChrTalk(
        0xFE,
        (
            "Professor Seiland is\x01",
            "quite a famous person\x01",
            "in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She has a doctorate in the medicine field and\x01",
            "they say her ties with the Archduke family are deep.\x01",
            "Well, you can say that she has good references.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore and more than anything,\x01",
            "I like her scrappy attitude.\x01",
            "Nowadays, a woman has to be like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43DB")

    label("loc_4374")


    ChrTalk(
        0xFE,
        (
            "I like Professor\x01",
            "Seiland's scrappy\x01",
            "attitude, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nowadays, a woman has to be like that.\x02",
    )

    CloseMessageWindow()

    label("loc_43DB")

    TalkEnd(0xFE)
    Return()

    # Function_7_2F39 end

    def Function_8_43DF(): pass

    label("Function_8_43DF")

    OP_4B(0xA, 0xFF)
    OP_4B(0x17, 0xFF)

    ChrTalk(
        0x17,
        (
            "Although I had come to watch\x01",
            "the long awaited Arc-en-ciel,\x01",
            "I was in a train accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Uuh, what a pity...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, now that you mention it, the\x01",
            "renewal public opening is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, while there's life, there's hope.\x01",
            "You have to be grateful to the\x01",
            "Goddess to have been saved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x17, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x17, 0xFF)
    Return()

    # Function_8_43DF end

    def Function_9_4525(): pass

    label("Function_9_4525")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Honestly, you girl...\x01",
            "How many times will you repeat the same mistakes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uuh, but I did it properly\x01",
            "like I told you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's a mistake that a\x01",
            "mistake happened!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_4525 end

    def Function_10_45E4(): pass

    label("Function_10_45E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_460D")
    Call(0, 52)
    Return()

    label("loc_460D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_469B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462B")
    Call(0, 12)
    Jump("loc_4696")

    label("loc_462B")


    ChrTalk(
        0xFE,
        (
            "Tee-hee-hee, they look similar so I made a mistake.\x01",
            "At a closer look, their dimensions are different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4696")

    Jump("loc_4AE0")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_470A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B6")
    Call(0, 12)
    Jump("loc_4705")

    label("loc_46B6")


    ChrTalk(
        0xFE,
        (
            "I wonder if Baggio, father\x01",
            "and mother who're in the\x01",
            "city are all right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4705")

    Jump("loc_4AE0")

    label("loc_470A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4718")
    Jump("loc_4AE0")

    label("loc_4718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4726")
    Jump("loc_4AE0")

    label("loc_4726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4816")

    ChrTalk(
        0xFE,
        (
            "...It was the first time I saw so\x01",
            "many patients getting carried in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all looked to be hurting so much...\x01",
            "Since then, I've become\x01",
            "afraid to be alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have Meihua stay with\x01",
            "me tonight too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48AA")

    label("loc_4816")


    ChrTalk(
        0xFE,
        (
            "...Due to be the first time I saw so\x01",
            "many patients getting carried in,\x01",
            "I somehow got scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have Meihua stay with\x01",
            "me tonight too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AA")

    Jump("loc_4AE0")

    label("loc_48AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48BD")
    Jump("loc_4AE0")

    label("loc_48BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E2")
    Call(0, 9)
    Jump("loc_4939")

    label("loc_48E2")


    ChrTalk(
        0xFE,
        (
            "Like I told you, I'm sure it\x01",
            "must be some mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uuh, please believe meee!\x02",
    )

    CloseMessageWindow()

    label("loc_4939")

    Jump("loc_4AA5")

    label("loc_493E")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A34")

    ChrTalk(
        0xFE,
        (
            "Ehehe, a Kagemaru's strap...\x01",
            "I'm glad it got delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FKagemaru is nice...\x01",
            "I like him too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right☆\x01",
            "See, isn't he cuuute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...HEY, are you listening!?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TurnDirection(0xFE, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_4AA1")

    label("loc_4A34")


    ChrTalk(
        0xFE,
        (
            "Uuh, Head Nurse Martha,\x01",
            "here, pease look!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't the Kagemaru's strap\x01",
            "suuuper cute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Who cares!\x02",
    )

    CloseMessageWindow()

    label("loc_4AA1")

    OP_4C(0xA, 0xFF)

    label("loc_4AA5")

    Jump("loc_4AE0")

    label("loc_4AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4AB8")
    Jump("loc_4AE0")

    label("loc_4AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AC6")
    Jump("loc_4AE0")

    label("loc_4AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4AD4")
    Jump("loc_4AE0")

    label("loc_4AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AE0")
    Call(0, 11)

    label("loc_4AE0")

    TalkEnd(0xFE)
    Return()

    # Function_10_45E4 end

    def Function_11_4AE4(): pass

    label("Function_11_4AE4")

    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x10, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C51")

    ChrTalk(
        0xB,
        "Aaallright, let's do an intravenous drip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Ugh... Miss nurse, will it\x01",
            "go all right today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What if you pierced again a wrong place\x01",
            "and a spurt of blood came out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh come'on, the other time\x01",
            "I only missed my aim...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, please don't worry.\x01",
            "It will probably absolutely be all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "(I-I'm too worried...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_4C98")

    label("loc_4C51")


    ChrTalk(
        0xB,
        (
            "...Oh?\x01",
            "It seems I forgot the needle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "P-Please, Miss nurse...\x02",
    )

    CloseMessageWindow()

    label("loc_4C98")

    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_11_4AE4 end

    def Function_12_4CA1(): pass

    label("Function_12_4CA1")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4DB6")

    ChrTalk(
        0xC,
        (
            "Then, Xilun, let's divide our labor and\x01",
            "go measure the inpatients' temperatures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, Meihua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You have the medical thermometer with you, eh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeees♪, I have it here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...The one you got there\x01",
            "is not a thermometer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Uh, oh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA2")

    label("loc_4DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4EA2")

    ChrTalk(
        0xB,
        (
            "Meihua, what's\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm a little scared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It seems something big happened in the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, you don't have to worry.\x01",
            "Everything will be fine if we\x01",
            "do properly what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Y-Yes...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_4EA2")

    SetScenarioFlags(0x3, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_4CA1 end

    def Function_13_4EAE(): pass

    label("Function_13_4EAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECC")
    Call(0, 12)
    Jump("loc_4F09")

    label("loc_4ECC")


    ChrTalk(
        0xFE,
        (
            "Just about everything is wrong!\x01",
            "...Honestly, this girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F09")

    Jump("loc_5361")

    label("loc_4F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F29")
    Call(0, 12)
    Jump("loc_4FAB")

    label("loc_4F29")


    ChrTalk(
        0xFE,
        (
            "It seems certain that something\x01",
            "big happened in the city, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's important now is to do\x01",
            "properly what we can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAB")

    Jump("loc_5361")

    label("loc_4FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4FBE")
    Jump("loc_5361")

    label("loc_4FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4FCC")
    Jump("loc_5361")

    label("loc_4FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C0")

    ChrTalk(
        0xFE,
        (
            "The kids that were brought in room 202\x01",
            "were really energetic at first, but after\x01",
            "a little while they calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it's not only due to their injuries.\x01",
            "I wonder if something happened in the city...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5151")

    label("loc_50C0")


    ChrTalk(
        0xFE,
        (
            "Now that I think about it, lately Xilun\x01",
            "seems to be frightened for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder what will\x01",
            "happen to us from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5151")

    Jump("loc_5361")

    label("loc_5156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5164")
    Jump("loc_5361")

    label("loc_5164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5172")
    Jump("loc_5361")

    label("loc_5172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5180")
    Jump("loc_5361")

    label("loc_5180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_518E")
    Jump("loc_5361")

    label("loc_518E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B4")

    ChrTalk(
        0xFE,
        (
            "The other day, that Xilun was basking\x01",
            "in the sun on the rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, wrapped in the sheets she\x01",
            "had put to dry and with a happy-looking face...\x01",
            "Really, unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aah, I've got a bad presentiment.\x01",
            "Like she's doing the same thing again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5353")

    label("loc_52B4")


    ChrTalk(
        0xFE,
        (
            "The other day, that Xilun was basking\x01",
            "in the sun on the rooftop.\x01",
            "She also dirtied the sheets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I think I'll go check on\x01",
            "her later, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5353")

    Jump("loc_5361")

    label("loc_5358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5361")

    label("loc_5361")

    TalkEnd(0xFE)
    Return()

    # Function_13_4EAE end

    def Function_14_5365(): pass

    label("Function_14_5365")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5477")

    ChrTalk(
        0xFE,
        (
            "After a brief hospital round,\x01",
            "I have surgeries to do.\x01",
            "...Boy, I'm really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, no matter where it happens,\x01",
            "what we should do doesn't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go help a patient in front of your eyes...\x01",
            "That's the very job of a doctor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_550E")

    label("loc_5477")


    ChrTalk(
        0xFE,
        (
            "No matter where it happens,\x01",
            "what we should do doesn't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go help a patient in front of your eyes...\x01",
            "That's the very job of a doctor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550E")

    Jump("loc_60F9")

    label("loc_5513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_556D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552E")
    Call(0, 15)
    Jump("loc_5568")

    label("loc_552E")


    ChrTalk(
        0xFE,
        (
            "Our hospital staff is excellent.\x01",
            "Please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5568")

    Jump("loc_60F9")

    label("loc_556D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_557E")
    Call(0, 41)
    Jump("loc_60F9")

    label("loc_557E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5722")

    ChrTalk(
        0xFE,
        (
            "The police officers and the group\x01",
            "of delinquent youngsters who were\x01",
            "hospitalised have already been discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, I'd look at their conditions after having\x01",
            "been discharged by having them commuting to the\x01",
            "hospital for a while, but due to the highways\x01",
            "movements restriction, that's not possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a doctor, I can't help\x01",
            "but question this...\x01",
            "Irresponsible compulsory act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_581C")

    label("loc_5722")


    ChrTalk(
        0xFE,
        (
            "Normally, there would be the need to look for a while \x01",
            "at a discharged patient's progress too, but due to the\x01",
            "highways movements restriction, that's not possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a doctor, I can't help\x01",
            "but question this...\x01",
            "Irresponsible compulsory act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581C")

    Jump("loc_60F9")

    label("loc_5821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_59DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5943")

    ChrTalk(
        0xFE,
        (
            "As for him, it seems that the big damage he \x01",
            "suffered is to his mind more than to his body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A patient's' mind heals illnesses and injuries.\x01",
            "With feelings of despair, even\x01",
            "healing becomes further away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be nice if he\x01",
            "regained his footing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_59D8")

    label("loc_5943")


    ChrTalk(
        0xFE,
        (
            "As for him, it seems that the big damage he \x01",
            "suffered is to his mind more than to his body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be nice if he\x01",
            "regained his footing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D8")

    Jump("loc_60F9")

    label("loc_59DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A61")

    ChrTalk(
        0xFE,
        (
            "...The fracture in the leg\x01",
            "has already been treated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not an injury you'd die for,\x01",
            "so please calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F9")

    label("loc_5A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCB")

    ChrTalk(
        0xFE,
        (
            "When the "surgical department" was born at first,\x01",
            "it was harshly said that "it's inexcusable to cut\x01",
            "a person's body", however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, I feel like I gradually got\x01",
            "a deeper understanding of that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the great pioneers who had successes\x01",
            "and demonstrated its usefulness.\x01",
            "I have to be thankful for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C97")

    label("loc_5BCB")


    ChrTalk(
        0xFE,
        (
            "Recently, I feel like I gradually got\x01",
            "a deeper understanding of surgeries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the great pioneers who had successes\x01",
            "and demonstrated their usefulness.\x01",
            "I have to be thankful for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C97")

    Jump("loc_60F9")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E80")

    ChrTalk(
        0xFE,
        (
            "Shizuku's condition is an intricate\x01",
            "problem where surgery, internal\x01",
            "medicine and neurology interfere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A complete recovery is said to be impossible,\x01",
            "but it can also be said that there's a faint\x01",
            "hope that it's not a complete failure too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You can also say that to seek a\x01",
            "faint hope is, in a certain sense,\x01",
            "tougher and more painful than giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I learned what respect is from\x01",
            "those father and daughter who never give up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F3B")

    label("loc_5E80")


    ChrTalk(
        0xFE,
        (
            "You can also say that to seek a faint hope is, \x01",
            "in a certain sense, tough and painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I learned what respect is from\x01",
            "those father and daughter who never give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F3B")

    Jump("loc_60F9")

    label("loc_5F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F4E")
    Jump("loc_60F9")

    label("loc_5F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_60F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6055")

    ChrTalk(
        0xFE,
        (
            "Because of Joachim's matter, the trust\x01",
            "in the hospital fell down temporarily, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For our doctors' job, helping a\x01",
            "patient in earnest is everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we keep showing that attitude,\x01",
            "we'll get that trust back for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60EB")

    label("loc_6055")


    ChrTalk(
        0xFE,
        (
            "For our doctors' job, helping a\x01",
            "patient in earnest is everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we keep showing that attitude,\x01",
            "we'll get the lost trust back for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EB")

    Jump("loc_60F9")

    label("loc_60F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_60F9")

    label("loc_60F9")

    TalkEnd(0xFE)
    Return()

    # Function_14_5365 end

    def Function_15_60FD(): pass

    label("Function_15_60FD")

    OP_4B(0xD, 0xFF)
    OP_4B(0x2C, 0xFF)

    ChrTalk(
        0x2C,
        (
            "Doctor...I've heard that the hospital\x01",
            "is lacking many kinds of medicines.\x01",
            "Is it going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...At present, the entire hospital is working\x01",
            "over a kind of countermeasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our hospital staff is excellent.\x01",
            "Please don't worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x2C, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x2C, 0xFF)
    Return()

    # Function_15_60FD end

    def Function_16_6213(): pass

    label("Function_16_6213")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6224")
    Jump("loc_6637")

    label("loc_6224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6232")
    Jump("loc_6637")

    label("loc_6232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6240")
    Jump("loc_6637")

    label("loc_6240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_624E")
    Jump("loc_6637")

    label("loc_624E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6534")

    ChrTalk(
        0xFE,
        (
            "Lytton's round of the 202 room is 1 minute \x01",
            "and 14 seconds over what scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already finished here, and yet he...\x01",
            "...He's still got a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I thought about this too before...\x01",
            "You're oddly stric with\x01",
            "times, professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A mere moment can govern life and death....\x01",
            "That's the kind of world a medical treatment site is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To save even more people's lives,\x01",
            "strictly observing time and acting\x01",
            "according to schedule is quite obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIndeed...\x01",
            "It could hold true\x01",
            "for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, in order to do that,\x01",
            "skills must not be imperfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To perform their work quickly and flawlessly.\x01",
            "...I want the young doctors too\x01",
            "to become like that in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_661B")

    label("loc_6534")


    ChrTalk(
        0xFE,
        (
            "To save even more people's lives\x01",
            "strictly observing time and acting\x01",
            "according to schedule is quite obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To perform their work quickly and flawlessly.\x01",
            "...I want the young doctors too\x01",
            "to become like that in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_661B")

    Jump("loc_6637")

    label("loc_6620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_662E")
    Jump("loc_6637")

    label("loc_662E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6637")

    label("loc_6637")

    TalkEnd(0xFE)
    Return()

    # Function_16_6213 end

    def Function_17_663B(): pass

    label("Function_17_663B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_66CD")

    ChrTalk(
        0xFE,
        (
            "Doctor Seiland is really\x01",
            "a great person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She uses harsh words, but\x01",
            "her medical examinations\x01",
            "are extremely considerate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67E2")

    label("loc_66CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6775")

    ChrTalk(
        0xFE,
        (
            "The meals of this hospital\x01",
            "are very well thought for\x01",
            "nutrients balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness somehow the healing\x01",
            "after the surgery is going well too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67E2")

    label("loc_6775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67E2")

    ChrTalk(
        0xFE,
        (
            "In this hospital the\x01",
            "nurses and doctors\x01",
            "are very kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I quite like the\x01",
            "inpatient's life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E2")

    TalkEnd(0xFE)
    Return()

    # Function_17_663B end

    def Function_18_67E6(): pass

    label("Function_18_67E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_68A4")

    ChrTalk(
        0xFE,
        (
            "That female doctor is somewhat\x01",
            "cool and scary at the same time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you complain, she gives you a hostile look...\x01",
            "I guess I'll behave until I leave the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692B")

    label("loc_68A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_691F")

    ChrTalk(
        0xFE,
        "Aah, I wish I were discharged quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've had enough of frugal meals too.\x01",
            "I wanna eat a beefsteak!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692B")

    label("loc_691F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_692B")
    Call(0, 11)

    label("loc_692B")

    TalkEnd(0xFE)
    Return()

    # Function_18_67E6 end

    def Function_19_692F(): pass

    label("Function_19_692F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_69B6")

    ChrTalk(
        0xFE,
        (
            "*peel peel peel*...\x01",
            "I'm peeling an apple my\x01",
            "grandchild brought me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, would you like\x01",
            "to eat it with me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C02")

    label("loc_69B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ABE")

    ChrTalk(
        0xFE,
        (
            "If I remember correctly, today there's\x01",
            "the unveiling ceremony in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to see that Orchis\x01",
            "Tower or like it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I believe I'll leave it as something to\x01",
            "look forward to after I have been discharged.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B5B")

    label("loc_6ABE")


    ChrTalk(
        0xFE,
        (
            "I wanted to see that Orchis\x01",
            "Tower or like it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I believe I'll leave it as something to\x01",
            "look forward to after I have been discharged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5B")

    Jump("loc_6C02")

    label("loc_6B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C02")

    ChrTalk(
        0xFE,
        (
            "Previously, the doctors\x01",
            "were in an uproar due to a big\x01",
            "incident having happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a very good hospital.\x01",
            "I'm not worried anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C02")

    TalkEnd(0xFE)
    Return()

    # Function_19_692F end

    def Function_20_6C06(): pass

    label("Function_20_6C06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C78")

    ChrTalk(
        0xFE,
        "Ooh, is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what a relief.\x01",
            "I have to get well quick\x01",
            "and return to my job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E22")

    label("loc_6C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D48")

    ChrTalk(
        0xFE,
        (
            "Although my colleague is busy,\x01",
            "he came to visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said to not worry about work\x01",
            "and concentrate on getting well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's right, in this case\x01",
            "I'll forget about work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6DA5")

    label("loc_6D48")


    ChrTalk(
        0xFE,
        (
            "In this case, I'll\x01",
            "forget about work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I must concentrate\x01",
            "of healing my injury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DA5")

    Jump("loc_6E22")

    label("loc_6DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E22")

    ChrTalk(
        0xFE,
        (
            "I've broken a leg in\x01",
            "a traffic accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh man, I have\x01",
            "important work to do\x01",
            "and yet I have to quit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E22")

    TalkEnd(0xFE)
    Return()

    # Function_20_6C06 end

    def Function_21_6E26(): pass

    label("Function_21_6E26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EB9")

    ChrTalk(
        0xFE,
        (
            "All the sickroom beds\x01",
            "were occupied suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there was a big accident,\x01",
            "but I'm really glad that no one died.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710D")

    label("loc_6EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F7D")

    ChrTalk(
        0xFE,
        (
            "I was worried if my husband,\x01",
            "who remained at home, was\x01",
            "properly feeding the children, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that man is somehow\x01",
            "try cooking in his own way.\x01",
            "For now I'm relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710D")

    label("loc_6F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_710D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7084")

    ChrTalk(
        0xFE,
        (
            "My surgery is nothing special, so it seems\x01",
            "that my hospitalisation will be brief too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, being away from home\x01",
            "I'm really worried about my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband and the\x01",
            "children are properly eating meals.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_710D")

    label("loc_7084")


    ChrTalk(
        0xFE,
        (
            "Being away from home, I'm\x01",
            "really worried about my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband and the\x01",
            "children are properly eating meals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_710D")

    TalkEnd(0xFE)
    Return()

    # Function_21_6E26 end

    def Function_22_7111(): pass

    label("Function_22_7111")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71A3")

    ChrTalk(
        0xFE,
        (
            "To think that a train\x01",
            "derailment accident would...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, incidents have\x01",
            "happened in succession...\x01",
            "That's disturbing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_748C")

    label("loc_71A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730C")

    ChrTalk(
        0xFE,
        (
            "Just for recreation while I'm hospitalised,\x01",
            "I've read over again this year's\x01",
            "Crossbell Times from the first issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attempted assassination incident of\x01",
            "former mayor MacDowell, the Founding\x01",
            "Anniversary Festival, that Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considered all this, in just over half a year\x01",
            "many different things have happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_73EB")

    label("loc_730C")


    ChrTalk(
        0xFE,
        (
            "The attempted assassination incident of the \x01",
            "former mayor, the Cult incident, the Orchis \x01",
            "Tower raid incident by terrorists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considered all this, in just over half a year\x01",
            "many different incidents have happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73EB")

    Jump("loc_748C")

    label("loc_73F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_748C")

    ChrTalk(
        0xFE,
        (
            "When you're hospitalised, you have too\x01",
            "much free time on your hands, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll read the books I\x01",
            "had collected all at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_748C")

    TalkEnd(0xFE)
    Return()

    # Function_22_7111 end

    def Function_23_7490(): pass

    label("Function_23_7490")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7542")

    ChrTalk(
        0xFE,
        (
            "To cure so many patients\x01",
            "without a hitch...\x01",
            "That's those doctors for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as there's St. Ursula Hospital,\x01",
            "Crossbell citizens can feel at ease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7650")

    label("loc_7542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_75C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_755D")
    Call(0, 39)
    Jump("loc_75BF")

    label("loc_755D")


    ChrTalk(
        0xFE,
        (
            "I was a little worried\x01",
            "since he's young, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doctor Lytton is quite\x01",
            "trustworthy too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75BF")

    Jump("loc_7650")

    label("loc_75C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7650")

    ChrTalk(
        0xFE,
        (
            "Doctor Belldine's medical examinations\x01",
            "are very thorough and nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm very happy to be looked\x01",
            "after by skilled doctors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7650")

    TalkEnd(0xFE)
    Return()

    # Function_23_7490 end

    def Function_24_7654(): pass

    label("Function_24_7654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_77ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7739")

    ChrTalk(
        0xFE,
        (
            "Getting hospitalised due to a\x01",
            "train accident is really pitiable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As pitiable as being\x01",
            "hospitalised for a strained back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What's with that face that\x01",
            "seems to want to say something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_77E8")

    label("loc_7739")


    ChrTalk(
        0xFE,
        (
            "Getting hospitalised due to a train\x01",
            "accident is as pitiable as being\x01",
            "hospitalised for a strained back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What's with that face that\x01",
            "looks to want to say something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77E8")

    Jump("loc_79DE")

    label("loc_77ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_795B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D0")

    ChrTalk(
        0xFE,
        "...The other day, a friend came to visit me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting hospitalised for a\x01",
            "strained back is lame so I\x01",
            "didn't tell that to anyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my mother spilled it out.\x01",
            "Cruel...too cruel...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7956")

    label("loc_78D0")


    ChrTalk(
        0xFE,
        (
            "Getting hospitalised for a\x01",
            "strained back is lame so I\x01",
            "didn't tell that to anyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I was happy\x01",
            "he came to see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7956")

    Jump("loc_79DE")

    label("loc_795B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_79DE")

    ChrTalk(
        0xFE,
        (
            "Aah, I, a youthful maiden,\x01",
            "having to be hospitalised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And furthermore, for a strained back.\x01",
            "Lame...so lame...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DE")

    TalkEnd(0xFE)
    Return()

    # Function_24_7654 end

    def Function_25_79E2(): pass

    label("Function_25_79E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A00")
    Call(0, 8)
    Jump("loc_7A50")

    label("loc_7A00")


    ChrTalk(
        0xFE,
        (
            "Although I'm safe, my long\x01",
            "awaited Arc-en-ciel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uuh, what a pity...\x02",
    )

    CloseMessageWindow()

    label("loc_7A50")

    TalkEnd(0xFE)
    Return()

    # Function_25_79E2 end

    def Function_26_7A54(): pass

    label("Function_26_7A54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AEA")

    ChrTalk(
        0xFE,
        (
            "When the train turned sideways,\x01",
            "I thought I was a goner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being, I don't want to\x01",
            "make use of the railway anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AEA")

    TalkEnd(0xFE)
    Return()

    # Function_26_7A54 end

    def Function_27_7AEE(): pass

    label("Function_27_7AEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7B30")

    ChrTalk(
        0xFE,
        (
            "Ow ow ow ow...!\x01",
            "I-I'm dying! I'm gonna dieee...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B30")

    TalkEnd(0xFE)
    Return()

    # Function_27_7AEE end

    def Function_28_7B34(): pass

    label("Function_28_7B34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7BEC")

    ChrTalk(
        0xFE,
        (
            "...The guy over there, although he's\x01",
            "a man, he's squawking so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we managed to survive\x01",
            "from such an accident, we have \x01",
            "to endure at least a little pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BEC")

    TalkEnd(0xFE)
    Return()

    # Function_28_7B34 end

    def Function_29_7BF0(): pass

    label("Function_29_7BF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CEA")

    ChrTalk(
        0xFE,
        (
            "I can just say that we couldn't\x01",
            "oppose the "Red Constellation"\x01",
            "fighting strength at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We probably ended up giving a\x01",
            "big unrest to the citizens too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What good is the police for...?\x01",
            "I feel so pathetic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7D8F")

    label("loc_7CEA")


    ChrTalk(
        0xFE,
        (
            "I can just say that we couldn't\x01",
            "oppose the "Red Constellation"\x01",
            "fighting strength at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that Inspector Donovan too\x01",
            "recovers in a way or another...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D8F")

    TalkEnd(0xFE)
    Return()

    # Function_29_7BF0 end

    def Function_30_7D93(): pass

    label("Function_30_7D93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6D")

    ChrTalk(
        0xFE,
        (
            "We officers have been cheered up\x01",
            "a whole lot until now by Miss Fran\x01",
            "being at the reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really happy that she\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F...Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7ECA")

    label("loc_7E6D")


    ChrTalk(
        0xFE,
        (
            "I'm really happy that\x01",
            "Miss Fran regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she gets\x01",
            "well fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ECA")

    TalkEnd(0xFE)
    Return()

    # Function_30_7D93 end

    def Function_31_7ECE(): pass

    label("Function_31_7ECE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_802D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F7B")

    ChrTalk(
        0xFE,
        (
            "They even hurt very bad\x01",
            "Miss Fran of the reception...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit...!\x01",
            "For what purpose did we do all\x01",
            "that training at the Police Academy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_802D")

    label("loc_7F7B")


    ChrTalk(
        0xFE,
        (
            "Shit...!\x01",
            "For what purpose did we do all\x01",
            "that training at the Police Academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even hurt very bad\x01",
            "Miss Fran of the reception...\x01",
            "I can't stand to be so pathetic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_802D")

    TalkEnd(0xFE)
    Return()

    # Function_31_7ECE end

    def Function_32_8031(): pass

    label("Function_32_8031")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_80E7")

    ChrTalk(
        0xFE,
        (
            "Those monsters the jaeger were using,\x01",
            "they were terrifically well trained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those guys come to attack us once again,\x01",
            "the next time we'll all be done for...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80E7")

    TalkEnd(0xFE)
    Return()

    # Function_32_8031 end

    def Function_33_80EB(): pass

    label("Function_33_80EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_817A")

    ChrTalk(
        0xFE,
        (
            "Mr. Wald...\x01",
            "You wanted to become strong to the\x01",
            "extent of turning into such a thing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Shit, it makes no sense at all...\x02",
    )

    CloseMessageWindow()

    label("loc_817A")

    TalkEnd(0xFE)
    Return()

    # Function_33_80EB end

    def Function_34_817E(): pass

    label("Function_34_817E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8224")

    ChrTalk(
        0xFE,
        (
            "I had a feud with him, but...\x01",
            "In any case, that guy is\x01",
            "no leader anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather, this could be...\x01",
            "The Saber Viper's end too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_8286")

    label("loc_8224")


    ChrTalk(
        0xFE,
        (
            "That guy...\x01",
            "He's no leader anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather, this could be...\x01",
            "The Saber Viper's end too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8286")

    TalkEnd(0xFE)
    Return()

    # Function_34_817E end

    def Function_35_828A(): pass

    label("Function_35_828A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8411")

    ChrTalk(
        0xFE,
        (
            "In our case it was over with bone fractures, but...\x01",
            "Kｷki has got some extraordinary heavy injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After arriving at the hospital, he was\x01",
            "carried to the ICU on the double...\x01",
            "Now he's receiving treatment at the research laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard them saying that he hasn't\x01",
            "even regained consciousness yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit, why did such a\x01",
            "thing happen...!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_8479")

    label("loc_8411")


    ChrTalk(
        0xFE,
        (
            "Even Slash is\x01",
            "totally scared.\x01",
            "He can't even talk well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit, why did such a\x01",
            "thing happen...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8479")

    TalkEnd(0xFE)
    Return()

    # Function_35_828A end

    def Function_36_847D(): pass

    label("Function_36_847D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_84CF")

    ChrTalk(
        0xFE,
        (
            "*tremble tremble tremble*...\x01",
            "A m-monster...a monster attacked...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84CF")

    TalkEnd(0xFE)
    Return()

    # Function_36_847D end

    def Function_37_84D3(): pass

    label("Function_37_84D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_856F")

    ChrTalk(
        0xFE,
        (
            "Well, now I should\x01",
            "go do the cleanings\x01",
            "at the nurse station, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's the women's garden, you see.\x01",
            "I can't help but be nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_856F")

    TalkEnd(0xFE)
    Return()

    # Function_37_84D3 end

    def Function_38_8573(): pass

    label("Function_38_8573")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8584")
    Jump("loc_8945")

    label("loc_8584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8592")
    Jump("loc_8945")

    label("loc_8592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_85A3")
    Call(0, 41)
    Jump("loc_8945")

    label("loc_85A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85BE")
    Call(0, 40)
    Jump("loc_866E")

    label("loc_85BE")


    ChrTalk(
        0xFE,
        (
            "It's not that the patients who\x01",
            "are discharged can go back \x01",
            "to the city freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's vigilance about \x01",
            ""Cryptids" on the highway,\x01",
            "but I really feel it's too strict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_866E")

    Jump("loc_8945")

    label("loc_8673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8756")

    ChrTalk(
        0xFE,
        (
            "Police officers are hospitalised\x01",
            "in this sickroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aside from that Section Two inspector,\x01",
            "they aren't injured that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also think that they won't stay\x01",
            "hospitalised for a long time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_8823")

    label("loc_8756")


    ChrTalk(
        0xFE,
        (
            "That Section Two inspector...\x01",
            "He hasn't regained consciousness yet,\x01",
            "but for now he should've passed the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he was hospitalised\x01",
            "in room 302 on 3F. Please\x01",
            "pay him a visit, if you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8823")

    Jump("loc_8945")

    label("loc_8828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8836")
    Jump("loc_8945")

    label("loc_8836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8851")
    Call(0, 39)
    Jump("loc_8890")

    label("loc_8851")


    ChrTalk(
        0xFE,
        (
            ""Doctor" Lytton, eh...?\x01",
            "Uuhm, it has a nice ring to it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8890")

    Jump("loc_8945")

    label("loc_8895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_88A3")
    Jump("loc_8945")

    label("loc_88A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_892E")

    ChrTalk(
        0xFE,
        (
            "Yes, the bone too seems to\x01",
            "have adhered considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be able to walk again\x01",
            "if you'll endure a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8945")

    label("loc_892E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_893C")
    Jump("loc_8945")

    label("loc_893C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8945")

    label("loc_8945")

    TalkEnd(0xFE)
    Return()

    # Function_38_8573 end

    def Function_39_8949(): pass

    label("Function_39_8949")

    OP_4B(0x24, 0xFF)

    ChrTalk(
        0x24,
        (
            "Yes, the progress is going well.\x01",
            "I think you'll be able to\x01",
            "be discharged soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I see, I see,\x01",
            "thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Hu hu, somehow you're\x01",
            "trustworthy too, doctor Lytton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I-I-Is that so?\x01",
            "Well, ha ha...you're embarrassing me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 0)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x24, 0xFF)
    Return()

    # Function_39_8949 end

    def Function_40_8A4B(): pass

    label("Function_40_8A4B")

    OP_4B(0x24, 0xFF)
    OP_4B(0x26, 0xFF)

    ChrTalk(
        0x24,
        "Yes, the postoperative progress is going well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Actually, I would like to\x01",
            "discharge you immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Aah, now that I think about it, there're restrictions\x01",
            "about coming and going on the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Oh boy, I guess I can only stay\x01",
            "hospitalised for a little longer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 3)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x10)
    OP_4C(0x24, 0xFF)
    OP_4C(0x26, 0xFF)
    Return()

    # Function_40_8A4B end

    def Function_41_8B88(): pass

    label("Function_41_8B88")

    OP_4B(0x24, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9B")

    ChrTalk(
        0xD,
        (
            "Although the hospital is receiving\x01",
            "aid from the President...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As expected, it seems that a lot of\x01",
            "anxiety is spreading among the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Yes. Even the coming and going of the\x01",
            "ambulances has been restricted a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "It could be that the anxiety someone\x01",
            "like me feels for being a medical\x01",
            "intern passes to the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In a case like this, they'd feel anxious\x01",
            "even if you weren't a medical intern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Either way, we need to\x01",
            "be considerate to be able\x01",
            "to reassure the patients.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 2)
    Jump("loc_8E48")

    label("loc_8D9B")


    ChrTalk(
        0x24,
        (
            "Even you, \x01",
            "Doctor Belldine,\x01",
            "feel anxious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Everyone feels like that, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Either way, we need to\x01",
            "be considerate to be able\x01",
            "to reassure the patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E48")

    OP_4C(0x24, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_41_8B88 end

    def Function_42_8E51(): pass

    label("Function_42_8E51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8E62")
    Jump("loc_9211")

    label("loc_8E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8E70")
    Jump("loc_9211")

    label("loc_8E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8E7E")
    Jump("loc_9211")

    label("loc_8E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_909B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FDE")

    ChrTalk(
        0xFE,
        (
            "I think there're pros and cons about\x01",
            "Shizuku's surgery results, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's amazing that there was even just\x01",
            "a little improvement in her eyes function that\x01",
            "it couldn't be healed in the slightest until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, we have advanced a step\x01",
            "towards their treatment.\x01",
            "The entire hospital must do its best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_9096")

    label("loc_8FDE")


    ChrTalk(
        0xFE,
        (
            "Finally, we have advanced a step\x01",
            "towards Shizuku's treatment.\x01",
            "I think that's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, looking at the patient herself,\x01",
            "she has some preoccupations, as expected...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9096")

    Jump("loc_9211")

    label("loc_909B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_90A9")
    Jump("loc_9211")

    label("loc_90A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_917F")

    ChrTalk(
        0xFE,
        (
            "Professor Seiland...\x01",
            "Although she's young,\x01",
            "she has a cool personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She truly is the ideal image of the\x01",
            ""capable female doctor" I seek to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must study\x01",
            "diligently.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_9203")

    label("loc_917F")


    ChrTalk(
        0xFE,
        (
            "Professor Seiland \x01",
            "perfectly fits the ideal image of the\x01",
            ""capable female doctor" I seek to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must study\x01",
            "diligently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9203")

    Jump("loc_9211")

    label("loc_9208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9211")

    label("loc_9211")

    TalkEnd(0xFE)
    Return()

    # Function_42_8E51 end

    def Function_43_9215(): pass

    label("Function_43_9215")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9256")

    ChrTalk(
        0xFE,
        "*sigh*, I want to be discharged already...\x02",
    )

    CloseMessageWindow()
    Jump("loc_92B8")

    label("loc_9256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_92B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9271")
    Call(0, 40)
    Jump("loc_92B8")

    label("loc_9271")


    ChrTalk(
        0xFE,
        (
            "Oh boy, I guess I can only stay\x01",
            "hospitalised for a little longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B8")

    TalkEnd(0xFE)
    Return()

    # Function_43_9215 end

    def Function_44_92BC(): pass

    label("Function_44_92BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9375")

    ChrTalk(
        0xFE,
        (
            "My application went through,\x01",
            "so I can return home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it'll take some more until\x01",
            "the State Guard comes next time.\x01",
            "Oh boy, I'll wait patiently...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_943E")

    label("loc_9375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_943E")

    ChrTalk(
        0xFE,
        (
            "A bothersome application is needed even to\x01",
            "return to the city after being discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can only go back home when the\x01",
            "State Guard comes for a patrol...\x01",
            "That's a depressing thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_943E")

    TalkEnd(0xFE)
    Return()

    # Function_44_92BC end

    def Function_45_9442(): pass

    label("Function_45_9442")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_94C6")

    ChrTalk(
        0xFE,
        (
            "Even if I complained against the President,\x01",
            "there's nothing that could be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now it's time to endure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_957E")

    label("loc_94C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_957E")

    ChrTalk(
        0xFE,
        (
            "Well, I have a lot of complaints\x01",
            "against the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, even if I said them, the\x01",
            "independence has been carried over\x01",
            "so they're useless to a certain extent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_957E")

    TalkEnd(0xFE)
    Return()

    # Function_45_9442 end

    def Function_46_9582(): pass

    label("Function_46_9582")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9674")

    ChrTalk(
        0xFE,
        (
            "I didn't talk directly to her or anything,\x01",
            "but seeig Ilya doing her best during\x01",
            "rehabilitation really cheered me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I'll be back in the city after\x01",
            "a short time, I want to tell Ilya's\x01",
            "tenacity to everyone too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A3")

    label("loc_9674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_97A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977D")

    ChrTalk(
        0xFE,
        (
            "I had a fleeting expectation\x01",
            "to maybe meet Ilya since\x01",
            "she's hospitalised here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I saw her doing her best in\x01",
            "rehabilitation with a staggering look,\x01",
            "the super fan in me was blown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I wish she does her best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 1)
    Jump("loc_97A3")

    label("loc_977D")


    ChrTalk(
        0xFE,
        "Ilya...I wish she does her best.\x02",
    )

    CloseMessageWindow()

    label("loc_97A3")

    TalkEnd(0xFE)
    Return()

    # Function_46_9582 end

    def Function_47_97A7(): pass

    label("Function_47_97A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_981E")

    ChrTalk(
        0xFE,
        (
            "Aah, so booored.\x01",
            "It's a hospital so I can't\x01",
            "even read Hot Shot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Won't anyone come see me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_98DB")

    label("loc_981E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_98DB")

    ChrTalk(
        0xFE,
        (
            "I only got a compound fracture\x01",
            "and got carried to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's improved quite a lot, but since\x01",
            "going back to the city seems quite\x01",
            "troublesome too, I don't want to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98DB")

    TalkEnd(0xFE)
    Return()

    # Function_47_97A7 end

    def Function_48_98DF(): pass

    label("Function_48_98DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9962")

    ChrTalk(
        0xFE,
        (
            "What in the world is that azure pale\x01",
            "tree you can see in eastern skies...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, o Goddess.\x01",
            "Save us...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99E3")

    label("loc_9962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_99E3")

    ChrTalk(
        0xFE,
        (
            "What will be of Crossbell...?\x01",
            "Only the Goddess can tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray she points out to us\x01",
            "the path to salvation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99E3")

    TalkEnd(0xFE)
    Return()

    # Function_48_98DF end

    def Function_49_99E7(): pass

    label("Function_49_99E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9AAB")

    ChrTalk(
        0xFE,
        (
            "I feel really relieved since it's been\x01",
            "decided that I can leave the hospital today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside the situation is like that, but...\x01",
            "I want to go home and reassure my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B04")

    label("loc_9AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AC6")
    Call(0, 15)
    Jump("loc_9B04")

    label("loc_9AC6")


    ChrTalk(
        0xFE,
        (
            "*phew*, if the doctor says so,\x01",
            "it should be all right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B04")

    TalkEnd(0xFE)
    Return()

    # Function_49_99E7 end

    def Function_50_9B08(): pass

    label("Function_50_9B08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9BBD")

    ChrTalk(
        0xFE,
        "The doctors doing the rounds look very busy too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all it seems that outpatients are coming in droves.\x01",
            "I hope they do their best in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C9B")

    label("loc_9BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9C9B")

    ChrTalk(
        0xFE,
        (
            "It appears that even in a hospital there're many problems,\x01",
            "but it seems that the doctors are doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing less expected from St. Ursula Hospital...\x01",
            "We can get hospitalised and feel at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C9B")

    TalkEnd(0xFE)
    Return()

    # Function_50_9B08 end

    def Function_51_9C9F(): pass

    label("Function_51_9C9F")

    Sound(160, 0, 100, 0)
    Return()

    # Function_51_9C9F end

    def Function_52_9CA6(): pass

    label("Function_52_9CA6")

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
        "Honestly, you girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Couldn't you stop making mistakes\x01",
            "in the purchase orders already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uhhm, there's something off here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I compiled the purchase order,\x01",
            "Meihua was strictly watching me㈱\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even so, I ended up mistaking\x01",
            "the digits about 20 times, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...*haah*, I can picture \x01",
            "Meihua's hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExcuse us...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, this girl was\x01",
            "entrusted with the medical\x01",
            "articles purchase order, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I looked at the delivered\x01",
            "package, there was a worn out\x01",
            "doll inside it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This girl, previously\x01",
            "she mistook and ordered\x01",
            "absurd general goods too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uuh, please believe me.\x01",
            "I told you that I made it right this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Lloyd, don't you think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, that's proof of it.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FWell, you see...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about the\x01",
            "misdelivered packages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "A misdelivery...\x01",
            "So that's what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWe're currently in the midst\x01",
            "of redelivering things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThis is the package that was\x01",
            "addressed to the hospital, right?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x330, 1)

    ChrTalk(
        0xA,
        (
            "Hm...indeed, these are the medical\x01",
            "tools I had asked to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you for having come\x01",
            "on purpose to deliver them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "Also...\x01",
            "I'm sorry, Xilun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that just this time\x01",
            "I jumped to conclusions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu, it's ok.\x01",
            "Of course I don't mind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, that's right.\x01",
            "I wonder if they have put THAT in too...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Xilun put her hand deep inside the\x01",
            "bag and groped for something.\x07\x00\x02",
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
            "Ah, here it is!\x01",
            "The "Kagemaru"'s strap!㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since I was doing a purchase,\x01",
            "I ordered it together.\x01",
            "Uhuhu, how cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Xilun, as I thought I'll\x01",
            "have to lecture you later.\x02",
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
            "#00006FE-Eehm...\x02\x03",
            "#00000FExcuse me, but could\x01",
            "we have the package\x01",
            "that was misdelivered?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Yeah, that's right.\x01",
            "Wait a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Here, this is it.\x01",
            "You can have it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33A, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThank you very much.\x02\x03",
            "#00003FLet's see, according to the sales\x01",
            "slip we got from Mr. Aaron...\x02\x03",
            "#00000FThe receiver's address is a private \x01",
            "house in Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A798():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A798)
    Sleep(50)

    def lambda_A7A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A7A8)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FWhen we deliver that, the request\x01",
            "will be officially completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FResidential Street...\x01",
            "Chairman MacDowell's\x01",
            "residence is there too, right?\x02\x03",
            "#10300FElie, do you know\x01",
            "where is this address?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A88B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A88B)
    Sleep(50)

    def lambda_A89B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A89B)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FUhhm, let's see...\x02",
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
            "#00105FOh, but isn't this address...\x02\x03",
            "The empty house near\x01",
            "congressman Campbell's?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE1")
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
            "The Residential Street Empty House (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",                                        # 0
            "[Entered in for Thief B quest]\x01",                     # 1
            "[Investigated in Zero for Vacant Units quest]\x01",      # 2
            "[You did not investigate it]\x01",                       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAC7")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x1, 0x2)
    Jump("loc_AAE1")

    label("loc_AAC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAE1")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x2, 0x2)

    label("loc_AAE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_AB73")

    ChrTalk(
        0x101,
        (
            "#00005FWait, the one clamored\x01",
            "to have been a haunted\x01",
            "house for at least ten years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FY-Yes...I'm sure it's that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC5C")

    label("loc_AB73")


    ChrTalk(
        0x101,
        (
            "#00005FWasn't that the name of a\x01",
            "Republican Faction congressman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes... He has a mansion on the \x01",
            "north side of Residential Street.\x02\x03",
            "#00101FThe one next to his should've been an\x01",
            "empty house for more than ten years...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC5C")


    ChrTalk(
        0x104,
        (
            "#00305F...What's goin' on then?\x02\x03",
            "#00300FCould a tenant have\x01",
            "moved in just recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FUhhm, I don't really know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...In any case, let's try to\x01",
            "go deliver the package.\x02",
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

    # Function_52_9CA6 end

    def Function_53_AD76(): pass

    label("Function_53_AD76")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is the 301, right?\x01",
            "Let's go see how she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 8600, 0, 3680, 180)
    EventEnd(0x4)
    Return()

    # Function_53_AD76 end

    def Function_54_ADD6(): pass

    label("Function_54_ADD6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is the 301, right?\x01",
            "Let's go see how she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26800, 0, -25170, 0)
    EventEnd(0x4)
    Return()

    # Function_54_ADD6 end

    SaveToFile()

Try(main)
