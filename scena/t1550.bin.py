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
        "Function_13_1B55",        # 0D, 13
        "Function_14_1CEA",        # 0E, 14
        "Function_15_1DB8",        # 0F, 15
        "Function_16_1EF0",        # 10, 16
        "Function_17_1FBF",        # 11, 17
        "Function_18_210C",        # 12, 18
        "Function_19_2A75",        # 13, 19
        "Function_20_2E00",        # 14, 20
        "Function_21_3542",        # 15, 21
        "Function_22_3CBD",        # 16, 22
        "Function_23_3E88",        # 17, 23
        "Function_24_5208",        # 18, 24
        "Function_25_53A8",        # 19, 25
        "Function_26_573E",        # 1A, 26
        "Function_27_65A6",        # 1B, 27
        "Function_28_6A17",        # 1C, 28
        "Function_29_70DF",        # 1D, 29
        "Function_30_7476",        # 1E, 30
        "Function_31_75C2",        # 1F, 31
        "Function_32_76D7",        # 20, 32
        "Function_33_7BEF",        # 21, 33
        "Function_34_7CE1",        # 22, 34
        "Function_35_7E77",        # 23, 35
        "Function_36_84C7",        # 24, 36
        "Function_37_8DCB",        # 25, 37
        "Function_38_8DD2",        # 26, 38
        "Function_39_900D",        # 27, 39
        "Function_40_9075",        # 28, 40
        "Function_41_A503",        # 29, 41
        "Function_42_A538",        # 2A, 42
        "Function_43_A55E",        # 2B, 43
        "Function_44_A58A",        # 2C, 44
        "Function_45_A5B0",        # 2D, 45
        "Function_46_A5E5",        # 2E, 46
        "Function_47_A60B",        # 2F, 47
        "Function_48_B013",        # 30, 48
        "Function_49_B01D",        # 31, 49
        "Function_50_CA80",        # 32, 50
        "Function_51_CA9F",        # 33, 51
        "Function_52_CAAF",        # 34, 52
        "Function_53_CAC4",        # 35, 53
        "Function_54_CAE0",        # 36, 54
        "Function_55_CAFC",        # 37, 55
        "Function_56_CB18",        # 38, 56
        "Function_57_CB34",        # 39, 57
        "Function_58_CB50",        # 3A, 58
        "Function_59_CB6C",        # 3B, 59
        "Function_60_CBB8",        # 3C, 60
        "Function_61_DB4E",        # 3D, 61
        "Function_62_DF54",        # 3E, 62
        "Function_63_EFF3",        # 3F, 63
        "Function_64_F758",        # 40, 64
        "Function_65_F781",        # 41, 65
        "Function_66_F7AA",        # 42, 66
        "Function_67_F7BD",        # 43, 67
        "Function_68_105AB",       # 44, 68
        "Function_69_10604",       # 45, 69
        "Function_70_1065D",       # 46, 70
        "Function_71_106B6",       # 47, 71
        "Function_72_1070F",       # 48, 72
        "Function_73_10768",       # 49, 73
        "Function_74_107C1",       # 4A, 74
        "Function_75_107D4",       # 4B, 75
        "Function_76_1104C",       # 4C, 76
        "Function_77_11298",       # 4D, 77
        "Function_78_11FB5",       # 4E, 78
        "Function_79_11FF2",       # 4F, 79
        "Function_80_120C4",       # 50, 80
        "Function_81_120F4",       # 51, 81
        "Function_82_12124",       # 52, 82
        "Function_83_12154",       # 53, 83
        "Function_84_12170",       # 54, 84
        "Function_85_1218C",       # 55, 85
        "Function_86_1219C",       # 56, 86
        "Function_87_1283E",       # 57, 87
        "Function_88_12857",       # 58, 88
        "Function_89_12882",       # 59, 89
        "Function_90_128AD",       # 5A, 90
        "Function_91_128D8",       # 5B, 91
        "Function_92_128F1",       # 5C, 92
        "Function_93_1293C",       # 5D, 93
        "Function_94_129D6",       # 5E, 94
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
    Jump("loc_1B51")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1389")
    Call(0, 27)
    Jump("loc_1B51")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")
    Call(0, 27)
    Jump("loc_1B51")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1549")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1514")

    ChrTalk(
        0xD,
        (
            "#11205F...Oh, that's right...\x02\x03",
            "#11203FYesterday KeA came\x01",
            "to visit me, but...\x02\x03",
            "#11210FIt seems she felt really down\x01",
            "hearing about my surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah, now that you mention it,\x01",
            "she didn't look very well today.\x02\x03",
            "#00000FBut don't worry.\x01",
            "If you're positive about it, Shizuku,\x01",
            "KeA too will cheer up in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11200FYes...I hope so.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1544")

    label("loc_1514")


    ChrTalk(
        0xD,
        (
            "#11200FKeA...\x01",
            "I hope she cheers up quick.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1544")

    Jump("loc_1B51")

    label("loc_1549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_155A")
    Call(0, 13)
    Jump("loc_1B51")

    label("loc_155A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157F")
    Call(0, 18)
    Jump("loc_1A93")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159B")
    Call(0, 17)
    Jump("loc_1A93")

    label("loc_159B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E8")

    ChrTalk(
        0xD,
        (
            "#01505F...Oh, by the way...\x02\x03",
            "#01500FSomehow didn't KeA seem\x01",
            "to be acting strange yesterday?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E3")
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
            "#1K◆KeA spacing out at the Support Section? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",           # 0
            "[Talked to]\x01",           # 1
            "[Didn't talk to]\x01",      # 2
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
        (0, "loc_16CE"),
        (1, "loc_16D3"),
        (2, "loc_16DB"),
        (SWITCH_DEFAULT, "loc_16E3"),
    )


    label("loc_16CE")

    Jump("loc_16E3")

    label("loc_16D3")

    SetScenarioFlags(0x151, 6)
    Jump("loc_16E3")

    label("loc_16DB")

    ClearScenarioFlags(0x151, 6)
    Jump("loc_16E3")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 6)), scpexpr(EXPR_END)), "loc_1793")

    ChrTalk(
        0x109,
        "#10105FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...Now that you mention it, just now\x01",
            "I felt like she was spacing out.\x02\x03",
            "#00001FHas something happened during\x01",
            "the unveiling ceremony?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180F")

    label("loc_1793")


    ChrTalk(
        0x109,
        (
            "#10105FEh...?\x01",
            "It didn't seem like that to me at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FHas something happened during\x01",
            "the unveiling ceremony?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180F")


    ChrTalk(
        0xD,
        (
            "#01500FNo, I don't think is\x01",
            "anything that important...\x02\x03",
            "#01508FIt felt like KeA was somehow dumbfounded \x01",
            "when watching the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHm, could it be that she was just\x01",
            "surprised by Orchis Tower's dimensions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FOh...could it have\x01",
            "been like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUhhm, I don't really get it,\x01",
            "but I'll keep it in mind.\x02\x03",
            "#00000FThank you, Shizuku.\x01",
            "For worrying about KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01500FNo, not at all...\x01",
            "I'm sorry, I said\x01",
            "something weird.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 2)
    Jump("loc_1A93")

    label("loc_19E8")


    ChrTalk(
        0xD,
        (
            "#01502FThanks to KeA, today\x01",
            "I had a lot of fun at the\x01",
            "unveiling ceremony.\x02\x03",
            "If one day I'll be able to see with my eyes,\x01",
            "I want to watch Orchis Tower again with KeA.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A93")

    Jump("loc_1B43")

    label("loc_1A98")


    ChrTalk(
        0xD,
        (
            "#01502FThanks to KeA, today\x01",
            "I had a lot of fun at the\x01",
            "unveiling ceremony.\x02\x03",
            "If one day I'll be able to see with my eyes,\x01",
            "I want to watch Orchis Tower again with KeA.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_1B51")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B51")

    label("loc_1B51")

    TalkEnd(0xD)
    Return()

    # Function_12_1367 end

    def Function_13_1B55(): pass

    label("Function_13_1B55")

    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C48")

    ChrTalk(
        0xD,
        (
            "#01502FMihail, they say you'll\x01",
            "leave the hospital soon.\x02\x03",
            "Uh uh, congratulations.\x01",
            "Stay always healthy, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes... Shizuku, thank you\x01",
            "for everything until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll write you letters.\x01",
            "Stay well too, Shizuku!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1CE5")

    label("loc_1C48")


    ChrTalk(
        0xD,
        (
            "#01502FMihail, I too am really happy\x01",
            "that you can be discharged.\x02\x03",
            "One day I'll come to visit\x01",
            "you in Leman with my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes...!\x01",
            "I'll be waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE5")

    OP_4C(0xE, 0xFF)
    Return()

    # Function_13_1B55 end

    def Function_14_1CEA(): pass

    label("Function_14_1CEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CFB")
    Jump("loc_1DB4")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D0C")
    Call(0, 13)
    Jump("loc_1DB4")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D1D")
    Call(0, 29)
    Jump("loc_1DB4")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D38")
    Call(0, 34)
    Jump("loc_1DB4")

    label("loc_1D38")


    ChrTalk(
        0xE,
        (
            "Leaving the hospital...\x01",
            "To think that such a day would really come...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I-I must contact my parents\x01",
            "in Leman quick!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB4")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CEA end

    def Function_15_1DB8(): pass

    label("Function_15_1DB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E5F")

    ChrTalk(
        0xF,
        (
            "#01400FI leave the "Cryptids" investigation to you.\x02\x03",
            "I plan to go back in the morning\x01",
            "and join it, so until then,\x01",
            "help out Scott and the others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEC")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7B")
    Call(0, 18)
    Jump("loc_1EEC")

    label("loc_1E7B")


    ChrTalk(
        0xF,
        (
            "#01400FHis Grace said he wanted\x01",
            "to meet Shizuku.\x02\x03",
            "#01403F...I appreciated it.\x01",
            "I'll have to thank him later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEC")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DB8 end

    def Function_16_1EF0(): pass

    label("Function_16_1EF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0F")
    Call(0, 18)
    Jump("loc_1FBB")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F21")
    Call(0, 17)
    Jump("loc_1FBB")

    label("loc_1F21")


    ChrTalk(
        0x15,
        (
            "Oh, right, later I'll absolutely \x01",
            "have to go check on how\x01",
            "Seiland is doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's been a long time since I saw her,\x01",
            "I hope she's in good health.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1EF0 end

    def Function_17_1FBF(): pass

    label("Function_17_1FBF")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "Now that I think about it, Shizuku,\x01",
            "your eyes have some troubles, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...I think you're worried, but\x01",
            "the skills of this hospital's\x01",
            "doctors are worthy to be trusted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It may take some time but you\x01",
            "must fight assiduously believing\x01",
            "in your full recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01505FTh...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x15, 0xFF)
    Return()

    # Function_17_1FBF end

    def Function_18_210C(): pass

    label("Function_18_210C")

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
        "#01505FAh...the Support Section people?\x02",
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
            "#00005FH-His Grace Archduke Albert from\x01",
            "the Principality of Remiferia...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAnd Mr. Arios too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403FHm, what a coincidence.\x02\x03",
            "#01400FYour Grace, they are the persons from the\x01",
            ""Special Support Section" I told you about before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        "Ooh, are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "...Nice to meet you, Support Section ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "My name is Albert von Bartholomeus.\x01",
            "I serve as Remiferia's Head of State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please do your very best for\x01",
            "Crossbell's sake in the future too.\x02",
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
            "Hu hu, I heard about\x01",
            "you all from Arios.\x01",
            "I really wanted to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Also, Elie, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, yes it has.\x01",
            "You look well too, Your Grace...\x02\x03",
            "#00103FHowever, I didn't know\x01",
            "you had come to\x01",
            "visit the hospital.\x02\x03",
            "#00105FDid you come to\x01",
            "inspect it today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Hm, the Principality of Remiferia is\x01",
            "one of this hospital's sponsors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I also wanted to absolutely greet Arios'\x01",
            "daughter whom I had heard about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01502FT-Thank you very much, Archduke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01400FRegarding that, I personally\x01",
            "wanted you to have a little\x01",
            "more guards...\x02\x03",
            "#01403FIt's only the limousine's\x01",
            "driver and I, after all...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "Hu hu, it's just because\x01",
            "I have confidence in\x01",
            "you, Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Also, I couldn't have brought with me a\x01",
            "group of guards in my inspection, or else \x01",
            "I would've disturbed the hospital work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Archduke Albert...\x01",
            "He didn't only know Mr.\x01",
            "Arios, but also Elie.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes. Miss Elie, Mr. Arios...\x01",
            "And Professor Seiland too, he seems\x01",
            "to have known them since some time ago.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hu hu, he seems to be a more\x01",
            "sociable person than I thought.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "At any rate, I'll\x01",
            "cheer for you all too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Keep doing your best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYour Grace Archduke too, please be\x01",
            "careful when going back today.\x02\x03",
            "We'll be assisting too on\x01",
            "tomorrow's Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Ha ha, I'll do my best for sure.\x02",
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

    # Function_18_210C end

    def Function_19_2A75(): pass

    label("Function_19_2A75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_2B0E")

    ChrTalk(
        0x8,
        (
            "#01900FI can't really thank the\x01",
            "Inspector enough for\x01",
            "having saved me.\x02\x03",
            "#01909FI'll come again to visit\x01",
            "when I find the right time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFC")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3D")

    ChrTalk(
        0x8,
        (
            "#06400FEhhm, notebook,\x01",
            "ENIGMA, toothbrush...\x02\x03",
            "#06405FAh, I have to finish greeting\x01",
            "the other patients and\x01",
            "nurses too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(It seems that Fran's preparations\x01",
            "are going to take a little longer...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F(Well it would be better\x01",
            "if we ended our\x01",
            "visits first.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CCC")

    label("loc_2C3D")


    ChrTalk(
        0x8,
        (
            "#06405FOh, I also must properly\x01",
            "change into my uniform...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "#06401F...Please don't peep, ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I won't peep.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_2CCC")

    Jump("loc_2DFC")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_END)), "loc_2DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(
        0x8,
        "#11703Fzzz...zzz...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB6")

    ChrTalk(
        0x105,
        "#10300FHu hu, she seems to be sleeping well, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01302FIt's all right, Miss Noｱl.\x01",
            "At this rate, she will get well soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FYes...thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DDB")

    label("loc_2DB6")


    ChrTalk(
        0x109,
        (
            "#10103F(Fran...\x01",
            "Get well soon.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDB")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2DFC")

    label("loc_2DE3")


    ChrTalk(
        0x8,
        "#11703Fzzz...zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_2DFC")

    TalkEnd(0xFE)
    Return()

    # Function_19_2A75 end

    def Function_20_2E00(): pass

    label("Function_20_2E00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1E")
    Call(0, 21)
    Jump("loc_2ED8")

    label("loc_2E1E")


    ChrTalk(
        0x9,
        (
            "I'm going to join the police now, but...\x01",
            "Well, I intend to do what I can to help\x01",
            "out somehow, without overdoing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems you're having it quite hard,\x01",
            "so be very careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED8")

    Jump("loc_353E")

    label("loc_2EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_312F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3030")

    ChrTalk(
        0x9,
        (
            "A declaration of invalidity for the\x01",
            "independent state, huh...?\x01",
            "To think you'd go this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even Sergei and the others in the\x01",
            "city should be starting to move taking\x01",
            "advantage of this opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being in this condition, I won't\x01",
            "be able to join you for a while.\x01",
            "...I leave the rest to you, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_312A")

    label("loc_3030")


    ChrTalk(
        0x9,
        (
            "It would be alright to suppose that even Sergei\x01",
            "and the others in the city should be starting to\x01",
            "move taking advantage of this opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being in this condition, I won't\x01",
            "be able to join you for a while.\x01",
            "...I leave the rest to you, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_312A")

    Jump("loc_353E")

    label("loc_312F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_31F0")

    ChrTalk(
        0x9,
        (
            "At any rate, it doesn't seem I'll\x01",
            "be able to join the police soon,\x01",
            "so I'll rest my body for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until then, Raymond, Sergei and\x01",
            "the others will have do their best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353E")

    label("loc_31F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_3279")

    ChrTalk(
        0x9,
        (
            "Ha ha, I'm safe and sound too,\x01",
            "so there's nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're convalescent\x01",
            "too so be careful got it?\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353E")

    label("loc_3279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3294")
    Call(0, 21)
    Jump("loc_32FF")

    label("loc_3294")


    ChrTalk(
        0x9,
        (
            "Well, in any case...\x01",
            "Be careful, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope I'll be able to join\x01",
            "Sergei and the others soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32FF")

    Jump("loc_353E")

    label("loc_3304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_353E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3528")

    ChrTalk(
        0x9,
        "#90W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...When the Inspector will regain\x01",
            "his consciousness, I'll have to\x01",
            "formally thank him for protecting Fran.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F0")

    ChrTalk(
        0x136,
        (
            "#01303FBecause he received severe damage\x01",
            "to his respiratory system, his\x01",
            "recovery will probably be far...\x02\x03",
            "#01300FHowever, he passed the\x01",
            "worst, so he should be\x01",
            "waking up soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI hope so...\x02\x03",
            "#00100F...It seems it'll be fine\x01",
            "to leave the rest to Mr.\x01",
            "Raymond, so let's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3520")

    label("loc_34F0")


    ChrTalk(
        0x101,
        (
            "#00003FRight...\x01",
            "I hope he gets well quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3520")

    SetScenarioFlags(0x0, 1)
    Jump("loc_353E")

    label("loc_3528")


    ChrTalk(
        0x9,
        "#90W............\x02",
    )

    CloseMessageWindow()

    label("loc_353E")

    TalkEnd(0xFE)
    Return()

    # Function_20_2E00 end

    def Function_21_3542(): pass

    label("Function_21_3542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38F3")
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)

    def lambda_3558():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3558)
    Sleep(0)

    def lambda_3568():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3568)
    Sleep(0)

    def lambda_3578():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3578)
    Sleep(0)

    def lambda_3588():
        TurnDirection(0x3, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_3588)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x16, 0x0, 0)

    ChrTalk(
        0x9,
        "Ooh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Uhuhu, good day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FInspector Donovan...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIs it all right for you to move yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, the papers for my\x01",
            "discharge were just completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the operation to free\x01",
            "Crossbell City went well and I\x01",
            "thought to join the police too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Actually, the scheduled day for\x01",
            "his discharge was still far.\x02",
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
            "#00309FHa ha, even Raymond\x01",
            "will be happy, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf the Inspector joins, even Crime\x01",
            "Investigations Section Two will be\x01",
            "able to display its strength even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I intend to do what I can to help\x01",
            "out somehow, without overdoing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems you're having it quite hard,\x01",
            "so be very careful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 7)
    TurnDirection(0x9, 0x16, 0)
    TurnDirection(0x16, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_3CBC")

    label("loc_38F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3CBC")

    def lambda_3901():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3901)
    Sleep(0)

    def lambda_3911():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3911)
    Sleep(0)

    def lambda_3921():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3921)
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39C9")
    Jump("loc_3A13")

    label("loc_39C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39E9")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A13")

    label("loc_39E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A09")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A13")

    label("loc_3A09")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A13")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC9")
    Jump("loc_3B13")

    label("loc_3AC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AE9")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B13")

    label("loc_3AE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B09")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B13")

    label("loc_3B09")

    OP_52(0x16, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B13")

    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x10)

    ChrTalk(
        0x9,
        (
            "Man, I've made you see\x01",
            "something embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I keep getting caught in Fara's\x01",
            "pace since the time I married her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, she's a nice wife, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHu hu, very lovely.\x02",
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
            "Uh uh, lovely you say.\x01",
            "You heard it, right, dear?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "(...Because she's like this even in front of\x01",
            "these guys and Raymond, she's troublesome...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x10)

    label("loc_3CBC")

    Return()

    # Function_21_3542 end

    def Function_22_3CBD(): pass

    label("Function_22_3CBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC6")

    ChrTalk(
        0xA,
        (
            "My life was saved\x01",
            "by Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm spiritless, but...\x01",
            "I'll have to get my act together\x01",
            "more from now onward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One day I'll have to become a\x01",
            "splendid detective as the Inspector's\x01",
            "subordinate to not embarrass him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E84")

    label("loc_3DC6")


    ChrTalk(
        0xA,
        (
            "I'm spiritless, but...\x01",
            "I'll have to get my act together\x01",
            "more from now onward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One day I'll have to become a\x01",
            "splendid detective as the Inspector's\x01",
            "subordinate to not embarrass him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E84")

    TalkEnd(0xFE)
    Return()

    # Function_22_3CBD end

    def Function_23_3E88(): pass

    label("Function_23_3E88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_461E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B6")

    ChrTalk(
        0xB,
        (
            "#11601FIt's you guys...\x01",
            "It seems that something\x01",
            "terrible is going on.\x02\x03",
            "#11606FThey say that something like\x01",
            "a mysterious "huge tree"\x01",
            "has appeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes...to tell you the truth,\x01",
            "we still don't know what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWe can't even say that the\x01",
            "hospital is completely safe.\x02\x03",
            "#00101FMiss Ilya, please be careful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609FAhaha, thanks.\x01",
            "I don't know the\x01",
            "full details, but...\x02\x03",
            "#11600FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11604FI too won't ever give up until\x01",
            "I stand on the stage again...\x02\x03",
            "#11609FSo you too, do your\x01",
            "best until the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FIf we've got Miss Ilya's support,\x01",
            "our strength will increase a hundredfold!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_41AE")
    Call(0, 77)
    Return()

    label("loc_41AE")

    SetScenarioFlags(0x0, 3)
    Jump("loc_42A1")

    label("loc_41B6")


    ChrTalk(
        0xB,
        (
            "#11604FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11609FI too won't ever give up until\x01",
            "I stand on the stage again...\x01",
            "So do your best until the very end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A1")

    Jump("loc_4619")

    label("loc_42A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6C), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42C1")
    Call(0, 86)
    Jump("loc_4619")

    label("loc_42C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_4410")

    ChrTalk(
        0xB,
        (
            "#11600FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11604FI too won't ever give up until\x01",
            "I stand on the stage again...\x01",
            "So do your best until the very end.\x02\x03",
            "#11609FUh uh, and please take care of\x01",
            "the girl who's standing outside too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4526")

    label("loc_4410")


    ChrTalk(
        0xB,
        (
            "#11600FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11604FI too won't ever give up until\x01",
            "I stand on the stage again...\x01",
            "So do your best until the very end.\x02\x03",
            "#11609FUh uh, take care of that girl too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4526")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4619")

    label("loc_452E")


    ChrTalk(
        0xB,
        (
            "#11604FI'm sure that if you don't give up,\x01",
            "you'll make it through. I'm sure you'll\x01",
            "be able to catch what's important to you.\x02\x03",
            "#11609FI too won't ever give up until\x01",
            "I stand on the stage again...\x01",
            "So do your best until the very end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4619")

    Jump("loc_5204")

    label("loc_461E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498B")

    ChrTalk(
        0xB,
        (
            "#11603FRumor goes that something terrible has\x01",
            "happened in the city, younger brother...\x02\x03",
            "#11601FIt seems they reporeted the shocking truth\x01",
            "of the raid incident of back then?\x02\x03",
            "Although it seems that detail information\x01",
            "was regulated and didn't flow around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FMiss Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(For Miss Ilya that matter\x01",
            "is the fundamental cause\x01",
            "of her severe injury...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11603F...Well, now of all time I don't have\x01",
            "any interest in that incident truth.\x02\x03",
            "#11600FMore importantly, I wonder\x01",
            "when my next rehabilitation is.\x02\x03",
            "#11609FIn order to also come back to the stage,\x01",
            "I want to move my body soon and\x01",
            "I'm itching to do something, you know♪\x02",
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
        "#00012FHa ha, what can I say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FAs expected from Miss Ilya.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 2)
    Jump("loc_4A51")

    label("loc_498B")


    ChrTalk(
        0xB,
        (
            "#11602FI'll keep doing rehabilitation\x01",
            "and absolutely return on stage,\x01",
            "so I've got no interest in other stuff.\x02\x03",
            "#11609FAah, can't I do the next rehabilitation yet?\x01",
            "I want to move my body soon♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A51")

    Jump("loc_5204")

    label("loc_4A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D91")

    ChrTalk(
        0xB,
        (
            "#11600FAccording to Professor Seiland,\x01",
            "she can't actually tell if I'll be\x01",
            "able to walk again or not...\x02\x03",
            "#11604FIt's not that the possibility is zero,\x01",
            "so I've got no reason to give up.\x02\x03",
            "#11602FAfter all, man is a living being who can do\x01",
            "his utmost best for what's precious to him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD7")

    ChrTalk(
        0x103,
        (
            "#00200FLooking at you Miss Ilya,\x01",
            "I can really think like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHu hu, younger brother, guys.\x01",
            "When you meet Rixia, tell her this.\x02\x03",
            "#11600F"Can you be in front of that precious thing\x01",
            "and not help doing your best for it?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, understood.\x01",
            "When we meet her, we'll\x01",
            "absolutely tell her these words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D89")

    label("loc_4CD7")


    ChrTalk(
        0x101,
        (
            "#00008F(We passed this message\x01",
            "from Miss Ilya to Rixia, but...\x01",
            "It seems it's not the case they can meet yet.)\x02\x03",
            "#00003F(At present, it's better to\x01",
            "not tell her about Rixia.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D89")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4E56")

    label("loc_4D91")


    ChrTalk(
        0xB,
        (
            "#11604FMan is a living being who can do his\x01",
            "utmost best for what's precious to him.\x02\x03",
            "#11600FIt's not that the possibility that\x01",
            "I'll be walking again is zero,\x01",
            "so I've got no reason to give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E56")

    Jump("loc_5204")

    label("loc_4E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_50EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5055")

    ChrTalk(
        0xB,
        (
            "#11600FI'm worried about everyone in the\x01",
            "Arc-en-ciel who're in the city.\x02\x03",
            "#11609FWell, I'm talking about them, so they'll be\x01",
            "probably practicing even in such a situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, is that what you're worried about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThe persons from Arc-en-ciel are\x01",
            "zealously practicing for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FHu hu, after all everyone\x01",
            "is an artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHu hu, Sully is in her growth period too...\x02\x03",
            "#11609FShe must practice diligently\x01",
            "even for when I'll go back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50E5")

    label("loc_5055")


    ChrTalk(
        0xB,
        (
            "#11600FI'm worried about everyone in the\x01",
            "Arc-en-ciel who're in the city.\x02\x03",
            "#11609FThey must practice diligently\x01",
            "even for when I'll go back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E5")

    Jump("loc_5204")

    label("loc_50EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_5204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51E7")

    ChrTalk(
        0xB,
        "#11603F#90W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...Still, to think we'd seen\x01",
            "Miss Ilya in such a state...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FRight...\x01",
            "I can't believe it's real even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMiss Ilya will come back for sure.\x01",
            "...Let's believe that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5204")

    label("loc_51E7")


    ChrTalk(
        0xB,
        "#11603F#90W............\x02",
    )

    CloseMessageWindow()

    label("loc_5204")

    TalkEnd(0xFE)
    Return()

    # Function_23_3E88 end

    def Function_24_5208(): pass

    label("Function_24_5208")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5300")

    ChrTalk(
        0xC,
        (
            "#04200FYou guys...\x01",
            "Please, take care of\x01",
            "sis Rixia's matter.\x02\x03",
            "#04203FIf sis Rixia comes back,\x01",
            "Miss Ilya too will get better...\x01",
            "I've got that feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Yeah, wait for us.\x01",
            "We'll find her out for sure.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53A4")

    label("loc_5300")


    ChrTalk(
        0xC,
        (
            "#04203FIf sis Rixia comes back,\x01",
            "Miss Ilya too will get better...\x01",
            "I've got that feeling.\x02\x03",
            "#04200FUntil then, we Arc-en-ciel must\x01",
            "support Miss Ilya in some way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A4")

    TalkEnd(0xFE)
    Return()

    # Function_24_5208 end

    def Function_25_53A8(): pass

    label("Function_25_53A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53B9")
    Jump("loc_573A")

    label("loc_53B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DE")

    ChrTalk(
        0x10,
        (
            "It's about time we request supplies\x01",
            "for the goods we're lacking, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "By accepting the declaration of invalidity\x01",
            "for the independent state, the State\x01",
            "Guard people returned to their units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Uuhm, what a problem.\x01",
            "How should we negotiate from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5553")

    label("loc_54DE")


    ChrTalk(
        0x10,
        (
            "Uuhm, what a problem.\x01",
            "The State Guard went away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "How should we negotiate for\x01",
            "goods supplies from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5553")

    Jump("loc_573A")

    label("loc_5558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5566")
    Jump("loc_573A")

    label("loc_5566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5574")
    Jump("loc_573A")

    label("loc_5574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_573A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5698")

    ChrTalk(
        0x10,
        (
            "It seems that when the hospital\x01",
            "was previously attacked, some\x01",
            "people hid in this linen room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At the time of that incident\x01",
            "I ended up getting shot in\x01",
            "the belly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thinking about it now,\x01",
            "I should've hidden quickly too.\x01",
            "Uuhm, what a mistake I did.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_573A")

    label("loc_5698")


    ChrTalk(
        0x10,
        (
            "Previously, when the hospital was attacked,\x01",
            "I ended up getting shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thinking about it now,\x01",
            "I should've hidden quickly too.\x01",
            "Uuhm, what a mistake I did.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573A")

    TalkEnd(0xFE)
    Return()

    # Function_25_53A8 end

    def Function_26_573E(): pass

    label("Function_26_573E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_574F")
    Jump("loc_65A2")

    label("loc_574F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_575D")
    Jump("loc_65A2")

    label("loc_575D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_576B")
    Jump("loc_65A2")

    label("loc_576B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B66")
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
            "#00200FKeA was\x01",
            "worried too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThinking about them,\x01",
            "they should be at\x01",
            "Orchis Tower now.\x02\x03",
            "#00003FI hope she can\x01",
            "meet her somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FLloyd...\x01",
            "I hope all the people from\x01",
            "the SSS will be reunited quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406FWell, frankly speaking,\x01",
            "the road ahead is quite hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...In order to get KeA back,\x01",
            "we absolutely need everyone's strength.\x02\x03",
            "#00000FThat's why no matter how painful it is,\x01",
            "I'll move forward without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FUh uh, you will do it for sure.\x02\x03",
            "#01304FI will pray the venerable Goddess from here.\x01",
            "...Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, sister Cecil. Hearing you say\x01",
            "that gives me tremendous strength.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B57")

    ChrTalk(
        0x107,
        (
            "#01200F#13C............\x02\x03",
            "(She really is your descendant...\x01",
            "──Ursula.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 500)

    ChrTalk(
        0x103,
        (
            "#00205FZeit...\x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 500)

    ChrTalk(
        0x107,
        (
            "#01203F#13C...Hu hu, don't worry.\x01",
            "It also happens to me to\x01",
            "be lost in thoughts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B57")

    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1AC, 2)
    Jump("loc_5D1F")

    label("loc_5B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C58")
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0x11,
        (
            "#01300FIlya, let's go to\x01",
            "do rehabilitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604FHm, got it.\x02\x03",
            "#11609FI'll be in your care today too,\x01",
            "Head Nurse Cecil㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FUh uh, I am here for you and everyone.\x01",
            "I will help you thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_5D1F")

    label("loc_5C58")


    ChrTalk(
        0x11,
        (
            "#01302FIf it is you, Lloyd, I am sure\x01",
            "you will be able to save all the Support\x01",
            "Section members and reunite with KeA.\x02\x03",
            "#01304FI will pray the venerable Goddess from here.\x01",
            "...Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1F")

    Jump("loc_65A2")

    label("loc_5D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5D32")
    Jump("loc_65A2")

    label("loc_5D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D40")
    Jump("loc_65A2")

    label("loc_5D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D51")
    Call(0, 27)
    Jump("loc_65A2")

    label("loc_5D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D62")
    Call(0, 27)
    Jump("loc_65A2")

    label("loc_5D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D70")
    Jump("loc_65A2")

    label("loc_5D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6101")
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x103, 500)

    ChrTalk(
        0x11,
        (
            "#01302FMy, if it isn't Tio.\x01",
            "You returned to the Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, I came back just yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01309FUh uh, I am happy to see you again.\x02\x03",
            "#01304FI heard you were\x01",
            "really busy, but...\x01",
            "Yes, today your complexion is nice.\x02\x03",
            "#01300FPlease pay attention to your\x01",
            "physical condition so to not\x01",
            "collapse again like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FUh uh, thank you for all\x01",
            "you did in that occasion.\x02\x03",
            "#00200FWell, if I could sleep again in \x01",
            "Miss Cecil's soft bed, I would be\x01",
            "willing to even pass out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHm, I totally agree with you 'bout that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FRandy, listen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FPlease, have a little respect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01302FUh uh...\x01",
            "It seems you are the\x01",
            "same as always.\x02\x03",
            "#01304FWith Tio coming back, the\x01",
            "Support Section is finally\x01",
            "completely operative, eh?\x02\x03",
            "#01309FI will always support you,\x01",
            "so do your best from now on too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 5)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_6181")

    label("loc_6101")


    ChrTalk(
        0x11,
        (
            "#01300FMihail is going to be discharged soon.\x02\x03",
            "#01304FI will be a little sad, however...\x01",
            "Uh uh, I am really happy for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6181")

    Jump("loc_65A2")

    label("loc_6186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6197")
    Call(0, 29)
    Jump("loc_65A2")

    label("loc_6197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_65A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6513")

    ChrTalk(
        0x101,
        (
            "#00000FAh...\x01",
            "Sister Cecil, so you were here.\x02",
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
            "#01300FYes, because she's outside,\x01",
            "I am cleaning now that I can.\x02\x03",
            "#01304FToday, Shizuku went\x01",
            "to play in the city.\x02\x03",
            "#01309FA little while ago she was\x01",
            "very happily talking that\x01",
            "she was going to meet KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, they've become\x01",
            "good pals for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, she IS KeA.\x01",
            "It's only obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, I, for sure, have a certain feeling\x01",
            "that she possesses something like a\x01",
            "talent for becoming friends with people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F*chuckle chuckle*...you can say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300FThanks to her, Shizuku too has\x01",
            "become brighter than before...\x01",
            "I am grateful to KeA.\x02\x03",
            "#01302FThe next time I can take a day off,\x01",
            "I want to come play with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, I'm sure KeA will be happy too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01309FUh uh, I can't wait for that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 1)
    Jump("loc_65A2")

    label("loc_6513")


    ChrTalk(
        0x11,
        (
            "#01300FI guess that Shizuku\x01",
            "is playing with KeA\x01",
            "at this time.\x02\x03",
            "#01309FUh uh, it's a rare day out, so I\x01",
            "hope she enjoys it to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65A2")

    TalkEnd(0xFE)
    Return()

    # Function_26_573E end

    def Function_27_65A6(): pass

    label("Function_27_65A6")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6794")

    ChrTalk(
        0xD,
        (
            "#11200FMiss Cecil...\x01",
            "It seems that yesterday\x01",
            "there were a lot of ambulances.\x02\x03",
            "#11210FI heard that there was\x01",
            "a big accident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01303FIt seems that a train derailed\x01",
            "at the West Crossbell Highway.\x02\x03",
            "#01302FBut stay assured.\x01",
            "It seems that thanks to the doctors'\x01",
            "efforts there were no victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FIs that so? Thank goodness.\x02\x03",
            "#11208FWhen I thought it could've been a severe\x01",
            "accident like when it happened to me, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01308FShizuku...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6860")

    label("loc_6794")


    ChrTalk(
        0x11,
        (
            "#01300FThanks to the doctors' efforts,\x01",
            "all the train accident patients\x01",
            "were saved.\x02\x03",
            "So, you shouldn't\x01",
            "worry about the accident.\x01",
            "Let's concentrate on the rehabilitation now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11202FYes...please.\x02",
    )

    CloseMessageWindow()

    label("loc_6860")

    Jump("loc_6A0E")

    label("loc_6865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6880")
    Call(0, 28)
    Jump("loc_6A0E")

    label("loc_6880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697C")

    ChrTalk(
        0x11,
        (
            "#01304FUh uh, then I will read it.\x01",
            "...*ahhem*.\x02\x03",
            "#01300F"Shizuku, are you well?\x01",
            "I am."\x02\x03",
            ""Every night I pray the\x01",
            "Goddess so you can \x01",
            "become able to see."\x02\x03",
            "#01309FUh uh, typical of that boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11202FMihail...\x01",
            "...I'm very happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6A0E")

    label("loc_697C")


    ChrTalk(
        0x11,
        (
            "#01304FOh right, he enclosed\x01",
            "a picture too.\x02\x03",
            "#01302FUh uh, he's between his parents\x01",
            "and looks very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11209F*chuckle*, how nice...\x02",
    )

    CloseMessageWindow()

    label("loc_6A0E")

    SetChrSubChip(0xD, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_27_65A6 end

    def Function_28_6A17(): pass

    label("Function_28_6A17")

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
        "#12P#00000FHi, sister Cecil, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#11202FOh...good morning, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FMy, if it isn't Lloyd and the others.\x02\x03",
            "#01309FUh uh, could you have come\x01",
            "to visit Shizuku?\x02",
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
            "#N#12P#10105FEehm, could we have\x01",
            "interrupted you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x11, 0xB4, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FUh uh, that is not the case.\x02\x03",
            "#01304FActually, a letter from Mihail who went back to \x01",
            "the autonomous state of Leman arrived today.\x02\x03",
            "#01300FI had just thought to\x01",
            "read it with Shizuku.\x02",
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
            "#12P#10302FThe little boy who Professor\x01",
            "Seiland operated, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#11204FYes, he was a boy I really\x01",
            "went along well with...\x02\x03",
            "#11200FWhen he was discharged, we \x01",
            "promised to exchange letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHa ha, ain't that nice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#01300FAt St. Ursula Hospital we\x01",
            "happen to receive letters from\x01",
            "discharged patients, like this one.\x02\x03",
            "#01304FWe are busy so we can't quite\x01",
            "make the time to reply, but...\x02\x03",
            "#01300FBeing able to know what happened to the patients\x01",
            "afterwards becomes my source of energy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha, being who you're, sister Cecil, \x01",
            "you're probably diligently replying to\x01",
            "each one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204F...It would be better if I too sent\x01",
            "letters to Head Nurse Martha.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xE1, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#5P#01302FUh uh, when she met you again,\x01",
            "the Head Nurse was really happy.\x02\x03",
            "#01309FIt is not too late, so why don't you\x01",
            "try to start if you have the chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FUh uh, I will think about\x01",
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

    # Function_28_6A17 end

    def Function_29_70DF(): pass

    label("Function_29_70DF")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73CF")

    ChrTalk(
        0x11,
        "#01300FMihail, how are you feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I haven't got even a single spasm.\x01",
            "It seems unreal that I was suffering for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01304FUh uh, I'm glad for you.\x02\x03",
            "#01300FThe day you'll be discharged is coming close...\x01",
            "You will be able to live again\x01",
            "with your parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I think I'm half happy\x01",
            "and half sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When I'll go back to the autonomous\x01",
            "state of Leman, I'll be separated\x01",
            "from Miss Cecil and Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#01300F...We have fought together against\x01",
            "that illness for a long time, eh?\x01",
            "It is true that it will be very sad, but...\x02\x03",
            "#01304FEven if we are far away,\x01",
            "these bonds will not break.\x01",
            "...I believe that.\x02",
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
            "Thank you for everything, Miss Cecil.\x01",
            "I'll never forget you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 3)
    Jump("loc_746D")

    label("loc_73CF")


    ChrTalk(
        0x11,
        (
            "#01309FUh uh, let's go towards the day\x01",
            "you will be discharged with a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, I'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I must properly say\x01",
            "farewell to Shizuku too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746D")

    SetChrSubChip(0xE, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_29_70DF end

    def Function_30_7476(): pass

    label("Function_30_7476")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7487")
    Jump("loc_75BE")

    label("loc_7487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_757D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A2")
    Call(0, 31)
    Jump("loc_7578")

    label("loc_74A2")

    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        (
            "Uhhm, according to how the sky felt yesterday,\x01",
            "I had a hunch that it wouldn't have rained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If your intuition had got it right\x01",
            "instead of the weather forecast,\x01",
            "it would've been too damn amazing!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_7578")

    Jump("loc_75BE")

    label("loc_757D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_758B")
    Jump("loc_75BE")

    label("loc_758B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7599")
    Jump("loc_75BE")

    label("loc_7599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_75A7")
    Jump("loc_75BE")

    label("loc_75A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_75B5")
    Jump("loc_75BE")

    label("loc_75B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_75BE")

    label("loc_75BE")

    TalkEnd(0xFE)
    Return()

    # Function_30_7476 end

    def Function_31_75C2(): pass

    label("Function_31_75C2")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Xilun, you...\x01",
            "You were on the rooftop drying the sheets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Didn't the manager said that the weather\x01",
            "forecast said it was going to rain!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I thought what if it unexpectedly didn't rain?\x01",
            "Ehehe, I tried to wage on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Why did you do it!?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 7)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_31_75C2 end

    def Function_32_76D7(): pass

    label("Function_32_76D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_76E8")
    Jump("loc_7BEB")

    label("loc_76E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_778D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7703")
    Call(0, 31)
    Jump("loc_7788")

    label("loc_7703")


    ChrTalk(
        0x13,
        (
            "Honestly, the sheets I so painstakingly\x01",
            "washed must be all washed again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Wait, more importantly,\x01",
            "I must get them in quick!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7788")

    Jump("loc_7BEB")

    label("loc_778D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_779B")
    Jump("loc_7BEB")

    label("loc_779B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_796B")

    ChrTalk(
        0x13,
        (
            "Looking at Mihail energetically waving\x01",
            "his hand on the day he was discharged,\x01",
            "I got moved and ended up crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "When that happened, Xilun gave\x01",
            "me a handkerchief in silence.\x01",
            "When I thought that every now and then she's thoughtful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Looking at it carefully, it wasn't\x01",
            "a handkerchief but my favourite\x01",
            "skirt that I previously lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "...There were so many things to retort about\x01",
            "and being deeply moved I made a mess of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7A2C")

    label("loc_796B")


    ChrTalk(
        0x13,
        (
            "Well, leaving that aside...\x01",
            "I'm really happy that Mihail\x01",
            "could leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I believe that by now he'll be in \x01",
            "the autonomous state of Leman\x01",
            "living happily with his parents...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A2C")

    Jump("loc_7BEB")

    label("loc_7A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A3F")
    Jump("loc_7BEB")

    label("loc_7A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7A4D")
    Jump("loc_7BEB")

    label("loc_7A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B28")

    ChrTalk(
        0x13,
        (
            "Mr. Geval, who was hospitalised here,\x01",
            "has been discharged a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Than man was so selfish and\x01",
            "really gave us troubles, but...\x01",
            "I wonder where is he now and what is he doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7BEB")

    label("loc_7B28")


    ChrTalk(
        0x13,
        (
            "Ah, now that I think about it, Xilun is\x01",
            "supposed to do an intravenous drip today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Because that girl always does some\x01",
            "crazy mistakes, I'm worried.\x01",
            "...I guess I'll go check on her later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BEB")

    TalkEnd(0xFE)
    Return()

    # Function_32_76D7 end

    def Function_33_7BEF(): pass

    label("Function_33_7BEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C00")
    Jump("loc_7CDD")

    label("loc_7C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7C0E")
    Jump("loc_7CDD")

    label("loc_7C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C1C")
    Jump("loc_7CDD")

    label("loc_7C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7C2A")
    Jump("loc_7CDD")

    label("loc_7C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C38")
    Jump("loc_7CDD")

    label("loc_7C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7C46")
    Jump("loc_7CDD")

    label("loc_7C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C61")
    Call(0, 34)
    Jump("loc_7CDD")

    label("loc_7C61")


    ChrTalk(
        0x14,
        (
            "Even so,\x01",
            "Professor Seiland is...\x01",
            "Wonderfully skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It seems that there're many\x01",
            "things I'll learn from her too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CDD")

    TalkEnd(0xFE)
    Return()

    # Function_33_7BEF end

    def Function_34_7CE1(): pass

    label("Function_34_7CE1")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            "Hm...\x01",
            "The postoperative progress seems good.\x01",
            "You'll be able to leave the hospital soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Contact your parents in the\x01",
            "autonomous state of Leman later.\x02",
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
        "Yeah, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Professor Seiland is skilled too, but most \x01",
            "of all it was your courage to undergo\x01",
            "surgery that overcame the illness.\x02",
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
            "...*sob*...\x01",
            "Thank you, doctor...!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 6)
    SetChrSubChip(0xE, 0x0)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_34_7CE1 end

    def Function_35_7E77(): pass

    label("Function_35_7E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E95")
    Call(0, 21)
    Jump("loc_7F70")

    label("loc_7E95")


    ChrTalk(
        0x16,
        (
            "To tell the truth, the scheduled day to be \x01",
            "discharged was still some days away, but...\x01",
            "He asked me earnestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Uhuhu, however, I am glad.\x01",
            "After all, what I like about him the\x01",
            "most is his figure when working㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F70")

    Jump("loc_84C3")

    label("loc_7F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8082")

    ChrTalk(
        0x16,
        (
            "I completely read the book\x01",
            "I brought for the visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It would be useless reading the same book over again...\x01",
            "Yes, I think I will give it to you as a present♪\x01\x02",
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
    Jump("loc_810D")

    label("loc_8082")


    ChrTalk(
        0x16,
        (
            "Even all the State Guard persons who came\x01",
            "to the hospital seem to have gone back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "...I wonder if they're trying to do something?\x02",
    )

    CloseMessageWindow()

    label("loc_810D")

    Jump("loc_84C3")

    label("loc_8112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_826C")

    ChrTalk(
        0x16,
        (
            "At the time of the independence declaration\x01",
            "I was making a visit and I have been\x01",
            "staying here since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The required application to come and go to\x01",
            "the city has seriously become a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I didn't have quite many chances to\x01",
            "quiety spend time with him, so since\x01",
            "I have the opportunity, I must enjoy it♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8353")

    label("loc_826C")


    ChrTalk(
        0x16,
        (
            "At the time of the independence declaration\x01",
            "I was making a visit and I have been\x01",
            "staying here since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I didn't have quite many chances to\x01",
            "quiety spend time with him, so since\x01",
            "I have the opportunity, I must enjoy it♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8353")

    Jump("loc_84C3")

    label("loc_8358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_8428")

    ChrTalk(
        0x16,
        (
            "Uh uh, oh, this man... He's no longer young\x01",
            "but he does nothing but reckless things...\x01",
            "He worried you too, Miss Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "However, protecting a\x01",
            "cute girl like you was\x01",
            "his best fine play♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_84C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8443")
    Call(0, 21)
    Jump("loc_84C3")

    label("loc_8443")


    ChrTalk(
        0x16,
        (
            "Somehow I understand that\x01",
            "there're troubles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Now I must properly watch him\x01",
            "so he doesn't do anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84C3")

    TalkEnd(0xFE)
    Return()

    # Function_35_7E77 end

    def Function_36_84C7(): pass

    label("Function_36_84C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_84D8")
    Jump("loc_8DC7")

    label("loc_84D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_84E6")
    Jump("loc_8DC7")

    label("loc_84E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8747")

    ChrTalk(
        0x17,
        (
            "The hardest blow as an independent\x01",
            "state that cut diplomatic ties is that I\x01",
            "can't cooperate with Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "As for the amount of medical goods, it seems\x01",
            "that a large quantity of those has been prepared \x01",
            "by the President in case of emergency, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "In the first place, medicines are things to be\x01",
            "carefully selected and prescribed to match \x01",
            "the patient's condition and constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "With the amount of the medicines\x01",
            "the President stored, it'll be difficult\x01",
            "to deal with all the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "What should I do from here on...?\x01",
            "I need to think about some methods.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8800")

    label("loc_8747")


    ChrTalk(
        0x17,
        (
            "With the amount of the medicines\x01",
            "the President stored, it'll be difficult\x01",
            "to deal with all the patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "What should I do from here on...?\x01",
            "I need to think about some methods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8800")

    Jump("loc_8DC7")

    label("loc_8805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD9")

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
        "...You guys? It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThis was Shizuku's room.\x01",
            "...What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "She was a patient I was in charge of.\x01",
            "I was just indulging in some thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...Like how she's doing after she was forced\x01",
            "by Arios MacLaine to leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FNow that I think about it, we\x01",
            "haven't met her since then.\x02\x03",
            "#10403FShe's probably being sheltered\x01",
            "somewhere at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting taken away the patient\x01",
            "you're in charge of is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Though I understand that it couldn't have\x01",
            "been helped under that situation where he \x01",
            "was appointed Secretary of Defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I understand that, but...\x01",
            "There's no way I can accept it.\x02",
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
            "...I'm sorry, it seems I've ended up\x01",
            "doing a foolish talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "You've come for a visit, right?\x01",
            "...Sorry, but could you leave me alone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 6)
    ClearChrFlags(0x17, 0x10)
    Jump("loc_8DC7")

    label("loc_8BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D0D")

    ChrTalk(
        0x17,
        (
            "Shizuku MacLaine...\x01",
            "I had carefully prepared for over one\x01",
            "year the medical treatment plan for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting taken away the patient\x01",
            "you're in charge of is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I guess it also can't be helped to\x01",
            "be bound to a discharged patient too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8DC7")

    label("loc_8D0D")


    ChrTalk(
        0x17,
        (
            "...No matter if he's her father,\x01",
            "getting taken away the patient\x01",
            "you're in charge of is sheer disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I guess it also can't be helped to\x01",
            "be bound to a discharged patient too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DC7")

    TalkEnd(0xFE)
    Return()

    # Function_36_84C7 end

    def Function_37_8DCB(): pass

    label("Function_37_8DCB")

    Sound(160, 0, 100, 0)
    Return()

    # Function_37_8DCB end

    def Function_38_8DD2(): pass

    label("Function_38_8DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FA8")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E87")
    SetChrPos(0x109, -16360, 0, 29320, 90)

    label("loc_8E87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EA8")
    SetChrPos(0x105, -16360, 0, 29320, 90)

    label("loc_8EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EC9")
    SetChrPos(0x10A, -16360, 0, 29320, 90)

    label("loc_8EC9")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#10703F(...Everyone.\x01",
            "If you're going inside, I'll stay here...)\x02",
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
        "#00300F(Well, behavin' the same as always, huh?)\x02",
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
    Jump("loc_900C")

    label("loc_8FA8")

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

    label("loc_900C")

    Return()

    # Function_38_8DD2 end

    def Function_39_900D(): pass

    label("Function_39_900D")

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

    # Function_39_900D end

    def Function_40_9075(): pass

    label("Function_40_9075")

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
        "#2P#2S──Excuse us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_68(5670, 1000, -47970, 2500)

    def lambda_924B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_924B)
    Sleep(200)

    def lambda_9263():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9263)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    def lambda_927F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_927F)

    def lambda_9294():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9294)
    Sleep(50)

    def lambda_92A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92A4)
    Sleep(50)

    def lambda_92BC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_92BC)
    Sleep(50)

    def lambda_92D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_92D4)

    def lambda_92E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_92E9)
    Sleep(200)

    def lambda_92FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_92FD)
    Sleep(500)

    def lambda_9311():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9311)

    def lambda_9322():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9322)
    Sleep(500)

    def lambda_9336():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9336)

    def lambda_9347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9347)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11705F#2723V#5P#40WAh...\x01",
            "Big sis, and everyone...!\x02",
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
        "#00000F#6PSo you were here, sister Cecil.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#6P#NI'm sorry.\x01",
            "Is it all right to visit her now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x136,
        (
            "#01309F#11PUh uh, it is.\x01",
            "I just changed her intravenous drip.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5920, 1000, -48010, 2000)

    def lambda_9491():
        OP_9B(0x1, 0xFE, 0xE1, 0x6D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9491)
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
            "#30WEhehe...\x01",
            "Thank you very much.\x02\x03",
            "You came on purpose\x01",
            "to see me...?\x02",
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
            "#00002F#12PYeah, we heard from Noｱl that\x01",
            "you had regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, I'm relieved, you\x01",
            "look better than what I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PYou're right. Her complexion\x01",
            "looks good too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WEhehe, I'm fine, fine.\x01",
            "I'm all right now.\x02\x03",
            "#11700FIt also seems that I'll be able to be moved \x01",
            "to a normal room in two or three days...\x02\x03",
            "#11709FAfter that, it'll be really soon\x01",
            "until I can leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PThat's no good, Fran.\x02\x03",
            "#10101FBecause your stamina has dropped,\x01",
            "you must rest quietly for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30WEhehe...\x01",
            "I'm a fragile person.\x02\x03",
            "#11708FInspector Donovan\x01",
            "protected me and...\x02\x03",
            "#11706F#40W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PMiss Fran...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6P...You don't have to worry\x01",
            "about that, dear Fran.\x02\x03",
            "#00301FIt was those guys' fault...\x01",
            "Those damn "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#5P#30WEhehe...yes.\x02\x03",
            "#11711FHowever, I have everyone\x01",
            "support and back up...\x02\x03",
            "#11706FI must do my best and recover...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PIt's ok, don't worry.\x02\x03",
            "#00000FIt's sad not being able to hear your voice,\x01",
            "but the reports are processed somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PNow please focus on recovering\x01",
            "and get healthy a lot.\x02\x03",
            "#00102FIf you do that, we too will\x01",
            "count on you non stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W...Yes.\x01",
            "Thank you very much.\x02\x03",
            "#11705FBy the way...\x01",
            "Big sis, I heard you went\x01",
            "back to the CGF...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PHave you heard it from mother?\x01",
            "...Yes, I thought about many things.\x02\x03",
            "#10112FI guess I'll be a little\x01",
            "sad since I won't get\x01",
            "your support, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11701F#5P#40WMrr, "a little" you say,\x01",
            "you're heartless...\x02\x03",
            "#11706F#50W...And substantially, big sis, you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9C20():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9C20)
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
        "#10111F#12PFran...!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x136,
        (
            "#01304F#11PShe is fine, it is only the intravenous\x01",
            "drip medicine that took effect.\x02\x03",
            "#01302FIt would be better to stop\x01",
            "talking and sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11706F#11P#40WI'm all right...\x01",
            "Mr. Lloyd and the others went\x01",
            "out of their way to come here...\x02\x03",
            "#11701FAlso, before she goes back to the CGF,\x01",
            "I have to tell big sis a foolproof winning way to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12P*sigh*, what the heck are you saying?\x02\x03",
            "#10108F...Everyone, I'm sorry.\x01",
            "Could we let her sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POf course.\x01",
            "...Fran, we'll come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PPlease sleep soundly.\x02\x03",
            "#00202FWhen you have regained your stamina,\x01",
            "I will bring you a cake as present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11712F#11P#40WAhaha...\x01",
            "Yes, I can't wait...\x02\x03",
            "#11704F#50W............\x02",
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
            "#10308F#6P...As expected, her stamina\x01",
            "seems to have really dropped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11PYes, she had a serious blood\x01",
            "transfusion during the surgery...\x02\x03",
            "#01300FHowever, she will get better.\x02\x03",
            "#01309FDon't worry, she will recover in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#12PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P...Let's go outside for now.\x02",
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

    def lambda_A252():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_A252)
    Sleep(50)

    def lambda_A26A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_A26A)
    WaitChrThread(0x136, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00005F#6PBy the way...\x02\x03",
            "#00001FAre Inspector Donovan and Miss\x01",
            "Ilya still no visitors allowed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#11P...They are.\x02\x03",
            "#01308FBut you seem to be acquaintances\x01",
            "of both of them, so...\x02\x03",
            "#01300FI will come along with you, so\x01",
            "would you like to check on them?\x02",
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
        "#00301F#5PMiss Cecil, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#11PUh uh...\x01",
            "Let's go then.\x02\x03",
            "#01300FRoom 302 just over there\x01",
            "is Mr. Donovan's.\x02\x03",
            "Ilya is in room 303...\x01",
            "Opposite of Shizuku's room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PGot it, shall we go?\x02",
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

    # Function_40_9075 end

    def Function_41_A503(): pass

    label("Function_41_A503")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_41_A503 end

    def Function_42_A538(): pass

    label("Function_42_A538")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xFA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_A538 end

    def Function_43_A55E(): pass

    label("Function_43_A55E")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_43_A55E end

    def Function_44_A58A(): pass

    label("Function_44_A58A")

    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x79E, 0x7D0, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_44_A58A end

    def Function_45_A5B0(): pass

    label("Function_45_A5B0")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_A5B0 end

    def Function_46_A5E5(): pass

    label("Function_46_A5E5")

    OP_9B(0x0, 0xFE, 0x4, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_46_A5E5 end

    def Function_47_A60B(): pass

    label("Function_47_A60B")

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
            "#2S#5PMr. Raymond?\x01",
            "I am coming in.\x07\x00\x02",
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

    def lambda_A7F5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_A7F5)

    def lambda_A80A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_A80A)
    Sleep(100)
    Sleep(100)

    def lambda_A821():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A821)

    def lambda_A832():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A832)
    Sleep(100)

    def lambda_A84A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A84A)
    Sleep(100)

    def lambda_A862():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A862)

    def lambda_A873():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A873)
    Sleep(100)

    def lambda_A88B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A88B)

    def lambda_A89C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A89C)
    Sleep(100)

    def lambda_A8B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A8B4)

    def lambda_A8C5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A8C5)
    Sleep(100)

    def lambda_A8DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A8DD)

    def lambda_A8EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A8EE)
    Sleep(100)

    def lambda_A906():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A906)
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
            "#6PMiss Cecil...\x01",
            "And you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PMr. Raymond...\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PYou were nursing him, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PAhaha...every now and then, I do\x01",
            "it instead of the Inspector's wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PAlthough I feel like if the Inspector\x01",
            "opened his eyes he'd yell at me\x01",
            ""what the hell are you loafing around!?"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#11PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11P...Indeed, it feels like\x01",
            "something he would say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PThat equipment...\x01",
            "Is it an artificial respirator?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PYes...it seems his respiratory\x01",
            "system was really hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf he somehow regained consciousness,\x01",
            "I think his recovery would speed up too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#30W............\x02",
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
            "#11PSomeone worthless like me\x01",
            "who at that terrible time\x01",
            "was just flustered...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PFurthermore, Fran was so badly hurt\x01",
            "she even had to undergo surgery,\x01",
            "and yet I had just some scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P...My good luck and impudence\x01",
            "are just so deplorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11PMr. Raymond...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11P...It's not your fault, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#11P...Mr. Raymond.\x01",
            "Why don't you take a break?\x02\x03",
            "#01301FHis condition is stable now\x01",
            "and we are doing our rounds too.\x02\x03",
            "You won't last if you don't\x01",
            "rest a little, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    ChrTalk(
        0xA,
        "#6PAhaha...thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHowever, the Inspector's wife\x01",
            "is going to come in a little, \x01",
            "so, until then, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#01306F#11P*sigh*...all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11P...Please, take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWe will come visiting again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYes... \x01",
            "I think the Inspector would be glad too.\x02",
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

    # Function_47_A60B end

    def Function_48_B013(): pass

    label("Function_48_B013")

    Sleep(600)
    Sound(107, 0, 100, 0)
    Return()

    # Function_48_B013 end

    def Function_49_B01D(): pass

    label("Function_49_B01D")

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
        (
            "#2S#11PSully?\x01",
            "Can I come in?\x07\x00\x02",
        )
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

    def lambda_B1E7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_B1E7)
    Sleep(50)

    def lambda_B1FF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1FF)

    def lambda_B214():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_B214)
    Sleep(50)

    def lambda_B228():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B228)
    Sleep(50)

    def lambda_B240():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B240)
    Sleep(50)

    def lambda_B258():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B258)
    Sleep(50)

    def lambda_B270():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B270)
    Sleep(50)

    def lambda_B288():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B288)
    Sleep(50)
    Sleep(100)

    def lambda_B2A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B2A3)

    def lambda_B2B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B2B4)
    Sleep(400)

    def lambda_B2C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B2C8)

    def lambda_B2D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B2D9)
    Sleep(400)

    def lambda_B2ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B2ED)

    def lambda_B2FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B2FE)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_B37F")

    ChrTalk(
        0x102,
        "#00108F#5P............\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3A2")

    label("loc_B37F")


    ChrTalk(
        0x102,
        "#00106F#5PSo you were here...\x02",
    )

    CloseMessageWindow()

    label("loc_B3A2")

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
        "#00208F#6P#NMiss Ilya...\x02",
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
            "#04206F#6P#30WWhat a peaceful and...pretty sleeping face, eh?\x02\x03",
            "#04208FShe always sleeps like a log,\x01",
            "with her hair all messed up...\x01",
            "And yet, only on such a time she...\x02\x03",
            "#04202FHa ha...\x01",
            "It's so unlike\x01",
            "Ilya Platiｲre...\x02",
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
        "#10301F#5P...How's her condition?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01303F#5P...Bone fractures in all her body\x01",
            "and damage to her internal organs.\x02\x03",
            "#01308FThe surgery was successful,\x01",
            "but she continues to be in a coma...\x02\x03",
            "#01301FAt present she must rely\x01",
            "on a life-support system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...It's that bad...\x02",
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
            "#04202F#6P#30W...Even if she wakes up, they say\x01",
            "that a full recovery is desperate...\x02\x03",
            "Can you believe it?\x01",
            "That that Miss Ilya will never\x01",
            "stand on stage again...?\x02\x03",
            "#04208FAnd that too was...\x01",
            "Because she protected someone like me...\x02\x03",
            "#04206F#40W...Such a thing...\x01",
            "...Such a thing shouldn't have...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B81E():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B81E)
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
        "#04205F#6P#40W......Eh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#5PIt's all right...it will be all right.\x02\x03",
            "I am who knows\x01",
            "best about Ilya.\x02\x03",
            "#01308FNo matter the adversities, she never gives up\x01",
            "and just keeps gazing forward...\x02\x03",
            "#01302FThat is who Ilya Platiｲre is.\x02",
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
            "#00004F#5P──I think so too.\x02\x03",
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
            "#00102FI think that Miss Ilya's greediness\x01",
            "is what can realize that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00204F#6P#NAs long as there is a stage...\x01",
            "I am sure Miss Ilya will come back.\x02\x03",
            "#00202FIt is strange, but I think it is like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#04205F#6P#30W......ah......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PYeah...\x02\x03",
            "#00300FFor now, believe in the Goddess and in\x01",
            "Miss Ilya and do what only you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PAside for today, don't you think\x01",
            "you shouldn't skip stage practice?\x02\x03",
            "#10302FThat way, she'd be lured too\x01",
            "and wake up to come there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PYes...for sure!\x02\x03",
            "#10102FGetting lured by an enjoyable stage\x01",
            "she'd open her eyes for sure...!\x02",
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
            "#04204F#6P......Thanks.\x01",
            "I've cheered up a bit.\x02\x03",
            "#04208FYou're right...\x01",
            "We must get our act together...\x02\x03",
            "Sis Rixia too...\x01",
            "Has gone away, so...\x02",
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
            "If possible, couldn't you\x01",
            "find where sis Rixia is...?\x02\x03",
            "#04208FNo matter the circumstances she had,\x01",
            "sis Rixia is sis Rixia...\x02\x03",
            "#04201FAlso, if sis Rixia comes back,\x01",
            "I think Miss Ilya too would get better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P──All right.\x02\x03",
            "#00000FOn the name of the Special Support\x01",
            "Section, we'll find her out for sure.\x02",
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
            "#01302F#12P...Thank you, everyone.\x02\x03",
            "I think that now Sully too will be \x01",
            "able to get back her cheerfulness.\x02\x03",
            "#01304FI also...\x01",
            "Have been encouraged a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5PSister Cecil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PAs we suspected, her condition\x01",
            "is quite serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01306F#12PYes... \x01",
            "Honestly, I am worried.\x02\x03",
            "#01308F...But even so,\x01",
            "I really believe in Ilya.\x02\x03",
            "#01302FAlso, I think that the more people believe\x01",
            "in her and the more she will respond to that.\x02",
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
            "#00204F#5PIndeed, that could be\x01",
            "the case with Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PHowever, for that to happen...\x01",
            "As expected, Rixia is the key, eh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C289():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C289)
    WaitChrThread(0x105, 2)
    Sleep(150)

    ChrTalk(
        0x105,
        "#10300F#5PLloyd, can you find her?\x02",
    )

    CloseMessageWindow()

    def lambda_C2C5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C2C5)
    Sleep(150)

    def lambda_C2D5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C2D5)
    Sleep(50)

    def lambda_C2E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C2E5)
    Sleep(50)

    def lambda_C2F5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C2F5)
    Sleep(50)

    def lambda_C305():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C305)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x101,
        (
            "#00003F#6P...Frankly, I don't know.\x02\x03",
            "#00008FIf she's seriously hiding,\x01",
            "finding her will be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PYou're right...\x02\x03",
            "#10108FLikewise, it's not really clear\x01",
            "if the missing "Heiyue" are in\x01",
            "the autonomous state or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PIt's also possible she\x01",
            "went back to Calvard...\x02\x03",
            "#00300FHowever, after seeing Sully\x01",
            "counting so much on us, we\x01",
            "can't even give up, can we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah──of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PWe should pay attention to\x01",
            "the "Heiyue" whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PI too will constantly\x01",
            "check the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01304F#12PUh uh...thank you, really.\x02\x03",
            "#01300FI will return to the nurse center.\x01",
            "What will you do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5BE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5BE)
    Sleep(150)

    def lambda_C5CE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C5CE)
    Sleep(50)

    def lambda_C5DE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C5DE)
    Sleep(50)

    def lambda_C5EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C5EE)
    Sleep(50)

    def lambda_C5FE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C5FE)
    Sleep(50)

    def lambda_C60E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C60E)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00002F#5PWell, we still have work to do,\x01",
            "so it's time to say goodbye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PThank you for\x01",
            "having guided us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#01309F#12PUh uh, likewise.\x02\x03",
            "#01302FIt is a terrible situation, but...\x01",
            "Let's do each other's best.\x02\x03",
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

    def lambda_C77B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C77B)
    Sleep(350)

    def lambda_C78B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C78B)
    Sleep(150)

    def lambda_C79B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C79B)
    Sleep(250)

    def lambda_C7AB():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C7AB)
    Sleep(150)

    def lambda_C7BB():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C7BB)
    Sleep(150)

    def lambda_C7CB():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C7CB)
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

    def lambda_C88A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C88A)
    Sleep(150)

    def lambda_C89A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C89A)
    Sleep(50)

    def lambda_C8AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C8AA)
    Sleep(50)

    def lambda_C8BA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C8BA)
    Sleep(50)

    def lambda_C8CA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C8CA)
    Sleep(50)

    def lambda_C8DA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C8DA)
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
            "#00006F#6PReally...\x01",
            "It's time to brace our legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PYes...you're right.\x02\x03",
            "#00108FIn order to also retrieve the smiles of the persons \x01",
            "who have been damaged mentally and physically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P............\x01",
            "(Brace our legs, eh?)\x02",
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

    # Function_49_B01D end

    def Function_50_CA80(): pass

    label("Function_50_CA80")

    OP_9B(0x0, 0xFE, 0x5, 0xFA, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x5, 0xC8, 0x1F4, 0x0)
    Return()

    # Function_50_CA80 end

    def Function_51_CA9F(): pass

    label("Function_51_CA9F")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1F4, 0x0)
    Return()

    # Function_51_CA9F end

    def Function_52_CAAF(): pass

    label("Function_52_CAAF")

    OP_96(0x136, 0xFFFE7C08, 0x0, 0xFFFFED7C, 0x4B0, 0x0)
    Return()

    # Function_52_CAAF end

    def Function_53_CAC4(): pass

    label("Function_53_CAC4")

    OP_95(0xFE, -97730, 0, -3800, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_53_CAC4 end

    def Function_54_CAE0(): pass

    label("Function_54_CAE0")

    OP_95(0xFE, -100440, 0, -7000, 1500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_CAE0 end

    def Function_55_CAFC(): pass

    label("Function_55_CAFC")

    OP_95(0xFE, -101020, 0, -6010, 1500, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_CAFC end

    def Function_56_CB18(): pass

    label("Function_56_CB18")

    OP_95(0xFE, -98500, 0, -3400, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_56_CB18 end

    def Function_57_CB34(): pass

    label("Function_57_CB34")

    OP_95(0xFE, -99600, 0, -3350, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_57_CB34 end

    def Function_58_CB50(): pass

    label("Function_58_CB50")

    OP_95(0xFE, -100570, 0, -4650, 1500, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_58_CB50 end

    def Function_59_CB6C(): pass

    label("Function_59_CB6C")

    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xBB8, 0x7D0, 0x1)
    Return()

    # Function_59_CB6C end

    def Function_60_CBB8(): pass

    label("Function_60_CBB8")

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
            "Who is it?\x01",
            "You can come in.\x02",
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

    def lambda_CDAD():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CDAD)

    def lambda_CDC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDC2)
    Sleep(100)

    def lambda_CDD6():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CDD6)

    def lambda_CDEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDEB)
    Sleep(100)

    def lambda_CDFF():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CDFF)

    def lambda_CE14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CE14)
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
            "#11605F#11PEeh, if it isn't the younger brother!?\x02\x03",
            "#11602FAnd also...\x01",
            "Wazy, was it?\x02",
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
            "#00002F#5PMiss Ilya...\x01",
            "It's really been a long time.\x02\x03",
            "#00006FI'm sorry, we came to visit\x01",
            "and yet we're empty-handed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11609F#11POh, jeez!\x01",
            "Don't worry about that!\x02\x03",
            "#11602FNow now, you three.\x01",
            "Come here.\x02\x03",
            "#11605FOh, you can help yourself to the\x01",
            "sweets from the fans, you know?\x02\x03",
            "#11609FIf they're cookies, I think\x01",
            "they haven't expired yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThen, excuse us.\x02",
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
            "#11603F#11PI see...\x01",
            "You too have got it hard in many ways.\x02\x03",
            "#11601FAlthough I had heard that\x01",
            "Crossbell itself had become\x01",
            "a really troublesome place.\x02",
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
            "#10406F#6PWell, troublesome is indeed the\x01",
            "only way I'd describe the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11606F#11PUhhm, I can't help but being irritated\x01",
            "that I can't move my legs, you see...\x02\x03",
            "#11608FBut I'd have liked to ascertain the\x01",
            "Arc-en-ciel condition with my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WUhm, Miss Ilya.\x02\x03",
            "#00008FYour body, I mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11605F#11PAh, yes.\x02\x03",
            "#11603FDoctor Seiland says that at the \x01",
            "present time, she doesn't know\x01",
            "if I'll go back to walk or not.\x02\x03",
            "#11600FWell, she didn't state that\x01",
            "it's 100% impossible, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#40W...I...see.\x02",
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
            "#11606F#11POh, jeez, if you do that face\x01",
            "I'll get depressed too, you know.\x02\x03",
            "#11601FListen── if you're convinced that\x01",
            "it's impossible, just with that the\x01",
            "possibility will vanish, you know?\x02",
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
            "#11604F#11PIt's the same with the stage...\x01",
            "There's absolutely an "answer" somewhere.\x02\x03",
            "#11600FNo matter how painful or hopeless,\x01",
            "there's absolutely a ray of hope.\x02\x03",
            "#11609FFor sure, as long as you don't give up.\x02",
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
        "#00204F#12PUh uh...\x02",
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
            "#11606F#11PUuhm, I don't think \x01",
            "I'm so amazing.\x02\x03",
            "#11601FForemost, from what I hear, you're\x01",
            "the ones who have it tough, right?\x02",
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
            "#00206F#12P...True, if we think about it normally,\x01",
            "it is a dreadfully difficult path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11604F#11PIt's the same, the same.\x02\x03",
            "#11600F"Man" is a living being who can try his utmost\x01",
            "best if it's for what it's important to him.\x02\x03",
            "To varying degrees...\x01",
            "I think that's man's strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PThe strength of the living being called "man"...\x02",
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
            "#11602F#11PWell, even if I'm among them,\x01",
            "I think I'm a pretty greedy person.\x02\x03",
            "Even so, I think that other\x01",
            "people are essentially like that.\x02\x03",
            "#11604FEven our troupe members...\x02\x01",
            "#11600F──And Rixia too, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F#6PMiss Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11602F#11PHu hu, can you pass this\x01",
            "to her when you meet?\x02\x03",
            "#11604F"──What's the most\x01",
            "precious thing to you?"\x02\x03",
            ""Can you be in front of that precious thing\x01",
            "and not help doing your best for it?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P...Understood.\x02\x03",
            "#00000FWhen I'll be able to see Rixia,\x01",
            "I'll tell her those words for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11609F#11PYes, I'm counting on you!\x02",
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

    # Function_60_CBB8 end

    def Function_61_DB4E(): pass

    label("Function_61_DB4E")

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

    def lambda_DBEA():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DBEA)

    def lambda_DBFF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBFF)
    Sleep(50)

    def lambda_DC17():
        OP_9B(0x0, 0xFE, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DC17)
    Sleep(50)
    Sleep(50)
    Sleep(100)

    def lambda_DC35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DC35)

    def lambda_DC46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DC46)
    Sleep(400)

    def lambda_DC5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DC5A)
    Sleep(800)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    OP_0D()

    def lambda_DC81():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DC81)
    Sleep(50)

    def lambda_DC91():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DC91)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10404F#12PHa ha...\x01",
            "Really, she's incredible.\x02\x03",
            "#10402FNot for nothing she's\x01",
            "called the "Flame Dancer".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5P...Rather, she is the play's\x01",
            ""Sun Princess" herself.\x02\x03",
            "#00208FAfter having been brought here,\x01",
            "I talked to her many times...\x02\x03",
            "#00202FShe and Miss Cecil\x01",
            "really cheered me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00008F...It would be nice if we could\x01",
            "locate Rixia too somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, that could only\x01",
            "be a fated chance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_DEDB")

    ChrTalk(
        0x103,
        (
            "#00202F#5PShould we go back\x01",
            "and speak to Miss Fran?\x02",
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
    Jump("loc_DF53")

    label("loc_DEDB")


    ChrTalk(
        0x103,
        (
            "#00202F#5PShould we go visit \x01",
            "Inspector Donovan too?\x02",
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

    label("loc_DF53")

    Return()

    # Function_61_DB4E end

    def Function_62_DF54(): pass

    label("Function_62_DF54")

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
        "#6POh, could it be time to measure your temperature?\x02",
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

    def lambda_E0D9():
        OP_95(0x101, -53180, 0, -49830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0D9)

    def lambda_E0F3():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0F3)
    Sleep(500)

    def lambda_E107():
        OP_95(0x105, -53100, 0, -50830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E107)

    def lambda_E121():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E121)
    Sleep(600)

    def lambda_E135():
        OP_95(0x103, -51840, 50, -50110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E135)

    def lambda_E14F():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E14F)
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
            "Ooh, if it isn't the\x01",
            "Support Section's guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PHa ha, long time no see,\x01",
            "Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10405F#12POh, who is the beautiful lady?\x02\x03",
            "#10409FHu hu, could we have\x01",
            "interrupted a date...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "What the heck are you saying all\x01",
            "of a sudden after we just met again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PWazy, listen here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#2PShe is Mrs. Fara,\x01",
            "Inspector Donovan's wife.\x02\x03",
            "She is been staying here for a while\x01",
            "after she came visit him some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PUhuhu, nice to meet you.\x01",
            "Thank you for always taking care of my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PEvery now and then I heard stories\x01",
            "about you from my husband and Tio.\x01",
            "You all seem interesting persons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHu hu, I'm really flattered for the compliment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P(I think that maybe she isn't\x01",
            "making a compliment...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, we have a great deal of things to talk about...\x01",
            "Could you explain me the situation for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes, all right.\x02",
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
            "#1PHm...more serious things are\x01",
            "happening than I thought of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PAlso, from what I hear, even the\x01",
            "fact that I met you here would be \x01",
            "better to not be reported to HQ, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYes, it would really help us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, I'm fine with either options,\x01",
            "since it's Lloyd who's a wanted criminal.\x02",
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
            "#00001F#12PA-Anyway.\x01",
            "...Inspector, what's the situation\x01",
            "inside Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWell, I too have only heard about it\x01",
            "from Raymond who came to visit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIt seems that Crossbell Police\x01",
            "has been completely taken in\x01",
            "as a State Guard lower branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIt seems the business outline didn't\x01",
            "change, but now it's been flushed \x01",
            "out to just do odd jobs in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FSo it really is like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, considering the present situation,\x01",
            "it probably can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PBut... Wasn't such a system\x01",
            "opposed as I expect?\x02\x03",
            "#00003FSetting aside Vice Chief Pierre,\x01",
            "I can't think that Chief Sergei or\x01",
            "Mr. Dudley silently complied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PYeah, just between you and me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIt seems that Sergei, Dudley\x01",
            "and policemen including even\x01",
            "Raymond are acting in secret.\x02",
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
        "#00205FThe Chief and the others are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PIn utmost and absolute secrecy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWhile pocketing their pride, they're \x01",
            "probably looking for a way to somehow\x01",
            "break out of the present situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PI guess that everyone staying\x01",
            "silent was only a stratagem.\x02\x03",
            "#10404FHu hu, maybe we can see some hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah. Making contact with them\x01",
            "now seems difficult, so...\x01",
            "It appears it's better to leave the city to them.\x02\x03",
            "#00003FWe should look for means\x01",
            "to break out of the current\x01",
            "situation in our own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PExactly right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PIt'll probably be quite difficult in practice,\x01",
            "but somehow try to do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PWhen I go back, I'll immediately\x01",
            "join with Sergei and the others and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PWell, my dear...\x01",
            "For now you will leave the matter to them, Raymond \x01",
            "and the others and heal your body at leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PI will not let you do anything reckless\x01",
            "until you have completely recovered.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1PH-Hm...I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P(Ha ha...\x01",
            "She spoke her mind to him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Even the Inspector seems\x01",
            "to be no match for his wife.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12P(Hu hu, the Inspector too is lucky to\x01",
            "have been blessed with a good wife.)\x02",
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

    # Function_62_DF54 end

    def Function_63_EFF3(): pass

    label("Function_63_EFF3")

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

    def lambda_F0E0():
        OP_95(0x101, -15360, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F0E0)

    def lambda_F0FA():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F0FA)
    Sleep(600)

    def lambda_F10E():
        OP_95(0x103, -14800, 0, 7940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F10E)

    def lambda_F128():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F128)
    Sleep(600)

    def lambda_F13C():
        OP_95(0x105, -14980, 0, 10240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F13C)

    def lambda_F156():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F156)
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

    def lambda_F1CB():

        label("loc_F1CB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F1CB")

    QueueWorkItem2(0x101, 2, lambda_F1CB)

    def lambda_F1DD():

        label("loc_F1DD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F1DD")

    QueueWorkItem2(0x105, 2, lambda_F1DD)

    def lambda_F1EF():

        label("loc_F1EF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F1EF")

    QueueWorkItem2(0x103, 2, lambda_F1EF)
    OP_95(0x8, -13480, 0, 9000, 3000, 0x0)
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, Fran...\x01",
            "Have you finished packing your things?\x02",
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
            "#00202F#6PIt has been a long time since we\x01",
            "saw Miss Fran in her uniform too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01909F#11PUh uh, it's been like that for me too.\x02\x03",
            "#01900FEveryone, did you go to\x01",
            "visit Inspector Donovan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, we just finished.\x02\x03",
            "#00000FAre you going too, Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01904F#11PYes, I was thinking to\x01",
            "greet him before I\x01",
            "leave the hospital.\x02\x03",
            "#01902FI must thank him again,\x01",
            "since he especially saved\x01",
            "me from a dangerous situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PHa ha, I see.\x01",
            "Then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01909F#11PYes, see you lateeer!\x02",
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

    def lambda_F592():
        OP_95(0xFE, -19090, 0, 8900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F592)

    def lambda_F5AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F5AC)
    WaitChrThread(0x8, 2)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_F5D8():
        OP_95(0xFE, -16200, 0, 8800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5D8)
    Sleep(50)

    def lambda_F5F5():
        OP_95(0xFE, -14800, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F5F5)
    Sleep(50)

    def lambda_F612():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F612)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    SetScenarioFlags(0x1A1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_END)), "loc_F6C7")

    ChrTalk(
        0x105,
        (
            "#10402F#5PWell then, should we go back to the\x01",
            "Merkabah after she finishes her greetings?\x02",
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
    Jump("loc_F757")

    label("loc_F6C7")


    ChrTalk(
        0x105,
        (
            "#10402F#5PAlright, let's go visit\x01",
            "Miss Ilya then,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's go.\x02",
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

    label("loc_F757")

    Return()

    # Function_63_EFF3 end

    def Function_64_F758(): pass

    label("Function_64_F758")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xE1, 0x320, 0x3E8, 0x0)

    def lambda_F773():

        label("loc_F773")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F773")

    QueueWorkItem2(0xFE, 2, lambda_F773)
    Return()

    # Function_64_F758 end

    def Function_65_F781(): pass

    label("Function_65_F781")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xA0, 0x5DC, 0x3E8, 0x0)

    def lambda_F79C():

        label("loc_F79C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F79C")

    QueueWorkItem2(0xFE, 2, lambda_F79C)
    Return()

    # Function_65_F781 end

    def Function_66_F7AA(): pass

    label("Function_66_F7AA")

    Sleep(1850)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    Return()

    # Function_66_F7AA end

    def Function_67_F7BD(): pass

    label("Function_67_F7BD")

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
            "#01400F...Mr. Sergei, it seems you have\x01",
            "taken over the "Cryptids" case.\x02\x03",
            "#01403FOriginally, it should be me, as a Bracer, that\x01",
            "should go investigate and exterminate them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01000FNo need to worry.\x02\x03",
            "#01003FRegarding the Cryptids, we're coping\x01",
            "with them by sharing the work.\x02\x03",
            "#01000FWell, just leave that to\x01",
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
            "#12P#01002FWell, they've grown up too, you\x01",
            "don't have to be worried so much.\x02\x03",
            "#01004FAlso, usually you can't\x01",
            "come to visit her.\x02\x03",
            "#01002FAt least on such a time,\x01",
            "it's a father's job to stay\x01",
            "close to his daugher.\x02",
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
            "#11P#11209FUh uh...\x01",
            "Thank you very much, Mr. Chief.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 160, -1, -1)
    SetChrName("Lloyd's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "......Excuse us.\x07\x00\x02",
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

    def lambda_FC1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_FC1B)
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
        "#01405FYou guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#01005FWhat, did you come?\x02\x03",
            "#01006FJeez, because we're busy\x01",
            "I told you it would've been\x01",
            "fine just me visiting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FS-Sorry, Chief.\x02\x03",
            "#00000FWe were very\x01",
            "worried about\x01",
            "Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FUh uh, everyone...\x01",
            "Thank you for coming on purpose.\x02",
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
        "#6P#00105FShizuku, your eyes are open...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FUhm, could it be\x01",
            "that you can see...?\x02",
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
            "#01403F...In this surgery, Professor\x01",
            "Seiland did her very best\x01",
            "as the operating surgeon.\x02\x03",
            "#01400FIn outline, the surgery was a success, but...\x01",
            "It's not a full recovery.\x02\x03",
            "#01408FIt seems that she has finally recovered to a\x01",
            "degree that she can perceive light around her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FI...see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FWhat should I say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11200FUh uh, please don't mind it.\x01",
            "I'm fine.\x02\x03",
            "#11202FMore importantly, father...\x01",
            "I would like to go on the roof with everyone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)

    ChrTalk(
        0x19,
        (
            "#6P#01002FYeah, that would be nice.\x02\x03",
            "#01004FThere're also so many people\x01",
            "gathered in the sickroom that\x01",
            "breathing fresh air could be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FB-But, Shizuku, you\x01",
            "just had a surgery, so\x01",
            "you shouldn't over do it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F...No, according to the doctor, there won't be\x01",
            "that much of a negative effect unless she's \x01",
            "exposed to strong light for a long time.\x02\x03",
            "#01400FWith how the weather is today, there shouldn't \x01",
            "be any problems even if she goes out.\x02\x03",
            "#01403F...I'll go get permission.\x01",
            "I'm sorry but, help\x01",
            "Shizuku prepare.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_102DB():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_102DB)

    def lambda_102F5():

        label("loc_102F5")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_102F5")

    QueueWorkItem2(0x19, 2, lambda_102F5)

    def lambda_10307():

        label("loc_10307")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_10307")

    QueueWorkItem2(0x101, 2, lambda_10307)

    def lambda_10319():

        label("loc_10319")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_10319")

    QueueWorkItem2(0x102, 2, lambda_10319)

    def lambda_1032B():

        label("loc_1032B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1032B")

    QueueWorkItem2(0x103, 2, lambda_1032B)

    def lambda_1033D():

        label("loc_1033D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1033D")

    QueueWorkItem2(0x104, 2, lambda_1033D)

    def lambda_1034F():

        label("loc_1034F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1034F")

    QueueWorkItem2(0x109, 2, lambda_1034F)

    def lambda_10361():

        label("loc_10361")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_10361")

    QueueWorkItem2(0x105, 2, lambda_10361)
    BeginChrThread(0x1A, 1, 0, 74)
    WaitChrThread(0xF, 1)

    def lambda_1037D():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1037D)

    def lambda_10397():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_10397)
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
            "#12P#10304FOh boy, even that "Divine Blade of Wind"\x01",
            "seems to be very indulgent towards his daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11209FFather is always\x01",
            "very kind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10478():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10478)
    Sleep(50)

    def lambda_10488():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10488)
    Sleep(50)

    def lambda_10498():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10498)
    Sleep(50)

    def lambda_104A8():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_104A8)
    Sleep(50)

    def lambda_104B8():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_104B8)
    Sleep(50)

    def lambda_104C8():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_104C8)
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
            "#01004FWell, that's the story, and since\x01",
            "we're here, why don't we tag along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes...you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P#11202FUh uh, I'm in your care, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_67_F7BD end

    def Function_68_105AB(): pass

    label("Function_68_105AB")


    def lambda_105B0():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105B0)

    def lambda_105CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_105CA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_105E3():
        OP_95(0xFE, -99000, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105E3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_68_105AB end

    def Function_69_10604(): pass

    label("Function_69_10604")


    def lambda_10609():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10609)

    def lambda_10623():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10623)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1063C():
        OP_95(0xFE, -100940, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1063C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_69_10604 end

    def Function_70_1065D(): pass

    label("Function_70_1065D")


    def lambda_10662():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10662)

    def lambda_1067C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1067C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_10695():
        OP_95(0xFE, -98340, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10695)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_1065D end

    def Function_71_106B6(): pass

    label("Function_71_106B6")


    def lambda_106BB():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_106BB)

    def lambda_106D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_106D5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_106EE():
        OP_95(0xFE, -100740, 0, 51800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_106EE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_71_106B6 end

    def Function_72_1070F(): pass

    label("Function_72_1070F")


    def lambda_10714():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10714)

    def lambda_1072E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1072E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_10747():
        OP_95(0xFE, -99240, 0, 50800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10747)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_1070F end

    def Function_73_10768(): pass

    label("Function_73_10768")


    def lambda_1076D():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1076D)

    def lambda_10787():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10787)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_107A0():
        OP_95(0xFE, -100740, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_107A0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_73_10768 end

    def Function_74_107C1(): pass

    label("Function_74_107C1")

    Sleep(2600)
    Sound(107, 0, 100, 0)
    Sleep(1100)
    Sound(107, 0, 100, 0)
    Return()

    # Function_74_107C1 end

    def Function_75_107D4(): pass

    label("Function_75_107D4")

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
            "#12P#01002F...Then, I'll\x01",
            "return to the\x01",
            "Support Section.\x02\x03",
            "#01004FArios, keep staying near\x01",
            "Shizuku for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01403F...Yes, I'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FThank you for your hard work, Chief.\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "#01005FYeah, as for you all, keep proceeding\x01",
            "with the "Cryptids" investigation.\x02\x03",
            "#01002FWhile the "Divine Blade of Wind"\x01",
            "can't move, you have to increase your\x01",
            "achievements as much as possible.\x02",
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
        "#01004FEh eh, bye then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    ChrTalk(
        0xD,
        (
            "#5P#11202FTh...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)
    Sleep(500)
    OP_93(0x19, 0xB4, 0x1F4)

    def lambda_10B82():
        OP_95(0xFE, -99820, 0, 54000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10B82)
    WaitChrThread(0x19, 1)

    def lambda_10BA0():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10BA0)

    def lambda_10BBA():

        label("loc_10BBA")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10BBA")

    QueueWorkItem2(0xF, 2, lambda_10BBA)

    def lambda_10BCC():

        label("loc_10BCC")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10BCC")

    QueueWorkItem2(0x101, 2, lambda_10BCC)

    def lambda_10BDE():

        label("loc_10BDE")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10BDE")

    QueueWorkItem2(0x102, 2, lambda_10BDE)

    def lambda_10BF0():

        label("loc_10BF0")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10BF0")

    QueueWorkItem2(0x103, 2, lambda_10BF0)

    def lambda_10C02():

        label("loc_10C02")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10C02")

    QueueWorkItem2(0x104, 2, lambda_10C02)

    def lambda_10C14():

        label("loc_10C14")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10C14")

    QueueWorkItem2(0x109, 2, lambda_10C14)

    def lambda_10C26():

        label("loc_10C26")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_10C26")

    QueueWorkItem2(0x105, 2, lambda_10C26)
    Sleep(1500)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_10C45():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10C45)

    def lambda_10C5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_10C5F)
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
            "#5P#00306FOh boy, what a thing to say just in\x01",
            "front of the "Divine Blade of Wind".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHu hu, he's always the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01402FUh uh, there's no doubt\x01",
            "he's the excellent superior\x01",
            "from my officer days.\x02\x03",
            "#01403F...I ask you too to take care\x01",
            "of the "Cryptids" investigation.\x02\x03",
            "#01400FI plan to return tomorrow\x01",
            "and join, but until then,\x01",
            "help out Scott and the others.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10E1F():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10E1F)
    Sleep(50)

    def lambda_10E2F():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10E2F)
    Sleep(50)

    def lambda_10E3F():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10E3F)
    Sleep(50)

    def lambda_10E4F():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10E4F)
    Sleep(50)

    def lambda_10E5F():
        TurnDirection(0x105, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10E5F)
    Sleep(50)

    def lambda_10E6F():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10E6F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x103,
        "#12P#00200FYes, we will do what we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P#11202FEveryone too, really,\x01",
            "thank you very much.\x02\x03",
            "#11209FI'm glad I could talk about many things.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10F2C():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10F2C)
    Sleep(50)

    def lambda_10F3C():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10F3C)
    Sleep(50)

    def lambda_10F4C():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10F4C)
    Sleep(50)

    def lambda_10F5C():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10F5C)
    Sleep(50)

    def lambda_10F6C():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10F6C)
    Sleep(50)

    def lambda_10F7C():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F7C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#12P#10100FNo, we too had a great time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWe'll come again, so be well.\x02",
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

    # Function_75_107D4 end

    def Function_76_1104C(): pass

    label("Function_76_1104C")

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
            "#00005FWhat? This should be\x01",
            "Shizuku's room, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FMaybe she's outside now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FHowever, we didn't spot her\x01",
            "in this hospital ward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FWell, why not lookin' for her, then?\x02",
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

    # Function_76_1104C end

    def Function_77_11298(): pass

    label("Function_77_11298")

    StopBGM(0xBB8)

    ChrTalk(
        0xB,
        "#11603FBy the way──\x02",
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
            "#11602F...A certain someone who's over there\x01",
            "seems to still be worried, eh?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11451")
    SetChrPos(0x109, -100670, 0, -7660, 90)
    Jump("loc_11498")

    label("loc_11451")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11477")
    SetChrPos(0x105, -100670, 0, -7660, 90)
    Jump("loc_11498")

    label("loc_11477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11498")
    SetChrPos(0x10A, -100670, 0, -7660, 90)

    label("loc_11498")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00005FM-Miss Ilya...?\x02",
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
            "#11P#11604FHu hu, I don't know who it is, but\x01",
            "it seems a very, very shy person.\x02\x03",
            "#11609FAlthough, it has probably a reserved\x01",
            "personality and yet it's whimsical\x01",
            "and has an outrageous body㈱\x02",
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
        "#6P#00206F(She has completely recognised her.)\x02",
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
            "#11P#11603F──I don't know who it is, but\x01",
            "I've already started rehabilitation.\x02\x03",
            "#11601FIf this person misses practice too much,\x01",
            "I'll immediately catch up and surpass it.\x02\x03",
            "#11604FIf this person doesn't want to be left behind,\x01",
            "it's better it goes settle things quickly.\x02",
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
            "#11P#11604FAlso, it has to be very careful.\x02\x03",
            "#11600FNo matter how strong it is, it has\x01",
            "to keep in mind that she's a woman.\x02\x03",
            "#11603FLike on our stage, there's also a\x01",
            "strength that only a woman can show...\x02\x03",
            "#11600FI'm sure that will protect you.\x02",
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
        "#12P#00102FMiss Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#11604FHu hu, I took a lot of your free time, eh?\x02\x03",
            "#11600F──Younger brother, and you guys, be careful too.\x01",
            "Don't you make Cecil sad, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...Yes!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B44")
    BeginChrThread(0x109, 1, 0, 79)
    WaitChrThread(0x109, 1)
    Jump("loc_11B7D")

    label("loc_11B44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B63")
    BeginChrThread(0x105, 1, 0, 79)
    WaitChrThread(0x105, 1)
    Jump("loc_11B7D")

    label("loc_11B63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B7D")
    BeginChrThread(0x10A, 1, 0, 79)
    WaitChrThread(0x10A, 1)

    label("loc_11B7D")

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
            "#6P#00006FUhmm...sorry.\x02\x03",
            "#00008FI didn't think she\x01",
            "could notice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FDear Rixia, you completely concealed\x01",
            "your presence, and yet she...eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#30WUh uh...\x01",
            "After all, Miss Ilya is a genius...\x02\x03",
            "#10704F#30WI think she probably knew immediately that it was\x01",
            "me from my faint respiration and footsteps sounds.\x02\x03",
            "Matching our respiration is\x01",
            "something we always do on stage...\x02\x03",
            "#10716F#30WReally...except when it comes to the stage,\x01",
            "she's a lazybone and irresponsible...\x02",
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
        (
            "#6P#00204FReally...\x01",
            "Miss Ilya is Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11E22")

    ChrTalk(
        0x109,
        (
            "#6P#10109F*chuckle*...\x01",
            "But...I'm glad for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11ECA")

    label("loc_11E22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11E70")

    ChrTalk(
        0x105,
        (
            "#6P#10409FHu hu...\x01",
            "I keep getting surprised by her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11ECA")

    label("loc_11E70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11ECA")

    ChrTalk(
        0x10A,
        (
            "#6P#00602FHmph...\x01",
            "Nothing less expected from Miss Ilya, I could say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11ECA")

    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    OP_93(0x106, 0x10E, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10704FThis has──\x01",
            "Strengthened my resolve too.\x02\x03",
            "#10702FLet's go, everyone...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYes...!\x02",
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

    # Function_77_11298 end

    def Function_78_11FB5(): pass

    label("Function_78_11FB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11FF1")
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(500)
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(800)
    Jump("Function_78_11FB5")

    label("loc_11FF1")

    Return()

    # Function_78_11FB5 end

    def Function_79_11FF2(): pass

    label("Function_79_11FF2")

    SetChrPos(0xFE, -16470, 0, 25770, 0)

    def lambda_12008():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12008)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12038")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 80)
    Jump("loc_120C3")

    label("loc_12038")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1205C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 81)
    Jump("loc_120C3")

    label("loc_1205C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12080")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 82)
    Jump("loc_120C3")

    label("loc_12080")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120A4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 83)
    Jump("loc_120C3")

    label("loc_120A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120C3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 84)

    label("loc_120C3")

    Return()

    # Function_79_11FF2 end

    def Function_80_120C4(): pass

    label("Function_80_120C4")

    OP_95(0xFE, -16340, 0, 28470, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 29900, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_80_120C4 end

    def Function_81_120F4(): pass

    label("Function_81_120F4")

    OP_95(0xFE, -16360, 0, 29870, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 31030, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_81_120F4 end

    def Function_82_12124(): pass

    label("Function_82_12124")

    OP_95(0xFE, -16400, 0, 27970, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 28800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_82_12124 end

    def Function_83_12154(): pass

    label("Function_83_12154")

    OP_95(0xFE, -16360, 0, 30550, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_83_12154 end

    def Function_84_12170(): pass

    label("Function_84_12170")

    OP_95(0xFE, -16360, 0, 29320, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_84_12170 end

    def Function_85_1218C(): pass

    label("Function_85_1218C")

    StopBGM(0x7D0)
    Sleep(2000)
    Sleep(10)
    PlayBGM("ed7563", 0)
    Return()

    # Function_85_1218C end

    def Function_86_1219C(): pass

    label("Function_86_1219C")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xB, 0x2)
    OP_68(-98530, 900, -5100, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_1229E")
    SetChrPos(0x101, -99960, 0, -5280, 90)
    SetChrPos(0x102, -99960, 0, -6600, 90)
    SetChrPos(0x103, -100870, 0, -4700, 90)
    SetChrPos(0x104, -100870, 0, -6000, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12248")
    SetChrPos(0x109, -100670, 0, -7360, 90)
    Jump("loc_1228F")

    label("loc_12248")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1226E")
    SetChrPos(0x105, -100670, 0, -7360, 90)
    Jump("loc_1228F")

    label("loc_1226E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1228F")
    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_1228F")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_1241B")

    label("loc_1229E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -99960, 0, -6000, 90)
    SetChrPos(0x102, -99960, 0, -4700, 90)
    SetChrPos(0x103, -99960, 0, -7360, 90)
    SetChrPos(0x104, -100870, 0, -4700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12317")
    SetChrPos(0x109, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12317")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12367")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12356")
    SetChrPos(0x105, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12367")

    label("loc_12356")

    SetChrPos(0x105, -100670, 0, -7360, 90)

    label("loc_12367")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123B7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A6")
    SetChrPos(0x106, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_123B7")

    label("loc_123A6")

    SetChrPos(0x106, -100670, 0, -7360, 90)

    label("loc_123B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12407")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F6")
    SetChrPos(0x10A, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12407")

    label("loc_123F6")

    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_12407")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1241B")

    OP_0D()

    ChrTalk(
        0xB,
        (
            "#11P#11600FOh, right, younger brother...\x01",
            "Can you take this?\x02",
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
        "#6P#00000FWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11600FIt's the hair ornament I was wearing \x01",
            "when I was standing on the stage as \x01",
            "the main protagonist for the first time.\x02\x03",
            "#11604FI was always carrying it with me to\x01",
            "not forget my initial resolution.\x02\x03",
            "#11609FHu hu, don't you think it's\x01",
            "a rare article for enthusiasts?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12675")
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_12675")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(Indeed, seems that there would be guys\x01",
            "who would want this no matter the price...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FB-But...\x01",
            "Can I really have such\x01",
            "an important item?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#11604FHu hu, it's fine, it's fine.\x01",
            "It's a gift for all you've done until now.\x02\x03",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_127F7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_1280B")

    label("loc_127F7")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1280B")

    SetChrPos(0x0, -100140, 0, -6120, 90)
    SetScenarioFlags(0x1AD, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1283B")
    OP_E0(0x34, 0x0)

    label("loc_1283B")

    EventEnd(0x5)
    Return()

    # Function_86_1219C end

    def Function_87_1283E(): pass

    label("Function_87_1283E")

    EventBegin(0x1)
    Call(0, 92)
    SetChrPos(0x0, -13440, 0, 8760, 89)
    EventEnd(0x4)
    Return()

    # Function_87_1283E end

    def Function_88_12857(): pass

    label("Function_88_12857")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1286B")
    Call(0, 92)
    Jump("loc_1286E")

    label("loc_1286B")

    Call(0, 94)

    label("loc_1286E")

    SetChrPos(0x0, -9210, 0, 13390, 180)
    EventEnd(0x4)
    Return()

    # Function_88_12857 end

    def Function_89_12882(): pass

    label("Function_89_12882")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12896")
    Call(0, 94)
    Jump("loc_12899")

    label("loc_12896")

    Call(0, 93)

    label("loc_12899")

    SetChrPos(0x0, 1350, 0, 80, 89)
    EventEnd(0x4)
    Return()

    # Function_89_12882 end

    def Function_90_128AD(): pass

    label("Function_90_128AD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128C1")
    Call(0, 94)
    Jump("loc_128C4")

    label("loc_128C1")

    Call(0, 93)

    label("loc_128C4")

    SetChrPos(0x0, -5500, 0, 12500, 225)
    EventEnd(0x4)
    Return()

    # Function_90_128AD end

    def Function_91_128D8(): pass

    label("Function_91_128D8")

    EventBegin(0x1)
    Call(0, 93)
    SetChrPos(0x0, -19350, 0, 29820, 89)
    EventEnd(0x4)
    Return()

    # Function_91_128D8 end

    def Function_92_128F1(): pass

    label("Function_92_128F1")


    ChrTalk(
        0x101,
        (
            "#00000FFran's room is the 301, right?\x01",
            "Let's go see how she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_92_128F1 end

    def Function_93_1293C(): pass

    label("Function_93_1293C")


    ChrTalk(
        0x136,
        (
            "#01300FIlya's room is the 303 one.\x02\x03",
            "I think it will not take a lot of time, \x01",
            "so I wonder if we can go there now.\x02",
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

    # Function_93_1293C end

    def Function_94_129D6(): pass

    label("Function_94_129D6")


    ChrTalk(
        0x136,
        (
            "#01300FMr. Donovan's room is the 302 one.\x02\x03",
            "I think it will not take a lot of time, \x01",
            "so I wonder if we can go there now.\x02",
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

    # Function_94_129D6 end

    SaveToFile()

Try(main)
