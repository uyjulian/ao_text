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
        "Function_4_1841",         # 04, 4
        "Function_5_1D6C",         # 05, 5
        "Function_6_1D70",         # 06, 6
        "Function_7_2E96",         # 07, 7
        "Function_8_4254",         # 08, 8
        "Function_9_43BA",         # 09, 9
        "Function_10_447D",        # 0A, 10
        "Function_11_4973",        # 0B, 11
        "Function_12_4B1F",        # 0C, 12
        "Function_13_4D28",        # 0D, 13
        "Function_14_51CE",        # 0E, 14
        "Function_15_5E1C",        # 0F, 15
        "Function_16_5F27",        # 10, 16
        "Function_17_633D",        # 11, 17
        "Function_18_64C5",        # 12, 18
        "Function_19_6602",        # 13, 19
        "Function_20_68B6",        # 14, 20
        "Function_21_6ADD",        # 15, 21
        "Function_22_6DA7",        # 16, 22
        "Function_23_70FE",        # 17, 23
        "Function_24_72BF",        # 18, 24
        "Function_25_7606",        # 19, 25
        "Function_26_7679",        # 1A, 26
        "Function_27_770A",        # 1B, 27
        "Function_28_7750",        # 1C, 28
        "Function_29_780C",        # 1D, 29
        "Function_30_7993",        # 1E, 30
        "Function_31_7AC0",        # 1F, 31
        "Function_32_7C29",        # 20, 32
        "Function_33_7CCE",        # 21, 33
        "Function_34_7D58",        # 22, 34
        "Function_35_7E78",        # 23, 35
        "Function_36_8068",        # 24, 36
        "Function_37_80BF",        # 25, 37
        "Function_38_8155",        # 26, 38
        "Function_39_851E",        # 27, 39
        "Function_40_860F",        # 28, 40
        "Function_41_873D",        # 29, 41
        "Function_42_89C5",        # 2A, 42
        "Function_43_8D87",        # 2B, 43
        "Function_44_8E2D",        # 2C, 44
        "Function_45_8FA7",        # 2D, 45
        "Function_46_90D9",        # 2E, 46
        "Function_47_92D5",        # 2F, 47
        "Function_48_9407",        # 30, 48
        "Function_49_94E5",        # 31, 49
        "Function_50_95F1",        # 32, 50
        "Function_51_9781",        # 33, 51
        "Function_52_9788",        # 34, 52
        "Function_53_A7C1",        # 35, 53
        "Function_54_A821",        # 36, 54
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1359")
    Call(0, 4)
    Jump("loc_14D1")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1421")

    ChrTalk(
        0x8,
        (
            "#01304FNow that the SSS members are all\x01",
            "together, I'm sure you'll be able\x01",
            "to solve the chain of incidents.\x02\x03",
            "#01300FI will be cheering you on from\x01",
            "here. Please do your best, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D1")

    label("loc_1421")


    ChrTalk(
        0x8,
        (
            "#01304FHaha. This being the case,\x01",
            "I've got to my best with my\x01",
            "work at the hospital as well.\x02\x03",
            "#01300FI am sure the Goddess is\x01",
            "watching over. Everyone,\x01",
            "please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D1")

    Jump("loc_183D")

    label("loc_14D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_156C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1567")

    ChrTalk(
        0x8,
        (
            "#01300FPlease say hello to your\x01",
            "chief and KeA for me.\x02\x03",
            "It's a tough situation,\x01",
            "but... Let's all do our\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1567")

    label("loc_1567")

    Jump("loc_183D")

    label("loc_156C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_157A")
    Jump("loc_183D")

    label("loc_157A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1588")
    Jump("loc_183D")

    label("loc_1588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1781")

    ChrTalk(
        0x8,
        (
            "#01308FDue to Shizuku's surgery,\x01",
            "the mood at the hospital\x01",
            "has become very gloomy.\x02\x03",
            "#01300FHowever, it's precisely\x01",
            "in times like these that\x01",
            "we nurses must smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're right. I feel\x01",
            "like we've been helped\x01",
            "by KeA's smile...\x02\x03",
            "#00009FWith your smile, I'm\x01",
            "sure the patients will\x01",
            "feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm sure their\x01",
            "worries will be blown\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01309FHaha, thank you.\x02\x03",
            "#01300FShizuku is positive about\x01",
            "it as well. We've got to\x01",
            "pull ourselves together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1813")

    label("loc_1781")


    ChrTalk(
        0x8,
        (
            "#01300FIt's precisely in gloomy\x01",
            "times like this that we\x01",
            "nurses must smile.\x02\x03",
            "It is also a duty of us\x01",
            "nurses to relieve our\x01",
            "patients' worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1813")

    Jump("loc_183D")

    label("loc_1818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1826")
    Jump("loc_183D")

    label("loc_1826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1834")
    Jump("loc_183D")

    label("loc_1834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_183D")

    label("loc_183D")

    TalkEnd(0xFE)
    Return()

    # Function_3_133B end

    def Function_4_1841(): pass

    label("Function_4_1841")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1923")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18F8")
    SetChrPos(0x109, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_1923")

    label("loc_18F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1923")
    SetChrPos(0x105, 101220, 0, -300, 41)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1923")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1961")
    SetChrPos(0x105, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_198C")

    label("loc_1961")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_198C")
    SetChrPos(0x109, 104020, 0, -60, 311)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_198C")

    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P#01305FOh, Lloyd, everyone!\x02\x03",
            "#01309FHaha, it seems the SSS\x01",
            "members are all together\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, finally.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5D")

    ChrTalk(
        0x105,
        (
            "#12P#10402FHaha, it's thanks to\x01",
            "your support.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5D")


    ChrTalk(
        0x102,
        (
            "#12P#00100FSorry to have worried\x01",
            "you, Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01300FElie... and everyone\x01",
            "else too. You seem to\x01",
            "have gone through a lot.\x02\x03",
            "#01304FHaha, but I wonder\x01",
            "why...\x02\x03",
            "#01302FTo me, it seems like\x01",
            "your bonds have deepened\x01",
            "more than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FAlthough we managed to\x01",
            "reach this point, there\x01",
            "were a lot of hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FMaybe that makes the\x01",
            "sense of accomplishment\x01",
            "even greater.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C3F")

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha... There're still\x01",
            "a heap of things to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3F")


    ChrTalk(
        0x8,
        (
            "#5P#01304FIt seems the hard times will\x01",
            "continue, but...\x02\x03",
            "#01300FI'm sure that, if it is you\x01",
            "all, you'll be able to solve\x01",
            "this chain of incidents.\x02\x03",
            "#01309FPlease do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1AC, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 102700, 0, 940, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D46")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1D46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5E")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1D5E")

    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_4_1841 end

    def Function_5_1D6C(): pass

    label("Function_5_1D6C")

    Call(0, 6)
    Return()

    # Function_5_1D6C end

    def Function_6_1D70(): pass

    label("Function_6_1D70")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E57")

    ChrTalk(
        0x9,
        (
            "For a tree like that to\x01",
            "appear... T-Things have\x01",
            "really gotten serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The head nurse told me to\x01",
            "keep composed so as not\x01",
            "worry the patients, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, I really can't\x01",
            "stay calm...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EEB")

    label("loc_1E57")


    ChrTalk(
        0x9,
        (
            "Oh, if you're looking for\x01",
            "Cecil, she went to the lounge\x01",
            "after seeing that big tree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, Cecil is cool\x01",
            "with how calm she is and\x01",
            "all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEB")

    Jump("loc_2E92")

    label("loc_1EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1FA6")

    ChrTalk(
        0x9,
        (
            "I'm treating the inpatients\x01",
            "and outpatients who can't\x01",
            "return to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After what happened in the\x01",
            "city, it seems this situation\x01",
            "will continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E92")

    label("loc_1FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CA")

    ChrTalk(
        0x9,
        (
            "Mr. Donovan's recovery is\x01",
            "progressing well, so I think\x01",
            "he'll be discharged soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, they say that even if Ilya\x01",
            "undergoes intense rehab, they don't\x01",
            "know if she'll recover fully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope she does her best\x01",
            "and manages to make a\x01",
            "comeback somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218B")

    label("loc_20CA")


    ChrTalk(
        0x9,
        (
            "However, they say that even if Ilya\x01",
            "undergoes intense rehab, they don't\x01",
            "know if she'll recover fully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, making us feel an\x01",
            "indescribable hope is one\x01",
            "of Ilya's amazing traits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218B")

    Jump("loc_2E92")

    label("loc_2190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_22C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0x9,
        (
            "Ilya and Mr. Donovan\x01",
            "have regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately, bad things are all anyone talks about\x01",
            "and I'm honestly feeling down, but... I'm glad\x01",
            "a cheerful topic of conversation has appeared.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22BF")

    label("loc_2273")


    ChrTalk(
        0x9,
        (
            "I'm really glad that Ilya\x01",
            "and Mr. Donovan have\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BF")

    Jump("loc_2E92")

    label("loc_22C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_248D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23ED")

    ChrTalk(
        0x9,
        (
            "The people of the CGF were\x01",
            "housed in the ICU in the\x01",
            "research building, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone suffered severe injuries\x01",
            "from the jaegers and it'll be some\x01",
            "time before they're discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Many patients have been\x01",
            "hospitalised until now,\x01",
            "but... I averted my eyes...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2488")

    label("loc_23ED")


    ChrTalk(
        0x9,
        (
            "Many patients have been\x01",
            "hospitalised up to this\x01",
            "point, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I averted my eyes from the\x01",
            "injuries of the CGF soldiers\x01",
            "who were put in the ICU...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2488")

    Jump("loc_2E92")

    label("loc_248D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255C")

    ChrTalk(
        0x9,
        (
            "It seems things have finally\x01",
            "calmed down after dealing\x01",
            "with yesterday's derailment.\x02",
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
            "...Now that I think about\x01",
            "it, I haven't eaten\x01",
            "enough. I'm hungry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25B0")

    label("loc_255C")


    ChrTalk(
        0x9,
        (
            "Being busy I haven't\x01",
            "eaten enough. I'm\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll go have a meal\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B0")

    Jump("loc_2E92")

    label("loc_25B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_281A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2729")

    ChrTalk(
        0x9,
        (
            "It seems Professor Seiland is\x01",
            "reworking a surgical operation\x01",
            "for healing Shizuku's eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At first, I thought she was feeling down\x01",
            "and it was hard to talk to her, but...\x01",
            "She's already changed her way of thinking.\x02",
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
    Jump("loc_2815")

    label("loc_2729")


    ChrTalk(
        0x9,
        (
            "Immediately changing your way of\x01",
            "thinking when things don't go well is\x01",
            "more difficult than you might think.\x02",
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

    label("loc_2815")

    Jump("loc_2E92")

    label("loc_281A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(
        0x9,
        (
            "When I was feeling down due to\x01",
            "Shizuku's surgery, the head\x01",
            "nurse suddenly slapped my butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, that surprised\x01",
            "me... It's still\x01",
            "tingles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, thanks to that, my gloomy\x01",
            "feelings have been blown away for some\x01",
            "reason. I must do my best today too, yes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A17")

    label("loc_2944")


    ChrTalk(
        0x9,
        (
            "Thanks to having been slapped, my gloomy\x01",
            "feelings have been blown off for some\x01",
            "reason. That's Head Nurse Martha for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, I would've liked\x01",
            "she had held back a little.\x01",
            "My butt still tingles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A17")

    Jump("loc_2E92")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2ADF")

    ChrTalk(
        0x9,
        (
            "I'm happy Mihail is\x01",
            "leaving the hospital.\x01",
            "However, we'll miss him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Especially Shizuku. I think she'll\x01",
            "miss him the most because they're\x01",
            "so close in age and great friends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E92")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BBD")

    ChrTalk(
        0x9,
        (
            "I wanted to go see the\x01",
            "Orchis Tower unveiling\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it's not so\x01",
            "easy to take days off\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can't be helped if\x01",
            "we're busy, but I'd like\x01",
            "to have some fun soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C6F")

    label("loc_2BBD")


    ChrTalk(
        0x9,
        (
            "I even doubt if I'll be able to\x01",
            "wait in line to buy tickets for\x01",
            "the next Arc-en-Ciel performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can't be helped if\x01",
            "we're busy, but I'd like\x01",
            "to have some fun soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6F")

    Jump("loc_2E92")

    label("loc_2C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E18")

    ChrTalk(
        0x9,
        (
            "Good morniiing, this is\x01",
            "the nurses' station...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Wait, aah! Little bro\x01",
            "and Randyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHey there, Filia.\x02",
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
            "It really iiis! Haha,\x01",
            "but you look well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Randy, my schedule\x01",
            "will be open soon!\x02",
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
            "#10106FRandy, you still promise\x01",
            "those things so\x01",
            "easily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F*sigh*, my oh my.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 5)
    Jump("loc_2E92")

    label("loc_2E18")


    ChrTalk(
        0x9,
        (
            "I want to go on a group\x01",
            "date with everyone one\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Little bro, you'll\x01",
            "definitely have to come\x01",
            "when it happens!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E92")

    TalkEnd(0x9)
    Return()

    # Function_6_1D70 end

    def Function_7_2E96(): pass

    label("Function_7_2E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EBF")
    Call(0, 52)
    Return()

    label("loc_2EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE9")

    ChrTalk(
        0xFE,
        (
            "Now that we're accepting outpatients\x01",
            "again, this place is busier than\x01",
            "it's been in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems a lot of outpatients have come\x01",
            "to make up for the fact that we haven't\x01",
            "been able to see them until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I'll give it my\x01",
            "all and work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_307B")

    label("loc_2FE9")


    ChrTalk(
        0xFE,
        (
            "I asked Harold to bring us the\x01",
            "goods we're lacking. The patient\x01",
            "acceptance system is perfect now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll give it my all and\x01",
            "be work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307B")

    Jump("loc_4250")

    label("loc_3080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3125")

    ChrTalk(
        0xFE,
        (
            "I'm going to the\x01",
            "outpatients at the\x01",
            "dormitory.\x02",
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
    Jump("loc_4250")

    label("loc_3125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327D")

    ChrTalk(
        0xFE,
        (
            "Anyway, the fact that only patients with\x01",
            "serious illnesses or injuries can be\x01",
            "taken to the hospital is an absurd rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only natural that there are\x01",
            "illnesses and wounds that can't\x01",
            "be understood just by appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be too awful if\x01",
            "there were patients we could\x01",
            "have saved by treating early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_331F")

    label("loc_327D")


    ChrTalk(
        0xFE,
        (
            "Only patients with serious illnesses\x01",
            "or injuries can get taken to the\x01",
            "hospital... That's an absurd rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if President\x01",
            "Dieter understands that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331F")

    Jump("loc_4250")

    label("loc_3324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_358B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D9")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio... I'm told you're\x01",
            "leaving the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes... Head Nurse Martha,\x01",
            "thank you for everything\x01",
            "you did for me.\x02\x03",
            "#00204FI hope I was able to\x01",
            "repay you for when I was\x01",
            "hospitalised in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, goodness. That's in\x01",
            "the past, so you don't\x01",
            "have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come see me again whenever\x01",
            "you like... And please, be\x01",
            "careful out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHaha, yes. I'll be sure\x01",
            "to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3586")

    label("loc_34D9")


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
            "Come see me again whenever\x01",
            "you like... And please, be\x01",
            "careful out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3586")

    Jump("loc_4250")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_37F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374A")

    ChrTalk(
        0xFE,
        (
            "As a matter of course, we medical\x01",
            "professionals have many chances\x01",
            "to be present when someone dies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why when people like the professors and\x01",
            "I do this job for a long time we end up not\x01",
            "even shedding tears for each person's death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this attack... When I\x01",
            "think about the number of victims,\x01",
            "anger starts boiling within me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carelessly taking away\x01",
            "people's lives... It's\x01",
            "an unforgivable act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37EF")

    label("loc_374A")


    ChrTalk(
        0xFE,
        (
            "There are people like doctors who save\x01",
            "many lives and, on the other hand,\x01",
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

    label("loc_37EF")

    Jump("loc_4250")

    label("loc_37F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380F")
    Call(0, 8)
    Jump("loc_38DE")

    label("loc_380F")


    ChrTalk(
        0xFE,
        (
            "Well, even when it comes to\x01",
            "watching Arc-en-Ciel performances,\x01",
            "where there's life, there's hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have to be grateful to the\x01",
            "Goddess that you're safe and focus\x01",
            "on healing your injuries for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DE")

    Jump("loc_4250")

    label("loc_38E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3908")
    Call(0, 9)
    Jump("loc_397E")

    label("loc_3908")


    ChrTalk(
        0xFE,
        (
            "You can't even say\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I think about the mistakes\x01",
            "you've made until now, you're\x01",
            "really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397E")

    Jump("loc_3A47")

    label("loc_3983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A08")

    ChrTalk(
        0xFE,
        (
            "Thank you for having\x01",
            "come all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to lecture this\x01",
            "girl here right now, so\x01",
            "see you later, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A47")

    label("loc_3A08")


    ChrTalk(
        0xFE,
        (
            "Goodness gracious...\x01",
            "Looking after Xilun is\x01",
            "really tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A47")

    Jump("loc_4250")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA4")

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
            "I understand how they feel since\x01",
            "it concerns that Shizuku. Anyone\x01",
            "would feel down after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if we seem\x01",
            "depressed, the other\x01",
            "patients will become uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is precisely in times like\x01",
            "these that we must show our\x01",
            "cheerfulness. That's what I think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C4B")

    label("loc_3BA4")


    ChrTalk(
        0xFE,
        (
            "Honestly, it's not good\x01",
            "that they're all feeling\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it's a put-on cheeriness,\x01",
            "cheeriness is the most important\x01",
            "thing. Come on, you too, cheer up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4B")

    Jump("loc_4250")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1C")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "My, my, my! Isn't that\x01",
            "Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, long time no see!\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FFine, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FTio, do you know the\x01",
            "Head Nurse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. She looked after me\x01",
            "when I was hospitalized\x01",
            "here before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahaha, as a nurse, I\x01",
            "didn't do anything\x01",
            "special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being a police officer is\x01",
            "difficult too, but watch out for\x01",
            "your health and do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FWe will... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 4)
    Jump("loc_3EBB")

    label("loc_3E1C")


    ChrTalk(
        0xFE,
        (
            "I've said it before, but\x01",
            "Tio has become a real\x01",
            "beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being a police officer is\x01",
            "difficult too, but watch out for\x01",
            "your health and do your very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBB")

    Jump("loc_4250")

    label("loc_3EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4098")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF4")

    ChrTalk(
        0xFE,
        (
            "No matter the person, Cecil\x01",
            "doesn't discriminate and can\x01",
            "connect compassionately with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She makes it look easy, but there\x01",
            "aren't many people who can do that.\x01",
            "I think she has magnificent talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Maybe it was the\x01",
            "Goddess' will that guided\x01",
            "her to be a nurse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4093")

    label("loc_3FF4")


    ChrTalk(
        0xFE,
        (
            "Compassion can give peace of\x01",
            "mind to the patients. It's\x01",
            "Cecil's splendid talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Maybe it was the\x01",
            "Goddess' will that guided\x01",
            "her to be a nurse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4093")

    Jump("loc_4250")

    label("loc_4098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E9")

    ChrTalk(
        0xFE,
        (
            "Professor Seiland is\x01",
            "quite famous in\x01",
            "Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She is a doctor of medicine and they say she has\x01",
            "deep ties to the Archduke's family. Well, you\x01",
            "can say that she has good references, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore and more than anything,\x01",
            "I like her scrappy attitude. That's\x01",
            "how a woman has to be nowadays.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4250")

    label("loc_41E9")


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
        (
            "Nowadays, a woman has to\x01",
            "be like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4250")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E96 end

    def Function_8_4254(): pass

    label("Function_8_4254")

    OP_4B(0xA, 0xFF)
    OP_4B(0x17, 0xFF)

    ChrTalk(
        0x17,
        (
            "Though I came to watch the long\x01",
            "awaited Arc-en-Ciel performance, I\x01",
            "got caught up in a train accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Ooh, what a pity...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, now that you mention it,\x01",
            "tomorrow is opening night\x01",
            "for the renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, where there's life, there's\x01",
            "hope. You have to be grateful to\x01",
            "the Goddess that you were saved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x17, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x17, 0xFF)
    Return()

    # Function_8_4254 end

    def Function_9_43BA(): pass

    label("Function_9_43BA")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Honestly, girl... How many\x01",
            "times are you going to\x01",
            "repeat the same mistakes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ooh, but I did it\x01",
            "properly like I told\x01",
            "you!\x02",
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

    # Function_9_43BA end

    def Function_10_447D(): pass

    label("Function_10_447D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A6")
    Call(0, 52)
    Return()

    label("loc_44A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C4")
    Call(0, 12)
    Jump("loc_4533")

    label("loc_44C4")


    ChrTalk(
        0xFE,
        (
            "Tee-hee-hee, they look similar so I\x01",
            "made a mistake. On closer inspection,\x01",
            "their dimensions are different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4533")

    Jump("loc_496F")

    label("loc_4538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_45A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4553")
    Call(0, 12)
    Jump("loc_459B")

    label("loc_4553")


    ChrTalk(
        0xFE,
        (
            "I wonder if Baggio,\x01",
            "father and mother in the\x01",
            "city are all right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459B")

    Jump("loc_496F")

    label("loc_45A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_45AE")
    Jump("loc_496F")

    label("loc_45AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_45BC")
    Jump("loc_496F")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AD")

    ChrTalk(
        0xFE,
        (
            "...It was the first time\x01",
            "I saw so many patients\x01",
            "brought here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all looked like they were\x01",
            "in great pain... Since then,\x01",
            "I've been afraid to be alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have Meihua stay\x01",
            "with me again tonight...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_473C")

    label("loc_46AD")


    ChrTalk(
        0xFE,
        (
            "I got scared because it was\x01",
            "the first time I saw so many\x01",
            "patients being brought here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have Meihua stay\x01",
            "with me again tonight...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473C")

    Jump("loc_496F")

    label("loc_4741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_474F")
    Jump("loc_496F")

    label("loc_474F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4774")
    Call(0, 9)
    Jump("loc_47C9")

    label("loc_4774")


    ChrTalk(
        0xFE,
        (
            "I'm telling you, it must\x01",
            "have been some mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, please believe\x01",
            "meee!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C9")

    Jump("loc_4934")

    label("loc_47CE")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C2")

    ChrTalk(
        0xFE,
        (
            "Ehehe, a Kagemaru\x01",
            "strap... I'm glad it got\x01",
            "delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FKagemaru is nice... I\x01",
            "like him too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right☆ See, isn't\x01",
            "he cuuute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...HEY, are you\x01",
            "listening!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TurnDirection(0xFE, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_4930")

    label("loc_48C2")


    ChrTalk(
        0xFE,
        (
            "Ooh, Head Nurse Martha,\x01",
            "here, pease look!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't this Kagemaru\x01",
            "strap suuuper cuuute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Who cares!\x02",
    )

    CloseMessageWindow()

    label("loc_4930")

    OP_4C(0xA, 0xFF)

    label("loc_4934")

    Jump("loc_496F")

    label("loc_4939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4947")
    Jump("loc_496F")

    label("loc_4947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4955")
    Jump("loc_496F")

    label("loc_4955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4963")
    Jump("loc_496F")

    label("loc_4963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_496F")
    Call(0, 11)

    label("loc_496F")

    TalkEnd(0xFE)
    Return()

    # Function_10_447D end

    def Function_11_4973(): pass

    label("Function_11_4973")

    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x10, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD4")

    ChrTalk(
        0xB,
        (
            "Aaallright, let's do an\x01",
            "IV drip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Ooh... Nurse, will it go\x01",
            "all right today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What if you stick me in\x01",
            "the wrong place again and\x01",
            "blood comes gushing out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh c'mon. My aim was off\x01",
            "last time, that's all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, please don't\x01",
            "worry. It will probably\x01",
            "be definitely all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "(I-I'm too worried...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_4B16")

    label("loc_4AD4")


    ChrTalk(
        0xB,
        (
            "...Huh? I guess I forgot\x01",
            "the needle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "P-Please, nurse...\x02",
    )

    CloseMessageWindow()

    label("loc_4B16")

    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_11_4973 end

    def Function_12_4B1F(): pass

    label("Function_12_4B1F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C32")

    ChrTalk(
        0xC,
        (
            "Then, Xilun, let's split\x01",
            "up and go measure the\x01",
            "inpatients' temperatures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Right, Meihua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You have the medical\x01",
            "thermometer, don't you!?\x02",
        )
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
            "...What you're holding\x01",
            "isn't a medical\x01",
            "thermometer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Uh, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D1C")

    label("loc_4C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D1C")

    ChrTalk(
        0xB,
        "Meihua, what's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm a little scared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems something big\x01",
            "happened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, you don't have to\x01",
            "worry. Everything will be fine\x01",
            "if we just do what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "R-Right...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_4D1C")

    SetScenarioFlags(0x3, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_4B1F end

    def Function_13_4D28(): pass

    label("Function_13_4D28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D46")
    Call(0, 12)
    Jump("loc_4D7D")

    label("loc_4D46")


    ChrTalk(
        0xFE,
        (
            "She has everything\x01",
            "wrong! ...Honestly, this\x01",
            "girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D7D")

    Jump("loc_51CA")

    label("loc_4D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9D")
    Call(0, 12)
    Jump("loc_4E1D")

    label("loc_4D9D")


    ChrTalk(
        0xFE,
        (
            "It seems certain that\x01",
            "something big happened\x01",
            "in the city, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's important right\x01",
            "now is to do all that we\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E1D")

    Jump("loc_51CA")

    label("loc_4E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4E30")
    Jump("loc_51CA")

    label("loc_4E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4E3E")
    Jump("loc_51CA")

    label("loc_4E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2E")

    ChrTalk(
        0xFE,
        (
            "The kids that were brought to room No.\x01",
            "202 were really energetic at first, but\x01",
            "they calmed down after a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it's not just due to\x01",
            "their injuries. I wonder what\x01",
            "happened in the city...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FB3")

    label("loc_4F2E")


    ChrTalk(
        0xFE,
        (
            "Come to think of it,\x01",
            "Xilun seems frightened\x01",
            "lately for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder what\x01",
            "will happen to us from\x01",
            "now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB3")

    Jump("loc_51CA")

    label("loc_4FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4FC6")
    Jump("loc_51CA")

    label("loc_4FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4FD4")
    Jump("loc_51CA")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4FE2")
    Jump("loc_51CA")

    label("loc_4FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4FF0")
    Jump("loc_51CA")

    label("loc_4FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_51C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511D")

    ChrTalk(
        0xFE,
        (
            "The other day, that\x01",
            "Xilun was basking in the\x01",
            "sun on the rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, she wrapped herself in the\x01",
            "sheets she put out to dry with a happy\x01",
            "look on her face... Really, unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aah, I've got a bad\x01",
            "feeling. Like she's doing\x01",
            "the same thing again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51BC")

    label("loc_511D")


    ChrTalk(
        0xFE,
        (
            "The other day, that Xilun was\x01",
            "basking in the sun on the rooftop.\x01",
            "She also dirtied the sheets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I think I'll go check\x01",
            "on her later, just in\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BC")

    Jump("loc_51CA")

    label("loc_51C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51CA")

    label("loc_51CA")

    TalkEnd(0xFE)
    Return()

    # Function_13_4D28 end

    def Function_14_51CE(): pass

    label("Function_14_51CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_535B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52CF")

    ChrTalk(
        0xFE,
        (
            "After brief hospital rounds,\x01",
            "I have surgeries to do.\x01",
            "...Man, I'm really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, no matter where\x01",
            "it happens, what we must\x01",
            "do won't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To help the patient in\x01",
            "front of you... That's\x01",
            "the job of a doctor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5356")

    label("loc_52CF")


    ChrTalk(
        0xFE,
        (
            "No matter where it\x01",
            "happens, what we must do\x01",
            "won't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To help the patient in\x01",
            "front of you... That's\x01",
            "the job of a doctor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5356")

    Jump("loc_5E18")

    label("loc_535B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_53B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5376")
    Call(0, 15)
    Jump("loc_53B0")

    label("loc_5376")


    ChrTalk(
        0xFE,
        (
            "Our hospital staff is\x01",
            "excellent. Please don't\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B0")

    Jump("loc_5E18")

    label("loc_53B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_53C6")
    Call(0, 41)
    Jump("loc_5E18")

    label("loc_53C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_55FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5522")

    ChrTalk(
        0xFE,
        (
            "The police officers and\x01",
            "delinquents hospitalised here\x01",
            "have already been discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, I'd monitor their condition with follow-\x01",
            "up appointments, but due to the highway movement\x01",
            "restrictions, that's currently not possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a doctor, I can't help but\x01",
            "question this...\x01",
            "irresponsible compulsory act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55F7")

    label("loc_5522")


    ChrTalk(
        0xFE,
        (
            "I normally monitor discharged patients'\x01",
            "progress but due to the highway movement\x01",
            "restrictions, that's currently not possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a doctor, I can't help but\x01",
            "question this...\x01",
            "irresponsible compulsory act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F7")

    Jump("loc_5E18")

    label("loc_55FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E6")

    ChrTalk(
        0xFE,
        (
            "They suffered more\x01",
            "damage to the mind than\x01",
            "the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A patient's mind heals illnesses\x01",
            "and injuries. When they despair,\x01",
            "their recovery is delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they get back on\x01",
            "their feet somehow...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5753")

    label("loc_56E6")


    ChrTalk(
        0xFE,
        (
            "They suffered more\x01",
            "damage to the mind than\x01",
            "the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they get back on\x01",
            "their feet somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5753")

    Jump("loc_5E18")

    label("loc_5758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_57D3")

    ChrTalk(
        0xFE,
        (
            "...I've already treated\x01",
            "his leg fracture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not something\x01",
            "you'll die from, so\x01",
            "please calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E18")

    label("loc_57D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_59F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5926")

    ChrTalk(
        0xFE,
        (
            "When the Surgery Department was\x01",
            "created, at first they said "it's\x01",
            "inexcusable to cut a person's body".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But recently, I feel like\x01",
            "I've gained a deeper\x01",
            "understanding of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the great pioneers who\x01",
            "succeeded and demonstrated the usefulness\x01",
            "of surgery. I have to be thankful for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_59F3")

    label("loc_5926")


    ChrTalk(
        0xFE,
        (
            "Recently, I feel like I've\x01",
            "gained a deeper\x01",
            "understanding of surgeries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the great pioneers who\x01",
            "succeeded and demonstrated the usefulness\x01",
            "of surgery. I have to be thankful for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F3")

    Jump("loc_5E18")

    label("loc_59F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BDA")

    ChrTalk(
        0xFE,
        (
            "Shizuku's condition is an intricate\x01",
            "problem where surgery, internal\x01",
            "medicine and neurology collide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be hard to call it a complete recovery,\x01",
            "but that doesn't mean it was a complete failure.\x01",
            "You could say there's a glimmer of hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You could say that seeking a faint\x01",
            "hope is tougher and more painful than\x01",
            "giving up, in a certain sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I have nothing\x01",
            "but respect for that father and\x01",
            "daughter who never gave up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C80")

    label("loc_5BDA")


    ChrTalk(
        0xFE,
        (
            "In a way, you could say\x01",
            "seeking a faint hope is\x01",
            "tough and painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I have nothing\x01",
            "but respect for that father and\x01",
            "daughter who never gave up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C80")

    Jump("loc_5E18")

    label("loc_5C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C93")
    Jump("loc_5E18")

    label("loc_5C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D85")

    ChrTalk(
        0xFE,
        (
            "Because of the matter of\x01",
            "Joachim, trust in the hospital\x01",
            "fell temporarily, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us doctors, helping\x01",
            "our patients is\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we keep showing that\x01",
            "attitude, we'll regain\x01",
            "that trust for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E0A")

    label("loc_5D85")


    ChrTalk(
        0xFE,
        (
            "To us doctors, helping\x01",
            "our patients is\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we keep showing that\x01",
            "attitude, we'll regain\x01",
            "our lost trust for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E0A")

    Jump("loc_5E18")

    label("loc_5E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E18")

    label("loc_5E18")

    TalkEnd(0xFE)
    Return()

    # Function_14_51CE end

    def Function_15_5E1C(): pass

    label("Function_15_5E1C")

    OP_4B(0xD, 0xFF)
    OP_4B(0x2C, 0xFF)

    ChrTalk(
        0x2C,
        (
            "Doctor... I've heard that the hospital\x01",
            "is lacking all kinds of medicines. Is\x01",
            "it going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...At present, the entire\x01",
            "hospital is working on\x01",
            "countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our hospital staff is\x01",
            "excellent. Please don't\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 5)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x2C, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0x2C, 0xFF)
    Return()

    # Function_15_5E1C end

    def Function_16_5F27(): pass

    label("Function_16_5F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F38")
    Jump("loc_6339")

    label("loc_5F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F46")
    Jump("loc_6339")

    label("loc_5F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5F54")
    Jump("loc_6339")

    label("loc_5F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F62")
    Jump("loc_6339")

    label("loc_5F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6322")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6240")

    ChrTalk(
        0xFE,
        (
            "Lytton's round in room No.\x01",
            "202 was 1 minute 14 seconds\x01",
            "over what was scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already finished here,\x01",
            "and yet he... ...He's still\x01",
            "got a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I thought about this\x01",
            "before, but... You're oddly\x01",
            "strict with times, professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A mere moment can govern life and\x01",
            "death.... That's the kind of world\x01",
            "a medical treatment facility is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To save the most lives, strict\x01",
            "observation of time and acting according\x01",
            "to a schedule is quite obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIndeed... That could\x01",
            "hold true for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, in order to\x01",
            "do that, skills must not\x01",
            "be imperfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To perform their work quickly and\x01",
            "flawlessly. ...I want the young\x01",
            "doctors be like that in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_631D")

    label("loc_6240")


    ChrTalk(
        0xFE,
        (
            "Saving the most lives through strict\x01",
            "observance of time and acting according\x01",
            "to a schedule is quite obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To perform their work quickly and\x01",
            "flawlessly. ...I want the young\x01",
            "doctors be like that in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_631D")

    Jump("loc_6339")

    label("loc_6322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6330")
    Jump("loc_6339")

    label("loc_6330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6339")

    label("loc_6339")

    TalkEnd(0xFE)
    Return()

    # Function_16_5F27 end

    def Function_17_633D(): pass

    label("Function_17_633D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63C7")

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
            "Her words are harsh, but\x01",
            "her medical exams are\x01",
            "extremely considerate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64C1")

    label("loc_63C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_645A")

    ChrTalk(
        0xFE,
        (
            "The meals served here\x01",
            "have excellent\x01",
            "nutritional balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness the\x01",
            "recovery after surgery\x01",
            "is going well somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64C1")

    label("loc_645A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_64C1")

    ChrTalk(
        0xFE,
        (
            "The nurses and doctors\x01",
            "of this hospital are\x01",
            "very kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I quite like inpatient\x01",
            "life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C1")

    TalkEnd(0xFE)
    Return()

    # Function_17_633D end

    def Function_18_64C5(): pass

    label("Function_18_64C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_657D")

    ChrTalk(
        0xFE,
        (
            "That female doctor is\x01",
            "somewhat cool and scary\x01",
            "at the same time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you complain, she gives you\x01",
            "a hostile look... I guess I'll\x01",
            "behave until I'm discharged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65FE")

    label("loc_657D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_65F2")

    ChrTalk(
        0xFE,
        (
            "Aah, I hope I'm\x01",
            "discharged soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've had enough of\x01",
            "frugal meals too. I\x01",
            "wanna eat beefsteak!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65FE")

    label("loc_65F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_65FE")
    Call(0, 11)

    label("loc_65FE")

    TalkEnd(0xFE)
    Return()

    # Function_18_64C5 end

    def Function_19_6602(): pass

    label("Function_19_6602")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_668A")

    ChrTalk(
        0xFE,
        (
            "*peel, peel, peel*...\x01",
            "I'm peeling an apple my\x01",
            "grandchild brought me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, would you like to\x01",
            "eat it with me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B2")

    label("loc_668A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678A")

    ChrTalk(
        0xFE,
        (
            "If I remember correctly,\x01",
            "there's the unveiling\x01",
            "ceremony in the city today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to see that\x01",
            "Orchis Tower or whatever\x01",
            "it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think I'll leave it\x01",
            "as something to look forward\x01",
            "to after my discharge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_681F")

    label("loc_678A")


    ChrTalk(
        0xFE,
        (
            "I wanted to see that\x01",
            "Orchis Tower or whatever\x01",
            "it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think I'll leave it\x01",
            "as something to look forward\x01",
            "to after my discharge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_681F")

    Jump("loc_68B2")

    label("loc_6824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_68B2")

    ChrTalk(
        0xFE,
        (
            "Previously, the doctors\x01",
            "were in an uproar due to\x01",
            "a big incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a great\x01",
            "hospital. I'm not\x01",
            "worried anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B2")

    TalkEnd(0xFE)
    Return()

    # Function_19_6602 end

    def Function_20_68B6(): pass

    label("Function_20_68B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6928")

    ChrTalk(
        0xFE,
        "Oh, is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's a relief. I\x01",
            "have to get well soon\x01",
            "and return to my job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AD9")

    label("loc_6928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F7")

    ChrTalk(
        0xFE,
        (
            "Though my colleague is\x01",
            "busy, he came to visit\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said to not worry about\x01",
            "work and concentrate on\x01",
            "getting well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's right. In this\x01",
            "case, I'll forget about\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6A59")

    label("loc_69F7")


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
            "For now, I must\x01",
            "concentrate of healing\x01",
            "my injury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A59")

    Jump("loc_6AD9")

    label("loc_6A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6AD9")

    ChrTalk(
        0xFE,
        (
            "I broke my leg in a\x01",
            "traffic accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh man, I have important\x01",
            "work to do and yet I\x01",
            "have to abandon it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD9")

    TalkEnd(0xFE)
    Return()

    # Function_20_68B6 end

    def Function_21_6ADD(): pass

    label("Function_21_6ADD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6B69")

    ChrTalk(
        0xFE,
        (
            "All the sickroom beds\x01",
            "were suddenly occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard there was a big\x01",
            "accident, but I'm really\x01",
            "glad no one died.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DA3")

    label("loc_6B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C27")

    ChrTalk(
        0xFE,
        (
            "I was worried that my husband,\x01",
            "who is at home, wasn't properly\x01",
            "feeding the children, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that man is\x01",
            "trying to cook in his own\x01",
            "way. For now I'm relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DA3")

    label("loc_6C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D24")

    ChrTalk(
        0xFE,
        (
            "My surgery was nothing special,\x01",
            "so it seems my hospitalisation\x01",
            "will be brief as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, being away from\x01",
            "home I'm really worried\x01",
            "about my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband\x01",
            "and children are eating\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6DA3")

    label("loc_6D24")


    ChrTalk(
        0xFE,
        (
            "Being away from home,\x01",
            "I'm really worried about\x01",
            "my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband\x01",
            "and children are eating\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DA3")

    TalkEnd(0xFE)
    Return()

    # Function_21_6ADD end

    def Function_22_6DA7(): pass

    label("Function_22_6DA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6E3F")

    ChrTalk(
        0xFE,
        (
            "To think that a train\x01",
            "derailment accident\x01",
            "would...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, incidents have happened\x01",
            "in rapid succession... That's\x01",
            "disturbing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FA")

    label("loc_6E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA3")

    ChrTalk(
        0xFE,
        (
            "Just for recreation while I'm hospitalised,\x01",
            "I've reread this year's Crossbell Times\x01",
            "starting with the first issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attempted assassination of former\x01",
            "Mayor MacDowell, the Founding Anniversary\x01",
            "Festival, that cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All things considered, a lot of\x01",
            "different things have happened\x01",
            "in this past half year.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7072")

    label("loc_6FA3")


    ChrTalk(
        0xFE,
        (
            "The attempted assassination of the\x01",
            "former mayor, the cult incident, the\x01",
            "terrorists' attack on Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All things considered, a lot of\x01",
            "different things have happened\x01",
            "in this past half year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7072")

    Jump("loc_70FA")

    label("loc_7077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_70FA")

    ChrTalk(
        0xFE,
        (
            "When you're hospitalised,\x01",
            "you have too much time on\x01",
            "your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll read all\x01",
            "the books I've\x01",
            "collected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70FA")

    TalkEnd(0xFE)
    Return()

    # Function_22_6DA7 end

    def Function_23_70FE(): pass

    label("Function_23_70FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71B7")

    ChrTalk(
        0xFE,
        (
            "To cure so many patients\x01",
            "without a hitch... That's\x01",
            "these doctors for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as there's St. Ursula\x01",
            "Hospital, the citizens of\x01",
            "Crossbell can feel at ease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72BB")

    label("loc_71B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D2")
    Call(0, 39)
    Jump("loc_7234")

    label("loc_71D2")


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

    label("loc_7234")

    Jump("loc_72BB")

    label("loc_7239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_72BB")

    ChrTalk(
        0xFE,
        (
            "Doctor Belldine's\x01",
            "medical exams are very\x01",
            "thorough and nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm very happy to be\x01",
            "cared for by skilled\x01",
            "doctors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72BB")

    TalkEnd(0xFE)
    Return()

    # Function_23_70FE end

    def Function_24_72BF(): pass

    label("Function_24_72BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_742A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738D")

    ChrTalk(
        0xFE,
        (
            "Getting hospitalised due\x01",
            "to a train accident is\x01",
            "really pathetic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As pathetic as being\x01",
            "hospitalised for a\x01",
            "strained back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What, do you have\x01",
            "something to say?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7425")

    label("loc_738D")


    ChrTalk(
        0xFE,
        (
            "Getting hospitalised due to a train\x01",
            "accident is as pathetic as being\x01",
            "hospitalised for a strained back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What, do you have\x01",
            "something to say?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7425")

    Jump("loc_7602")

    label("loc_742A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7502")

    ChrTalk(
        0xFE,
        (
            "...The other day, a\x01",
            "friend came to visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting hospitalised for a\x01",
            "strained back is lame so I\x01",
            "didn't tell anyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my mother\x01",
            "spilled it. Cruel... Too\x01",
            "cruel...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7580")

    label("loc_7502")


    ChrTalk(
        0xFE,
        (
            "Getting hospitalised for a\x01",
            "strained back is lame so I\x01",
            "didn't tell anyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I was happy he\x01",
            "came to see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7580")

    Jump("loc_7602")

    label("loc_7585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7602")

    ChrTalk(
        0xFE,
        (
            "Aah, I, a youthful\x01",
            "maiden, being\x01",
            "hospitalised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And furthermore, for a\x01",
            "strained back. Lame...\x01",
            "so lame...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7602")

    TalkEnd(0xFE)
    Return()

    # Function_24_72BF end

    def Function_25_7606(): pass

    label("Function_25_7606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7624")
    Call(0, 8)
    Jump("loc_7675")

    label("loc_7624")


    ChrTalk(
        0xFE,
        (
            "Although I'm safe, my\x01",
            "long awaited Arc-en-\x01",
            "Ciel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, what a pity...\x02",
    )

    CloseMessageWindow()

    label("loc_7675")

    TalkEnd(0xFE)
    Return()

    # Function_25_7606 end

    def Function_26_7679(): pass

    label("Function_26_7679")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7706")

    ChrTalk(
        0xFE,
        (
            "When the train turned\x01",
            "sideways, I thought I\x01",
            "was a goner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being, I\x01",
            "don't want to ride the\x01",
            "train anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7706")

    TalkEnd(0xFE)
    Return()

    # Function_26_7679 end

    def Function_27_770A(): pass

    label("Function_27_770A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_774C")

    ChrTalk(
        0xFE,
        (
            "Ow ow ow ow...! I-I'm\x01",
            "dying! I'm gonna\x01",
            "dieee...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_774C")

    TalkEnd(0xFE)
    Return()

    # Function_27_770A end

    def Function_28_7750(): pass

    label("Function_28_7750")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7808")

    ChrTalk(
        0xFE,
        (
            "...That guy over there.\x01",
            "Although he's a man,\x01",
            "he's squawking so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we managed to survive an\x01",
            "accident like that, we have to\x01",
            "endure at least a little pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7808")

    TalkEnd(0xFE)
    Return()

    # Function_28_7750 end

    def Function_29_780C(): pass

    label("Function_29_780C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_798F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78F6")

    ChrTalk(
        0xFE,
        (
            "Against the might of Red\x01",
            "Constellation, everything we\x01",
            "have wouldn't stand a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're probably causing\x01",
            "the citizens great\x01",
            "worry, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What good are the\x01",
            "police...? I feel so\x01",
            "pathetic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_798F")

    label("loc_78F6")


    ChrTalk(
        0xFE,
        (
            "Against the might of Red\x01",
            "Constellation, everything we\x01",
            "have wouldn't stand a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that Inspector\x01",
            "Donovan recovers somehow\x01",
            "or other...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_798F")

    TalkEnd(0xFE)
    Return()

    # Function_29_780C end

    def Function_30_7993(): pass

    label("Function_30_7993")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A64")

    ChrTalk(
        0xFE,
        (
            "We officers have been cheered\x01",
            "up a whole lot until now by\x01",
            "Fran at the reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really happy she's\x01",
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
    Jump("loc_7ABC")

    label("loc_7A64")


    ChrTalk(
        0xFE,
        (
            "I'm really happy that\x01",
            "Fran regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she gets well\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ABC")

    TalkEnd(0xFE)
    Return()

    # Function_30_7993 end

    def Function_31_7AC0(): pass

    label("Function_31_7AC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B70")

    ChrTalk(
        0xFE,
        (
            "They even seriously\x01",
            "injured Fran from the\x01",
            "reception desk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit...! Why the hell did\x01",
            "we do all that training\x01",
            "at the police academy...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_7C25")

    label("loc_7B70")


    ChrTalk(
        0xFE,
        (
            "Shit...! Why the hell did\x01",
            "we do all that training\x01",
            "at the police academy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even seriously injured Fran\x01",
            "from the reception desk... I\x01",
            "can't stand being so pathetic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C25")

    TalkEnd(0xFE)
    Return()

    # Function_31_7AC0 end

    def Function_32_7C29(): pass

    label("Function_32_7C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7CCA")

    ChrTalk(
        0xFE,
        (
            "Those monsters the\x01",
            "jaegers were using were\x01",
            "terribly well trained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those guys come attack\x01",
            "us again, we'll all be\x01",
            "done for next time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CCA")

    TalkEnd(0xFE)
    Return()

    # Function_32_7C29 end

    def Function_33_7CCE(): pass

    label("Function_33_7CCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D54")

    ChrTalk(
        0xFE,
        (
            "Wald... You wanted to\x01",
            "become strong so badly that\x01",
            "you'd turn into that thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit, it makes no sense\x01",
            "at all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D54")

    TalkEnd(0xFE)
    Return()

    # Function_33_7CCE end

    def Function_34_7D58(): pass

    label("Function_34_7D58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E08")

    ChrTalk(
        0xFE,
        (
            "I had a feud with him, but...\x01",
            "In any case, that guy is no\x01",
            "leader of ours anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather, this might be...\x01",
            "the end of the Saber\x01",
            "Vipers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_7E74")

    label("loc_7E08")


    ChrTalk(
        0xFE,
        (
            "That guy... He's no\x01",
            "leader of ours anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather, this might be...\x01",
            "the end of the Saber\x01",
            "Vipers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E74")

    TalkEnd(0xFE)
    Return()

    # Function_34_7D58 end

    def Function_35_7E78(): pass

    label("Function_35_7E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FEF")

    ChrTalk(
        0xFE,
        (
            "We just suffered some\x01",
            "fractures, but... Kｷki has some\x01",
            "ridiculously heavy injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After arriving at the hospital, he was\x01",
            "taken to the ICU right away... Now he's\x01",
            "receiving treatment in the research lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard them saying that\x01",
            "he hasn't even regained\x01",
            "consciousness yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit, why'd something\x01",
            "like this have to\x01",
            "happen...!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_8064")

    label("loc_7FEF")


    ChrTalk(
        0xFE,
        (
            "Even Slash is totally\x01",
            "scared. He can't even\x01",
            "talk well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shit, why'd something\x01",
            "like this have to\x01",
            "happen...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8064")

    TalkEnd(0xFE)
    Return()

    # Function_35_7E78 end

    def Function_36_8068(): pass

    label("Function_36_8068")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_80BB")

    ChrTalk(
        0xFE,
        (
            "*tremble tremble\x01",
            "tremble*... A m-monster...\x01",
            "A monster attacked...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BB")

    TalkEnd(0xFE)
    Return()

    # Function_36_8068 end

    def Function_37_80BF(): pass

    label("Function_37_80BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8151")

    ChrTalk(
        0xFE,
        (
            "Well, I be cleaning the\x01",
            "nurse's station right\x01",
            "now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's the women's\x01",
            "garden, you see. I can't\x01",
            "help but be nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8151")

    TalkEnd(0xFE)
    Return()

    # Function_37_80BF end

    def Function_38_8155(): pass

    label("Function_38_8155")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8166")
    Jump("loc_851A")

    label("loc_8166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8174")
    Jump("loc_851A")

    label("loc_8174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8185")
    Call(0, 41)
    Jump("loc_851A")

    label("loc_8185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A0")
    Call(0, 40)
    Jump("loc_8253")

    label("loc_81A0")


    ChrTalk(
        0xFE,
        (
            "It's not the case that patients\x01",
            "who are discharged can go back\x01",
            "to the city freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's vigilance about\x01",
            "Cryptids on the highway, but I\x01",
            "feel that it's way too strict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8253")

    Jump("loc_851A")

    label("loc_8258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_83F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_832B")

    ChrTalk(
        0xFE,
        (
            "Police officers are\x01",
            "hospitalised in this\x01",
            "sickroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aside from that Section\x01",
            "Two inspector, none are\x01",
            "seriously injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think they'll be\x01",
            "hospitalized for so\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_83F0")

    label("loc_832B")


    ChrTalk(
        0xFE,
        (
            "That Section Two inspector... He\x01",
            "hasn't regained consciousness yet,\x01",
            "but the worst is over for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he was hospitalised\x01",
            "in room No. 302 on 3F. Please\x01",
            "pay him a visit, if you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F0")

    Jump("loc_851A")

    label("loc_83F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8403")
    Jump("loc_851A")

    label("loc_8403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_841E")
    Call(0, 39)
    Jump("loc_845F")

    label("loc_841E")


    ChrTalk(
        0xFE,
        (
            ""Doctor" Lytton, huh...?\x01",
            "Hmm, that has a nice\x01",
            "ring to it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_845F")

    Jump("loc_851A")

    label("loc_8464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8472")
    Jump("loc_851A")

    label("loc_8472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8503")

    ChrTalk(
        0xFE,
        (
            "Yes, the bone seems to\x01",
            "have taken hold as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be able to walk again\x01",
            "soon if you're patient for a\x01",
            "little longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_851A")

    label("loc_8503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8511")
    Jump("loc_851A")

    label("loc_8511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_851A")

    label("loc_851A")

    TalkEnd(0xFE)
    Return()

    # Function_38_8155 end

    def Function_39_851E(): pass

    label("Function_39_851E")

    OP_4B(0x24, 0xFF)

    ChrTalk(
        0x24,
        (
            "Yes, you're progressing\x01",
            "well. I think you'll be\x01",
            "discharged soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I see, I see. Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha. I feel like I can\x01",
            "trust you too, Dr.\x01",
            "Lytton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I-I-Is that so? Well,\x01",
            "haha... You're\x01",
            "embarrassing me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 0)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x24, 0xFF)
    Return()

    # Function_39_851E end

    def Function_40_860F(): pass

    label("Function_40_860F")

    OP_4B(0x24, 0xFF)
    OP_4B(0x26, 0xFF)

    ChrTalk(
        0x24,
        (
            "Yes, you're progressing\x01",
            "well post-surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Actually, I'd like to\x01",
            "discharge you\x01",
            "immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Aah, come to think of it, there\x01",
            "are those highway movement\x01",
            "restrictions to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Oh man. I guess I have\x01",
            "to stay hospitalised for\x01",
            "a little longer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 3)
    ClearChrFlags(0x24, 0x10)
    ClearChrFlags(0x26, 0x10)
    OP_4C(0x24, 0xFF)
    OP_4C(0x26, 0xFF)
    Return()

    # Function_40_860F end

    def Function_41_873D(): pass

    label("Function_41_873D")

    OP_4B(0x24, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8912")

    ChrTalk(
        0xD,
        (
            "Although the hospital is\x01",
            "receiving aid from the\x01",
            "President...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As expected, it seems that a\x01",
            "lot of anxiety is spreading\x01",
            "among the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Yes. Even ambulance\x01",
            "travel has been greatly\x01",
            "restricted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Perhaps the anxiety of an\x01",
            "intern like me is being\x01",
            "transmitted to the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In this case, they'd\x01",
            "feel anxious even if you\x01",
            "weren't an intern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Either way, we need\x01",
            "to be considerate so the\x01",
            "patients can be at ease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 2)
    Jump("loc_89BC")

    label("loc_8912")


    ChrTalk(
        0x24,
        (
            "So even you, Doctor\x01",
            "Belldine, feel\x01",
            "anxious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Everyone feels like\x01",
            "that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Either way, we need\x01",
            "to be considerate so the\x01",
            "patients can be at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89BC")

    OP_4C(0x24, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_41_873D end

    def Function_42_89C5(): pass

    label("Function_42_89C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_89D6")
    Jump("loc_8D83")

    label("loc_89D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_89E4")
    Jump("loc_8D83")

    label("loc_89E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_89F2")
    Jump("loc_8D83")

    label("loc_89F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4F")

    ChrTalk(
        0xFE,
        (
            "I think there're pros\x01",
            "and cons about Shizuku's\x01",
            "surgery results, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's amazing that there was even just\x01",
            "a little improvement in her eye function. They\x01",
            "couldn't be healed in the slightest until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, we have advanced one\x01",
            "step towards her treatment. The\x01",
            "entire hospital must do its best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_8C09")

    label("loc_8B4F")


    ChrTalk(
        0xFE,
        (
            "Finally, we have advanced one\x01",
            "step towards Shizuku's treatment.\x01",
            "I think that's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, looking at the\x01",
            "patient herself, she has some\x01",
            "preoccupations, as expected...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C09")

    Jump("loc_8D83")

    label("loc_8C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8C1C")
    Jump("loc_8D83")

    label("loc_8C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8D7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF2")

    ChrTalk(
        0xFE,
        (
            "Professor Seiland...\x01",
            "Although she's young, she\x01",
            "has a cool personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She truly is the ideal image\x01",
            "of the "capable female\x01",
            "doctor" I seek to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must study diligently.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_8D75")

    label("loc_8CF2")


    ChrTalk(
        0xFE,
        (
            "Professor Seiland fits the ideal\x01",
            "image of the "capable female\x01",
            "doctor" I seek to be perfectly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must study diligently.\x02",
    )

    CloseMessageWindow()

    label("loc_8D75")

    Jump("loc_8D83")

    label("loc_8D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8D83")

    label("loc_8D83")

    TalkEnd(0xFE)
    Return()

    # Function_42_89C5 end

    def Function_43_8D87(): pass

    label("Function_43_8D87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8DC8")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I want to be\x01",
            "discharged already...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E29")

    label("loc_8DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE3")
    Call(0, 40)
    Jump("loc_8E29")

    label("loc_8DE3")


    ChrTalk(
        0xFE,
        (
            "Oh man. I guess I have\x01",
            "to stay hospitalised for\x01",
            "a little longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E29")

    TalkEnd(0xFE)
    Return()

    # Function_43_8D87 end

    def Function_44_8E2D(): pass

    label("Function_44_8E2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8EE2")

    ChrTalk(
        0xFE,
        (
            "My application went\x01",
            "through so I can return\x01",
            "home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it'll be some time until\x01",
            "State Guard comes again. I guess\x01",
            "I've got to wait patiently...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA3")

    label("loc_8EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8FA3")

    ChrTalk(
        0xFE,
        (
            "A bothersome application is\x01",
            "needed even to return to the\x01",
            "city after being discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can only return to the city\x01",
            "when the State Guard comes on\x01",
            "patrol... How depressing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FA3")

    TalkEnd(0xFE)
    Return()

    # Function_44_8E2D end

    def Function_45_8FA7(): pass

    label("Function_45_8FA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9035")

    ChrTalk(
        0xFE,
        (
            "Even if I complained about\x01",
            "the President, there's\x01",
            "nothing that can be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I've just got to\x01",
            "grin and bear it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90D5")

    label("loc_9035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_90D5")

    ChrTalk(
        0xFE,
        (
            "I have a lot of\x01",
            "complaints against the\x01",
            "President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, even if I stated them,\x01",
            "independence has carried out so\x01",
            "they're largely pointless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90D5")

    TalkEnd(0xFE)
    Return()

    # Function_45_8FA7 end

    def Function_46_90D9(): pass

    label("Function_46_90D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_91C7")

    ChrTalk(
        0xFE,
        (
            "I didn't talk speak with her directly\x01",
            "or anything, but seeing Ilya doing her\x01",
            "best during rehab really cheered me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I arrive back in the city in\x01",
            "a little while, I want to tell\x01",
            "everyone of Ilya's tenacity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92D1")

    label("loc_91C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_92D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92AA")

    ChrTalk(
        0xFE,
        (
            "I had a faint expectation\x01",
            "of meeting Ilya here since\x01",
            "she's hospitalised, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I saw her doing her\x01",
            "best in rehab, the super\x01",
            "fan in me was blown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I hope she does her\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x3, 1)
    Jump("loc_92D1")

    label("loc_92AA")


    ChrTalk(
        0xFE,
        (
            "Ilya... I hope she does\x01",
            "her best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D1")

    TalkEnd(0xFE)
    Return()

    # Function_46_90D9 end

    def Function_47_92D5(): pass

    label("Function_47_92D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_934C")

    ChrTalk(
        0xFE,
        (
            "Aah, so booored. It's a\x01",
            "hospital so I can't even\x01",
            "read Hot Shot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Won't anyone come see\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9403")

    label("loc_934C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9403")

    ChrTalk(
        0xFE,
        (
            "I suffered a compound\x01",
            "fracture and got taken\x01",
            "to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's improved quite a lot, but\x01",
            "since going back to the city seems\x01",
            "quite troublesome, I don't want to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9403")

    TalkEnd(0xFE)
    Return()

    # Function_47_92D5 end

    def Function_48_9407(): pass

    label("Function_48_9407")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9470")

    ChrTalk(
        0xFE,
        (
            "What in the world is\x01",
            "that azure tree in the\x01",
            "eastern sky!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O Goddess. Save us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_94E1")

    label("loc_9470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_94E1")

    ChrTalk(
        0xFE,
        (
            "What will become of\x01",
            "Crossbell...? Only the\x01",
            "Goddess knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray she leads us to\x01",
            "salvation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94E1")

    TalkEnd(0xFE)
    Return()

    # Function_48_9407 end

    def Function_49_94E5(): pass

    label("Function_49_94E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9596")

    ChrTalk(
        0xFE,
        (
            "I feel relieved since my\x01",
            "discharge is today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's an awful situation going on\x01",
            "outside this place, but... I want\x01",
            "to go home and reassure my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95ED")

    label("loc_9596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_95ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95B1")
    Call(0, 15)
    Jump("loc_95ED")

    label("loc_95B1")


    ChrTalk(
        0xFE,
        (
            "Phew. If the doctor says\x01",
            "so, it should be all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95ED")

    TalkEnd(0xFE)
    Return()

    # Function_49_94E5 end

    def Function_50_95F1(): pass

    label("Function_50_95F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_96A4")

    ChrTalk(
        0xFE,
        (
            "The doctors doing the\x01",
            "rounds look very busy\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it seems that outpatients\x01",
            "are coming in droves. I hope they do\x01",
            "their best somehow or other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_977D")

    label("loc_96A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_977D")

    ChrTalk(
        0xFE,
        (
            "It appears there's a lot of problems\x01",
            "even here at the hospital, but it seems\x01",
            "the doctors are doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected from St. Ursula\x01",
            "Hospital... We can even get\x01",
            "hospitalised and feel at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_977D")

    TalkEnd(0xFE)
    Return()

    # Function_50_95F1 end

    def Function_51_9781(): pass

    label("Function_51_9781")

    Sound(160, 0, 100, 0)
    Return()

    # Function_51_9781 end

    def Function_52_9788(): pass

    label("Function_52_9788")

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
        "Honestly, girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Can you stop making\x01",
            "mistakes on the purchase\x01",
            "orders already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhhm, there's something\x01",
            "off here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I compiled the\x01",
            "purchase order, Meihua\x01",
            "was strictly watching me㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even so, I messed up the\x01",
            "numbers around 20 times,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...*sigh*, I feel\x01",
            "Meihua's pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm... Has something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "Oh, it's you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I asked this girl\x01",
            "to order medical\x01",
            "supplies for us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I looked at package\x01",
            "that arrived, there was\x01",
            "this worn-out doll inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This girl has made ordering\x01",
            "mistakes on all sorts of\x01",
            "things before too, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ooh, please believe me.\x01",
            "I swear I did it right\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FLloyd, don't you\x01",
            "think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, this is proof.\x02",
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
            "Lloyd explained about\x01",
            "the misdelivered\x01",
            "packages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "A misdelivery... So\x01",
            "that's what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWe're currently in the\x01",
            "middle of redelivering\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThis is the package that\x01",
            "was addressed to the\x01",
            "hospital, right?\x02",
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
            "Hmm... Indeed, these are\x01",
            "the medical supplies I\x01",
            "asked her to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you for coming all\x01",
            "this way to deliver\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        "And... I'm sorry, Xilun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems I jumped to\x01",
            "conclusions this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu, it's ok. Please\x01",
            "don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, that's right. I\x01",
            "wonder if they put THAT\x01",
            "in there too?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Xilun reached deep\x01",
            "inside the bag and\x01",
            "groped for something.\x07\x00\x02",
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
            "Ah, here it is! The\x01",
            "Kagemaru strap!㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since I was making a\x01",
            "purchase, I also ordered\x01",
            "this. Uhuhu, how cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Xilun. As I thought,\x01",
            "I'll have to lecture you\x01",
            "later.\x02",
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
            "#00006FU-Umm...\x02\x03",
            "#00000FExcuse me, but could we\x01",
            "have the package that\x01",
            "was misdelivered?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Oh, that's right. One\x01",
            "moment please.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Here, this is it. You\x01",
            "can have it.\x02",
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
            "#00003FLet's see, according to\x01",
            "the sales slip we got\x01",
            "from Aaron...\x02\x03",
            "#00000FThe delivery address is\x01",
            "a house on Residential\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A21D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A21D)
    Sleep(50)

    def lambda_A22D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A22D)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FOnce we deliver this,\x01",
            "the request will be\x01",
            "officially complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FResidential Street... Chairman\x01",
            "MacDowell's residence is there\x01",
            "too, right?\x02\x03",
            "#10300FElie, do you know this\x01",
            "address?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A306():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A306)
    Sleep(50)

    def lambda_A316():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A316)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00103FHmm, let's see...\x02",
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
            "#00105FOh, but isn't this\x01",
            "address...\x02\x03",
            "The vacant house near\x01",
            "Congressman Campbell's?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A54F")
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
            "The Residential Street\x01",
            "Empty House (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",                                        # 0
            "[Entered for Thief B Quest]\x01",                        # 1
            "[Investigated in Zero for Vacant Units Quest]\x01",      # 2
            "[Not Investigated]\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A535")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x1, 0x2)
    Jump("loc_A54F")

    label("loc_A535")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A54F")
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x3, 0x2, 0x2)

    label("loc_A54F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_A5D4")

    ChrTalk(
        0x101,
        (
            "#00005FWait, the one said to be\x01",
            "haunted for at least ten\x01",
            "years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FY-Yes... I'm sure that's\x01",
            "the one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6B7")

    label("loc_A5D4")


    ChrTalk(
        0x101,
        (
            "#00005FWasn't that the name of\x01",
            "a Republican Faction\x01",
            "congressman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes... He has a mansion\x01",
            "on the north side of\x01",
            "Residential Street.\x02\x03",
            "#00101FThe house next to his\x01",
            "should have been vacant\x01",
            "for at least ten years...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6B7")


    ChrTalk(
        0x104,
        (
            "#00305F...What's goin' on then?\x02\x03",
            "#00300FCould someone have moved\x01",
            "in recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FHmm. I'm not quite sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Anyway, let's try to\x01",
            "deliver the package.\x02",
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

    # Function_52_9788 end

    def Function_53_A7C1(): pass

    label("Function_53_A7C1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is no. 301,\x01",
            "right? Let's go see how\x01",
            "she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 8600, 0, 3680, 180)
    EventEnd(0x4)
    Return()

    # Function_53_A7C1 end

    def Function_54_A821(): pass

    label("Function_54_A821")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is no. 301,\x01",
            "right? Let's go see how\x01",
            "she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26800, 0, -25170, 0)
    EventEnd(0x4)
    Return()

    # Function_54_A821 end

    SaveToFile()

Try(main)
