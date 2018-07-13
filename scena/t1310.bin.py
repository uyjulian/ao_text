from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1310.bin",                # FileName
        "t1310",                    # MapName
        "t1310",                    # Location
        0x00BD,                     # MapIndex
        "ed7161",
        0x00002000,                 # Flags
        ("t1310", "t1310_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 189, 0, 12, 0, 13],
    )

    BuildStringList((
        "t1310",                  # 0
        "Cecil",                  # 1
        "Rixia",                  # 2
        "Elie",                   # 3
        "Tio",                    # 4
        "Fran",                   # 5
        "Zeit",                   # 6
        "KeA",                    # 7
        "Sully",                  # 8
        "Ilya",                   # 9
        "Randy",                  # 10
        "Noｱl",                  # 11
        "Wazy",                   # 12
        "ボール",                 # 13
        "メルカバ",               # 14
        "メルカバ",               # 15
        "Jaeger",                 # 16
        "Jaeger",                 # 17
        "Jaeger",                 # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Jaeger",                 # 21
        "Military Dog",           # 22
        "Military Dog",           # 23
        "Military Dog",           # 24
        "Military Dog",           # 25
        "Elizabeth",              # 26
        "Tapper",                 # 27
        "Watchman Wave",          # 28
        "Peng",                   # 29
        "Peng",                   # 30
        "Peng",                   # 31
        "Peng",                   # 32
        "Peng",                   # 33
        "Peng",                   # 34
        "SE制御",                 # 35
        "bt1310",                 # 36
        "bt1310",                 # 37
        "bt1310",                 # 38
        "bt1320",                 # 39
        "To Hotel Delphinia",     # 40
    ))

    ATBonus("ATBonus_7C4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_884", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_888", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_88C", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_890", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_894", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_898", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_89C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_864", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_868", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_86C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_870", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_874", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_878", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_87C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_880", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8EC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F8", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8FC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_900", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 0, 0, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_904", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42001.dat", "ms41902.dat", "ms41902.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, 0, "MonsterBattlePostion_884", "MonsterBattlePostion_864", "ed7540", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D0", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42001.dat", "ms41902.dat", "ms41902.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, "MonsterBattlePostion_8E4", "MonsterBattlePostion_864", "ed7540", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A4", "MonsterBattlePostion_864", "ed7451", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_98C", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87000.dat", "ms87100.dat", "ms87200.dat", "ms87300.dat", "ms87400.dat", "ms87500.dat", 0, 0, "MonsterBattlePostion_8C4", "MonsterBattlePostion_864", "ed7452", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch15700.itc",                   # 00
        "chr/ch15600.itc",                   # 01
        "apl/ch51330.itc",                   # 02
        "chr/ch15900.itc",                   # 03
        "apl/ch51329.itc",                   # 04
        "chr/ch16100.itc",                   # 05
        "apl/ch51328.itc",                   # 06
        "apl/ch51316.itc",                   # 07
        "chr/ch15300.itc",                   # 08
        "chr/ch15500.itc",                   # 09
        "chr/ch15400.itc",                   # 0A
        "apl/ch51706.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch39100.itc",                   # 11
        "chr/ch24800.itc",                   # 12
        "chr/ch23602.itc",                   # 13
        "chr/ch02708.itc",                   # 14
        "apl/ch51338.itc",                   # 15
        "apl/ch51317.itc",                   # 16
        "apl/ch51332.itc",                   # 17
        "apl/ch51347.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "apl/ch51343.itc",                   # 1C
        "apl/ch51351.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   29,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(54880,   4294965296, 4294929596, 0,    385,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(4294958026, 4294965796, 8449,    90,   257,  0x0, 0,   18,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(31920,   4294962987, 42560,   90,   261,  0x0, 0,   19,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 33,  -12.380000114440918,   0.0,                   -2.5,                  126.5625,              [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1111111119389534,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.952000141143799,     -0.0,                  0.5,                   1.0])
    DeclEvent(0x0000, 0, 34,  8.600000381469727,     0.07000000029802322,   -5.0,                  156.25,                [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.440000295639038,    -0.007000000216066837, 1.0,                   1.0])
    DeclEvent(0x0000, 0, 35,  8.949999809265137,     46.0,                  -5.0,                  87.890625,             [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.13333332538604736,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.5799999237060547,   -6.133333206176758,    1.0,                   1.0])
    DeclEvent(0x0000, 0, 37,  26.0,                  -16.0,                 -6.0,                  2304.0,                [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.25,                 1.3333333730697632,    1.2000000476837158,    1.0])

    DeclActor(27000,   4294961286, 38000,   1200,    27000,   4294963286, 38000,   0x007C, 0,  56, 0x0000)
    DeclActor(4294958846, 4294965796, 8340,    2000,    4294958026, 0,       8450,    0x007E, 0,  14, 0x0000)
    DeclActor(14680,   4294961296, 9990,    1200,    14280,   4294962796, 9990,    0x007C, 0,  32, 0x0000)
    DeclActor(48500,   4294960186, 4294950356, 1200,    48500,   4294961186, 4294950356, 0x007C, 0,  47, 0x0000)
    DeclActor(54330,   4294960026, 4294964456, 1200,    54330,   4294961026, 4294964456, 0x007C, 0,  48, 0x0000)
    DeclActor(67070,   4294959816, 17930,   1000,    67070,   4294960816, 17930,   0x007C, 0,  49, 0x0000)
    DeclActor(39320,   4294960516, 26760,   1000,    39320,   4294961516, 26760,   0x007C, 0,  50, 0x0000)
    DeclActor(50260,   4294960086, 49470,   800,     50260,   4294961086, 49470,   0x007C, 0,  51, 0x0000)

    PlaceName(-50.0, 0.0, 0.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(3088, 0)                                       # 0

    ScpFunction((
        "Function_0_C10",          # 00, 0
        "Function_1_CC0",          # 01, 1
        "Function_2_D13",          # 02, 2
        "Function_3_D3E",          # 03, 3
        "Function_4_D69",          # 04, 4
        "Function_5_D94",          # 05, 5
        "Function_6_DBF",          # 06, 6
        "Function_7_DDF",          # 07, 7
        "Function_8_DFF",          # 08, 8
        "Function_9_E1F",          # 09, 9
        "Function_10_E3F",         # 0A, 10
        "Function_11_ED1",         # 0B, 11
        "Function_12_EEA",         # 0C, 12
        "Function_13_12D7",        # 0D, 13
        "Function_14_15E5",        # 0E, 14
        "Function_15_15E9",        # 0F, 15
        "Function_16_1723",        # 10, 16
        "Function_17_1C8A",        # 11, 17
        "Function_18_1FBA",        # 12, 18
        "Function_19_21E8",        # 13, 19
        "Function_20_244C",        # 14, 20
        "Function_21_2568",        # 15, 21
        "Function_22_26FB",        # 16, 22
        "Function_23_286B",        # 17, 23
        "Function_24_2DC8",        # 18, 24
        "Function_25_3278",        # 19, 25
        "Function_26_3526",        # 1A, 26
        "Function_27_3714",        # 1B, 27
        "Function_28_3774",        # 1C, 28
        "Function_29_3A4A",        # 1D, 29
        "Function_30_3FBC",        # 1E, 30
        "Function_31_40D5",        # 1F, 31
        "Function_32_450D",        # 20, 32
        "Function_33_46D3",        # 21, 33
        "Function_34_4780",        # 22, 34
        "Function_35_47FC",        # 23, 35
        "Function_36_4878",        # 24, 36
        "Function_37_48D9",        # 25, 37
        "Function_38_5F1E",        # 26, 38
        "Function_39_7383",        # 27, 39
        "Function_40_7A0B",        # 28, 40
        "Function_41_8715",        # 29, 41
        "Function_42_A216",        # 2A, 42
        "Function_43_A22E",        # 2B, 43
        "Function_44_AD13",        # 2C, 44
        "Function_45_CBAE",        # 2D, 45
        "Function_46_CC39",        # 2E, 46
        "Function_47_D56E",        # 2F, 47
        "Function_48_D61B",        # 30, 48
        "Function_49_D6BB",        # 31, 49
        "Function_50_D79F",        # 32, 50
        "Function_51_D84D",        # 33, 51
        "Function_52_D919",        # 34, 52
        "Function_53_DBE8",        # 35, 53
        "Function_54_EE6B",        # 36, 54
        "Function_55_EFE4",        # 37, 55
        "Function_56_F798",        # 38, 56
        "Function_57_FAD1",        # 39, 57
        "Function_58_1381E",       # 3A, 58
        "Function_59_138AD",       # 3B, 59
        "Function_60_138C5",       # 3C, 60
        "Function_61_138F0",       # 3D, 61
        "Function_62_1391B",       # 3E, 62
        "Function_63_13946",       # 3F, 63
        "Function_64_13971",       # 40, 64
        "Function_65_1399C",       # 41, 65
        "Function_66_139C7",       # 42, 66
        "Function_67_139F2",       # 43, 67
        "Function_68_13A1D",       # 44, 68
        "Function_69_13A48",       # 45, 69
        "Function_70_13A5F",       # 46, 70
        "Function_71_13A74",       # 47, 71
        "Function_72_13A89",       # 48, 72
        "Function_73_13A9E",       # 49, 73
        "Function_74_13B7E",       # 4A, 74
        "Function_75_13C61",       # 4B, 75
        "Function_76_13D41",       # 4C, 76
        "Function_77_13E24",       # 4D, 77
        "Function_78_13E88",       # 4E, 78
        "Function_79_13F18",       # 4F, 79
        "Function_80_13FA8",       # 50, 80
        "Function_81_14116",       # 51, 81
        "Function_82_14F82",       # 52, 82
        "Function_83_14FA1",       # 53, 83
        "Function_84_15001",       # 54, 84
        "Function_85_15038",       # 55, 85
        "Function_86_150B2",       # 56, 86
        "Function_87_150D7",       # 57, 87
        "Function_88_1513C",       # 58, 88
        "Function_89_15158",       # 59, 89
        "Function_90_15249",       # 5A, 90
        "Function_91_15368",       # 5B, 91
        "Function_92_1538F",       # 5C, 92
        "Function_93_153B6",       # 5D, 93
        "Function_94_153D5",       # 5E, 94
        "Function_95_153F4",       # 5F, 95
        "Function_96_1542C",       # 60, 96
        "Function_97_15464",       # 61, 97
        "Function_98_1549C",       # 62, 98
        "Function_99_154B6",       # 63, 99
        "Function_100_15808",      # 64, 100
        "Function_101_158A2",      # 65, 101
        "Function_102_15EB4",      # 66, 102
        "Function_103_16004",      # 67, 103
        "Function_104_160BB",      # 68, 104
        "Function_105_160CB",      # 69, 105
        "Function_106_160DB",      # 6A, 106
        "Function_107_16353",      # 6B, 107
        "Function_108_163ED",      # 6C, 108
        "Function_109_165D1",      # 6D, 109
        "Function_110_166D4",      # 6E, 110
        "Function_111_17F5F",      # 6F, 111
        "Function_112_17F8D",      # 70, 112
        "Function_113_1807C",      # 71, 113
        "Function_114_18A1E",      # 72, 114
        "Function_115_18A31",      # 73, 115
        "Function_116_18A44",      # 74, 116
        "Function_117_18A57",      # 75, 117
        "Function_118_18A6A",      # 76, 118
        "Function_119_18A7D",      # 77, 119
        "Function_120_18ABD",      # 78, 120
        "Function_121_18AFD",      # 79, 121
        "Function_122_18B3D",      # 7A, 122
        "Function_123_18B7D",      # 7B, 123
        "Function_124_18BBD",      # 7C, 124
        "Function_125_18BE7",      # 7D, 125
        "Function_126_18C00",      # 7E, 126
    ))


    def Function_0_C10(): pass

    label("Function_0_C10")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_C48"),
        (1, "loc_C54"),
        (2, "loc_C60"),
        (3, "loc_C6C"),
        (4, "loc_C78"),
        (5, "loc_C84"),
        (6, "loc_C90"),
        (SWITCH_DEFAULT, "loc_C9C"),
    )


    label("loc_C48")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C54")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C60")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C6C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C78")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C84")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C90")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_CA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_CBF")

    Return()

    # Function_0_C10 end

    def Function_1_CC0(): pass

    label("Function_1_CC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D12")
    OP_95(0xFE, 45340, -7050, -19380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 42650, -7010, 17060, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_1_CC0")

    label("loc_D12")

    Return()

    # Function_1_CC0 end

    def Function_2_D13(): pass

    label("Function_2_D13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3D")
    OP_94(0xFE, 0x514, 0x13D8, 0xFFFFF650, 0x4254, 0x3E8)
    Sleep(300)
    Jump("Function_2_D13")

    label("loc_D3D")

    Return()

    # Function_2_D13 end

    def Function_3_D3E(): pass

    label("Function_3_D3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D68")
    OP_94(0xFE, 0x64C8, 0x995C, 0xAB9A, 0x49AC, 0x7D0)
    Sleep(300)
    Jump("Function_3_D3E")

    label("loc_D68")

    Return()

    # Function_3_D3E end

    def Function_4_D69(): pass

    label("Function_4_D69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D93")
    OP_94(0xFE, 0xD16A, 0xFFFFE908, 0xEA60, 0x1EC8, 0x7D0)
    Sleep(300)
    Jump("Function_4_D69")

    label("loc_D93")

    Return()

    # Function_4_D69 end

    def Function_5_D94(): pass

    label("Function_5_D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBE")
    OP_94(0xFE, 0xDEA8, 0xFFFFA600, 0xF618, 0xFFFFC158, 0x7D0)
    Sleep(300)
    Jump("Function_5_D94")

    label("loc_DBE")

    Return()

    # Function_5_D94 end

    def Function_6_DBF(): pass

    label("Function_6_DBF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DDE")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_6_DBF")

    label("loc_DDE")

    Return()

    # Function_6_DBF end

    def Function_7_DDF(): pass

    label("Function_7_DDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFE")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_7_DDF")

    label("loc_DFE")

    Return()

    # Function_7_DDF end

    def Function_8_DFF(): pass

    label("Function_8_DFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1E")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_8_DFF")

    label("loc_E1E")

    Return()

    # Function_8_DFF end

    def Function_9_E1F(): pass

    label("Function_9_E1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E3E")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_9_E1F")

    label("loc_E3E")

    Return()

    # Function_9_E1F end

    def Function_10_E3F(): pass

    label("Function_10_E3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ED0")
    SetChrFlags(0x14, 0x8000)
    OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB30C, 0x7D0, 0x3E8)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x11, 0x1)
    OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB9B0, 0xBB8, 0x3E8)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x1)
    OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFD058, 0x7D0, 0x3E8)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x10, 0x1)
    OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFCD38, 0xBB8, 0x3E8)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x13, 0x1)
    Jump("Function_10_E3F")

    label("loc_ED0")

    Return()

    # Function_10_E3F end

    def Function_11_ED1(): pass

    label("Function_11_ED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE9")
    SetChrFlags(0xFE, 0x8000)
    Sleep(1)
    Jump("Function_11_ED1")

    label("loc_EE9")

    Return()

    # Function_11_ED1 end

    def Function_12_EEA(): pass

    label("Function_12_EEA")

    SetChrChipByIndex(0x23, 0x13)
    SetChrSubChip(0x23, 0x0)
    EndChrThread(0x23, 0x0)
    SetChrBattleFlags(0x23, 0x4)
    BeginChrThread(0x23, 0, 0, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F1D")
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    EndChrThread(0x23, 0x0)
    Jump("loc_1247")

    label("loc_F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F2B")
    Jump("loc_1247")

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1247")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)
    Jump("loc_10D7")

    label("loc_1078")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_10D7")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_113E")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_1176")

    label("loc_113E")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_1176")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_11C7")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_1231")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_1203")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_1231")

    label("loc_1203")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_1231")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_125B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 80)
    Jump("loc_1292")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_126F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 81)
    Jump("loc_1292")

    label("loc_126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1283")
    ClearScenarioFlags(0x22, 2)
    Event(0, 108)
    Jump("loc_1292")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1292")
    ClearScenarioFlags(0x22, 3)
    Event(0, 109)

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    Event(0, 57)

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_12D6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D6")
    SetChrPos(0x0, 27000, -6010, 38000, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_12D6")

    Return()

    # Function_12_EEA end

    def Function_13_12D7(): pass

    label("Function_13_12D7")

    Sound(136, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_12F7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 0)
    Jump("loc_1309")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1309")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131C")
    OP_1B(0x0, 0x0, 0x65)

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1329")
    OP_65(0x1, 0x1)

    label("loc_1329")

    MiniGame(0x2F, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")
    SetMapObjFlags(0x0, 0x4)
    OP_65(0x0, 0x1)

    label("loc_135F")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138F")
    OP_66(0x3, 0x1)

    label("loc_138F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139D")
    OP_66(0x4, 0x1)

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AB")
    OP_66(0x5, 0x1)

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B9")
    OP_66(0x6, 0x1)

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    OP_66(0x7, 0x1)

    label("loc_13C7")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13EE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1406")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1406")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1423")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1434")
    Call(0, 100)

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1445")
    Call(0, 107)

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_148A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_14CA")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_14CA")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_14CA")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E8")
    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_14F5")
    OP_70(0xA, 0x2)

    label("loc_14F5")

    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E4")
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)

    label("loc_15E4")

    Return()

    # Function_13_12D7 end

    def Function_14_15E5(): pass

    label("Function_14_15E5")

    Call(0, 15)
    Return()

    # Function_14_15E5 end

    def Function_15_15E9(): pass

    label("Function_15_15E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 3)), scpexpr(EXPR_END)), "loc_15F6")
    Call(0, 55)
    Return()

    label("loc_15F6")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1607")
    Jump("loc_171F")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_171F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B4")

    ChrTalk(
        0x22,
        (
            "You're the guests to whom\x01",
            "the beach is reserved today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Tch, how enviable.\x01",
            "I'd love to play water games together\x01",
            "with such beauties too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_171F")

    label("loc_16B4")


    ChrTalk(
        0x22,
        (
            "Ah, I'm preparing the\x01",
            "stand merchandise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Sorry but, could you come\x01",
            "back again in a little while?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171F")

    TalkEnd(0x22)
    Return()

    # Function_15_15E9 end

    def Function_16_1723(): pass

    label("Function_16_1723")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187D")

    ChrTalk(
        0xFE,
        (
            "A "White Stone" is a totally white\x01",
            "pretty stone you can happen\x01",
            "to find sometimes in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a stone that sometimes is\x01",
            "buried in a "White Heaven" sandy beach,\x01",
            "so maybe it was transported in together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for one too,\x01",
            "don't search only the water\x01",
            "area, but the sandy beach too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1941")

    label("loc_187D")


    ChrTalk(
        0xFE,
        (
            "White Stones are said to originally\x01",
            "be stones sometimes buried in a\x01",
            ""White Heaven" sandy beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for one too,\x01",
            "don't search only the water\x01",
            "area, but the sandy beach too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1941")

    Jump("loc_1C86")

    label("loc_1946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A37")

    ChrTalk(
        0xFE,
        (
            "Still, to think that such a monster was\x01",
            "the rumored habitual swimsuits tearer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was for sure just\x01",
            "a maniac or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad things were settled \x01",
            "for the time being. Thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AD0")

    label("loc_1A37")


    ChrTalk(
        0xFE,
        (
            "Still, to think that such a monster was\x01",
            "the rumored habitual swimsuits tearer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad things were settled \x01",
            "for the time being. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD0")

    Jump("loc_1C86")

    label("loc_1AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE1")

    ChrTalk(
        0xFE,
        (
            "I keep a watchful eye so\x01",
            "that nothing dangerous\x01",
            "happens at this beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Near here is still shallow,\x01",
            "but if you go too far, a child's \x01",
            "legs won't touch anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be very careful to not go\x01",
            "too far when playing water games.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C86")

    label("loc_1BE1")


    ChrTalk(
        0xFE,
        (
            "Near here is still shallow,\x01",
            "but if you go too far, a child's \x01",
            "legs won't touch anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be very careful to not go\x01",
            "too far when playing water games.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C86")

    TalkEnd(0xFE)
    Return()

    # Function_16_1723 end

    def Function_17_1C8A(): pass

    label("Function_17_1C8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")
    TalkEnd(0xFE)
    Call(0, 52)
    Return()

    label("loc_1CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")

    ChrTalk(
        0xA,
        (
            "#12613FHonestly!\x01",
            "Going through something\x01",
            "like this all of a sudden...\x02\x03",
            "#12611FShouldn't you\x01",
            "have a little\x01",
            "more tact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506FI-I have no words...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D85")

    label("loc_1D5E")


    ChrTalk(
        0xA,
        (
            "#12613F*sigh*, honestly,\x01",
            "Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D85")

    Jump("loc_1FB6")

    label("loc_1D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA0")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F07")

    ChrTalk(
        0xA,
        (
            "#12600FI'm glad you applied\x01",
            "the sunscreen for me, but...\x02\x03",
            "#12613FA-As I thought, having\x01",
            "it applied by a colleague\x01",
            "was a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FHa...ha ha.\x01",
            "Frankly, I was embarrassed too.\x02\x03",
            "#12503F(Even so..."glom".)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612F...Hmm, Lloyd?\x01",
            "I'd like you didn't\x01",
            "stare for so long.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12511FS-Sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FB6")

    label("loc_1F07")


    ChrTalk(
        0xA,
        (
            "#12613FIt was a little embarrassing having\x01",
            "it applied by you who're a colleague.\x02\x03",
            "#12611FAlthough, I think it was better than having\x01",
            "it applied by Randy or someone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB6")

    TalkEnd(0xFE)
    Return()

    # Function_17_1C8A end

    def Function_18_1FBA(): pass

    label("Function_18_1FBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(
        0x8,
        (
            "#13305FOh, Lloyd. Are you looking for\x01",
            "something with KeA and the others?\x02\x03",
            "#13303FWhite Stones...?\x01",
            "Uhhm, I haven't seen any nearby.\x01",
            "I'm sorry for having not been of help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E4")

    label("loc_207F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2095")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_2095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2175")

    ChrTalk(
        0x8,
        (
            "#13304FUh uh, it was pleasant.\x01",
            "Thank you, Lloyd.\x02\x03",
            "#13309F...Oh, that's right.\x01",
            "Should I now apply the lotion \x01",
            "to you in return, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FI-I'm fine like this!\x01",
            "You sleep soundly, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21E4")

    label("loc_2175")


    ChrTalk(
        0x8,
        (
            "#13304FIt feels so good I think\x01",
            "I'll sleep like this.\x02\x03",
            "#13309FUh uh, wake me up if something happens, hm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E4")

    TalkEnd(0xFE)
    Return()

    # Function_18_1FBA end

    def Function_19_21E8(): pass

    label("Function_19_21E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228F")

    ChrTalk(
        0x9,
        (
            "#13505FWhite, round, pretty stones...?\x01",
            "No, I didn't see any.\x02\x03",
            "#13503FThe beach itself is white and pretty,\x01",
            "It will be hard to look for one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2448")

    label("loc_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A5")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_22A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A5")

    ChrTalk(
        0x9,
        "#13508F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12505F...Rixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13505FAh, no, I'm sorry.\x01",
            "I was thinking about something.\x02\x03",
            "#13504FEhm, Mr. Lloyd.\x01",
            "Thank you very much.\x02\x03",
            "#13502FUh uh, it seems that I\x01",
            "won't have to worry about\x01",
            "sunburns for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2448")

    label("loc_23A5")


    ChrTalk(
        0x9,
        (
            "#13504FIt seems that I won't\x01",
            "have to worry about\x01",
            "sunburns for a while.\x02\x03",
            "#13502FIt seems that Miss Ilya and\x01",
            "Sully are having fun too...\x01",
            "Uh uh, thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2448")

    TalkEnd(0xFE)
    Return()

    # Function_19_21E8 end

    def Function_20_244C(): pass

    label("Function_20_244C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C0")

    ChrTalk(
        0x11,
        (
            "#12805FHm? You're lookin' for white pebbles?\x02\x03",
            "#12803FSorry, but I didn't see one nearby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CF")
    Jump("loc_2564")

    label("loc_24CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E1")
    Call(0, 21)
    Jump("loc_2564")

    label("loc_24E1")


    ChrTalk(
        0x11,
        (
            "#12800FI wanted to do surfing\x01",
            "but they say they don't\x01",
            "rent boards.\x02\x03",
            "#12806FIt was my chance to show\x01",
            "the girls my good points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2564")

    TalkEnd(0xFE)
    Return()

    # Function_20_244C end

    def Function_21_2568(): pass

    label("Function_21_2568")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "#13002FAfter I've rested for a while,\x01",
            "I'd like to do something else.\x02\x03",
            "#13004FUhhm, were there any other\x01",
            "games to do at the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FLet's see, I think we did\x01",
            "the sort of beach staple...\x02\x03",
            "#12806FActually, I would've liked to dress up\x01",
            "and pick up girls, but with the beach\x01",
            "reserved, I can't meet any babes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006FYou're really incorrigible, senior...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_2568 end

    def Function_22_26FB(): pass

    label("Function_22_26FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27A8")

    ChrTalk(
        0x12,
        (
            "#13000FIf you're searching for something,\x01",
            "it could be good to change\x01",
            "your point of view.\x02\x03",
            "#13003FIt could be in an unexpected,\x01",
            "unthinkable place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2867")

    label("loc_27A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B7")
    Jump("loc_2867")

    label("loc_27B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C9")
    Call(0, 21)
    Jump("loc_2867")

    label("loc_27C9")


    ChrTalk(
        0x12,
        (
            "#13003FUhhm, were there any other\x01",
            "games to do at the beach?\x02\x03",
            "#13000FIt would be nice if there were more, like,\x01",
            "to enjoy with a great number of people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2867")

    TalkEnd(0xFE)
    Return()

    # Function_22_26FB end

    def Function_23_286B(): pass

    label("Function_23_286B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")

    ChrTalk(
        0x13,
        (
            "#12900FWhite Stones...?\x01",
            "I'm sure I've heard they're stones made of\x01",
            "the same materials as White Heaven's beach.\x02\x03",
            "#12904FAlmost all White Stones turn to sand after\x01",
            "many years, but it is said that sometimes,\x01",
            "they remain as pretty as they're.\x02\x03",
            "#12902FHu hu, if you find a big one,\x01",
            "you can consider yourself pretty lucky.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2AA2")

    label("loc_29D0")


    ChrTalk(
        0x13,
        (
            "#12904FAlmost all White Stones turn to sand after\x01",
            "many years, but it is said that sometimes,\x01",
            "they remain as pretty as they're.\x02\x03",
            "#12902FHu hu, if you find a big one,\x01",
            "you can consider yourself pretty lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA2")

    Jump("loc_2DC4")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB6")
    Jump("loc_2DC4")

    label("loc_2AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D06")

    ChrTalk(
        0x13,
        (
            "#12906FOh boy, I'm completely tired due\x01",
            "to it being a game I'm not used to.\x02\x03",
            "#12900FEssentially, games which involve\x01",
            "body movement are not my forte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12503FConsidering what you said,\x01",
            "you aren't even out of breath...\x02\x03",
            "#12502FWait, I feel like you were pretty\x01",
            "knowledgeable about the rules too,\x01",
            "couldn't it actually be your forte?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FHu hu, as if.\x01",
            "I'm a genuine city boy, you know?\x02\x03",
            "#12900FAs for the beach volleyball rules,\x01",
            "I just remembered them from having\x01",
            "read them in a magazine to pass the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12503F(I think that's amazing in its own way...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2DC4")

    label("loc_2D06")


    ChrTalk(
        0x13,
        (
            "#12906FOh boy, I'm completely tired due\x01",
            "to it being a game I'm not used to.\x02\x03",
            "#12909FHu hu, I believe I'll gracefully spend my time on\x01",
            "a deck chair associating with Elie and the others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC4")

    TalkEnd(0xFE)
    Return()

    # Function_23_286B end

    def Function_24_2DC8(): pass

    label("Function_24_2DC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED3")

    ChrTalk(
        0x10,
        (
            "#13400FIt seems that KeA is\x01",
            "playing with our Sully, eh?\x02\x03",
            "#13404FUh uh, that kid, because\x01",
            "she doesn't have friends her age,\x01",
            "she isn't used to be yearned for.\x02\x03",
            "#13402FToday, maybe I'll see a new side of her.\x01",
            "Uh uh, I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2F73")

    label("loc_2ED3")


    ChrTalk(
        0x10,
        (
            "#13404FBecause Sully doesn't have friends her age,\x01",
            "she isn't used to be yearned for.\x02\x03",
            "#13402FToday, maybe I'll see a new side of her.\x01",
            "Uh uh, I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F73")

    Jump("loc_3274")

    label("loc_2F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F87")
    Jump("loc_3274")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319E")

    ChrTalk(
        0x10,
        (
            "#13409FMaaan, devoting myself to such sports\x01",
            "from time to time is nice too.\x02\x03",
            "#13402FI can also enjoy cute\x01",
            "girls in swimsuits...\x01",
            "I'm really glad I came.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12512FMiss Ilya, you're\x01",
            "actually an old man\x01",
            "disguised as an artist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406FMy, how rude.\x02\x03",
            "#13402FEh eh, you too weren't able to take your\x01",
            "eyes off from Cecil, Rixia and the others \x01",
            "in a swimsuit, eh, younger brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511FN-No comment.\x02\x03",
            "#12506F(Rather, I think Miss Ilya's swimsuit\x01",
            "is the most amazing of all...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3274")

    label("loc_319E")


    ChrTalk(
        0x10,
        (
            "#13404FNow that I think about it, maybe it's\x01",
            "been really a long time since I've moved\x01",
            "around my body like this aside from practice.\x02\x03",
            "#13402FYes, yes, accepting the invitation\x01",
            "was really the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3274")

    TalkEnd(0xFE)
    Return()

    # Function_24_2DC8 end

    def Function_25_3278(): pass

    label("Function_25_3278")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3338")

    ChrTalk(
        0xB,
        (
            "#12705FWhite Stones...\x01",
            "Such things are on this beach?\x02\x03",
            "#12703FWe used the sand in this area\x01",
            "as the sand castle's foundation,\x01",
            "but we didn't found anything like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3522")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334E")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_334E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349D")

    ChrTalk(
        0xB,
        (
            "#12703FI was dubious that with sand\x01",
            "such a thing could be built, but...\x02\x03",
            "#12702FRather, now I do even feel that\x01",
            "I could build anything with sand.\x02\x03",
            "#12704FUh uh, it culd be nice\x01",
            "to built a house for\x01",
            "Zeit next.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F(I'm sure that Zeit\x01",
            "really hates sand...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01203FGrrowl...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3522")

    label("loc_349D")


    ChrTalk(
        0xB,
        (
            "#12704FNow I do even feel that\x01",
            "I could build anything with sand.\x02\x03",
            "#12702FUh uh, it culd be nice\x01",
            "to built a house for\x01",
            "Zeit next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3522")

    TalkEnd(0xFE)
    Return()

    # Function_25_3278 end

    def Function_26_3526(): pass

    label("Function_26_3526")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3599")

    ChrTalk(
        0xC,
        (
            "#13105FOh, you're searching for something?\x02\x03",
            "#13103FWhite Stones...?\x01",
            "Uhhm, I'm not sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3710")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AF")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_35AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A5")

    ChrTalk(
        0xC,
        (
            "#13109FWooow, it really turned out\x01",
            "into a magnificent castle!\x02\x03",
            "#13106FIf we had brought a camera\x01",
            "we could've taken a picture, but...\x01",
            "Boo, what a pity.\x02\x03",
            "#13101FI must at least firmly print it in\x01",
            "the photo Quartz of my mind!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3710")

    label("loc_36A5")


    ChrTalk(
        0xC,
        (
            "#13101FThe shape of this castle...I will go back home\x01",
            "with it printed in the photo Quartz of my mind!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3710")

    TalkEnd(0xFE)
    Return()

    # Function_26_3526 end

    def Function_27_3714(): pass

    label("Function_27_3714")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373F")

    ChrTalk(
        0xD,
        "#01200F...Woof?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3770")

    label("loc_373F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3755")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_3755")


    ChrTalk(
        0xD,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3770")

    TalkEnd(0xFE)
    Return()

    # Function_27_3714 end

    def Function_28_3774(): pass

    label("Function_28_3774")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3802")

    ChrTalk(
        0xE,
        (
            "#13210FAh, Lloyd...\x01",
            "Have you already found\x01",
            "a "White Stone"?\x02\x03",
            "#13209FEheheh, I wonder if there're\x01",
            "any big anywhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A46")

    label("loc_3802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3818")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_END)), "loc_39E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3955")

    ChrTalk(
        0xE,
        (
            "#13210FThis White Stone\x01",
            "is really big!\x02\x03",
            "#13209FMaybe this is the best memory\x01",
            "I've made at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12509FHa ha, we've just arrived,\x01",
            "so isn't it early for that?\x02\x03",
            "#12504FHowever, if you're that glad,\x01",
            "it makes me happy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209FEheheh, thank you, Lloyd.\x01",
            "I'll treasure it!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_39DB")

    label("loc_3955")


    ChrTalk(
        0xE,
        (
            "#13202FEheheh, maybe this is the best\x01",
            "memory I've made at Michelam.\x02\x03",
            "#13209FThank you, Lloyd.\x01",
            "I'll treasure this\x01",
            ""White Stone"!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39DB")

    Jump("loc_3A46")

    label("loc_39E0")


    ChrTalk(
        0xE,
        (
            "#13209FIt was fun looking for\x01",
            "a White Stone, eh?\x02\x03",
            "#13204FEheheh, I'll show\x01",
            "it to Zeit too later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A46")

    TalkEnd(0xFE)
    Return()

    # Function_28_3774 end

    def Function_29_3A4A(): pass

    label("Function_29_3A4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A86")
    Call(0, 30)
    Jump("loc_3D20")

    label("loc_3A86")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Show the White Stone\x01",      # 1
            "Quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF6")
    Call(0, 30)
    Jump("loc_3D20")

    label("loc_3AF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D11")

    ChrTalk(
        0xF,
        (
            "#13605FMrr...\x01",
            "It looks like you found\x01",
            "a "White Stone", huh.\x02\x03",
            "#13600FDo you want to compare\x01",
            "the "White Stone" size\x01",
            "with ours?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Challenge Them\x01",      # 0
            "I Better Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C9F")

    ChrTalk(
        0x101,
        "#12504FYeah, let's do this now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13605FEeh, full of confidence, ain't you?\x02\x03",
            "#13604FThen, I'll go call shorty.\x01",
            "Eh eh, you'll regret it, you know?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    Call(0, 53)
    Return()

    label("loc_3C9F")


    ChrTalk(
        0x101,
        "#12500FNo, wait a little longer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606FTch, what the heck.\x01",
            "You're a man, show some determination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D20")

    label("loc_3D11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D20")

    label("loc_3D20")

    Jump("loc_3FB8")

    label("loc_3D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3B")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 2)), scpexpr(EXPR_END)), "loc_3F13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC8")

    ChrTalk(
        0xF,
        (
            "#13600FH-Hey, uhmm...\x01",
            "Thanks for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FFor the White Stone?\x01",
            "You don't have to worry about it.\x02\x03",
            "#12509FHa ha, you can show that to\x01",
            "everyone at the Arc-en-ciel next time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#13611FI-Idiot...\x01",
            "As if I'd ever act in\x01",
            "such a childish way!\x02\x03",
            "#13606FUse some common sense, jeez...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F(It's tough to be an adolescent girl...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3F0E")

    label("loc_3EC8")


    ChrTalk(
        0xF,
        (
            "#13603FThanks for the\x01",
            "White Stone.\x02\x03",
            "#13608F...H-Hmph, just that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0E")

    Jump("loc_3FB8")

    label("loc_3F13")


    ChrTalk(
        0xF,
        (
            "#13603FIt's nice searching for pebbles, but...\x01",
            "I've come to the beach so\x01",
            "I'd want to swim properly.\x02\x03",
            "#13602FIt would be nice if I'd\x01",
            "become better than Rixia...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB8")

    TalkEnd(0xFE)
    Return()

    # Function_29_3A4A end

    def Function_30_3FBC(): pass

    label("Function_30_3FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406A")

    ChrTalk(
        0xF,
        (
            "#13600FTell me if you find\x01",
            "a "White Stone".\x02\x03",
            "Then we'll compare the size and\x01",
            "who's got the biggest one wins.\x02\x03",
            "#13604FWell, as If I'd ever\x01",
            "lose to you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_40D4")

    label("loc_406A")


    ChrTalk(
        0xF,
        (
            "#13600FWe'll see whose "White Stone"\x01",
            "is the biggest later.\x02\x03",
            "#13604FWell, as If I'd ever\x01",
            "lose to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D4")

    Return()

    # Function_30_3FBC end

    def Function_31_40D5(): pass

    label("Function_31_40D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_40E6")
    Jump("loc_4509")

    label("loc_40E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4163")

    ChrTalk(
        0x101,
        (
            "#12500FOh, this black cat...\x01",
            "I think I saw it somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nyaa～...[I'm hungry]\x02",
    )

    CloseMessageWindow()
    Jump("loc_417E")

    label("loc_4163")


    ChrTalk(
        0xFE,
        "Nyaa～...[I'm hungry]\x02",
    )

    CloseMessageWindow()

    label("loc_417E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_43B7")

    ChrTalk(
        0x101,
        (
            "#12505F...Could it\x01",
            "be hungry?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Give her "Catfood"\x01",      # 0
            "Quit\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A3")

    ChrTalk(
        0x101,
        "#12500FYou can eat it if you like.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " was given to her.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xFE,
        "Nyanyayayaa～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*avidly eating*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509FHa ha, were you that hungry?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Nyaon㈱[That's right.]\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F3, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FEh...are you giving me this book?\x02\x03",
            "#12500FHa ha, thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 5)
    SubItemNumber(0x1D9, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43B2")

    label("loc_43A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B2")

    label("loc_43B2")

    Jump("loc_44EA")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445B")

    ChrTalk(
        0x101,
        (
            "#12505F...Could it be\x01",
            "hungry?\x02\x03",
            "#12503FI could  give it "Catfood"\x01",
            "if I had it with me, but...\x02\x03",
            "#12512FUnfortunately, I don't have it now.\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44D1")

    label("loc_445B")


    ChrTalk(
        0x101,
        (
            "#12503FI could  give it "Catfood"\x01",
            "if I had it with me, but...\x02\x03",
            "#12512FUnfortunately, I don't have it now.\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D1")


    ChrTalk(
        0xFE,
        "Nyaon...[I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_44EA")

    SetScenarioFlags(0x1, 6)
    Jump("loc_4509")

    label("loc_44F2")


    ChrTalk(
        0xFE,
        "Nyaon㈱[Goodbye.]\x02",
    )

    CloseMessageWindow()

    label("loc_4509")

    TalkEnd(0xFE)
    Return()

    # Function_31_40D5 end

    def Function_32_450D(): pass

    label("Function_32_450D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Advises on how to Enjoy the Lake Beach\x01",
            "─────────────────────────────\x01",
            "・Please, absolutely warm up.\x01",
            "・Please, do not enter dressed into the water.\x01",
            "  (We loan swimsuits at the reception)\x01",
            "・Please, observe the watchman's indications.\x01",
            "─────────────────────────────\x01",
            " Let's mind our manners and have fun.\x01",
            "  　──Michelam Management Division\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_450D end

    def Function_33_46D3(): pass

    label("Function_33_46D3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FOops... This way takes\x01",
            "to the building inside.\x02\x03",
            "Since Miss Mariabell went out\x01",
            "of her way to reserve it for us,\x01",
            "let's enjoy the beach now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10330, -2000, -920, 90)
    EventEnd(0x4)
    Return()

    # Function_33_46D3 end

    def Function_34_4780(): pass

    label("Function_34_4780")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FThe "White Stone" should be\x01",
            "somewhere on the seashore.\x01",
            "Let's search for a little longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11580, -5080, -120, 90)
    EventEnd(0x4)
    Return()

    # Function_34_4780 end

    def Function_35_47FC(): pass

    label("Function_35_47FC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FThe "White Stone" should be\x01",
            "somewhere on the seashore.\x01",
            "Let's search for a little longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11210, -4940, 46030, 90)
    EventEnd(0x4)
    Return()

    # Function_35_47FC end

    def Function_36_4878(): pass

    label("Function_36_4878")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FWhoops...let's look for it without\x01",
            "hindering the beachvolley.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 32500, -6000, -13500, 90)
    EventEnd(0x5)
    Return()

    # Function_36_4878 end

    def Function_37_48D9(): pass

    label("Function_37_48D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48EB")
    Call(0, 36)
    Return()

    label("loc_48EB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51311.itc", 0x1E)
    LoadChrToIndex("apl/ch51312.itc", 0x1F)
    LoadChrToIndex("apl/ch51313.itc", 0x20)
    LoadChrToIndex("apl/ch51314.itc", 0x21)
    LoadChrToIndex("apl/ch51315.itc", 0x22)
    LoadChrToIndex("apl/ch51331.itc", 0x23)
    LoadChrToIndex("apl/ch51333.itc", 0x25)
    LoadChrToIndex("apl/ch51334.itc", 0x26)
    LoadChrToIndex("apl/ch51335.itc", 0x27)
    LoadChrToIndex("apl/ch51336.itc", 0x28)
    LoadChrToIndex("apl/ch51337.itc", 0x29)
    LoadChrToIndex("apl/ch51339.itc", 0x2B)
    LoadChrToIndex("apl/ch51340.itc", 0x2C)
    LoadChrToIndex("apl/ch51341.itc", 0x2D)
    LoadChrToIndex("apl/ch51342.itc", 0x2E)
    LoadChrToIndex("apl/ch51344.itc", 0x30)
    LoadChrToIndex("apl/ch51345.itc", 0x31)
    LoadChrToIndex("apl/ch51346.itc", 0x32)
    LoadChrToIndex("apl/ch51348.itc", 0x34)
    LoadChrToIndex("apl/ch51349.itc", 0x35)
    LoadChrToIndex("apl/ch51350.itc", 0x36)
    LoadEffect(0x0, "event\\ev13001.eff")
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x12, 0x20)
    ClearChrFlags(0x10, 0x20)
    ClearChrFlags(0x13, 0x20)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x101, 31000, -6000, -14500, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA3")
    Call(1, 1)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)

    ChrTalk(
        0x10,
        "#13400F#11P──Alright♪\x02",
    )

    CloseMessageWindow()

    def lambda_4A48():
        TurnDirection(0x13, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4A48)
    Sleep(50)

    def lambda_4A58():
        TurnDirection(0x11, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4A58)
    Sleep(50)

    def lambda_4A68():
        TurnDirection(0x12, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4A68)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x11,
        "#12809F#5PGhh, I knew it...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006F#6PI couldn't see the ball...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x10, 500)

    ChrTalk(
        0x13,
        (
            "#12902F#12PHu hu, she used her entire body\x01",
            "as a spring to do a great spike.\x02\x03",
            "#12904FI believe I can only say that's to\x01",
            "be expected from Ilya Platiｲre.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x13, 500)

    ChrTalk(
        0x10,
        "#13409F#5PUh uh, you're welcome♪\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(28000, -4800, -15000, 0)
    MoveCamera(260, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12505F#6PA-Amazing...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C46():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4C46)
    Sleep(50)

    def lambda_4C56():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4C56)
    Sleep(50)

    def lambda_4C66():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4C66)
    Sleep(50)

    def lambda_4C76():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4C76)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x10,
        (
            "#13400F#11POh, younger brother, were you watching?\x02\x03",
            "#13409FUh uh, how was my killer move?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PW-Well...\x01",
            "It was really impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PMan, I was really amazed.\x02\x03",
            "#12804FYou even easily\x01",
            "received my spikes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWazy too, he assisted Miss Ilya by tossing\x01",
            "the ball to her like he had no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#11PHu hu, it was just a whim of mine.\x01",
            "Also, you two are quite the\x01",
            "combination too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PWell...frankly, everyone's\x01",
            "level is so high that I\x01",
            "don't have any words.\x02\x03",
            "#12500FIf you entered a competition with this lineup,\x01",
            "you could aim for the championship right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PUh uh, well, I don't think it\x01",
            "would really go so easy,\x01",
            "but we could reach a good spot.\x02\x03",
            "#13409FRight, why don't we enjoy\x01",
            "the next game together?♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15D, 2)
    Jump("loc_50D0")

    label("loc_4FA3")

    SetChrPos(0x10, 24500, -6000, -15000, 90)
    SetChrPos(0x11, 24500, -6000, -17000, 90)
    SetChrPos(0x12, 27500, -6000, -19000, 45)
    SetChrPos(0x13, 27500, -6000, -13000, 90)
    SetChrPos(0x14, 23500, -6000, -14000, 0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    OP_68(28000, -4800, -15000, 0)
    MoveCamera(260, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#13400F#11PYou're already here, so, wanna\x01",
            "join the next game, younger brother?\x02\x03",
            "#13409FLet's enjoy beach volley together♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50D0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Take Part in Beach Volley\x01",      # 0
            "Quit\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D97")

    ChrTalk(
        0x101,
        (
            "#12500F#6PThen, I'll accept your\x01",
            "offer and join you.\x02\x03",
            "#12506FAlthough, I don't know beach\x01",
            "volley rules very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000FThe basics are just like volleyball.\x02\x03",
            "#13004FIf I have to roughly say what's different \x01",
            "is that the teams are made by two persons\x01",
            "and it's played on a sandy beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FAlso, in practice the team that gets\x01",
            "21 points finally wins a set, but...\x02\x03",
            "This time, to enjoy it in an easy way,\x01",
            "let's make it an irregular match\x01",
            "with a team to get 12 points first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHm, I see...\x01",
            "There should be no problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PWell, let's leave the small stuff\x01",
            "aside and split into teams now.\x02\x03",
            "#12806FWith Lloyd joinin', we'll have to assign\x01",
            "the extra person to be the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#6PAh, that's right...\x01",
            "I guess that I somehow bothered you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PAhaha, not at all.\x02\x03",
            "#13400FThen younger brother, can you choose\x01",
            "the partner you want to team up with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6PAll right, then...\x02",
    )

    CloseMessageWindow()
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
            "#1KWith whom will you team up?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Randy\x01",       # 0
            "Noｱl\x01",       # 1
            "Wazy  \x01",      # 2
            "Ilya  \x01",      # 3
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
        (0, "loc_5573"),
        (1, "loc_5767"),
        (2, "loc_5961"),
        (3, "loc_5B6C"),
        (SWITCH_DEFAULT, "loc_5D78"),
    )


    label("loc_5573")


    ChrTalk(
        0x101,
        "#12500F#6PRandy, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12800F#5PAll right, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13004F#5PWe just need to decide the\x01",
            "other team and the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FWell, how about the impartial\x01",
            "rock-scissors-paper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PUh uh, got it.\x01",
            "Let's decide it at once.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the rock-scissors-paper result,\x01",
            "Ilya was assigned to be the referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The match of Lloyd and\x01",
            "Randy team versus the Wazy\x01",
            "and Noｱl team began.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 3)
    Call(1, 9)
    Jump("loc_5D78")

    label("loc_5767")


    ChrTalk(
        0x101,
        "#12500F#6PNoｱl, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PUnderstood! \x01",
            "Let's do our best, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FThen, shall we decide the\x01",
            "remaining team and referee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13400F#11PWell, how about the impartial\x01",
            "rock-scissors-paper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#5PRight, let's decide\x01",
            "it at once!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the rock-scissors-paper result,\x01",
            "Randy was assigned to be the referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The match of Lloyd and\x01",
            "Noｱl team versus the Ilya\x01",
            "and Wazy team began.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 4)
    Call(1, 24)
    Jump("loc_5D78")

    label("loc_5961")


    ChrTalk(
        0x101,
        "#12500F#6PWazy, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12900FHu hu, that's a simple request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PThen, let's decide the\x01",
            "remaining team and referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800F#5PWell, what do you say 'bout the\x01",
            "impartial rock-scissors-paper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#5PRight, let's decide it quickly\x01",
            "and begin the game!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the rock-scissors-paper result,\x01",
            "Noｱl was assigned to be the referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The match of Lloyd and\x01",
            "Wazy team versus the Ilya\x01",
            "and Randy team began.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 5)
    Call(1, 49)
    Jump("loc_5D78")

    label("loc_5B6C")


    ChrTalk(
        0x101,
        "#12500F#6PMiss Ilya, please, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#13400F#11POkay, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12804F#5PThen, shall we decide the\x01",
            "remaining team and referee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWell, we should be fine using the\x01",
            "impartial rock-scissors-paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902FHu hu, right.\x01",
            "Well, let's decide this fast.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the rock-scissors-paper result,\x01",
            "Wazy was assigned to be the referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The match of Lloyd and\x01",
            "Ilya team versus the Randy\x01",
            "and Noｱl team began.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 6)
    Call(1, 69)
    Jump("loc_5D78")

    label("loc_5D78")

    Call(0, 38)
    Call(0, 39)
    Call(0, 45)
    SetChrPos(0x0, 20000, -6000, -15000, 0)
    Jump("loc_5F03")

    label("loc_5D97")


    ChrTalk(
        0x101,
        "#12500F#6PEhm, now it wouldn't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13405F#11PMy, is that so?\x01",
            "Well, it can't be helped.\x02\x03",
            "#13400FThen, if you want to join just\x01",
            "tell me whenever you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF2")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)

    label("loc_5EF2")

    SetChrPos(0x0, 32500, -6000, -13500, 90)

    label("loc_5F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1B")
    Call(0, 54)

    label("loc_5F1B")

    EventEnd(0x5)
    Return()

    # Function_37_48D9 end

    def Function_38_5F1E(): pass

    label("Function_38_5F1E")

    OP_68(26000, -4700, -16000, 0)
    MoveCamera(330, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x14, 0x8)
    SetChrPos(0x14, 29100, -6000, -11900, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_62A6")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x11, 27000, -6000, -18000, 0)
    SetChrPos(0x12, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x10, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12809F#6PHa ha, that was\x01",
            "a quite good match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12902FHu hu, not bad indeed.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x10,
        (
            "#13401F#5PAww, no fair! Everyone's\x01",
            "having such a good time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60F1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60F1)
    Sleep(50)

    def lambda_6101():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6101)
    Sleep(50)

    def lambda_6111():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6111)
    Sleep(50)

    def lambda_6121():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6121)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x12,
        "#13005F#11PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#5PThere's no way just watching such\x01",
            "a fun game could ever be enough.\x02\x03",
            "#13409FLet's play another game\x01",
            "where I'm in the mix!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHa ha, then let's form\x01",
            "different teams this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#12PHa ha. Sure, why not.\x02\x03",
            "#12800FSo Lloyd, who do\x01",
            "you want to team\x01",
            "up with this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D14")

    label("loc_62A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_6605")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x12, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x12,
        "#13009F#6P*haah*...what a heated match!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#13409F#11PYes, yes, that was a nice workout.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x11, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#12806F#5PMrr...the moment Lloyd joined,\x01",
            "things somehow became heated up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6428():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6428)
    Sleep(50)

    def lambda_6438():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6438)
    Sleep(50)

    def lambda_6448():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6448)
    Sleep(50)

    def lambda_6458():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6458)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x13,
        "#12905F#12PHm, is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12803F#5PWell, as expected,\x01",
            "it's unfair havin' only\x01",
            "me just watchin', right?\x02\x03",
            "#12800FLet's have another match\x01",
            "with me in the mix too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PYeah, then let's form different\x01",
            "teams this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#12PYes, sound nice.\x02\x03",
            "#13000FThen, Mr. Lloyd, please\x01",
            "choose the partner with whom \x01",
            "you want to team up next!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D14")

    label("loc_6605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_694E")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x13, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x11, 27000, -6000, -14000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        "#12902F#6PHu hu, it was pretty fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12809F#11PYeah, quite the nice match.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x12,
        (
            "#13001F#5P...Uhm, everyone! If possible,\x01",
            "would you like to do another game?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_677B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_677B)
    Sleep(50)

    def lambda_678B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_678B)
    Sleep(50)

    def lambda_679B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_679B)
    Sleep(50)

    def lambda_67AB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_67AB)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x10,
        "#13405F#11POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006F#5PIt's just that, while I was watching the game\x01",
            "just now, I couldn't contain myself...\x02\x03",
            "#13002FPlease, let me join too in the next one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PYeah, then let's form different\x01",
            "teams this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904F#12PHu hu, I too don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902F#12PThen Lloyd, choose the\x01",
            "partner you want to\x01",
            "team up with next.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D14")

    label("loc_694E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_6D14")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x10, 27000, -6000, -18000, 0)
    SetChrPos(0x11, 25000, -6000, -14000, 180)
    SetChrPos(0x12, 27000, -6000, -14000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        "#13409F#6PWow, that was exciting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009F#11PYes, it was really fun!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#12900F#5PHu hu, then should\x01",
            "we close it here?\x02\x03",
            "#12904FI also got thirsty.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#12504F#12PWell...since we're here,\x01",
            "why don't we have another game?\x02\x03",
            "#12500FWith Wazy in, this time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B2E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6B2E)
    Sleep(50)

    def lambda_6B3E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6B3E)
    Sleep(50)

    def lambda_6B4E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6B4E)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)

    ChrTalk(
        0x11,
        (
            "#12800F#11PYeah, that sounds good.\x01",
            "You too are tired of being\x01",
            "the referee, right, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#12906F#5PWell, to me either\x01",
            "one is fine, but...\x02\x03",
            "#12900F...Hu hu, I have no choice then.\x01",
            "If you're up to it, I think\x01",
            "I can keep you company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12PUh uh, it's decided then.\x02\x03",
            "#13400FThen, younger brother,\x01",
            "choose the partner you\x01",
            "want to team up with next.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12500F#6PYes, alright.\x01",
            "Then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D14")

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
            "#1KWith whom will you team up?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "Ilya")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_6D84")
    MenuCmd(3, 0, 0x0)

    label("loc_6D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_6D91")
    MenuCmd(3, 0, 0x1)

    label("loc_6D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_6D9E")
    MenuCmd(3, 0, 0x2)

    label("loc_6D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_6DAB")
    MenuCmd(3, 0, 0x3)

    label("loc_6DAB")

    MenuCmd(2, 0, -1, 85, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DF0"),
        (1, "loc_6F4D"),
        (2, "loc_70B3"),
        (3, "loc_7214"),
        (SWITCH_DEFAULT, "loc_7382"),
    )


    label("loc_6DF0")

    TurnDirection(0x101, 0x11, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NThen, you're up, Randy.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x11, 0x101, 500)

    ChrTalk(
        0x11,
        "#12809F#5P#NAll right, leave it to me!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to another rock-scissors-\x01",
            "paper, Ilya was chosen as\x01",
            "the second game referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Lloyd and Randy team versus\x01",
            "the Wazy and Noｱl team match\x01",
            "was decided to take place next.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 9)
    Jump("loc_7382")

    label("loc_6F4D")

    TurnDirection(0x101, 0x12, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NNoｱl, you're up.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x12, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "#13009F#5P#NUnderstood! \x01",
            "Let's do our best, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to another rock-scissors-\x01",
            "paper, Randy was chosen as\x01",
            "the second game referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Lloyd and Noｱl team versus\x01",
            "the Ilya and Wazy team match\x01",
            "was decided to take place next.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 24)
    Jump("loc_7382")

    label("loc_70B3")

    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NThen, you're up, Wazy.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHu hu, that's a simple request.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to another rock-scissors-\x01",
            "paper, Noｱl was chosen as\x01",
            "the second game referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Lloyd and Wazy team versus\x01",
            "the Ilya and Randy team match\x01",
            "was decided to take place next.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 49)
    Jump("loc_7382")

    label("loc_7214")

    TurnDirection(0x101, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NThen, the next one will be Miss Ilya.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        "#13409F#5P#NOkay, leave it to me!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to another rock-scissors-\x01",
            "paper, Wazy was chosen as\x01",
            "the second game referee...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Lloyd and Ilya team versus\x01",
            "the Randy and Noｱl team match\x01",
            "was decided to take place next.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 69)
    Jump("loc_7382")

    label("loc_7382")

    Return()

    # Function_38_5F1E end

    def Function_39_7383(): pass

    label("Function_39_7383")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, 20000, -6000, -15000, 180)
    SetChrPos(0x11, 20600, -6000, -17000, 0)
    SetChrPos(0x10, 19400, -6000, -17000, 0)
    SetChrPos(0x13, 20600, -6000, -18000, 0)
    SetChrPos(0x12, 19400, -6000, -18000, 0)
    SetChrPos(0x14, 26000, -6000, -16000, 0)
    ClearChrFlags(0x14, 0x8)
    OP_68(20000, -5000, -16000, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#6P#13409F...Man, that was fun!\x02\x03",
            "#13400FBecause the younger brother joined,\x01",
            "we could enjoy different team formations too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FHa ha, two games in a row\x01",
            "were pretty intense, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12803FYeah, but...\x02\x03",
            "#12809FIt's too bad we didn't get\x01",
            "a fanservice scene.\x02\x03",
            "#12806FI was hoping\x01",
            "Noｱl would\x01",
            "do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#6P#13405FYeah, seriously!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P#12904FHu hu, that would've heated up\x01",
            "beach volley unintentionally, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#6P#13006FS-Senior, Wazy...\x01",
            "What're you saying, geez.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FI'm interested in Miss Ilya's\x01",
            "overreaction too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12500FOh, that's right.\x01",
            "Are you guys thirsty?\x02\x03",
            "I could buy you something fresh\x01",
            "at the stand, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FOh, how considerate, younger brother\x01",
            "Now, what do I want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12800FI think I heard there's\x01",
            "a new juice you can\x01",
            "buy at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6P#13000FYeah, I heard\x01",
            "about it too.\x02\x03",
            "#13004FIt's called "Bell-Cola",\x01",
            "and it's supposed to be\x01",
            "bubbly and refreshing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P#12902FHa ha, that seems\x01",
            "pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FThen, "Bell-Cola"\x01",
            "for everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FYes, please.\x02\x03",
            "#13404FWell, I'm not that\x01",
            "thirsty right now,\x01",
            "so no need to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FHa ha, got it. I'll\x01",
            "bring them by later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2B)
    OP_D7(0x2C)
    OP_D7(0x2D)
    OP_D7(0x2E)
    OP_D7(0x30)
    OP_D7(0x31)
    OP_D7(0x32)
    OP_D7(0x34)
    OP_D7(0x35)
    OP_D7(0x36)
    SetScenarioFlags(0x15E, 0)
    ModifyEventFlags(0, 3, 0x80)
    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x14, 25950, -6000, -13400, 0)
    BeginChrThread(0x11, 0, 0, 0)
    BeginChrThread(0x12, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    Return()

    # Function_39_7383 end

    def Function_40_7A0B(): pass

    label("Function_40_7A0B")

    EventBegin(0x0)
    Fade(500)
    OP_68(19000, -4700, 20700, 0)
    MoveCamera(319, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 20500, -6000, 20700, 270)
    SetChrSubChip(0x9, 0x2)
    SetChrSubChip(0xA, 0x1)
    SetMapObjFlags(0x1, 0x1000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8557")

    ChrTalk(
        0x8,
        "#5P#13302FOh, if it isn't Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13502FUh uh, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12504FSister Cecil, Rixia, Elie, you're sunbathing, huh.\x02\x03",
            "#12500FIt seems you haven't swum in the lake yet.\x01",
            "Are you at least having fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FYes. Even just relaxing\x01",
            "here is plenty fun.\x02\x03",
            "#13309FAnd I can chat with\x01",
            "Miss Elie and Miss Rixia, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602FAhaha. We're having\x01",
            "fun too... But we\x01",
            "have a small problem.\x02\x03",
            "#12606FMiss Cecil keeps asking me\x01",
            ""How are things with Lloyd?"\x01",
            "and nothing else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509FY-Yes...\x01",
            "I was a little shocked.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#12506FN-Now look here, sister Cecil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FUh uh, I am curious, you know?\x02\x03",
            "Sisters always have to check up on their\x01",
            "brothers' relationships, you know.\x02\x03",
            "#13301FAnd I want to know who is going\x01",
            "to be your future bride ASAP!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12506FN-No no,\x01",
            "stop that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13500F(Hmm, as expected, not for nothing\x01",
            "she's Miss Ilya's childhood friend...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#13302FLloyd, why don't\x01",
            "you sunbathe\x01",
            "with us a bit?\x02\x03",
            "#13309FWe have an extra deck chair,\x01",
            "and we can chat a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12512FU-Uh, well, it's\x01",
            "kind of embarrassing\x01",
            "butting in like this.\x02\x03",
            "#12500FI'll have to pass this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#13305FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12600F*giggle*, too late to be\x01",
            "getting all embarrassed now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13503FThat's right. I want\x01",
            "to chat with you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12502FHa ha. I'm happy to hear\x01",
            "you say that, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#5P#13303FHmm... In that case...\x02\x03",
            "#13309FIn exchange,\x01",
            "would you put\x01",
            "sunscreen on us?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#12505FHuh......\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0xC8, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#12511F#4SWHAAAAAAT!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12605FW-Wait, Miss Cecil!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13506FThat's really a bit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FUh uh, what is wrong with that?\x01",
            "I have no problem with it at all.\x02\x03",
            "#13304FAnd Miss Elie and Miss Rixia, didn't\x01",
            "you say earlier you wanted to avoid\x01",
            "sunburn as much as possible?\x02\x03",
            "#13309FYou were the one who said\x01",
            ""Too late to be getting all embarrassed", \x01",
            "didn't you, Miss Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12605FY-Yes, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12607FU-Understood!\x02\x03",
            "#12613FAlright... Lloyd,\x01",
            "please go ahead.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        "#12P#12505FE-Elie...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12611FI-I mean, everyone else is enjoying\x01",
            "themselves. I wouldn't want to interrupt.\x02\x03",
            "#12606FAnd it is true that I\x01",
            "don't want to burn...\x02\x03",
            "#12613FAnd I think it will be better than having\x01",
            "it applied by Randy or someone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#13503FT-That's true\x02\x03",
            "#13506FI put some on Miss Ilya\x01",
            "back at our hotel room.\x02\x03",
            "#13502FAnd, if it's Mr. Lloyd doing it,\x01",
            "I guess I'm not so opposed to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        "#12P#12511FR-Rixia too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FUh uh, you see, Lloyd? \x01",
            "Your sister and these lovely ladies\x01",
            "are specifically requesting you.\x02\x03",
            "#13302FSo you will do it, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    SetScenarioFlags(0x15D, 0)
    Jump("loc_858F")

    label("loc_8557")


    ChrTalk(
        0x8,
        (
            "#5P#13302FOh, Lloyd.\x01",
            "Will you put\x01",
            "sunscreen on us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_858F")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Put Sunscreen on the Girls\x01",      # 0
            "Quit\x01",                            # 1
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
        (0, "loc_85FF"),
        (1, "loc_8607"),
        (SWITCH_DEFAULT, "loc_8714"),
    )


    label("loc_85FF")

    Call(0, 41)
    Jump("loc_8714")

    label("loc_8607")


    ChrTalk(
        0x101,
        (
            "#12P#12511FW-Wait just a moment.\x01",
            "I have to mentally prepare...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FMy...uh uh, it can't be helped.\x01",
            "Then, please come later.\x02\x03",
            "#13304FHowever, try to do as fast as possible,\x01",
            "or else, we'll get sunburns at this rate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 21500, -6000, 20700, 90)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearMapObjFlags(0x1, 0x1000)
    EventEnd(0x5)
    Jump("loc_8714")

    label("loc_8714")

    Return()

    # Function_40_7A0B end

    def Function_41_8715(): pass

    label("Function_41_8715")

    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#12P#12501FF-Fine. I'll do\x01",
            "it respectfully!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12611F"Respectfully"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509FAhaha... There's a strange\x01",
            "tension in the air now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13300FUh uh, then, \x01",
            "please do it right now.\x02\x03",
            "#13303FWho will you put it on first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#12506FU-Uhhm...\x02",
    )

    CloseMessageWindow()
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
            "#1KWho will you put it on first?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Start with Elie\x01",       # 0
            "Start with Cecil\x01",      # 1
            "Start with Rixia\x01",      # 2
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
        (0, "loc_88D1"),
        (1, "loc_8E91"),
        (2, "loc_954A"),
        (SWITCH_DEFAULT, "loc_9C53"),
    )


    label("loc_88D1")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then...\x01",
            "I think I'll start with Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612FM-Me!?\x02\x03",
            "#12613F...I-It's fine... But don't touch \x01",
            "any strange places, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#12503FI-I'll be careful.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 18300, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 18900, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0xA, 18400, -5900, 18300, 0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_70(0x1, 0x2)
    SetChrSubChip(0x8, 0x2)
    OP_68(18400, -4700, 18300, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#12501FH-Here I go...\x02\x03",
            "#12503F(*squeeze*)\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x64, 0xBB8, 0x12C)

    def lambda_8AAC():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8AAC)

    ChrTalk(
        0xA,
        "#6P#12615F#4SAhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12505FS-Sorry! You ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#12613FY-Yeah. It was just a bit\x01",
            "cold, I was just surprised.\x02\x03",
            "#12602FIt's fine, please continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FA-Alright, then...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 9000)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(*sigh*, this is worse for the\x01",
            "heart than I had imagined...)\x02\x03",
            "#12508F(But Elie, you're\x01",
            "really pretty...)\x02\x03",
            "#12503F(Your pure white\x01",
            "skin and shiny\x01",
            "pearl grey hair...)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#6P#12612F...H-Hey. Don't you go\x01",
            "quiet all of a sudden.\x02\x03",
            "#12611FYou're not thinking about\x01",
            "anything lewd, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FD-Don't be ridiculous!\x02\x03",
            "#12503F(If I'm careless, Miss Mariabell will sink\x01",
            "me to the bottom of this lake...!!)\x02\x03",
            "#12501F(...I've got to calm myself.\x01",
            "Think empty thoughts...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_4C(0x101, 0xFF)
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#N#13506FMr. Lloyd...\x01",
            "Somehow your face looks like the\x01",
            "East Street venerable Jizｷ's one.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P#13309FUh uh, Lloyd.\x01",
            "After you're finished with Miss Elie,\x01",
            "please take care of us too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_9C53")

    label("loc_8E91")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then...\x01",
            "I think I'll start with sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FUh uh, all right.\x01",
            "Then, please.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 20800, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 21400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x8, 18400, -5900, 20800, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    OP_70(0x1, 0x3)
    OP_68(18400, -4700, 20800, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#11P#12500F...How is it, sister Cecil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304FYes, like that.\x01",
            "Then, apply it by spreading it thinly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12500FYes, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304F...Uh uh, somehow this\x01",
            "brings back memories.\x02\x03",
            "#13302FWhen you were a kid, sometimes we\x01",
            "washed our backs each other in the bath.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FGaaah, s-sister Cecil!!\x01",
            "What're you saying in front of everyone!?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_63(0x8, 0xFFFFFE0C, 1700, 0x2, 0x7, 0x50, 0x1)

    def lambda_917E():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_917E)

    ChrTalk(
        0x8,
        (
            "#6P#13306FEek!\x02\x03",
            "#13309F...Uh uh, oh, Lloyd.\x01",
            "No touching in strange places, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#12511FWhoah, s-sorry!!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    SetCameraDistance(13500, 9000)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(Aah, jeez...\x01",
            "You're too defenseless, sister Cecil!!)\x02\x03",
            "#12508F(A-Also, when she's exposed she's got \x01",
            "such an outstanding destructive power...)\x02\x03",
            "#12506F(...Wait, what am I saying!?\x01",
            "I can't think about sister Cecil that way!)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#13305FLloyd, what's wrong?\x01",
            "It seems you've been applying it\x01",
            "to the same spot for some time...\x02\x03",
            "#13308F...Could I've become...fat?\x02\x03",
            "#13306FBecause I often receive pastries\x01",
            "from the patients and the Head Nurse,\x01",
            "I end up eating them without thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FN-No no, that's not\x01",
            "the case at all!!\x01",
            "You don't have to worry, you're very pretty...\x02\x03",
            "#12506F...Ah, no, I mean...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#13309FUh uh, thank you Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#12611F(Hmmm...\x01",
            "Pampered as always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509F(Ahaha...\x01",
            "It seems it's like I had heard.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9C53")

    label("loc_954A")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then...\x01",
            "I think I'll start with Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13505FY-Yes!\x02\x03",
            "#13503FI am inexperienced, but please\x01",
            "take good care of me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#12506F...There's something wrong in what you said.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 23200, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 23800, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x9, 18400, -5900, 23200, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    OP_70(0x1, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_68(18400, -4700, 23200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#11P#12502FWhoops...i-is it ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13503FAh, yes.\x01",
            "I think you're doing it all right.\x02\x03",
            "#13506F*haah*, thank you, really.\x01",
            "Since I appear in the Arc-en-ciel\x01",
            "plays, I can't get sunburns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FAh, I that so?\x02\x03",
            "#12505FOh, but...\x01",
            "Didn't you put sunscreen\x01",
            "on Miss Ilya?\x02\x03",
            "#12511FYou could've asked her to──\x01",
            "...Ah, wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13509FE-Eeehm...Ahaha.\x01",
            "In short, it's as you think.\x02\x03",
            "#13506FIf Miss Ilya had me in such\x01",
            "a defenseless state, I can't\x01",
            "imagine what she'd do to me...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(13500, 9000)

    ChrTalk(
        0x101,
        (
            "#11P#12512F(It means that I'm better than\x01",
            "the old man-like Miss Ilya...?\x01",
            "It's a mixed motive, though.)\x02\x03",
            "#12501F(...Even so, it's hard to tell\x01",
            "from her appearance, but Rixia\x01",
            "has quite a trained body.)\x02\x03",
            "#12508F(Despite these proportions,\x01",
            "she has such physical abilities...\x01",
            "I guess this is also what's to be a "genius".)\x02\x03",
            "#12503F(Rather, with this height it's probably\x01",
            "not exaggerated saying that she's\x01",
            "truly a dangerous weapon...)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#6P#13505FM-Mr. Lloyd? Your glance is...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FWah, s-sorry!\x02\x03",
            "#12512FW-Well, you see, it's not like that.\x01",
            "I was thinking that you're really trained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#N#12611F*haah*...I wonder why\x01",
            "boys are like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13309FUh uh, Lloyd.\x01",
            "Please put the sunscreen on us too\x01",
            "after you're finished with Rixia, hm?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9C53")

    label("loc_9C53")

    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 20300, -6000, 17500, 315)
    SetChrPos(0x9, 18400, -5900, 23000, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x8, 18400, -5900, 20600, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0xA, 18400, -5900, 18100, 0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_70(0x1, 0x6)
    Sleep(2000)
    OP_68(18400, -5000, 24100, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_68(18400, -5000, 18200, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(19000, -5000, 20000, 0)
    MoveCamera(319, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#12506F(L-Looking again, it really\x01",
            "is an amazing view...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FAhhh... Thanks, Lloyd.\x01",
            "That was very relaxing.\x02\x03",
            "#13309FUhuhu, I might fall asleep at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1P#12606FM-Miss Cecil, I think\x01",
            "sleeping like that would\x01",
            "be rather dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P#13509FAhaha... That might\x01",
            "be overstating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#13304FUh uh, but it feels so good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#12500FAlright then, how about some\x01",
            "cold drinks to wake everyone up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1P#12605FOh, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12503F(This experience was more\x01",
            "like a dream, in a way...)\x02\x03",
            "#12512F(Honestly, if I don't do at least\x01",
            "this much, Aidios will punish me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P#13505F...Mr. Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12512FU-Uhh, no, nevermind.\x02\x03",
            "#12500FHow about non-alcoholic\x01",
            "cocktails for everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FYes that would be fine.\x02\x03",
            "#13309FOh, but you don't have to hurry.\x01",
            "We want you to have fun too, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12500FSure, thanks.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetScenarioFlags(0x15D, 1)
    Call(0, 45)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x20)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    ClearMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A202")
    Call(0, 54)
    EventEnd(0x5)
    Jump("loc_A215")

    label("loc_A202")

    SetChrPos(0x0, 21500, -6000, 20700, 90)
    EventEnd(0x5)

    label("loc_A215")

    Return()

    # Function_41_8715 end

    def Function_42_A216(): pass

    label("Function_42_A216")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A22D")
    OP_A0(0xFE, 500, 0x0, 0x3)
    Jump("Function_42_A216")

    label("loc_A22D")

    Return()

    # Function_42_A216 end

    def Function_43_A22E(): pass

    label("Function_43_A22E")

    EventBegin(0x0)
    Fade(500)
    OP_68(32000, -4750, 6750, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2500)
    SetChrPos(0x101, 30690, -6000, 8050, 135)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7DF")

    ChrTalk(
        0xC,
        "#6P#13101F*pack, pack*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12701F*pat, pat*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12505F(T-They're concentrating pretty\x01",
            "hard on this, aren't they...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200F...Grrowl...woof.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A406")
    Jump("loc_A450")

    label("loc_A406")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A426")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A450")

    label("loc_A426")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A446")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A450")

    label("loc_A446")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A450")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A506")
    Jump("loc_A550")

    label("loc_A506")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A526")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A550")

    label("loc_A526")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A546")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A550")

    label("loc_A546")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A550")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xB,
        "#12P#12705F...Oh, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13100FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FHa ha, guess I interrupted you.\x02\x03",
            "#12500FI was just wondering what\x01",
            "you girls were making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FNo, no, don't worry about it.\x02\x03",
            "#13109FWe're making a\x01",
            "sand castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FIn other words, "sand crafts."\x02\x03",
            "#12706FBut it is not going so well...\x01",
            "Anything we make keeps collapsing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FHmm, looks pretty tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh! Since you're here, why\x01",
            "don't you help us out, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12505FHuh? Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FYes, she is right. With your help, \x01",
            "we might be able to make some progress.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 1)
    Jump("loc_AA73")

    label("loc_A7DF")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A870")
    Jump("loc_A8BA")

    label("loc_A870")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A890")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8BA")

    label("loc_A890")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8B0")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8BA")

    label("loc_A8B0")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8BA")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A970")
    Jump("loc_A9BA")

    label("loc_A970")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A990")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A9BA")

    label("loc_A990")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9B0")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A9BA")

    label("loc_A9B0")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9BA")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, Mr. Lloyd.\x01",
            "Will you help us\x01",
            "to make a sand castle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FBy all means, please.\x01",
            "we might be able to make some progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA73")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Help Build the Sand Castle\x01",      # 0
            "Quit\x01",                            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABFD")

    ChrTalk(
        0x101,
        (
            "#11P#12500FSure, alright.\x01",
            "If you're fine with me, I'll help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FAs expected from Mr. Lloyd!\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHa ha. I say that but I'm\x01",
            "a total newbie at this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, I think we all are.\x02\x03",
            "#12704FThen, let's get started now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 44)
    Call(0, 45)
    Jump("loc_ACE7")

    label("loc_ABFD")


    ChrTalk(
        0x101,
        "#11P#12512FUhmm, now it wouldn't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13106FEeh, no waay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, please absolutely tell us\x01",
            "if you feel like it.\x02\x03",
            "#12704FUntil then, I will do my best\x01",
            "with Miss Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)

    label("loc_ACE7")

    SetChrPos(0x0, 29920, -6000, 8910, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD10")
    Call(0, 54)

    label("loc_AD10")

    EventEnd(0x5)
    Return()

    # Function_43_A22E end

    def Function_44_AD13(): pass

    label("Function_44_AD13")

    LoadChrToIndex("chr/ch15200.itc", 0x1E)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "#6P#13100F...*phew*, it is coming along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12700FYes. Almost th──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(1023, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    OP_70(0xA, 0x3)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#01203F...Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12706F...This is really difficult.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FHmm. Maybe there's\x01",
            "some problem with the\x01",
            "hardness of the sand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105FHardness...?\x02\x03",
            "#13106FWe've put sand and water in a bucket\x01",
            "and diligently made the foundations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FBut it dries out when you make\x01",
            "something with it, right?\x02\x03",
            "#12504FI think I've heard it's better \x01",
            "to add water a little at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12705FI see... \x01",
            "That makes sense.\x02\x03",
            "#12702FAlright then, how much water\x01",
            "should we add at a time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FHmm, let me think...\x02",
    )

    CloseMessageWindow()
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
            "#1KHow much water will you add?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Plenty\x01",                  # 0
            "A Little More\x01",           # 1
            "Just a Tiny Little\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1E2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500FJust a tiny little, I think...\x01",
            "Just enough to get it wet.\x02\x03",
            "#12504FIf you add too much, the\x01",
            "hardness will decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FNow that you say it,\x01",
            "I think I get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FThen, let's try doing\x01",
            "as Mr. Lloyd says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B35B")

    label("loc_B1E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B280")

    ChrTalk(
        0x101,
        (
            "#11P#12500FShouldn't it be the case\x01",
            "to make it while using\x01",
            "plenty of water?\x02\x03",
            "#12504FThat way the hardness would increase...\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B302")

    label("loc_B280")


    ChrTalk(
        0x101,
        (
            "#11P#12500FMaybe we should make it\x01",
            "while using a little more water?\x02\x03",
            "#12504FThat way the hardness would increase...\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B302")


    ChrTalk(
        0xC,
        "#6P#13105FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FWell, let's try doing it\x01",
            "like Mr. Lloyd says.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B35B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B509")
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#12P#12702FIt is almost done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FYeah, thanks to \x01",
            "Mr. Lloyd's advice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12502FHa ha, I'm happy to hear you say that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702FUh uh... Then, it is finally\x01",
            "time for the finishing touches.\x02\x03",
            "We need to improve the details\x01",
            "on the main part of the castle...\x01",
            "Mr. Lloyd, can we ask you to do it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6D1")

    label("loc_B509")


    ChrTalk(
        0xB,
        "#12P#12700FIt is almost done, however...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xC,
        "#6P#13105FS-Somehow water is coming out here and there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12506F(U-Uhhm...\x01",
            "Maybe there was really too much water...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FWell, I don't think it\x01",
            "will collapse for now...\x01",
            "It is time for the finishing touches.\x02\x03",
            "#12702FWe need to improve the details\x01",
            "on the main part of the castle...\x01",
            "Mr. Lloyd, can we ask you to do it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6D1")


    ChrTalk(
        0x101,
        (
            "#11P#12500FYeah, got it.\x01",
            "Leave it to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FWe're betting everything on you,\x01",
            "Mr. Lloyd! We're counting on you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(S-So much pressure...\x01",
            "Anyway, I've gotta do this.)\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12501F(Alright. We used water to\x01",
            "harden the sand, but in\x01",
            "the end, it's just sand...)\x02\x03",
            "#12503F(What's important here are\x01",
            "probably speed and power.\x01",
            "...How should I proceed?)\x02",
        )
    )

    CloseMessageWindow()
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
            "#1KWhat about the speed and power?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Slowly/Gently\x01",         # 0
            "Slowly/Strongly\x01",       # 1
            "Quickly/Gently\x01",        # 2
            "Quickly/Strongly\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B93F"),
        (1, "loc_B984"),
        (2, "loc_B9CB"),
        (3, "loc_BA1B"),
        (SWITCH_DEFAULT, "loc_BA63"),
    )


    label("loc_B93F")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it slowly, yet gently!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA63")

    label("loc_B984")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it slowly, yet strongly!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA63")

    label("loc_B9CB")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it quickly, yet gently!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA63")

    label("loc_BA1B")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it quickly, yet strongly!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA63")

    label("loc_BA63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA81")
    Jump("loc_BE35")

    label("loc_BA81")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(1023, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    OP_70(0xA, 0x3)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#12511F#4SAh.#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12705FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FAww... Ahaha.\x01",
            "It went down.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#11P#12505FWell, uhm, what should I say...\x02\x03",
            "#12506F...I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F...Well, it can't be helped.\x02\x03",
            "#12700FLet's rebuild it\x01",
            "from square one.\x02\x03",
            "Mr. Lloyd, please\x01",
            "support Miss Fran and me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12512FR-Roger that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FMr. Lloyd, \x01",
            "please don't feel down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD3B")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(The amount of water\x01",
            "seemed right, but...)\x02\x03",
            "(*haah*...I lost my face.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE35")

    label("loc_BD3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDB0")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(The way I did it shouldn't\x01",
            "have been wrong, but...)\x02\x03",
            "(*haah*...I lost my face.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE35")

    label("loc_BDB0")


    ChrTalk(
        0x101,
        (
            "#11P#12506F(I can only think that both the amount of water\x01",
            "and the way I did it were wrong, but...)\x02\x03",
            "(*haah*...I lost my face.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE35")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x2)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#12500F*phew*... That should do it.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#6P#13100FIt's... \x01",
            "It's finally done!!\x02\x03",
            "#13109FEek! We did it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFED")
    OP_2C(0xA5, 0x1)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12704FHow moving. Good\x01",
            "work, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHa ha, don't mention it. It's because\x01",
            "you two worked so hard, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FNo, no! It's because of you, Mr. Lloyd!\x01",
            "Thank you so very much!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0C8")

    label("loc_BFED")

    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F...In any case, I am glad.\x01",
            "Many things happened until it was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12506FI-I'm really sorry for all that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FAhaha, it's fine already.\x01",
            "We managed to complete it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0C8")

    TurnDirection(0xB, 0xD, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F#5PGood job too, Zeit.\x02\x03",
            "#12704FIn the final part, you helped by\x01",
            "supplying us sand and water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        "#11P#12500F#5PHa ha, as expected from Zeit.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#12505FBy the way, does this\x01",
            "castle have a name?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x5A, 0x1F4)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        "#6P#13105FA...name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FWell, we went through all the\x01",
            "trouble of making it. A name will\x01",
            "help us remember that experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12703FIt makes sense.\x01",
            "Hmm, then...\x02\x03",
            "#12700FHow about\x01",
            ""Michey Castle"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105FAww, no fair, Tio!\x02\x03",
            "#13109FIn that case, I'm going\x01",
            "with "Ban Ban Castle"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FMichey is more well known, but...\x02\x03",
            "#12503FI think Ban Ban is the\x01",
            "name of your favorite\x01",
            "stuffed animal, Fran?\x02\x03",
            "#12509FHa ha... I guess I\x01",
            "like both names.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F...However, the same castle\x01",
            "can't have two names.\x02\x03",
            "#12700FWhy don't we have Mr. Lloyd\x01",
            "decide which is better?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FYeah, I like it!\x02\x03",
            "#13109FYou'll decide it, Mr.\x01",
            "Lloyd! No objections!\x01",
            "Give it to us straight!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(T-This is a heavy responsibility.)\x02\x03",
            "#12500FHmm, let's see...\x02",
        )
    )

    CloseMessageWindow()
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
            "#1KWhich castle name will you choose?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Michey Castle\x01",       # 0
            "Ban Ban Castle\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C727")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#5PWell, since we're\x01",
            "at Michelam...\x02\x03",
            "#12500FHow about we go with\x01",
            ""Michey Castle"?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13106FHmm. That does make sense, \x01",
            "now that I think about it.\x02\x03",
            "#13102FIt can't be helped. \x01",
            "I'll have to hand this one to Tio!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        "#12P#12702FUh uh... Thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C856")

    label("loc_C727")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#11PLet's see, we can see Michey as\x01",
            "much as we want later too, so...\x02\x03",
            "#12500FHow about\x01",
            ""Ban Ban Castle"?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F...Hm, you have a point.\x02\x03",
            "#12702FWell, alright, we will go with\x01",
            "Miss Fran's suggestion this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        "#6P#13109FUh uh, thank you, Tio!\x02",
    )

    CloseMessageWindow()

    label("loc_C856")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#12509FHa ha, well that was settled peacefully.\x02\x03",
            "#12505FThat's right... Tio, Fran, you've always been\x01",
            "here at the beach, aren't you getting thirsty?\x02\x03",
            "#12500FIf you like, I can bring\x01",
            "you something fresh later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FLet me think...\x02\x03",
            "#12700FI would like to eat the shaved\x01",
            "ice they have at the stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, I want to eat it too!\x02\x03",
            "#13109FMr. Lloyd, can we ask you that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12509FYeah, leave it to me.\x02\x03",
            "#12500FFor Zeit... Will\x01",
            "a hot dog be ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01203FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702F"Please do", he says.\x02\x03",
            "#12703F...Oh, but there is no need to\x01",
            "rush. We are good for now.\x02\x03",
            "#12702FIt is a rare opportunity to come here,\x01",
            "so please enjoy yourself too, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12502FHa ha, roger that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15E, 2)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)
    OP_49()
    OP_D7(0x1E)
    Return()

    # Function_44_AD13 end

    def Function_45_CBAE(): pass

    label("Function_45_CBAE")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_END)), "loc_CBCB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CBCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_END)), "loc_CBDE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CBDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_CBF1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CBF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC38")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_CC38")

    Return()

    # Function_45_CBAE end

    def Function_46_CC39(): pass

    label("Function_46_CC39")

    EventBegin(0x0)
    Fade(500)
    OP_68(44860, -6090, 2460, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2000)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 44110, -7060, 2460, 90)
    OP_6F(0x79)
    OP_0D()
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D16D")

    ChrTalk(
        0xE,
        (
            "#13209F#6PWaaah... \x01",
            "Sully's pretty too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#11PH-Hmph, it's no big deal.\x02\x03",
            "#13600FBut this stone... I've never\x01",
            "seen anything like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PYou girls are back.\x01",
            "...What're you up to?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CDAC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_CDAC)
    Sleep(50)

    def lambda_CDBC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CDBC)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xE,
        (
            "#13210F#12PAh, Lloyd.\x01",
            "Look at this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12PEhehe, pretty, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PWow, it's round and pure white...\x01",
            "A pretty stone almost like a jewel.\x02\x03",
            "#12505FWhere did you get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13600F#12PShorty here picked it up\x01",
            "earlier when she was swimming.\x02\x03",
            "#13604FIt seems there's more\x01",
            "all over the place so we\x01",
            "went looking for them.\x02\x03",
            "#13602FWe asked the lifeguard,\x01",
            "and he said they're\x01",
            "called "White Stones".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PHmm. The sand here seems it was \x01",
            "carried in from another country...\x02\x03",
            "#12503FSo maybe there're more of\x01",
            "them mixed in around here.\x02\x03",
            "#12500FThere might be even pretty\x01",
            "big ones buried in the sand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#13205F#12PReally!?\x02\x03",
            "#13200FHey, hey, let's all look\x01",
            "for the White Stones!\x02\x03",
            "#13209FAnd in the end, whoever has the\x01",
            "biggest one, will be the winner!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#13602F#12PHeh, sounds interesting.\x02\x03",
            "#13604FYou're playing too, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 6)
    Jump("loc_D211")

    label("loc_D16D")


    def lambda_D172():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_D172)
    Sleep(50)

    def lambda_D182():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_D182)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xF,
        (
            "#13600F#12PHm, you want to take part\x01",
            "in this too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13202F#12PLloyd, let's search\x01",
            "for "White Stones"\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D211")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Start Searching\x01",      # 0
            "Quit\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D488")

    ChrTalk(
        0x101,
        (
            "#12500F#5PSure, since I'm here,\x01",
            "I guess I'll play along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12PIt's decided then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13600F#12PThen, tell me once\x01",
            "you've found a\x01",
            ""White Stone" too.\x02\x03",
            "#13604FThen we'll compare the size and\x01",
            "who's got the biggest one wins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509F#5PHa ha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13201F#12PAlllright...\x01",
            "Start!\x02\x03",
            "#13200FKeA will definitely\x01",
            "find the biggest one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#12PHmph, as if I'd\x01",
            "lose to you guys.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15C, 0)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    SetChrPos(0x0, 45110, -7080, 2460, 90)
    Jump("loc_D56B")

    label("loc_D488")


    ChrTalk(
        0x101,
        "#12512F#5PUhhm, I won't do it now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13205F#12PEeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606F#12PTch, you're no fun.\x02\x03",
            "#13600FWell, tell me when you feel like doing it.\x01",
            "We'll let you join then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 43610, -7090, 2460, 270)

    label("loc_D56B")

    EventEnd(0x5)
    Return()

    # Function_46_CC39 end

    def Function_47_D56E(): pass

    label("Function_47_D56E")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12503FHmm, this one's a little small...?\x02\x03",
            "I think there's bigger ones around...\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x15C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_47_D56E end

    def Function_48_D61B(): pass

    label("Function_48_D61B")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FFound one, but...it's small.\x02\x03",
            "Should I search a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x15C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_48_D61B end

    def Function_49_D6BB(): pass

    label("Function_49_D6BB")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x329, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12500FA size that cleanly fits\x01",
            "into the palm of a hand.\x02\x03",
            "#12503FIt seems that both KeA and Sully\x01",
            "have found at least some like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x15C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_D6BB end

    def Function_50_D79F(): pass

    label("Function_50_D79F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x329, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12503F...This one's kind of big.\x02\x03",
            "#12500FThis one might do\x01",
            "for a good contender.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x15C, 4)
    TalkEnd(0xFF)
    Return()

    # Function_50_D79F end

    def Function_51_D84D(): pass

    label("Function_51_D84D")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FOoh...!?\x01",
            "It's got the size of a crystal ball!\x02\x03",
            "#12509FHa ha, it seems I'll hardly\x01",
            "lose with such a size.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x15C, 5)
    TalkEnd(0xFF)
    Return()

    # Function_51_D84D end

    def Function_52_D919(): pass

    label("Function_52_D919")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 18310, -6000, 15790, 0)
    SetChrSubChip(0xA, 0x2)
    OP_68(18950, -4400, 16440, 0)
    MoveCamera(312, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "#12605FOh, Lloyd. What're you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12500FI'm playing with KeA and Sully...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#12505FHey, is that...?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd reached under\x01",
            "the deck chair.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12612FEh, w-wait...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12502F──Got it!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#6P#12500FTo think it was buried\x01",
            "in a place like this...\x02\x03",
            "#12504FBut, it's huge.\x01",
            "I should definitely win with this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12611FY-You... What were\x01",
            "you thinking, suddenly\x01",
            "crawling down there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12511FAh... S-Sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12606F*sigh*, seriously.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x15C, 6)
    EventEnd(0x5)
    Return()

    # Function_52_D919 end

    def Function_53_DBE8(): pass

    label("Function_53_DBE8")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_68(44860, -6090, 2460, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2000)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrPos(0xE, 45610, -7090, 1880, 270)
    SetChrPos(0xF, 45610, -7090, 3000, 270)
    SetChrPos(0x101, 44110, -7060, 2460, 90)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#12P#13600FAlright, let's compare sizes.\x02\x03",
            "#13603FBring out your\x01",
            "biggest one on the\x01",
            "count of three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12500FYeah, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13210FI'm all set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13601FAlright, here we go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12501FOne, two...\x02",
    )


    ChrTalk(
        0xE,
        "#3P#13201FOne, two...\x02",
    )


    ChrTalk(
        0xF,
        "#4P#13601FOne, two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12500F#4SThree!#3S\x02",
    )


    ChrTalk(
        0xE,
        "#3P#13200F#4SThree!!#3S\x02",
    )


    ChrTalk(
        0xF,
        "#4P#13600F#4SThree!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E81A")
    OP_2C(0xA5, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13210FWaaaaaa... Lloyd's\x01",
            ""White Stone"...\x01",
            "It's huge!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13601FTch... I can't believe\x01",
            "you found one like that.\x02\x03",
            "#13606FDamn. Guess I can \x01",
            "only accept my loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12502FHa ha, then it seems you're\x01",
            "fine with me winning, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13606FTch, such a sore winner. How childish.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12506F...You make me lose my face\x01",
            "if you tell me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12P#13200FBut it's really big and pretty.\x02\x03",
            "#13206FKeA wanted one like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FYeah... I'll keep looking \x01",
            "a little more too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E284")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FHa ha, then I'll give you\x01",
            "these "White Stones"\x01",
            "as a present.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12P#13210FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13605FA-Are you sure?\x01",
            "Also, two...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, I've picked up\x01",
            "another one of the\x01",
            "same size.\x02\x03",
            "#12509FIt's a rare occasion to have come to the beach,\x01",
            "so they could be a nice memento.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave KeA and Sully\x01",
            "a big "White Stone" each.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#12P#13612FH-Hmph...thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13209FEhehe. I'll treasure it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber(0x32C, 2)
    Jump("loc_E815")

    label("loc_E284")


    ChrTalk(
        0x101,
        (
            "#5P#12500F(That's right, I went to the\x01",
            "trouble of getting it... Maybe I\x01",
            "should give it to one of them.)\x02",
        )
    )

    CloseMessageWindow()
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
            "#1KWho will you give the "White Stone" to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Give it to KeA\x01",        # 0
            "Give it to Sully\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E5")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FAlright then, how about\x01",
            "I give you this "White Stone"\x01",
            "as a present, KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12P#13210FHuh, really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, of course.\x02\x03",
            "#12509FI think this will make a nice memento\x01",
            "of our beach vacation for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave the big\x01",
            ""White Stone" to KeA.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        "#12P#13209FEhehe. I'll treasure it!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "#12P#13606F#11PTch, how nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FSorry, Sully. You're older\x01",
            "than KeA, so can I ask\x01",
            "you to grin and bear it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xF,
        (
            "#12P#13612FI-I didn't...\x01",
            "Want such a pebble at all, you know!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber(0x32C, 1)
    Jump("loc_E815")

    label("loc_E5E5")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FAlright then, how about\x01",
            "I give you this "White Stone"\x01",
            "as a present, Sully?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#12P#13605FHuh...i-is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, of course.\x02\x03",
            "#12509FI think this will make a nice memento\x01",
            "of our beach vacation for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave the big\x01",
            ""White Stone" to Sully.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#12P#13612FH-Hmph...thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#12P#13209F#6PHow nice, eh, Sully?\x01",
            "Let me touch it later, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FSorry KeA.\x01",
            "In exchange, I'll buy you\x01",
            "a new book next time.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#12P#13200FAh, yes!\x01",
            "I can't wait!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SubItemNumber(0x32C, 1)

    label("loc_E815")

    Jump("loc_EB19")

    label("loc_E81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E946")
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13205FOoh, they're\x01",
            "all the same size!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FYeah...it looks like their\x01",
            "size is basically the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FThen, I guess that\x01",
            "it's a draw this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13606FTch, what a boring conclusion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12512FHa ha, don't say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB19")

    label("loc_E946")

    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13200FWaah, Lloyd's stone\x01",
            "is tiny and cute!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13600FYeah...pretty small.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12512FH-Ha ha ha...\x01",
            "It seems I've lost, eh?\x02\x03",
            "#12500FKeA's and Sully's looks\x01",
            "almost the same size,\x01",
            "so you win this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13209FYaay, hooray!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13606FTch, somehow you're\x01",
            "showing some composure.\x02\x03",
            "#13602FUh uh, but in your heart\x01",
            "you're regretting it badly, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12506FUgh...\x01",
            "T-That's not true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB19")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12500FThat's right... KeA, Sully, do you\x01",
            "want anything cold to drink...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13200FHuh? You'll get it for us, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12504FYeah. You've been playing on the\x01",
            "seashore the whole time, and you\x01",
            "must be getting pretty tired, right?\x02\x03",
            "#12500FIf there's anything you want\x01",
            "to eat or drink, just say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13600FHmm, how thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13204FHmm, then...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13210FAh, I want the ice cream\x01",
            "I saw at the shop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FIce cream, eh?\x01",
            "Ha ha, got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13604FMe too, then.\x02\x03",
            "#13600FOh, but I want to play a bit more,\x01",
            "so don't bring them right away, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, got it.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15C, 7)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    SetChrPos(0x0, 43610, -7090, 2460, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE68")
    Call(0, 54)

    label("loc_EE68")

    EventEnd(0x5)
    Return()

    # Function_53_DBE8 end

    def Function_54_EE6B(): pass

    label("Function_54_EE6B")

    FadeToBright(1000, 0)
    OP_68(22000, -4500, 0, 0)
    OP_68(22000, -5000, 0, 2500)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetChrPos(0x101, 22000, -6000, 0, 90)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12500FEveryone's having a good time\x01",
            "and it seems they're relaxing now.\x02\x03",
            "#12503F...But I'm kind\x01",
            "of thirsty too.\x02\x03",
            "#12500FI did promise to buy cold food and\x01",
            "drinks for everyone. I think it's\x01",
            "about time I headed to the shop.\x02\x03",
            "It's just up the stairs.\x01",
            "...I'll go check it out.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    SetScenarioFlags(0x15E, 3)
    Return()

    # Function_54_EE6B end

    def Function_55_EFE4(): pass

    label("Function_55_EFE4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-8270, -500, 8450, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(13250, 2500)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x101, -7270, -1500, 8450, 270)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2FA")

    ChrTalk(
        0x22,
        (
            "Hey, welcome. Enjoying\x01",
            "your beach reservation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12502F#12PHa ha, yeah. Everyone's having a good time.\x02\x03",
            "Actually, I need to order\x01",
            "quite a few things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I just finished getting\x01",
            "everything ready.\x01",
            "Please order anything you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#12PUmm, then...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F#12P...Ah. Come to think of it, \x01",
            "I left my wallet in the locker.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oh, don't worry about paying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Miss Mariabell said to give you guys\x01",
            "anything you wanted on the house \x01",
            "during your reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#12PR-Really!?\x02\x03",
            "#12512FShe's nothing if not thorough...\x01",
            "I have to take my hat off to\x01",
            "Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Ha ha. Your thanks are enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Then, will you be ordering?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F364")

    label("loc_F2FA")


    ChrTalk(
        0x22,
        (
            "During your reservation,\x01",
            "anything you want is on the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Will you be ordering something now?\x02",
    )

    CloseMessageWindow()

    label("loc_F364")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Once you place your\x01",
            "order, the lake beach\x01",
            "event will end.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Order]\x01",      # 0
            "[Quit]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F70C")

    ChrTalk(
        0x101,
        (
            "#12500F#12PYes, thank you.\x02\x03",
            "#12503FUmm, 4 Bell-Colas, \x01",
            "3 non-alcoholic cocktails...\x02\x03",
            "#12500F2 ice creams, 2 shaved ices... \x01",
            "Oh, and one hot dog, please.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "Planning on carrying all\x01",
            "of that in one trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Could you possibly be... The type that's overly\x01",
            "softhearted to the point of self-destruction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#12PN-No, ha ha... \x01",
            "I don't think so.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(136, 2000, 90)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──And so, everyone had a fun time at the beach.\x02\x03",
            "After that, Lloyd and the others enjoyed\x01",
            "a watermelon splitting game together──\x02\x03",
            "As they savored lunchboxes\x01",
            "delivered by the hotel, their\x01",
            "excitement began to build.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15E, 4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_END)), "loc_F6C9")
    SubItemNumber(0x32B, 1)

    label("loc_F6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_END)), "loc_F6D7")
    SubItemNumber(0x32B, 1)

    label("loc_F6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_END)), "loc_F6E5")
    SubItemNumber(0x329, 1)

    label("loc_F6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_END)), "loc_F6F3")
    SubItemNumber(0x329, 1)

    label("loc_F6F3")

    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_F780")

    label("loc_F70C")


    ChrTalk(
        0x101,
        "#12500F#12PNo, I'm still fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Well, please do it before\x01",
            "your reserved time ends.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F780")

    SetChrPos(0x0, -6770, -1500, 8450, 90)
    OP_4C(0x22, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_55_EFE4 end

    def Function_56_F798(): pass

    label("Function_56_F798")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7CA")
    SetScenarioFlags(0x31, 2)

    label("loc_F7CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F810")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_F80A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F7FF")
    Sound(2499, 255, 100, 0)
    Jump("loc_F805")

    label("loc_F7FF")

    Sound(3537, 255, 100, 0)

    label("loc_F805")

    Jump("loc_F810")

    label("loc_F80A")

    Sound(3344, 255, 100, 0)

    label("loc_F810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_F883")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F863"),
        (SWITCH_DEFAULT, "loc_F874"),
    )


    label("loc_F863")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_F87E")

    label("loc_F874")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F87E")

    Jump("loc_FABE")

    label("loc_F883")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F8B5")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_F8B5")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F8E7"),
        (1, "loc_F9EB"),
        (2, "loc_FA7C"),
        (SWITCH_DEFAULT, "loc_FAB4"),
    )


    label("loc_F8E7")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F918")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F928")

    label("loc_F918")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F928")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F97E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F97E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9A1")
    Sound(461, 0, 100, 0)

    label("loc_F9A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F9C1")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_F9D1")

    label("loc_F9C1")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_F9D1")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_F810")

    label("loc_F9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_FA5D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_FA20")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_FA38")

    label("loc_FA20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_FA33")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_FA38")

    label("loc_FA33")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_FA38")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA77")

    label("loc_FA5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_FA6D")
    OP_AF(0xFB)
    Jump("loc_FA77")

    label("loc_FA6D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA77")

    Jump("loc_FABE")

    label("loc_FA7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA95")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FAAF")

    label("loc_FA95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_FAA5")
    OP_AF(0xFB)
    Jump("loc_FAAF")

    label("loc_FAA5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAAF")

    Jump("loc_FABE")

    label("loc_FAB4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FABE")

    Jump("loc_F810")

    label("loc_FAC3")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_F798 end

    def Function_57_FAD1(): pass

    label("Function_57_FAD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FAED")
    Jump("loc_12341")

    label("loc_FAED")

    LoadChrToIndex("chr/ch15100.itc", 0x1F)
    LoadChrToIndex("chr/ch15200.itc", 0x20)
    LoadChrToIndex("chr/ch15800.itc", 0x24)
    LoadChrToIndex("chr/ch16000.itc", 0x25)
    LoadChrToIndex("apl/ch51303.itc", 0x28)
    SoundLoad(3395)
    SoundLoad(2716)
    SoundLoad(3516)
    SoundLoad(2677)
    SoundLoad(3245)
    SoundLoad(3613)
    OP_90(0x101, 3000, 0, 2500, 90)
    OP_90(0x104, 2000, 0, 1500, 90)
    OP_90(0x105, 1500, 0, 3500, 90)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrFlags(0xE, 0x8)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x8)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrFlags(0xB, 0x8)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrFlags(0x12, 0x8)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x8)
    OP_4B(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrFlags(0x10, 0x8)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x8)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x8)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xF, 0x40)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_68(50000, 0, -28000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(41500, 0)
    FadeToBright(1000, 0)
    OP_68(50000, 0, 12000, 10000)
    Sleep(9000)
    Fade(1000)
    OP_68(39000, -4000, -1000, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(39000, 3000, -1000, 9000)
    OP_6F(0x79)
    Fade(1000)
    OP_68(86000, 3800, 6000, 0)
    MoveCamera(90, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(70000, 0)
    PlaceName2(340, 200, "c_plac45", 0x0, 3000)
    MoveCamera(90, 0, 0, 9000)
    SetCameraDistance(60000, 9000)
    OP_6F(0x79)
    Fade(1000)
    OP_68(50000, -1000, 0, 0)
    MoveCamera(321, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20000, 0)
    OP_68(20000, -1000, 0, 10000)
    Sleep(1500)

    def lambda_FE52():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FE52)
    Sleep(0)

    def lambda_FE6A():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FE6A)
    Sleep(0)

    def lambda_FE82():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FE82)
    Sleep(0)
    Sleep(5500)
    Sound(2757, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#12809F#5P#10A#4SWoah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Fade(1000)
    OP_68(17000, -5000, 2500, 0)
    MoveCamera(321, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(12500, 2500)
    Sleep(1500)
    Sound(2080, 255, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#12502F#5PThis is incredible...\x02\x03",
            "#12509FIt's my first time at a beach but I\x01",
            "didn't think it would be this pretty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12904F#5PBeaches are normally on the coast,\x01",
            "so the sand isn't usually this white.\x02\x03",
            "#12902FThey probably trucked in this\x01",
            "sand from "White Heaven"\x01",
            "beach in eastern Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1007F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1007F)
    Sleep(50)

    def lambda_1008F():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1008F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12511F#12PSeriously...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12806F#6PI can hardly believe it...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12909F#5PHa ha, it reminds you of IBC's\x01",
            "asset strength all over again.\x02\x03",
            "#12900FBut shouldn't we prepare\x01",
            "things before the girls come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12800F#6POh, that's right.\x02\x03",
            "#12809FParasols are standard\x01",
            "for a beach, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#12PI see. I think I remember\x01",
            "seeing them in a magazine.\x02\x03",
            "#12500FAlright. Let's split up and get everything ready.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    ClearMapObjFlags(0x1, 0x4)
    OP_68(18000, -5000, 20000, 0)
    MoveCamera(305, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 21000, -6000, 20000, 270)
    SetChrPos(0x104, 20500, -6000, 21500, 225)
    SetChrPos(0x105, 20500, -6000, 18500, 315)
    FadeToBright(1000, 0)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#12504F#12P*phew*, that should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12800F#11PYeah, not bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12902F#6PWell done, well done.\x02\x03",
            "#12909FWell then, I guess\x01",
            "I'll take a break.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 58)
    WaitChrThread(0x105, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12506F#12PNow look here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#11PIt seems there's someone who\x01",
            "fools around more than even me...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xE, 0x80)
    Sound(3042, 255, 80, 0)

    NpcTalk(
        0xE,
        "KeA's Voice",
        "#10ALloyd!\x02",
    )

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#12502F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12802F#11POh, they're here!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(17000, -5000, -2500, 0)
    MoveCamera(238, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(15000, 6000)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0xC, 0x8)
    BeginChrThread(0xE, 3, 0, 60)
    BeginChrThread(0xA, 3, 0, 61)
    BeginChrThread(0xB, 3, 0, 62)
    BeginChrThread(0xC, 3, 0, 64)
    WaitChrThread(0xE, 3)
    Sound(3033, 255, 100, 0)
    Sleep(1300)
    OP_63(0xE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#13209F#11PAmazing!\x01",
            "It's pure white!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        (
            "#12705F#11PIndeed...\x01",
            "How surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602F#11PThat Bell... Just when did\x01",
            "she make something like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#13109F#6PC'mon bis sis!\x01",
            "Hurry up, hurry!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16000, -5000, -2500, 4000)

    def lambda_106F0():

        label("loc_106F0")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_106F0")

    QueueWorkItem2(0xE, 2, lambda_106F0)

    def lambda_10702():

        label("loc_10702")

        TurnDirection(0xFE, 0x12, 400)
        Yield()
        Jump("loc_10702")

    QueueWorkItem2(0xA, 2, lambda_10702)

    def lambda_10714():

        label("loc_10714")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_10714")

    QueueWorkItem2(0xB, 2, lambda_10714)

    def lambda_10726():

        label("loc_10726")

        TurnDirection(0xFE, 0x12, 600)
        Yield()
        Jump("loc_10726")

    QueueWorkItem2(0xC, 2, lambda_10726)
    BeginChrThread(0x12, 3, 0, 63)
    WaitChrThread(0x12, 3)
    TurnDirection(0x12, 0xC, 500)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)

    ChrTalk(
        0x12,
        (
            "#13012F#5POh, Fran. The beach isn't\x01",
            "going anywhere you know.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18000, 3500)
    BeginChrThread(0xC, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 69)
    Sleep(80)
    BeginChrThread(0x12, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 69)
    OP_6F(0x79)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0xC, 0x3)
    Fade(500)
    OP_68(18450, -5000, 18500, 0)
    MoveCamera(230, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0xE, 19430, -6000, 8270, 15)
    SetChrPos(0xA, 18930, -6000, 7270, 15)
    SetChrPos(0xB, 19930, -6000, 7270, 15)
    SetChrPos(0x12, 18430, -6000, 6270, 15)
    SetChrPos(0xC, 17930, -6000, 7270, 15)
    SetChrPos(0x101, 21000, -6000, 18500, 180)
    SetChrPos(0x104, 19750, -6000, 18250, 180)
    SetChrPos(0x105, 18450, -6000, 18500, 90)
    SetChrSubChip(0x105, 0x10)
    OP_68(21000, -5000, 16750, 6000)
    MoveCamera(230, 24, 0, 6000)
    SetCameraDistance(17500, 6000)
    OP_0D()
    BeginChrThread(0x105, 3, 0, 59)

    def lambda_108D4():
        OP_9B(0x0, 0xE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_108D4)
    Sleep(50)

    def lambda_108EC():
        OP_9B(0x0, 0xC, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_108EC)
    Sleep(50)

    def lambda_10904():
        OP_9B(0x0, 0xA, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10904)
    Sleep(50)

    def lambda_1091C():
        OP_9B(0x0, 0xB, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1091C)
    Sleep(50)

    def lambda_10934():
        OP_9B(0x0, 0x12, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_10934)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x12, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x12, 0x0, 0x0)
    OP_93(0xC, 0x0, 0x0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(21000, -5500, 15000, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    SetChrPos(0x101, 21000, -6000, 19500, 180)
    SetChrPos(0x104, 19750, -6000, 19250, 180)
    SetChrPos(0x105, 18100, -6000, 18550, 90)
    SetChrSubChip(0x105, 0x4)
    Sleep(1500)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xE,
        "#3613V#30WEhehe, sorry for the wait.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE1D)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13000.itp")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "#3395V#30W*giggle*, you even got the\x01",
            "parasols ready for us?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD43)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xB,
        "#2677V#30WHow really thoughtful.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    OP_24(0xA75)
    OP_93(0xC, 0x87, 0x1F4)
    OP_98(0xC, 0x64, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_10CA1():
        OP_98(0xFE, 0xFFFFFF9C, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10CA1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_10CD0():
        OP_98(0xFE, 0xFFFFFF6A, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_10CD0)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x12, 1)
    OP_64(0x12)
    Sleep(200)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xC,
        (
            "#2716V#40WC'mon big sis! You\x01",
            "#30Wgotta get yourself\x01",
            "out there!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA9C)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x12,
        (
            "#3516V#30WH-Hey! Don't\x01",
            "push so hard!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDBC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(20500, -4800, 16750, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 21000, -6000, 18500, 180)
    SetChrPos(0x104, 19750, -6000, 18250, 180)
    SetChrPos(0x105, 18450, -6000, 17900, 90)
    SetChrSubChip(0x105, 0xC)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#12505F#11P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2757, 255, 70, 0)
    Sleep(600)

    ChrTalk(
        0x104,
        (
            "#12809F#11PHoh hoh!\x01",
            "Not bad, not bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12902F#11PEeh, you all look great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12609F#6PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12706F#6PI am not too confident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13109F#5PEhehe, Mr. Lloyd.\x02\x03",
            "Who looks the best\x01",
            "in her swimsuit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12511F#11PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13001F#6PGeez Fran, quit\x01",
            "embarrassing him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12902F#5PHu hu, what's wrong? \x01",
            "You've been staring for awhile.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#12809F#5PHa ha ha, too much\x01",
            "excitement for ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#11PHa ha... Yeah,\x01",
            "it's a bit tempting.\x02\x03",
            "#12502F#11P──You all look so good...\x01",
            "I'm speechless.\x02\x03",
            "#12509FYou could even be in a\x01",
            "photo shoot or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#13209F#6PEhehe, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12612F#6PL-Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13014F#6PW-Whaaa...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#13106F#5PHmph, that's Mr. Lloyd for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12711F#6P...Definitely lacking tact.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12505F#11PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12806F#5P(This guy... He'll bring ruin\x01",
            "upon himself one day.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12902F#5P(Well, that's how men are, too.)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Woman's Voice",
        "Yoohoo! Sorry for the wait.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(17000, -5000, -2500, 0)
    MoveCamera(238, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(15000, 6000)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xF, 0x8)
    BeginChrThread(0x10, 3, 0, 65)
    BeginChrThread(0x8, 3, 0, 66)
    BeginChrThread(0x9, 3, 0, 67)
    BeginChrThread(0xF, 3, 0, 68)
    WaitChrThread(0x10, 3)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 3)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10,
        "#13405F#11PWoah! This is incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#13309F#11PUh uh... It is like\x01",
            "heaven on earth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PThe sand is pure white...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#13605F#11P...Wow...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    BeginChrThread(0x10, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 69)
    OP_6F(0x79)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xF, 0x3)
    Fade(500)
    OP_68(21000, -5000, 18500, 0)
    MoveCamera(230, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x10, 21500, -6000, 10500, 0)
    SetChrPos(0x8, 20500, -6000, 10000, 0)
    SetChrPos(0x9, 21000, -6000, 8500, 0)
    SetChrPos(0xF, 20000, -6000, 8000, 0)
    OP_93(0xE, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    SetChrPos(0x105, 18450, -6000, 18500, 90)
    SetChrSubChip(0x105, 0x14)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(21000, -5000, 17000, 4000)
    MoveCamera(230, 24, 0, 4000)

    def lambda_116EC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_116EC)

    def lambda_11701():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11701)

    def lambda_11716():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11716)

    def lambda_1172B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1172B)

    def lambda_11740():

        label("loc_11740")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_11740")

    QueueWorkItem2(0xE, 2, lambda_11740)

    def lambda_11752():

        label("loc_11752")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_11752")

    QueueWorkItem2(0xA, 2, lambda_11752)

    def lambda_11764():

        label("loc_11764")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_11764")

    QueueWorkItem2(0xB, 2, lambda_11764)

    def lambda_11776():

        label("loc_11776")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11776")

    QueueWorkItem2(0x12, 2, lambda_11776)

    def lambda_11788():

        label("loc_11788")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11788")

    QueueWorkItem2(0xC, 2, lambda_11788)
    BeginChrThread(0xE, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 72)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 71)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xF, 1)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(21000, -5200, 15500, 0)
    MoveCamera(180, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 2000)
    SetChrPos(0x101, 21000, -6000, 19500, 180)
    SetChrPos(0x104, 19750, -6000, 19250, 180)
    SetChrPos(0x105, 18100, -6000, 18550, 90)
    SetChrSubChip(0x105, 0x4)
    OP_93(0xE, 0x13B, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0x12, 0x2D, 0x0)
    OP_93(0xC, 0x2D, 0x0)
    Sleep(1500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        "Uh uh, sorry for the wait.\x02",
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
        0x10,
        (
            "Oh, surrounded by\x01",
            "cuties already, I see.\x02",
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
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        (
            "#3245V#30WAh, you got the parasols\x01",
            "and other things ready for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCAD)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xF,
        (
            "...I would've done it\x01",
            "if you asked, y'know.\x02",
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
    Sound(822, 0, 100, 0)
    OP_63(0x10, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x9, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12505F#6P#N#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#12807F#12P#N#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        "#13205F#5PHuuuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12606F#5P...S-Somehow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13012F#11P#NPretty... Or maybe...\x01",
            "Overwhelming?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#12706F#5PLike they have a different aura...\x01",
            "It is that sort of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#13101F#11PA-Amazing...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13402F#6PYou girls are looking\x01",
            "pretty good yourselves.\x02\x03",
            "#13409FYes, yes, I approve㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#13304F#12PUh uh, I agree.\x02\x03",
            "#13302FElie too, you are as\x01",
            "glamorous as I thought.\x02\x03",
            "#13309FAnd Tio and KeA, I want\x01",
            "to hug you both㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12609F#5PA-Ahaha...\x01",
            "(Look who's talking, Miss Cecil.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#5PEhehe, really?\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#13509F#11PUh uh... But this really\x01",
            "is a beautiful beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13604F#11PWell, not too shabby I guess...\x02\x03",
            "#13601F──Hey guys! How long are you gonna\x01",
            "stand there and stare for!?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x10)
    OP_64(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11EE1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_11EE1)

    def lambda_11EEE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11EEE)

    def lambda_11EFB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11EFB)

    def lambda_11F08():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_11F08)

    def lambda_11F15():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11F15)

    def lambda_11F22():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11F22)

    def lambda_11F2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11F2F)
    WaitChrThread(0xE, 2)
    Sleep(50)
    WaitChrThread(0xA, 2)
    Sleep(50)
    WaitChrThread(0xB, 2)
    Sleep(50)
    WaitChrThread(0x12, 2)
    Sleep(50)
    WaitChrThread(0xC, 2)
    Sleep(50)
    WaitChrThread(0x10, 2)
    Sleep(50)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12511F#6P#NHah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12806F#12P#NWhoa, careful. A moment longer and\x01",
            "you would've gone to the other world.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#12711F#5PMen are so simple minded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#12PWell, compared to women,\x01",
            "men are simple creatures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13106F#11PHmm... We're gonna\x01",
            "lose at this rate.\x02\x03",
            "#13101FLet's do our best, big sis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13012F#5P#ND-Don't be ridiculous.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then, after some warm-up exercises, each\x01",
            "of them enjoyed the beach in their own way...\x02\x03",
            "Lloyd, together with Rixia,\x01",
            "gave KeA and Sully\x01",
            "swimming lessons.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x8000)
    OP_4C(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 0, 0, 0, 0)
    ClearChrFlags(0xC, 0x8000)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, 0, 0, 0, 0)
    ClearChrFlags(0x10, 0x8000)
    OP_4C(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    OP_4C(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, 0, 0, 0, 0)
    ClearChrFlags(0xB, 0x8000)
    OP_4C(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x8000)
    OP_4C(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xF, 0x40)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x28)
    OP_CC(0x1, 0xFF, 0x0)

    label("loc_12341")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1265F")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12490")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)
    Jump("loc_124EF")

    label("loc_12490")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_124EF")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12556")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_1258E")

    label("loc_12556")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_1258E")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_125DF")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_12649")

    label("loc_125DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_1261B")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_12649")

    label("loc_1261B")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_12649")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_1265F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_126BE")
    ClearChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x7)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x7)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 31510, -6050, 7720, 180)
    SetChrFlags(0xC, 0x2)
    SetChrPos(0xC, 32049, -6100, 5840, 90)
    SetChrPos(0xD, 32870, -6180, 10310, 180)

    label("loc_126BE")

    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12714")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)

    label("loc_12714")

    LoadChrToIndex("apl/ch51305.itc", 0x1E)
    LoadChrToIndex("apl/ch51307.itc", 0x1F)
    LoadChrToIndex("apl/ch51306.itc", 0x20)
    LoadChrToIndex("apl/ch51309.itc", 0x21)
    LoadChrToIndex("apl/ch51308.itc", 0x22)
    LoadChrToIndex("apl/ch51310.itc", 0x23)
    LoadChrToIndex("chr/ch16000.itc", 0x24)
    LoadEffect(0x0, "eff\\step04.eff")
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0xE, 0, 0, 73)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x1)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 75)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    OP_90(0x101, 59000, 0, 27000, 0)
    OP_90(0x9, 57500, 0, 27000, 0)
    OP_90(0xE, 59000, -7250, 28000, 180)
    OP_90(0xF, 57500, -7250, 28000, 180)
    OP_68(58250, -5500, 27000, 0)
    OP_68(58250, -6500, 27000, 4000)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayBGM("ed7161", 0)
    Sound(988, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12502F#5POh, that's really good, KeA.\x02\x03",
            "#12509FJust keep going like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209F#12PEhehe, really?\x02\x03",
            "#13201FAh... \x01",
            "I think I get it.\x02\x03",
            "#13210FLet go of my hands, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PY-You're sure?\x02\x03",
            "#12501FOk then──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_12987():

        label("loc_12987")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_12987")

    QueueWorkItem2(0x101, 2, lambda_12987)
    EndChrThread(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    Sound(989, 2, 80, 0)
    OP_25(0x3DC, 0x3C)
    Sound(3034, 255, 100, 0)
    BeginChrThread(0xE, 0, 0, 74)
    BeginChrThread(0xE, 3, 0, 77)
    OP_0D()

    ChrTalk(
        0x9,
        "#13505F#11PMy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#5PWhoa!\x02\x03",
            "#12502FKeA, you've swum\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13200F#12P#NHmm, I don't know.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13605F#11PN-Not bad, shorty...\x02\x03",
            "#13607FTeach me the trick too,\x01",
            "sis Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#5PUh uh. Sure, sure.\x02\x03",
            "#13502FHmm, you're relying too\x01",
            "much on your upper body...\x02",
        )
    )

    CloseMessageWindow()
    StopSound(988, 2000, 50)
    StopSound(989, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 78)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)

    def lambda_12B2A():

        label("loc_12B2A")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_12B2A")

    QueueWorkItem2(0x9, 2, lambda_12B2A)
    EndChrThread(0xF, 0x0)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 76)
    BeginChrThread(0xF, 3, 0, 79)
    Sleep(1000)
    OP_68(58250, -6500, 29000, 0)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    Sound(989, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12509F#5PYou girls are\x01",
            "fast learners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13204F#12P#NEhehe.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13612F#11P#NH-Hmph.\x02\x03",
            "There's no meaning in\x01",
            "being able to do this...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#13210F#12P#NHey, hey Sully!\x02\x03",
            "Let's swim out to that rock!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#13611F#11P#NW-Why do I have to...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12509F#5PHa ha, be careful.\x02\x03",
            "#12500FDon't go past that rock.\x01",
            "That goes for both of you, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12P#NRoger!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13607F#11P#NOh, fine! \x01",
            "I'll go with you, alright.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(225, 20, 0, 5000)
    SetCameraDistance(13000, 5000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D88")
    Sleep(1)
    Jump("loc_12D71")

    label("loc_12D88")

    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xE, 64510, -7460, 28680, 75)
    SetChrPos(0xF, 62580, -7430, 29030, 75)

    def lambda_12DCE():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_12DCE)

    def lambda_12DE3():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_12DE3)
    OP_68(62940, -4600, 28510, 0)
    OP_68(62940, -3600, 28510, 4000)
    MoveCamera(75, 5, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    Sleep(2500)
    StopSound(989, 2000, 70)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(58250, -6500, 27000, 0)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x9, 0x8)
    OP_0D()

    ChrTalk(
        0x101,
        "#12512F#11PHmm. Will they be all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PUh uh, it's pretty shallow\x01",
            "all around here, so they'll\x01",
            "be fine either way.\x02\x03",
            "#13502FBut KeA...\x01",
            "She's amazing.\x02\x03",
            "It looked like she got the\x01",
            "hang of it in an instant.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12504F#6PMaybe her body\x01",
            "remembers how to\x01",
            "swim from before.\x02\x03",
            "#12500FSully's pretty amazing too.\x02\x03",
            "She said she's never once\x01",
            "gone swimming before now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13504F#11PLately she's been training\x01",
            "explosiveness and\x01",
            "flexibility in practice.\x02\x03",
            "#13502FYou just have to show her\x01",
            "once and she gets it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PI see... Looks like she's\x01",
            "working hard, then.\x02\x03",
            "#12505FThat's right... I heard\x01",
            "Arc-en-ciel's performance\x01",
            "is being updated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13505F#11PYes, well it's still\x01",
            "the same "Golden Sun,\x01",
            "Silver Moon."\x02\x03",
            "#13502FBut we've arranged it\x01",
            "so Sully will appear\x01",
            "as a third "princess."\x02\x03",
            "#13509FShe's been added to all\x01",
            "of the main scenes.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13328")

    ChrTalk(
        0x101,
        (
            "#12511F#6PThat's amazing...\x02\x03",
            "#12512FI can't believe she's\x01",
            "getting such a major role\x01",
            "this soon after we met her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PUh uh, so do I.\x02\x03",
            "#13510FIt's probably because of\x01",
            "Miss Ilya's guidance and\x01",
            "Sully's own tenacity.\x02\x03",
            "#13508FMaybe more that even my own, this whole time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1346B")

    label("loc_13328")


    ChrTalk(
        0x101,
        (
            "#12505F#6PThat's amazing...\x02\x03",
            "#12501FWasn't she resenting Miss\x01",
            "Ilya at first and tried to\x01",
            "cause an incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13504F#11PIt wasn't something exaggerated \x01",
            "like an incident, but...\x02\x03",
            "#13510FIt's probably because of\x01",
            "Miss Ilya's guidance and\x01",
            "Sully's own tenacity.\x02\x03",
            "#13508FMaybe more that even my own, this whole time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1346B")


    ChrTalk(
        0x101,
        "#12505F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#13509F#11PAhaha, it's no big deal.\x02\x03",
            "#13510FUmm, I'm a bit tired, so\x01",
            "I'll go rest over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PI see. Nice work.\x02\x03",
            "#12500FWe still have plenty of time left, \x01",
            "so let's enjoy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PRight...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57250, -5600, 29000, 6000)
    MoveCamera(235, 10, 0, 6000)
    SetCameraDistance(13500, 6000)
    OP_93(0x9, 0x10E, 0x1F4)

    def lambda_135B2():
        OP_9B(0x0, 0xFE, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_135B2)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12503F#6P(Hmm. Even though she's\x01",
            "not so tall, she's so...)\x02\x03",
            "#12511F(──No, stop!)\x02\x03",
            "#12500F(There's a lot of time until noon.\x01",
            "I should check in with everyone.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x8000)
    OP_4C(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    OP_4C(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_137E2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x2)
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    ClearChrFlags(0xC, 0x2)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_137E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_137F7")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_137F7")

    OP_90(0x0, 40000, 0, 17000, 270)
    SetScenarioFlags(0x145, 0)
    OP_29(0xA5, 0x1, 0x3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_57_FAD1 end

    def Function_58_1381E(): pass

    label("Function_58_1381E")

    OP_68(17500, -5000, 20000, 2000)
    OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x4B0, 0x7D0, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(500)
    Sound(318, 0, 40, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 18450, -6000, 17900, 90)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x28)
    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x5, 0xC, 0xB, 0xA, 0x9, 0x8)
    Sound(811, 0, 20, 0)
    OP_0D()
    Return()

    # Function_58_1381E end

    def Function_59_138AD(): pass

    label("Function_59_138AD")

    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x546, 0x5, 0x10, 0x11, 0x12, 0x13, 0x14)
    Sound(318, 0, 40, 0)
    Return()

    # Function_59_138AD end

    def Function_60_138C5(): pass

    label("Function_60_138C5")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_60_138C5 end

    def Function_61_138F0(): pass

    label("Function_61_138F0")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_61_138F0 end

    def Function_62_1391B(): pass

    label("Function_62_1391B")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6000, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_62_1391B end

    def Function_63_13946(): pass

    label("Function_63_13946")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_63_13946 end

    def Function_64_13971(): pass

    label("Function_64_13971")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4500, 0, -1500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_13971 end

    def Function_65_1399C(): pass

    label("Function_65_1399C")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_65_1399C end

    def Function_66_139C7(): pass

    label("Function_66_139C7")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_139C7 end

    def Function_67_139F2(): pass

    label("Function_67_139F2")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 5500, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_67_139F2 end

    def Function_68_13A1D(): pass

    label("Function_68_13A1D")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_13A1D end

    def Function_69_13A48(): pass

    label("Function_69_13A48")

    OP_93(0xFE, 0xF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_69_13A48 end

    def Function_70_13A5F(): pass

    label("Function_70_13A5F")

    OP_98(0xFE, 0x4B0, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_70_13A5F end

    def Function_71_13A74(): pass

    label("Function_71_13A74")

    OP_98(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_71_13A74 end

    def Function_72_13A89(): pass

    label("Function_72_13A89")

    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_72_13A89 end

    def Function_73_13A9E(): pass

    label("Function_73_13A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B7D")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    Jump("Function_73_13A9E")

    label("loc_13B7D")

    Return()

    # Function_73_13A9E end

    def Function_74_13B7E(): pass

    label("Function_74_13B7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13C60")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    Sleep(200)
    Jump("Function_74_13B7E")

    label("loc_13C60")

    Return()

    # Function_74_13B7E end

    def Function_75_13C61(): pass

    label("Function_75_13C61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D40")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    Jump("Function_75_13C61")

    label("loc_13D40")

    Return()

    # Function_75_13C61 end

    def Function_76_13D41(): pass

    label("Function_76_13D41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E23")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    Sleep(200)
    Jump("Function_76_13D41")

    label("loc_13E23")

    Return()

    # Function_76_13D41 end

    def Function_77_13E24(): pass

    label("Function_77_13E24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E87")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60080, -6950, 27560)
    OP_9F(0x1, 61500, -6850, 28810)
    OP_9F(0x1, 60190, -7050, 30310)
    OP_9F(0x1, 58950, -7150, 29090)
    OP_9F(0x1, 59200, -7250, 28000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("Function_77_13E24")

    label("loc_13E87")

    Return()

    # Function_77_13E24 end

    def Function_78_13E88(): pass

    label("Function_78_13E88")

    SetChrPos(0xFE, 58250, -6850, 29000, 0)

    label("loc_13E99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF2")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60250, -6750, 31000)
    OP_9F(0x1, 58250, -7200, 33000)
    OP_9F(0x1, 56250, -7250, 31000)
    OP_9F(0x1, 58250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("loc_13E99")

    label("loc_13EF2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Return()

    # Function_78_13E88 end

    def Function_79_13F18(): pass

    label("Function_79_13F18")

    SetChrPos(0xFE, 58250, -6950, 30000, 0)

    label("loc_13F29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13F82")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 59250, -6950, 31000)
    OP_9F(0x1, 58250, -7250, 32000)
    OP_9F(0x1, 57250, -7250, 31000)
    OP_9F(0x1, 58250, -6950, 30000)
    OP_9F(0x2, 0xFE, 1000, 0x6)
    Jump("loc_13F29")

    label("loc_13F82")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6950, 30000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_79_13F18 end

    def Function_80_13FA8(): pass

    label("Function_80_13FA8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(18000, -4400, 0, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 18000, -6000, 0, 90)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──And so, everyone had\x01",
            "a fun time at the beach.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and the others enjoyed\x01",
            "a watermelon splitting game together──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As they savored lunchboxes\x01",
            "delivered by the hotel, their\x01",
            "excitement began to build.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    StopSound(136, 1000, 100)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_80_13FA8 end

    def Function_81_14116(): pass

    label("Function_81_14116")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch41950.itc", 0x20)
    LoadChrToIndex("chr/ch41951.itc", 0x21)
    LoadChrToIndex("chr/ch42050.itc", 0x22)
    LoadChrToIndex("chr/ch42051.itc", 0x23)
    LoadChrToIndex("monster/ch82050.itc", 0x24)
    LoadChrToIndex("monster/ch82051.itc", 0x25)
    LoadChrToIndex("chr/ch41952.itc", 0x26)
    LoadChrToIndex("chr/ch00050.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch02950.itc", 0x2A)
    LoadChrToIndex("chr/ch03150.itc", 0x2B)
    LoadChrToIndex("chr/ch03250.itc", 0x2C)
    LoadEffect(0x0, "battle/btgun00.eff")
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    OP_90(0x101, 39900, -6010, 30100, 270)
    OP_90(0x103, 41000, -6000, 30950, 270)
    OP_90(0x104, 40730, -6000, 29440, 270)
    OP_90(0x106, 41890, -6070, 28860, 270)
    OP_90(0x109, 42050, -6090, 29980, 270)
    OP_90(0x105, 42230, -6120, 31120, 270)
    OP_90(0xD, 40800, -3000, 32000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x17, 0x20)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x8)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x4)
    ClearChrFlags(0x1F, 0x4)
    OP_90(0x17, 9500, 1000, 2700, 90)
    OP_90(0x18, 6600, 1000, -3650, 90)
    OP_90(0x19, 3100, 1000, 3350, 90)
    OP_90(0x1D, 8550, 1000, -1650, 90)
    OP_90(0x1E, 6700, 1000, 1600, 90)
    OP_90(0x1F, 2900, 1000, -1850, 90)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x2, 0x15)
    OP_49()
    SetChrPos(0x15, 45000, 20000, 30000, 270)
    OP_D5(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x1, 0x78, 0x0, 0x20)
    OP_75(0x2, 0x1, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x3, 0x16)
    OP_49()
    SetChrPos(0x16, 45000, 20000, 30000, 270)
    OP_D5(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0xD, 0x8)
    OP_68(45000, 2500, 30000, 0)
    MoveCamera(315, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_68(45000, -500, 30000, 7000)
    MoveCamera(305, 40, 0, 7000)
    BeginChrThread(0x15, 3, 0, 82)
    BeginChrThread(0x16, 3, 0, 83)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x15, 0x3)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0xD, 0x8)
    OP_68(35000, -4500, 30000, 0)
    MoveCamera(60, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_68(31000, -4500, 30000, 5000)
    MoveCamera(45, 10, 0, 5000)
    BeginChrThread(0x15, 3, 0, 84)
    BeginChrThread(0x16, 3, 0, 85)

    def lambda_1454B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1454B)
    Sleep(30)

    def lambda_14563():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14563)
    Sleep(30)

    def lambda_1457B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1457B)
    Sleep(30)

    def lambda_14593():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14593)
    Sleep(30)

    def lambda_145AB():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_145AB)
    Sleep(30)

    def lambda_145C3():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_145C3)
    Sleep(30)

    def lambda_145DB():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_145DB)
    StopSound(497, 4000, 90)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    SetMapObjFlags(0x2, 0x4)
    SetChrFlags(0x15, 0x80)
    SetMapObjFlags(0x3, 0x4)
    SetChrFlags(0x16, 0x80)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(31000, -5000, 30000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    OP_0D()
    OP_68(31000, -5000, 31500, 1200)
    OP_93(0xD, 0xB4, 0x1C2)
    OP_6F(0x79)

    NpcTalk(
        0xD,
        "Divine Wolf Zeit",
        (
            "#01203F#3C#5PWell then, I'll go rampage as much\x01",
            "as possible in the theme park area.\x02\x03",
            "#01200FGoing back to my original form will be\x01",
            "the signal, so you'll take advantage of\x01",
            "that chance and head to the mansion.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14767():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14767)
    Sleep(50)

    def lambda_14777():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14777)
    Sleep(50)

    def lambda_14787():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14787)
    Sleep(50)

    def lambda_14797():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14797)
    Sleep(50)

    def lambda_147A7():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_147A7)
    Sleep(50)

    def lambda_147B7():
        TurnDirection(0x106, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_147B7)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#00013F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PZeit...\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Divine Wolf Zeit",
        (
            "#01200F#3C#5PHu hu, you too.\x02\x03",
            "#01203FMay Aidios be with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(31000, -4200, 32000, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11500, 0)
    OP_68(31000, 2100, 42000, 3000)
    MoveCamera(40, 5, 0, 3000)

    def lambda_148C7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_148C7)

    def lambda_148D4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_148D4)

    def lambda_148E1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_148E1)

    def lambda_148EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_148EE)

    def lambda_148FB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_148FB)

    def lambda_14908():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_14908)
    BeginChrThread(0xD, 3, 0, 89)
    WaitChrThread(0xD, 3)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()
    Fade(1000)
    OP_68(31000, -4800, 30000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x105,
        "#10409F#11PHa ha, how reliable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PAlright, first of all, we'll\x01",
            "go to the hotel's arcad──\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1E, 0x8)
    ClearChrFlags(0x1F, 0x8)
    StopBGM(0xBB8)

    NpcTalk(
        0x17,
        "Man's Voice",
        "#2S#2PThey they're...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man's Voice",
        "#2S#2PIt's Bannings and the others!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_14AFD():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14AFD)
    Sleep(50)

    def lambda_14B0D():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14B0D)
    Sleep(50)

    def lambda_14B1D():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14B1D)
    Sleep(50)

    def lambda_14B2D():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14B2D)
    Sleep(50)

    def lambda_14B3D():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14B3D)
    Sleep(50)

    def lambda_14B4D():
        OP_93(0x106, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_14B4D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    ReplaceBGM("ed7251", "ed7540")
    ReplaceBGM("ed7565", "ed7540")
    Fade(1000)
    OP_68(18000, -2500, 5000, 0)
    OP_68(18000, -5000, 5000, 6000)
    MoveCamera(240, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16000, 0)
    BeginChrThread(0x17, 3, 0, 90)
    BeginChrThread(0x18, 3, 0, 91)
    BeginChrThread(0x19, 3, 0, 92)
    BeginChrThread(0x1D, 3, 0, 95)
    BeginChrThread(0x1E, 3, 0, 96)
    BeginChrThread(0x1F, 3, 0, 97)
    BeginChrThread(0x2A, 1, 0, 98)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1D, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x1F, 3)
    EndChrThread(0x2A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(31000, -5200, 30000, 0)
    MoveCamera(340, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00310F#11PTch...\x01",
            "Already here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#11PEnemies: 3 jaegers and 3 military monsters!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#12PThey look pretty\x01",
            "powerful......!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00007F#11PReady to intercept them!\x01",
            "We'll crush them cooperating!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(11000, 0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2A)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2B)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x2C)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00307F#1K#1P#NRight!\x02",
    )


    ChrTalk(
        0x105,
        "#10407F#1K#2P#NYeah!\x02",
    )


    ChrTalk(
        0x109,
        "#10107F#1K#4P#NRoger!\x02",
    )


    NpcTalk(
        0x101,
        "Rixia",
        "#10707F#1K#3P#NYes...!\x02",
    )

    SetMessageWindowPos(180, 70, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201F#1K#NYes!\x02",
    )

    Sound(2249, 255, 100, 0)
    Sound(2343, 255, 100, 1)
    Sound(2417, 255, 100, 2)
    Sound(2478, 255, 100, 3)
    Sound(3174, 255, 100, 4)
    OP_57(0x1)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(29800, -5000, 27200, 0)
    MoveCamera(210, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    SetCameraDistance(10000, 1000)

    def lambda_14E86():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_14E86)

    def lambda_14E9B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_14E9B)

    def lambda_14EB0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_14EB0)

    def lambda_14EC5():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_14EC5)

    def lambda_14EDA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14EDA)

    def lambda_14EEF():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_14EEF)
    BeginChrThread(0x2A, 1, 0, 98)
    Sleep(500)
    BlurSwitch(0x15E, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x4)
    EndChrThread(0x2A, 0x1)
    OP_24(0x1F1)
    OP_24(0x3B6)
    Battle("BattleInfo_904", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 99)
    Return()

    # Function_81_14116 end

    def Function_82_14F82(): pass

    label("Function_82_14F82")

    BeginChrThread(0xFE, 0, 0, 86)
    OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_82_14F82 end

    def Function_83_14FA1(): pass

    label("Function_83_14FA1")


    def lambda_14FA6():
        OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14FA6)
    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    Sleep(1000)
    OP_75(0x2, 0x2, 0x0)
    OP_79(0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_14FA1 end

    def Function_84_15001(): pass

    label("Function_84_15001")

    BeginChrThread(0xFE, 0, 0, 87)
    OP_75(0x2, 0x2, 0x0)
    SetChrPos(0xFE, 45000, -1000, 30000, 270)
    OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_84_15001 end

    def Function_85_15038(): pass

    label("Function_85_15038")

    SetChrPos(0xFE, 45000, -1000, 30000, 270)

    def lambda_1504E():
        OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1504E)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    OP_75(0x2, 0x1, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_15038 end

    def Function_86_150B2(): pass

    label("Function_86_150B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_150D6")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_86_150B2")

    label("loc_150D6")

    Return()

    # Function_86_150B2 end

    def Function_87_150D7(): pass

    label("Function_87_150D7")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_87_150D7 end

    def Function_88_1513C(): pass

    label("Function_88_1513C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15157")
    OP_A1(0xFE, 0xBB8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_88_1513C")

    label("loc_15157")

    Return()

    # Function_88_1513C end

    def Function_89_15158(): pass

    label("Function_89_15158")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 70, 0)
    OP_9D(0xFE, 0x7918, 0xFFFFF8F8, 0xA410, 0x1388, 0x1B58)
    SetChrFlags(0xFE, 0x1)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 70, 0)
    OP_9D(0xFE, 0x7918, 0x8FC, 0xD2F0, 0x157C, 0x1770)
    SetChrFlags(0xFE, 0x1)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x32C8, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_89_15158 end

    def Function_90_15249(): pass

    label("Function_90_15249")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x1B58, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_90_15249 end

    def Function_91_15368(): pass

    label("Function_91_15368")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5DC0, 0x1388, 0x0)
    Return()

    # Function_91_15368 end

    def Function_92_1538F(): pass

    label("Function_92_1538F")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x4844, 0x1388, 0x0)
    Return()

    # Function_92_1538F end

    def Function_93_153B6(): pass

    label("Function_93_153B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_153D4")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_93_153B6")

    label("loc_153D4")

    Return()

    # Function_93_153B6 end

    def Function_94_153D5(): pass

    label("Function_94_153D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_153F3")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_94_153D5")

    label("loc_153F3")

    Return()

    # Function_94_153D5 end

    def Function_95_153F4(): pass

    label("Function_95_153F4")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x57E4, 0x1388, 0x0)
    Return()

    # Function_95_153F4 end

    def Function_96_1542C(): pass

    label("Function_96_1542C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5208, 0x1388, 0x0)
    Return()

    # Function_96_1542C end

    def Function_97_15464(): pass

    label("Function_97_15464")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x55F0, 0x1388, 0x0)
    Return()

    # Function_97_15464 end

    def Function_98_1549C(): pass

    label("Function_98_1549C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_154B5")
    Sound(845, 0, 60, 0)
    Sleep(400)
    Jump("Function_98_1549C")

    label("loc_154B5")

    Return()

    # Function_98_1549C end

    def Function_99_154B6(): pass

    label("Function_99_154B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 29900, 0, 30100, 225)
    OP_90(0x103, 31000, 0, 30950, 225)
    OP_90(0x104, 30730, 0, 29440, 225)
    OP_90(0x106, 31890, 0, 28860, 225)
    OP_90(0x109, 32049, 0, 29980, 225)
    OP_90(0x105, 32229, 0, 31120, 225)
    Call(0, 100)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_68(28170, -5200, 26570, 0)
    MoveCamera(270, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_68(29230, -5200, 27630, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00010F#11PKh...\x01",
            "They really are strong...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PA bunch of elites!\x01",
            "We can only go full power here...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PLet's hurry...! Zeit's\x01",
            "diversion is beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11PYeah, to the arcade!\x02\x03",
            "The entire staff had\x01",
            "evacuated, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PYes, no need to worry to\x01",
            "involve them in fights!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PThen it seems we\x01",
            "can go all out...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, 31290, -6030, 30470, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 4)
    OP_29(0xAF, 0x1, 0x12)
    OP_1B(0x0, 0x0, 0x65)
    SetMapObjFlags(0x0, 0x4)
    OP_65(0x0, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_99_154B6 end

    def Function_100_15808(): pass

    label("Function_100_15808")

    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x40)
    ClearChrFlags(0x17, 0x1)
    SetChrPos(0x17, 29420, -6000, 23550, 270)
    SetChrChipByIndex(0x18, 0xB)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x1)
    SetChrPos(0x18, 26080, -6000, 26400, 315)
    SetChrChipByIndex(0x19, 0xB)
    SetChrSubChip(0x19, 0x1)
    ClearChrFlags(0x19, 0x80)
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x40)
    ClearChrFlags(0x19, 0x1)
    SetChrPos(0x19, 28590, -6000, 26930, 180)
    Return()

    # Function_100_15808 end

    def Function_101_158A2(): pass

    label("Function_101_158A2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch41950.itc", 0x24)
    LoadChrToIndex("chr/ch41951.itc", 0x25)
    LoadChrToIndex("chr/ch41952.itc", 0x26)
    LoadChrToIndex("chr/ch42050.itc", 0x27)
    LoadChrToIndex("chr/ch42051.itc", 0x28)
    LoadChrToIndex("monster/ch82050.itc", 0x29)
    LoadChrToIndex("monster/ch82051.itc", 0x2A)
    LoadEffect(0x0, "battle/btgun00.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1D, 0, 0, 94)
    BeginChrThread(0x1E, 0, 0, 94)
    BeginChrThread(0x1F, 0, 0, 94)
    BeginChrThread(0x20, 0, 0, 94)
    SetChrPos(0x1A, -33000, -2000, 1300, 90)
    SetChrPos(0x1B, -38000, -2000, 0, 90)
    SetChrPos(0x1C, -28000, -2000, -1300, 90)
    SetChrPos(0x1D, -49500, -2000, 3000, 90)
    SetChrPos(0x1E, -47000, -2000, 1000, 90)
    SetChrPos(0x1F, -48500, -2000, -1000, 90)
    SetChrPos(0x20, -47000, -2000, -3000, 90)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x8)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x8)
    SetChrFlags(0x20, 0x8)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    OP_68(-13000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(12000, 1500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-25000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(12000, 6000)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x1C, 0x8)
    ClearChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1E, 0x8)
    ClearChrFlags(0x1F, 0x8)
    ClearChrFlags(0x20, 0x8)
    BeginChrThread(0x1A, 3, 0, 103)
    BeginChrThread(0x1B, 3, 0, 104)
    BeginChrThread(0x1C, 3, 0, 102)
    BeginChrThread(0x1D, 3, 0, 105)
    BeginChrThread(0x1E, 3, 0, 105)
    BeginChrThread(0x1F, 3, 0, 105)
    BeginChrThread(0x20, 3, 0, 105)
    BeginChrThread(0x2A, 1, 0, 98)
    WaitChrThread(0x1A, 3)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1D, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x1F, 3)
    WaitChrThread(0x20, 3)
    EndChrThread(0x2A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(-18000, -1000, 0, 0)
    OP_68(-14000, -1000, 0, 1500)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(11000, 1500)
    SetChrPos(0x1A, -24500, -2000, 1200, 90)
    SetChrPos(0x1B, -22500, -2000, 0, 90)
    SetChrPos(0x1C, -24000, -2000, -1100, 90)
    SetChrPos(0x1D, -29500, -2000, 3000, 90)
    SetChrPos(0x1E, -27000, -2000, 1300, 90)
    SetChrPos(0x1F, -28500, -2000, -1000, 90)
    SetChrPos(0x20, -27000, -2000, -3100, 90)

    def lambda_15D8C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_15D8C)

    def lambda_15DA1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_15DA1)

    def lambda_15DB6():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_15DB6)

    def lambda_15DCB():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_15DCB)

    def lambda_15DE0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_15DE0)

    def lambda_15DF5():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_15DF5)

    def lambda_15E0A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_15E0A)
    BeginChrThread(0x2A, 1, 0, 98)
    OP_0D()
    Fade(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x2A, 0x1)
    Battle("BattleInfo_9D0", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 106)
    Return()

    # Function_101_158A2 end

    def Function_102_15EB4(): pass

    label("Function_102_15EB4")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(150)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(150)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_102_15EB4 end

    def Function_103_16004(): pass

    label("Function_103_16004")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_103_16004 end

    def Function_104_160BB(): pass

    label("Function_104_160BB")

    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1770, 0x0)
    Return()

    # Function_104_160BB end

    def Function_105_160CB(): pass

    label("Function_105_160CB")

    OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x1770, 0x0)
    Return()

    # Function_105_160CB end

    def Function_106_160DB(): pass

    label("Function_106_160DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    Call(0, 107)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_68(-13000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12400, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(11400, 1500)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)
    Sound(913, 0, 60, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PThat's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PZeit's diversion!\x02",
    )

    CloseMessageWindow()
    StopSound(136, 500, 100)
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetScenarioFlags(0x22, 0)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_106_160DB end

    def Function_107_16353(): pass

    label("Function_107_16353")

    SetChrChipByIndex(0x1A, 0xB)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    OP_52(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1A, 0x1)
    SetChrPos(0x1A, -17580, -2000, -1910, 270)
    SetChrChipByIndex(0x1B, 0xB)
    SetChrSubChip(0x1B, 0x1)
    ClearChrFlags(0x1B, 0x80)
    OP_52(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1B, 0x1)
    SetChrPos(0x1B, -15910, -2000, 640, 315)
    SetChrChipByIndex(0x1C, 0xB)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    OP_52(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x1)
    SetChrPos(0x1C, -18880, -2000, 120, 180)
    Return()

    # Function_107_16353 end

    def Function_108_163ED(): pass

    label("Function_108_163ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    Call(0, 107)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    OP_68(-15000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_68(-13000, -1000, 0, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#10702F#11PIt seems that the fight has\x01",
            "started at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#5PAlright, let's take this chance\x01",
            "to pass through the arcade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12PYessir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    SetChrPos(0x0, -10140, -2000, 270, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 5)
    OP_29(0xAF, 0x1, 0x13)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_108_163ED end

    def Function_109_165D1(): pass

    label("Function_109_165D1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch15000.itc", 0x1E)
    LoadChrToIndex("chr/ch15700.itc", 0x1F)
    LoadChrToIndex("chr/ch15100.itc", 0x20)
    LoadChrToIndex("chr/ch15200.itc", 0x21)
    LoadChrToIndex("chr/ch15500.itc", 0x22)
    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87153.itc", 0x2E)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("apl/ch51352.itc", 0x2B)
    LoadChrToIndex("apl/ch51353.itc", 0x2C)
    LoadChrToIndex("apl/ch51354.itc", 0x2D)
    Call(0, 110)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_1663D")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_16657")

    label("loc_1663D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16651")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_16657")

    label("loc_16651")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_16657")

    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87050.itc", 0x26)
    LoadChrToIndex("monster/ch87250.itc", 0x27)
    LoadChrToIndex("monster/ch87350.itc", 0x28)
    LoadChrToIndex("monster/ch87450.itc", 0x29)
    LoadChrToIndex("monster/ch87550.itc", 0x2A)
    Call(0, 113)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16698")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_166B2")

    label("loc_16698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_166AC")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_166B2")

    label("loc_166AC")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_166B2")

    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Call(0, 126)
    Return()

    # Function_109_165D1 end

    def Function_110_166D4(): pass

    label("Function_110_166D4")

    OP_68(41670, -5400, 440, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9670, 0)
    LoadEffect(0x0, "eff\\mgm03_02.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    LoadEffect(0x2, "eff\\step04.eff")
    LoadEffect(0x3, "battle\\ms00053.eff")
    SoundLoad(989)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x153, 0x1F)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x153, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16775")
    SetChrChipByIndex(0xEF, 0x20)
    Jump("loc_1678B")

    label("loc_16775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16787")
    SetChrChipByIndex(0xEF, 0x21)
    Jump("loc_1678B")

    label("loc_16787")

    SetChrChipByIndex(0xEF, 0x22)

    label("loc_1678B")

    SetChrPos(0x101, 40230, -6910, 1770, 135)
    SetChrPos(0x153, 42190, -7020, 1260, 270)
    SetChrPos(0xEF, 40720, -6970, -210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#12503FWell then, let's begin our strategy.\x02\x03",
            "#12500FWe'll do like I explained earlier, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_169F0")

    ChrTalk(
        0x102,
        (
            "#6P#12600FYes, we'll play at the beach\x01",
            "and lure out the monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FAlright. I'm counting on you.\x02\x03",
            "#12503FAnyhow, the monster's\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#12601FYes, I know.\x02\x03",
            "#12603FI was surprised getting suddenly asked to\x01",
            "take out a monster that tears swimsuits, but...\x02\x03",
            "#12600FIt's also for Bell's sake,\x01",
            "so I'll cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGood luck, Lloyd, Elie!\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D9C")

    label("loc_169F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16BB9")

    ChrTalk(
        0x103,
        (
            "#6P#12700FYes, we'll play at the beach\x01",
            "and lure out the monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FAlright. I'm counting on you.\x02\x03",
            "#12503FAnyhow, the monster's\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#12700FYes, of course.\x02\x03",
            "#12703FI was surprised getting suddenly asked to\x01",
            "take out a monster that tears swimsuits, but...\x02\x03",
            "#12701FI cannot forgive such evil\x01",
            "deeds on Michey's home turf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGood luck, Lloyd, Tio!\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D9C")

    label("loc_16BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16D9C")

    ChrTalk(
        0x109,
        (
            "#6P#13000FYes, we'll play at the beach\x01",
            "and lure out the monster!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FAlright. I'm counting on you.\x02\x03",
            "#12503FAnyhow, the monster's\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#13000FYes, of course!\x02\x03",
            "#13003FI was surprised getting suddenly asked to\x01",
            "take out a monster that tears swimsuits, but...\x02\x03",
            "#13000FI'll do my best for the sake of everyone playing\x01",
            "at the beach too and exterminate it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGood luck, Lloyd, Noｱl!\x02",
    )

    CloseMessageWindow()

    label("loc_16D9C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(47130, -5780, 17350, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9650, 0)
    SetChrPos(0x101, 46390, -7080, 15860, 0)
    SetChrPos(0x153, 36870, -6410, 18860, 90)
    SetChrPos(0xEF, 46670, -7080, 19800, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 46670, -7080, 19800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(11, 0, 70, 0)

    ChrTalk(
        0x101,
        "#6P#12500FTake that!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16EEF")

    ChrTalk(
        0x102,
        "#12602FEek, geez, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12606F...*sigh*, still, no monster\x01",
            "is showing up, hm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FDF")

    label("loc_16EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16F69")

    ChrTalk(
        0x103,
        "#12702FMrr, now you've done it, eh?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#12706F...But I don't see any\x01",
            "monster or the likes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FDF")

    label("loc_16F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16FDF")

    ChrTalk(
        0x109,
        "#13002FKuuh, you did it, eh!\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x109,
        (
            "#13006F...*sigh*, still, no monster\x01",
            "is showing up at all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FDF")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#12505FYeah... I wonder if it\x01",
            "could be vigilant...\x02\x03",
            "#12503FBut I'm sure there's a monster around.\x01",
            "Let's keep watching the situation...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xB4, 0x1F4)
    Sleep(100)
    OP_97(0xEF, 0x0, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 46390, -7080, 16360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(11, 0, 70, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#12511FUgh!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17121")

    ChrTalk(
        0x102,
        "#12609F*giggle*, payback.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17173")

    label("loc_17121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17147")

    ChrTalk(
        0x103,
        "#12704F...Payback.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17173")

    label("loc_17147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17173")

    ChrTalk(
        0x109,
        "#13009FAhaha, that's payback!\x02",
    )

    CloseMessageWindow()

    label("loc_17173")


    ChrTalk(
        0x101,
        "#6P#12512FY-You got me...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_0D()
    OP_68(38460, -5480, 18640, 3000)
    MoveCamera(279, 17, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10180, 3000)
    OP_6F(0x79)
    OP_63(0x153, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#5P#13206F(Awww, KeA wants to\x01",
            "play with them, too.)\x02\x03",
            "#13208F(Lloyd said it's dangerous,\x01",
            "but it looks so fun...)\x02\x03",
            "#13205F(...Huh?)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrChipByIndex(0x24, 0x23)
    SetChrPos(0x24, 47570, -7100, 21350, 180)
    Fade(500)
    OP_68(47030, -5480, 17480, 0)
    MoveCamera(295, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10110, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_68(47500, -5480, 18810, 3000)
    MoveCamera(295, 40, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10110, 3000)
    Sleep(1000)
    Sound(989, 2, 60, 0)
    BeginChrThread(0x24, 3, 0, 112)
    OP_6F(0x79)

    ChrTalk(
        0x153,
        "#13205FAh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_1767C")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4SElie, behind you!!\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#12605FEh...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x2)
    SetChrPos(0x102, 46670, -7080, 19300, 180)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    Sound(3391, 255, 100, 0)

    ChrTalk(
        0x102,
        "#12615F#4S──Eeeeeek...!?!?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_175CA():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_175CA)
    Sleep(1000)

    def lambda_175E7():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_175E7)

    ChrTalk(
        0x101,
        "#6P#12511FE-Elie...!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x102,
        (
            "#12613FI-I'm fine...\x01",
            "Chase after the monster!!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_17CCA")

    label("loc_1767C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_179A1")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4STio, behind you!\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#12705FWhat...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x103, 0x2)
    SetChrPos(0x103, 46670, -7080, 19300, 180)
    Sound(2225, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x103,
        "#12710F#4S──Eek...!?!?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_178F3():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_178F3)
    Sleep(1000)

    def lambda_17910():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17910)

    ChrTalk(
        0x101,
        "#6P#12511FT-Tio!!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x103,
        (
            "#12701FI-I'm all right...\x01",
            "Hurry, the monster!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_17CCA")

    label("loc_179A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17CCA")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4SNoｱl, behind you!\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#13005FHuh...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x8)
    SetChrFlags(0x109, 0x2)
    SetChrPos(0x109, 46670, -7080, 19300, 180)
    Sound(3517, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x109,
        "#13014F#4S──Eeek...!?!?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_17C19():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17C19)
    Sleep(1000)

    def lambda_17C36():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17C36)

    ChrTalk(
        0x101,
        "#6P#12511FN-Noｱl...!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x109,
        (
            "#13006FI-I'm all right...\x01",
            "Go after the monster...!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x4, 0x3, 0x2)

    label("loc_17CCA")


    def lambda_17CCF():
        OP_95(0xFE, 34050, -6300, 8750, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17CCF)
    Sleep(100)

    def lambda_17CEC():
        OP_99(0xFE, 0xEF, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_17CEC)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(19420, -5480, -8710, 0)
    MoveCamera(246, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15040, 0)
    SetChrPos(0x101, 24590, -6010, -1280, 225)
    SetChrPos(0x24, 27950, -6000, -4240, 225)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17D85")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_17DA8")

    label("loc_17D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17D99")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_17DA8")

    label("loc_17D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17DA8")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x52, 0xFF)

    label("loc_17DA8")


    def lambda_17DAD():
        OP_95(0xFE, 9860, -6000, -21850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17DAD)
    Sleep(2000)

    def lambda_17DCA():
        OP_95(0xFE, 11690, -6000, -17960, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DCA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(10060, -5780, -20380, 6000)
    MoveCamera(246, 22, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(12250, 6000)
    WaitChrThread(0x24, 1)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_17E35():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17E35)
    Sleep(1000)

    def lambda_17E45():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17E45)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00006F*pant, pant*...\x01",
            "T-That's far enough!\x02\x03",
            "#00001FHow mean to tear off\x01",
            "girls' swimsuits!\x01",
            "You'll pay for this!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x24)
    TurnDirection(0x24, 0x101, 500)
    OP_63(0x24, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(997, 0, 100, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 1, 0, 111)
    Fade(250)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00007FHere I go!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_110_166D4 end

    def Function_111_17F5F(): pass

    label("Function_111_17F5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17F8C")

    def lambda_17F6F():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17F6F)
    WaitChrThread(0xFE, 2)
    Jump("Function_111_17F5F")

    label("loc_17F8C")

    Return()

    # Function_111_17F5F end

    def Function_112_17F8D(): pass

    label("Function_112_17F8D")

    PlayEffect(0x0, 0x0, 0xFF, 0x0, 53980, -7250, 28200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 49870, -7170, 27390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x1, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 49750, -7140, 23530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x2, 0x2)
    PlayEffect(0x0, 0x3, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_112_17F8D end

    def Function_113_1807C(): pass

    label("Function_113_1807C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18094")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_180BB")

    label("loc_18094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_180AA")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_180BB")

    label("loc_180AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_180BB")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_180BB")

    OP_68(10060, -5780, -20380, 0)
    MoveCamera(246, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12250, 0)
    LoadEffect(0x0, "event/ev13002.eff")
    LoadEffect(0x1, "event/ev13003.eff")
    LoadEffect(0x2, "event/ev10017.eff")
    SetChrPos(0x101, 11690, -6000, -17960, 180)
    SetChrPos(0xEF, 20760, -6000, -10490, 225)
    SetChrPos(0x153, 18910, -6000, -9190, 225)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0x153, 0x80)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x25, 0x26)
    SetChrChipByIndex(0x26, 0x27)
    SetChrChipByIndex(0x27, 0x28)
    SetChrChipByIndex(0x28, 0x29)
    SetChrChipByIndex(0x29, 0x2A)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x24, 9860, -6000, -21850, 0)
    SetChrPos(0x25, 28140, -2000, -38880, 315)
    SetChrPos(0x26, 31250, -2000, -37580, 315)
    SetChrPos(0x27, 16490, -2000, -39030, 315)
    SetChrPos(0x28, 20180, -2000, -40520, 315)
    SetChrPos(0x29, 29330, -2000, -41320, 315)
    PlayBGM("ed7451", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x24, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00000FHow do you like that...?\x01",
            "Prepare yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9490, -5480, -21070, 3000)

    def lambda_18298():
        OP_99(0xFE, 0x24, 0xBB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18298)
    Sleep(500)

    def lambda_182AF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_182AF)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x24)
    StopBGM(0xBB8)
    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_18335():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18335)
    Sleep(100)

    def lambda_18345():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_18345)

    ChrTalk(
        0x101,
        "#12P#00005FWhat...!?\x02",
    )

    CloseMessageWindow()

    def lambda_1836C():
        OP_95(0xFE, 23660, -2000, -35810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1836C)
    Sleep(100)

    def lambda_18389():
        OP_95(0xFE, 24940, -2000, -35780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_18389)
    Sleep(100)

    def lambda_183A6():
        OP_95(0xFE, 21250, -2000, -36870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_183A6)
    Sleep(100)

    def lambda_183C3():
        OP_95(0xFE, 21590, -2000, -35820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_183C3)
    Sleep(100)

    def lambda_183E0():
        OP_95(0xFE, 23090, -2000, -36580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_183E0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    Fade(500)
    OP_68(22400, -980, -33530, 0)
    MoveCamera(196, 24, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14520, 0)
    OP_68(21730, -980, -33480, 5000)
    MoveCamera(155, -3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(10320, 5000)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(8410, 500)
    Sleep(100)
    Sound(997, 0, 100, 0)
    BeginChrThread(0x25, 3, 0, 114)
    BeginChrThread(0x26, 3, 0, 115)
    BeginChrThread(0x27, 3, 0, 116)
    BeginChrThread(0x28, 3, 0, 117)
    BeginChrThread(0x29, 3, 0, 118)
    WaitChrThread(0x25, 3)
    Sound(556, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 28360, -2000, -46730, -30, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 24080, -2000, -38350, -30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, -30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(1500)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sleep(2000)
    SetMessageWindowPos(400, 300, -1, -1)

    AnonymousTalk(
        0x101,
        "#00011FI-It had comrades!?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(22520, -980, -32840, 0)
    MoveCamera(310, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16650, 0)
    BeginChrThread(0x25, 3, 0, 119)
    Sleep(300)
    BeginChrThread(0x26, 3, 0, 120)
    Sleep(300)
    BeginChrThread(0x27, 3, 0, 121)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 122)
    Sleep(300)
    BeginChrThread(0x29, 3, 0, 123)
    OP_68(10920, -5480, -18810, 2000)
    MoveCamera(281, 22, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(12890, 2000)
    TurnDirection(0x24, 0x101, 500)
    WaitChrThread(0x24, 3)
    BeginChrThread(0x24, 3, 0, 124)
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 124)
    WaitChrThread(0x26, 3)
    BeginChrThread(0x26, 3, 0, 124)
    WaitChrThread(0x25, 3)
    BeginChrThread(0x25, 3, 0, 124)
    WaitChrThread(0x29, 3)
    BeginChrThread(0x29, 3, 0, 124)
    WaitChrThread(0x27, 3)
    BeginChrThread(0x27, 3, 0, 124)
    BeginChrThread(0x2A, 1, 0, 125)
    OP_6F(0x79)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#11P#00010FUgh...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xEF, 0x80)
    ClearChrFlags(0x153, 0x80)

    NpcTalk(
        0x153,
        "KeA's Voice",
        "#4SLloyd!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1877D():
        OP_95(0xFE, 15180, -6000, -13330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1877D)

    def lambda_18797():
        OP_95(0xFE, 15380, -6000, -15880, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18797)

    def lambda_187B1():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_187B1)

    def lambda_187BE():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_187BE)

    def lambda_187CB():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_187CB)

    def lambda_187D8():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_187D8)
    Fade(500)
    OP_68(12740, -5980, -10870, 0)
    MoveCamera(308, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15750, 0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_68(9910, -5980, -17140, 3000)
    MoveCamera(290, 19, 0, 3000)
    WaitChrThread(0xEF, 1)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0xEF, 0x25)
    SetChrSubChip(0xEF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1885D")
    Sound(805, 0, 100, 0)
    Jump("loc_18863")

    label("loc_1885D")

    Sound(531, 0, 100, 0)

    label("loc_18863")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_188E3")

    ChrTalk(
        0x101,
        (
            "#00005FElie, KeA!\x01",
            "...Are you all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FW-We'll talk later!\x01",
            "Let's defeat the monsters now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189D5")

    label("loc_188E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18960")

    ChrTalk(
        0x101,
        (
            "#00005FTio, KeA!\x01",
            "...Are you all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...We'll talk later!\x01",
            "Let's take the monsters out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189D5")

    label("loc_18960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_189D5")

    ChrTalk(
        0x101,
        (
            "#00005FNoｱl, KeA!\x01",
            "...Are you all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FY-Yes!!\x01",
            "At any rate, let's\x01",
            "take them out now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189D5")


    ChrTalk(
        0x101,
        "#00000FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01107FGet 'em guys!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_98C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_113_1807C end

    def Function_114_18A1E(): pass

    label("Function_114_18A1E")

    OP_93(0x25, 0x13B, 0x1F4)
    OP_A1(0x25, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_114_18A1E end

    def Function_115_18A31(): pass

    label("Function_115_18A31")

    OP_93(0x26, 0x13B, 0x1F4)
    OP_A1(0x26, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_115_18A31 end

    def Function_116_18A44(): pass

    label("Function_116_18A44")

    OP_93(0x27, 0x13B, 0x1F4)
    OP_A1(0x27, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_116_18A44 end

    def Function_117_18A57(): pass

    label("Function_117_18A57")

    OP_93(0x28, 0x13B, 0x1F4)
    OP_A1(0x28, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_117_18A57 end

    def Function_118_18A6A(): pass

    label("Function_118_18A6A")

    OP_93(0x29, 0x13B, 0x1F4)
    OP_A1(0x29, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_118_18A6A end

    def Function_119_18A7D(): pass

    label("Function_119_18A7D")

    OP_A1(0x25, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x25, 0x50BE, 0xFFFFE890, 0xFFFF9A34, 0x7D0, 0x1388)
    OP_95(0x25, 10410, -6000, -16510, 5000, 0x0)
    TurnDirection(0x25, 0x101, 500)
    Return()

    # Function_119_18A7D end

    def Function_120_18ABD(): pass

    label("Function_120_18ABD")

    OP_A1(0x26, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x26, 0x4C22, 0xFFFFE890, 0xFFFF952A, 0x7D0, 0x1388)
    OP_95(0x26, 8150, -6000, -20170, 5000, 0x0)
    TurnDirection(0x26, 0x101, 500)
    Return()

    # Function_120_18ABD end

    def Function_121_18AFD(): pass

    label("Function_121_18AFD")

    OP_A1(0x27, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x27, 0x5942, 0xFFFFE890, 0xFFFF94DA, 0x7D0, 0x1388)
    OP_95(0x27, 12360, -6000, -15910, 5000, 0x0)
    TurnDirection(0x27, 0x101, 500)
    Return()

    # Function_121_18AFD end

    def Function_122_18B3D(): pass

    label("Function_122_18B3D")

    OP_A1(0x28, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x28, 0x4A4C, 0xFFFFE890, 0xFFFF9098, 0x7D0, 0x1388)
    OP_95(0x28, 13700, -6000, -22060, 5000, 0x0)
    TurnDirection(0x28, 0x101, 500)
    Return()

    # Function_122_18B3D end

    def Function_123_18B7D(): pass

    label("Function_123_18B7D")

    OP_A1(0x29, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x29, 0x51E0, 0xFFFFE890, 0xFFFF93CC, 0x7D0, 0x1388)
    OP_95(0x29, 14480, -6000, -18580, 5000, 0x0)
    TurnDirection(0x29, 0x101, 500)
    Return()

    # Function_123_18B7D end

    def Function_124_18BBD(): pass

    label("Function_124_18BBD")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18BE6")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_18BC8")

    label("loc_18BE6")

    Return()

    # Function_124_18BBD end

    def Function_125_18BE7(): pass

    label("Function_125_18BE7")

    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    Return()

    # Function_125_18BE7 end

    def Function_126_18C00(): pass

    label("Function_126_18C00")

    EventBegin(0x0)
    OP_68(13510, -4600, -17730, 0)
    MoveCamera(239, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8670, 0)
    SetChrPos(0x101, 11690, -6000, -17960, 180)
    SetChrPos(0x153, 13410, -6000, -16830, 180)
    SetChrPos(0xEF, 13730, -6000, -18890, 180)
    SetCameraDistance(9670, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(250)
    Sound(805, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18CA4")
    Sound(531, 0, 100, 0)

    label("loc_18CA4")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006F*phew*... \x01",
            "Well, we did it somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FGood work, you two.\x02",
    )

    CloseMessageWindow()

    def lambda_18D0C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_18D0C)
    Sleep(100)

    def lambda_18D1C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18D1C)
    Sleep(500)

    ChrTalk(
        0x153,
        "#12P#01109FEhehe, nice one!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18EA9")

    ChrTalk(
        0x102,
        (
            "#6P#00104FIn any case, with this\x01",
            "I believe the case is closed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F...Uhmm, Elie.\x02\x03",
            "#00006FHow to say this...\x01",
            "Sorry, I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x102,
        (
            "#6P#00112FE-Enough of that, don't worry.\x01",
            "I let my guard down too...\x02\x03",
            "#00103FMore importantly, I wonder why those\x01",
            "monsters appeared on the beach...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1914F")

    label("loc_18EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18FFC")

    ChrTalk(
        0x103,
        (
            "#6P#00204FIt seems the case is\x01",
            "closed for the time being.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F...Uhmm, Tio.\x02\x03",
            "#00006FHow to say this...\x01",
            "Sorry, I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x103,
        (
            "#6P#00203F...Don't worry about it.\x01",
            "I too let my guard down...\x02\x03",
            "#00200FMore importantly, I wonder why those\x01",
            "monsters appeared on the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1914F")

    label("loc_18FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1914F")

    ChrTalk(
        0x109,
        "#6P#10109FWith this, the case is closed for now!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F...Uhmm, Noｱl.\x02\x03",
            "#00006FHow to say this...\x01",
            "Sorry, I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x109,
        (
            "#6P#10112FP-Please don't be that concerned!\x01",
            "I too let my guard down...\x02\x03",
            "#10105FMore importantly, I wonder why those\x01",
            "monsters appeared at the beach, hm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1914F")


    ChrTalk(
        0x101,
        (
            "#00006FI can only guess. Most likely, it's due\x01",
            "to the impact of this area's development.\x02\x03",
            "#00001FMonsters, having no place to go due to\x01",
            "development, started to retaliate against\x01",
            "people... That's my best guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_19367")

    ChrTalk(
        0x102,
        (
            "#6P#00103FI see... It could be.\x02\x03",
            "#00101FMaybe they were encouraged\x01",
            "by seeing the commotion they\x01",
            "caused by ripping swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F...I feel kind of\x01",
            "bad for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000F...Well, for now, let's go\x01",
            "report to Miss Carmina\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYes, let's do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_195EB")

    label("loc_19367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_194AD")

    ChrTalk(
        0x103,
        (
            "#6P#00203FI see... It's a possibility.\x02\x03",
            "#00200FI wonder if they were encouraged\x01",
            "by seeing the commotion they\x01",
            "caused by ripping swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F...I feel kind of\x01",
            "bad for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000F...Well, for now, let's go\x01",
            "report to Miss Carmina\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_195EB")

    label("loc_194AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_195EB")

    ChrTalk(
        0x109,
        (
            "#6P#10103FI see... It's possible.\x02\x03",
            "#10101FCould they have been encouraged\x01",
            "by seeing the commotion they\x01",
            "caused by ripping swimsuits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F...I feel kind of\x01",
            "bad for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000F...Well, for now, let's go\x01",
            "report to Miss Carmina\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYes, let's go!\x02",
    )

    CloseMessageWindow()

    label("loc_195EB")

    StopSound(136, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("t1320", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_126_18C00 end

    SaveToFile()

Try(main)
