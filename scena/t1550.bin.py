from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1550.bin",                # FileName
        "t1550",                    # MapName
        "t1550",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1550",                  # 0
        "Franc",                 # 1
        "Donovan",           # 2
        "Raymond investigator",       # 3
        "Ilia",                 # 4
        "Shuri",                 # 5
        "Suzuku",                 # 6
        "Mikhail",               # 7
        "Arios",               # 8
        "Dyson official",         # 9
        "Cecil",                 # 10
        "Nurse Shillon",           # 11
        "Nurse machine",         # 12
        "Doctor Doctor",       # 13
        "Prince Albert",         # 14
        "Mrs. Fara",             # 15
        "Professor Seyland",         # 16
        "A round chair",                 # 17
        "Sergei",               # 18
        "SE control",                 # 19
    ))

    AddCharChip((
        "apl/ch51518.itc",                   # 00
        "apl/ch51519.itc",                   # 01
        "chr/ch30202.itc",                   # 02
        "apl/ch51520.itc",                   # 03
        "chr/ch10002.itc",                   # 04
        "apl/ch50105.itc",                   # 05
        "chr/ch34000.itc",                   # 06
        "apl/ch50145.itc",                   # 07
        "chr/ch02400.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch05300.itc",                   # 0A
        "chr/ch29900.itc",                   # 0B
        "chr/ch29800.itc",                   # 0C
        "chr/ch29300.itc",                   # 0D
        "chr/ch11800.itc",                   # 0E
        "chr/ch21900.itc",                   # 0F
        "chr/ch21902.itc",                   # 10
        "chr/ch44800.itc",                   # 11
        "apl/ch51703.itc",                   # 12
        "chr/ch30300.itc",                   # 13
        "chr/ch08500.itc",                   # 14
        "chr/ch06900.itc",                   # 15
        "apl/ch51702.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(6199,    0,       4294919796, 270,  389,  0x0, 0,   0,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(4294912296, 0,       4294919796, 270,  389,  0x0, 0,   1,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4294911596, 100,     4294917497, 0,    389,  0x0, 0,   2,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(4294869296, 0,       4294962097, 180,  389,  0x0, 0,   3,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(4294867796, 100,     4294961597, 90,   389,  0x0, 0,   4,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294869557, 699,     56169,   180,  325,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6050,    699,     4294919747, 270,  389,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(4294868076, 0,       56180,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294958986, 0,       25229,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294868076, 0,       56180,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294958696, 0,       10350,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(4294959697, 0,       9350,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(4809,    0,       4294918396, 45,   389,  0x0, 0,   13,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(4294868076, 0,       55110,   45,   389,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294911596, 100,     4294917497, 0,    389,  0x0, 0,   15,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(4294868076, 0,       56180,   90,   389,  0x0, 0,   17,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 87,  -15.210000038146973,   8.899999618530273,     -1.0,                  64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   7.605000019073486,     -1.1124999523162842,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 88,  -9.210000038146973,    15.65999984741211,     -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.1512500047683716,    -7.829999923706055,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 91,  -21.149999618530273,   29.889999389648438,    -1.0,                  64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   10.574999809265137,    -3.7362499237060547,   0.20000000298023224,   1.0])

    DeclActor(4294868986, 0,       54690,   1200,    4294869556, 1500,    56170,   0x007E, 0,  12, 0x0000)

    ChipFrameInfo(1504, 0)                                       # 0

    ScpFunction((
        "Function_0_5E0",          # 00, 0
        "Function_1_698",          # 01, 1
        "Function_2_D6C",          # 02, 2
        "Function_3_12A4",         # 03, 3
        "Function_4_12B3",         # 04, 4
        "Function_5_12FA",         # 05, 5
        "Function_6_1301",         # 06, 6
        "Function_7_130E",         # 07, 7
        "Function_8_1321",         # 08, 8
        "Function_9_1328",         # 09, 9
        "Function_10_1335",        # 0A, 10
        "Function_11_133C",        # 0B, 11
        "Function_12_1367",        # 0C, 12
        "Function_13_1B3E",        # 0D, 13
        "Function_14_1CAE",        # 0E, 14
        "Function_15_1D66",        # 0F, 15
        "Function_16_1E8A",        # 10, 16
        "Function_17_1F40",        # 11, 17
        "Function_18_204C",        # 12, 18
        "Function_19_298B",        # 13, 19
        "Function_20_2D1B",        # 14, 20
        "Function_21_3345",        # 15, 21
        "Function_22_3A25",        # 16, 22
        "Function_23_3BB0",        # 17, 23
        "Function_24_4CE5",        # 18, 24
        "Function_25_4EAE",        # 19, 25
        "Function_26_518B",        # 1A, 26
        "Function_27_5F1B",        # 1B, 27
        "Function_28_6393",        # 1C, 28
        "Function_29_69FC",        # 1D, 29
        "Function_30_6D0C",        # 1E, 30
        "Function_31_6E09",        # 1F, 31
        "Function_32_6EEB",        # 20, 32
        "Function_33_7318",        # 21, 33
        "Function_34_73ED",        # 22, 34
        "Function_35_7555",        # 23, 35
        "Function_36_7AA3",        # 24, 36
        "Function_37_8207",        # 25, 37
        "Function_38_820E",        # 26, 38
        "Function_39_8434",        # 27, 39
        "Function_40_849C",        # 28, 40
        "Function_41_9811",        # 29, 41
        "Function_42_9846",        # 2A, 42
        "Function_43_986C",        # 2B, 43
        "Function_44_9898",        # 2C, 44
        "Function_45_98BE",        # 2D, 45
        "Function_46_98F3",        # 2E, 46
        "Function_47_9919",        # 2F, 47
        "Function_48_A256",        # 30, 48
        "Function_49_A260",        # 31, 49
        "Function_50_BBF3",        # 32, 50
        "Function_51_BC12",        # 33, 51
        "Function_52_BC22",        # 34, 52
        "Function_53_BC37",        # 35, 53
        "Function_54_BC53",        # 36, 54
        "Function_55_BC6F",        # 37, 55
        "Function_56_BC8B",        # 38, 56
        "Function_57_BCA7",        # 39, 57
        "Function_58_BCC3",        # 3A, 58
        "Function_59_BCDF",        # 3B, 59
        "Function_60_BD2B",        # 3C, 60
        "Function_61_CBCF",        # 3D, 61
        "Function_62_CFF3",        # 3E, 62
        "Function_63_DE5D",        # 3F, 63
        "Function_64_E581",        # 40, 64
        "Function_65_E5AA",        # 41, 65
        "Function_66_E5D3",        # 42, 66
        "Function_67_E5E6",        # 43, 67
        "Function_68_F2F0",        # 44, 68
        "Function_69_F349",        # 45, 69
        "Function_70_F3A2",        # 46, 70
        "Function_71_F3FB",        # 47, 71
        "Function_72_F454",        # 48, 72
        "Function_73_F4AD",        # 49, 73
        "Function_74_F506",        # 4A, 74
        "Function_75_F519",        # 4B, 75
        "Function_76_FD4C",        # 4C, 76
        "Function_77_FF93",        # 4D, 77
        "Function_78_10C49",       # 4E, 78
        "Function_79_10C86",       # 4F, 79
        "Function_80_10D58",       # 50, 80
        "Function_81_10D88",       # 51, 81
        "Function_82_10DB8",       # 52, 82
        "Function_83_10DE8",       # 53, 83
        "Function_84_10E04",       # 54, 84
        "Function_85_10E20",       # 55, 85
        "Function_86_10E30",       # 56, 86
        "Function_87_11462",       # 57, 87
        "Function_88_1147B",       # 58, 88
        "Function_89_114A6",       # 59, 89
        "Function_90_114D1",       # 5A, 90
        "Function_91_114FC",       # 5B, 91
        "Function_92_11515",       # 5C, 92
        "Function_93_11563",       # 5D, 93
        "Function_94_115F6",       # 5E, 94
    ))


    def Function_0_5E0(): pass

    label("Function_0_5E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_620"),
        (1, "loc_62C"),
        (2, "loc_638"),
        (3, "loc_644"),
        (4, "loc_650"),
        (5, "loc_65C"),
        (6, "loc_668"),
        (SWITCH_DEFAULT, "loc_674"),
    )


    label("loc_620")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_62C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_638")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_644")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_650")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_65C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_674")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_697")

    Return()

    # Function_0_5E0 end

    def Function_1_698(): pass

    label("Function_1_698")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B0")
    ClearScenarioFlags(0x25, 1)
    Call(0, 37)

    label("loc_6B0")

    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_731")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55260, 0, -49740, 270)
    SetChrChipByIndex(0x9, 0x13)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -56460, 0, -49740, 90)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jump("loc_C40")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_C40")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_844")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -99490, 0, -5640, 90)
    Jump("loc_C40")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_902")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x15)
    SetChrPos(0x8, -55180, 0, -49470, 0)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -56380, 0, -49470, 90)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FD")
    SetChrFlags(0x17, 0x10)

    label("loc_8FD")

    Jump("loc_C40")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9B2")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x14)
    SetChrPos(0x8, 7850, 0, -50750, 90)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AD")
    SetChrFlags(0x17, 0x10)

    label("loc_9AD")

    Jump("loc_C40")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A6C")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrPos(0x8, 6100, 400, -47500, 270)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x9, -55500, 400, -47700, 270)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x1000)
    SetChrPos(0xB, -97700, 420, -5500, 180)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x80)
    Jump("loc_C40")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D")
    SetChrFlags(0x13, 0x10)

    label("loc_A9D")

    Jump("loc_C40")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ABA")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_C40")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AE3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 4810, 0, -48900, 45)
    Jump("loc_C40")

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B49")
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, -99220, 0, 56180, 90)
    SetChrChipByIndex(0xE, 0x6)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -100590, 0, 57320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    SetChrFlags(0x11, 0x10)

    label("loc_B3F")

    ClearChrFlags(0x10, 0x80)
    Jump("loc_C40")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BDC")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4810, 0, -48900, 45)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD7")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -100500, 0, 54700, 45)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -100500, 0, 55990, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC8")
    SetChrFlags(0xF, 0x10)

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD7")
    SetChrFlags(0x15, 0x10)

    label("loc_BD7")

    Jump("loc_C40")

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C40")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C00")
    SetChrFlags(0x11, 0x80)

    label("loc_C00")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -55020, 0, -49520, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40")
    SetChrFlags(0x14, 0x10)

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C4F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 75)

    label("loc_C4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6E")
    Event(0, 40)
    Jump("loc_D23")

    label("loc_C6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8D")
    Event(0, 47)
    Jump("loc_D23")

    label("loc_C8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAC")
    Event(0, 49)
    Jump("loc_D23")

    label("loc_CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCB")
    Event(0, 60)
    Jump("loc_D23")

    label("loc_CCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    Event(0, 61)
    Jump("loc_D23")

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
    Event(0, 62)
    Jump("loc_D23")

    label("loc_D09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23")
    Event(0, 63)

    label("loc_D23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4C")
    Event(0, 76)
    Jump("loc_D6B")

    label("loc_D4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6B")
    Event(0, 67)

    label("loc_D6B")

    Return()

    # Function_1_698 end

    def Function_2_D6C(): pass

    label("Function_2_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_D7E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5")
    Sound(1016, 1, 60, 0)
    Jump("loc_DA8")

    label("loc_DA5")

    OP_24(0x3F8)

    label("loc_DA8")

    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mec_T15_02n", 0x0, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E83")
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ED4")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F25")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F83")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")
    Call(0, 9)

    label("loc_F78")

    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1005")
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    Call(0, 8)
    Call(0, 5)
    Call(0, 6)
    Call(0, 7)
    SetMapObjFrame(0xFF, "mec_T15_02e", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_1091")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_1091")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1021")
    Jump("loc_1091")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_102F")
    Jump("loc_1091")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_103D")
    Jump("loc_1091")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1063")
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    Jump("loc_1091")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1091")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)

    label("loc_1091")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AC")
    OP_66(0x0, 0x1)
    Jump("loc_10C5")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C5")
    OP_66(0x0, 0x1)

    label("loc_10C5")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EC")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1109")
    ModifyEventFlags(1, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1126")
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_114D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_114D")
    OP_1B(0x8, 0x0, 0x26)
    OP_1B(0x9, 0x0, 0x27)

    label("loc_114D")

    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116F")
    Jump("loc_11CE")

    label("loc_116F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A1")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_11CE")

    label("loc_11A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CE")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -99500, 0, -5700, 0)

    label("loc_11CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11E2")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_1267")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_120B")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_1267")

    label("loc_120B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1234")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_1267")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1267")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_1267")
    SetMapObjFlags(0x6, 0x4)

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_12A3")

    Return()

    # Function_2_D6C end

    def Function_3_12A4(): pass

    label("Function_3_12A4")

    SetMapObjFrame(0xFF, "obj_07", 0x1, 0x1)
    Return()

    # Function_3_12A4 end

    def Function_4_12B3(): pass

    label("Function_4_12B3")

    SetMapObjFrame(0xFF, "obj_08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_10", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_09", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_11", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_12", 0x1, 0x1)
    Return()

    # Function_4_12B3 end

    def Function_5_12FA(): pass

    label("Function_5_12FA")

    ClearMapObjFlags(0x7, 0x4)
    Return()

    # Function_5_12FA end

    def Function_6_1301(): pass

    label("Function_6_1301")

    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Return()

    # Function_6_1301 end

    def Function_7_130E(): pass

    label("Function_7_130E")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Return()

    # Function_7_130E end

    def Function_8_1321(): pass

    label("Function_8_1321")

    ClearMapObjFlags(0x11, 0x4)
    Return()

    # Function_8_1321 end

    def Function_9_1328(): pass

    label("Function_9_1328")

    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    Return()

    # Function_9_1328 end

    def Function_10_1335(): pass

    label("Function_10_1335")

    ClearMapObjFlags(0xD, 0x4)
    Return()

    # Function_10_1335 end

    def Function_11_133C(): pass

    label("Function_11_133C")

    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    Return()

    # Function_11_133C end

    def Function_12_1367(): pass

    label("Function_12_1367")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1378")
    Jump("loc_1B3A")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1389")
    Call(0, 27)
    Jump("loc_1B3A")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")
    Call(0, 27)
    Jump("loc_1B3A")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_155E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(
        0xD,
        (
            "#11205FAh, that's right …\x02\x03",
            "#11203FYesterday, Kaaya\x01",
            "He came to visit me ….\x02\x03",
            "#11210FListening to my surgery story,\x01",
            "It seems that it was very depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Oh, certainly today\x01",
            "It seems I had no energy from the morning.\x02\x03",
            "#00000FBut, that's fine.\x01",
            "If Shizuoka is positive,\x01",
            "Ka'aa will get well soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11200FI hope it will be … Yes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1559")

    label("loc_1512")


    ChrTalk(
        0xD,
        (
            "#11200FKa'a-chan ……\x01",
            "As soon as you get well\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1559")

    Jump("loc_1B3A")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_156F")
    Call(0, 13)
    Jump("loc_1B3A")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1594")
    Call(0, 18)
    Jump("loc_1A7C")

    label("loc_1594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B0")
    Call(0, 17)
    Jump("loc_1A7C")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(
        0xD,
        (
            "#01505FOh, that's right ……\x02\x03",
            "#01500FKa'a-chan, what is it today?\x01",
            "Was not it strange?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1701")
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
            "#1K◆ What is Kaoru who dumps at the support section? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【speaking】\x01",        # 1
            "[I'm not talking]\x01",      # 2
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
        (0, "loc_16EC"),
        (1, "loc_16F1"),
        (2, "loc_16F9"),
        (SWITCH_DEFAULT, "loc_1701"),
    )


    label("loc_16EC")

    Jump("loc_1701")

    label("loc_16F1")

    SetScenarioFlags(0x151, 6)
    Jump("loc_1701")

    label("loc_16F9")

    ClearScenarioFlags(0x151, 6)
    Jump("loc_1701")

    label("loc_1701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 6)), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(
        0x109,
        "#10105FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FBy the way, what was that about a while ago?\x01",
            "I feel like I was drowning.\x02\x03",
            "#00001FDid you do something with the unveiling ceremony?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F2")

    label("loc_1797")


    ChrTalk(
        0x109,
        (
            "#10105FHuh……?\x01",
            "Especially I did not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FDid you do something with the unveiling ceremony?\x02",
    )

    CloseMessageWindow()

    label("loc_17F2")


    ChrTalk(
        0xD,
        (
            "#01500FNo, such a big deal\x01",
            "I do not think so ….\x02\x03",
            "#01508FKa'a-chan who saw the unveiling ceremony,\x01",
            "I felt something stunned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHmm, to the size of the Orkis Tower\x01",
            "Were not you just surprised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FOh … that kind of thing\x01",
            "Was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, I do not really know.\x01",
            "I will keep it in mind.\x02\x03",
            "#00000FThank you, Shizuku-chan.\x01",
            "You are worried about Kea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01500FNo, such a thing ….\x01",
            "I'm sorry, I am\x01",
            "Saying strange things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 2)
    Jump("loc_1A7C")

    label("loc_19D1")


    ChrTalk(
        0xD,
        (
            "#01502FToday 's unveiling ceremony,\x01",
            "Thanks to Kea-chan\x01",
            "it was very fun.\x02\x03",
            "When I can see my eyes someday,\x01",
            "With Ka'a-chan\x01",
            "I'd like to see the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    Jump("loc_1B2C")

    label("loc_1A81")


    ChrTalk(
        0xD,
        (
            "#01502FToday 's unveiling ceremony,\x01",
            "Thanks to Kea-chan\x01",
            "it was very fun.\x02\x03",
            "When I can see my eyes someday,\x01",
            "With Ka'a-chan\x01",
            "I'd like to see the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2C")

    Jump("loc_1B3A")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B3A")

    label("loc_1B3A")

    TalkEnd(0xD)
    Return()

    # Function_12_1367 end

    def Function_13_1B3E(): pass

    label("Function_13_1B3E")

    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1B")

    ChrTalk(
        0xD,
        (
            "#01502FMikhail, soon\x01",
            "You have to leave the hospital.\x02\x03",
            "Huhu, congratulations.\x01",
            "Keep it up all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah …… Shizuku-chan,\x01",
            "Thank you for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I will write a letter at all.\x01",
            "Suzuku is doing fine, too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1CA9")

    label("loc_1C1B")


    ChrTalk(
        0xD,
        (
            "#01502FMikhail can be discharged from the hospital,\x01",
            "I am also really happy.\x02\x03",
            "Someday, with my father\x01",
            "I'm going to visit Leman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yup……!\x01",
            "I'll be waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA9")

    OP_4C(0xE, 0xFF)
    Return()

    # Function_13_1B3E end

    def Function_14_1CAE(): pass

    label("Function_14_1CAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CBF")
    Jump("loc_1D62")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CD0")
    Call(0, 13)
    Jump("loc_1D62")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CE1")
    Call(0, 29)
    Jump("loc_1D62")

    label("loc_1CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFC")
    Call(0, 34)
    Jump("loc_1D62")

    label("loc_1CFC")


    ChrTalk(
        0xE,
        (
            "Hospital discharge …\x01",
            "It is true that such a day will come true …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's fast, Leman's\x01",
            "I have to contact my mothers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CAE end

    def Function_15_1D66(): pass

    label("Function_15_1D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DFA")

    ChrTalk(
        0xF,
        (
            "#01400FI ask about your investigation of \"Phantom beast\".\x02\x03",
            "I will also be back tomorrow\x01",
            "I plan to join, until then\x01",
            "Please help Scott.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E86")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E16")
    Call(0, 18)
    Jump("loc_1E86")

    label("loc_1E16")


    ChrTalk(
        0xF,
        (
            "#01400FI wish to see your Excellency in Shizuku\x01",
            "You say.\x02\x03",
            "#01403F… … It is a pleasant story.\x01",
            "I have to thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E86")

    TalkEnd(0xFE)
    Return()

    # Function_15_1D66 end

    def Function_16_1E8A(): pass

    label("Function_16_1E8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA9")
    Call(0, 18)
    Jump("loc_1F3C")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBB")
    Call(0, 17)
    Jump("loc_1F3C")

    label("loc_1EBB")


    ChrTalk(
        0x15,
        (
            "Oh, I see you later\x01",
            "Seireland's appearance also\x01",
            "I definitely have to go look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I have not seen you for a long time,\x01",
            "I hope she is also an expert.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3C")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E8A end

    def Function_17_1F40(): pass

    label("Function_17_1F40")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "By the way, Shizuku\x01",
            "You have been suffering from eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "… … There will be anxiety,\x01",
            "The doctor's arms of this hospital\x01",
            "It should deserve credit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Although it may take time,\x01",
            "Believe in complete recovery and perseverance\x01",
            "Fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FAh……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x15, 0xFF)
    Return()

    # Function_17_1F40 end

    def Function_18_204C(): pass

    label("Function_18_204C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xF, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_68(-99630, 1000, 53940, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19710, 0)
    SetChrPos(0x101, -100420, 0, 52850, 0)
    SetChrPos(0x102, -98870, 0, 52710, 315)
    SetChrPos(0x104, -98240, 0, 51510, 315)
    SetChrPos(0x109, -99630, 50, 50760, 0)
    SetChrPos(0x105, -100770, 50, 51180, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#01505FAh … everyone in the support section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh, you guys ……\x02",
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FLes, in the princess of Remiferia\x01",
            "Dear Grand Prince Albert … …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAlso, to Mr. Arios ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403FHmm, that's a strange idea.\x02\x03",
            "#01400FYour experts, they talked about before\x01",
            "They are those of the \"Special Affairs Support Division\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        "Oh, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "…… Hello, you guys at the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "My name is Albert von Bartholomeus.\x01",
            "He is the head of State of Remifria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "From now on for the crossbell,\x01",
            "Please do your best hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Huh, you guys,\x01",
            "Please listen to me from Arios.\x01",
            "I definitely wanted to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Also, Ellie is the first time in a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, it's been a long time.\x01",
            "His Excellency seems to be well … …\x02\x03",
            "#00103FBut just to the hospital\x01",
            "What was it that you were seeing?\x01",
            "I did not know.\x02\x03",
            "#00105FToday we came to visit\x01",
            "Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, the Prime Minister of Remifria is at this hospital\x01",
            "It's one of the sponsors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "To Aios' daughter who was listening to the story,\x01",
            "I wanted to say hello to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01502FOh, thank you, Grand Prince.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01400FRegarding that, personally\x01",
            "Let me put a little more escort\x01",
            "It is a place I wanted to receive.\x02\x03",
            "#01403FOnly me and a driver of a limousine,\x01",
            "I wonder what it is like ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "Huff, you about Arios\x01",
            "Because it is trusted\x01",
            "Please think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Besides, for my visit\x01",
            "Take the escort and get the job of the hospital\x01",
            "I can not prevent it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Grand Duke Albert … ….\x01",
            "Not only Mr. Arios,\x01",
            "I also met Ellie. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yeah, Eli and Arios … …\x01",
            "Besides Professor Seyland\x01",
            "I'd like to know acquainted from before. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Huh, more than I thought\x01",
            "It looks like a friendly person. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "Anyway, you guys\x01",
            "I am also cheering for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Keep doing your best in the future.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FDear Grand Prince, please take care of today.\x01",
            "Please return.\x02\x03",
            "Tomorrow's trade meeting,\x01",
            "We will support you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Haha, I will do my best at all times.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xD, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0xF, 0x5A, 0x0)
    OP_93(0x15, 0x2D, 0x0)
    SetScenarioFlags(0x1C6, 5)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -99930, 0, 52260, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_18_204C end

    def Function_19_298B(): pass

    label("Function_19_298B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_2A25")

    ChrTalk(
        0x8,
        (
            "#01900FThere is a dangerous place for the police\x01",
            "Help me, really\x01",
            "I can not thank you enough ~.\x02\x03",
            "#01909FAlso, to see a broken visit\x01",
            "I will tell you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B54")

    ChrTalk(
        0x8,
        (
            "#06400FWell, the notebook and enigma,\x01",
            "Toothbrush set ……\x02\x03",
            "#06405FOh, other patients\x01",
            "Also for the nurses\x01",
            "I have to say hello to you ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(The dress of frank is\x01",
            "It looks like it will take a little more … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F(Well, before this too\x01",
            "You may as well finish your sympathy\x01",
            "Looks good. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BE2")

    label("loc_2B54")


    ChrTalk(
        0x8,
        (
            "#06405FOh, properly in uniform\x01",
            "I have to change my clothes ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "#06401F…… Please do not peek ~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI will not peek.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_2BE2")

    Jump("loc_2D17")

    label("loc_2BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_END)), "loc_2D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFA")

    ChrTalk(
        0x8,
        "#11703FSue … …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC0")

    ChrTalk(
        0x105,
        "#10300FHe seems to be sleeping well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01302FAll right, Mr. Noel.\x01",
            "It will be fine as soon as this condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2CC0")


    ChrTalk(
        0x109,
        (
            "#10103F(Fran …\x01",
            "Get well soon. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF2")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2D17")

    label("loc_2CFA")


    ChrTalk(
        0x8,
        "#11703FSue … …\x02",
    )

    CloseMessageWindow()

    label("loc_2D17")

    TalkEnd(0xFE)
    Return()

    # Function_19_298B end

    def Function_20_2D1B(): pass

    label("Function_20_2D1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D39")
    Call(0, 21)
    Jump("loc_2DCC")

    label("loc_2D39")


    ChrTalk(
        0x9,
        (
            "I will join the police from now on … …\x01",
            "Well, to the extent not impossible\x01",
            "I am going to help somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You seem to be pretty tough,\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCC")

    Jump("loc_3341")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBE")

    ChrTalk(
        0x9,
        (
            "Is it an invalid declaration of an independent country …?\x01",
            "You guys are not\x01",
            "I do not think I will do so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sergei in the city, too,\x01",
            "Ride this machine\x01",
            "It should be moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If this is the case\x01",
            "I can not join for a while.\x01",
            "… … I will leave it to you later, you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5A")

    label("loc_2EBE")


    ChrTalk(
        0x9,
        (
            "Sergei in the city, too,\x01",
            "When I am multiplying this machine and moving it out\x01",
            "You can watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If this is the case\x01",
            "I can not join for a while.\x01",
            "… … I will leave it to you later, you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5A")

    Jump("loc_3341")

    label("loc_2F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3010")

    ChrTalk(
        0x9,
        (
            "In any case, I immediately\x01",
            "I will not be able to join the police\x01",
            "Let's say you are resting your body for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until then to Raymond and Sergei\x01",
            "I must do my best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_3095")

    ChrTalk(
        0x9,
        (
            "Haha, I was safe.\x01",
            "I do not care about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You also\x01",
            "Because I am sick,\x01",
            "Be careful, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B0")
    Call(0, 21)
    Jump("loc_3112")

    label("loc_30B0")


    ChrTalk(
        0x9,
        (
            "Well, anyway … …\x01",
            "You should be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sergei and soon are nearby\x01",
            "I hope to join you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Jump("loc_3341")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(
        0x9,
        "#90W………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F… … When the police woke up,\x01",
            "I hope you have caught the franc\x01",
            "I must reward you again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E3")

    ChrTalk(
        0x136,
        (
            "#01303FA considerable respiratory system\x01",
            "Because I am receiving damage,\x01",
            "Recovery may be slow …\x02\x03",
            "#01300FBut the mountain is exceeding\x01",
            "Surely within close proximity\x01",
            "You should be awake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI hope it will be ……\x02\x03",
            "#00100F…… Afterwards to Raymond\x01",
            "It seems to be okay to leave it to me,\x01",
            "Let's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, let's\x02",
    )

    CloseMessageWindow()
    Jump("loc_3319")

    label("loc_32E3")


    ChrTalk(
        0x101,
        (
            "#00003FThat's right.\x01",
            "I hope it gets better soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3319")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3341")

    label("loc_3321")


    ChrTalk(
        0x9,
        "#90W………………………….\x02",
    )

    CloseMessageWindow()

    label("loc_3341")

    TalkEnd(0xFE)
    Return()

    # Function_20_2D1B end

    def Function_21_3345(): pass

    label("Function_21_3345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3674")
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)

    def lambda_335B():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_335B)
    Sleep(0)

    def lambda_336B():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_336B)
    Sleep(0)

    def lambda_337B():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_337B)
    Sleep(0)

    def lambda_338B():
        TurnDirection(0x3, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_338B)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x16, 0x0, 0)

    ChrTalk(
        0x9,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Hello, Hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FDonovan police …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIs it okay to move already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, I left the procedure of discharge\x01",
            "I have done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Crossbell City's release strategy\x01",
            "It seems that it went well,\x01",
            "I thought I'd join the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Actually, what is the planned discharge date?\x01",
            "It was ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I do not want to make impossible,\x01",
            "Because I say absolutely\x01",
            "I decided to break up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, who is Raymond\x01",
            "I'm going to be pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf police are confronted,\x01",
            "The investigation division also has more power\x01",
            "You seem to be able to demonstrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, to the extent not impossible\x01",
            "I am going to help somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You seem to be pretty tough,\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 7)
    TurnDirection(0x9, 0x16, 0)
    TurnDirection(0x16, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_3A24")

    label("loc_3674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A24")

    def lambda_3682():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3682)
    Sleep(0)

    def lambda_3692():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3692)
    Sleep(0)

    def lambda_36A2():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_36A2)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_374A")
    Jump("loc_3794")

    label("loc_374A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_376A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3794")

    label("loc_376A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_378A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3794")

    label("loc_378A")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3794")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x10)
    TurnDirection(0x16, 0x0, 0)
    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_384A")
    Jump("loc_3894")

    label("loc_384A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_386A")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3894")

    label("loc_386A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_388A")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3894")

    label("loc_388A")

    OP_52(0x16, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3894")

    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x10)

    ChrTalk(
        0x9,
        (
            "Whew, embarrassing place\x01",
            "I could not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since Farah married,\x01",
            "Do not leave the pace grabbed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FIs not it a nice wife?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHuh, I'm pretty cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Well … ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hehe he is pretty.\x01",
            "You heard it, you spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "(… … even in front of Raymond this time\x01",
            "I am troubled because of this condition, so … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x10)

    label("loc_3A24")

    Return()

    # Function_21_3345 end

    def Function_22_3A25(): pass

    label("Function_22_3A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B12")

    ChrTalk(
        0xA,
        (
            "With a great deal of security to the Donovan\x01",
            "I had my life helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am not pretentious but … ….\x01",
            "From now on, more firmly\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One day as a member of the police station\x01",
            "not embarrassing,\x01",
            "You must be a good investigator.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BAC")

    label("loc_3B12")


    ChrTalk(
        0xA,
        (
            "I am not pretentious but … ….\x01",
            "From now on, more firmly\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One day as a member of the police station\x01",
            "not embarrassing,\x01",
            "You must be a good investigator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BAC")

    TalkEnd(0xFE)
    Return()

    # Function_22_3A25 end

    def Function_23_3BB0(): pass

    label("Function_23_3BB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_426D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")

    ChrTalk(
        0xB,
        (
            "#11601FMy brother you guys ……\x01",
            "Apparently tough thing\x01",
            "You seem to be getting.\x02\x03",
            "#11606FSomewhat incomprehensible\x01",
            "Things like \"Taiki\"\x01",
            "Have you appeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah …. To be honest,\x01",
            "It is a situation I do not know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThe hospital, never being safe\x01",
            "It may not be possible to say.\x02\x03",
            "#00101FPlease pay attention to Iria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609FAhaha, thanks.\x01",
            "I too much\x01",
            "I do not know it ….\x02\x03",
            "#11600FIf you were younger brother,\x01",
            "You can surely do it if you do not give up.\x01",
            "You should be able to grasp important things.\x02\x03",
            "#11604FI, too, until I stand on stage again,\x01",
            "I will never give up … ….\x02\x03",
            "#11609FSo, you also\x01",
            "Please do your best until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWith Ilia's support\x01",
            "One hundred power!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_3E75")
    Call(0, 77)
    Return()

    label("loc_3E75")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3F45")

    label("loc_3E7D")


    ChrTalk(
        0xB,
        (
            "#11604FIf you were younger brother,\x01",
            "You can surely do it if you do not give up.\x01",
            "You should surely grasp the important things.\x02\x03",
            "#11609FI, too, until I stand on stage again,\x01",
            "I will never give up … ….\x01",
            "So please do your best till the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F45")

    Jump("loc_4268")

    label("loc_3F4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6C), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F65")
    Call(0, 86)
    Jump("loc_4268")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_409D")

    ChrTalk(
        0xB,
        (
            "#11600FIf you were younger brother,\x01",
            "You can surely do it if you do not give up.\x01",
            "You should surely grasp the important things.\x02\x03",
            "#11604FI, too, until I stand on stage again,\x01",
            "I will never give up … ….\x01",
            "So please do your best till the end.\x02\x03",
            "#11609FHuff, that child standing outside#6R噵 噵 噵#Also,\x01",
            "I'm honored to say hello.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4198")

    label("loc_409D")


    ChrTalk(
        0xB,
        (
            "#11600FIf you were younger brother,\x01",
            "You can surely do it if you do not give up.\x01",
            "You should surely grasp the important things.\x02\x03",
            "#11604FI, too, until I stand on stage again,\x01",
            "I will never give up … ….\x01",
            "So please do your best till the end.\x02\x03",
            "#11609FHuff, that girl#6R噵 噵 噵#See you also.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4198")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4268")

    label("loc_41A0")


    ChrTalk(
        0xB,
        (
            "#11604FIf you were younger brother,\x01",
            "You can surely do it if you do not give up.\x01",
            "You should surely grasp the important things.\x02\x03",
            "#11609FI, too, until I stand on stage again,\x01",
            "I will never give up … ….\x01",
            "So please do your best till the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4268")

    Jump("loc_4CE1")

    label("loc_426D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_45E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4537")

    ChrTalk(
        0xB,
        (
            "#11603FMy brother, a serious thing in town\x01",
            "It's a rumor that it happened ….\x02\x03",
            "#11601FThe truth of a raid incident a few months ago,\x01",
            "Did you get covered by electric shock?\x02\x03",
            "Detailed information is regulated\x01",
            "It seems that it did not flow … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FIlia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(For Iria,\x01",
            "The underlying fundamental injury\x01",
            "It's a story that causes … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11603F… Well, now that incident\x01",
            "I do not care for the truth.\x02\x03",
            "#11600FFrom such a thing,\x01",
            "When is the next rehab?\x02\x03",
            "#11609FTo return to the stage,\x01",
            "I want to move my body soon\x01",
            "I'm running out ♪\x02",
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
        0x101,
        "#00012FHaha, what is that …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FAs expected, Iria.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 2)
    Jump("loc_45DE")

    label("loc_4537")


    ChrTalk(
        0xB,
        (
            "#11602FPerforming cancer cancer rehab\x01",
            "I will never return to the stage,\x01",
            "I'm not interested in anything else.\x02\x03",
            "#11609FOh, I guess the next rehab is still.\x01",
            "I want to move my body soon ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DE")

    Jump("loc_4CE1")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C2")

    ChrTalk(
        0xB,
        (
            "#11600FAccording to Dr. Seyland\x01",
            "Whether it will become possible to walk or not\x01",
            "It seems I do not know at the moment, but …\x02\x03",
            "#11604FThere is no possibility,\x01",
            "I do not think it is a reason to give up.\x02\x03",
            "#11602FAnyway, if people are for important things\x01",
            "Because it is a living thing that you can do your best everywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480B")

    ChrTalk(
        0x103,
        (
            "#00200FWhile watching Yuria\x01",
            "It really seems like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHugh, younger brothers.\x01",
            "Please tell me when you meet Risha.\x02\x03",
            "#11600F\"Before that important thing\x01",
            "Can you go without trying hard? Do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, understood\x01",
            "If I can meet you,\x01",
            "I will surely tell you the words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48BA")

    label("loc_480B")


    ChrTalk(
        0x101,
        (
            "#00008F(From Lyrica to Mr. Iria\x01",
            "I tell you the message … …\x01",
            "I do not seem to be in a state to meet yet. )\x02\x03",
            "#00003F(At the moment,\x01",
            "It seems better to stay silent. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48BA")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4961")

    label("loc_48C2")


    ChrTalk(
        0xB,
        (
            "#11604FIf a person is for an important thing\x01",
            "It is a creature that you can work hard anywhere.\x02\x03",
            "#11600FThe possibility of becoming able to walk again\x01",
            "There is no reason,\x01",
            "I do not think it is a reason to give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4961")

    Jump("loc_4CE1")

    label("loc_4966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2B")

    ChrTalk(
        0xB,
        (
            "#11600FThe alkane shell in the city\x01",
            "I am worried about everyone.\x02\x03",
            "#11609FWell, it's about everyone\x01",
            "I should practice even in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FIs not that worried?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FIf you are an alkane shell person\x01",
            "It is likely that he will devote himself to practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FHuff, everyone\x01",
            "It is an artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHuhu, Shri and others are also growing … …\x02\x03",
            "#11609FEven for the time I returned,\x01",
            "You have to practice hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4BB5")

    label("loc_4B2B")


    ChrTalk(
        0xB,
        (
            "#11600FThe alkane shell in the city\x01",
            "I am worried about everyone.\x02\x03",
            "#11609FEven for when I returned.\x01",
            "You have to practice hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB5")

    Jump("loc_4CE1")

    label("loc_4BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_4CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBA")

    ChrTalk(
        0xB,
        "#11603F#90W………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F…… But Yuria's\x01",
            "It is nice to see such a figure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FI agree……\x01",
            "I still can not get the reality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIrly will definitely come back.\x01",
            "…… I believe so now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CE1")

    label("loc_4CBA")


    ChrTalk(
        0xB,
        "#11603F#90W………………………….\x02",
    )

    CloseMessageWindow()

    label("loc_4CE1")

    TalkEnd(0xFE)
    Return()

    # Function_23_3BB0 end

    def Function_24_4CE5(): pass

    label("Function_24_4CE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE4")

    ChrTalk(
        0xC,
        (
            "#04200FYou are …\x01",
            "Lisa's older sister,\x01",
            "Please do not ask.\x02\x03",
            "#04203FIf Lisa's older sister comes back,\x01",
            "Iria will also be fine …\x01",
            "I feel like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F…… Oh, please wait.\x01",
            "Surely we found out\x01",
            "I will show you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EAA")

    label("loc_4DE4")


    ChrTalk(
        0xC,
        (
            "#04203FIf Lisa's older sister comes back,\x01",
            "Iria will also be fine …\x01",
            "I feel like that.\x02\x03",
            "#04200FUntil then, somehow alkane shell#14ROreuta#But\x01",
            "I should not support Iria.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EAA")

    TalkEnd(0xFE)
    Return()

    # Function_24_4CE5 end

    def Function_25_4EAE(): pass

    label("Function_25_4EAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EBF")
    Jump("loc_5187")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F98")

    ChrTalk(
        0x10,
        (
            "It is almost time to pay for missing supplies\x01",
            "I have to ask a question … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In response to the invalid declaration of an independent country,\x01",
            "Defense forces people to unit\x01",
            "Please go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmm, I was in trouble.\x01",
            "How can I negotiate from now …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5004")

    label("loc_4F98")


    ChrTalk(
        0x10,
        (
            "Hmm, I was in trouble.\x01",
            "The Defense Forces have returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Negotiation of supply of goods from now\x01",
            "I wonder what I should do ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5004")

    Jump("loc_5187")

    label("loc_5009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5017")
    Jump("loc_5187")

    label("loc_5017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5025")
    Jump("loc_5187")

    label("loc_5025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510A")

    ChrTalk(
        0x10,
        (
            "Previously, when a hospital was attacked\x01",
            "A person hidden in this linen room\x01",
            "It seems there were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At the time of that incident,\x01",
            "I was shot in my stomach with a gun\x01",
            "Did not it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If I think about it now, I will do it as soon as possible\x01",
            "You should have hid.\x01",
            "Well, I failed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5187")

    label("loc_510A")


    ChrTalk(
        0x10,
        (
            "Previously, when a hospital was attacked\x01",
            "I got shot by a gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If I think about it now, I will do it as soon as possible\x01",
            "You should have hid.\x01",
            "Well, I failed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5187")

    TalkEnd(0xFE)
    Return()

    # Function_25_4EAE end

    def Function_26_518B(): pass

    label("Function_26_518B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_519C")
    Jump("loc_5F17")

    label("loc_519C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51AA")
    Jump("loc_5F17")

    label("loc_51AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_51B8")
    Jump("loc_5F17")

    label("loc_51B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55BC")
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x11,
        (
            "#01309FEven so …… Shizuku-chan, too\x01",
            "I hope you are doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… Yeah, really.\x02\x03",
            "#00200FKa'aa is also awesome\x01",
            "I was worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FAs a rule of thumb,\x01",
            "Now I am at the Orkis Tower\x01",
            "You should be there.\x02\x03",
            "#00003FBoth Shizuoka\x01",
            "I hope to see you somehow … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FLloyd's also ……\x01",
            "Everyone in the support department, soon all\x01",
            "You ought to be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406FWell, to be honest, the way\x01",
            "It will be pretty tough, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… To regain Ka'aa\x01",
            "Absolutely everyone's power will be needed.\x02\x03",
            "#00000FNo matter how painful it is\x01",
            "I will go ahead without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHehe, you can do with Lloyd's surely.\x02\x03",
            "#01304FI also pray to the goddess here.\x01",
            "… … Please, do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, Cecil elder sister.\x01",
            "If you say so it is hundred people.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55AD")

    ChrTalk(
        0x107,
        (
            "#01200F#13C……………………………………\x02\x03",
            "(It is still a strange blood line … …\x01",
            "── Ursula. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 500)

    ChrTalk(
        0x103,
        (
            "#00205FZeit ……\x01",
            "What's up?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 500)

    ChrTalk(
        0x107,
        (
            "#01203F#13C…… Huh, do not mind.\x01",
            "I also want to indulge in thought\x01",
            "There is that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AD")

    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1AC, 2)
    Jump("loc_5761")

    label("loc_55BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56AE")
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0x11,
        (
            "#01300FIlya, soon will\x01",
            "Shall we go for rehab?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FOK, OK.\x02\x03",
            "#11609FI will ask you to do it again today,\x01",
            "Cecil nurse's head Sun\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHehe, for Iria and everyone.\x01",
            "I will help you firmly.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_5761")

    label("loc_56AE")


    ChrTalk(
        0x11,
        (
            "#01302FIf Lloyd's\x01",
            "I'm sure to rescue everyone in the support section,\x01",
            "You should be able to meet again with Kia.\x02\x03",
            "#01304FI also pray to the goddess here.\x01",
            "… … Please, do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5761")

    Jump("loc_5F17")

    label("loc_5766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5774")
    Jump("loc_5F17")

    label("loc_5774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5782")
    Jump("loc_5F17")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5793")
    Call(0, 27)
    Jump("loc_5F17")

    label("loc_5793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_57A4")
    Call(0, 27)
    Jump("loc_5F17")

    label("loc_57A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B2")
    Jump("loc_5F17")

    label("loc_57B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ADE")
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x103, 500)

    ChrTalk(
        0x11,
        (
            "#01302FOh, it is not Tio.\x01",
            "You came back to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, I just came back yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHehe, I'm happy to see you again.\x02\x03",
            "#01304FI was very busy.\x01",
            "I'm listening … ….\x01",
            "Yes, today you look pale.\x02\x03",
            "#01300FAs before\x01",
            "In order not to collapse,\x01",
            "Take care of your health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FHehe, that clause\x01",
            "thank you for helping me.\x02\x03",
            "#00200FWell, also Cecil's\x01",
            "If you can sleep in a soft bed,\x01",
            "Although it is not bothersome to collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWell, I agree with that at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FRandy, huh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FGive me a little self-weight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FWhatching\x01",
            "Tone of the previous day\x01",
            "You seem to have come back.\x02\x03",
            "#01304FTio came back,\x01",
            "The support department finally\x01",
            "I wonder if it is a perfect start.\x02\x03",
            "#01309FBecause I'm supporting you forever,\x01",
            "Hang in there!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 5)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_5B41")

    label("loc_5ADE")


    ChrTalk(
        0x11,
        (
            "#01300FMikhail, I will leave the hospital soon.\x02\x03",
            "#01304FIt will be somewhat sad ….\x01",
            "Hehe, it was really nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B41")

    Jump("loc_5F17")

    label("loc_5B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B57")
    Call(0, 29)
    Jump("loc_5F17")

    label("loc_5B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E90")

    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "Cecil elder sister, I was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FFor sure,\x01",
            "It is a hospital room of Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300FYes, because I am out.\x01",
            "Please clean it up now.\x02\x03",
            "#01304FToday is Shizuku,\x01",
            "You are going out to the city.\x02\x03",
            "#01309FA while ago\x01",
            "\"I can meet Kea-chan\"\x01",
            "I was talking very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, really a good friend\x01",
            "It was confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, the other party is Ka'a.\x01",
            "Naturally speaking it is natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, indeed for Kia,\x01",
            "It's like talent to be friendly with people\x01",
            "You even feel like being equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FGiggle … … I heard that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300FThanks to Shizuku-chan, too\x01",
            "It got brighter than before … …\x01",
            "I am grateful to Kia - chan.\x02\x03",
            "#01302FNext time I can take a break,\x01",
            "I want to go out to play from my side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, Ka'a surely will be delighted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01309FHuhuu, thank you for that time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 1)
    Jump("loc_5F17")

    label("loc_5E90")


    ChrTalk(
        0x11,
        (
            "#01300FShizuku-chan,\x01",
            "Around this time with Ka'a-chan\x01",
            "I wonder if I am playing.\x02\x03",
            "#01309FHuhu, it's a long day away from work\x01",
            "I hope you will enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F17")

    TalkEnd(0xFE)
    Return()

    # Function_26_518B end

    def Function_27_5F1B(): pass

    label("Function_27_5F1B")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_619D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CC")

    ChrTalk(
        0xD,
        (
            "#11200FMs. Cecil …\x01",
            "Yesterday a lot of ambulance\x01",
            "It sounds like it was moving.\x02\x03",
            "#11210FThere was a big accident\x01",
            "I was caught in the ear ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01303FSomehow, on the West Crossbell Highway\x01",
            "It seems the train has derailed.\x02\x03",
            "#01302FBut, at ease.\x01",
            "Thanks to the teachers, the victims\x01",
            "It seems that it was zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FIs that so … I'm glad.\x02\x03",
            "#11208FI like it.\x01",
            "I thought it was a serious accident ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01308FShizuoka … ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6198")

    label("loc_60CC")


    ChrTalk(
        0x11,
        (
            "#01300FThanks to my best efforts\x01",
            "The patients of the train accident\x01",
            "Everyone was saved.\x02\x03",
            "So, about the accident\x01",
            "You do not have to worry.\x01",
            "Let's concentrate on rehabilitation right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11202FYes, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_6198")

    Jump("loc_638A")

    label("loc_619D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_638A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B8")
    Call(0, 28)
    Jump("loc_638A")

    label("loc_61B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F3")

    ChrTalk(
        0x11,
        (
            "#01304FHuhu, then I'll read it.\x01",
            "…… Kohon.\x02\x03",
            "#01300F\"Shizuoka, how are you?\x01",
            "I am fine. \"\x02\x03",
            "\"As I can see the eye of Shizuoka\x01",
            "Let's make it to the goddess every night\x01",
            "I pray. \"\x02\x03",
            "#01309FHehe, it seems like that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FMikhail you ……\x01",
            "…… Very, I am happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_638A")

    label("loc_62F3")


    ChrTalk(
        0x11,
        (
            "#01304FOh yes, pictures\x01",
            "I was enclosed.\x02\x03",
            "#01302FHuhu, caught between my parents,\x01",
            "It seems to be very fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11209FCouscous, nice …\x02",
    )

    CloseMessageWindow()

    label("loc_638A")

    SetChrSubChip(0xD, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_27_5F1B end

    def Function_28_6393(): pass

    label("Function_28_6393")

    EventBegin(0x0)
    Fade(500)
    OP_68(-98690, 1000, 54300, 0)
    MoveCamera(36, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18760, 0)
    SetChrPos(0x101, -99000, 50, 53000, 0)
    SetChrPos(0x102, -100940, 50, 53000, 45)
    SetChrPos(0x103, -100740, 0, 51800, 45)
    SetChrPos(0x104, -98340, 0, 52200, 0)
    SetChrPos(0x109, -100740, 0, 50600, 0)
    SetChrPos(0x105, -99240, 0, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_93(0x11, 0xB4, 0x0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FHey Cecil elder sister, Shizuku-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#11202FAh … Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FOh, it is not Lloyd's.\x02\x03",
            "#01309FHuhu, in hospitality of Shizuoka\x01",
            "I wonder if they came?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FWell, that's the place ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#N#12P#10105FUm, maybe\x01",
            "Were you disturbing?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x11, 0xB4, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FHehe, that is not true.\x02\x03",
            "#01304FActually, I returned to Leman Autonomous Region today\x01",
            "A letter came from Mikhail.\x02\x03",
            "#01300FFrom now on Shizuoka\x01",
            "I was thinking of reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FI mean Mikhail you ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FDr. Seyland has performed surgery\x01",
            "Was it a boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11204FYes, both of us\x01",
            "It was a girl who made me very friendly ……\x02\x03",
            "#11200FWhen you leave the hospital, let me write you a letter\x01",
            "I promised it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHa ha, he was nice, was not he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FUrsula hospital\x01",
            "From the patient who was discharged like this\x01",
            "Your letter may arrive, do not you?\x02\x03",
            "#01304FIt is quite busy\x01",
            "I can not make time to reply, but …\x02\x03",
            "#01300FI can know the patient 's later,\x01",
            "It is also a source of my vitality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FBecause it's about Cecil's older sister\x01",
            "Truly one by one firmly\x01",
            "I wonder if they are replying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204F… … I also write a letter to Mr. Martha\x01",
            "I wish I had put it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xE1, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FHehe, the principal is Tio and\x01",
            "I was really pleased when we met again.\x02\x03",
            "#01309FIt is not too late from now,\x01",
            "I wonder if you get started when you have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FHuhu, if the work settles down\x01",
            "I will think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x16B, 7)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -99740, 0, 53570, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xD, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_6393 end

    def Function_29_69FC(): pass

    label("Function_29_69FC")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C78")

    ChrTalk(
        0x11,
        "#01300FMikhail, how are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah, I did not have any attacks at all,\x01",
            "It seems like a lie that it was painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01304FHehe, it was good.\x02\x03",
            "#01300FThe day of discharge is getting closer ……\x01",
            "With my mothers again\x01",
            "You will be able to spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… I am lucky to be happy\x01",
            "It is half a half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When I return to Leman Autonomous Region,\x01",
            "Both Cecil's older sister and Shizuku-chan\x01",
            "It will be separated ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300F……a long time,\x01",
            "You fought with sickness together.\x01",
            "Surely I'm very lonely ….\x02\x03",
            "#01304FEven if it is far away,\x01",
            "This bond will never expire.\x01",
            "…… I think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "… Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Cecil Onee, thanks so far.\x01",
            "I will never forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 3)
    Jump("loc_6D03")

    label("loc_6C78")


    ChrTalk(
        0x11,
        (
            "#01309FHuhu, the day of discharge\x01",
            "I'm sure you will greet with a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Also for Shizuku-chan,\x01",
            "I have to say good-bye to you properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D03")

    SetChrSubChip(0xE, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_29_69FC end

    def Function_30_6D0C(): pass

    label("Function_30_6D0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D1D")
    Jump("loc_6E05")

    label("loc_6D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D38")
    Call(0, 31)
    Jump("loc_6DBF")

    label("loc_6D38")

    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        (
            "Well, it's the feeling of the sky yesterday.\x01",
            "I felt it would not rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "From weather forecast\x01",
            "If your can is hit\x01",
            "It is too wonderful.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_6DBF")

    Jump("loc_6E05")

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DD2")
    Jump("loc_6E05")

    label("loc_6DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6DE0")
    Jump("loc_6E05")

    label("loc_6DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6DEE")
    Jump("loc_6E05")

    label("loc_6DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DFC")
    Jump("loc_6E05")

    label("loc_6DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E05")

    label("loc_6E05")

    TalkEnd(0xFE)
    Return()

    # Function_30_6D0C end

    def Function_31_6E09(): pass

    label("Function_31_6E09")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Shillong you …\x01",
            "You dried the sheets on the roof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Weather forecasts say it's raining,\x01",
            "The secretary-san said that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I wonder if it will surprise me.\x01",
            "Well, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Why are you going to bet! Is it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 7)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_31_6E09 end

    def Function_32_6EEB(): pass

    label("Function_32_6EEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6EFC")
    Jump("loc_7314")

    label("loc_6EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F17")
    Call(0, 31)
    Jump("loc_6F8B")

    label("loc_6F17")


    ChrTalk(
        0x13,
        (
            "At all, wash sheets washed away\x01",
            "Everything washing it wash again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "From such a thing\x01",
            "I have to incorporate it soon! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8B")

    Jump("loc_7314")

    label("loc_6F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F9E")
    Jump("loc_7314")

    label("loc_6F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FC")

    ChrTalk(
        0x13,
        (
            "Mihail 's day of discharge,\x01",
            "Look at that gently waving a hand\x01",
            "I was deeply moved and cried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Then Shillon gave it to me\x01",
            "Keep silent and lend a handkerchief.\x01",
            "Sometimes I feel sick … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Looking closely, it's not a handkerchief\x01",
            "I lost it before\x01",
            "It was my favorite scarf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "…… There are too many Pacific shrines\x01",
            "It was a touching collapse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7192")

    label("loc_70FC")


    ChrTalk(
        0x13,
        (
            "Well, that is OK ……\x01",
            "Mikhail, you really\x01",
            "I'm glad I could leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "By around this time, in Les Autonomous states\x01",
            "Have fun with your mothers\x01",
            "I guess you are living … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7192")

    Jump("loc_7314")

    label("loc_7197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_71A5")
    Jump("loc_7314")

    label("loc_71A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_71B3")
    Jump("loc_7314")

    label("loc_71B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7271")

    ChrTalk(
        0x13,
        (
            "People who are hospitalized here are people,\x01",
            "I left the hospital a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That man, selfishly\x01",
            "I was struggled really … ….\x01",
            "I wonder where and what I am doing now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7314")

    label("loc_7271")


    ChrTalk(
        0x13,
        (
            "Oh, by the way, today\x01",
            "Shillon is going on dripping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That girl, always mistaking a mistake\x01",
            "I am worried because I will do it.\x01",
            "…… Let's go to see the situation later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7314")

    TalkEnd(0xFE)
    Return()

    # Function_32_6EEB end

    def Function_33_7318(): pass

    label("Function_33_7318")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7329")
    Jump("loc_73E9")

    label("loc_7329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7337")
    Jump("loc_73E9")

    label("loc_7337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7345")
    Jump("loc_73E9")

    label("loc_7345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7353")
    Jump("loc_73E9")

    label("loc_7353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7361")
    Jump("loc_73E9")

    label("loc_7361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_736F")
    Jump("loc_73E9")

    label("loc_736F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_73E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738A")
    Call(0, 34)
    Jump("loc_73E9")

    label("loc_738A")


    ChrTalk(
        0x14,
        (
            "Even so\x01",
            "Professor Seyland … ….\x01",
            "It's a wonderful skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I also learn from her\x01",
            "That seems to be a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E9")

    TalkEnd(0xFE)
    Return()

    # Function_33_7318 end

    def Function_34_73ED(): pass

    label("Function_34_73ED")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "HM……\x01",
            "The postoperative course seems to be good,\x01",
            "I will be able to leave the hospital soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Later to parents of Leman Autonomous Region\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Honestly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, it is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Professor Seyland also has some skills,\x01",
            "Your courage to decide surgery than anything is\x01",
            "I overcame my illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "… Good luck with ne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… …. Gusun … ….\x01",
            "Thanks teacher……!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 6)
    SetChrSubChip(0xE, 0x0)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_34_73ED end

    def Function_35_7555(): pass

    label("Function_35_7555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_762C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7573")
    Call(0, 21)
    Jump("loc_7627")

    label("loc_7573")


    ChrTalk(
        0x16,
        (
            "The truth is, the expected discharge date is\x01",
            "It was already a few days ahead ….\x01",
            "I was asked by this person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Uhufu, but I'm really happy.\x01",
            "I see that this person is working\x01",
            "Because I like the most\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7627")

    Jump("loc_7A9F")

    label("loc_762C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_77A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772F")

    ChrTalk(
        0x16,
        (
            "The book that I brought for my wedlock,\x01",
            "I read it completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "There is no point in reading the same book a number of times ……\x01",
            "Yes, to you\x01",
            "I will give you a gift ♪\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝13卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝13卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 4)
    Jump("loc_779C")

    label("loc_772F")


    ChrTalk(
        0x16,
        (
            "Defense forces people who came to the hospital, too,\x01",
            "She seems to have returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "…… What is going to happen?\x02",
    )

    CloseMessageWindow()

    label("loc_779C")

    Jump("loc_7A9F")

    label("loc_77A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_795A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A9")

    ChrTalk(
        0x16,
        (
            "When I am declaring independence\x01",
            "I came to visit you, as it is\x01",
            "I was staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Requests for traveling to and from the city\x01",
            "It just became a hassle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I also spend it slowly with this person\x01",
            "It was quite a chance,\x01",
            "In this case it will be a loss unless you enjoy it ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7955")

    label("loc_78A9")


    ChrTalk(
        0x16,
        (
            "When I am declaring independence\x01",
            "I came to visit you, as it is\x01",
            "I was staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I also spend it slowly with this person\x01",
            "It was quite a chance,\x01",
            "In this case it will be a loss unless you enjoy it ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7955")

    Jump("loc_7A9F")

    label("loc_795A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_7A1C")

    ChrTalk(
        0x16,
        (
            "Hehe, this person\x01",
            "I am not young now and it is inconsistent … …\x01",
            "I was worried about Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "But, like you\x01",
            "Because I could protect a cute girl,\x01",
            "It was the best fine play ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9F")

    label("loc_7A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A37")
    Call(0, 21)
    Jump("loc_7A9F")

    label("loc_7A37")


    ChrTalk(
        0x16,
        (
            "Somehow it seems to be hard\x01",
            "I know, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For now not to be unreasonable,\x01",
            "I have to look properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A9F")

    TalkEnd(0xFE)
    Return()

    # Function_35_7555 end

    def Function_36_7AA3(): pass

    label("Function_36_7AA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7AB4")
    Jump("loc_8203")

    label("loc_7AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7AC2")
    Jump("loc_8203")

    label("loc_7AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C86")

    ChrTalk(
        0x17,
        (
            "Being a diplomatic official as an independent country\x01",
            "The biggest pain is, with Remiferia\x01",
            "It is that cooperation can not be taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "To some extent medical supplies,\x01",
            "There is a large stockpile on the president side\x01",
            "It seems to be prepared … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "In the first place,\x01",
            "Depending on the patient's symptoms and constitution\x01",
            "It chooses carefully and prescribes it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "The extent to which the president is stockpiling\x01",
            "In the type of medicine, for all patients\x01",
            "It will be difficult to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "From now on how to do … …\x01",
            "I need to think about something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_7D23")

    label("loc_7C86")


    ChrTalk(
        0x17,
        (
            "The extent to which the president is stockpiling\x01",
            "In the type of medicine, for all patients\x01",
            "It will be difficult to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "From now on how to do … …\x01",
            "I need to think about something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D23")

    Jump("loc_8203")

    label("loc_7D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8073")

    ChrTalk(
        0x17,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMr. Cayland … …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 500)

    ChrTalk(
        0x17,
        "…… You guys are a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt was Shizuku 's hospital room here.\x01",
            "…… What in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "It is a patient who was in charge of your doctor.\x01",
            "I was a little intrigued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "… … by Arios McRae\x01",
            "I wonder what you are doing after being discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FBy the way, since then\x01",
            "I have not seen her either.\x02\x03",
            "#10403FPerhaps, somewhere in the Orchis Tower\x01",
            "I guess they are protected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "…… How much father, though,\x01",
            "I was deprived of my patient\x01",
            "It is nothing but humiliation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I transferred to the Secretary of Defense\x01",
            "Under that circumstance, there is no choice\x01",
            "I do not know but.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I do not know but …\x01",
            "I can not be convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001Fteacher……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Sorry\x01",
            "It seems like we had a useless story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Is he in the middle of a visit?\x01",
            "…… Worse but you can leave me alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 6)
    ClearChrFlags(0x17, 0x10)
    Jump("loc_8203")

    label("loc_8073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_816E")

    ChrTalk(
        0x17,
        (
            "Shizuoku · Mc Rain …\x01",
            "Her treatment policy is up to the next year\x01",
            "It was planned carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "…… How much father, though,\x01",
            "I was deprived of my patient\x01",
            "It is nothing but humiliation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Even if I dragged himself out of the discharged patient\x01",
            "Maybe it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8203")

    label("loc_816E")


    ChrTalk(
        0x17,
        (
            "…… How much father, though,\x01",
            "I was deprived of my patient\x01",
            "It is nothing but humiliation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Even if I dragged himself out of the discharged patient\x01",
            "Maybe it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8203")

    TalkEnd(0xFE)
    Return()

    # Function_36_7AA3 end

    def Function_37_8207(): pass

    label("Function_37_8207")

    Sound(160, 0, 100, 0)
    Return()

    # Function_37_8207 end

    def Function_38_820E(): pass

    label("Function_38_820E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83CF")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13500, 600, 30340, 0)
    MoveCamera(43, 29, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20580, 0)
    SetChrPos(0x106, -12930, 0, 29900, 270)
    SetChrPos(0x101, -15140, 0, 29900, 90)
    SetChrPos(0x102, -15140, 0, 31030, 90)
    SetChrPos(0x103, -15140, 0, 28800, 90)
    SetChrPos(0x104, -16360, 0, 30550, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82C3")
    SetChrPos(0x109, -16360, 0, 29320, 90)

    label("loc_82C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82E4")
    SetChrPos(0x105, -16360, 0, 29320, 90)

    label("loc_82E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8305")
    SetChrPos(0x10A, -16360, 0, 29320, 90)

    label("loc_8305")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#10703F(……everyone.\x01",
            "If you get in, I am here … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(……I understood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F(Will you act as usual?)\x02",
    )

    CloseMessageWindow()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -16360, 0, 29440, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    SetScenarioFlags(0x1CE, 3)
    Jump("loc_8433")

    label("loc_83CF")

    TalkBegin(0xFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-100110, 1050, -1300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x5, 0xFF)
    SetScenarioFlags(0x2, 3)
    SetChrPos(0x0, -100110, 50, -1300, 180)
    FadeToBright(500, 0)
    TalkEnd(0xFF)

    label("loc_8433")

    Return()

    # Function_38_820E end

    def Function_39_8434(): pass

    label("Function_39_8434")

    TalkBegin(0xFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-16500, 1000, 27500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x2, 3)
    SetChrPos(0x0, -16500, 0, 27500, 0)
    FadeToBright(500, 0)
    TalkEnd(0xFF)
    Return()

    # Function_39_8434 end

    def Function_40_849C(): pass

    label("Function_40_849C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(2723)
    AddParty(0x35, 0xFF, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11700.itp")
    SetChrPos(0x101, -1400, 0, -50500, 90)
    SetChrPos(0x102, -1400, 0, -49500, 90)
    SetChrPos(0x103, -2500, 0, -50500, 90)
    SetChrPos(0x104, -2500, 0, -49500, 90)
    SetChrPos(0x109, -3600, 0, -50500, 90)
    SetChrPos(0x105, -3600, 0, -49500, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6300, 600, -47500, 270)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x136, 6000, 0, -49000, 0)
    OP_68(6080, 2500, -47450, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_68(6080, 1000, -47450, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2P#2SExcuse me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_68(5670, 1000, -47970, 2500)

    def lambda_8674():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8674)
    Sleep(200)

    def lambda_868C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_868C)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    def lambda_86A8():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86A8)

    def lambda_86BD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_86BD)
    Sleep(50)

    def lambda_86CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_86CD)
    Sleep(50)

    def lambda_86E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_86E5)
    Sleep(50)

    def lambda_86FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86FD)

    def lambda_8712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8712)
    Sleep(200)

    def lambda_8726():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8726)
    Sleep(500)

    def lambda_873A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_873A)

    def lambda_874B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_874B)
    Sleep(500)

    def lambda_875F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_875F)

    def lambda_8770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8770)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11705F#2723V#5P#40WAh……\x01",
            "Onee, everyone …!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA3)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x136,
        "#01302F#11POh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PCecil elder sister, I was here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#6P#NExcuse me.\x01",
            "Will it be okay now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x136,
        (
            "#01309F#11PHuhu, that's fine.\x01",
            "I just replaced the drip.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5920, 1000, -48010, 2000)

    def lambda_88A6():
        OP_9B(0x1, 0xFE, 0xE1, 0x6D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_88A6)
    Sleep(350)
    BeginChrThread(0x101, 1, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 42)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 44)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 43)
    Sleep(150)
    BeginChrThread(0x105, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 46)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#30WErr …\x01",
            "Thank you.\x02\x03",
            "Take the trouble to visit\x01",
            "Did she come … -?\x02",
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
        0x101,
        (
            "#00002F#12POh, from Noel\x01",
            "Please listen to your consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHehe, than I thought\x01",
            "I was relieved to be healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PYeah.\x01",
            "Your complexion seems to be good, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WEven, I'm fine.\x01",
            "It is all right now.\x02\x03",
            "#11700FAlso in the general hospital room in a couple of days\x01",
            "It seems I can move … ….\x02\x03",
            "#11709FIf you do so\x01",
            "It is soon to be discharged from the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PNo, Fran.\x02\x03",
            "#10101FMy physical strength is falling down.\x01",
            "I have to rest for a while … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WErr …\x01",
            "How lucky I am.\x02\x03",
            "#11708FIt shields me\x01",
            "Donovan security officer …\x02\x03",
            "#11706F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PMr. Fran. ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6P…… Franc is\x01",
            "You do not need to be sick.\x02\x03",
            "#00301FThat guy's … evil …\x01",
            "It is a hunter of \"red constellation\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#5P#30WErr … Yes.\x02\x03",
            "#11711FBut, for your support\x01",
            "I also have backups ……\x02\x03",
            "#11706FI do my best and I have to recover …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PDo not worry, be relieved.\x02\x03",
            "#00000FI'm lonely that I can not hear francers' voices\x01",
            "It seems that we can manage the report anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PNow concentrate on recovery\x01",
            "Please be full of energy.\x02\x03",
            "#00102FThen we\x01",
            "Because I can depend on you without reserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W……Yes.\x01",
            "Thank you.\x02\x03",
            "#11705Fby the way……\x01",
            "Onee, my guard\x01",
            "I guess I get back …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PDid you ask from my mother?\x01",
            "…. Yeah, I thought of various things.\x02\x03",
            "#10112FFuran's support\x01",
            "It will not be accepted\x01",
            "I am somewhat lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11701F#5P#40WMum, what a little\x01",
            "Because I am downright ……\x02\x03",
            "#11706F#50W…… roughly sister ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8F9C():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8F9C)
    WaitChrThread(0x8, 2)
    Sleep(500)
    SetChrSubChip(0x8, 0x2)
    Fade(250)
    OP_0D()
    Sleep(300)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x109,
        "#10111F#12PFran … …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x136,
        (
            "#01304F#11PAll right, drip medicine\x01",
            "Because it is only effective.\x02\x03",
            "#01302FTalk about this story\x01",
            "You had better go to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11706F#11P#40WIt's okay …\x01",
            "Mr. Lloyd's\x01",
            "He came and ……\x02\x03",
            "#11701FBesides, before returning to the guard\x01",
            "My sister has a winning method ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PHuh, what are you talking about?\x02\x03",
            "#10108F…… Everyone, I'm sorry.\x01",
            "Can I get it to sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12Pof course.\x01",
            "… … Fran, I will come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6Pplease rest at ease.\x02\x03",
            "#00202FIf your strength returns, even cake\x01",
            "Because I will come to the deposit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#11P#40WHaha ……\x01",
            "Yeah, I'm looking forward to it ….\x02\x03",
            "#11704F#50W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(6270, 1000, -47800, 800)
    SetCameraDistance(21380, 800)
    Sound(898, 0, 100, 0)
    SetChrPos(0x8, 6100, 400, -47500, 270)
    SetChrSubChip(0x8, 0x3)
    OP_0D()
    Sleep(300)
    OP_6F(0x79)
    OP_63(0x8, 0x12C, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x105,
        (
            "#10308F#6P…… after all reasonable,\x01",
            "Your physical strength seems to be falling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11PYes, at the time of surgery\x01",
            "I had a considerable transfusion … …\x02\x03",
            "#01300FBut the rest will only get better.\x02\x03",
            "#01309FI am fine, I will be fine soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#12PYes..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P… … Once I go out.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x8)
    OP_68(4990, 1000, 7500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23300, 0)
    SetChrPos(0x101, 3250, 0, 7700, 90)
    SetChrPos(0x102, 3250, 0, 6300, 90)
    SetChrPos(0x104, 3750, 0, 8800, 135)
    SetChrPos(0x103, 3750, 0, 5500, 45)
    SetChrPos(0x109, 2100, 0, 7900, 90)
    SetChrPos(0x105, 2100, 0, 6100, 90)
    SetChrPos(0x136, 7200, 0, 7500, 270)
    OP_A7(0x136, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    SetCameraDistance(22800, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    Sound(107, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)

    def lambda_9550():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9550)
    Sleep(50)

    def lambda_9568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_9568)
    WaitChrThread(0x136, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00005F#6Pby the way……\x02\x03",
            "#00001FAfter all, Donovan police and\x01",
            "Is Iria an apology forgiveness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#11P… Well, for a moment.\x02\x03",
            "#01308FBut you both\x01",
            "It's like a stake … ….\x02\x03",
            "#01300FBecause I am accompanied\x01",
            "Do you look into the situation of the two people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PIs not it good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#12PThat is appreciated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PCecil, I will ask you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#11PWhatching\x01",
            "Well then let's go.\x02\x03",
            "#01300FRoom 302 is right there\x01",
            "I will become a hospital room for Mr. Donovan.\x02\x03",
            "Iria room 303 … …\x01",
            "It is opposite the room of Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI understood, I should go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x1, 0x1E)
    SetChrPos(0x0, 4500, 0, 7500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x180, 7)
    OP_29(0xAC, 0x1, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_40_849C end

    def Function_41_9811(): pass

    label("Function_41_9811")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_41_9811 end

    def Function_42_9846(): pass

    label("Function_42_9846")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xFA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_9846 end

    def Function_43_986C(): pass

    label("Function_43_986C")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_43_986C end

    def Function_44_9898(): pass

    label("Function_44_9898")

    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x79E, 0x7D0, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_44_9898 end

    def Function_45_98BE(): pass

    label("Function_45_98BE")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_98BE end

    def Function_46_98F3(): pass

    label("Function_46_98F3")

    OP_9B(0x0, 0xFE, 0x4, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_46_98F3 end

    def Function_47_9919(): pass

    label("Function_47_9919")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-50500, 1000, -50000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_68(-54200, 1000, -46530, 0)
    MoveCamera(39, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(23500, 2000)
    SetChrPos(0x136, -50000, 50, -50000, 270)
    SetChrPos(0x101, -48900, 50, -49660, 270)
    SetChrPos(0x102, -48900, 50, -50640, 270)
    SetChrPos(0x103, -47900, 50, -50640, 270)
    SetChrPos(0x104, -47900, 50, -49660, 270)
    SetChrPos(0x109, -46900, 50, -49660, 270)
    SetChrPos(0x105, -46900, 50, -50640, 270)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    NpcTalk(
        0x136,
        "Cecil's voice",
        (
            "#2S#5PMr. Raymond?\x01",
            "I will enter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    Sound(107, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-53710, 1000, -47510, 3000)
    SetCameraDistance(24000, 3000)

    def lambda_9B01():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9B01)

    def lambda_9B16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_9B16)
    Sleep(100)
    Sleep(100)

    def lambda_9B2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B2D)

    def lambda_9B3E():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B3E)
    Sleep(100)

    def lambda_9B56():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B56)
    Sleep(100)

    def lambda_9B6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B6E)

    def lambda_9B7F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B7F)
    Sleep(100)

    def lambda_9B97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B97)

    def lambda_9BA8():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BA8)
    Sleep(100)

    def lambda_9BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BC0)

    def lambda_9BD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BD1)
    Sleep(100)

    def lambda_9BE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9BE9)

    def lambda_9BFA():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9BFA)
    Sleep(100)

    def lambda_9C12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C12)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x4, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#6PMs. Cecil …\x01",
            "Besides, you guys ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PRaymond,\x01",
            "…… Thank you very much for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PI was in attendance, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHaha … by chance\x01",
            "Instead of Mrs. Guard's wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PIf the police woke up\x01",
            "\"What sells oil! \"\x01",
            "She seems to be shouting yells ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#11PReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PVery much\x01",
            "It seems like I'm going to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PThat device …\x01",
            "Could it be a mechanical ventilator?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PYeah … quite respiratory system\x01",
            "They seem to have been damaged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf somehow consciousness comes back\x01",
            "I think recovery will be accelerated, though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11P…… The policeman is.\x01",
            "At the time of the explosion, I and Fran-chan\x01",
            "It protected me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThat hard time,\x01",
            "It was only Orooro.\x01",
            "I'm sick of someone ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PMoreover, Fran?\x01",
            "It was a huge injury to operate\x01",
            "I was almost scraped … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P…… Good luck with your luck\x01",
            "The figure will be miserable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11PRaymond san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11P… … It's not your fault.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11P…… Raymond.\x01",
            "Why do not you take a break?\x02\x03",
            "#01301FNow the condition is stable,\x01",
            "Because we are patrolling.\x02\x03",
            "I do not have a little to rest.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    ChrTalk(
        0xA,
        "#6PHaha … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PBut a little more\x01",
            "Because the wife 's wife comes,\x01",
            "Until then … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#01306F#11PWell … OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11P… please be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PI will come to visit you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYup……\x01",
            "I think the policeman will be delighted, too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    SetCameraDistance(24250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x4, 0x1E)
    SetChrPos(0x0, -53500, 0, -50000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 0)
    OP_29(0xAC, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_47_9919 end

    def Function_48_A256(): pass

    label("Function_48_A256")

    Sleep(600)
    Sound(107, 0, 100, 0)
    Return()

    # Function_48_A256 end

    def Function_49_A260(): pass

    label("Function_49_A260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-96210, 1600, -4360, 0)
    MoveCamera(55, 15, 0, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22330, 0)
    LoadChrToIndex("apl/ch51521.itc", 0x1E)
    SetChrPos(0x136, -100000, 50, -150, 180)
    SetChrPos(0x102, -100660, 50, 1100, 180)
    SetChrPos(0x101, -99640, 50, 1100, 180)
    SetChrPos(0x103, -100660, 50, 2200, 180)
    SetChrPos(0x104, -99640, 50, 2200, 180)
    SetChrPos(0x109, -100660, 50, 3300, 180)
    SetChrPos(0x105, -99640, 50, 3300, 180)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-96210, 800, -4360, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    NpcTalk(
        0x136,
        "Cecil's voice",
        (
            "#2S#11PShri-chan?\x01",
            "I wonder if that is OK.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04208F#5P#30W…\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-97700, 1000, -3750, 3000)

    def lambda_A43B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_A43B)
    Sleep(50)

    def lambda_A453():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A453)

    def lambda_A468():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_A468)
    Sleep(50)

    def lambda_A47C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A47C)
    Sleep(50)

    def lambda_A494():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A494)
    Sleep(50)

    def lambda_A4AC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4AC)
    Sleep(50)

    def lambda_A4C4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4C4)
    Sleep(50)

    def lambda_A4DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A4DC)
    Sleep(50)
    Sleep(100)

    def lambda_A4F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4F7)

    def lambda_A508():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A508)
    Sleep(400)

    def lambda_A51C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A51C)

    def lambda_A52D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A52D)
    Sleep(400)

    def lambda_A541():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A541)

    def lambda_A552():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A552)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x5, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008F#5PShuri …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_A5DF")

    ChrTalk(
        0x102,
        "#00108F#5P………………………….\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5FD")

    label("loc_A5DF")


    ChrTalk(
        0x102,
        "#00106F#5PI was coming … ….\x02",
    )

    CloseMessageWindow()

    label("loc_A5FD")

    OP_68(-97460, 1000, -5050, 2500)
    MoveCamera(50, 20, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(20500, 2500)
    OP_93(0x136, 0x87, 0x1F4)
    BeginChrThread(0x136, 1, 0, 52)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 53)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 54)
    Sleep(100)
    BeginChrThread(0x103, 1, 0, 55)
    Sleep(100)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(100)
    BeginChrThread(0x105, 1, 0, 57)
    Sleep(100)
    BeginChrThread(0x109, 1, 0, 58)
    OP_6F(0x79)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#11P#5P#60W………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P#NIlia…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00301F#5P…\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#04206F#6P#30WIt's quiet … … is a pretty sleeping face?\x02\x03",
            "#04208FAlways Gusuka,\x01",
            "To the habit of being unrestrainedly sleeping\x01",
            "Only at such times ……\x02\x03",
            "#04202FHahaha ….\x01",
            "Iria · Platier seems like\x01",
            "It's too much ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#5P… … How is the condition?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#5P…… With a fracture of the whole body\x01",
            "Damage to internal organs.\x02\x03",
            "#01308FAlthough the surgery was successful\x01",
            "I am still in a coma state … …\x02\x03",
            "#01301FNow to life support equipment\x01",
            "It is a situation I have no choice but to rely on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P… until that point ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5P… … damn it …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P#N…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#04202F#6P#30W…… Even if regaining consciousness\x01",
            "It's desperate for return ……\x02\x03",
            "Can you believe it?\x01",
            "That Iria got on stage\x01",
            "I will not do it again … ….?\x02\x03",
            "#04208FThat also me ……\x01",
            "I will elevate my something#2RHippopotamus#That's why ….\x02\x03",
            "#04206F#40W……such a……\x01",
            "There is not such a thing ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA20():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AA20)
    Sleep(800)
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00001F#5P… … Shuri ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#01303F#5P…\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0xB4, 0x190)
    Sleep(300)
    SetCameraDistance(19500, 1500)
    BeginChrThread(0x136, 1, 0, 50)
    WaitChrThread(0x136, 1)
    SetChrFlags(0x136, 0x2)
    SetChrChipByIndex(0x136, 0x1E)
    SetChrSubChip(0x136, 0x0)
    Sound(898, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#04205F#6P#40W………Huh……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#5PIt's okay … It will be fine.\x02\x03",
            "About Ilya\x01",
            "I know best.\x02\x03",
            "#01308FNever give up on any adversity\x01",
            "Just keep on watching over … …\x02\x03",
            "#01302FThat's Iria-Platier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04212F#6P#40WWell … but ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P─ ─ I think so.\x02\x03",
            "#00002FOtherwise,\x01",
            "I do not think such a stage of common sense\x01",
            "I think that it can not be created.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6P#NI see …\x02\x03",
            "#00102FIria's greed is there\x01",
            "I think that it is the space that can be realized for the first time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00204F#6P#NAs long as there is a stage there ……\x01",
            "I'm sure Mr. Ilia will come back.\x02\x03",
            "#00202FIt seems strange to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#04205F#6P#30W… … … … … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PRight\x02\x03",
            "#00300FNow believe in the goddess and Iria\x01",
            "It is time to do what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PRegardless of today, the stage practice is\x01",
            "You better not miss it?\x02\x03",
            "#10302FShe is also\x01",
            "I'm getting caught and getting up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PWell … I bet it is!\x02\x03",
            "#10102FFished in a stage that looks like a fun\x01",
            "I will definitely wake up … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04212F#6P#30W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19750, 800)
    ClearChrFlags(0x136, 0x2)
    SetChrChipByIndex(0x136, 0xA)
    SetChrSubChip(0x136, 0x0)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x136, 1, 0, 51)
    WaitChrThread(0x136, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#04204F#6P… with ….\x01",
            "I came out a little.\x02\x03",
            "#04208FThat's right …\x01",
            "If we do not get firm … …\x02\x03",
            "Lisa's older sister ….\x01",
            "I have gone away … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P#NAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#5P…\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#04206F#6P…… Hello, I guess.\x02\x03",
            "If possible, Lisa's older sister,\x01",
            "Can you find me …?\x02\x03",
            "#04208FWhatever the circumstances may be\x01",
            "Lisa's older sister is Lisa's older sister … …\x02\x03",
            "#04201FBesides, if Lisa's older sister comes back,\x01",
            "I think that Iria will be well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P── It turned out.\x02\x03",
            "#00000FBet on the name of the Special Affairs Support Division\x01",
            "I will definitely find it and show it out.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(1016, 1000, 100)
    SetCameraDistance(20250, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-16329, 3200, 29420, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17760, 0)
    SetChrPos(0x101, -17100, 0, 29000, 180)
    SetChrPos(0x102, -15900, 0, 29000, 180)
    SetChrPos(0x103, -17600, 0, 29700, 180)
    SetChrPos(0x104, -15400, 0, 30300, 180)
    SetChrPos(0x109, -17200, 0, 31200, 180)
    SetChrPos(0x105, -15800, 0, 31200, 180)
    SetChrPos(0x136, -16500, 0, 27500, 0)
    OP_68(-16329, 1200, 29420, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x136,
        (
            "#01302F#12P……Thanks guys.\x02\x03",
            "Shuri in this too\x01",
            "I think I can regain my energy.\x02\x03",
            "#01304FMe too……\x01",
            "I got a little encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5PCecil elder sister …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PAfter all it is equivalent,\x01",
            "It is a serious condition …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#12PYeah ….\x01",
            "To be honest, I can not rest assured.\x02\x03",
            "#01308F…… But still after all,\x01",
            "Because I believe in Iria.\x02\x03",
            "#01302FThe more people that believe in it\x01",
            "I think she will respond to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#5PThat's right …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5PCertainly it is\x01",
            "Maybe Iria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PBut then …\x01",
            "After all the key \"her#4RLisha#\"?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B423():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B423)
    WaitChrThread(0x105, 2)
    Sleep(150)

    ChrTalk(
        0x105,
        "#10300F#5PLloyd, can you find it?\x02",
    )

    CloseMessageWindow()

    def lambda_B463():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B463)
    Sleep(150)

    def lambda_B473():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B473)
    Sleep(50)

    def lambda_B483():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B483)
    Sleep(50)

    def lambda_B493():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B493)
    Sleep(50)

    def lambda_B4A3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B4A3)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x101,
        (
            "#00003F#6P…… To be honest, I do not know.\x02\x03",
            "#00008FIf I seriously hid myself\x01",
            "It will be quite difficult to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PI agree……\x02\x03",
            "#10108FLike the missing \"Black Moon\"\x01",
            "I might be in autonomous state\x01",
            "I do not know clearly … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PI got back to Calvert.\x01",
            "There is also a possibility ……\x02\x03",
            "#00300FHowever,\x01",
            "If such a request asks you\x01",
            "I can not give it up, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6POh, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PTogether with the way of \"Black moon\"\x01",
            "You should take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PI will also drive the direction of the Internet\x01",
            "Always check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#12PHehe … … Thank you so much.\x02\x03",
            "#01300FI will return to the nurse station\x01",
            "What about Lloyd's?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B749():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B749)
    Sleep(150)

    def lambda_B759():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B759)
    Sleep(50)

    def lambda_B769():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B769)
    Sleep(50)

    def lambda_B779():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B779)
    Sleep(50)

    def lambda_B789():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B789)
    Sleep(50)

    def lambda_B799():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B799)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00002F#5POh, I still have work\x01",
            "Soon it's time#2RIt is#I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PPlease show me around\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01309F#12PHuhu, this is it.\x02\x03",
            "#01302FIt's a tough situation ….\x01",
            "Let's work hard.\x02\x03",
            "But do not overdo it, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PAcknowledgment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PCongratulations.\x02",
    )

    CloseMessageWindow()
    OP_68(-14130, 1200, 29280, 3000)
    BeginChrThread(0x136, 1, 0, 59)
    Sleep(400)

    def lambda_B90B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B90B)
    Sleep(350)

    def lambda_B91B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B91B)
    Sleep(150)

    def lambda_B92B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B92B)
    Sleep(250)

    def lambda_B93B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B93B)
    Sleep(150)

    def lambda_B94B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B94B)
    Sleep(150)

    def lambda_B95B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B95B)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(-16329, 1200, 29420, 1300)
    MoveCamera(43, 22, 0, 1300)
    OP_6E(440, 1300)
    SetCameraDistance(17760, 1300)

    def lambda_BA1A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA1A)
    Sleep(150)

    def lambda_BA2A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA2A)
    Sleep(50)

    def lambda_BA3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA3A)
    Sleep(50)

    def lambda_BA4A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA4A)
    Sleep(50)

    def lambda_BA5A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BA5A)
    Sleep(50)

    def lambda_BA6A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BA6A)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6Ptruly……\x01",
            "This place is in the edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PYeah … That's right.\x02\x03",
            "#00108FTo those who have been hurt the heart and body\x01",
            "To have a smile come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P…………………………\x01",
            "(Walking around, is it?)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18260, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RemoveParty(0x35, 0xFF)
    OP_74(0x5, 0x1E)
    SetChrPos(0x0, -16500, 0, 29250, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 1)
    OP_29(0xAC, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_49_A260 end

    def Function_50_BBF3(): pass

    label("Function_50_BBF3")

    OP_9B(0x0, 0xFE, 0x5, 0xFA, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x5, 0xC8, 0x1F4, 0x0)
    Return()

    # Function_50_BBF3 end

    def Function_51_BC12(): pass

    label("Function_51_BC12")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1F4, 0x0)
    Return()

    # Function_51_BC12 end

    def Function_52_BC22(): pass

    label("Function_52_BC22")

    OP_96(0x136, 0xFFFE7C08, 0x0, 0xFFFFED7C, 0x4B0, 0x0)
    Return()

    # Function_52_BC22 end

    def Function_53_BC37(): pass

    label("Function_53_BC37")

    OP_95(0xFE, -97730, 0, -3800, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_53_BC37 end

    def Function_54_BC53(): pass

    label("Function_54_BC53")

    OP_95(0xFE, -100440, 0, -7000, 1500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_BC53 end

    def Function_55_BC6F(): pass

    label("Function_55_BC6F")

    OP_95(0xFE, -101020, 0, -6010, 1500, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_BC6F end

    def Function_56_BC8B(): pass

    label("Function_56_BC8B")

    OP_95(0xFE, -98500, 0, -3400, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_56_BC8B end

    def Function_57_BCA7(): pass

    label("Function_57_BCA7")

    OP_95(0xFE, -99600, 0, -3350, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_57_BCA7 end

    def Function_58_BCC3(): pass

    label("Function_58_BCC3")

    OP_95(0xFE, -100570, 0, -4650, 1500, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_58_BCC3 end

    def Function_59_BCDF(): pass

    label("Function_59_BCDF")

    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xBB8, 0x7D0, 0x1)
    Return()

    # Function_59_BCDF end

    def Function_60_BD2B(): pass

    label("Function_60_BD2B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11600.itp")
    OP_68(-100000, 1000, -3500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100660, 50, 1100, 180)
    SetChrPos(0x103, -99640, 50, 1100, 180)
    SetChrPos(0x105, -100160, 50, 2200, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(808, 0, 80, 0)
    Sleep(300)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x2)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "#11PAhh?\x02\x03",
            "In what way?\x01",
            "You can enter.\x02",
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
    Sound(107, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)

    ChrTalk(
        0x103,
        "#00204F#6PExcuse us\x02",
    )

    CloseMessageWindow()
    OP_68(-97660, 1000, -3500, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_BF2F():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF2F)

    def lambda_BF44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF44)
    Sleep(100)

    def lambda_BF58():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF58)

    def lambda_BF6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF6D)
    Sleep(100)

    def lambda_BF81():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF81)

    def lambda_BF96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BF96)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x5, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#11602F#11PAh it's Tio and\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#11605F#11PHuh, it's little bro!?\x02\x03",
            "#11602FAnd you …\x01",
            "I wonder if Was it certainly Washi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5PYes, nice to see you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PIlia…\x01",
            "It is really long time no see.\x02\x03",
            "#00006FI'm sorry, I have a wed list\x01",
            "I came by hand … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609F#11POh no!\x01",
            "I should not mind that!\x02\x03",
            "#11602FHorahora, three of us.\x01",
            "Welcome to come over here.\x02\x03",
            "#11605FOh, sweets from fans or something\x01",
            "You can eat it without permission?\x02\x03",
            "#11609FIf it was cookie\x01",
            "I think that it is still within the expiration date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PAhah\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PWell then excuse us\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -99500, 0, -5700, 0)
    SetChrPos(0x101, -99300, 200, -5700, 90)
    SetChrPos(0x103, -99500, 0, -6800, 45)
    SetChrPos(0x105, -100100, 0, -5100, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    OP_68(-97700, 400, -3750, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    Sleep(500)
    SetCameraDistance(21000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#11603F#11PI see…\x01",
            "You guys seems to be in trouble.\x02\x03",
            "#11601FCrossbell itself\x01",
            "It is unbelievable that\x01",
            "I have heard a lot of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYes..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6PWell, surely it is ridiculous\x01",
            "It's a situation you can not express.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11PWell, my legs do not move.\x01",
            "It's frustrating and it can not be helped …\x02\x03",
            "#11608FThe appearance of alkane shell\x01",
            "I'd like to check with this eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WUh, Ilia\x02\x03",
            "#00008FYour body… uh\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11605F#11POh yes…\x02\x03",
            "#11603FMr. Seyland,\x01",
            "Whether it will become possible to walk or not\x01",
            "I do not know at the moment.\x02\x03",
            "#11600FWell, 100 impossible\x01",
            "I was not asserted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#40WI … see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#6P#30W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11POh, if I can have such a face\x01",
            "It's going to be dark here.\x02\x03",
            "#11601FHey ─ ─ If I think I can not do it\x01",
            "That alone will not eliminate the possibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604F#11PEven if it's on the stage … …\x01",
            "There is always an \"answer\" somewhere.\x02\x03",
            "#11600FNo matter how painful or desperate,\x01",
            "Absolute light is absolute#4R噵 噵#I have it.\x02\x03",
            "#11609FAs long as you don't give up, for sure\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PEhe\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6PYou are amazing\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11PWell, something extraordinary\x01",
            "I wonder if it is enough to be told.\x02\x03",
            "#11601FFirst, as long as you talk,\x01",
            "Are you serious, are not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P…… Certainly, if you think normally\x01",
            "It was a terribly difficult course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604F#11PSame here, same\x02\x03",
            "#11600FIf people are important things\x01",
            "It is a living thing that I can keep trying anywhere.\x02\x03",
            "Degree of degree ……\x01",
            "I think that is the strength of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PThe strength of a person\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11602F#11PWell, I am among them\x01",
            "I think that it is a rather greedy person.\x02\x03",
            "Still the essential point is\x01",
            "I think other people are the same.\x02\x03",
            "#11604FMy theater company members ……\x02\x01",
            "#11600F─ ─ Of course Lisha, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F#6PIlia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11602F#11PIf you can see that girl\x01",
            "Can you tell me?\x02\x03",
            "#11604F\"── For you,\x01",
            "What is the most important thing? \"\x02\x03",
            "\"Before that important thing\x01",
            "Can you go without trying hard? What?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PUnderstood\x02\x03",
            "#00000FIf I can meet Lisha\x01",
            "I will surely tell you the words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11609F#11PYes, I'll be counting on you\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21225, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -100000, 0, -5000, 90)
    OP_69(0xFF, 0x0)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrSubChip(0xB, 0x0)
    OP_74(0x5, 0x1E)
    SetScenarioFlags(0x1A0, 6)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_60_BD2B end

    def Function_61_CBCF(): pass

    label("Function_61_CBCF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-16500, 1000, 30000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -17100, 0, 26000, 0)
    SetChrPos(0x103, -15900, 0, 26000, 0)
    SetChrPos(0x105, -16500, 0, 25000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_CC6B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CC6B)

    def lambda_CC80():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC80)
    Sleep(50)

    def lambda_CC98():
        OP_9B(0x0, 0xFE, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CC98)
    Sleep(50)
    Sleep(50)
    Sleep(100)

    def lambda_CCB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CCB6)

    def lambda_CCC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CCC7)
    Sleep(400)

    def lambda_CCDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CCDB)
    Sleep(800)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    OP_0D()

    def lambda_CD02():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD02)
    Sleep(50)

    def lambda_CD12():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CD12)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10404F#12PAhah\x01",
            "Really, that's unexpected.\x02\x03",
            "#10402FTruly \"Princess of Fire\"\x01",
            "There is nothing to be called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5P… Rather, the stage\x01",
            "\"Is it the princess of the sun\" itself.\x02\x03",
            "#00208FI was brought here, too,\x01",
            "I have been talking a couple of times ….\x02\x03",
            "#00202FMr. Cecil,\x01",
            "I was very encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see…\x02\x03",
            "#00008F…… Really, Leitha too\x01",
            "I hope I can find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, that's all\x01",
            "It seems that the goddesss are meeting each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_CF71")

    ChrTalk(
        0x103,
        (
            "#00202F#5PTalk to Mr. Fran\x01",
            "Shall we return soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, let's\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_CFF2")

    label("loc_CF71")


    ChrTalk(
        0x103,
        (
            "#00202F#5PDonovan police also\x01",
            "Shall we go to visit you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, let's\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16500, 0, 30000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_CFF2")

    Return()

    # Function_61_CBCF end

    def Function_62_CFF3(): pass

    label("Function_62_CFF3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-52720, 1000, -50000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -49020, 0, -49670, 270)
    SetChrPos(0x103, -49020, 0, -49670, 270)
    SetChrPos(0x105, -49020, 0, -49670, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(808, 0, 80, 0)
    Sleep(300)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x16, 0x2)
    SetChrSubChip(0x9, 0x1)

    ChrTalk(
        0x16,
        "#6PAh, is it visiting hours?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please come in\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6PExcuse us\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-54130, 1000, -49290, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(20740, 3000)

    def lambda_D166():
        OP_95(0x101, -53180, 0, -49830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D166)

    def lambda_D180():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D180)
    Sleep(500)

    def lambda_D194():
        OP_95(0x105, -53100, 0, -50830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D194)

    def lambda_D1AE():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D1AE)
    Sleep(600)

    def lambda_D1C2():
        OP_95(0x103, -51840, 50, -50110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D1C2)

    def lambda_D1DC():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D1DC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x10E, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x10E, 0x1F4)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x4, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh, you guys …\x01",
            "Is not it a support department!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PHaha, it's been a long time.\x01",
            "Donovan police station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10405F#12POh and who is that beauty there?\x02\x03",
            "#10409FHuh, maybe\x01",
            "I guess I bothered you for the banquet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "As soon as we meet again,\x01",
            "What are you going to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PWazy, come on\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#2PThis is the wife's wife's\x01",
            "I'm Farra.\x02\x03",
            "Since I came to visit you a while ago\x01",
            "I am staying for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PHave started.\x01",
            "My husband always takes care of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PFrom my husband or Tio\x01",
            "Sometimes I was listening to the story,\x01",
            "They seem like very interesting people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHa, we're honored to have been praised \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P(Probably praising you\x01",
            "I do not think so …).)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, there will be stories to pile up ….\x01",
            "Could you explain circumstances once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes, understood\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x18, -56080, 0, -50980, 0)
    SetChrPos(0x16, -57180, 0, -49690, 90)
    SetChrPos(0x101, -56170, 0, -50280, 0)
    SetChrPos(0x105, -54970, 0, -50480, 0)
    SetChrPos(0x103, -54150, 0, -49250, 315)
    OP_68(-55150, 1000, -48820, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#1PHmm … more than I thought\x01",
            "A serious thing will not happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PBesides, as long as I heard it.\x01",
            "Also in the headquarters I met here\x01",
            "Should not you not report it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYes, that would help us a lot\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, I do not care either way\x01",
            "Lloyd would have been wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6PAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PAnd anyway.\x01",
            "…… Guard, Crossbell in the city\x01",
            "How is the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1POh, I came to visit\x01",
            "I just heard from Raymond … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PCrossbell Police,\x01",
            "As a subordinate to the Defense Forces\x01",
            "It seems that it was completely taken in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PThe work content has not changed,\x01",
            "Now for the miscellaneous use in the city\x01",
            "She seems to be running around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FAs we thought…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, considering the current situation\x01",
            "I guess it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PBut … such a system,\x01",
            "Indeed there was a rebound?\x02\x03",
            "#00003FRegardless of Deputy Director Pierre,\x01",
            "Sergey manager and Mr. Dudley\x01",
            "It is said that you are silent and obeying … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PKeep this to yourselves but\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PApparently Sergei and Dudley,\x01",
            "Policemen including Raymond\x01",
            "She seems to move secretly.\x02",
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
        0x103,
        "#00205FThe Director too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PIt's just getting started though\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWhile watching the aircraft,\x01",
            "A way to overcome the current situation somehow\x01",
            "I wonder what he is looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PEveryone is still silent\x01",
            "Is not that it is not a tama?\x02\x03",
            "#10404FAh, I wonder if we have some hope\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12POh, for now so far\x01",
            "It seems to be difficult to take ….\x01",
            "You are likely to leave those in the city.\x02\x03",
            "#00003FWe, we,\x01",
            "The technique to overcome the current situation\x01",
            "You'd better explore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PThat's what you guys are for\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PActually it will be pretty tough,\x01",
            "Try somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1POnce I get back, even soon\x01",
            "Merging with Sergei … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PWell, you guys ……\x01",
            "Now let them and Raymond you guys,\x01",
            "Cure your body slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PUntil I completely recovered, I absolutely\x01",
            "Is not it impossible?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1PR-right, got it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P(my mother……\x01",
            "Did you say what you want to say? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(The policeman also to this wife\x01",
            "I do not think my head will rise. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12P(Huh, I am blessed with a good wife\x01",
            "The policemen are also happy people. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    SetChrPos(0x16, -55700, 100, -49800, 0)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrSubChip(0x9, 0x0)
    OP_74(0x4, 0x1E)
    SetChrPos(0x0, -53970, 0, -49930, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 0)
    EventEnd(0x5)
    Return()

    # Function_62_CFF3 end

    def Function_63_DE5D(): pass

    label("Function_63_DE5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-16120, 1000, 8160, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21280, 0)
    SetChrPos(0x101, -19090, 0, 8790, 90)
    SetChrPos(0x103, -19090, 0, 8790, 90)
    SetChrPos(0x105, -19090, 0, 8790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x15)
    SetChrPos(0x8, -840, 0, 9000, 270)
    OP_4B(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_68(-14770, 1000, 8790, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(19350, 5000)

    def lambda_DF4A():
        OP_95(0x101, -15360, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF4A)

    def lambda_DF64():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DF64)
    Sleep(600)

    def lambda_DF78():
        OP_95(0x103, -14800, 0, 7940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DF78)

    def lambda_DF92():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF92)
    Sleep(600)

    def lambda_DFA6():
        OP_95(0x105, -14980, 0, 10240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFA6)

    def lambda_DFC0():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DFC0)
    Sleep(1200)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0x8,
        "Oh, what do you think?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_E036():

        label("loc_E036")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E036")

    QueueWorkItem2(0x101, 2, lambda_E036)

    def lambda_E048():

        label("loc_E048")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E048")

    QueueWorkItem2(0x105, 2, lambda_E048)

    def lambda_E05A():

        label("loc_E05A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E05A")

    QueueWorkItem2(0x103, 2, lambda_E05A)
    OP_95(0x8, -13480, 0, 9000, 3000, 0x0)
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, Fran …\x01",
            "Did you finish gathering your luggage?\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        "Yes, as you can see\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    OP_93(0x8, 0x1E, 0x1F4)
    OP_93(0x8, 0x96, 0x1F4)
    OP_93(0x8, 0x10E, 0x1F4)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#00202F#6PFuran's uniform appearance also\x01",
            "Long time, no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01909F#11PHuhu, I am also ~.\x02\x03",
            "#01900FEveryone is a Donovan\x01",
            "Did you see him in law?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYes. We just finished\x02\x03",
            "#00000FDid you come to see him too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01904F#11PYes, before I leave the hospital\x01",
            "Let's greet us all\x01",
            "I thought.\x02\x03",
            "#01902FEspecially for the police department a dangerous place\x01",
            "I had you help me,\x01",
            "I have to thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha, that's right.\x01",
            "Well then again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01909F#11PYes, I will come back later ~!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    OP_68(-14920, 1000, 8940, 3000)
    BeginChrThread(0x105, 1, 0, 64)
    BeginChrThread(0x101, 1, 0, 65)
    Sleep(500)
    BeginChrThread(0x1A, 1, 0, 66)
    OP_95(0x8, -18060, 0, 8900, 2500, 0x1)

    def lambda_E3BA():
        OP_95(0xFE, -19090, 0, 8900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E3BA)

    def lambda_E3D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E3D4)
    WaitChrThread(0x8, 2)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_E400():
        OP_95(0xFE, -16200, 0, 8800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E400)
    Sleep(50)

    def lambda_E41D():
        OP_95(0xFE, -14800, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E41D)
    Sleep(50)

    def lambda_E43A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E43A)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    SetScenarioFlags(0x1A1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_END)), "loc_E4DC")

    ChrTalk(
        0x105,
        (
            "#10402F#5PWell, when her greeting ends\x01",
            "Shall I return to Mercapa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, right\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_E580")

    label("loc_E4DC")


    ChrTalk(
        0x105,
        (
            "#10402F#5PWell then, we are\x01",
            "Iria's person's\x01",
            "Shall I go visit you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, right\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1000)
    SetChrPos(0x0, -15000, 0, 9000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_E580")

    Return()

    # Function_63_DE5D end

    def Function_64_E581(): pass

    label("Function_64_E581")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xE1, 0x320, 0x3E8, 0x0)

    def lambda_E59C():

        label("loc_E59C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E59C")

    QueueWorkItem2(0xFE, 2, lambda_E59C)
    Return()

    # Function_64_E581 end

    def Function_65_E5AA(): pass

    label("Function_65_E5AA")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xA0, 0x5DC, 0x3E8, 0x0)

    def lambda_E5C5():

        label("loc_E5C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E5C5")

    QueueWorkItem2(0xFE, 2, lambda_E5C5)
    Return()

    # Function_65_E5AA end

    def Function_66_E5D3(): pass

    label("Function_66_E5D3")

    Sleep(1850)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    Return()

    # Function_66_E5D3 end

    def Function_67_E5E6(): pass

    label("Function_67_E5E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -99220, 0, 55110, 315)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99820, 0, 55990, 135)
    SetChrFlags(0xD, 0x8000)
    SetChrSubChip(0xD, 0x2)
    OP_68(-99000, 1000, 56020, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, -100000, 50, 48000, 0)
    SetChrPos(0x102, -100000, 50, 48000, 0)
    SetChrPos(0x103, -100000, 50, 48000, 0)
    SetChrPos(0x104, -100000, 50, 48000, 0)
    SetChrPos(0x109, -100000, 50, 48000, 0)
    SetChrPos(0x105, -100000, 50, 48000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#01400F…… Sergei, the matter of \"Phantom Beast\"\x01",
            "It seems that he took over.\x02\x03",
            "#01403FOriginally I also as a hackpot,\x01",
            "I should go to the investigation and extermination … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01000FThere is no need for you to be sick.\x02\x03",
            "#01003FRegarding the eidolon, share it\x01",
            "I have a way to respond.\x02\x03",
            "#01000FWell, for today\x01",
            "You should leave it to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01408Fbut……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01002FWell, they are also growing up,\x01",
            "There is nothing to worry about so far.\x02\x03",
            "#01004FBesides, it is usually quite\x01",
            "You probably can not come to visit.\x02\x03",
            "#01002FAbout this time\x01",
            "I want to be by my daughter\x01",
            "It is my honor to serve you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01403F…… I will wear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11209FWhatching\x01",
            "Thank you, the section chief.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 160, -1, -1)
    SetChrName("Voice of Lloyd")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Excuse us\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_EA1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_EA1B)
    Sleep(50)
    OP_93(0x19, 0xB4, 0x1F4)
    OP_68(-98690, 1100, 54300, 4000)
    MoveCamera(40, 15, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(20840, 4000)
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 71)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 73)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0xF,
        "#01405Fyou……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#01005FWhat, did you come?\x02\x03",
            "#01006FBecause it is busy to go\x01",
            "I'm gonna get on my own.\x01",
            "I told you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FWell, sorry, the section chief.\x02\x03",
            "#00000FAbsolutely\x01",
            "The state of Shizuoka\x01",
            "I am concerned ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FHuhu, everyone ……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FShizuku-chan, your eyes are open ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FThat, maybe,\x01",
            "Are you seeing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P#11208F…… No, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F…… In this surgery,\x01",
            "Dr. Seyland as a surgeon\x01",
            "He did his best.\x02\x03",
            "#01400FThe operation succeeded for the time being … …\x01",
            "I have not arrived until the cure.\x02\x03",
            "#01408FTo the extent that ambient light can be felt\x01",
            "It seems he was able to recover at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FWhat can I say ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11200FHehe, do not mind.\x01",
            "Because I am fine.\x02\x03",
            "#11202FBetter than that … …\x01",
            "I, I want to go to the rooftop together.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)

    ChrTalk(
        0x19,
        (
            "#6P#01002FOh, it might be nice.\x02\x03",
            "#01004FThere are so many people in the hospital room\x01",
            "What is gathering up,\x01",
            "I want to suck fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FBut, Shizuoka,\x01",
            "I have not had a surgery\x01",
            "It is better not to impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F… No, according to a doctor\x01",
            "I have to expose it to intense light for a long time\x01",
            "There seems to be no adverse effect to that extent.\x02\x03",
            "#01400FIf the weather is about today,\x01",
            "There should be no problem with going out a little.\x02\x03",
            "#01403F… … I get permission.\x01",
            "Sorry but preparation for Shizuku\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F044():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F044)

    def lambda_F05E():

        label("loc_F05E")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F05E")

    QueueWorkItem2(0x19, 2, lambda_F05E)

    def lambda_F070():

        label("loc_F070")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F070")

    QueueWorkItem2(0x101, 2, lambda_F070)

    def lambda_F082():

        label("loc_F082")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F082")

    QueueWorkItem2(0x102, 2, lambda_F082)

    def lambda_F094():

        label("loc_F094")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F094")

    QueueWorkItem2(0x103, 2, lambda_F094)

    def lambda_F0A6():

        label("loc_F0A6")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0A6")

    QueueWorkItem2(0x104, 2, lambda_F0A6)

    def lambda_F0B8():

        label("loc_F0B8")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0B8")

    QueueWorkItem2(0x109, 2, lambda_F0B8)

    def lambda_F0CA():

        label("loc_F0CA")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0CA")

    QueueWorkItem2(0x105, 2, lambda_F0CA)
    BeginChrThread(0x1A, 1, 0, 74)
    WaitChrThread(0xF, 1)

    def lambda_F0E6():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F0E6)

    def lambda_F100():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_F100)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xF, 2)
    SetChrFlags(0xF, 0x80)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)

    ChrTalk(
        0x102,
        "#00105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, that \"Wind sword of the wind\" also\x01",
            "It seems to be sweeter to my daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11209FDad from usual\x01",
            "I am very gentle.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F1D4():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F1D4)
    Sleep(50)

    def lambda_F1E4():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F1E4)
    Sleep(50)

    def lambda_F1F4():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F1F4)
    Sleep(50)

    def lambda_F204():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F204)
    Sleep(50)

    def lambda_F214():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F214)
    Sleep(50)

    def lambda_F224():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F224)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    TurnDirection(0x19, 0x101, 500)

    ChrTalk(
        0x19,
        (
            "#01004FWell, if that's the case\x01",
            "Would you mind going out with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, you are right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P#11202FHehe, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_67_E5E6 end

    def Function_68_F2F0(): pass

    label("Function_68_F2F0")


    def lambda_F2F5():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2F5)

    def lambda_F30F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F30F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F328():
        OP_95(0xFE, -99000, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_68_F2F0 end

    def Function_69_F349(): pass

    label("Function_69_F349")


    def lambda_F34E():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F34E)

    def lambda_F368():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F368)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F381():
        OP_95(0xFE, -100940, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F381)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_69_F349 end

    def Function_70_F3A2(): pass

    label("Function_70_F3A2")


    def lambda_F3A7():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3A7)

    def lambda_F3C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F3C1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F3DA():
        OP_95(0xFE, -98340, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3DA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_F3A2 end

    def Function_71_F3FB(): pass

    label("Function_71_F3FB")


    def lambda_F400():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F400)

    def lambda_F41A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F41A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F433():
        OP_95(0xFE, -100740, 0, 51800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F433)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_71_F3FB end

    def Function_72_F454(): pass

    label("Function_72_F454")


    def lambda_F459():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F459)

    def lambda_F473():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F473)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F48C():
        OP_95(0xFE, -99240, 0, 50800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F48C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_F454 end

    def Function_73_F4AD(): pass

    label("Function_73_F4AD")


    def lambda_F4B2():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4B2)

    def lambda_F4CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F4CC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F4E5():
        OP_95(0xFE, -100740, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4E5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_73_F4AD end

    def Function_74_F506(): pass

    label("Function_74_F506")

    Sleep(2600)
    Sound(107, 0, 100, 0)
    Sleep(1100)
    Sound(107, 0, 100, 0)
    Return()

    # Function_74_F506 end

    def Function_75_F519(): pass

    label("Function_75_F519")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -99220, 0, 55110, 315)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99820, 0, 55990, 135)
    SetChrFlags(0xD, 0x8000)
    OP_68(-98690, 1100, 54300, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x101, -99000, 50, 53000, 0)
    SetChrPos(0x102, -100940, 50, 53000, 45)
    SetChrPos(0x103, -100740, 0, 51800, 45)
    SetChrPos(0x104, -98340, 0, 52200, 0)
    SetChrPos(0x109, -100740, 0, 50600, 0)
    SetChrPos(0x105, -99240, 0, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#12P#01002F… Well then,\x01",
            "Let me return to the support department soon\x01",
            "Let's get it.\x02\x03",
            "#01004FArios, today tightly\x01",
            "Keep me by your side Shizuoka.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01403F…… Yes, I will do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FGood job, the section chief.\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "#01005FOh, you guys continue,\x01",
            "Advance the investigation of \"Phantom beast\".\x02\x03",
            "#01002FBefore the \"sword of the wind\" moved\x01",
            "You got a record of accomplishment at the most.\x02",
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
        0x102,
        "#6P#00106FOr the section chief …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#01004FWell, then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    ChrTalk(
        0xD,
        (
            "#5P#11202FAh……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)
    Sleep(500)
    OP_93(0x19, 0xB4, 0x1F4)

    def lambda_F8AB():
        OP_95(0xFE, -99820, 0, 54000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F8AB)
    WaitChrThread(0x19, 1)

    def lambda_F8C9():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F8C9)

    def lambda_F8E3():

        label("loc_F8E3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F8E3")

    QueueWorkItem2(0xF, 2, lambda_F8E3)

    def lambda_F8F5():

        label("loc_F8F5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F8F5")

    QueueWorkItem2(0x101, 2, lambda_F8F5)

    def lambda_F907():

        label("loc_F907")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F907")

    QueueWorkItem2(0x102, 2, lambda_F907)

    def lambda_F919():

        label("loc_F919")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F919")

    QueueWorkItem2(0x103, 2, lambda_F919)

    def lambda_F92B():

        label("loc_F92B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F92B")

    QueueWorkItem2(0x104, 2, lambda_F92B)

    def lambda_F93D():

        label("loc_F93D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F93D")

    QueueWorkItem2(0x109, 2, lambda_F93D)

    def lambda_F94F():

        label("loc_F94F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F94F")

    QueueWorkItem2(0x105, 2, lambda_F94F)
    Sleep(1500)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_F96E():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F96E)

    def lambda_F988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F988)
    Sleep(100)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)
    WaitChrThread(0x19, 2)
    SetChrFlags(0x19, 0x80)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)

    ChrTalk(
        0x104,
        (
            "#5P#00306FWhew, the true \"sword of the wind\"\x01",
            "The thing I say before my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHuh, it's as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01402FHuh, since my police era\x01",
            "Being an excellent boss\x01",
            "There is no doubt.\x02\x03",
            "#01403F…… As for the investigation of \"Phantom beast\"\x01",
            "I also ask you from my side.\x02\x03",
            "#01400FI will also be back tomorrow\x01",
            "I plan to join, until then\x01",
            "Please help Scott.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB23():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FB23)
    Sleep(50)

    def lambda_FB33():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FB33)
    Sleep(50)

    def lambda_FB43():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FB43)
    Sleep(50)

    def lambda_FB53():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FB53)
    Sleep(50)

    def lambda_FB63():
        TurnDirection(0x105, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FB63)
    Sleep(50)

    def lambda_FB73():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FB73)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x103,
        "#12P#00200FYes, we will do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FEveryone really\x01",
            "Thank you very much.\x02\x03",
            "#11209FI am glad that we could talk about various things.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC1F():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FC1F)
    Sleep(50)

    def lambda_FC2F():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FC2F)
    Sleep(50)

    def lambda_FC3F():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FC3F)
    Sleep(50)

    def lambda_FC4F():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FC4F)
    Sleep(50)

    def lambda_FC5F():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FC5F)
    Sleep(50)

    def lambda_FC6F():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FC6F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#12P#10100FNo, we were also very happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FI will come again, so please be fine.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x170, 3)
    SetChrPos(0xF, -99220, 0, 56180, 90)
    OP_4C(0xF, 0xFF)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -100000, 50, 53000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_75_F519 end

    def Function_76_FD4C(): pass

    label("Function_76_FD4C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-99000, 900, 55030, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100000, 50, 48000, 0)
    SetChrPos(0x102, -100000, 50, 48000, 0)
    SetChrPos(0x103, -100000, 50, 48000, 0)
    SetChrPos(0x104, -100000, 50, 48000, 0)
    SetChrPos(0x109, -100000, 50, 48000, 0)
    SetChrPos(0x105, -100000, 50, 48000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 71)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 73)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        (
            "#00005FWell, here is Shizuku's\x01",
            "It's a hospital in the hospital room ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FPerhaps it is going out now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FBut in this ward\x01",
            "I did not see it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FWell, why do not you try looking if you feel like it?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18E, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -100000, 50, 52410, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_76_FD4C end

    def Function_77_FF93(): pass

    label("Function_77_FF93")

    StopBGM(0xBB8)

    ChrTalk(
        0xB,
        "#11603FBy the way, ───\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#11602F…… Someone there\x01",
            "You still do not feel that way?\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Fade(500)
    EventBegin(0x0)
    OP_68(-98780, 1000, -4030, 0)
    MoveCamera(71, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -99960, 0, -5580, 90)
    SetChrPos(0x102, -99960, 0, -6900, 90)
    SetChrPos(0x103, -100870, 0, -5000, 90)
    SetChrPos(0x104, -100870, 0, -6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10145")
    SetChrPos(0x109, -100670, 0, -7660, 90)
    Jump("loc_1018C")

    label("loc_10145")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1016B")
    SetChrPos(0x105, -100670, 0, -7660, 90)
    Jump("loc_1018C")

    label("loc_1016B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1018C")
    SetChrPos(0x10A, -100670, 0, -7660, 90)

    label("loc_1018C")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00005FAh, Iria … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhat on earth ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11604FHuh, I do not know who it is#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "It sounds much shy.\x02\x03",
            "#11609FPerhaps, for discreet personality\x01",
            "Self-care in a selfish body\x01",
            "I wonder what the owner is, but\x02",
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
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#00306F(This is …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206F(It is perfectly noticed.)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Lisha")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10708F#3C#40W#2S…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#11603F── I do not know who it is\x01",
            "I am already rehabilitating.\x02\x03",
            "#11601FIf you really skip training\x01",
            "Catch it quickly and pull apart?\x02\x03",
            "#11604FIf you do not want to leave it\x01",
            "Let's finish the rush at last.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Lisha")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10717F#3C#40W#2S…………… Uh …………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#11604FAnd be careful again.\x02\x03",
            "#11600FRegardless of how strong it is,\x01",
            "Please be conscious of yourself being a woman.\x02\x03",
            "#11603FOur stage#5Rstage#As well,\x01",
            "There are strengths that can only be shown to women ……\x02\x03",
            "#11600FIt surely will protect you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Lisha")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10715F#3C#40W#2S…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00102FIlia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#11604FHuh, I let you take extra effort.\x02\x03",
            "#11600F── Your brother and you also take care.\x01",
            "Do not make Cecil sorrowful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F……Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FOK!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_68(-14240, 1000, 29970, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20470, 0)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x2, 3)
    OP_49()
    SetChrPos(0x106, -12930, 0, 29900, 90)
    BeginChrThread(0x106, 1, 0, 78)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 79)
    WaitChrThread(0x101, 1)
    Sleep(600)
    BeginChrThread(0x102, 1, 0, 79)
    WaitChrThread(0x102, 1)
    Sleep(600)
    BeginChrThread(0x103, 1, 0, 79)
    WaitChrThread(0x103, 1)
    Sleep(600)
    BeginChrThread(0x104, 1, 0, 79)
    WaitChrThread(0x104, 1)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1082A")
    BeginChrThread(0x109, 1, 0, 79)
    WaitChrThread(0x109, 1)
    Jump("loc_10863")

    label("loc_1082A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10849")
    BeginChrThread(0x105, 1, 0, 79)
    WaitChrThread(0x105, 1)
    Jump("loc_10863")

    label("loc_10849")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10863")
    BeginChrThread(0x10A, 1, 0, 79)
    WaitChrThread(0x10A, 1)

    label("loc_10863")

    Sleep(2500)
    EndChrThread(0x106, 0x1)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0x106,
        "#10715F#40W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThat … … sorry.\x02\x03",
            "#00008FNot to be noticed\x01",
            "I did not think so …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FLisa-chan, you can feel sick\x01",
            "I wish I was erasing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#30WWhatching\x01",
            "Because Ilia is a genius … …\x02\x03",
            "#10704F#30WProbably, with slight breathing and footsteps\x01",
            "I think I understood it soon ……\x02\x03",
            "When matching breathing on the stage\x01",
            "It is what I always do ……\x02\x03",
            "#10716F#30WReally … … If it's something other than the stage\x01",
            "Even though it is a pain in a bothersome room … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204Ftruly……\x01",
            "Iria is Iria, is not he?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AC8")

    ChrTalk(
        0x109,
        (
            "#6P#10109FGrueling\x01",
            "But … it was good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B5B")

    label("loc_10AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B14")

    ChrTalk(
        0x105,
        (
            "#6P#10409FGiggle\x01",
            "It is amazing for her to keep on standing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B5B")

    label("loc_10B14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B5B")

    ChrTalk(
        0x10A,
        (
            "#6P#00602FHydrofluoric acid\x01",
            "Should I call it Miss Yuria?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B5B")

    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    OP_93(0x106, 0x10E, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10704FWith this\x01",
            "My resolution also solidified.\x02\x03",
            "#10702FLet's go, everyone …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYeah … …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AD, 0)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    BeginChrThread(0x1A, 1, 0, 85)
    SetChrPos(0x0, -16360, 0, 29440, 0)
    EventEnd(0x5)
    TalkEnd(0xFE)
    Return()

    # Function_77_FF93 end

    def Function_78_10C49(): pass

    label("Function_78_10C49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C85")
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(500)
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(800)
    Jump("Function_78_10C49")

    label("loc_10C85")

    Return()

    # Function_78_10C49 end

    def Function_79_10C86(): pass

    label("Function_79_10C86")

    SetChrPos(0xFE, -16470, 0, 25770, 0)

    def lambda_10C9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10C9C)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CCC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 80)
    Jump("loc_10D57")

    label("loc_10CCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CF0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 81)
    Jump("loc_10D57")

    label("loc_10CF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D14")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 82)
    Jump("loc_10D57")

    label("loc_10D14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D38")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 83)
    Jump("loc_10D57")

    label("loc_10D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D57")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 84)

    label("loc_10D57")

    Return()

    # Function_79_10C86 end

    def Function_80_10D58(): pass

    label("Function_80_10D58")

    OP_95(0xFE, -16340, 0, 28470, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 29900, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_80_10D58 end

    def Function_81_10D88(): pass

    label("Function_81_10D88")

    OP_95(0xFE, -16360, 0, 29870, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 31030, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_81_10D88 end

    def Function_82_10DB8(): pass

    label("Function_82_10DB8")

    OP_95(0xFE, -16400, 0, 27970, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 28800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_82_10DB8 end

    def Function_83_10DE8(): pass

    label("Function_83_10DE8")

    OP_95(0xFE, -16360, 0, 30550, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_83_10DE8 end

    def Function_84_10E04(): pass

    label("Function_84_10E04")

    OP_95(0xFE, -16360, 0, 29320, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_84_10E04 end

    def Function_85_10E20(): pass

    label("Function_85_10E20")

    StopBGM(0x7D0)
    Sleep(2000)
    Sleep(10)
    PlayBGM("ed7563", 0)
    Return()

    # Function_85_10E20 end

    def Function_86_10E30(): pass

    label("Function_86_10E30")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xB, 0x2)
    OP_68(-98530, 900, -5100, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_10F32")
    SetChrPos(0x101, -99960, 0, -5280, 90)
    SetChrPos(0x102, -99960, 0, -6600, 90)
    SetChrPos(0x103, -100870, 0, -4700, 90)
    SetChrPos(0x104, -100870, 0, -6000, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EDC")
    SetChrPos(0x109, -100670, 0, -7360, 90)
    Jump("loc_10F23")

    label("loc_10EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F02")
    SetChrPos(0x105, -100670, 0, -7360, 90)
    Jump("loc_10F23")

    label("loc_10F02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F23")
    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_10F23")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_110AF")

    label("loc_10F32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -99960, 0, -6000, 90)
    SetChrPos(0x102, -99960, 0, -4700, 90)
    SetChrPos(0x103, -99960, 0, -7360, 90)
    SetChrPos(0x104, -100870, 0, -4700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FAB")
    SetChrPos(0x109, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FFB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FEA")
    SetChrPos(0x105, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10FFB")

    label("loc_10FEA")

    SetChrPos(0x105, -100670, 0, -7360, 90)

    label("loc_10FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1104B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1103A")
    SetChrPos(0x106, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1104B")

    label("loc_1103A")

    SetChrPos(0x106, -100670, 0, -7360, 90)

    label("loc_1104B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1109B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108A")
    SetChrPos(0x10A, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1109B")

    label("loc_1108A")

    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_1109B")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_110AF")

    OP_0D()

    ChrTalk(
        0xB,
        (
            "#11P#11600FYes, my younger brother …\x01",
            "Will you take this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '舞姬的发饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('舞姬的发饰', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000Fthis is……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11600FI for the first time\x01",
            "When I stood on the stage as a protagonist\x01",
            "I was wearing hair accessories.\x02\x03",
            "#11604FDo not forget your prayers\x01",
            "You had to keep your skin clean, were not you?\x02\x03",
            "#11609FHuff, mania beating\x01",
            "Do not you think it is a rare dish?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B0")
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_112B0")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(Certainly, no matter how much money he places\x01",
            "There seems to be someone who wants to be … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut,\x01",
            "Such an important thing\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11604FHuh, that's fine.\x01",
            "Because I thank you so far.\x02\x03",
            "#11600FAs a good luck charm\x01",
            "Take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00002F……Thank you.\x01",
            "I will take care of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_1141B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_1142F")

    label("loc_1141B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1142F")

    SetChrPos(0x0, -100140, 0, -6120, 90)
    SetScenarioFlags(0x1AD, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1145F")
    OP_E0(0x34, 0x0)

    label("loc_1145F")

    EventEnd(0x5)
    Return()

    # Function_86_10E30 end

    def Function_87_11462(): pass

    label("Function_87_11462")

    EventBegin(0x1)
    Call(0, 92)
    SetChrPos(0x0, -13440, 0, 8760, 89)
    EventEnd(0x4)
    Return()

    # Function_87_11462 end

    def Function_88_1147B(): pass

    label("Function_88_1147B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1148F")
    Call(0, 92)
    Jump("loc_11492")

    label("loc_1148F")

    Call(0, 94)

    label("loc_11492")

    SetChrPos(0x0, -9210, 0, 13390, 180)
    EventEnd(0x4)
    Return()

    # Function_88_1147B end

    def Function_89_114A6(): pass

    label("Function_89_114A6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114BA")
    Call(0, 94)
    Jump("loc_114BD")

    label("loc_114BA")

    Call(0, 93)

    label("loc_114BD")

    SetChrPos(0x0, 1350, 0, 80, 89)
    EventEnd(0x4)
    Return()

    # Function_89_114A6 end

    def Function_90_114D1(): pass

    label("Function_90_114D1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114E5")
    Call(0, 94)
    Jump("loc_114E8")

    label("loc_114E5")

    Call(0, 93)

    label("loc_114E8")

    SetChrPos(0x0, -5500, 0, 12500, 225)
    EventEnd(0x4)
    Return()

    # Function_90_114D1 end

    def Function_91_114FC(): pass

    label("Function_91_114FC")

    EventBegin(0x1)
    Call(0, 93)
    SetChrPos(0x0, -19350, 0, 29820, 89)
    EventEnd(0x4)
    Return()

    # Function_91_114FC end

    def Function_92_11515(): pass

    label("Function_92_11515")


    ChrTalk(
        0x101,
        (
            "#00000FFran's room was room 301.\x01",
            "Let's go to see the situation as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_92_11515 end

    def Function_93_11563(): pass

    label("Function_93_11563")


    ChrTalk(
        0x136,
        (
            "#01300FIlla's room is room 303.\x02\x03",
            "I think that I can not take much time,\x01",
            "I wonder if you can get me right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FThat's right, I agree.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_93_11563 end

    def Function_94_115F6(): pass

    label("Function_94_115F6")


    ChrTalk(
        0x136,
        (
            "#01300FDonovan's room is in Room 302.\x02\x03",
            "I think that I can not take much time,\x01",
            "I wonder if you can get me right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThat's right, I agree.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_94_115F6 end

    SaveToFile()

Try(main)
