from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Fran",                   # 1
        "Inspector Donovan",      # 2
        "Detective Raymond",      # 3
        "Ilya",                   # 4
        "Sully",                  # 5
        "Shizuku",                # 6
        "Mihail",                 # 7
        "Arios",                  # 8
        "Janitor Dyson",          # 9
        "Cecil",                  # 10
        "Nurse Xilun",            # 11
        "Nurse Meihua",           # 12
        "Doctor Belldine",        # 13
        "Archduke Albert",        # 14
        "Mrs. Fara",              # 15
        "Professor Seiland",      # 16
        "丸椅子",                 # 17
        "Sergei",                 # 18
        "SE制御",                 # 19
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
        "Function_13_1B2C",        # 0D, 13
        "Function_14_1CB3",        # 0E, 14
        "Function_15_1D80",        # 0F, 15
        "Function_16_1EB2",        # 10, 16
        "Function_17_1F66",        # 11, 17
        "Function_18_20A5",        # 12, 18
        "Function_19_29C3",        # 13, 19
        "Function_20_2D3A",        # 14, 20
        "Function_21_3478",        # 15, 21
        "Function_22_3BD5",        # 16, 22
        "Function_23_3D9C",        # 17, 23
        "Function_24_511C",        # 18, 24
        "Function_25_5297",        # 19, 25
        "Function_26_5603",        # 1A, 26
        "Function_27_640D",        # 1B, 27
        "Function_28_6878",        # 1C, 28
        "Function_29_6F0B",        # 1D, 29
        "Function_30_7262",        # 1E, 30
        "Function_31_739D",        # 1F, 31
        "Function_32_74B7",        # 20, 32
        "Function_33_797C",        # 21, 33
        "Function_34_7A5A",        # 22, 34
        "Function_35_7BDF",        # 23, 35
        "Function_36_81F4",        # 24, 36
        "Function_37_8AB0",        # 25, 37
        "Function_38_8AB7",        # 26, 38
        "Function_39_8CDE",        # 27, 39
        "Function_40_8D46",        # 28, 40
        "Function_41_A13C",        # 29, 41
        "Function_42_A171",        # 2A, 42
        "Function_43_A197",        # 2B, 43
        "Function_44_A1C3",        # 2C, 44
        "Function_45_A1E9",        # 2D, 45
        "Function_46_A21E",        # 2E, 46
        "Function_47_A244",        # 2F, 47
        "Function_48_AC58",        # 30, 48
        "Function_49_AC62",        # 31, 49
        "Function_50_C626",        # 32, 50
        "Function_51_C645",        # 33, 51
        "Function_52_C655",        # 34, 52
        "Function_53_C66A",        # 35, 53
        "Function_54_C686",        # 36, 54
        "Function_55_C6A2",        # 37, 55
        "Function_56_C6BE",        # 38, 56
        "Function_57_C6DA",        # 39, 57
        "Function_58_C6F6",        # 3A, 58
        "Function_59_C712",        # 3B, 59
        "Function_60_C75E",        # 3C, 60
        "Function_61_D652",        # 3D, 61
        "Function_62_DA3F",        # 3E, 62
        "Function_63_EA12",        # 3F, 63
        "Function_64_F145",        # 40, 64
        "Function_65_F16E",        # 41, 65
        "Function_66_F197",        # 42, 66
        "Function_67_F1AA",        # 43, 67
        "Function_68_FF7C",        # 44, 68
        "Function_69_FFD5",        # 45, 69
        "Function_70_1002E",       # 46, 70
        "Function_71_10087",       # 47, 71
        "Function_72_100E0",       # 48, 72
        "Function_73_10139",       # 49, 73
        "Function_74_10192",       # 4A, 74
        "Function_75_101A5",       # 4B, 75
        "Function_76_10A09",       # 4C, 76
        "Function_77_10C48",       # 4D, 77
        "Function_78_1193F",       # 4E, 78
        "Function_79_1197C",       # 4F, 79
        "Function_80_11A4E",       # 50, 80
        "Function_81_11A7E",       # 51, 81
        "Function_82_11AAE",       # 52, 82
        "Function_83_11ADE",       # 53, 83
        "Function_84_11AFA",       # 54, 84
        "Function_85_11B16",       # 55, 85
        "Function_86_11B26",       # 56, 86
        "Function_87_121BF",       # 57, 87
        "Function_88_121D8",       # 58, 88
        "Function_89_12203",       # 59, 89
        "Function_90_1222E",       # 5A, 90
        "Function_91_12259",       # 5B, 91
        "Function_92_12272",       # 5C, 92
        "Function_93_122BD",       # 5D, 93
        "Function_94_12350",       # 5E, 94
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
    Jump("loc_1B28")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1389")
    Call(0, 27)
    Jump("loc_1B28")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")
    Call(0, 27)
    Jump("loc_1B28")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_154E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151B")

    ChrTalk(
        0xD,
        (
            "#11205F...Oh, that's right...\x02\x03",
            "#11203FYesterday KeA came to\x01",
            "visit me, but...\x02\x03",
            "#11210FIt seems she felt really\x01",
            "depressed after hearing\x01",
            "about my surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah. Now that you mention\x01",
            "it, she did look down this\x01",
            "morning.\x02\x03",
            "#00000FBut don't worry. If you're\x01",
            "positive about it, Shizuku,\x01",
            "KeA will cheer up in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11200FYes... I hope so.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1549")

    label("loc_151B")


    ChrTalk(
        0xD,
        (
            "#11200FKeA... I hope she cheers\x01",
            "up soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1549")

    Jump("loc_1B28")

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_155F")
    Call(0, 13)
    Jump("loc_1B28")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1584")
    Call(0, 18)
    Jump("loc_1A78")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A0")
    Call(0, 17)
    Jump("loc_1A78")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(
        0xD,
        (
            "#01505F...Oh, come to think of\x01",
            "it...\x02\x03",
            "#01500FHas KeA been acting\x01",
            "strange today?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D8")
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
            "#1K◆KeA spacing out at the\x01",
            "Support Section? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",          # 0
            "[Talked to Her]\x01",      # 1
            "[Didn't]\x01",             # 2
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
        (0, "loc_16C3"),
        (1, "loc_16C8"),
        (2, "loc_16D0"),
        (SWITCH_DEFAULT, "loc_16D8"),
    )


    label("loc_16C3")

    Jump("loc_16D8")

    label("loc_16C8")

    SetScenarioFlags(0x151, 6)
    Jump("loc_16D8")

    label("loc_16D0")

    ClearScenarioFlags(0x151, 6)
    Jump("loc_16D8")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 6)), scpexpr(EXPR_END)), "loc_1786")

    ChrTalk(
        0x109,
        "#10105FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...Now that you mention\x01",
            "it, I felt like she was\x01",
            "spacing out earlier.\x02\x03",
            "#00001FDid something happen\x01",
            "during the unveiling\x01",
            "ceremony?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_1786")


    ChrTalk(
        0x109,
        (
            "#10105FHuh? It didn't seem like\x01",
            "that to me at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FDid something happen\x01",
            "during the unveiling\x01",
            "ceremony?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FE")


    ChrTalk(
        0xD,
        (
            "#01500FNo, I don't think it's\x01",
            "anything that important,\x01",
            "but...\x02\x03",
            "#01508FIt felt like KeA was somehow\x01",
            "dumbfounded when she watched\x01",
            "the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHmm, could she just have\x01",
            "been surprised by Orchis\x01",
            "Tower's massive size?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FAh... I guess that's\x01",
            "what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm. I don't really get\x01",
            "it, but I'll keep that\x01",
            "in mind.\x02\x03",
            "#00000FThanks, Shizuku. For\x01",
            "worrying about KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01500FNo, not at all... I'm\x01",
            "sorry, I said something\x01",
            "weird.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 2)
    Jump("loc_1A78")

    label("loc_19DB")


    ChrTalk(
        0xD,
        (
            "#01502FThanks to KeA, I had a lot\x01",
            "of fun at today's unveiling\x01",
            "ceremony.\x02\x03",
            "If I become able to see\x01",
            "someday, I want to go see\x01",
            "Orchis Tower again with KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A78")

    Jump("loc_1B1A")

    label("loc_1A7D")


    ChrTalk(
        0xD,
        (
            "#01502FThanks to KeA, I had a lot\x01",
            "of fun at today's unveiling\x01",
            "ceremony.\x02\x03",
            "If I become able to see\x01",
            "someday, I want to go see\x01",
            "Orchis Tower again with KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1A")

    Jump("loc_1B28")

    label("loc_1B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B28")

    label("loc_1B28")

    TalkEnd(0xD)
    Return()

    # Function_12_1367 end

    def Function_13_1B2C(): pass

    label("Function_13_1B2C")

    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1D")

    ChrTalk(
        0xD,
        (
            "#01502FMihail, they say you'll\x01",
            "be leaving the hospital\x01",
            "soon.\x02\x03",
            "Haha, congratulations.\x01",
            "Stay well always, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I will... Shizuku, thank\x01",
            "you for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll write you letters.\x01",
            "You stay well too,\x01",
            "Shizuku!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1CAE")

    label("loc_1C1D")


    ChrTalk(
        0xD,
        (
            "#01502FMihail, I'm very happy\x01",
            "you're being discharged.\x02\x03",
            "One day I'll come to\x01",
            "visit you in Lｳman with\x01",
            "my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sure! I'll be waiting.\x02",
    )

    CloseMessageWindow()

    label("loc_1CAE")

    OP_4C(0xE, 0xFF)
    Return()

    # Function_13_1B2C end

    def Function_14_1CB3(): pass

    label("Function_14_1CB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CC4")
    Jump("loc_1D7C")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CD5")
    Call(0, 13)
    Jump("loc_1D7C")

    label("loc_1CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CE6")
    Call(0, 29)
    Jump("loc_1D7C")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D01")
    Call(0, 34)
    Jump("loc_1D7C")

    label("loc_1D01")


    ChrTalk(
        0xE,
        (
            "Leaving the hospital...\x01",
            "To think this day would\x01",
            "really come...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I-I must contact my\x01",
            "parents in Lｳman\x01",
            "immediately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7C")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CB3 end

    def Function_15_1D80(): pass

    label("Function_15_1D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E1F")

    ChrTalk(
        0xF,
        (
            "#01400FI leave the Cryptids\x01",
            "investigation to you.\x02\x03",
            "I plan to return tomorrow and\x01",
            "join it, but until then, help\x01",
            "out Scott and the others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAE")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3B")
    Call(0, 18)
    Jump("loc_1EAE")

    label("loc_1E3B")


    ChrTalk(
        0xF,
        (
            "#01400FHis Excellency said he\x01",
            "wanted to meet Shizuku.\x02\x03",
            "#01403F...I welcomed it. I'll\x01",
            "have to thank him later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAE")

    TalkEnd(0xFE)
    Return()

    # Function_15_1D80 end

    def Function_16_1EB2(): pass

    label("Function_16_1EB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED1")
    Call(0, 18)
    Jump("loc_1F62")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE3")
    Call(0, 17)
    Jump("loc_1F62")

    label("loc_1EE3")


    ChrTalk(
        0x15,
        (
            "Oh that's right, I must\x01",
            "go see how Seiland is\x01",
            "doing later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's been a long time\x01",
            "since I saw her. I hope\x01",
            "she's well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F62")

    TalkEnd(0xFE)
    Return()

    # Function_16_1EB2 end

    def Function_17_1F66(): pass

    label("Function_17_1F66")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "Come to think of it, there's\x01",
            "something wrong with your\x01",
            "eyes, right Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...I'm sure you're worried, but\x01",
            "the skills of this hospital's\x01",
            "doctors are worthy of your trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It may take time, but\x01",
            "believe in your full\x01",
            "recovery and fight hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FTh... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x15, 0xFF)
    Return()

    # Function_17_1F66 end

    def Function_18_20A5(): pass

    label("Function_18_20A5")

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
        (
            "#01505FAh... The Support\x01",
            "Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh, you're...\x02",
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
            "#00005FArchduke Albert from the\x01",
            "Principality of\x01",
            "Remiferia!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAnd Arios too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403FHmm, what a coincidence.\x02\x03",
            "#01400FYour Excellency, they are the\x01",
            ""Special Support Section" I\x01",
            "told you about previously.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "Oh, so that's who they\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...How do you do, ladies\x01",
            "and gentlemen of the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I am Albert von\x01",
            "Bartholomeus. I serve as\x01",
            "Remiferia's Head of State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please do your very best\x01",
            "for Crossbell from now\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FP-Pleased to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I heard about you all\x01",
            "from Arios. I really\x01",
            "wanted to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Also, Elie, it's been a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it has. You\x01",
            "look well, Your Grace...\x02\x03",
            "#00103FHowever, I didn't know\x01",
            "you were visiting the\x01",
            "hospital.\x02\x03",
            "#00105FAre you here for an\x01",
            "inspection today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Yes. The Principality of\x01",
            "Remiferia is one of this\x01",
            "hospital's sponsors, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I also had to meet\x01",
            "Arios' daughter whom I\x01",
            "had heard so much about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01502FT-Thank you very much,\x01",
            "Archduke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01400FRegarding that, the Archduke\x01",
            "asked me to escort him\x01",
            "personally a while longer.\x02\x03",
            "#01403FI wonder if it's alright\x01",
            "with just the driver and I,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "Haha. It's because I\x01",
            "have such confidence in\x01",
            "you, Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "And, I can't exactly go disturbing\x01",
            "hospital operations with a swarm\x01",
            "of escorts, now can I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Archduke Albert... He\x01",
            "didn't know just Arios,\x01",
            "but Elie too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes. Elie, Arios... and it\x01",
            "looks like he's known Professor\x01",
            "Seiland for a long time.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hehe. He seems to be\x01",
            "more sociable than I\x01",
            "thought.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "At any rate, I'll be\x01",
            "rooting for you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Continue to do your\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYour Excellency, please be\x01",
            "careful when returning to\x01",
            "the city today.\x02\x03",
            "Likewise, we'll be rooting\x01",
            "for you at tomorrow's\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, I'll be sure to do\x01",
            "my best.\x02",
        )
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

    # Function_18_20A5 end

    def Function_19_29C3(): pass

    label("Function_19_29C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_2A4D")

    ChrTalk(
        0x8,
        (
            "#01900FI really can't thank the\x01",
            "Inspector enough for\x01",
            "saving me.\x02\x03",
            "#01909FI'll come visit again\x01",
            "when I find the time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B90")

    ChrTalk(
        0x8,
        (
            "#06400FUmm, notebook, ENIGMA,\x01",
            "toothbrush...\x02\x03",
            "#06405FAh, I have to finish\x01",
            "saying goodbye the other\x01",
            "patients and nurses too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(It seems that Fran's\x01",
            "preparations are going to\x01",
            "take a little longer...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F(Well, I think we should\x01",
            "finish visiting everyone\x01",
            "we want to as well.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C11")

    label("loc_2B90")


    ChrTalk(
        0x8,
        (
            "#06405FOh, I also must change\x01",
            "into my uniform...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "#06401F...Please don't peep,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I won't.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_2C11")

    Jump("loc_2D36")

    label("loc_2C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_END)), "loc_2D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1C")

    ChrTalk(
        0x8,
        "#11703Fzzz... zzz...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEF")

    ChrTalk(
        0x105,
        (
            "#10300FHehe. She's sound\x01",
            "asleep, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01302FIt's all right, Noｱl. At\x01",
            "this rate, she'll be\x01",
            "better soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FWe will... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2CEF")


    ChrTalk(
        0x109,
        "#10103F(Fran... Get well soon.)\x02",
    )

    CloseMessageWindow()

    label("loc_2D14")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2D36")

    label("loc_2D1C")


    ChrTalk(
        0x8,
        "#11703Fzzz... zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_2D36")

    TalkEnd(0xFE)
    Return()

    # Function_19_29C3 end

    def Function_20_2D3A(): pass

    label("Function_20_2D3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D58")
    Call(0, 21)
    Jump("loc_2E12")

    label("loc_2D58")


    ChrTalk(
        0x9,
        (
            "I'm going to rejoin the police now,\x01",
            "but... Well, I intend to do what I can\x01",
            "to help out, without overdoing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems things are\x01",
            "quite hard on your end,\x01",
            "so be very careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E12")

    Jump("loc_3474")

    label("loc_2E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F69")

    ChrTalk(
        0x9,
        (
            "A declaration of invalidity of\x01",
            "the independent state, huh...?\x01",
            "To think you'd go this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even Sergei and the others in the\x01",
            "city should be starting to act to\x01",
            "take advantage of this opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If things are like this, I won't\x01",
            "be able to join you for a while.\x01",
            "...I leave the rest to you, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_304B")

    label("loc_2F69")


    ChrTalk(
        0x9,
        (
            "I think you can assume Sergei and the\x01",
            "others in the city are starting to act\x01",
            "to take advantage of this opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If things are like this, I won't\x01",
            "be able to join you for a while.\x01",
            "...I leave the rest to you, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304B")

    Jump("loc_3474")

    label("loc_3050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_311B")

    ChrTalk(
        0x9,
        (
            "At any rate, it doesn't seem I'll be\x01",
            "able to rejoin the police anytime soon,\x01",
            "so I'll rest my body for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until then, Raymond,\x01",
            "Sergei and the others\x01",
            "will have do their best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3474")

    label("loc_311B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_31A8")

    ChrTalk(
        0x9,
        (
            "Haha, I'm safe and sound\x01",
            "too, so there's nothing\x01",
            "to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're still recovering\x01",
            "too, so be careful, got\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3474")

    label("loc_31A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C3")
    Call(0, 21)
    Jump("loc_3230")

    label("loc_31C3")


    ChrTalk(
        0x9,
        (
            "Well, in any case... Be\x01",
            "careful, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope I'll be able to\x01",
            "rejoin Sergei and the\x01",
            "others soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3230")

    Jump("loc_3474")

    label("loc_3235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345E")

    ChrTalk(
        0x9,
        "#90W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...When the Inspector regains\x01",
            "consciousness, I'll have to formally\x01",
            "thank him for protecting Fran.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3427")

    ChrTalk(
        0x136,
        (
            "#01303FBecause he suffered severe damage to\x01",
            "his respiratory system, his recovery\x01",
            "will probably take a long while...\x02\x03",
            "#01300FHowever, he's gotten through the\x01",
            "worst of it, so he should wake up\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI hope so...\x02\x03",
            "#00100F...It seems we can leave\x01",
            "the rest to Raymond, so\x01",
            "let's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3456")

    label("loc_3427")


    ChrTalk(
        0x101,
        (
            "#00003FRight... I hope he gets\x01",
            "well soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3456")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3474")

    label("loc_345E")


    ChrTalk(
        0x9,
        "#90W............\x02",
    )

    CloseMessageWindow()

    label("loc_3474")

    TalkEnd(0xFE)
    Return()

    # Function_20_2D3A end

    def Function_21_3478(): pass

    label("Function_21_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_380E")
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)

    def lambda_348E():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_348E)
    Sleep(0)

    def lambda_349E():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_349E)
    Sleep(0)

    def lambda_34AE():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_34AE)
    Sleep(0)

    def lambda_34BE():
        TurnDirection(0x3, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_34BE)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x16, 0x0, 0)

    ChrTalk(
        0x9,
        "Oh, you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Uhuhu, good day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FInspector Donovan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIs it okay for you be\x01",
            "out of bed already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, my discharge\x01",
            "papers were just\x01",
            "completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the operation to liberate\x01",
            "Crossbell City went well and I thought I'd\x01",
            "take this opportunity to rejoin the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Actually, his scheduled\x01",
            "discharge date is still\x01",
            "far off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I don't want him to overdo it,\x01",
            "but I decided to fold after he\x01",
            "practically begged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha. I bet Raymond will\x01",
            "be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf the Inspector rejoins,\x01",
            "Section Two will get that\x01",
            "much stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I intend to do what\x01",
            "I can to help out somehow,\x01",
            "without overdoing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems things are\x01",
            "quite hard on your end,\x01",
            "so be very careful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, thank you very\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 7)
    TurnDirection(0x9, 0x16, 0)
    TurnDirection(0x16, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_3BD4")

    label("loc_380E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3BD4")

    def lambda_381C():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_381C)
    Sleep(0)

    def lambda_382C():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_382C)
    Sleep(0)

    def lambda_383C():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_383C)
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38E4")
    Jump("loc_392E")

    label("loc_38E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3904")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_392E")

    label("loc_3904")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3924")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_392E")

    label("loc_3924")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_392E")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39E4")
    Jump("loc_3A2E")

    label("loc_39E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A04")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A2E")

    label("loc_3A04")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A24")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A2E")

    label("loc_3A24")

    OP_52(0x16, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A2E")

    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x10)

    ChrTalk(
        0x9,
        (
            "Man, I made you see\x01",
            "something embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I keep getting caught up\x01",
            "in Fara's pace ever\x01",
            "since I married her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, she's a lovely\x01",
            "wife, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHehe, very lovely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "My...♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Haha, lovely you say.\x01",
            "You heard that, right,\x01",
            "dear?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "(...Because she's like this\x01",
            "even in front of these guys and\x01",
            "Raymond, she's troublesome...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x10)

    label("loc_3BD4")

    Return()

    # Function_21_3478 end

    def Function_22_3BD5(): pass

    label("Function_22_3BD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CDC")

    ChrTalk(
        0xA,
        (
            "My life was saved by\x01",
            "Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm a coward, but...\x01",
            "I'll have to get my act\x01",
            "together going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As the Inspector's subordinate, I'll\x01",
            "have to become a splendid detective\x01",
            "someday so as not to embarrass him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D98")

    label("loc_3CDC")


    ChrTalk(
        0xA,
        (
            "I'm a coward, but...\x01",
            "I'll have to get my act\x01",
            "together going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As the Inspector's subordinate, I'll\x01",
            "have to become a splendid detective\x01",
            "someday so as not to embarrass him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D98")

    TalkEnd(0xFE)
    Return()

    # Function_22_3BD5 end

    def Function_23_3D9C(): pass

    label("Function_23_3D9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_453A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D4")

    ChrTalk(
        0xB,
        (
            "#11601FIt's you guys... It\x01",
            "seems that something\x01",
            "terrible is going on.\x02\x03",
            "#11606FThey say that something\x01",
            "like a mysterious Huge\x01",
            "Tree has appeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes... To tell you the\x01",
            "truth, we still don't\x01",
            "know what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWe can't even say that\x01",
            "the hospital is\x01",
            "completely safe.\x02\x03",
            "#00101FIlya, please be careful\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609FAhaha, thanks. I don't know the full\x01",
            "details, but...\x02\x03",
            "#11600FI'm sure that if you don't give up, you'll\x01",
            "make it through. I'm sure you'll be able\x01",
            "to grab hold of what's important to you.\x02\x03",
            "#11604FI won't ever give up until I stand on the\x01",
            "stage again either...\x02\x03",
            "#11609FSo please do your best until the very end\x01",
            "too, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FIf we've got Ilya's\x01",
            "support, our strength will\x01",
            "increase a hundredfold!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_40CC")
    Call(0, 77)
    Return()

    label("loc_40CC")

    SetScenarioFlags(0x0, 3)
    Jump("loc_41BF")

    label("loc_40D4")


    ChrTalk(
        0xB,
        (
            "#11604FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11609FI too won't ever give up until I stand on\x01",
            "the stage again... So do your best until\x01",
            "the very end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41BF")

    Jump("loc_4535")

    label("loc_41C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6C), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41DF")
    Call(0, 86)
    Jump("loc_4535")

    label("loc_41DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_432D")

    ChrTalk(
        0xB,
        (
            "#11600FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11604FI too won't ever give up until I stand on\x01",
            "the stage again... So do your best until\x01",
            "the very end.\x02\x03",
            "#11609FFufu, and please take care of the girl\x01",
            "who's standing outside too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4442")

    label("loc_432D")


    ChrTalk(
        0xB,
        (
            "#11600FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11604FI too won't ever give up until I stand on\x01",
            "the stage again... So do your best until\x01",
            "the very end.\x02\x03",
            "#11609FFufu, take care of that girl too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4442")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4535")

    label("loc_444A")


    ChrTalk(
        0xB,
        (
            "#11604FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11609FI too won't ever give up until I stand on\x01",
            "the stage again... So do your best until\x01",
            "the very end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4535")

    Jump("loc_5118")

    label("loc_453A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_495A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4894")

    ChrTalk(
        0xB,
        (
            "#11603FRumor has it that something\x01",
            "terrible has happened in the\x01",
            "city, little bro...\x02\x03",
            "#11601FI hear they reported the\x01",
            "shocking truth of the attack on\x01",
            "Crossbell City back then?\x02\x03",
            "Although it seems that detailed\x01",
            "information was restricted and\x01",
            "didn't circulate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FIlya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(For Ilya, that attack\x01",
            "is the root cause of her\x01",
            "severe injuries...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11603F...Well, I don't have any interest\x01",
            "in the truth of that incident at\x01",
            "this late date.\x02\x03",
            "#11600FMore importantly, I wonder when my\x01",
            "next rehabilitation is.\x02\x03",
            "#11609FAnd to return to the stage, I want\x01",
            "to move my body ASAP. I'm just\x01",
            "itching to do something, you know♪\x02",
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
        "#00012FHaha, what can I say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FAs expected from Ilya.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 2)
    Jump("loc_4955")

    label("loc_4894")


    ChrTalk(
        0xB,
        (
            "#11602FI'll keep doing rehab and absolutely\x01",
            "return to the stage, so I've got no\x01",
            "interest in other stuff.\x02\x03",
            "#11609FAah, can't I do the next\x01",
            "rehabilitation yet? I want to move\x01",
            "my body ASAP♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4955")

    Jump("loc_5118")

    label("loc_495A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAB")

    ChrTalk(
        0xB,
        (
            "#11600FAccording to Professor Seiland,\x01",
            "she can't actually tell if I'll\x01",
            "be able to walk again or not...\x02\x03",
            "#11604FThe possibility isn't zero, so\x01",
            "I've got no reason to give up.\x02\x03",
            "#11602FAfter all, man is a living being\x01",
            "who can do his utmost best for\x01",
            "what's precious to him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE6")

    ChrTalk(
        0x103,
        (
            "#00200FLooking at you Ilya, I\x01",
            "can really think like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHehe, little brother, guys. When you\x01",
            "meet Rixia, tell her this.\x02\x03",
            "#11600F"If you put whatever that is in front\x01",
            "of you... Wouldn't you try your best\x01",
            "for that which you hold most dear?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, understood. When we\x01",
            "meet her, we'll absolutely\x01",
            "tell her these words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA3")

    label("loc_4BE6")


    ChrTalk(
        0x101,
        (
            "#00008F(We passed this message from Ilya to\x01",
            "Rixia already, but... It's neither the\x01",
            "time nor place for them to meet yet.)\x02\x03",
            "#00003F(At this time, it's better to keep\x01",
            "quiet about Rixia.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA3")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4D70")

    label("loc_4CAB")


    ChrTalk(
        0xB,
        (
            "#11604FMan is a living being who can do\x01",
            "his utmost best for what's\x01",
            "precious to him.\x02\x03",
            "#11600FIt's not that the possibility that\x01",
            "I'll be walking again is zero, so\x01",
            "I've got no reason to give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D70")

    Jump("loc_5118")

    label("loc_4D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_500F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F79")

    ChrTalk(
        0xB,
        (
            "#11600FI'm worried about everyone in Arc-\x01",
            "en-Ciel who're in the city.\x02\x03",
            "#11609FWell, it's them we're talking about,\x01",
            "so they'll be probably practicing\x01",
            "even in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, is that what\x01",
            "you're worried about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThe people from Arc-en-\x01",
            "Ciel are zealously\x01",
            "practicing for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FHehe. After all, they're\x01",
            "all artists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHehe, Sully is in her\x01",
            "growth period too...\x02\x03",
            "#11609FShe must practice\x01",
            "diligently for when I\x01",
            "make my comeback too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_500A")

    label("loc_4F79")


    ChrTalk(
        0xB,
        (
            "#11600FI'm worried about\x01",
            "everyone in Arc-en-Ciel\x01",
            "who're in the city.\x02\x03",
            "#11609FThey must practice\x01",
            "diligently for when I\x01",
            "make my comeback too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500A")

    Jump("loc_5118")

    label("loc_500F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_5118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FB")

    ChrTalk(
        0xB,
        "#11603F#90W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...Still, to think we'd\x01",
            "see Ilya like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FRight... I can't believe\x01",
            "it's real even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIlya will come back for\x01",
            "sure. ...Let's believe\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5118")

    label("loc_50FB")


    ChrTalk(
        0xB,
        "#11603F#90W............\x02",
    )

    CloseMessageWindow()

    label("loc_5118")

    TalkEnd(0xFE)
    Return()

    # Function_23_3D9C end

    def Function_24_511C(): pass

    label("Function_24_511C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5293")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F9")

    ChrTalk(
        0xC,
        (
            "#04200FYou guys... Please, take\x01",
            "care of Rixia.\x02\x03",
            "#04203FIf Rixia comes back, Ilya\x01",
            "will get better too...\x01",
            "I've got that feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Yeah, wait for us.\x01",
            "We'll find her for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5293")

    label("loc_51F9")


    ChrTalk(
        0xC,
        (
            "#04203FIf Rixia comes back, Ilya\x01",
            "will get better too...\x01",
            "I've got that feeling.\x02\x03",
            "#04200FUntil then, we Arc-en-\x01",
            "Ciel must support Ilya\x01",
            "however we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5293")

    TalkEnd(0xFE)
    Return()

    # Function_24_511C end

    def Function_25_5297(): pass

    label("Function_25_5297")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_52A8")
    Jump("loc_55FF")

    label("loc_52A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5426")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B2")

    ChrTalk(
        0x10,
        (
            "It's about time for us\x01",
            "to request the needed\x01",
            "supplies, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Accepting the independent state\x01",
            "declaration of invalidity, the State\x01",
            "Guard returned to their units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmm, that's a problem.\x01",
            "How should we negotiate\x01",
            "from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5421")

    label("loc_53B2")


    ChrTalk(
        0x10,
        (
            "Hmm, that's a problem.\x01",
            "The State Guard left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "How can we negotiate for\x01",
            "goods supplies from now\x01",
            "on...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5421")

    Jump("loc_55FF")

    label("loc_5426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5434")
    Jump("loc_55FF")

    label("loc_5434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5442")
    Jump("loc_55FF")

    label("loc_5442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_55FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5560")

    ChrTalk(
        0x10,
        (
            "When the hospital was previously\x01",
            "attacked, it seems some people\x01",
            "hid in this linen room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At the time of that\x01",
            "incident I ended up getting\x01",
            "shot in the stomach, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thinking about it now, I\x01",
            "should've hidden quickly too.\x01",
            "Hmm, that was a mistake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_55FF")

    label("loc_5560")


    ChrTalk(
        0x10,
        (
            "Previously, when the\x01",
            "hospital was attacked, I\x01",
            "ended up getting shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thinking about it now, I\x01",
            "should've hidden quickly too.\x01",
            "Hmm, that was a mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55FF")

    TalkEnd(0xFE)
    Return()

    # Function_25_5297 end

    def Function_26_5603(): pass

    label("Function_26_5603")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5614")
    Jump("loc_6409")

    label("loc_5614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5622")
    Jump("loc_6409")

    label("loc_5622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5630")
    Jump("loc_6409")

    label("loc_5630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A36")
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x11,
        (
            "#01309FBy the way... I hope\x01",
            "Shizuku is doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Yes, really.\x02\x03",
            "#00200FKeA was really worried\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FIf you think about it,\x01",
            "they should both be at\x01",
            "Orchis Tower around now.\x02\x03",
            "#00003FI hope we can meet up\x01",
            "with Shizuku somehow,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FLloyd... I hope you are\x01",
            "reunited with the\x01",
            "Support Section soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406FWell, honestly speaking,\x01",
            "the road ahead is quite\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...In order to take back\x01",
            "KeA, we absolutely need\x01",
            "everyone's strength.\x02\x03",
            "#00000FThat's why no matter how\x01",
            "painful it is, I'll move\x01",
            "forward without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHaha, I'm sure you will.\x02\x03",
            "#01304FI will pray to the\x01",
            "Goddess from here.\x01",
            "...Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, Cecil. Hearing\x01",
            "you say that gives me\x01",
            "tremendous strength.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A27")

    ChrTalk(
        0x107,
        (
            "#01200F#13C...............\x02\x03",
            "(She really is your\x01",
            "descendant... ─Ursula.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 500)

    ChrTalk(
        0x103,
        (
            "#00205FZeit... Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 500)

    ChrTalk(
        0x107,
        (
            "#01203F#13C...Hehe, don't worry. I\x01",
            "also get lost in thought\x01",
            "sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A27")

    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1AC, 2)
    Jump("loc_5BDA")

    label("loc_5A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2B")
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0x11,
        (
            "#01300FIlya, let's go do\x01",
            "rehabilitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FYeah, got it.\x02\x03",
            "#11609FThanks for taking care\x01",
            "of me again today, Head\x01",
            "Nurse Cecil㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHaha, I'm here for you\x01",
            "and everyone. I'll help\x01",
            "you properly.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_5BDA")

    label("loc_5B2B")


    ChrTalk(
        0x11,
        (
            "#01302FLloyd, I am sure you will be able\x01",
            "to save all the Support Section\x01",
            "members and reunite with KeA.\x02\x03",
            "#01304FI will pray the Goddess from\x01",
            "here. ...Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BDA")

    Jump("loc_6409")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5BED")
    Jump("loc_6409")

    label("loc_5BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BFB")
    Jump("loc_6409")

    label("loc_5BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C0C")
    Call(0, 27)
    Jump("loc_6409")

    label("loc_5C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C1D")
    Call(0, 27)
    Jump("loc_6409")

    label("loc_5C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C2B")
    Jump("loc_6409")

    label("loc_5C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA3")
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x103, 500)

    ChrTalk(
        0x11,
        (
            "#01302FMy, if it isn't Tio.\x01",
            "You've returned to the\x01",
            "Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, I got back just\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FHaha, I am happy to see\x01",
            "you again.\x02\x03",
            "#01304FI heard you were really\x01",
            "busy, but... Yes, your\x01",
            "complexion is nice today.\x02\x03",
            "#01300FPlease pay attention to\x01",
            "your health so you don't\x01",
            "collapse like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FHaha, thank you for all your\x01",
            "help back then.\x02\x03",
            "#00200FWell, if I could sleep again\x01",
            "in your soft bed, I might even\x01",
            "be willing to pass out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, I totally agree\x01",
            "with you 'bout that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNow look here, Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FPlease, have a little\x01",
            "respect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FHaha... It seems you all\x01",
            "are the same as always.\x02\x03",
            "#01304FNow that Tio's back, the\x01",
            "Support Section is finally\x01",
            "in full operation.\x02\x03",
            "#01309FI will always support you,\x01",
            "so do your best from now\x01",
            "on, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 5)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_601B")

    label("loc_5FA3")


    ChrTalk(
        0x11,
        (
            "#01300FMihail is going to be\x01",
            "discharged soon.\x02\x03",
            "#01304FI'm a little sad,\x01",
            "however... Haha, I'm\x01",
            "really happy for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601B")

    Jump("loc_6409")

    label("loc_6020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6031")
    Call(0, 29)
    Jump("loc_6409")

    label("loc_6031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637B")

    ChrTalk(
        0x101,
        (
            "#00000FAh... Sister Cecil, so\x01",
            "this is where you were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf I remember correctly,\x01",
            "this is Shizuku's room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300FYes, because she's out,\x01",
            "I'm cleaning while I can.\x02\x03",
            "#01304FToday, Shizuku went to\x01",
            "have fun in the city.\x02\x03",
            "#01309FA little while ago she was\x01",
            "happily talking, saying\x01",
            "she was going to meet KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, they've become\x01",
            "good friends for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, she IS KeA. It's\x01",
            "only obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. I'm certain that girl\x01",
            "has a talent for making\x01",
            "friends with people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHaha... You can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300FThanks to her, Shizuku has\x01",
            "become more cheerful than\x01",
            "before... I'm grateful to KeA.\x02\x03",
            "#01302FThe next time I can take a day\x01",
            "off, I want to spend some time\x01",
            "with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'm sure KeA would\x01",
            "like that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01309FHaha, I can't wait.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 1)
    Jump("loc_6409")

    label("loc_637B")


    ChrTalk(
        0x11,
        (
            "#01300FShizuku should be playing\x01",
            "with KeA around now.\x02\x03",
            "#01309FHaha. It's a rare day out\x01",
            "for her, so I hope she\x01",
            "enjoys it to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6409")

    TalkEnd(0xFE)
    Return()

    # Function_26_5603 end

    def Function_27_640D(): pass

    label("Function_27_640D")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E5")

    ChrTalk(
        0xD,
        (
            "#11200FCecil... It seems there\x01",
            "were a lot of ambulances\x01",
            "yesterday.\x02\x03",
            "#11210FI heard that there was a\x01",
            "big accident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01303FIt seems that a train\x01",
            "derailed along West\x01",
            "Crossbell Highway.\x02\x03",
            "#01302FBut rest assured. Thanks\x01",
            "to the doctors' efforts,\x01",
            "there were no casualties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FIs that so... Thank\x01",
            "goodness.\x02\x03",
            "#11208FWhen I thought it could've\x01",
            "been a severe accident like\x01",
            "what happened to me, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01308FShizuku...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_66AF")

    label("loc_65E5")


    ChrTalk(
        0x11,
        (
            "#01300FThanks to the doctors'\x01",
            "efforts, all the train\x01",
            "accident patients were saved.\x02\x03",
            "So, don't worry about the\x01",
            "accident. Let's concentrate on\x01",
            "your rehabilitation for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11202FYes... Please.\x02",
    )

    CloseMessageWindow()

    label("loc_66AF")

    Jump("loc_686F")

    label("loc_66B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_686F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66CF")
    Call(0, 28)
    Jump("loc_686F")

    label("loc_66CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D5")

    ChrTalk(
        0x11,
        (
            "#01304FHaha, then I will read\x01",
            "it. ...*ahem*.\x02\x03",
            "#01300F"Shizuku, how are you? I\x01",
            "am well."\x02\x03",
            ""Every night I pray the\x01",
            "Goddess that you become\x01",
            "able to see."\x02\x03",
            "#01309FHaha, how typical of\x01",
            "that boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FMihail... ...I'm very\x01",
            "happy for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_686F")

    label("loc_67D5")


    ChrTalk(
        0x11,
        (
            "#01304FOh right, he enclosed a\x01",
            "picture too.\x02\x03",
            "#01302FHaha. He's standing\x01",
            "between his parents and\x01",
            "looks very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11209F*chuckle*, how nice...\x02",
    )

    CloseMessageWindow()

    label("loc_686F")

    SetChrSubChip(0xD, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_27_640D end

    def Function_28_6878(): pass

    label("Function_28_6878")

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
        "#12P#00000FHi, Cecil, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11202FOh... Good morning,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FMy, if it isn't Lloyd\x01",
            "and the others.\x02\x03",
            "#01309FHaha, could you have\x01",
            "come to visit Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FYes, we have, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#N#12P#10105FUmm, could we have\x01",
            "interrupted you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x11, 0xB4, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FHaha, no, actually.\x02\x03",
            "#01304FA letter from Mihail,\x01",
            "who returned to Lｳman\x01",
            "State, arrived today.\x02\x03",
            "#01300FI was just thinking of\x01",
            "reading it to Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FMihail was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FThe little boy who\x01",
            "Professor Seiland\x01",
            "operated on, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11204FYes, he was a boy I got\x01",
            "along really well\x01",
            "with...\x02\x03",
            "#11200FWhen he was discharged,\x01",
            "we promised to exchange\x01",
            "letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHaha, ain't that nice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FAt St. Ursula Hospital we sometimes\x01",
            "receive letters from discharged\x01",
            "patients, like this one.\x02\x03",
            "#01304FWe are busy so we can't quite make\x01",
            "the time to reply, but...\x02\x03",
            "#01300FLearning what happened to our\x01",
            "patients after their treatments is\x01",
            "one of my sources of energy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha. Being who you are, Cecil,\x01",
            "you probably diligently replied\x01",
            "to each and every one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204F...Maybe I should have\x01",
            "sent letters to Head\x01",
            "Nurse Martha as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xE1, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FHaha. When she saw you\x01",
            "again, the head nurse\x01",
            "was really happy.\x02\x03",
            "#01309FIt is not too late, so\x01",
            "why not start now if you\x01",
            "have the chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FHaha. I'll think about\x01",
            "it when work slows down.\x02",
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

    # Function_28_6878 end

    def Function_29_6F0B(): pass

    label("Function_29_6F0B")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71CA")

    ChrTalk(
        0x11,
        (
            "#01300FMihail, how are you\x01",
            "feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I haven't gotten even\x01",
            "a single spasm. It seems\x01",
            "unreal that I was suffering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01304FHaha, I'm glad for you.\x02\x03",
            "#01300FThe day you'll be discharged is\x01",
            "coming soon... You'll be able to\x01",
            "live with your parents again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I think I'm half\x01",
            "happy and half sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When I'll go back to Lｳman\x01",
            "State, I'll won't be able to\x01",
            "see Miss Cecil and Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300F...We've fought your illness\x01",
            "for a long time, huh? It's true\x01",
            "that it will be sad, but...\x02\x03",
            "#01304FEven if we are far away, these\x01",
            "bonds will not break. ...I\x01",
            "believe that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...Yes, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Thank you for\x01",
            "everything, Miss Cecil.\x01",
            "I'll never forget you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 3)
    Jump("loc_7259")

    label("loc_71CA")


    ChrTalk(
        0x11,
        (
            "#01309FHaha. Let's head towards\x01",
            "the day of your\x01",
            "discharge with a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Okay, I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I must say my\x01",
            "goodbyes to Shizuku too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7259")

    SetChrSubChip(0xE, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_29_6F0B end

    def Function_30_7262(): pass

    label("Function_30_7262")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7273")
    Jump("loc_7399")

    label("loc_7273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_728E")
    Call(0, 31)
    Jump("loc_7353")

    label("loc_728E")

    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        (
            "Hmm, according to how the sky\x01",
            "felt yesterday, I had a hunch\x01",
            "that it wouldn't rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If your intuition got it right\x01",
            "instead of the weather forecast,\x01",
            "it would've been too amazing!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_7353")

    Jump("loc_7399")

    label("loc_7358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7366")
    Jump("loc_7399")

    label("loc_7366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7374")
    Jump("loc_7399")

    label("loc_7374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7382")
    Jump("loc_7399")

    label("loc_7382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7390")
    Jump("loc_7399")

    label("loc_7390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7399")

    label("loc_7399")

    TalkEnd(0xFE)
    Return()

    # Function_30_7262 end

    def Function_31_739D(): pass

    label("Function_31_739D")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Xilun, you... You were\x01",
            "on the rooftop drying\x01",
            "the sheets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Didn't the manager say\x01",
            "the forecast said it was\x01",
            "going to rain!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I thought what if it\x01",
            "unexpectedly didn't rain?\x01",
            "Ehehe, I tried betting on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Why would you do\x01",
            "something like that!?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 7)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_31_739D end

    def Function_32_74B7(): pass

    label("Function_32_74B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_74C8")
    Jump("loc_7978")

    label("loc_74C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E3")
    Call(0, 31)
    Jump("loc_756F")

    label("loc_74E3")


    ChrTalk(
        0x13,
        (
            "Honestly, the sheets I so\x01",
            "painstakingly washed must\x01",
            "all be washed again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Wait, more importantly,\x01",
            "I've got to bring them\x01",
            "in quick!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756F")

    Jump("loc_7978")

    label("loc_7574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7582")
    Jump("loc_7978")

    label("loc_7582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7741")

    ChrTalk(
        0x13,
        (
            "After I saw Mihail energetically waving\x01",
            "goodbye on the day of his discharge, I\x01",
            "was moved and ended up crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "When that happened, Xilun gave me a\x01",
            "handkerchief in silence. She can be\x01",
            "thoughtful every now and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Looking at it carefully, it wasn't\x01",
            "a handkerchief but my favorite\x01",
            "skirt that I previously lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "...There were so many things to\x01",
            "retort about and being deeply\x01",
            "moved I made a mess of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_77DB")

    label("loc_7741")


    ChrTalk(
        0x13,
        (
            "Well, that aside... I'm\x01",
            "really happy that Mihail\x01",
            "left the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I believe he's living\x01",
            "happily with his parents in\x01",
            "Lｳman State around now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77DB")

    Jump("loc_7978")

    label("loc_77E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77EE")
    Jump("loc_7978")

    label("loc_77EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_77FC")
    Jump("loc_7978")

    label("loc_77FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C8")

    ChrTalk(
        0x13,
        (
            "Mr. Geval, who was\x01",
            "hospitalised here, was\x01",
            "discharged a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That man was so selfish and really\x01",
            "gave us trouble, but... I wonder\x01",
            "where is and how he's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7978")

    label("loc_78C8")


    ChrTalk(
        0x13,
        (
            "Ah, come to think of it,\x01",
            "Xilun is supposed to do\x01",
            "an IV drip today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Because that girl always makes\x01",
            "crazy mistakes, I'm worried. ...I\x01",
            "guess I'll go check on her later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7978")

    TalkEnd(0xFE)
    Return()

    # Function_32_74B7 end

    def Function_33_797C(): pass

    label("Function_33_797C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_798D")
    Jump("loc_7A56")

    label("loc_798D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_799B")
    Jump("loc_7A56")

    label("loc_799B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_79A9")
    Jump("loc_7A56")

    label("loc_79A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_79B7")
    Jump("loc_7A56")

    label("loc_79B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_79C5")
    Jump("loc_7A56")

    label("loc_79C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_79D3")
    Jump("loc_7A56")

    label("loc_79D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79EE")
    Call(0, 34)
    Jump("loc_7A56")

    label("loc_79EE")


    ChrTalk(
        0x14,
        (
            "Even so, Professor\x01",
            "Seiland is...\x01",
            "wonderfully skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It seems I have much to\x01",
            "learn from her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A56")

    TalkEnd(0xFE)
    Return()

    # Function_33_797C end

    def Function_34_7A5A(): pass

    label("Function_34_7A5A")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "Hmm... Your postoperative\x01",
            "progress seems good. You'll be\x01",
            "able to leave the hospital soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Contact your parents in\x01",
            "the Lｳman State later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yes, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Professor Seiland is skilled too, but\x01",
            "it was your courage to undergo surgery\x01",
            "that overcame the illness most of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "...You did well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...*sob*... Thank you,\x01",
            "doctor!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 6)
    SetChrSubChip(0xE, 0x0)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_34_7A5A end

    def Function_35_7BDF(): pass

    label("Function_35_7BDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BFD")
    Call(0, 21)
    Jump("loc_7CCD")

    label("loc_7BFD")


    ChrTalk(
        0x16,
        (
            "To tell the truth, his scheduled\x01",
            "discharge isn't for a few days,\x01",
            "but... He asked me earnestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Uhuhu. However, I'm glad. After\x01",
            "all, what I like most about him is\x01",
            "seeing him when he's working hard㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CCD")

    Jump("loc_81F0")

    label("loc_7CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DD9")

    ChrTalk(
        0x16,
        (
            "I read through the book\x01",
            "I brought for the visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It would be useless reading the same\x01",
            "book over again... Yes, I think I'll\x01",
            "give it to you as a present♪\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2FA, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 4)
    Jump("loc_7E56")

    label("loc_7DD9")


    ChrTalk(
        0x16,
        (
            "All the state guardsmen\x01",
            "who came to the hospital\x01",
            "seem to have left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...I wonder if they're\x01",
            "trying to do something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E56")

    Jump("loc_81F0")

    label("loc_7E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FB1")

    ChrTalk(
        0x16,
        (
            "I was visiting at the time of\x01",
            "the declaration of independence,\x01",
            "and I've stayed here ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The required application to\x01",
            "travel to and from the city\x01",
            "has become a serious bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I didn't have many chances to quietly\x01",
            "spend time with him, so since I have the\x01",
            "opportunity, I might as well enjoy it♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8092")

    label("loc_7FB1")


    ChrTalk(
        0x16,
        (
            "I was visiting at the time of\x01",
            "the declaration of independence,\x01",
            "and I've stayed here ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I didn't have many chances to quietly\x01",
            "spend time with him, so since I have the\x01",
            "opportunity, I might as well enjoy it♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8092")

    Jump("loc_81F0")

    label("loc_8097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_815C")

    ChrTalk(
        0x16,
        (
            "Haha. Oh, this man... He's no longer\x01",
            "young but he does nothing but reckless\x01",
            "things... He worried you too, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "However, protecting a\x01",
            "cute girl like you was\x01",
            "his best play♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F0")

    label("loc_815C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_81F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8177")
    Call(0, 21)
    Jump("loc_81F0")

    label("loc_8177")


    ChrTalk(
        0x16,
        (
            "I understand that there\x01",
            "are troubles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Now I must properly\x01",
            "watch him so he doesn't\x01",
            "do anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F0")

    TalkEnd(0xFE)
    Return()

    # Function_35_7BDF end

    def Function_36_81F4(): pass

    label("Function_36_81F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8205")
    Jump("loc_8AAC")

    label("loc_8205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8213")
    Jump("loc_8AAC")

    label("loc_8213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_84FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8446")

    ChrTalk(
        0x17,
        (
            "The hardest blow as an independent\x01",
            "state that has cut diplomatic ties is\x01",
            "that I can't cooperate with Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "As for medical supplies, it seems that\x01",
            "a large quantity was prepared by the\x01",
            "President in case of emergency, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Medicines are to be carefully selected\x01",
            "and prescribed to match the patient's\x01",
            "condition and constitution to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "With the amount of the medicines the\x01",
            "President stored, it'll be difficult\x01",
            "to deal with all the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "What should I do from\x01",
            "here on...? I need to\x01",
            "think of a way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_84F5")

    label("loc_8446")


    ChrTalk(
        0x17,
        (
            "With the amount of the medicines the\x01",
            "President stored, it'll be difficult\x01",
            "to deal with all the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "What should I do from\x01",
            "here on...? I need to\x01",
            "think of a way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F5")

    Jump("loc_8AAC")

    label("loc_84FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88D3")

    ChrTalk(
        0x17,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FDoctor Seiland...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 500)

    ChrTalk(
        0x17,
        (
            "...You guys, huh. It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThis was Shizuku's room.\x01",
            "...What are you doing\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "She was a patient I was in\x01",
            "charge of. I was just\x01",
            "indulging in some thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...Like how she's doing after\x01",
            "she was forced from the\x01",
            "hospital by Arios MacLaine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FCome to think of it, we\x01",
            "haven't seen her since\x01",
            "then.\x02\x03",
            "#10403FShe's probably being\x01",
            "sheltered somewhere\x01",
            "within Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting the patient you're in charge\x01",
            "of taken away is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Although I understand there was nothing I\x01",
            "could have done about it, seeing as how he\x01",
            "is the newly appointed Secretary of Defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I understand that,\x01",
            "but... There's no way I\x01",
            "can accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FDoctor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...I'm sorry, it seems\x01",
            "I've engaged in\x01",
            "pointless talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "You've come for a visit,\x01",
            "right? ...Sorry, but\x01",
            "could you leave me alone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 6)
    ClearChrFlags(0x17, 0x10)
    Jump("loc_8AAC")

    label("loc_88D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89F7")

    ChrTalk(
        0x17,
        (
            "Shizuku MacLaine... I carefully\x01",
            "prepared for her treatment over\x01",
            "the course of one year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting the patient you're in charge\x01",
            "of taken away is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I guess being bound to a\x01",
            "discharged patient can't\x01",
            "be helped either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8AAC")

    label("loc_89F7")


    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting the patient you're in charge\x01",
            "of taken away is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I guess being bound to a\x01",
            "discharged patient can't\x01",
            "be helped either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AAC")

    TalkEnd(0xFE)
    Return()

    # Function_36_81F4 end

    def Function_37_8AB0(): pass

    label("Function_37_8AB0")

    Sound(160, 0, 100, 0)
    Return()

    # Function_37_8AB0 end

    def Function_38_8AB7(): pass

    label("Function_38_8AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C79")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B6C")
    SetChrPos(0x109, -16360, 0, 29320, 90)

    label("loc_8B6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B8D")
    SetChrPos(0x105, -16360, 0, 29320, 90)

    label("loc_8B8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BAE")
    SetChrPos(0x10A, -16360, 0, 29320, 90)

    label("loc_8BAE")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#10703F(...Everyone. If you're\x01",
            "going inside, I'll stay\x01",
            "here...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(...All right.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F(Same as always, eh?)\x02",
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
    Jump("loc_8CDD")

    label("loc_8C79")

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

    label("loc_8CDD")

    Return()

    # Function_38_8AB7 end

    def Function_39_8CDE(): pass

    label("Function_39_8CDE")

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

    # Function_39_8CDE end

    def Function_40_8D46(): pass

    label("Function_40_8D46")

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
        "#2P#2S─Excuse me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_68(5670, 1000, -47970, 2500)

    def lambda_8F1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F1A)
    Sleep(200)

    def lambda_8F32():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F32)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    def lambda_8F4E():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F4E)

    def lambda_8F63():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_8F63)
    Sleep(50)

    def lambda_8F73():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F73)
    Sleep(50)

    def lambda_8F8B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F8B)
    Sleep(50)

    def lambda_8FA3():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FA3)

    def lambda_8FB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FB8)
    Sleep(200)

    def lambda_8FCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8FCC)
    Sleep(500)

    def lambda_8FE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8FE0)

    def lambda_8FF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8FF1)
    Sleep(500)

    def lambda_9005():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9005)

    def lambda_9016():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9016)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11705F#2723V#5P#40WAh... Noｱl, and\x01",
            "everyone...!\x02",
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
        (
            "#00000F#6PSo this is where you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#6P#NExcuse us. Is now a good\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x136,
        (
            "#01309F#11PIt is. I just changed\x01",
            "her IV drip.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5920, 1000, -48010, 2000)

    def lambda_913A():
        OP_9B(0x1, 0xFE, 0xE1, 0x6D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_913A)
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
            "#30WEhehe... Thank you very much.\x02\x03",
            "You came all the way here to see\x01",
            "me?\x02",
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
            "#00002F#12PYeah, Noｱl said you had\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, I'm relieved. It\x01",
            "looks like you're doing\x01",
            "better than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PYou're right. Her\x01",
            "complexion looks good\x01",
            "too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WEhehe, I'm fine, fine.\x01",
            "I'm all right now.\x02\x03",
            "#11700FIt seems I'll be moved\x01",
            "to a normal room in two\x01",
            "or three days...\x02\x03",
            "#11709FMy discharge won't be\x01",
            "long after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PThat's no good, Fran.\x02\x03",
            "#10101FBecause your stamina has\x01",
            "dropped, you have to\x01",
            "rest for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WEhehe... I'm a fragile\x01",
            "person.\x02\x03",
            "#11708FInspector Donovan\x01",
            "protected me and...\x02\x03",
            "#11706F#40W...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PFran...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6P...There's no need to\x01",
            "worry about that, you\x01",
            "know.\x02\x03",
            "#00301FIt was those guys'\x01",
            "fault... Those damn Red\x01",
            "Constellation guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#5P#30WEhehe... Yes.\x02\x03",
            "#11711FBut, I have to support\x01",
            "you all and provide\x01",
            "backup...\x02\x03",
            "#11706FI have to do my best and\x01",
            "recover...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PIt's ok, don't worry.\x02\x03",
            "#00000FIt's sad not being able to hear\x01",
            "your voice, but the reports are\x01",
            "getting processed somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PFor now, please focus on\x01",
            "making a full recovery.\x02\x03",
            "#00102FIf you do that, we'll\x01",
            "once again rely on you\x01",
            "without reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W...Yes. Thank you very\x01",
            "much.\x02\x03",
            "#11705FBy the way... Noｱl, I\x01",
            "heard you're going back\x01",
            "to the CGF...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PDid mom tell you? Yes, it's\x01",
            "something I've been\x01",
            "thinking about.\x02\x03",
            "#10112FI guess I'll be a little\x01",
            "lonely since I won't\x01",
            "receive your support, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11701F#5P#40WMrr... "A little" you\x01",
            "say? You're heartless!\x02\x03",
            "#11706F#50W...Because you're...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_98A5():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_98A5)
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
        "#10111F#12PFran!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x136,
        (
            "#01304F#11PShe's fine, it's just\x01",
            "her IV medicine taking\x01",
            "effect.\x02\x03",
            "#01302FIt's best to end your\x01",
            "conversation here and\x01",
            "let her rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11706F#11P#40WI'm all right... Lloyd and\x01",
            "the others came all the way\x01",
            "here, you see...\x02\x03",
            "#11701FAlso, before she goes back\x01",
            "to the CGF, I've got to tell\x01",
            "Noｱl a foolproof way to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12P*sigh*, what the heck\x01",
            "are you saying?\x02\x03",
            "#10108F...Everyone, I'm sorry.\x01",
            "Could we let her rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POf course. ...Fran,\x01",
            "we'll come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PPlease sleep soundly.\x02\x03",
            "#00202FI'll bring you a cake as\x01",
            "present once you've\x01",
            "regained your stamina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#11P#40WAhaha... Yes, I can't\x01",
            "wait...\x02\x03",
            "#11704F#50W...............\x02",
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
            "#10308F#6P...Looks like her\x01",
            "stamina has dropped\x01",
            "considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11PYes, it's because she had\x01",
            "a large blood transfusion\x01",
            "during her surgery...\x02\x03",
            "#01300FHowever, she'll get\x01",
            "better.\x02\x03",
            "#01309FDon't worry, she'll\x01",
            "recover in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#12PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P...Let's leave for now.\x02",
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

    def lambda_9EB7():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9EB7)
    Sleep(50)

    def lambda_9ECF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_9ECF)
    WaitChrThread(0x136, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00005F#6PBy the way...\x02\x03",
            "#00001FAre Inspector Donovan\x01",
            "and Ilya still no\x01",
            "visitors allowed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#11P...More or less.\x02\x03",
            "#01308FBut it seems you know\x01",
            "both of them, so...\x02\x03",
            "#01300FI'll come with you, so\x01",
            "would you like to check\x01",
            "on them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PC-Can we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#12PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PCecil, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#11PHaha... Let's go then.\x02\x03",
            "#01300FRoom 302 over there is\x01",
            "Mr. Donovan's.\x02\x03",
            "Ilya is in room 303,\x01",
            "opposite Shizuku's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PGot it. Shall we go?\x02",
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

    # Function_40_8D46 end

    def Function_41_A13C(): pass

    label("Function_41_A13C")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_41_A13C end

    def Function_42_A171(): pass

    label("Function_42_A171")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xFA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_A171 end

    def Function_43_A197(): pass

    label("Function_43_A197")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_43_A197 end

    def Function_44_A1C3(): pass

    label("Function_44_A1C3")

    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x79E, 0x7D0, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_44_A1C3 end

    def Function_45_A1E9(): pass

    label("Function_45_A1E9")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_A1E9 end

    def Function_46_A21E(): pass

    label("Function_46_A21E")

    OP_9B(0x0, 0xFE, 0x4, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_46_A21E end

    def Function_47_A244(): pass

    label("Function_47_A244")

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
        "Cecil's Voice",
        (
            "#2S#5PMr. Raymond? I'm coming\x01",
            "in.\x07\x00\x02",
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

    def lambda_A42D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_A42D)

    def lambda_A442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_A442)
    Sleep(100)
    Sleep(100)

    def lambda_A459():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A459)

    def lambda_A46A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A46A)
    Sleep(100)

    def lambda_A482():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A482)
    Sleep(100)

    def lambda_A49A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A49A)

    def lambda_A4AB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A4AB)
    Sleep(100)

    def lambda_A4C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A4C3)

    def lambda_A4D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4D4)
    Sleep(100)

    def lambda_A4EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A4EC)

    def lambda_A4FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4FD)
    Sleep(100)

    def lambda_A515():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A515)

    def lambda_A526():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A526)
    Sleep(100)

    def lambda_A53E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A53E)
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
        "#6PCecil... And you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PMr. Raymond... Thank you\x01",
            "for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PYou were nursing him,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PAhaha... I do it every\x01",
            "now and then instead of\x01",
            "the Inspector's wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PAlthough I feel like if the Inspector\x01",
            "opened his eyes he'd yell at me. "Why the\x01",
            "hell are you loafing around!?", he'd say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11P...Indeed, it feels like\x01",
            "something he'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PThat equipment... Is it\x01",
            "an artificial\x01",
            "respirator?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PYeah... It seems his\x01",
            "respiratory system\x01",
            "suffered serious damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf he somehow regained\x01",
            "consciousness, I think his recovery\x01",
            "would speed up too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#30W...............\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11P...The Inspector, you see...\x01",
            "At the time of the explosion,\x01",
            "he protected Fran and I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PSomeone worthless like\x01",
            "me who just panicked in\x01",
            "that awful situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PFran was so badly hurt that she\x01",
            "had to undergo surgery, yet I\x01",
            "just had some scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P...My good luck and\x01",
            "impudence are just so\x01",
            "deplorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11PRaymond...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P...It's not your fault,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11P...Raymond. Why don't you\x01",
            "take a break?\x02\x03",
            "#01301FHe's now in stable condition,\x01",
            "you see. We'll take care of\x01",
            "him on our rounds as well.\x02\x03",
            "You won't last if you don't\x01",
            "rest a little, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    ChrTalk(
        0xA,
        "#6PAhaha... Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHowever, the Inspector's wife\x01",
            "will be here in a little\x01",
            "while, so until then, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#01306F#11P*sigh*... All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11P...Please, take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWe'll come visit again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYes... I think the\x01",
            "Inspector would like\x01",
            "that as well.\x02",
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

    # Function_47_A244 end

    def Function_48_AC58(): pass

    label("Function_48_AC58")

    Sleep(600)
    Sound(107, 0, 100, 0)
    Return()

    # Function_48_AC58 end

    def Function_49_AC62(): pass

    label("Function_49_AC62")

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
        "Cecil's Voice",
        "#2S#11PSully? Can I come in?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04208F#5P#30W............\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-97700, 1000, -3750, 3000)

    def lambda_AE2C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_AE2C)
    Sleep(50)

    def lambda_AE44():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE44)

    def lambda_AE59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_AE59)
    Sleep(50)

    def lambda_AE6D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE6D)
    Sleep(50)

    def lambda_AE85():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE85)
    Sleep(50)

    def lambda_AE9D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE9D)
    Sleep(50)

    def lambda_AEB5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AEB5)
    Sleep(50)

    def lambda_AECD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AECD)
    Sleep(50)
    Sleep(100)

    def lambda_AEE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEE8)

    def lambda_AEF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AEF9)
    Sleep(400)

    def lambda_AF0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF0D)

    def lambda_AF1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AF1E)
    Sleep(400)

    def lambda_AF32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF32)

    def lambda_AF43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AF43)
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
        "#00008F#5PSully...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_AFC4")

    ChrTalk(
        0x102,
        "#00108F#5P............\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFE2")

    label("loc_AFC4")


    ChrTalk(
        0x102,
        "#00106F#5PSo you came...\x02",
    )

    CloseMessageWindow()

    label("loc_AFE2")

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
        "#11P#5P#60W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P#NIlya...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00301F#5P............\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#04206F#6P#30WWhat a peaceful and... pretty\x01",
            "sleeping face, right?\x02\x03",
            "#04208FShe always sleeps like a log, with\x01",
            "her hair all messed up... And yet,\x01",
            "only at a time like this she...\x02\x03",
            "#04202FHaha... It's so unlike her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#5P...How is she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#5P...She had bone fractures\x01",
            "throughout her body and damage\x01",
            "to her internal organs.\x02\x03",
            "#01308FThe surgery was successful,\x01",
            "but she continues to be in a\x01",
            "coma...\x02\x03",
            "#01301FAt present she relies on a\x01",
            "life-support system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...That bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5P...Shit...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#04202F#6P#30W...Even if she regains\x01",
            "consciousness, they said\x01",
            "she'll never fully recover...\x02\x03",
            "Can you believe it? Ilya will\x01",
            "never stand on stage again...\x02\x03",
            "#04208FAnd... It was because she\x01",
            "protected someone like me...\x02\x03",
            "#04206F#40W...Something like that...\x01",
            "...Something like that\x01",
            "shouldn't have...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B451():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B451)
    Sleep(800)
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00001F#5P...Sully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#01303F#5P............\x02",
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
        "#04205F#6P#40W......Huh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#5PIt's all right... I'm sure\x01",
            "it'll be all right.\x02\x03",
            "I know Ilya better than\x01",
            "anyone.\x02\x03",
            "#01308FNo matter the adversity,\x01",
            "she doesn't give up and\x01",
            "just keeps gazing upward...\x02\x03",
            "#01302FThat is who Ilya Platiｲre\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04212F#6P#40W...B-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P─I think so too.\x02\x03",
            "#00002FIf she wasn't like that, I think\x01",
            "she wouldn't be able to create\x01",
            "such unconventional plays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6P#NRight...\x02\x03",
            "#00102FI think it's because of\x01",
            "Ilya's greed that she can\x01",
            "realize what's possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00204F#6P#NAs long as there's a\x01",
            "stage... I'm sure Ilya\x01",
            "will return.\x02\x03",
            "#00202FIt's strange, but it\x01",
            "does seem like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#04205F#6P#30W......Ah......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PYeah...\x02\x03",
            "#00300FFor now, believe in the\x01",
            "Goddess and Ilya and do\x01",
            "what only you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PToday aside, don't you\x01",
            "think you shouldn't skip\x01",
            "out on stage practice?\x02\x03",
            "#10302FThat way, she'd be lured\x01",
            "there and wake up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PYes... For sure!\x02\x03",
            "#10102FGetting sucked in by an\x01",
            "enjoyable performance would\x01",
            "open her eyes for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04212F#6P#30W............\x02",
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
            "#04204F#6P...Thanks. I've cheered\x01",
            "up a bit.\x02\x03",
            "#04208FYou're right... We've\x01",
            "got to pull ourselves\x01",
            "together...\x02\x03",
            "Rixia too... She's\x01",
            "gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#5P............\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#04206F#6P...Say, guys.\x02\x03",
            "If possible, could you\x01",
            "find Rixia for me?\x02\x03",
            "#04208FNo matter the\x01",
            "circumstances, Rixia's\x01",
            "still Rixia...\x02\x03",
            "#04201FAnd, if Rixia comes\x01",
            "back, I think Ilya will\x01",
            "get better too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P─All right.\x02\x03",
            "#00000FOn the name of the\x01",
            "Special Support Section,\x01",
            "we'll find her for sure.\x02",
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
            "#01302F#12PThank you, everyone.\x02\x03",
            "With this, I think Sully\x01",
            "will cheer up.\x02\x03",
            "#01304FYou even cheered me up a\x01",
            "little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5PCecil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PAs we thought, her\x01",
            "condition is quite\x01",
            "serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#12PYes... Honestly, I'm\x01",
            "worried.\x02\x03",
            "#01308F...But even so, I believe in\x01",
            "Ilya.\x02\x03",
            "#01302FAnd, I think the more people\x01",
            "believe in her, the more she\x01",
            "will respond to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#5PRighto...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5PThat sounds like Ilya to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PHowever, for that to\x01",
            "happen... As expected,\x01",
            "Rixia is the key, eh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE31():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BE31)
    WaitChrThread(0x105, 2)
    Sleep(150)

    ChrTalk(
        0x105,
        "#10300F#5PLloyd, can you find her?\x02",
    )

    CloseMessageWindow()

    def lambda_BE6D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE6D)
    Sleep(150)

    def lambda_BE7D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE7D)
    Sleep(50)

    def lambda_BE8D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BE8D)
    Sleep(50)

    def lambda_BE9D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BE9D)
    Sleep(50)

    def lambda_BEAD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BEAD)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x101,
        (
            "#00003F#6P...Honestly, I don't\x01",
            "know.\x02\x03",
            "#00008FIf she's seriously\x01",
            "hiding, finding her will\x01",
            "be quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PYou're right...\x02\x03",
            "#10108FLikewise, it's unclear if\x01",
            "the missing Heiyue are still\x01",
            "in the state or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PIt's also possible she went back to\x01",
            "Calvard...\x02\x03",
            "#00300FHowever, after seeing how much\x01",
            "Sullboy is counting on us, we can't\x01",
            "very well give up, now can we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah─ Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PWe should keep an eye\x01",
            "out for Heiyue as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PIn addition, I'll\x01",
            "periodically check the\x01",
            "orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#12PHaha... Thank you,\x01",
            "really.\x02\x03",
            "#01300FI'll return to the\x01",
            "nurses' station. What\x01",
            "will you do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C173():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C173)
    Sleep(150)

    def lambda_C183():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C183)
    Sleep(50)

    def lambda_C193():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C193)
    Sleep(50)

    def lambda_C1A3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C1A3)
    Sleep(50)

    def lambda_C1B3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C1B3)
    Sleep(50)

    def lambda_C1C3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C1C3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00002F#5PWell, we still have work\x01",
            "to do, so it's time to\x01",
            "say goodbye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PThank you for showing us\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01309F#12PHaha, likewise.\x02\x03",
            "#01302FThis is a terrible\x01",
            "situation, but... Let's\x01",
            "both do our best.\x02\x03",
            "But no overdoing it, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PGotcha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThank you.\x02",
    )

    CloseMessageWindow()
    OP_68(-14130, 1200, 29280, 3000)
    BeginChrThread(0x136, 1, 0, 59)
    Sleep(400)

    def lambda_C32E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C32E)
    Sleep(350)

    def lambda_C33E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C33E)
    Sleep(150)

    def lambda_C34E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C34E)
    Sleep(250)

    def lambda_C35E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C35E)
    Sleep(150)

    def lambda_C36E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C36E)
    Sleep(150)

    def lambda_C37E():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C37E)
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

    def lambda_C43D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C43D)
    Sleep(150)

    def lambda_C44D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C44D)
    Sleep(50)

    def lambda_C45D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C45D)
    Sleep(50)

    def lambda_C46D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C46D)
    Sleep(50)

    def lambda_C47D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C47D)
    Sleep(50)

    def lambda_C48D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C48D)
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
            "#00006F#6PReally... We've got to\x01",
            "brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PYes... You're right.\x02\x03",
            "#00108FAnd to take back the smiles\x01",
            "of those whose hearts and\x01",
            "bodies were wounded as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P............ (Brace\x01",
            "ourselves, huh.)\x02",
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

    # Function_49_AC62 end

    def Function_50_C626(): pass

    label("Function_50_C626")

    OP_9B(0x0, 0xFE, 0x5, 0xFA, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x5, 0xC8, 0x1F4, 0x0)
    Return()

    # Function_50_C626 end

    def Function_51_C645(): pass

    label("Function_51_C645")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1F4, 0x0)
    Return()

    # Function_51_C645 end

    def Function_52_C655(): pass

    label("Function_52_C655")

    OP_96(0x136, 0xFFFE7C08, 0x0, 0xFFFFED7C, 0x4B0, 0x0)
    Return()

    # Function_52_C655 end

    def Function_53_C66A(): pass

    label("Function_53_C66A")

    OP_95(0xFE, -97730, 0, -3800, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_53_C66A end

    def Function_54_C686(): pass

    label("Function_54_C686")

    OP_95(0xFE, -100440, 0, -7000, 1500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_C686 end

    def Function_55_C6A2(): pass

    label("Function_55_C6A2")

    OP_95(0xFE, -101020, 0, -6010, 1500, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_C6A2 end

    def Function_56_C6BE(): pass

    label("Function_56_C6BE")

    OP_95(0xFE, -98500, 0, -3400, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_56_C6BE end

    def Function_57_C6DA(): pass

    label("Function_57_C6DA")

    OP_95(0xFE, -99600, 0, -3350, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_57_C6DA end

    def Function_58_C6F6(): pass

    label("Function_58_C6F6")

    OP_95(0xFE, -100570, 0, -4650, 1500, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_58_C6F6 end

    def Function_59_C712(): pass

    label("Function_59_C712")

    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xBB8, 0x7D0, 0x1)
    Return()

    # Function_59_C712 end

    def Function_60_C75E(): pass

    label("Function_60_C75E")

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
            "#11POh...?\x02\x03",
            "Who is it? You can come in.\x02",
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
        "#00204F#6P...Excuse us.\x02",
    )

    CloseMessageWindow()
    OP_68(-97660, 1000, -3500, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_C953():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C953)

    def lambda_C968():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C968)
    Sleep(100)

    def lambda_C97C():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C97C)

    def lambda_C991():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C991)
    Sleep(100)

    def lambda_C9A5():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C9A5)

    def lambda_C9BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C9BA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x5, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#11602F#11POh, it's Tio and...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#11605F#11PHuh, little bro!?\x02\x03",
            "#11602FAnd you... Wazy, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5PYeah, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PIlya... It really has\x01",
            "been a long time.\x02\x03",
            "#00006FI'm sorry, we came to\x01",
            "visit empty-handed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609F#11POh, jeez! Don't worry\x01",
            "about stuff like that!\x02\x03",
            "#11602FNow now, you three. Come\x01",
            "here.\x02\x03",
            "#11605FOh, you can help\x01",
            "yourselves to sweets\x01",
            "from the fans, alright?\x02\x03",
            "#11609FI think the cookies\x01",
            "haven't expired yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PExcuse us, then.\x02",
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
            "#11603F#11PI see... So you guys\x01",
            "have it tough too.\x02\x03",
            "#11601FI heard terrible things\x01",
            "were happening to\x01",
            "Crossbell itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6PWell, unthinkable is the\x01",
            "only word you could use to\x01",
            "describe the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11PHmm. It's frustrating\x01",
            "not being able to\x01",
            "walk...\x02\x03",
            "#11608FI'd like to see how Arc-\x01",
            "en-Ciel is doing with my\x01",
            "own eyes, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WUmm, Ilya.\x02\x03",
            "#00008FAbout your condition,\x01",
            "umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11605F#11PAh, yes.\x02\x03",
            "#11603FDr. Seiland says she\x01",
            "doesn't yet know if I'll\x01",
            "ever walk again.\x02\x03",
            "#11600FShe didn't say it was\x01",
            "100% impossible, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#40W...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11POh, come on. If you make that face, I'll\x01",
            "get depressed too, you know.\x02\x03",
            "#11601FNow look here─ If you think something's\x01",
            "impossible, any chance you may have had\x01",
            "will disappear just like that, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604F#11PIt's the same with the\x01",
            "stage... There's an "answer"\x01",
            "out there. Definitely.\x02\x03",
            "#11600FNo matter how painful, no\x01",
            "matter how hopeless, there's\x01",
            "always a ray of hope.\x02\x03",
            "#11609FAs long as you don't give\x01",
            "up, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6P...You're amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11PUuhm, I don't think I'm so\x01",
            "amazing.\x02\x03",
            "#11601FFrom what I've heard, you\x01",
            "guys are the ones who have\x01",
            "it tough. Am I wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...Thinking about it normally,\x01",
            "there's an awfully difficult\x01",
            "journey ahead of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604F#11PIt's the same for me.\x01",
            "Exactly.\x02\x03",
            "#11600FMan is a creature that can\x01",
            "do anything as long as it's\x01",
            "for what's important to him.\x02\x03",
            "It's different from person\x01",
            "to person... But I think\x01",
            "that's man's strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PThe creature called\x01",
            "man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11602F#11PAmong them, I think I'm\x01",
            "one of the greediest,\x01",
            "though.\x02\x03",
            "Even so, I think others\x01",
            "are basically the same.\x02\x03",
            "#11604FEven our troupe members...\x02\x01",
            "#11600Fand Rixia as well, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F#6PIlya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11602F#11PHaha. If you see her, can\x01",
            "you pass this along for\x01",
            "me?\x02\x03",
            "#11604F"─What's the most\x01",
            "precious thing to you?"\x02\x03",
            ""Can you be in front of\x01",
            "that precious thing and\x01",
            "not do your best for it?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P...Understood.\x02\x03",
            "#00000FIf we see Rixia, we'll\x01",
            "be sure to tell her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609F#11PAlright. I'm counting on\x01",
            "you!\x02",
        )
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

    # Function_60_C75E end

    def Function_61_D652(): pass

    label("Function_61_D652")

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

    def lambda_D6EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D6EE)

    def lambda_D703():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D703)
    Sleep(50)

    def lambda_D71B():
        OP_9B(0x0, 0xFE, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D71B)
    Sleep(50)
    Sleep(50)
    Sleep(100)

    def lambda_D739():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D739)

    def lambda_D74A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D74A)
    Sleep(400)

    def lambda_D75E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D75E)
    Sleep(800)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    OP_0D()

    def lambda_D785():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D785)
    Sleep(50)

    def lambda_D795():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D795)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10404F#12PHaha... Really, she's\x01",
            "incredible.\x02\x03",
            "#10402FShe's called the Flame\x01",
            "Dancer for a reason,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5P...Rather, she might be\x01",
            "the Sun Princess\x01",
            "herself.\x02\x03",
            "#00208FSince I was brought\x01",
            "here, I've spoken with\x01",
            "her many times...\x02\x03",
            "#00202FIlya and Cecil really\x01",
            "cheered me up a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00008F...I really hope we find\x01",
            "Rixia as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, if it is the\x01",
            "Goddess' will.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_D9C1")

    ChrTalk(
        0x103,
        (
            "#00202F#5PShall we head back and\x01",
            "speak with Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_DA3E")

    label("loc_D9C1")


    ChrTalk(
        0x103,
        (
            "#00202F#5PShall pay a visit to\x01",
            "Inspector Donovan as\x01",
            "well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16500, 0, 30000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_DA3E")

    Return()

    # Function_61_D652 end

    def Function_62_DA3F(): pass

    label("Function_62_DA3F")

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
        (
            "#6PMy, it's time to take\x01",
            "your temperature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please, come in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P...Excuse us.\x02",
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

    def lambda_DBBA():
        OP_95(0x101, -53180, 0, -49830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBBA)

    def lambda_DBD4():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBD4)
    Sleep(500)

    def lambda_DBE8():
        OP_95(0x105, -53100, 0, -50830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBE8)

    def lambda_DC02():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DC02)
    Sleep(600)

    def lambda_DC16():
        OP_95(0x103, -51840, 50, -50110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC16)

    def lambda_DC30():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DC30)
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
            "Oh, if it isn't the\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PHaha. Long time no see,\x01",
            "Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10405F#12PHuh? Who's the beautiful\x01",
            "lady over there?\x02\x03",
            "#10409FHaha. Might we be\x01",
            "interrupting something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "We just reunited with\x01",
            "each other. What are you\x01",
            "saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PNow look here, Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#2PShe is Mrs. Fara,\x01",
            "Inspector Donovan's\x01",
            "wife.\x02\x03",
            "She came visit him a\x01",
            "while back and has been\x01",
            "staying here ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PUhuhu, nice to meet you.\x01",
            "Thank you for taking such\x01",
            "good care of my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PI hear stories about you every now\x01",
            "and then from my husband and Tio. You\x01",
            "all seem like interesting people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHaha. You flatter us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P(I don't think that's\x01",
            "flattery, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have a great deal of things to\x01",
            "talk about, but... For starters,\x01",
            "could you explain the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes, of course.\x02",
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
            "#1PHmm... Things are worse\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PAnd, I suppose I shouldn't\x01",
            "report what I've heard to\x01",
            "HQ, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PYes, that would be a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, I don't really care\x01",
            "either way, since Lloyd's\x01",
            "the wanted criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6PMy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PA-Anyway. ...Inspector,\x01",
            "what's the situation\x01",
            "inside Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWell, I only heard about\x01",
            "it from Raymond who came\x01",
            "to visit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PThe Crossbell Police have\x01",
            "been completely absorbed as\x01",
            "a branch of the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1POur duties haven't changed, but it\x01",
            "looks like we're doing nothing but\x01",
            "odd jobs within the city at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI thought that might be\x01",
            "the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, considering the\x01",
            "situation, it probably\x01",
            "can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PBut... Wasn't there any push-back\x01",
            "against that?\x02\x03",
            "#00003FSetting aside Vice Chief Pierre, I\x01",
            "can't think that Chief Sergei or Mr.\x01",
            "Dudley silently went along with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWell, just between you\x01",
            "and me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIt seems Sergei, Dudley,\x01",
            "Raymond and the other officers\x01",
            "are acting in secret.\x02",
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
        (
            "#00205FThe chief and the others\x01",
            "are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PIn absolute secrecy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PThey're biding their time, and\x01",
            "looking for a way to break out\x01",
            "of the current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PSo remaining silent was\x01",
            "just part of their plan,\x01",
            "eh?\x02\x03",
            "#10404FHaha. I guess there's\x01",
            "hope, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah. They seem difficult to\x01",
            "contact for now. It seems best\x01",
            "to leave the city to them.\x02\x03",
            "#00003FWe should look for our own way\x01",
            "to break through this\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PThat's just what I'd\x01",
            "expect from you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PReality is a harsh\x01",
            "mistress, but do your\x01",
            "best, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIf I make it back to\x01",
            "Crossbell City, I'll meet up\x01",
            "with Sergei and the others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PNow, now, dear... For now, you'll\x01",
            "leave things to Lloyd, Raymond and the\x01",
            "others and focus on getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PI will absolutely not allow you to\x01",
            "do anything reckless until you've\x01",
            "made a full recovery, you hear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1PH-Hmph... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Haha... So that's how\x01",
            "she really feels.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(It looks like even the\x01",
            "inspector is no match\x01",
            "for his wife.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12P(Haha. The inspector is\x01",
            "blessed with such a good\x01",
            "wife.)\x02",
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

    # Function_62_DA3F end

    def Function_63_EA12(): pass

    label("Function_63_EA12")

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

    def lambda_EAFF():
        OP_95(0x101, -15360, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EAFF)

    def lambda_EB19():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB19)
    Sleep(600)

    def lambda_EB2D():
        OP_95(0x103, -14800, 0, 7940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EB2D)

    def lambda_EB47():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EB47)
    Sleep(600)

    def lambda_EB5B():
        OP_95(0x105, -14980, 0, 10240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB5B)

    def lambda_EB75():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EB75)
    Sleep(1200)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0x8,
        "Ah, everyooone.\x02",
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

    def lambda_EBEA():

        label("loc_EBEA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_EBEA")

    QueueWorkItem2(0x101, 2, lambda_EBEA)

    def lambda_EBFC():

        label("loc_EBFC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_EBFC")

    QueueWorkItem2(0x105, 2, lambda_EBFC)

    def lambda_EC0E():

        label("loc_EC0E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_EC0E")

    QueueWorkItem2(0x103, 2, lambda_EC0E)
    OP_95(0x8, -13480, 0, 9000, 3000, 0x0)
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, Fran... Have you\x01",
            "finished packing your\x01",
            "things?\x02",
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
        "Yes, as you can see!\x02",
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
            "#00202F#6PIt's been a while since\x01",
            "I saw Fran in her\x01",
            "uniform as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01909F#11PHaha. It's the same for\x01",
            "me.\x02\x03",
            "#01900FEveryone, have you\x01",
            "visited Inspector\x01",
            "Donovan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, we just finished.\x02\x03",
            "#00000FAre you going to visit\x01",
            "him too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01904F#11PYes. I thought I would say\x01",
            "goodbye to everyone before\x01",
            "leaving the hospital.\x02\x03",
            "#01902FEspecially to the\x01",
            "inspector. I have to thank\x01",
            "him again for saving me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PI see. Well, see you\x01",
            "later, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01909F#11PYes, lateeer!\x02",
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

    def lambda_EF9C():
        OP_95(0xFE, -19090, 0, 8900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EF9C)

    def lambda_EFB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_EFB6)
    WaitChrThread(0x8, 2)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_EFE2():
        OP_95(0xFE, -16200, 0, 8800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EFE2)
    Sleep(50)

    def lambda_EFFF():
        OP_95(0xFE, -14800, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EFFF)
    Sleep(50)

    def lambda_F01C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F01C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    SetScenarioFlags(0x1A1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_END)), "loc_F0CB")

    ChrTalk(
        0x105,
        (
            "#10402F#5PThen, shall we return to\x01",
            "the Merkabah after she\x01",
            "finishes saying goodbye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F144")

    label("loc_F0CB")


    ChrTalk(
        0x105,
        (
            "#10402F#5PThen, shall we go visit\x01",
            "Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
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

    label("loc_F144")

    Return()

    # Function_63_EA12 end

    def Function_64_F145(): pass

    label("Function_64_F145")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xE1, 0x320, 0x3E8, 0x0)

    def lambda_F160():

        label("loc_F160")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F160")

    QueueWorkItem2(0xFE, 2, lambda_F160)
    Return()

    # Function_64_F145 end

    def Function_65_F16E(): pass

    label("Function_65_F16E")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xA0, 0x5DC, 0x3E8, 0x0)

    def lambda_F189():

        label("loc_F189")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F189")

    QueueWorkItem2(0xFE, 2, lambda_F189)
    Return()

    # Function_65_F16E end

    def Function_66_F197(): pass

    label("Function_66_F197")

    Sleep(1850)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    Return()

    # Function_66_F197 end

    def Function_67_F1AA(): pass

    label("Function_67_F1AA")

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
            "#01400F...Sergei, it appears\x01",
            "you've taken over the\x01",
            "Cryptids case.\x02\x03",
            "#01403FNormally I, as bracer,\x01",
            "would go investigate and\x01",
            "exterminate them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01000FNo need to worry.\x02\x03",
            "#01003FRegarding the cryptids, we\x01",
            "divided the work and made a\x01",
            "plan for dealing with them.\x02\x03",
            "#01000FWell, just leave it to\x01",
            "those guys for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01408FHowever...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01002FWell, they've grown up\x01",
            "too, you don't have worry\x01",
            "about them so much.\x02\x03",
            "#01004FAnd, it's normally hard\x01",
            "for you to come visit\x01",
            "her, right?\x02\x03",
            "#01002FAs her father, it's your\x01",
            "duty to be by her side at\x01",
            "a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01403F...I'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11209FHaha... Thank you very\x01",
            "much, Chief.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 160, -1, -1)
    SetChrName("Lloyd's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Excuse us.\x07\x00\x02",
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

    def lambda_F5FF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_F5FF)
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
        "#01405FYou all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#01005FWhat, you came?\x02\x03",
            "#01006FJeez. I told you, because\x01",
            "we're busy, I alone would\x01",
            "visit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FS-Sorry, Chief.\x02\x03",
            "#00000FWe couldn't help but\x01",
            "worry about how Shizuku\x01",
            "was doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FHaha, everyone... Thank\x01",
            "you for coming.\x02",
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
        (
            "#6P#00105FShizuku, your eyes are\x01",
            "open...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FUmm, could it be that\x01",
            "you can see...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P#11208F...No, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F...In this surgery, Dr.\x01",
            "Seiland did her very best as\x01",
            "the operating surgeon.\x02\x03",
            "#01400FThe surgery was a success,\x01",
            "but... It's not a full\x01",
            "recovery.\x02\x03",
            "#01408FIt seems that she has finally\x01",
            "recovered to a degree that she\x01",
            "can perceive light around her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FI... see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FWhat can I say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11200FHaha. Please don't worry\x01",
            "about it. I'm fine, you\x01",
            "see.\x02\x03",
            "#11202FMore importantly, father...\x01",
            "I would like to go on the\x01",
            "roof with everyone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)

    ChrTalk(
        0x19,
        (
            "#6P#01002FYeah, that would be nice.\x02\x03",
            "#01004FThere's also so many people in this\x01",
            "hospital room that you probably\x01",
            "want to breathe some fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FB-But, Shizuku, you just\x01",
            "had surgery, so you\x01",
            "shouldn't overdo it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F...Well according to the doctor, there won't\x01",
            "be that much of a negative effect unless she's\x01",
            "exposed to strong light for a long time.\x02\x03",
            "#01400FWith today's weather, there shouldn't be any\x01",
            "problems if she goes outside for a while.\x02\x03",
            "#01403F...I'll go get permission. I'm sorry, but help\x01",
            "Shizuku get ready.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FCB7():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_FCB7)

    def lambda_FCD1():

        label("loc_FCD1")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FCD1")

    QueueWorkItem2(0x19, 2, lambda_FCD1)

    def lambda_FCE3():

        label("loc_FCE3")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FCE3")

    QueueWorkItem2(0x101, 2, lambda_FCE3)

    def lambda_FCF5():

        label("loc_FCF5")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FCF5")

    QueueWorkItem2(0x102, 2, lambda_FCF5)

    def lambda_FD07():

        label("loc_FD07")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FD07")

    QueueWorkItem2(0x103, 2, lambda_FD07)

    def lambda_FD19():

        label("loc_FD19")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FD19")

    QueueWorkItem2(0x104, 2, lambda_FD19)

    def lambda_FD2B():

        label("loc_FD2B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FD2B")

    QueueWorkItem2(0x109, 2, lambda_FD2B)

    def lambda_FD3D():

        label("loc_FD3D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_FD3D")

    QueueWorkItem2(0x105, 2, lambda_FD3D)
    BeginChrThread(0x1A, 1, 0, 74)
    WaitChrThread(0xF, 1)

    def lambda_FD59():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_FD59)

    def lambda_FD73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_FD73)
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
        "#00105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FOh man. Even that Divine\x01",
            "Blade of Wind seems to\x01",
            "be soft on his daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11209FFather is always very\x01",
            "kind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FE43():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FE43)
    Sleep(50)

    def lambda_FE53():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FE53)
    Sleep(50)

    def lambda_FE63():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FE63)
    Sleep(50)

    def lambda_FE73():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FE73)
    Sleep(50)

    def lambda_FE83():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FE83)
    Sleep(50)

    def lambda_FE93():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FE93)
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
            "#01004FWell that being the case,\x01",
            "seeing as you're here and\x01",
            "all, why don't you join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes... You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FHaha. Thank you\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_67_F1AA end

    def Function_68_FF7C(): pass

    label("Function_68_FF7C")


    def lambda_FF81():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF81)

    def lambda_FF9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF9B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_FFB4():
        OP_95(0xFE, -99000, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFB4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_68_FF7C end

    def Function_69_FFD5(): pass

    label("Function_69_FFD5")


    def lambda_FFDA():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFDA)

    def lambda_FFF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFF4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1000D():
        OP_95(0xFE, -100940, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1000D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_69_FFD5 end

    def Function_70_1002E(): pass

    label("Function_70_1002E")


    def lambda_10033():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10033)

    def lambda_1004D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1004D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_10066():
        OP_95(0xFE, -98340, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10066)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_1002E end

    def Function_71_10087(): pass

    label("Function_71_10087")


    def lambda_1008C():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1008C)

    def lambda_100A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100A6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_100BF():
        OP_95(0xFE, -100740, 0, 51800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100BF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_71_10087 end

    def Function_72_100E0(): pass

    label("Function_72_100E0")


    def lambda_100E5():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100E5)

    def lambda_100FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100FF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_10118():
        OP_95(0xFE, -99240, 0, 50800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10118)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_100E0 end

    def Function_73_10139(): pass

    label("Function_73_10139")


    def lambda_1013E():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1013E)

    def lambda_10158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10158)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_10171():
        OP_95(0xFE, -100740, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10171)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_73_10139 end

    def Function_74_10192(): pass

    label("Function_74_10192")

    Sleep(2600)
    Sound(107, 0, 100, 0)
    Sleep(1100)
    Sound(107, 0, 100, 0)
    Return()

    # Function_74_10192 end

    def Function_75_101A5(): pass

    label("Function_75_101A5")

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
            "#12P#01002F...Then, it's about time\x01",
            "I returned to the\x01",
            "Support Section.\x02\x03",
            "#01004FArios, stay with Shizuku\x01",
            "for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F...Yeah, I'll do just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThank you for your hard\x01",
            "work, Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "#01005FYeah, continue your investigation\x01",
            "of the Cryptids.\x02\x03",
            "#01002FWhile the Divine Blade of Wind\x01",
            "can't act, you've gotta put up the\x01",
            "best results you possibly can.\x02",
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
        "#6P#00106FC-Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#01004FHehe, later then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    ChrTalk(
        0xD,
        (
            "#5P#11202FTh... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)
    Sleep(500)
    OP_93(0x19, 0xB4, 0x1F4)

    def lambda_10543():
        OP_95(0xFE, -99820, 0, 54000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10543)
    WaitChrThread(0x19, 1)

    def lambda_10561():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10561)

    def lambda_1057B():

        label("loc_1057B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_1057B")

    QueueWorkItem2(0xF, 2, lambda_1057B)

    def lambda_1058D():

        label("loc_1058D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_1058D")

    QueueWorkItem2(0x101, 2, lambda_1058D)

    def lambda_1059F():

        label("loc_1059F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_1059F")

    QueueWorkItem2(0x102, 2, lambda_1059F)

    def lambda_105B1():

        label("loc_105B1")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_105B1")

    QueueWorkItem2(0x103, 2, lambda_105B1)

    def lambda_105C3():

        label("loc_105C3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_105C3")

    QueueWorkItem2(0x104, 2, lambda_105C3)

    def lambda_105D5():

        label("loc_105D5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_105D5")

    QueueWorkItem2(0x109, 2, lambda_105D5)

    def lambda_105E7():

        label("loc_105E7")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_105E7")

    QueueWorkItem2(0x105, 2, lambda_105E7)
    Sleep(1500)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_10606():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10606)

    def lambda_10620():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_10620)
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
            "#5P#00306FOh man. What a thing to\x01",
            "say in front of the\x01",
            "Divine Blade of Wind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHehe, he never changes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01402FHehe. There's no doubt he's\x01",
            "the same excellent boss from\x01",
            "my days in the police.\x02\x03",
            "#01403F...I'm counting on your help\x01",
            "in the Cryptids investigation\x01",
            "as well.\x02\x03",
            "#01400FI plan to return tomorrow and\x01",
            "join it, but until then, help\x01",
            "out Scott and the others.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_107E2():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_107E2)
    Sleep(50)

    def lambda_107F2():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_107F2)
    Sleep(50)

    def lambda_10802():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10802)
    Sleep(50)

    def lambda_10812():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10812)
    Sleep(50)

    def lambda_10822():
        TurnDirection(0x105, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10822)
    Sleep(50)

    def lambda_10832():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10832)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00200FAlright, we'll do what\x01",
            "we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FReally, thank you\x01",
            "everyone.\x02\x03",
            "#11209FWe got to talk about a\x01",
            "lot of different things.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_108E9():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_108E9)
    Sleep(50)

    def lambda_108F9():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_108F9)
    Sleep(50)

    def lambda_10909():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10909)
    Sleep(50)

    def lambda_10919():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10919)
    Sleep(50)

    def lambda_10929():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10929)
    Sleep(50)

    def lambda_10939():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10939)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#12P#10100FNo, we had a great time\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe'll come again, so be\x01",
            "well.\x02",
        )
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

    # Function_75_101A5 end

    def Function_76_10A09(): pass

    label("Function_76_10A09")

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
            "#00005FHuh? This is Shizuku's\x01",
            "room, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FMaybe she's out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FBut, we didn't see her\x01",
            "in this ward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FWell if ya feel like it,\x01",
            "why not try lookin' for\x01",
            "her?\x02",
        )
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

    # Function_76_10A09 end

    def Function_77_10C48(): pass

    label("Function_77_10C48")

    StopBGM(0xBB8)

    ChrTalk(
        0xB,
        "#11603FBy the way─\x02",
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
            "#11602F...A certain someone\x01",
            "over there seems to\x01",
            "still be worried, eh?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10DF9")
    SetChrPos(0x109, -100670, 0, -7660, 90)
    Jump("loc_10E40")

    label("loc_10DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E1F")
    SetChrPos(0x105, -100670, 0, -7660, 90)
    Jump("loc_10E40")

    label("loc_10E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E40")
    SetChrPos(0x10A, -100670, 0, -7660, 90)

    label("loc_10E40")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00005FI-Ilya...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhat're you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11604FHehe, I don't know who it is, but they\x01",
            "seem to be a very, very shy person.\x02\x03",
            "#11609FAlthough, they probably have a\x01",
            "reserved personality, can be whimsical\x01",
            "at times and have an outrageous body㈱\x02",
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
        "#12P#00306F(Well...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F(She completely\x01",
            "recognized her.)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10708F#3C#40W#2S............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#11603F─I don't know who they are,\x01",
            "but I've already started\x01",
            "rehabilitation.\x02\x03",
            "#11601FIf this person misses too much\x01",
            "practice, I'll immediately\x01",
            "catch up and surpass them.\x02\x03",
            "#11604FIf this person doesn't want to\x01",
            "be left behind, they had best\x01",
            "go settle things quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10717F#3C#40W#2S............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#11P#11604FAlso, they have to be very\x01",
            "careful.\x02\x03",
            "#11600FNo matter how strong she is,\x01",
            "this person has to keep in\x01",
            "mind that she's a woman.\x02\x03",
            "#11603FJust like on our stage,\x01",
            "there's also a strength that\x01",
            "only a woman can show...\x02\x03",
            "#11600FAnd I'm sure that strength\x01",
            "will protect you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10715F#3C#40W#2S............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00102FIlya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#11604FHehe, I took up a lot of\x01",
            "your spare time, haven't\x01",
            "I.\x02\x03",
            "#11600F─Little bro, guys, you be\x01",
            "careful too. Don't you go\x01",
            "making Cecil sad, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FGotcha!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11514")
    BeginChrThread(0x109, 1, 0, 79)
    WaitChrThread(0x109, 1)
    Jump("loc_1154D")

    label("loc_11514")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11533")
    BeginChrThread(0x105, 1, 0, 79)
    WaitChrThread(0x105, 1)
    Jump("loc_1154D")

    label("loc_11533")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1154D")
    BeginChrThread(0x10A, 1, 0, 79)
    WaitChrThread(0x10A, 1)

    label("loc_1154D")

    Sleep(2500)
    EndChrThread(0x106, 0x1)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0x106,
        "#10715F#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FUhmm... Sorry.\x02\x03",
            "#00008FI didn't think she'd\x01",
            "notice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYou completely concealed\x01",
            "your presence, and yet\x01",
            "she...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#30WHaha... Ilya is a genius,\x01",
            "after all...\x02\x03",
            "#10704F#30WFrom my faint respiration\x01",
            "and footsteps, she probably\x01",
            "knew immediately.\x02\x03",
            "Synchronizing breathing is\x01",
            "something we do on stage all\x01",
            "the time...\x02\x03",
            "#10716F#30WHonestly... Except for when\x01",
            "it comes to the stage, she's\x01",
            "lazy and irresponsible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00204FReally... Ilya is Ilya.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117B9")

    ChrTalk(
        0x109,
        (
            "#6P#10109F*chuckle*... But...I'm\x01",
            "glad for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1185B")

    label("loc_117B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11806")

    ChrTalk(
        0x105,
        (
            "#6P#10409FHehe... I keep getting\x01",
            "surprised by her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1185B")

    label("loc_11806")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1185B")

    ChrTalk(
        0x10A,
        (
            "#6P#00602FHmph... Nothing less\x01",
            "expected from Ilya, I\x01",
            "could say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1185B")

    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    OP_93(0x106, 0x10E, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10704FThis has strengthened my\x01",
            "resolve as well.\x02\x03",
            "#10702FLet's go, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FRight!\x02",
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

    # Function_77_10C48 end

    def Function_78_1193F(): pass

    label("Function_78_1193F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1197B")
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(500)
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(800)
    Jump("Function_78_1193F")

    label("loc_1197B")

    Return()

    # Function_78_1193F end

    def Function_79_1197C(): pass

    label("Function_79_1197C")

    SetChrPos(0xFE, -16470, 0, 25770, 0)

    def lambda_11992():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11992)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119C2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 80)
    Jump("loc_11A4D")

    label("loc_119C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119E6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 81)
    Jump("loc_11A4D")

    label("loc_119E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 82)
    Jump("loc_11A4D")

    label("loc_11A0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A2E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 83)
    Jump("loc_11A4D")

    label("loc_11A2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A4D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 84)

    label("loc_11A4D")

    Return()

    # Function_79_1197C end

    def Function_80_11A4E(): pass

    label("Function_80_11A4E")

    OP_95(0xFE, -16340, 0, 28470, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 29900, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_80_11A4E end

    def Function_81_11A7E(): pass

    label("Function_81_11A7E")

    OP_95(0xFE, -16360, 0, 29870, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 31030, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_81_11A7E end

    def Function_82_11AAE(): pass

    label("Function_82_11AAE")

    OP_95(0xFE, -16400, 0, 27970, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 28800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_82_11AAE end

    def Function_83_11ADE(): pass

    label("Function_83_11ADE")

    OP_95(0xFE, -16360, 0, 30550, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_83_11ADE end

    def Function_84_11AFA(): pass

    label("Function_84_11AFA")

    OP_95(0xFE, -16360, 0, 29320, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_84_11AFA end

    def Function_85_11B16(): pass

    label("Function_85_11B16")

    StopBGM(0x7D0)
    Sleep(2000)
    Sleep(10)
    PlayBGM("ed7563", 0)
    Return()

    # Function_85_11B16 end

    def Function_86_11B26(): pass

    label("Function_86_11B26")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xB, 0x2)
    OP_68(-98530, 900, -5100, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_11C28")
    SetChrPos(0x101, -99960, 0, -5280, 90)
    SetChrPos(0x102, -99960, 0, -6600, 90)
    SetChrPos(0x103, -100870, 0, -4700, 90)
    SetChrPos(0x104, -100870, 0, -6000, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BD2")
    SetChrPos(0x109, -100670, 0, -7360, 90)
    Jump("loc_11C19")

    label("loc_11BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BF8")
    SetChrPos(0x105, -100670, 0, -7360, 90)
    Jump("loc_11C19")

    label("loc_11BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C19")
    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_11C19")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_11DA5")

    label("loc_11C28")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -99960, 0, -6000, 90)
    SetChrPos(0x102, -99960, 0, -4700, 90)
    SetChrPos(0x103, -99960, 0, -7360, 90)
    SetChrPos(0x104, -100870, 0, -4700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11CA1")
    SetChrPos(0x109, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11CF1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CE0")
    SetChrPos(0x105, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11CF1")

    label("loc_11CE0")

    SetChrPos(0x105, -100670, 0, -7360, 90)

    label("loc_11CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11D41")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D30")
    SetChrPos(0x106, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D41")

    label("loc_11D30")

    SetChrPos(0x106, -100670, 0, -7360, 90)

    label("loc_11D41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11D91")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D80")
    SetChrPos(0x10A, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D91")

    label("loc_11D80")

    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_11D91")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_11DA5")

    OP_0D()

    ChrTalk(
        0xB,
        (
            "#11P#11600FOh, right, little\x01",
            "brother... Can you take\x01",
            "this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x39F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000FThis is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11600FIt's the hair ornament I was wearing\x01",
            "when I was standing on the stage as the\x01",
            "main protagonist for the first time.\x02\x03",
            "#11604FI was always carrying it with me to not\x01",
            "forget my initial resolution.\x02\x03",
            "#11609FHehe, don't you think it's a rare\x01",
            "article for enthusiasts?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FF7")
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_11FF7")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(Indeed, seems that there\x01",
            "would be guys who would want\x01",
            "this no matter the price...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FB-But... Can I really\x01",
            "have such an important\x01",
            "item?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11604FHehe, it's fine, it's\x01",
            "fine. It's a gift for all\x01",
            "you've done until now.\x02\x03",
            "#11600FIf you want, you can\x01",
            "carry it as a charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00002F...Thank you very much.\x01",
            "I'll cherish it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_12178")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_1218C")

    label("loc_12178")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1218C")

    SetChrPos(0x0, -100140, 0, -6120, 90)
    SetScenarioFlags(0x1AD, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_121BC")
    OP_E0(0x34, 0x0)

    label("loc_121BC")

    EventEnd(0x5)
    Return()

    # Function_86_11B26 end

    def Function_87_121BF(): pass

    label("Function_87_121BF")

    EventBegin(0x1)
    Call(0, 92)
    SetChrPos(0x0, -13440, 0, 8760, 89)
    EventEnd(0x4)
    Return()

    # Function_87_121BF end

    def Function_88_121D8(): pass

    label("Function_88_121D8")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121EC")
    Call(0, 92)
    Jump("loc_121EF")

    label("loc_121EC")

    Call(0, 94)

    label("loc_121EF")

    SetChrPos(0x0, -9210, 0, 13390, 180)
    EventEnd(0x4)
    Return()

    # Function_88_121D8 end

    def Function_89_12203(): pass

    label("Function_89_12203")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12217")
    Call(0, 94)
    Jump("loc_1221A")

    label("loc_12217")

    Call(0, 93)

    label("loc_1221A")

    SetChrPos(0x0, 1350, 0, 80, 89)
    EventEnd(0x4)
    Return()

    # Function_89_12203 end

    def Function_90_1222E(): pass

    label("Function_90_1222E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12242")
    Call(0, 94)
    Jump("loc_12245")

    label("loc_12242")

    Call(0, 93)

    label("loc_12245")

    SetChrPos(0x0, -5500, 0, 12500, 225)
    EventEnd(0x4)
    Return()

    # Function_90_1222E end

    def Function_91_12259(): pass

    label("Function_91_12259")

    EventBegin(0x1)
    Call(0, 93)
    SetChrPos(0x0, -19350, 0, 29820, 89)
    EventEnd(0x4)
    Return()

    # Function_91_12259 end

    def Function_92_12272(): pass

    label("Function_92_12272")


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
    Return()

    # Function_92_12272 end

    def Function_93_122BD(): pass

    label("Function_93_122BD")


    ChrTalk(
        0x136,
        (
            "#01300FIlya's room is no. 303.\x02\x03",
            "I don't think it will take\x01",
            "much time, so I wonder if\x01",
            "we can go there now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYou're right, got it.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_93_122BD end

    def Function_94_12350(): pass

    label("Function_94_12350")


    ChrTalk(
        0x136,
        (
            "#01300FRoom 302 is Mr. Donovan's.\x02\x03",
            "I don't think it will take\x01",
            "much time, so I wonder if\x01",
            "we can go there now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYou're right, got it.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_94_12350 end

    SaveToFile()

Try(main)
