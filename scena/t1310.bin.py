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
        "Function_16_1724",        # 10, 16
        "Function_17_1C54",        # 11, 17
        "Function_18_1F82",        # 12, 18
        "Function_19_2195",        # 13, 19
        "Function_20_23DF",        # 14, 20
        "Function_21_24FB",        # 15, 21
        "Function_22_26A0",        # 16, 22
        "Function_23_280D",        # 17, 23
        "Function_24_2D0E",        # 18, 24
        "Function_25_3175",        # 19, 25
        "Function_26_3424",        # 1A, 26
        "Function_27_360B",        # 1B, 27
        "Function_28_366C",        # 1C, 28
        "Function_29_393D",        # 1D, 29
        "Function_30_3E72",        # 1E, 30
        "Function_31_3FA4",        # 1F, 31
        "Function_32_440F",        # 20, 32
        "Function_33_45DE",        # 21, 33
        "Function_34_4684",        # 22, 34
        "Function_35_46FA",        # 23, 35
        "Function_36_4770",        # 24, 36
        "Function_37_47DB",        # 25, 37
        "Function_38_5C68",        # 26, 38
        "Function_39_6FE0",        # 27, 39
        "Function_40_761E",        # 28, 40
        "Function_41_8294",        # 29, 41
        "Function_42_9CC5",        # 2A, 42
        "Function_43_9CDD",        # 2B, 43
        "Function_44_A74C",        # 2C, 44
        "Function_45_C49E",        # 2D, 45
        "Function_46_C529",        # 2E, 46
        "Function_47_CDD9",        # 2F, 47
        "Function_48_CE81",        # 30, 48
        "Function_49_CF29",        # 31, 49
        "Function_50_D010",        # 32, 50
        "Function_51_D0AB",        # 33, 51
        "Function_52_D167",        # 34, 52
        "Function_53_D415",        # 35, 53
        "Function_54_E5E3",        # 36, 54
        "Function_55_E75D",        # 37, 55
        "Function_56_EF00",        # 38, 56
        "Function_57_F23D",        # 39, 57
        "Function_58_12ECB",       # 3A, 58
        "Function_59_12F5A",       # 3B, 59
        "Function_60_12F72",       # 3C, 60
        "Function_61_12F9D",       # 3D, 61
        "Function_62_12FC8",       # 3E, 62
        "Function_63_12FF3",       # 3F, 63
        "Function_64_1301E",       # 40, 64
        "Function_65_13049",       # 41, 65
        "Function_66_13074",       # 42, 66
        "Function_67_1309F",       # 43, 67
        "Function_68_130CA",       # 44, 68
        "Function_69_130F5",       # 45, 69
        "Function_70_1310C",       # 46, 70
        "Function_71_13121",       # 47, 71
        "Function_72_13136",       # 48, 72
        "Function_73_1314B",       # 49, 73
        "Function_74_1322B",       # 4A, 74
        "Function_75_1330E",       # 4B, 75
        "Function_76_133EE",       # 4C, 76
        "Function_77_134D1",       # 4D, 77
        "Function_78_13535",       # 4E, 78
        "Function_79_135C5",       # 4F, 79
        "Function_80_13655",       # 50, 80
        "Function_81_137C5",       # 51, 81
        "Function_82_1463A",       # 52, 82
        "Function_83_14659",       # 53, 83
        "Function_84_146B9",       # 54, 84
        "Function_85_146F0",       # 55, 85
        "Function_86_1476A",       # 56, 86
        "Function_87_1478F",       # 57, 87
        "Function_88_147F4",       # 58, 88
        "Function_89_14810",       # 59, 89
        "Function_90_14901",       # 5A, 90
        "Function_91_14A20",       # 5B, 91
        "Function_92_14A47",       # 5C, 92
        "Function_93_14A6E",       # 5D, 93
        "Function_94_14A8D",       # 5E, 94
        "Function_95_14AAC",       # 5F, 95
        "Function_96_14AE4",       # 60, 96
        "Function_97_14B1C",       # 61, 97
        "Function_98_14B54",       # 62, 98
        "Function_99_14B6E",       # 63, 99
        "Function_100_14EB4",      # 64, 100
        "Function_101_14F4E",      # 65, 101
        "Function_102_15560",      # 66, 102
        "Function_103_156B0",      # 67, 103
        "Function_104_15767",      # 68, 104
        "Function_105_15777",      # 69, 105
        "Function_106_15787",      # 6A, 106
        "Function_107_159FF",      # 6B, 107
        "Function_108_15A99",      # 6C, 108
        "Function_109_15C7A",      # 6D, 109
        "Function_110_15D7D",      # 6E, 110
        "Function_111_175D1",      # 6F, 111
        "Function_112_175FF",      # 70, 112
        "Function_113_176EE",      # 71, 113
        "Function_114_1807B",      # 72, 114
        "Function_115_1808E",      # 73, 115
        "Function_116_180A1",      # 74, 116
        "Function_117_180B4",      # 75, 117
        "Function_118_180C7",      # 76, 118
        "Function_119_180DA",      # 77, 119
        "Function_120_1811A",      # 78, 120
        "Function_121_1815A",      # 79, 121
        "Function_122_1819A",      # 7A, 122
        "Function_123_181DA",      # 7B, 123
        "Function_124_1821A",      # 7C, 124
        "Function_125_18244",      # 7D, 125
        "Function_126_1825D",      # 7E, 126
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
    Jump("loc_1720")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B8")

    ChrTalk(
        0x22,
        (
            "You're our guests with\x01",
            "the reservation this\x01",
            "morning, I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Tch, how enviable. I'd\x01",
            "love to play in the water\x01",
            "with such beauties myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1720")

    label("loc_16B8")


    ChrTalk(
        0x22,
        (
            "Ah, I'm preparing this\x01",
            "stand's merchandise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Sorry but, could you\x01",
            "come back in a little\x01",
            "while?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1720")

    TalkEnd(0x22)
    Return()

    # Function_15_15E9 end

    def Function_16_1724(): pass

    label("Function_16_1724")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_192E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1867")

    ChrTalk(
        0xFE,
        (
            "A "White Stone" is a pure\x01",
            "white pretty stone you can\x01",
            "find in the area sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're sometimes buried in the\x01",
            ""white heaven" sand of our beach,\x01",
            "so maybe that's how they got here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for one too,\x01",
            "don't just search in the water,\x01",
            "but the beach area as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1929")

    label("loc_1867")


    ChrTalk(
        0xFE,
        (
            "I hear that White Stones are\x01",
            "sometimes found buried in the\x01",
            ""white heaven" sand of our beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for one too,\x01",
            "don't just search in the water,\x01",
            "but the beach area as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1929")

    Jump("loc_1C50")

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1AA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A13")

    ChrTalk(
        0xFE,
        (
            "Still, to think a monster\x01",
            "like that was the rumored\x01",
            "swimsuit tearer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought for sure it\x01",
            "was just a maniac or\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad things\x01",
            "are settled for the time\x01",
            "being. Thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AA0")

    label("loc_1A13")


    ChrTalk(
        0xFE,
        (
            "Still, to think a monster\x01",
            "like that was the rumored\x01",
            "swimsuit tearer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm glad things\x01",
            "are settled for the time\x01",
            "being. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA0")

    Jump("loc_1C50")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAE")

    ChrTalk(
        0xFE,
        (
            "I keep a watchful eye so\x01",
            "that nothing dangerous\x01",
            "happens on this beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still shallow nearby, but\x01",
            "if you go too far, a child's\x01",
            "legs can't reach bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care not to\x01",
            "go too far away when\x01",
            "playing in the water.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C50")

    label("loc_1BAE")


    ChrTalk(
        0xFE,
        (
            "It's still shallow nearby, but\x01",
            "if you go too far, a child's\x01",
            "legs can't reach bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care not to\x01",
            "go too far away when\x01",
            "playing in the water.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C50")

    TalkEnd(0xFE)
    Return()

    # Function_16_1724 end

    def Function_17_1C54(): pass

    label("Function_17_1C54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7B")
    TalkEnd(0xFE)
    Call(0, 52)
    Return()

    label("loc_1C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0xA,
        (
            "#12613FHonestly! Going through\x01",
            "something like this all\x01",
            "of a sudden...\x02\x03",
            "#12611FCan't you have a little\x01",
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
    Jump("loc_1D4B")

    label("loc_1D24")


    ChrTalk(
        0xA,
        (
            "#12613F*sigh*, honestly,\x01",
            "Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4B")

    Jump("loc_1F7E")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D66")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(
        0xA,
        (
            "#12600FI'm glad you applied\x01",
            "sunscreen on me, but...\x02\x03",
            "#12613FA-As I thought, having it\x01",
            "applied by a colleague was\x01",
            "a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FHa... Haha. To be\x01",
            "honest, I was\x01",
            "embarrassed too.\x02\x03",
            "#12503F(Even so... *gulp*.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612F...Umm, Lloyd? I'd like\x01",
            "it if you didn't stare\x01",
            "at me for so long.\x02",
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
    Jump("loc_1F7E")

    label("loc_1EDA")


    ChrTalk(
        0xA,
        (
            "#12613FIt was a little embarrassing\x01",
            "having it applied by a\x01",
            "colleague.\x02\x03",
            "#12611FAlthough, I think it was\x01",
            "better than having it applied\x01",
            "by Randy or someone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7E")

    TalkEnd(0xFE)
    Return()

    # Function_17_1C54 end

    def Function_18_1F82(): pass

    label("Function_18_1F82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203A")

    ChrTalk(
        0x8,
        (
            "#13305FOh, Lloyd. Are you looking\x01",
            "for something with KeA and\x01",
            "the others?\x02\x03",
            "#13303FWhite Stones...? Hmm, I\x01",
            "haven't seen any nearby.\x01",
            "I'm sorry I couldn't help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2191")

    label("loc_203A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2050")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(
        0x8,
        (
            "#13304FHaha, that was nice.\x01",
            "Thank you, Lloyd.\x02\x03",
            "#13309F...Oh, that's right.\x01",
            "Should I now apply lotion\x01",
            "to you in return, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FI-I'm fine already!\x01",
            "Sleep well, Cecil.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2191")

    label("loc_2118")


    ChrTalk(
        0x8,
        (
            "#13304FIt feels so good I think\x01",
            "I'll fall asleep just\x01",
            "like this.\x02\x03",
            "#13309FHaha. Wake me up if\x01",
            "something happens, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2191")

    TalkEnd(0xFE)
    Return()

    # Function_18_1F82 end

    def Function_19_2195(): pass

    label("Function_19_2195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2239")

    ChrTalk(
        0x9,
        (
            "#13505FWhite, round, pretty\x01",
            "stones...? No, I haven't\x01",
            "seen any.\x02\x03",
            "#13503FThe beach itself is\x01",
            "white and pretty. They\x01",
            "won't be easy to find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DB")

    label("loc_2239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224F")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_224F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2345")

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
            "#13505FAh, no, sorry. I was just\x01",
            "thinking about something.\x02\x03",
            "#13504FUmm, Lloyd? Thank you very\x01",
            "much.\x02\x03",
            "#13502FHaha. It seems I won't have\x01",
            "to worry about sunburn for\x01",
            "the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23DB")

    label("loc_2345")


    ChrTalk(
        0x9,
        (
            "#13504FIt seems I won't have to\x01",
            "worry about sunburn for a\x01",
            "while.\x02\x03",
            "#13502FIt seems Ilya and Sully\x01",
            "are having fun too...\x01",
            "Haha, I'm happy for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DB")

    TalkEnd(0xFE)
    Return()

    # Function_19_2195 end

    def Function_20_23DF(): pass

    label("Function_20_23DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2456")

    ChrTalk(
        0x11,
        (
            "#12805FHmm? You're lookin' for\x01",
            "white pebbles?\x02\x03",
            "#12803FSorry, but I haven't\x01",
            "seen any nearby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F7")

    label("loc_2456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2465")
    Jump("loc_24F7")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2477")
    Call(0, 21)
    Jump("loc_24F7")

    label("loc_2477")


    ChrTalk(
        0x11,
        (
            "#12800FI wanted to surf but\x01",
            "they said they don't\x01",
            "rent boards.\x02\x03",
            "#12806FIt was my chance to show\x01",
            "the girls my strong\x01",
            "points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F7")

    TalkEnd(0xFE)
    Return()

    # Function_20_23DF end

    def Function_21_24FB(): pass

    label("Function_21_24FB")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "#13002FAfter I've rested for a\x01",
            "while, I'd like to do\x01",
            "something else.\x02\x03",
            "#13004FHmm, I think there are\x01",
            "ways other than games to\x01",
            "enjoy the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FLet's see, I think we've run out of\x01",
            "most of the standbys...\x02\x03",
            "#12806FActually, I would've liked to dress up\x01",
            "and pick up girls, but with the beach\x01",
            "reserved, I can't meet any babes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006FYou really never do\x01",
            "change, do you...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_24FB end

    def Function_22_26A0(): pass

    label("Function_22_26A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2752")

    ChrTalk(
        0x12,
        (
            "#13000FIf you're looking for something,\x01",
            "it might be a good idea to\x01",
            "change your point of view.\x02\x03",
            "#13003FIt could be in an unexpected,\x01",
            "unthinkable place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2809")

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2761")
    Jump("loc_2809")

    label("loc_2761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2773")
    Call(0, 21)
    Jump("loc_2809")

    label("loc_2773")


    ChrTalk(
        0x12,
        (
            "#13003FHmm, I think there are\x01",
            "ways other than games to\x01",
            "enjoy the beach.\x02\x03",
            "#13000FIt would be nice if\x01",
            "there were a way to play\x01",
            "with more people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2809")

    TalkEnd(0xFE)
    Return()

    # Function_22_26A0 end

    def Function_23_280D(): pass

    label("Function_23_280D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2953")

    ChrTalk(
        0x13,
        (
            "#12900FWhite Stones...? If I recall,\x01",
            "they're stones this beach's white\x01",
            "heaven sand comes from.\x02\x03",
            "#12904FAlmost all White Stones turn to sand\x01",
            "after many years, but it is said\x01",
            "that sometimes, they remain pretty.\x02\x03",
            "#12902FHehe. If you find a big one, you can\x01",
            "consider yourself pretty lucky.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A16")

    label("loc_2953")


    ChrTalk(
        0x13,
        (
            "#12904FAlmost all White Stones turn to sand\x01",
            "after many years, but it is said\x01",
            "that sometimes, they remain pretty.\x02\x03",
            "#12902FHehe. If you find a big one, you can\x01",
            "consider yourself pretty lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A16")

    Jump("loc_2D0A")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2A")
    Jump("loc_2D0A")

    label("loc_2A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C60")

    ChrTalk(
        0x13,
        (
            "#12906FOh man. I'm completely\x01",
            "tired because it's a\x01",
            "game I'm not used to.\x02\x03",
            "#12900FEssentially, games which\x01",
            "involve body movement\x01",
            "aren't my forte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12503FYou say that, but you're not even\x01",
            "out of breath...\x02\x03",
            "#12502FWait, I feel like you were pretty\x01",
            "knowledgeable about the rules too.\x01",
            "Could it actually be your forte?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FHehe, as if. I'm a genuine city\x01",
            "boy, you know?\x02\x03",
            "#12900FAs for the beach volleyball rules,\x01",
            "I just remembered from having read\x01",
            "them in a magazine to kill time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12503F(I think that's amazing\x01",
            "in its own way...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2D0A")

    label("loc_2C60")


    ChrTalk(
        0x13,
        (
            "#12906FOh man. I'm completely tired\x01",
            "because it's a game I'm not\x01",
            "used to.\x02\x03",
            "#12909FHehe. I think I'll spend my\x01",
            "time on a deck chair mingling\x01",
            "with Elie and the others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0A")

    TalkEnd(0xFE)
    Return()

    # Function_23_280D end

    def Function_24_2D0E(): pass

    label("Function_24_2D0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E09")

    ChrTalk(
        0x10,
        (
            "#13400FLooks like KeA is playing\x01",
            "with our Sully, eh?\x02\x03",
            "#13404FHaha. Because she doesn't\x01",
            "have friends her age, she\x01",
            "isn't used to be yearned for.\x02\x03",
            "#13402FMaybe I'll see a new side of\x01",
            "her today. Hehe, I can't\x01",
            "wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2EA3")

    label("loc_2E09")


    ChrTalk(
        0x10,
        (
            "#13404FBecause Sully doesn't\x01",
            "have friends her age, she\x01",
            "isn't used to attachment.\x02\x03",
            "#13402FMaybe I'll see a new side\x01",
            "of her today. Hehe, I\x01",
            "can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA3")

    Jump("loc_3171")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB7")
    Jump("loc_3171")

    label("loc_2EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B7")

    ChrTalk(
        0x10,
        (
            "#13409FMaaan, working on sports\x01",
            "every now and then is\x01",
            "nice too.\x02\x03",
            "#13402FI also get to enjoy cute\x01",
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
            "#12512FIlya, you're actually an\x01",
            "old man disguised as an\x01",
            "artist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406FMy, how rude.\x02\x03",
            "#13402FHehe, you weren't able to take your\x01",
            "eyes off Cecil, Rixia and the others in\x01",
            "their swimsuits either, eh, little bro?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511FN-No comment.\x02\x03",
            "#12506F(Rather, I think Ilya's\x01",
            "swimsuit is the most\x01",
            "amazing of all...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3171")

    label("loc_30B7")


    ChrTalk(
        0x10,
        (
            "#13404FCome to think of it, it's been really\x01",
            "a long time since I've exercised like\x01",
            "this aside from training.\x02\x03",
            "#13402FYep, accepting the invitation really\x01",
            "was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3171")

    TalkEnd(0xFE)
    Return()

    # Function_24_2D0E end

    def Function_25_3175(): pass

    label("Function_25_3175")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323F")

    ChrTalk(
        0xB,
        (
            "#12705FWhite Stones... There are things\x01",
            "like that on this beach?\x02\x03",
            "#12703FWe used the sand in this area as\x01",
            "the sand castle's foundation, but\x01",
            "we didn't find anything like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3420")

    label("loc_323F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3255")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_3255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(
        0xB,
        (
            "#12703FI had my doubts as to whether\x01",
            "something like this could be\x01",
            "built with just sand, but...\x02\x03",
            "#12702FRather, I now feel like I\x01",
            "could build anything with\x01",
            "sand.\x02\x03",
            "#12704FHaha. It might be nice to\x01",
            "build a house for Zeit next.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F(I'm sure Zeit hates\x01",
            "sand...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01203FGrrowl...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3420")

    label("loc_33A7")


    ChrTalk(
        0xB,
        (
            "#12704FI feel like I could\x01",
            "build anything with\x01",
            "sand.\x02\x03",
            "#12702FHaha. It might be nice\x01",
            "to build a house for\x01",
            "Zeit next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3420")

    TalkEnd(0xFE)
    Return()

    # Function_25_3175 end

    def Function_26_3424(): pass

    label("Function_26_3424")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3494")

    ChrTalk(
        0xC,
        (
            "#13105FOh, you're looking for\x01",
            "something?\x02\x03",
            "#13103FWhite Stones...? Hmm,\x01",
            "I'm not sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3607")

    label("loc_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AA")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_34AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3599")

    ChrTalk(
        0xC,
        (
            "#13109FWooow, it really became a\x01",
            "magnificent castle!\x02\x03",
            "#13106FIf we had brought a camera\x01",
            "we could've taken a picture,\x01",
            "but... Boo, what a pity.\x02\x03",
            "#13101FI must at least firmly\x01",
            "imprint it in the photo\x01",
            "quartz of my mind!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3607")

    label("loc_3599")


    ChrTalk(
        0xC,
        (
            "#13101FThe shape of this castle... I will\x01",
            "go back home with it imprinted in\x01",
            "the photo quartz of my mind!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3607")

    TalkEnd(0xFE)
    Return()

    # Function_26_3424 end

    def Function_27_360B(): pass

    label("Function_27_360B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3636")

    ChrTalk(
        0xD,
        "#01200F...Woof?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3668")

    label("loc_3636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364C")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_364C")


    ChrTalk(
        0xD,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3668")

    TalkEnd(0xFE)
    Return()

    # Function_27_360B end

    def Function_28_366C(): pass

    label("Function_28_366C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36FD")

    ChrTalk(
        0xE,
        (
            "#13210FAh, Lloyd... Did you\x01",
            "already find a "White\x01",
            "Stone"?\x02\x03",
            "#13209FEhehe, I wonder if there\x01",
            "are any big ones\x01",
            "anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3939")

    label("loc_36FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3713")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_END)), "loc_38D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384F")

    ChrTalk(
        0xE,
        (
            "#13210FThis White Stone is\x01",
            "really big!\x02\x03",
            "#13209FIt's maybe the best\x01",
            "memory I've made at\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12509FWe've just arrived, so\x01",
            "isn't it a little early\x01",
            "for that?\x02\x03",
            "#12504FHowever, if you're that\x01",
            "happy, it makes me happy\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209FEhehe, thank you, Lloyd.\x01",
            "I'll treasure it!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_38D2")

    label("loc_384F")


    ChrTalk(
        0xE,
        (
            "#13202FEhehe, this is maybe the\x01",
            "best memory I've made at\x01",
            "Michelam.\x02\x03",
            "#13209FThank you, Lloyd. I'll\x01",
            "treasure this White\x01",
            "Stone!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D2")

    Jump("loc_3939")

    label("loc_38D7")


    ChrTalk(
        0xE,
        (
            "#13209FIt was fun looking for a\x01",
            "White Stone, huh.\x02\x03",
            "#13204FEhehe, I'll show it to\x01",
            "Zeit later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3939")

    TalkEnd(0xFE)
    Return()

    # Function_28_366C end

    def Function_29_393D(): pass

    label("Function_29_393D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3979")
    Call(0, 30)
    Jump("loc_3BF6")

    label("loc_3979")

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
            "Cancel\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39EB")
    Call(0, 30)
    Jump("loc_3BF6")

    label("loc_39EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE7")

    ChrTalk(
        0xF,
        (
            "#13605FHmm... Looks like you\x01",
            "found a white stone.\x02\x03",
            "#13600FShould we compare sizes\x01",
            "already?\x02",
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
            "Better Not\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6D")

    ChrTalk(
        0x101,
        (
            "#12504FYeah, let's get this\x01",
            "party started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13605FHmm, you seem awfully\x01",
            "confident.\x02\x03",
            "#13604FAlright, I'll call\x01",
            "shorty over. Heh, don't\x01",
            "cry, ok?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    Call(0, 53)
    Return()

    label("loc_3B6D")


    ChrTalk(
        0x101,
        (
            "#12500FNo, I need another\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606FTch, what's with you? If\x01",
            "you're a man, make up\x01",
            "your mind already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF6")

    label("loc_3BE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF6")

    label("loc_3BF6")

    Jump("loc_3E6E")

    label("loc_3BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C11")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 2)), scpexpr(EXPR_END)), "loc_3DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8D")

    ChrTalk(
        0xF,
        (
            "#13600FUmm, you know... Thanks\x01",
            "for earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FYou mean the White\x01",
            "Stone? Don't worry about\x01",
            "it.\x02\x03",
            "#12509FHaha. I think you should\x01",
            "show it to everyone at\x01",
            "Arc-en-Ciel.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#13611FI-Idiot... As if I'd\x01",
            "ever do such a childish\x01",
            "thing!\x02\x03",
            "#13606FUse some common sense,\x01",
            "jeez...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12506F(It's hard being a girl\x01",
            "her age...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3DD4")

    label("loc_3D8D")


    ChrTalk(
        0xF,
        (
            "#13603FThanks for the White\x01",
            "Stone.\x02\x03",
            "#13608F...H-Hmph, that's all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD4")

    Jump("loc_3E6E")

    label("loc_3DD9")


    ChrTalk(
        0xF,
        (
            "#13603FSearching for pebbles is\x01",
            "fine, but... Since we're at\x01",
            "the beach, I want to swim.\x02\x03",
            "#13602FIt'd be nice if I got\x01",
            "better than Rixia at it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6E")

    TalkEnd(0xFE)
    Return()

    # Function_29_393D end

    def Function_30_3E72(): pass

    label("Function_30_3E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2C")

    ChrTalk(
        0xF,
        (
            "#13600FTell me if you find a\x01",
            ""White Stone".\x02\x03",
            "Then we'll compare sizes\x01",
            "and whoever has the\x01",
            "biggest will win.\x02\x03",
            "#13604FWell, as If I'd ever\x01",
            "lose to the likes of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3FA3")

    label("loc_3F2C")


    ChrTalk(
        0xF,
        (
            "#13600FWe'll see whose "White\x01",
            "Stone" is the biggest\x01",
            "later.\x02\x03",
            "#13604FWell, as If I'd ever\x01",
            "lose to the likes of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA3")

    Return()

    # Function_30_3E72 end

    def Function_31_3FA4(): pass

    label("Function_31_3FA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3FB5")
    Jump("loc_440B")

    label("loc_3FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_440B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403A")

    ChrTalk(
        0x101,
        (
            "#12500FHuh, this black cat... I\x01",
            "feel like I've seen it\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nyaa~... [I'm hungry.]\x02",
    )

    CloseMessageWindow()
    Jump("loc_4056")

    label("loc_403A")


    ChrTalk(
        0xFE,
        "Nyaa~... [I'm hungry.]\x02",
    )

    CloseMessageWindow()

    label("loc_4056")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_429D")

    ChrTalk(
        0x101,
        (
            "#12505F...I wonder if she's\x01",
            "hungry.\x02",
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
            "Give her [Cat Food]\x01",      # 0
            "Cancel\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4289")

    ChrTalk(
        0x101,
        (
            "#12500FYou can eat it if you\x01",
            "like.\x02",
        )
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
        "Nyanyayayaa~㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*enthusiastically\x01",
            "eating*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12509FHaha, were you that\x01",
            "hungry?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Nyaon㈱ [Goodbye.]\x02",
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
            "#12505FHuh... Are you giving me\x01",
            "this book?\x02\x03",
            "#12500FHaha, thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 5)
    SubItemNumber(0x1D9, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4298")

    label("loc_4289")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4298")

    label("loc_4298")

    Jump("loc_43EB")

    label("loc_429D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4352")

    ChrTalk(
        0x101,
        (
            "#12505F...I wonder if she's\x01",
            "hungry...\x02\x03",
            "#12503FI could give you some\x01",
            "Cat Food if I brought\x01",
            "some, but...\x02\x03",
            "#12512FUnfortunately, I don't\x01",
            "have any right now.\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D1")

    label("loc_4352")


    ChrTalk(
        0x101,
        (
            "#12503FI could give you some\x01",
            "Cat Food if I brought\x01",
            "some, but...\x02\x03",
            "#12512FUnfortunately, I don't\x01",
            "have any right now.\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D1")


    ChrTalk(
        0xFE,
        "Nyaon... [I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_43EB")

    SetScenarioFlags(0x1, 6)
    Jump("loc_440B")

    label("loc_43F3")


    ChrTalk(
        0xFE,
        "Nyaon㈱ [Goodbye.]\x02",
    )

    CloseMessageWindow()

    label("loc_440B")

    TalkEnd(0xFE)
    Return()

    # Function_31_3FA4 end

    def Function_32_440F(): pass

    label("Function_32_440F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Cautions When Enjoying Lake Beach\x01",
            "─────────────────────────────\x01",
            "・Please be sure to warm up.\x01",
            "・Please, do not enter the water in street clothes.\x01",
            "  (We loan swimsuits at the reception desk)\x01",
            "・Please, observe the lifeguard's instructions.\x01",
            "─────────────────────────────\x01",
            "  Let's mind our manners and have fun.\x01",
            "  　──Michelam Operations Department\x07\x00\x02",
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

    # Function_32_440F end

    def Function_33_45DE(): pass

    label("Function_33_45DE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FWhoops... This is the way back\x01",
            "inside.\x02\x03",
            "Since Mariabell went to the\x01",
            "trouble of reserving it for us,\x01",
            "let's enjoy the beach for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10330, -2000, -920, 90)
    EventEnd(0x4)
    Return()

    # Function_33_45DE end

    def Function_34_4684(): pass

    label("Function_34_4684")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FThere should be "White Stones"\x01",
            "somewhere on the beach. I'll\x01",
            "search a while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11580, -5080, -120, 90)
    EventEnd(0x4)
    Return()

    # Function_34_4684 end

    def Function_35_46FA(): pass

    label("Function_35_46FA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FThere should be "White Stones"\x01",
            "somewhere on the beach. I'll\x01",
            "search a while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11210, -4940, 46030, 90)
    EventEnd(0x4)
    Return()

    # Function_35_46FA end

    def Function_36_4770(): pass

    label("Function_36_4770")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FWhoops... I'll look for\x01",
            "them without interrupting\x01",
            "the beach volleyball.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 32500, -6000, -13500, 90)
    EventEnd(0x5)
    Return()

    # Function_36_4770 end

    def Function_37_47DB(): pass

    label("Function_37_47DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47ED")
    Call(0, 36)
    Return()

    label("loc_47ED")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8E")
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
        "#13400F#11P─Alright♪\x02",
    )

    CloseMessageWindow()

    def lambda_4948():
        TurnDirection(0x13, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4948)
    Sleep(50)

    def lambda_4958():
        TurnDirection(0x11, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4958)
    Sleep(50)

    def lambda_4968():
        TurnDirection(0x12, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4968)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x11,
        (
            "#12809F#5PMan, I expected as\x01",
            "much!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006F#6PI couldn't even see the\x01",
            "ball...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x10, 500)

    ChrTalk(
        0x13,
        (
            "#12902F#12PHehe, your explosiveness\x01",
            "was perfect on that\x01",
            "spike.\x02\x03",
            "#12904FI'd expect nothing less\x01",
            "from the great Ilya\x01",
            "Platiere.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x13, 500)

    ChrTalk(
        0x10,
        "#13409F#5PHehe, you're welcome.\x02",
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

    def lambda_4B35():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4B35)
    Sleep(50)

    def lambda_4B45():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4B45)
    Sleep(50)

    def lambda_4B55():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4B55)
    Sleep(50)

    def lambda_4B65():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4B65)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x10,
        (
            "#13400F#11POh, little bro. See\x01",
            "that?\x02\x03",
            "#13409FHow'd you like my\x01",
            "special move?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PY-Yeah... It was really\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PYeah. It was seriously\x01",
            "awe-inspiring.\x02\x03",
            "#12804FYou even received my\x01",
            "spike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWazy, you also seem like\x01",
            "you've done this before, from\x01",
            "the way you assisted Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#11PHaha, that was just a\x01",
            "fluke. You guys make a good\x01",
            "combo yourselves, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PWell honestly, you guys are\x01",
            "at such a high level that I\x01",
            "can't put it into words.\x02\x03",
            "#12500FIf you guys entered a\x01",
            "tournament, you could go for\x01",
            "the championship immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PHaha, well I don't think it'd\x01",
            "be that easy, but it might go\x01",
            "ok.\x02\x03",
            "#13409FOh yeah! How 'bout you pick our\x01",
            "next game, little bro? Let's\x01",
            "enjoy some beach volleyball♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15D, 2)
    Jump("loc_4FAE")

    label("loc_4E8E")

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
            "#13400F#11PYou're here, so, wanna\x01",
            "join the next game,\x01",
            "little bro?\x02\x03",
            "#13409FLet's enjoy beach volley\x01",
            "together♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Play Beach Volleyball\x01",      # 0
            "Refuse\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD8")

    ChrTalk(
        0x101,
        (
            "#12500F#6PAlright, I'll take you\x01",
            "up on that.\x02\x03",
            "#12506FBut I don't know the\x01",
            "rules all that well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000FThey're basically the\x01",
            "same as regular\x01",
            "volleyball.\x02\x03",
            "#13004FThe main differences are\x01",
            "the teams of two and that\x01",
            "it's played on sand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FAlso, the first to 21\x01",
            "normally wins a set.\x02\x03",
            "But we've cut it to 12\x01",
            "today for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHmm, I see... No problem\x01",
            "here, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PLet's set aside the\x01",
            "details and pick teams.\x02\x03",
            "#12806FIf Lloyd joins, someone\x01",
            "will have to sit out and\x01",
            "be the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#6POh right. I guess I'm\x01",
            "intruding then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PAhaha, I don't mind.\x02\x03",
            "#13400FAlright then, little\x01",
            "bro. Who do you want to\x01",
            "team up with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6PGot it. Then...\x02",
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
            "#1KWith whom will you team\x01",
            "up?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Randy\x01",      # 0
            "Noｱl\x01",      # 1
            "Wazy\x01",       # 2
            "Ilya\x01",       # 3
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
        (0, "loc_5366"),
        (1, "loc_550B"),
        (2, "loc_56E3"),
        (3, "loc_58CE"),
        (SWITCH_DEFAULT, "loc_5AB9"),
    )


    label("loc_5366")


    ChrTalk(
        0x101,
        (
            "#12500F#6PRandy, I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800F#5PAll right, leave it to\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13004F#5PWe just need to decide\x01",
            "the other team and the\x01",
            "referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FHow about rock-paper-\x01",
            "scissors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#13409F#11PHaha, got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya lost at rock-paper-\x01",
            "scissors and became the\x01",
            "referee.\x07\x00\x02",
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
            "Randy versus Wazy and\x01",
            "Noｱl began.\x07\x00\x02",
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
    Jump("loc_5AB9")

    label("loc_550B")


    ChrTalk(
        0x101,
        (
            "#12500F#6PNoｱl, I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PUnderstood! Let's do our\x01",
            "best, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FThen, shall we decide\x01",
            "the remaining team and\x01",
            "referee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13400F#11PHow about rock-paper-\x01",
            "scissors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#5PRight, let's decide it\x01",
            "at once!\x02",
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
            "Due to result of the rock-\x01",
            "paper-scissors, Randy was\x01",
            "assigned to be the referee...\x07\x00\x02",
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
            "Noｱl versus Ilya and\x01",
            "Wazy began.\x07\x00\x02",
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
    Jump("loc_5AB9")

    label("loc_56E3")


    ChrTalk(
        0x101,
        (
            "#12500F#6PWazy, I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12900FHehe, an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PThen, let's decide the\x01",
            "remaining team and\x01",
            "referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800F#5PWell, what do you say\x01",
            "'bout rock-paper-\x01",
            "scissors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#5PRight, let's decide it\x01",
            "quickly and begin the\x01",
            "game!\x02",
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
            "Due to result of the rock-\x01",
            "paper-scissors, Noｱl was\x01",
            "assigned to be the referee...\x07\x00\x02",
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
            "Wazy versus Ilya and\x01",
            "Randy began.\x07\x00\x02",
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
    Jump("loc_5AB9")

    label("loc_58CE")


    ChrTalk(
        0x101,
        (
            "#12500F#6PIlya, please, I'm\x01",
            "counting on you.\x02",
        )
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
            "#12804F#5PThen, let's decide the\x01",
            "remaining team and\x01",
            "referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWell, rock-paper-\x01",
            "scissors should be fine\x01",
            "for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902FHehe, right. Well, let's\x01",
            "decide it quick.\x02",
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
            "Due to result of the rock-\x01",
            "paper-scissors, Wazy was\x01",
            "assigned to be the referee...\x07\x00\x02",
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
            "Ilya versus Randy and\x01",
            "Noｱl began.\x07\x00\x02",
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
    Jump("loc_5AB9")

    label("loc_5AB9")

    Call(0, 38)
    Call(0, 39)
    Call(0, 45)
    SetChrPos(0x0, 20000, -6000, -15000, 0)
    Jump("loc_5C4D")

    label("loc_5AD8")


    ChrTalk(
        0x101,
        (
            "#12500F#6PUmm, now isn't a great\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13405F#11PMy, is that so? Well, it\x01",
            "can't be helped.\x02\x03",
            "#13400FIn that case, just let\x01",
            "me know when you want to\x01",
            "join whenever.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C3C")
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

    label("loc_5C3C")

    SetChrPos(0x0, 32500, -6000, -13500, 90)

    label("loc_5C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C65")
    Call(0, 54)

    label("loc_5C65")

    EventEnd(0x5)
    Return()

    # Function_37_47DB end

    def Function_38_5C68(): pass

    label("Function_38_5C68")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_5FE5")
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
            "#12809F#6PHaha, that was a good\x01",
            "match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12902FHaha, yeah. Not too bad.\x02",
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

    def lambda_5E36():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E36)
    Sleep(50)

    def lambda_5E46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5E46)
    Sleep(50)

    def lambda_5E56():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5E56)
    Sleep(50)

    def lambda_5E66():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5E66)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x12,
        "#13005F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#5PThere's no way just\x01",
            "watching such a fun game\x01",
            "could ever be enough.\x02\x03",
            "#13409FLet's play another game\x01",
            "where I'm in the mix!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHaha, then let's form\x01",
            "different teams this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#12PHaha. Sure, why not.\x02\x03",
            "#12800FSo Lloyd, who do you\x01",
            "want to team up with\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, ok...\x02",
    )

    CloseMessageWindow()
    Jump("loc_69F0")

    label("loc_5FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_6314")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x12, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#13009F#6P*sigh*... What a heated\x01",
            "match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PYes, yes, that was a\x01",
            "nice workout.\x02",
        )
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
            "#12806F#5PMrr... The moment Lloyd\x01",
            "joined, things heated up\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6162():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6162)
    Sleep(50)

    def lambda_6172():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6172)
    Sleep(50)

    def lambda_6182():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6182)
    Sleep(50)

    def lambda_6192():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6192)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x13,
        "#12905F#12PHmm? Something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12803F#5PWell, unfair if I'm just\x01",
            "watchin', right?\x02\x03",
            "#12800FLet's have another match\x01",
            "with me in the mix!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PYeah, then let's form\x01",
            "different teams this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#12PYes, that sounds good.\x02\x03",
            "#13000FThen, Lloyd, please\x01",
            "choose who you'd like to\x01",
            "team up with next!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, ok...\x02",
    )

    CloseMessageWindow()
    Jump("loc_69F0")

    label("loc_6314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_663E")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x13, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x11, 27000, -6000, -14000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#12902F#6PHehe, that was pretty\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#11PYeah, it was quite the\x01",
            "nice match.\x02",
        )
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
            "#13001F#5P...Umm, everyone! If\x01",
            "possible, can we play\x01",
            "another game?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6489():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6489)
    Sleep(50)

    def lambda_6499():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6499)
    Sleep(50)

    def lambda_64A9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_64A9)
    Sleep(50)

    def lambda_64B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_64B9)
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
            "#13006F#5PIt's just, while watching\x01",
            "the game just now, I\x01",
            "couldn't contain myself...\x02\x03",
            "#13002FPlease, include me in the\x01",
            "next one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PYeah, then let's form\x01",
            "different teams this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904F#12PHehe, I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902F#12PThen Lloyd, choose who\x01",
            "you want to team up with\x01",
            "next.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5PYeah, ok...\x02",
    )

    CloseMessageWindow()
    Jump("loc_69F0")

    label("loc_663E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_69F0")
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
            "#12900F#5PHehe, then should end\x01",
            "things here?\x02\x03",
            "#12904FI'm also getting\x01",
            "thirsty.\x02",
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
            "#12504F#12PWell... Since we're\x01",
            "here, why don't we have\x01",
            "another game?\x02\x03",
            "#12500FWith Wazy in, this time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6823():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6823)
    Sleep(50)

    def lambda_6833():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6833)
    Sleep(50)

    def lambda_6843():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6843)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)

    ChrTalk(
        0x11,
        (
            "#12800F#11PYeah, that sounds good.\x01",
            "You're tired of being the\x01",
            "referee too, right, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#12906F#5PWell, either is fine with\x01",
            "me, but...\x02\x03",
            "#12900F...Hehe, no choice then. If\x01",
            "you're up to it, I think I\x01",
            "can keep you company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12PHehe, it's decided then.\x02\x03",
            "#13400FThen, little bro, choose\x01",
            "who you want to team up\x01",
            "with next.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#6PYes, alright. Then...\x02",
    )

    CloseMessageWindow()

    label("loc_69F0")

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
            "#1KWith whom will you team\x01",
            "up?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "Ilya")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_6A60")
    MenuCmd(3, 0, 0x0)

    label("loc_6A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_6A6D")
    MenuCmd(3, 0, 0x1)

    label("loc_6A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_6A7A")
    MenuCmd(3, 0, 0x2)

    label("loc_6A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_6A87")
    MenuCmd(3, 0, 0x3)

    label("loc_6A87")

    MenuCmd(2, 0, -1, 85, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6ACC"),
        (1, "loc_6C10"),
        (2, "loc_6D5D"),
        (3, "loc_6E9C"),
        (SWITCH_DEFAULT, "loc_6FDF"),
    )


    label("loc_6ACC")

    TurnDirection(0x101, 0x11, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NAlright, you're up,\x01",
            "Randy. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x11, 0x101, 500)

    ChrTalk(
        0x11,
        (
            "#12809F#5P#NAll right, leave it to\x01",
            "me!\x02",
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
            "In a second game of rock-paper-\x01",
            "scissors, Ilya was chosen as\x01",
            "the second game's referee...\x07\x00\x02",
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
            "This next match was\x01",
            "Lloyd and Randy versus\x01",
            "Wazy and Noｱl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 9)
    Jump("loc_6FDF")

    label("loc_6C10")

    TurnDirection(0x101, 0x12, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NAlright Noｱl, you're up.\x01",
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
            "#13009F#5P#NUnderstood! Let's do our\x01",
            "best, Lloyd!\x02",
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
            "In a second game of rock-paper-\x01",
            "scissors, Randy was chosen as\x01",
            "the second game's referee...\x07\x00\x02",
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
            "This next match was\x01",
            "Lloyd and Noｱl versus\x01",
            "Ilya and Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 24)
    Jump("loc_6FDF")

    label("loc_6D5D")

    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NAlright, you're up,\x01",
            "Wazy. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHehe, an easy request.\x02",
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
            "In a second game of rock-paper-\x01",
            "scissors, Noｱl was chosen as\x01",
            "the second game's referee...\x07\x00\x02",
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
            "This next match was\x01",
            "Lloyd and Wazy versus\x01",
            "Ilya and Randy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 49)
    Jump("loc_6FDF")

    label("loc_6E9C")

    TurnDirection(0x101, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#NThen, next up is Ilya.\x01",
            "Please, I'm counting on\x01",
            "you.\x02",
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
            "In a second game of rock-paper-\x01",
            "scissors, Wazy was chosen as\x01",
            "the second game's referee...\x07\x00\x02",
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
            "This next match was\x01",
            "Lloyd and Ilya versus\x01",
            "Randy and Noｱl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 69)
    Jump("loc_6FDF")

    label("loc_6FDF")

    Return()

    # Function_38_5C68 end

    def Function_39_6FE0(): pass

    label("Function_39_6FE0")

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
            "#6P#13409FMan, that was fun!\x02\x03",
            "#13400FChanging up the teams\x01",
            "was pretty fun too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FHaha. Playing two games\x01",
            "in a row was pretty\x01",
            "tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12803FYeah, but...\x02\x03",
            "#12809FIt's too bad you didn't\x01",
            "get the promised\x01",
            "fanservice scene.\x02\x03",
            "#12806FI was hoping Noｱl would\x01",
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
            "#6P#12904FHaha, seems like we got\x01",
            "really into beach\x01",
            "volleyball.\x02",
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
            "#6P#13006FRandy, Wazy... What are\x01",
            "you guys saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FI'm interested in Ilya's\x01",
            "overreaction, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12500FOh, that's right. Are\x01",
            "you guys thirsty?\x02\x03",
            "I could buy you\x01",
            "something at the stand,\x01",
            "if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FOh, how considerate,\x01",
            "little bro. Now what do\x01",
            "I want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12800FI think I heard about a\x01",
            "new juice you can buy at\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6P#13000FYeah, I heard about it\x01",
            "too.\x02\x03",
            "#13004FIt's called BelleCola,\x01",
            "and it's supposed to be\x01",
            "bubbly and refreshing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P#12902FHehe, that sounds pretty\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FThen, BelleColas for\x01",
            "everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FYes, please.\x02\x03",
            "#13404FWell, I'm not that\x01",
            "thirsty right now, so no\x01",
            "need to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FHaha, got it. I'll bring\x01",
            "them by later.\x02",
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

    # Function_39_6FE0 end

    def Function_40_761E(): pass

    label("Function_40_761E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80DB")

    ChrTalk(
        0x8,
        (
            "#5P#13302FOh, well if it isn't\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13502FHaha, good work out\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12504FYou guys are sunbathing,\x01",
            "huh.\x02\x03",
            "#12500FYou haven't swum in the\x01",
            "lake yet. Are you guys\x01",
            "having fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FYes. Even just relaxing\x01",
            "here is plenty fun.\x02\x03",
            "#13309FAnd I can chat with Elie\x01",
            "and Rixia, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602FAhaha. We're having fun\x01",
            "too... But we have a\x01",
            "small problem.\x02\x03",
            "#12606FCecil keeps pestering me,\x01",
            "asking "how are things\x01",
            "with Lloyd?" and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13509FY-Yeah, I'm shocked.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#12506FN-Now look here,\x01",
            "Cecil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FHaha. I'm curious, you\x01",
            "know?\x02\x03",
            "Sisters always have to\x01",
            "check up on their brothers'\x01",
            "relationships, you know.\x02\x03",
            "#13301FAnd I want to know who's\x01",
            "going to be your future\x01",
            "bride ASAP!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#12506FN-No no, stop that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13500F(Hmm, she's not all that\x01",
            "different from her\x01",
            "childhood friend Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#13302FLloyd, why don't you\x01",
            "sunbathe with us a bit?\x02\x03",
            "#13309FWe have an extra deck\x01",
            "chair, and we can chat a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12512FU-Uh, well, it's kind of\x01",
            "embarrassing butting in\x01",
            "like this.\x02\x03",
            "#12500FI'll have to pass this\x01",
            "time.\x02",
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
            "#12600FHaha, it's too late to\x01",
            "be getting all\x01",
            "embarrassed now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13503FThat's right. I want to\x01",
            "chat with you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12502FHaha. I'm happy to hear\x01",
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
            "#13309FIn exchange, would you\x01",
            "put sunscreen on us?\x02",
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
        "#12605FH-Hey, Cecil!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13506FThat's a bit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FHaha. It's fine, right? I mean\x01",
            "I have no problem with it.\x02\x03",
            "#13304FAnd Elie and Rixia, didn't you\x01",
            "say earlier you wanted to avoid\x01",
            "sunburn as much as possible?\x02\x03",
            "#13309FYou were the one who said "too\x01",
            "late to be getting all\x01",
            "embarrassed", didn't you, Elie.\x02",
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
            "#12613FAlright... Lloyd, please\x01",
            "go ahead.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        "#12P#12505FElie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12611FI-I mean, everyone else is\x01",
            "enjoying themselves. I\x01",
            "wouldn't want to interrupt.\x02\x03",
            "#12606FAnd it is true that I don't\x01",
            "want to burn.\x02\x03",
            "#12613FAnd I think you'd be better\x01",
            "at it than Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#13503FT-That's true.\x02\x03",
            "#13506FI put some on Ilya too\x01",
            "back at our hotel room.\x02\x03",
            "#13502FAnd, if it's Lloyd doing\x01",
            "it, I guess I'm not so\x01",
            "opposed to it.\x02",
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
            "#5P#13304FHaha. You see, Lloyd? You sister\x01",
            "and these lovely ladies are\x01",
            "specifically requesting you!\x02\x03",
            "#13302FSo you'll do it, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    SetScenarioFlags(0x15D, 0)
    Jump("loc_8113")

    label("loc_80DB")


    ChrTalk(
        0x8,
        (
            "#5P#13302FOh, Lloyd. Will you put\x01",
            "sunscreen on us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8113")

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
            "Put sunscreen on the girls\x01",      # 0
            "Refuse\x01",                          # 1
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
        (0, "loc_8185"),
        (1, "loc_818D"),
        (SWITCH_DEFAULT, "loc_8293"),
    )


    label("loc_8185")

    Call(0, 41)
    Jump("loc_8293")

    label("loc_818D")


    ChrTalk(
        0x101,
        (
            "#12P#12511FW-Wait just a moment. I\x01",
            "have to mentally\x01",
            "prepare!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FMy... Haha, it can't be\x01",
            "helped, I guess. In that\x01",
            "case, stop by later.\x02\x03",
            "#13304FBut please make it as\x01",
            "soon as possible. We'll\x01",
            "burn at this rate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 21500, -6000, 20700, 90)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearMapObjFlags(0x1, 0x1000)
    EventEnd(0x5)
    Jump("loc_8293")

    label("loc_8293")

    Return()

    # Function_40_761E end

    def Function_41_8294(): pass

    label("Function_41_8294")

    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#12P#12501FF-Fine. I'll do it\x01",
            "respectfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12611FRespectfully, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509FAhaha... There's this\x01",
            "strange tension in the\x01",
            "air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13300FHaha. I've got a\x01",
            "question for you right\x01",
            "off the bat.\x02\x03",
            "#13303FWho will you put it on\x01",
            "first?\x02",
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
            "#1KTo whom will you apply\x01",
            "sunscreen first?\x07\x00\x02",
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
        (0, "loc_846F"),
        (1, "loc_89A8"),
        (2, "loc_9018"),
        (SWITCH_DEFAULT, "loc_9707"),
    )


    label("loc_846F")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then... I'll\x01",
            "start with Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612FM-Me!?\x02\x03",
            "#12613F...I-It's fine... But\x01",
            "don't be weird, ok?\x02",
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

    def lambda_8631():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8631)

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
            "#6P#12613FY-Yeah. It was just a\x01",
            "bit cold, I was just\x01",
            "surprised.\x02\x03",
            "#12602FIt's fine, please\x01",
            "continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FAlright, then...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 9000)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(*sigh*, this is bad for\x01",
            "your heart...)\x02\x03",
            "#12508F(But Elie, you're really\x01",
            "pretty...)\x02\x03",
            "#12503F(Your pure white skin\x01",
            "and shiny pearl grey\x01",
            "hair...)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#6P#12612FH-Hey. You got quiet all\x01",
            "of a sudden.\x02\x03",
            "#12611FYou're not thinking\x01",
            "about anything lewd, are\x01",
            "you?\x02",
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
            "#12503F(If I'm careless,\x01",
            "Mariabell will sink me to\x01",
            "the bottom of this lake!!)\x02\x03",
            "#12501F(I've got to calm myself.\x01",
            "Think empty thoughts!)\x02",
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
            "#11P#N#13506FLloyd... Your face looks\x01",
            "like a Jizou statue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P#13309FHaha. After you finish\x01",
            "Elie, do Rixia and I\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_9707")

    label("loc_89A8")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then... I'll\x01",
            "start with Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FHaha, all right. Please\x01",
            "go ahead.\x02",
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
        "#11P#12500F...How is it, Cecil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304FYes, that's the way. Now\x01",
            "spread it thinly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12500FAlright, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304F...Haha. Somehow, this\x01",
            "brings back old\x01",
            "memories.\x02\x03",
            "#13302FWhen you were a kid,\x01",
            "we'd wash each other's\x01",
            "backs sometimes.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FGaaah, C-Cecil!! What're\x01",
            "you saying in front of\x01",
            "everyone!?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_63(0x8, 0xFFFFFE0C, 1700, 0x2, 0x7, 0x50, 0x1)

    def lambda_8C68():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8C68)

    ChrTalk(
        0x8,
        (
            "#6P#13306FEek!\x02\x03",
            "#13309F...Haha. Oh, Lloyd. No\x01",
            "touching in strange\x01",
            "places, ok?\x02",
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
            "#11P#12506F(Aah, jeez... You're too\x01",
            "defenseless, Cecil!!)\x02\x03",
            "#12508F(A-Also, when she's exposed\x01",
            "she's got this amazing\x01",
            "destructive energy...)\x02\x03",
            "#12506F(...Wait, what am I saying!?\x01",
            "I can't think about sister\x01",
            "Cecil that way!)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#13305FLloyd, what's wrong? It seems like\x01",
            "you've been applying it to the same\x01",
            "spot for some time...\x02\x03",
            "#13308F...Could I have gotten...fat?\x02\x03",
            "#13306FBecause I often receive pastries from\x01",
            "the patients and the head nurse, I end\x01",
            "up eating them without thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FN-No no, that's not true!!\x01",
            "You don't have to worry,\x01",
            "you're very pretty...\x02\x03",
            "#12506F...Ah, no, I mean...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#13309FHaha. Thank you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#12611F(Hmm... Sweet as\x01",
            "always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509F(Ahaha... It's just like\x01",
            "I'd heard.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9707")

    label("loc_9018")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FAlright then... Rixia,\x01",
            "I'll start with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13505FR-Right!\x02\x03",
            "#13503FUmm, I'm inexperienced,\x01",
            "but please take good\x01",
            "care of me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#12506FUmm... I think you're\x01",
            "making some kind of\x01",
            "mistake.\x02",
        )
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
        "#11P#12502FThere... H-How is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13503FAh, yes. I think you're doing it\x01",
            "right.\x02\x03",
            "#13506F*sigh*, thank you, really. Since\x01",
            "I'm in Arc-en-Ciel's performances,\x01",
            "I can't afford to get sunburned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FYeah, I suppose that's\x01",
            "true.\x02\x03",
            "#12505FOh, but... Didn't you\x01",
            "put sunscreen on Ilya?\x02\x03",
            "#12511FYou could've asked her\x01",
            "to─ ...Oh, wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13509FUmmm... Ahaha. In short, it's as\x01",
            "you think.\x02\x03",
            "#13506FIf I exposed myself to Ilya in such\x01",
            "a defenseless state, I can't even\x01",
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
            "#11P#12512F(She'd rather have me over the\x01",
            "lecherous Ilya, huh... What a\x01",
            "strange reason, though.)\x02\x03",
            "#12501F(...Even so, it's hard to tell\x01",
            "from her appearance, but Rixia\x01",
            "has quite the trained body.)\x02\x03",
            "#12508F(That she has such skills despite\x01",
            "these proportions... Maybe that's\x01",
            "what it means to be a "genius".\x02\x03",
            "#12503F(Above all, from this height, it\x01",
            "might be no exaggeration to call\x01",
            "her a dangerous weapon...)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#6P#13505FL-Lloyd? Umm, your\x01",
            "gaze...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FWah, s-sorry!\x02\x03",
            "#12512FW-Well, you see, it's not\x01",
            "like that. I was thinking\x01",
            "you're really trained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#N#12611F*sigh* ...I wonder why\x01",
            "boys are like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13309FHaha. Please do us when\x01",
            "you're finished with\x01",
            "Rixia, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9707")

    label("loc_9707")

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
            "#6P#12506F(Ah. Looking at it\x01",
            "again, it really is an\x01",
            "amazing view...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FAhhh... Thanks, Lloyd.\x01",
            "That was very relaxing.\x02\x03",
            "#13309FUhuhu, I might fall\x01",
            "asleep at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1P#12606FCecil, I think sleeping\x01",
            "like that would be\x01",
            "rather dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P#13509FAhaha... That might be\x01",
            "overstating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#13304FHaha, but it feels so\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#12500FAlright then, how about\x01",
            "some cold drinks to wake\x01",
            "everyone up?\x02",
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
            "#6P#12503F(In a way, this\x01",
            "experience was like a\x01",
            "dream, huh...)\x02\x03",
            "#12512F(Honestly, if I didn't\x01",
            "do this much, Aidios\x01",
            "would punish me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P#13505F...Lloyd?\x02",
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
            "#5P#13302FSure, that would be\x01",
            "great.\x02\x03",
            "#13309FOh, but you don't have\x01",
            "to hurry. We want you to\x01",
            "have fun too, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12500FSure, thanks. See you\x01",
            "guys later.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CB1")
    Call(0, 54)
    EventEnd(0x5)
    Jump("loc_9CC4")

    label("loc_9CB1")

    SetChrPos(0x0, 21500, -6000, 20700, 90)
    EventEnd(0x5)

    label("loc_9CC4")

    Return()

    # Function_41_8294 end

    def Function_42_9CC5(): pass

    label("Function_42_9CC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CDC")
    OP_A0(0xFE, 500, 0x0, 0x3)
    Jump("Function_42_9CC5")

    label("loc_9CDC")

    Return()

    # Function_42_9CC5 end

    def Function_43_9CDD(): pass

    label("Function_43_9CDD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A268")

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
            "#11P#12505F(T-They're concentrating\x01",
            "pretty hard on this,\x01",
            "aren't they...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200F...Grrowl... Woof.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EB6")
    Jump("loc_9F00")

    label("loc_9EB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9ED6")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F00")

    label("loc_9ED6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EF6")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F00")

    label("loc_9EF6")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F00")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FB6")
    Jump("loc_A000")

    label("loc_9FB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FD6")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A000")

    label("loc_9FD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FF6")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A000")

    label("loc_9FF6")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A000")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xB,
        "#12P#12705FOh, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13100FSomething wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FHaha, guess I\x01",
            "interrupted you.\x02\x03",
            "#12500FI was just wondering\x01",
            "what you guys were\x01",
            "making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FNo, no, don't worry\x01",
            "about it.\x02\x03",
            "#13109FWe're making a sand\x01",
            "castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FIn other words, "sand\x01",
            "crafts".\x02\x03",
            "#12706FBut it's not going so\x01",
            "well... Anything we make\x01",
            "keeps collapsing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FHmm, looks tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh! Since you're here,\x01",
            "why don't you help us\x01",
            "out, Lloyd?\x02",
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
            "#12P#12702FYes. With your help, we\x01",
            "might be able to make\x01",
            "some progress.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 1)
    Jump("loc_A4EA")

    label("loc_A268")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2F9")
    Jump("loc_A343")

    label("loc_A2F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A319")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A343")

    label("loc_A319")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A339")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A343")

    label("loc_A339")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A343")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3F9")
    Jump("loc_A443")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A419")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A443")

    label("loc_A419")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A439")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A443")

    label("loc_A439")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A443")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, Lloyd. Will you help\x01",
            "us make a sand castle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FPlease do. we might be\x01",
            "able to make some\x01",
            "progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Help build the sand castle\x01",      # 0
            "Refuse\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A64B")

    ChrTalk(
        0x101,
        (
            "#11P#12500FSure, alright. I'll do\x01",
            "my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FThat's our Lloyd! Thanks\x01",
            "a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHaha. I say that, but\x01",
            "I'm a total newbie at\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, I think we all\x01",
            "are.\x02\x03",
            "#12704FThen, let's get started.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 44)
    Call(0, 45)
    Jump("loc_A720")

    label("loc_A64B")


    ChrTalk(
        0x101,
        "#11P#12512FHmm, now isn't good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13106FHuh? No way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, let us know if you\x01",
            "change your mind.\x02\x03",
            "#12704FFran and I will do our\x01",
            "best until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)

    label("loc_A720")

    SetChrPos(0x0, 29920, -6000, 8910, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A749")
    Call(0, 54)

    label("loc_A749")

    EventEnd(0x5)
    Return()

    # Function_43_9CDD end

    def Function_44_A74C(): pass

    label("Function_44_A74C")

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
        "#6P#13100FHmm. It's coming along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12700FYes. Almost there.\x02",
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
        (
            "#12P#12706FThis is really\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FHmm. Maybe there's some\x01",
            "problem with the\x01",
            "strength of the sand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105FStrength?\x02\x03",
            "#13106FWe've been adding sand\x01",
            "and water to a bucket\x01",
            "and packing firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FBut it dries out when\x01",
            "you make something with\x01",
            "it, right?\x02\x03",
            "#12504FI heard it's better to\x01",
            "add water a little at a\x01",
            "time .\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12705FI see... That makes\x01",
            "sense.\x02\x03",
            "#12702FAlright then, how much\x01",
            "water should we add at a\x01",
            "time.\x02",
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
            "#1KHow much water will you\x01",
            "add?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Plenty\x01",             # 0
            "A little more\x01",      # 1
            "Just a bit\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABE8")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500FJust a little, I\x01",
            "think... Just enough to\x01",
            "get it wet.\x02\x03",
            "#12504FIf you add too much, the\x01",
            "strength will decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FNow that you say it, I\x01",
            "think I get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FThen, let's try doing as\x01",
            "Lloyd says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD67")

    label("loc_ABE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8A")

    ChrTalk(
        0x101,
        (
            "#11P#12500FWouldn't it be best to\x01",
            "make it while boldly\x01",
            "adding plenty of water?\x02\x03",
            "#12504FDoing it that way raises\x01",
            "its strength... I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0E")

    label("loc_AC8A")


    ChrTalk(
        0x101,
        (
            "#11P#12500FWouldn't it be best to\x01",
            "make it using a little\x01",
            "more water?\x02\x03",
            "#12504FDoing it that way raises\x01",
            "its strength... I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD0E")


    ChrTalk(
        0xC,
        "#6P#13105FIs that how it's done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FWell, let's try doing it\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD67")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF0E")
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#12P#12702FIt's almost done!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FYeah, thanks to Lloyd's\x01",
            "advice of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHaha, I'm happy to hear\x01",
            "you say that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702FHaha... Alright then, it's\x01",
            "finally time for the finishing\x01",
            "touches.\x02\x03",
            "We need to improve the details\x01",
            "on the main castle... Lloyd,\x01",
            "can we ask you to do it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0C5")

    label("loc_AF0E")


    ChrTalk(
        0xB,
        "#12P#12700FIt's nearly done, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xC,
        (
            "#6P#13105FS-Somehow water is\x01",
            "coming out all over the\x01",
            "place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12506F(H-Hmm... I should've\x01",
            "known that was too much\x01",
            "water...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FWell, I don't think it will\x01",
            "collapse for now... Let's\x01",
            "apply the finishing touches.\x02\x03",
            "#12702FWe need to improve the details\x01",
            "on the main castle... Lloyd,\x01",
            "can we ask you to do it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C5")


    ChrTalk(
        0x101,
        "#11P#12500FAlright. Leave it to me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FWe're betting everything\x01",
            "on you, Lloyd! We're\x01",
            "counting on you!\x02",
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
            "Anyway, I've gotta do\x01",
            "this.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12501F(Alright. We used water to\x01",
            "strengthen the sand, but in\x01",
            "the end it's just sand.)\x02\x03",
            "#12503F(I have to control the\x01",
            "speed and power. How should\x01",
            "I do this...?)\x02",
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
            "#1KWhat speed and power\x01",
            "should Lloyd use?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Slowly/Gently\x01",           # 0
            "Slowly/Forcefully\x01",       # 1
            "Quickly/Gently\x01",          # 2
            "Quickly/Forcefully\x01",      # 3
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
        (0, "loc_B328"),
        (1, "loc_B36D"),
        (2, "loc_B3B6"),
        (3, "loc_B406"),
        (SWITCH_DEFAULT, "loc_B450"),
    )


    label("loc_B328")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it slowly, yet gently!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B450")

    label("loc_B36D")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it slowly, yet\x01",
            "forcefully!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B450")

    label("loc_B3B6")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it quickly, yet gently!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B450")

    label("loc_B406")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright... I'll detail\x01",
            "it quickly, yet\x01",
            "forcefully!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B450")

    label("loc_B450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B46E")
    Jump("loc_B80F")

    label("loc_B46E")

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
        "#12P#12705FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FAww... Ahaha. It went\x01",
            "down.\x02",
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
            "#11P#12505FWell, umm, what can I\x01",
            "say...\x02\x03",
            "#12506F...I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F...Well, it can't be\x01",
            "helped.\x02\x03",
            "#12700FLet's rebuild it from\x01",
            "square one.\x02\x03",
            "Mr. Lloyd, please\x01",
            "support Fran and I.\x02",
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
            "#6P#13109FMr. Lloyd, please don't\x01",
            "feel down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B720")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(The amount of water\x01",
            "seemed right, but...)\x02\x03",
            "(*sigh*... This isn't\x01",
            "good.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B80F")

    label("loc_B720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78D")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(I thought I did it the\x01",
            "right way, but...)\x02\x03",
            "(*sigh*... This isn't\x01",
            "good.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B80F")

    label("loc_B78D")


    ChrTalk(
        0x101,
        (
            "#11P#12506F(I can only think both the\x01",
            "amount of water and the way\x01",
            "I did it were wrong, but...)\x02\x03",
            "(*sigh*... This isn't good.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B80F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x2)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#12500FPhew... That should do\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#6P#13100FIt's... It's finally\x01",
            "done!!\x02\x03",
            "#13109FKya! We did it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9B6")
    OP_2C(0xA5, 0x1)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12704FHow moving. Good work,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHaha, don't mention it.\x01",
            "It's because you two\x01",
            "worked so hard, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FNo, no! It's because of\x01",
            "you, Lloyd! Thank you so\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA93")

    label("loc_B9B6")

    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F...In any case, I'm\x01",
            "glad. Although it took a\x01",
            "while to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12506FI-I'm really sorry for\x01",
            "all that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FAhaha. I'm telling you,\x01",
            "it's fine. We managed to\x01",
            "complete it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA93")

    TurnDirection(0xB, 0xD, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F#5PZeit helped too.\x02\x03",
            "#12704FHe got sand and water\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        "#11P#12500F#5PHaha, good work, Zeit.\x02",
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
        "#6P#13105FA... name?\x02",
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
            "#12P#12703FI see. Hmm, then...\x02\x03",
            "#12700FHow about "Mishy\x01",
            "Castle"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105FAwww, no fair, Tio!\x02\x03",
            "#13109FIn that case, I'm going\x01",
            "with "Ban Ban Castle"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FMishy is more well\x01",
            "known, but...\x02\x03",
            "#12503FI think Ban Ban was the\x01",
            "name of your favorite\x01",
            "stuffed animal, Fran.\x02\x03",
            "#12509FHaha... I guess I like\x01",
            "both names.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FHowever, the same castle\x01",
            "can't have two names.\x02\x03",
            "#12700FWhy don't we have Lloyd\x01",
            "decide which is better?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FYeah, I like it!\x02\x03",
            "#13109FYou'll decide it, Lloyd!\x01",
            "No objections! Give it\x01",
            "to us straight!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(T-This is a heavy\x01",
            "responsibility.)\x02\x03",
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
            "#1KWhat will you name the\x01",
            "castle?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Mishy Castle\x01",        # 0
            "Ban Ban Castle\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0A9")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#5PWell, since we're at\x01",
            "Michelam...\x02\x03",
            "#12500FHow about we go with\x01",
            ""Mishy Castle".\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13106FHmm. That does make\x01",
            "sense, now that I think\x01",
            "about it.\x02\x03",
            "#13102FIt can't be helped. I\x01",
            "have to hand this one to\x01",
            "Tio.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702FHaha... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1D3")

    label("loc_C0A9")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#11PHmm. We'll be able to\x01",
            "see Mishy later all we\x01",
            "like, so...\x02\x03",
            "#12500FIsn't "Ban Ban Castle" a\x01",
            "nice name for it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F...Hmm, you have a\x01",
            "point.\x02\x03",
            "#12702FWell alright, we'll go\x01",
            "with Fran's suggestion\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        "#6P#13109FHaha, thanks Tio!\x02",
    )

    CloseMessageWindow()

    label("loc_C1D3")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#12509FHaha, well that was\x01",
            "settled peacefully.\x02\x03",
            "#12505FThat's right... Tio,\x01",
            "Fran, are you guys\x01",
            "getting thirsty?\x02\x03",
            "#12500FIf you like, I can bring\x01",
            "you refreshments later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FLet me think...\x02\x03",
            "#12700FI want their shaved ice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, me too!\x02\x03",
            "#13109FWill you get one for\x01",
            "each of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12509FYeah, leave it to me.\x02\x03",
            "#12500FFor Zeit... Will a hot\x01",
            "dog be ok?\x02",
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
            "#12P#12702F"Please", he says.\x02\x03",
            "#12703FOh, but there's no need\x01",
            "to rush. We're good for\x01",
            "now.\x02\x03",
            "#12702FI want you to have fun\x01",
            "too, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12502FHaha, roger that.\x02",
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

    # Function_44_A74C end

    def Function_45_C49E(): pass

    label("Function_45_C49E")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_END)), "loc_C4BB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_END)), "loc_C4CE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_C4E1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C528")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_C528")

    Return()

    # Function_45_C49E end

    def Function_46_C529(): pass

    label("Function_46_C529")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA28")

    ChrTalk(
        0xE,
        (
            "#13209F#6PWaaah... Sully's is so\x01",
            "pretty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#11PHehe, it's no big deal.\x02\x03",
            "#13600FBut this stone... I've\x01",
            "never seen anything like\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PYou guys are back. What\x01",
            "are you up to?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C696():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C696)
    Sleep(50)

    def lambda_C6A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_C6A6)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xE,
        "#13210F#12PAh, Lloyd. Look at this!\x02",
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
            "#12500F#5PWow, it's round and pure\x01",
            "white... Almost like a\x01",
            "jewel.\x02\x03",
            "#12505FWhere did you get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13600F#12PShorty here picked it up\x01",
            "earlier when we were\x01",
            "swimming.\x02\x03",
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
            "#12500F#5PHmm. The sand here was\x01",
            "carried in from another\x01",
            "country.\x02\x03",
            "#12503FSo there should be more\x01",
            "of them around here.\x02\x03",
            "#12500FThere might be ones even\x01",
            "bigger than that buried\x01",
            "in sand.\x02",
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
            "for the white stones!\x02\x03",
            "#13209FAnd whoever has the\x01",
            "biggest one will be the\x01",
            "winner!\x02",
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
            "#13604FYou're playing too, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 6)
    Jump("loc_CAAE")

    label("loc_CA28")


    def lambda_CA2D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_CA2D)
    Sleep(50)

    def lambda_CA3D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CA3D)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xF,
        "#13600F#12PYou want to join us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13202F#12PLet's look for the\x01",
            ""White Stones" together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Start looking\x01",      # 0
            "Refuse\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCFF")

    ChrTalk(
        0x101,
        "#12500F#5PSure, I'll play along.\x02",
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
            "#13600F#12PTell me once you've\x01",
            "found a white stone.\x02\x03",
            "#13604FThen we'll compare sizes\x01",
            "and whoever has the\x01",
            "biggest will win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509F#5PHaha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13201F#12PAlllright... Start!\x02\x03",
            "#13200FKeA will definitely find\x01",
            "the biggest one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#12PHmph, as if I'd lose to\x01",
            "you guys.\x02",
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
    Jump("loc_CDD6")

    label("loc_CCFF")


    ChrTalk(
        0x101,
        "#12512F#5PHmm. I won't do it now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13205F#12POh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606F#12PTch, you're no fun.\x02\x03",
            "#13600FWell, tell me when you\x01",
            "feel like it. We'll let\x01",
            "you join then.\x02",
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

    label("loc_CDD6")

    EventEnd(0x5)
    Return()

    # Function_46_C529 end

    def Function_47_CDD9(): pass

    label("Function_47_CDD9")

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
            "#12503FHmm, this one's a little\x01",
            "small.\x02\x03",
            "I think there's bigger\x01",
            "ones around.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x15C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_47_CDD9 end

    def Function_48_CE81(): pass

    label("Function_48_CE81")

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
            "#12505FI found one, but... it's\x01",
            "small.\x02\x03",
            "Should I look around a\x01",
            "little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x15C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_48_CE81 end

    def Function_49_CF29(): pass

    label("Function_49_CF29")

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
            "#12500FIt's a size that cleanly\x01",
            "fits into the palm the\x01",
            "hand.\x02\x03",
            "#12503FIt seems like both KeA\x01",
            "and Sully have found one\x01",
            "of about this size...\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x15C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_CF29 end

    def Function_50_D010(): pass

    label("Function_50_D010")

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
            "#12503FThis one's rather big.\x02\x03",
            "#12500FIt might be a contender.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x15C, 4)
    TalkEnd(0xFF)
    Return()

    # Function_50_D010 end

    def Function_51_D0AB(): pass

    label("Function_51_D0AB")

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
            "#12505FOh!? It's the size of a\x01",
            "crystal ball!\x02\x03",
            "#12509FHaha. If it's this big,\x01",
            "I can hardly lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x15C, 5)
    TalkEnd(0xFF)
    Return()

    # Function_51_D0AB end

    def Function_52_D167(): pass

    label("Function_52_D167")

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
        "#12605FOh, Lloyd. What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12500FI'm playing with KeA and\x01",
            "Sully.\x02",
        )
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
            "Lloyd reached under the\x01",
            "deck chair.\x07\x00\x02",
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
        "#12612FW-Wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12502FGot it!\x02",
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
            "in a place like this.\x02\x03",
            "#12504FBut, it's huge. I'll\x01",
            "definitely win with\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12611FY-You... What were you\x01",
            "thinking, suddenly\x01",
            "reaching down there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12511FAh... Sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12606FUgh, seriously.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x15C, 6)
    EventEnd(0x5)
    Return()

    # Function_52_D167 end

    def Function_53_D415(): pass

    label("Function_53_D415")

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
            "#12P#13600FAlright, let's compare\x01",
            "sizes.\x02\x03",
            "#13603FBring out your biggest\x01",
            "one on the count of\x01",
            "three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12500FYeah, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13210FI'm all set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13601FAlright, here we go.\x02",
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
        "#5P#12500F#4SThree!!#3S\x02",
    )


    ChrTalk(
        0xE,
        "#3P#13200F#4SThree!!#3S\x02",
    )


    ChrTalk(
        0xF,
        "#4P#13600F#4SThree!!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF9D")
    OP_2C(0xA5, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13210FWaaaaaa... Lloyd's white\x01",
            "stone, it's huge!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13601FTch... I can't believe\x01",
            "you found one like that.\x02\x03",
            "#13606FDamn. Guess I lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12502FHaha, looks like I win,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13606FTch, such a sore winner.\x01",
            "How childish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#12506F...Look who's talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12P#13200FBut it's so big and\x01",
            "pretty.\x02\x03",
            "#13206FKeA wanted one like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FYeah... I'll keep\x01",
            "looking too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA47")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FHaha. Then, I'll give\x01",
            "you guys this "White\x01",
            "Stone".\x02",
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
            "#12P#13605FY-You sure? And you've\x01",
            "got two of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, I just picked up\x01",
            "another about the same\x01",
            "size.\x02\x03",
            "#12509FSince we're here at the\x01",
            "beach, how about something\x01",
            "to remember this by?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave KeA and Sully\x01",
            "a big "White Stone"\x01",
            "each.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#12P#13612FH-Hmph... Thanks.\x02",
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
    Jump("loc_DF98")

    label("loc_DA47")


    ChrTalk(
        0x101,
        (
            "#5P#12500F(That's right, since\x01",
            "we're here... Should I\x01",
            "give it to one of them?)\x02",
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
            "#1KTo whom will you give\x01",
            "the "White Stone"?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD76")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FAlright then, how about\x01",
            "I give you this white\x01",
            "stone as a present, KeA?\x02",
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
            "#12509FI think this will make a\x01",
            "nice memento of our\x01",
            "beach vacation for you.\x02",
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
        "#12P#13606F#11PTch, how nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FSorry, Sully. You're older\x01",
            "than KeA, so can I ask you\x01",
            "to grin and bear it?\x02",
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
            "#12P#13612FI-I didn't want it that\x01",
            "badly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber(0x32C, 1)
    Jump("loc_DF98")

    label("loc_DD76")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FAlright then, I'll give\x01",
            "this "White Stone" to\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#12P#13605FHuh... Y-You sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, of course.\x02\x03",
            "#12509FI think this will make a\x01",
            "nice memento of our\x01",
            "beach vacation for you.\x02",
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
        "#12P#13612FH-Hmph... Thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#12P#13209F#6PHow nice, eh, Sully? Let\x01",
            "me touch it later, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FSorry, KeA. How about I\x01",
            "buy you a new book when\x01",
            "we get back instead?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        "#12P#13200FAh, yeah! I can't wait!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SubItemNumber(0x32C, 1)

    label("loc_DF98")

    Jump("loc_E2A4")

    label("loc_DF9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E0BF")
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13205FOoh, they're all the\x01",
            "same size!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FYeah... It looks like\x01",
            "their sizes aren't that\x01",
            "different, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FThen, looks like it's a\x01",
            "draw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13606FTch, such a boring\x01",
            "result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12512FHaha, don't say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2A4")

    label("loc_E0BF")

    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13200FWaah, Lloyd's stone is\x01",
            "tiny and cute!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FYeah... It's pretty\x01",
            "small.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12512FH-Hahaha... Looks like\x01",
            "I've lost.\x02\x03",
            "#12500FYour stones look about the\x01",
            "same size, so you guys are\x01",
            "the winners this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13209FYaay, we did iiit!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13606FTch. You're awfully calm\x01",
            "about all of this.\x02\x03",
            "#13602FHaha, but deep down, I\x01",
            "bet you're ashamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12506FGuh... I-I'm telling\x01",
            "you, that's not true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2A4")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12500FThat's right... KeA,\x01",
            "Sully, do want something\x01",
            "cold or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12P#13200FHuh? You'll get it for\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12504FYeah. You've been playing in the\x01",
            "water this whole time, and you\x01",
            "must be getting pretty tired.\x02\x03",
            "#12500FIf there's anything you want to\x01",
            "eat or drink, just say so.\x02",
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
        "#5P#12500FIce cream, huh? Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13604FMe too, then.\x02\x03",
            "#13600FOh, but I want to play a\x01",
            "bit more, so don't bring\x01",
            "them right away, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FYeah, got it. See you\x01",
            "guys later.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E0")
    Call(0, 54)

    label("loc_E5E0")

    EventEnd(0x5)
    Return()

    # Function_53_D415 end

    def Function_54_E5E3(): pass

    label("Function_54_E5E3")

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
            "#12500FEveryone's having a good time. I\x01",
            "think it's time for me to take it\x01",
            "easy.\x02\x03",
            "#12503F...But I'm kind of thirsty too.\x02\x03",
            "#12500FI did promise to buy cold food and\x01",
            "drink for everyone. I think it's\x01",
            "about time I headed to the shop.\x02\x03",
            "It's just up the stairs. I'll\x01",
            "check it out.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    SetScenarioFlags(0x15E, 3)
    Return()

    # Function_54_E5E3 end

    def Function_55_E75D(): pass

    label("Function_55_E75D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA63")

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
            "#12502F#12PHaha, yeah. Everyone's\x01",
            "having a good time.\x02\x03",
            "Actually, I need to\x01",
            "order quite a few\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I just finished getting\x01",
            "everything ready for you.\x01",
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
            "#12506F#12P...Ah. Come to think of\x01",
            "it, I left my wallet in\x01",
            "the locker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Oh, don't worry about\x01",
            "paying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Mariabell said to give you guys\x01",
            "anything you wanted on the\x01",
            "house during your reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#12PR-Really!?\x02\x03",
            "#12512FShe's nothing if not\x01",
            "thorough... I could\x01",
            "never hope to match her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. Your thanks are\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Then, will you be\x01",
            "ordering?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EACA")

    label("loc_EA63")


    ChrTalk(
        0x22,
        (
            "During your reservation,\x01",
            "anything you want is on\x01",
            "the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Will you be ordering\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EACA")

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
            "[Order]\x01",       # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE80")

    ChrTalk(
        0x101,
        (
            "#12500F#12PThanks. We're counting\x01",
            "on you.\x02\x03",
            "#12503FUmm, 4 BelleColas, 3\x01",
            "non-alcoholic\x01",
            "cocktails...\x02\x03",
            "#12500F2 ice creams, 2 shaved\x01",
            "ices... Oh, and one hot\x01",
            "dog please.\x02",
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
            "Could you possibly be... the type\x01",
            "that's overly soft hearted to the\x01",
            "point of self-destruction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#12PN-No, haha... I don't\x01",
            "think so.\x02",
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
            "─And so, everyone had a fun time\x01",
            "at the beach.\x02\x03",
            "After that, Lloyd and the others\x01",
            "enjoyed a watermelon splitting\x01",
            "game together.\x02\x03",
            "Later, as they enjoyed lunchboxes\x01",
            "delivered by the hotel, their\x01",
            "excitement began to build.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15E, 4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_END)), "loc_EE3D")
    SubItemNumber(0x32B, 1)

    label("loc_EE3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_END)), "loc_EE4B")
    SubItemNumber(0x32B, 1)

    label("loc_EE4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_END)), "loc_EE59")
    SubItemNumber(0x329, 1)

    label("loc_EE59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_END)), "loc_EE67")
    SubItemNumber(0x329, 1)

    label("loc_EE67")

    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_EEE8")

    label("loc_EE80")


    ChrTalk(
        0x101,
        "#12500F#12PNo, I'm good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Well, please do so\x01",
            "before your reservation\x01",
            "ends.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EEE8")

    SetChrPos(0x0, -6770, -1500, 8450, 90)
    OP_4C(0x22, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_55_E75D end

    def Function_56_EF00(): pass

    label("Function_56_EF00")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF32")
    SetScenarioFlags(0x31, 2)

    label("loc_EF32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EF78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_EF72")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EF67")
    Sound(2499, 255, 100, 0)
    Jump("loc_EF6D")

    label("loc_EF67")

    Sound(3537, 255, 100, 0)

    label("loc_EF6D")

    Jump("loc_EF78")

    label("loc_EF72")

    Sound(3344, 255, 100, 0)

    label("loc_EF78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F22F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_EFED")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EFCD"),
        (SWITCH_DEFAULT, "loc_EFDE"),
    )


    label("loc_EFCD")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_EFE8")

    label("loc_EFDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EFE8")

    Jump("loc_F22A")

    label("loc_EFED")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F01F")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_F01F")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F053"),
        (1, "loc_F157"),
        (2, "loc_F1E8"),
        (SWITCH_DEFAULT, "loc_F220"),
    )


    label("loc_F053")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F084")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F094")

    label("loc_F084")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F094")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0EA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0EA")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F10D")
    Sound(461, 0, 100, 0)

    label("loc_F10D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F12D")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_F13D")

    label("loc_F12D")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_F13D")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_EF78")

    label("loc_F157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F1C9")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F18C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F1A4")

    label("loc_F18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F19F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F1A4")

    label("loc_F19F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F1A4")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F1E3")

    label("loc_F1C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F1D9")
    OP_AF(0xFB)
    Jump("loc_F1E3")

    label("loc_F1D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1E3")

    Jump("loc_F22A")

    label("loc_F1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F201")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F21B")

    label("loc_F201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F211")
    OP_AF(0xFB)
    Jump("loc_F21B")

    label("loc_F211")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F21B")

    Jump("loc_F22A")

    label("loc_F220")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F22A")

    Jump("loc_EF78")

    label("loc_F22F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_EF00 end

    def Function_57_F23D(): pass

    label("Function_57_F23D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F259")
    Jump("loc_11A22")

    label("loc_F259")

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

    def lambda_F5BE():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F5BE)
    Sleep(0)

    def lambda_F5D6():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F5D6)
    Sleep(0)

    def lambda_F5EE():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F5EE)
    Sleep(0)
    Sleep(5500)
    Sound(2757, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#12809F#5P#10A#4SWhoo!!\x02",
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
            "#12509FIt's my first time at a\x01",
            "beach, but I didn't think\x01",
            "it would be this pretty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12904F#5PBeaches are normally on the\x01",
            "coast, so the sand isn't\x01",
            "usually this white.\x02\x03",
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

    def lambda_F7ED():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F7ED)
    Sleep(50)

    def lambda_F7FD():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F7FD)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12511F#12PSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12806F#6PI can hardly believe\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12909F#5PHaha, it reminds you of\x01",
            "IBC's asset strength all\x01",
            "over again.\x02\x03",
            "#12900FBut shouldn't we prepare\x01",
            "things before the girls\x01",
            "come?\x02",
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
            "#12504F#12PI see. I think I\x01",
            "remember seeing them in\x01",
            "a magazine.\x02\x03",
            "#12500FAlright. Let's split up\x01",
            "and get everything\x01",
            "ready.\x02",
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
        "#12504F#12PPhew, that should do it.\x02",
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
            "#12909FWell then, I guess I'll\x01",
            "take a break.\x02",
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
            "#12801F#11PIt seems there's someone\x01",
            "who fools around more\x01",
            "than even me.\x02",
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
            "#13209F#11PAmazing! It's pure\x01",
            "white!\x02",
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
            "#12705F#11PIndeed... How\x01",
            "surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602F#11PThat Bell... Just when\x01",
            "did she make something\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xC,
        "#13109F#6PC'mon Noｱl, hurry!\x02",
    )

    CloseMessageWindow()
    OP_68(16000, -5000, -2500, 4000)

    def lambda_FE49():

        label("loc_FE49")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_FE49")

    QueueWorkItem2(0xE, 2, lambda_FE49)

    def lambda_FE5B():

        label("loc_FE5B")

        TurnDirection(0xFE, 0x12, 400)
        Yield()
        Jump("loc_FE5B")

    QueueWorkItem2(0xA, 2, lambda_FE5B)

    def lambda_FE6D():

        label("loc_FE6D")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_FE6D")

    QueueWorkItem2(0xB, 2, lambda_FE6D)

    def lambda_FE7F():

        label("loc_FE7F")

        TurnDirection(0xFE, 0x12, 600)
        Yield()
        Jump("loc_FE7F")

    QueueWorkItem2(0xC, 2, lambda_FE7F)
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
            "#13012F#5POh, Fran. The beach\x01",
            "isn't going anywhere you\x01",
            "know.\x02",
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

    def lambda_1002D():
        OP_9B(0x0, 0xE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1002D)
    Sleep(50)

    def lambda_10045():
        OP_9B(0x0, 0xC, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10045)
    Sleep(50)

    def lambda_1005D():
        OP_9B(0x0, 0xA, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1005D)
    Sleep(50)

    def lambda_10075():
        OP_9B(0x0, 0xB, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10075)
    Sleep(50)

    def lambda_1008D():
        OP_9B(0x0, 0x12, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1008D)
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
        (
            "#3613V#30WEhehe, sorry for the\x01",
            "wait.\x02",
        )
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
            "#3395V#30WHaha, you even got the\x01",
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
        "#2677V#30WHow thoughtful.\x02",
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

    def lambda_103EF():
        OP_98(0xFE, 0xFFFFFF9C, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_103EF)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1041E():
        OP_98(0xFE, 0xFFFFFF6A, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1041E)
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
            "#2716V#40WC'mon Noｱl.\x01",
            "#30WSince we're here, you've got\x01",
            "to put yourself out there!\x02",
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
            "#3516V#30WH-Hey! Don't push so\x01",
            "hard!\x02",
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
        "#12809F#11PHoho! Not bad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12902F#11PWow, you all look great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12609F#6PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12706F#6PI'm not too confident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13109F#5PEhehe. Hey Lloyd.\x02\x03",
            "Who looks the best in\x01",
            "their swimsuit, huh?\x02",
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
            "#12902F#5PHehe, what's wrong?\x01",
            "You've been staring for\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#12809F#5PHahaha. Too much\x01",
            "excitement for ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#11PHaha... Yeah, it's a bit\x01",
            "much.\x02\x03",
            "#12502F#11PYou guys all look so\x01",
            "good... I'm speechless.\x02\x03",
            "#12509FYou could even be in a\x01",
            "photo shoot or\x01",
            "something.\x02",
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
        "#13106F#5PHmph, that's our Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12711F#6PDefinitely lacking tact.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12505F#11PHuh?\x02",
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
            "#12806F#5P(This guy... I swear\x01",
            "I'll kill him one day.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12902F#5P(Well, that's how men\x01",
            "are, too.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Woman's Voice",
        (
            "Hey there! Sorry for the\x01",
            "wait.\x02",
        )
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
        (
            "#13405F#11PWoah! This is\x01",
            "incredible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#13309F#11PHaha... It's like heaven\x01",
            "on earth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PThe sand is pure white!\x02",
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

    def lambda_10E26():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10E26)

    def lambda_10E3B():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10E3B)

    def lambda_10E50():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10E50)

    def lambda_10E65():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_10E65)

    def lambda_10E7A():

        label("loc_10E7A")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_10E7A")

    QueueWorkItem2(0xE, 2, lambda_10E7A)

    def lambda_10E8C():

        label("loc_10E8C")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_10E8C")

    QueueWorkItem2(0xA, 2, lambda_10E8C)

    def lambda_10E9E():

        label("loc_10E9E")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_10E9E")

    QueueWorkItem2(0xB, 2, lambda_10E9E)

    def lambda_10EB0():

        label("loc_10EB0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10EB0")

    QueueWorkItem2(0x12, 2, lambda_10EB0)

    def lambda_10EC2():

        label("loc_10EC2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10EC2")

    QueueWorkItem2(0xC, 2, lambda_10EC2)
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
        (
            "Haha, sorry for the\x01",
            "wait.\x02",
        )
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
            "Oh, surrounded by cuties\x01",
            "already, I see.\x02",
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
            "ready for us.\x02",
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
            "I would have done it if\x01",
            "you asked, y'know.\x02",
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
        "#12606F#5PS-Somehow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13012F#11P#NPretty... Or maybe\x01",
            "overwhelming?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#12706F#5PLike they have a\x01",
            "different aura... That\x01",
            "sort of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#13101F#11PA-Amazing...\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13402F#6PYou guys are looking\x01",
            "pretty good yourselves.\x02\x03",
            "#13409FYeah, I approve㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#13304F#12P*giggle*, that's right.\x02\x03",
            "#13302FElie, you're as\x01",
            "glamorous as I thought.\x02\x03",
            "#13309FAnd Tio and KeA, I wanna\x01",
            "hug you both㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12609F#5PA-Amazing...\x02",
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
            "#13509F#11PHaha... But this is\x01",
            "really is a beautiful\x01",
            "beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13604F#11PWell, not too bad I\x01",
            "guess.\x02\x03",
            "#13601F─Hey guys! How long are\x01",
            "you gonna stand there\x01",
            "and stare for!?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x10)
    OP_64(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_115D2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_115D2)

    def lambda_115DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_115DF)

    def lambda_115EC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_115EC)

    def lambda_115F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_115F9)

    def lambda_11606():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11606)

    def lambda_11613():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11613)

    def lambda_11620():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11620)
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
        "#12511F#6P#NHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12806F#12P#NWhoa, careful. A moment\x01",
            "longer and you've have\x01",
            "gone to the other side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#12711F#5PMen are so simple\x01",
            "minded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#12PCompared to women, men\x01",
            "are simple creatures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13106F#11PHmm... We're gonna lose\x01",
            "at this rate.\x02\x03",
            "#13101FLet's do our best, Noｱl!\x02",
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
            "Then, after some warm-up\x01",
            "exercises, each of them enjoyed\x01",
            "the beach in their own way.\x02\x03",
            "Lloyd, together with Rixia,\x01",
            "gave KeA and Sully swimming\x01",
            "lessons.\x07\x00\x02",
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

    label("loc_11A22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D40")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B71")
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
    Jump("loc_11BD0")

    label("loc_11B71")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_11BD0")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C37")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_11C6F")

    label("loc_11C37")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_11C6F")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_11CC0")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_11D2A")

    label("loc_11CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_11CFC")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_11D2A")

    label("loc_11CFC")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_11D2A")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_11D40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D9F")
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

    label("loc_11D9F")

    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DF5")
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

    label("loc_11DF5")

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
            "#12502F#5POh, that's really good,\x01",
            "KeA.\x02\x03",
            "#12509FJust keep going like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209F#12PEhehe, really?\x02\x03",
            "#13201FAh... I think I get it.\x02\x03",
            "#13210FLet go of me, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PY-You're sure?\x02\x03",
            "#12501FOk then─\x02",
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

    def lambda_1205F():

        label("loc_1205F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1205F")

    QueueWorkItem2(0x101, 2, lambda_1205F)
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
        "#13505F#11PWow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#5PRight!\x02\x03",
            "#12502FKeA, you've swum before,\x01",
            "right?\x02",
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
            "Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#5PHaha. Sure, sure.\x02\x03",
            "#13502FHmm, you're relying too\x01",
            "much on your upper body.\x02",
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

    def lambda_121FD():

        label("loc_121FD")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_121FD")

    QueueWorkItem2(0x9, 2, lambda_121FD)
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
            "#12509F#5PYou guys are fast\x01",
            "learners.\x02",
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
            "being able to do this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#13210F#12P#NHey Sully!\x02\x03",
            "Let's swim out to that\x01",
            "rock!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#13611F#11P#NW-Why do I have to?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12509F#5PHaha, be careful.\x02\x03",
            "#12500FDon't go past that rock.\x01",
            "That goes for both of\x01",
            "you. Ok, guys?\x02",
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
            "#13607F#11P#NOh, fine! I'll go with\x01",
            "you, alright!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(225, 20, 0, 5000)
    SetCameraDistance(13000, 5000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1243D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12454")
    Sleep(1)
    Jump("loc_1243D")

    label("loc_12454")

    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xE, 64510, -7460, 28680, 75)
    SetChrPos(0xF, 62580, -7430, 29030, 75)

    def lambda_1249A():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1249A)

    def lambda_124AF():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_124AF)
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
        (
            "#12512F#11PHmm. Think they'll be\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PHaha, it's pretty shallow\x01",
            "around here, so they'll\x01",
            "be fine either way.\x02\x03",
            "#13502FBut KeA... She's amazing.\x02\x03",
            "It looked like she got\x01",
            "the hang of it in an\x01",
            "instant.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12504F#6PMaybe her body remembers\x01",
            "how to swim from before.\x02\x03",
            "#12500FSully's pretty amazing\x01",
            "too.\x02\x03",
            "She said she's never\x01",
            "once gone swimming\x01",
            "before now.\x02",
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
            "Arc-en-Ciel's performance\x01",
            "is being updated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13505F#11PYes, well it's still the\x01",
            "same "Golden Sun, Silver\x01",
            "Moon".\x02\x03",
            "#13502FBut we've arranged it so\x01",
            "Sully will appear as a\x01",
            "third "princess".\x02\x03",
            "#13509FShe's been added to all\x01",
            "of the main scenes.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_129EA")

    ChrTalk(
        0x101,
        (
            "#12511F#6PThat's amazing...\x02\x03",
            "#12512FI can't believe she's\x01",
            "getting such a major role\x01",
            "this soon after we met her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PHaha, me too.\x02\x03",
            "#13510FIt's probably because of\x01",
            "Ilya's guidance and\x01",
            "Sully's own tenacity.\x02\x03",
            "#13508FMaybe more than even my\x01",
            "own, this whole time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B23")

    label("loc_129EA")


    ChrTalk(
        0x101,
        (
            "#12505F#6PThat's amazing...\x02\x03",
            "#12501FI heard she rebelled\x01",
            "against Ilya at first and\x01",
            "tried to cause an incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13504F#11PIt wasn't something as\x01",
            "big as an incident,\x01",
            "but...\x02\x03",
            "#13510FIt's probably because of\x01",
            "Ilya's guidance and\x01",
            "Sully's own tenacity.\x02\x03",
            "#13508FMaybe more than even my\x01",
            "own, this whole time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B23")


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
            "#12500FWe still have plenty of\x01",
            "time left, so let's\x01",
            "enjoy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57250, -5600, 29000, 6000)
    MoveCamera(235, 10, 0, 6000)
    SetCameraDistance(13500, 6000)
    OP_93(0x9, 0x10E, 0x1F4)

    def lambda_12C66():
        OP_9B(0x0, 0xFE, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12C66)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12503F#6PHmm. Even though she's\x01",
            "not so tall, she's so...\x02\x03",
            "#12511F(No stop!)\x02\x03",
            "#12500F(There's a lot of time\x01",
            "until noon. I should\x01",
            "check in with everyone.)\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E8F")
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

    label("loc_12E8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EA4")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_12EA4")

    OP_90(0x0, 40000, 0, 17000, 270)
    SetScenarioFlags(0x145, 0)
    OP_29(0xA5, 0x1, 0x3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_57_F23D end

    def Function_58_12ECB(): pass

    label("Function_58_12ECB")

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

    # Function_58_12ECB end

    def Function_59_12F5A(): pass

    label("Function_59_12F5A")

    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x546, 0x5, 0x10, 0x11, 0x12, 0x13, 0x14)
    Sound(318, 0, 40, 0)
    Return()

    # Function_59_12F5A end

    def Function_60_12F72(): pass

    label("Function_60_12F72")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_60_12F72 end

    def Function_61_12F9D(): pass

    label("Function_61_12F9D")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_61_12F9D end

    def Function_62_12FC8(): pass

    label("Function_62_12FC8")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6000, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_62_12FC8 end

    def Function_63_12FF3(): pass

    label("Function_63_12FF3")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_63_12FF3 end

    def Function_64_1301E(): pass

    label("Function_64_1301E")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4500, 0, -1500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_1301E end

    def Function_65_13049(): pass

    label("Function_65_13049")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_65_13049 end

    def Function_66_13074(): pass

    label("Function_66_13074")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_13074 end

    def Function_67_1309F(): pass

    label("Function_67_1309F")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 5500, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_67_1309F end

    def Function_68_130CA(): pass

    label("Function_68_130CA")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_130CA end

    def Function_69_130F5(): pass

    label("Function_69_130F5")

    OP_93(0xFE, 0xF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_69_130F5 end

    def Function_70_1310C(): pass

    label("Function_70_1310C")

    OP_98(0xFE, 0x4B0, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_70_1310C end

    def Function_71_13121(): pass

    label("Function_71_13121")

    OP_98(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_71_13121 end

    def Function_72_13136(): pass

    label("Function_72_13136")

    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_72_13136 end

    def Function_73_1314B(): pass

    label("Function_73_1314B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1322A")
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
    Jump("Function_73_1314B")

    label("loc_1322A")

    Return()

    # Function_73_1314B end

    def Function_74_1322B(): pass

    label("Function_74_1322B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1330D")
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
    Jump("Function_74_1322B")

    label("loc_1330D")

    Return()

    # Function_74_1322B end

    def Function_75_1330E(): pass

    label("Function_75_1330E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_133ED")
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
    Jump("Function_75_1330E")

    label("loc_133ED")

    Return()

    # Function_75_1330E end

    def Function_76_133EE(): pass

    label("Function_76_133EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_134D0")
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
    Jump("Function_76_133EE")

    label("loc_134D0")

    Return()

    # Function_76_133EE end

    def Function_77_134D1(): pass

    label("Function_77_134D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13534")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60080, -6950, 27560)
    OP_9F(0x1, 61500, -6850, 28810)
    OP_9F(0x1, 60190, -7050, 30310)
    OP_9F(0x1, 58950, -7150, 29090)
    OP_9F(0x1, 59200, -7250, 28000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("Function_77_134D1")

    label("loc_13534")

    Return()

    # Function_77_134D1 end

    def Function_78_13535(): pass

    label("Function_78_13535")

    SetChrPos(0xFE, 58250, -6850, 29000, 0)

    label("loc_13546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1359F")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60250, -6750, 31000)
    OP_9F(0x1, 58250, -7200, 33000)
    OP_9F(0x1, 56250, -7250, 31000)
    OP_9F(0x1, 58250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("loc_13546")

    label("loc_1359F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Return()

    # Function_78_13535 end

    def Function_79_135C5(): pass

    label("Function_79_135C5")

    SetChrPos(0xFE, 58250, -6950, 30000, 0)

    label("loc_135D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_1362F")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 59250, -6950, 31000)
    OP_9F(0x1, 58250, -7250, 32000)
    OP_9F(0x1, 57250, -7250, 31000)
    OP_9F(0x1, 58250, -6950, 30000)
    OP_9F(0x2, 0xFE, 1000, 0x6)
    Jump("loc_135D6")

    label("loc_1362F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6950, 30000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_79_135C5 end

    def Function_80_13655(): pass

    label("Function_80_13655")

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
            "─And so, everyone had a\x01",
            "fun time at the beach.\x07\x00\x02",
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
            "After that, Lloyd and the\x01",
            "others enjoyed a watermelon\x01",
            "splitting game together.\x07\x00\x02",
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
            "Later, as they enjoyed lunchboxes\x01",
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

    # Function_80_13655 end

    def Function_81_137C5(): pass

    label("Function_81_137C5")

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

    def lambda_13BFA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13BFA)
    Sleep(30)

    def lambda_13C12():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13C12)
    Sleep(30)

    def lambda_13C2A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13C2A)
    Sleep(30)

    def lambda_13C42():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13C42)
    Sleep(30)

    def lambda_13C5A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13C5A)
    Sleep(30)

    def lambda_13C72():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_13C72)
    Sleep(30)

    def lambda_13C8A():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13C8A)
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
            "#01203F#3C#5PWell then, I'll go rampage as much as\x01",
            "possible in the theme park area.\x02\x03",
            "#01200FReverting to my original form will be\x01",
            "the signal, so you'll take advantage of\x01",
            "that chance and head to the mansion.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13E15():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13E15)
    Sleep(50)

    def lambda_13E25():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13E25)
    Sleep(50)

    def lambda_13E35():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_13E35)
    Sleep(50)

    def lambda_13E45():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_13E45)
    Sleep(50)

    def lambda_13E55():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13E55)
    Sleep(50)

    def lambda_13E65():
        TurnDirection(0x106, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_13E65)
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
            "#00208F#12PZeit... Please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Divine Wolf Zeit",
        (
            "#01200F#3C#5PAnd you as well.\x02\x03",
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

    def lambda_13F76():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F76)

    def lambda_13F83():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13F83)

    def lambda_13F90():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13F90)

    def lambda_13F9D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_13F9D)

    def lambda_13FAA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_13FAA)

    def lambda_13FB7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_13FB7)
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
        "#10409F#11PHaha, how reliable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PAlright, first of all,\x01",
            "we'll go to the hotel's\x01",
            "arcad─\x02",
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
        "#2S#2PThere they are!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man's Voice",
        (
            "#2S#2PIt's Bannings and the\x01",
            "others!\x02",
        )
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

    def lambda_141A8():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141A8)
    Sleep(50)

    def lambda_141B8():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_141B8)
    Sleep(50)

    def lambda_141C8():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_141C8)
    Sleep(50)

    def lambda_141D8():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_141D8)
    Sleep(50)

    def lambda_141E8():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_141E8)
    Sleep(50)

    def lambda_141F8():
        OP_93(0x106, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_141F8)
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
            "#00310F#11PTch... They're already\x01",
            "here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PEnemies: 3 jaegers and 3\x01",
            "military monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#12PThey look pretty\x01",
            "powerful...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00007F#11PGet ready to intercept\x01",
            "them! We'll work\x01",
            "together and crush them!\x02",
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
        "#10107F#1K#4P#NYes!\x02",
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

    def lambda_1453E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1453E)

    def lambda_14553():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_14553)

    def lambda_14568():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_14568)

    def lambda_1457D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1457D)

    def lambda_14592():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14592)

    def lambda_145A7():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_145A7)
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

    # Function_81_137C5 end

    def Function_82_1463A(): pass

    label("Function_82_1463A")

    BeginChrThread(0xFE, 0, 0, 86)
    OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_82_1463A end

    def Function_83_14659(): pass

    label("Function_83_14659")


    def lambda_1465E():
        OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1465E)
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

    # Function_83_14659 end

    def Function_84_146B9(): pass

    label("Function_84_146B9")

    BeginChrThread(0xFE, 0, 0, 87)
    OP_75(0x2, 0x2, 0x0)
    SetChrPos(0xFE, 45000, -1000, 30000, 270)
    OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_84_146B9 end

    def Function_85_146F0(): pass

    label("Function_85_146F0")

    SetChrPos(0xFE, 45000, -1000, 30000, 270)

    def lambda_14706():
        OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14706)
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

    # Function_85_146F0 end

    def Function_86_1476A(): pass

    label("Function_86_1476A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1478E")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_86_1476A")

    label("loc_1478E")

    Return()

    # Function_86_1476A end

    def Function_87_1478F(): pass

    label("Function_87_1478F")

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

    # Function_87_1478F end

    def Function_88_147F4(): pass

    label("Function_88_147F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1480F")
    OP_A1(0xFE, 0xBB8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_88_147F4")

    label("loc_1480F")

    Return()

    # Function_88_147F4 end

    def Function_89_14810(): pass

    label("Function_89_14810")

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

    # Function_89_14810 end

    def Function_90_14901(): pass

    label("Function_90_14901")

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

    # Function_90_14901 end

    def Function_91_14A20(): pass

    label("Function_91_14A20")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5DC0, 0x1388, 0x0)
    Return()

    # Function_91_14A20 end

    def Function_92_14A47(): pass

    label("Function_92_14A47")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x4844, 0x1388, 0x0)
    Return()

    # Function_92_14A47 end

    def Function_93_14A6E(): pass

    label("Function_93_14A6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14A8C")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_93_14A6E")

    label("loc_14A8C")

    Return()

    # Function_93_14A6E end

    def Function_94_14A8D(): pass

    label("Function_94_14A8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14AAB")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_94_14A8D")

    label("loc_14AAB")

    Return()

    # Function_94_14A8D end

    def Function_95_14AAC(): pass

    label("Function_95_14AAC")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x57E4, 0x1388, 0x0)
    Return()

    # Function_95_14AAC end

    def Function_96_14AE4(): pass

    label("Function_96_14AE4")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5208, 0x1388, 0x0)
    Return()

    # Function_96_14AE4 end

    def Function_97_14B1C(): pass

    label("Function_97_14B1C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x55F0, 0x1388, 0x0)
    Return()

    # Function_97_14B1C end

    def Function_98_14B54(): pass

    label("Function_98_14B54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14B6D")
    Sound(845, 0, 60, 0)
    Sleep(400)
    Jump("Function_98_14B54")

    label("loc_14B6D")

    Return()

    # Function_98_14B54 end

    def Function_99_14B6E(): pass

    label("Function_99_14B6E")

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
        "#00010F#11PKh... They're strong...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PA bunch of elites! We\x01",
            "have to go full power\x01",
            "here...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PLet's hurry...! Zeit's\x01",
            "diversion is starting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11PYeah, to the arcade!\x02\x03",
            "The entire staff\x01",
            "evacuated, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PYes, no need to worry\x01",
            "about involving them in\x01",
            "fights!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PThen we don't need to\x01",
            "hold back!\x02",
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

    # Function_99_14B6E end

    def Function_100_14EB4(): pass

    label("Function_100_14EB4")

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

    # Function_100_14EB4 end

    def Function_101_14F4E(): pass

    label("Function_101_14F4E")

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

    def lambda_15438():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_15438)

    def lambda_1544D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1544D)

    def lambda_15462():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_15462)

    def lambda_15477():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_15477)

    def lambda_1548C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1548C)

    def lambda_154A1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_154A1)

    def lambda_154B6():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_154B6)
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

    # Function_101_14F4E end

    def Function_102_15560(): pass

    label("Function_102_15560")

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

    # Function_102_15560 end

    def Function_103_156B0(): pass

    label("Function_103_156B0")

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

    # Function_103_156B0 end

    def Function_104_15767(): pass

    label("Function_104_15767")

    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1770, 0x0)
    Return()

    # Function_104_15767 end

    def Function_105_15777(): pass

    label("Function_105_15777")

    OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x1770, 0x0)
    Return()

    # Function_105_15777 end

    def Function_106_15787(): pass

    label("Function_106_15787")

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

    # Function_106_15787 end

    def Function_107_159FF(): pass

    label("Function_107_159FF")

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

    # Function_107_159FF end

    def Function_108_15A99(): pass

    label("Function_108_15A99")

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
            "#10702F#11PIt seems the fight has\x01",
            "started at the theme\x01",
            "park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#5PAlright, let's take this\x01",
            "chance to pass through\x01",
            "the arcade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12PYes, sir!\x02",
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

    # Function_108_15A99 end

    def Function_109_15C7A(): pass

    label("Function_109_15C7A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15CE6")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_15D00")

    label("loc_15CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15CFA")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_15D00")

    label("loc_15CFA")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_15D00")

    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87050.itc", 0x26)
    LoadChrToIndex("monster/ch87250.itc", 0x27)
    LoadChrToIndex("monster/ch87350.itc", 0x28)
    LoadChrToIndex("monster/ch87450.itc", 0x29)
    LoadChrToIndex("monster/ch87550.itc", 0x2A)
    Call(0, 113)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15D41")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_15D5B")

    label("loc_15D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15D55")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_15D5B")

    label("loc_15D55")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_15D5B")

    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Call(0, 126)
    Return()

    # Function_109_15C7A end

    def Function_110_15D7D(): pass

    label("Function_110_15D7D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15E1E")
    SetChrChipByIndex(0xEF, 0x20)
    Jump("loc_15E34")

    label("loc_15E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15E30")
    SetChrChipByIndex(0xEF, 0x21)
    Jump("loc_15E34")

    label("loc_15E30")

    SetChrChipByIndex(0xEF, 0x22)

    label("loc_15E34")

    SetChrPos(0x101, 40230, -6910, 1770, 135)
    SetChrPos(0x153, 42190, -7020, 1260, 270)
    SetChrPos(0xEF, 40720, -6970, -210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#12503FWell then, let's begin\x01",
            "the operation.\x02\x03",
            "#12500FCan you do it like I\x01",
            "explained earlier?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_160A9")

    ChrTalk(
        0x102,
        (
            "#6P#12600FYes. We'll play on the\x01",
            "beach and lure the\x01",
            "monster out, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FAlright, I'm counting on\x01",
            "you.\x02\x03",
            "#12503FAnyhow, the monsters'\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#12601FYes, I know.\x02\x03",
            "#12603FI was surprised being suddenly\x01",
            "asked to help exterminate a\x01",
            "swimsuit-tearing monster, but...\x02\x03",
            "#12600FIt's for Bell as well, so I\x01",
            "would be happy to support you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGo for it Lloyd, Elie!\x02",
    )

    CloseMessageWindow()
    Jump("loc_16443")

    label("loc_160A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1627D")

    ChrTalk(
        0x103,
        (
            "#6P#12700FYes. We'll play on the\x01",
            "beach and lure the\x01",
            "monster out, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FAlright, I'm counting on\x01",
            "you.\x02\x03",
            "#12503FAnyhow, the monsters'\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#12700FYes, of course.\x02\x03",
            "#12703FI was surprised when we suddenly\x01",
            "got a request to exterminate\x01",
            "swimsuit-tearing monsters, but...\x02\x03",
            "#12701FI cannot forgive such evil deeds\x01",
            "on Mishy's home turf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGo for it Lloyd, Tio!\x02",
    )

    CloseMessageWindow()
    Jump("loc_16443")

    label("loc_1627D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16443")

    ChrTalk(
        0x109,
        (
            "#6P#13000FRight. We'll play on the\x01",
            "beach and lure the\x01",
            "monster out, right!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500FYeah, please do.\x02\x03",
            "#12503FAnyhow, the monsters'\x01",
            "behavior is strange enough\x01",
            "as it is. Let's be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#13000FYes, of course!\x02\x03",
            "#13003FI was surprised getting suddenly\x01",
            "asked to take out a monster that\x01",
            "tears swimsuits, but...\x02\x03",
            "#13000FIt's for all the beach visitors\x01",
            "as well, so I'll do my best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200FGo for it Lloyd, Noｱl!\x02",
    )

    CloseMessageWindow()

    label("loc_16443")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16597")

    ChrTalk(
        0x102,
        "#12602FEek. Geez, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12606F...*sigh*, still, no\x01",
            "monster is showing up,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1666A")

    label("loc_16597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16603")

    ChrTalk(
        0x103,
        "#12702FOh, you did it.\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#12706F...But I don't see any\x01",
            "monsters showing up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1666A")

    label("loc_16603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1666A")

    ChrTalk(
        0x109,
        "#13002FUgh, you did it!\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x109,
        (
            "#13006F...*sigh*, but no\x01",
            "monsters are showing up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1666A")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#12505FYeah... I wonder if they\x01",
            "realized it's a trap.\x02\x03",
            "#12503FBut I'm sure there are\x01",
            "monsters around. Let's\x01",
            "wait and see...\x02",
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
        "#6P#12511FUwah!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_167A2")

    ChrTalk(
        0x102,
        "#12609F*giggle*, payback.\x02",
    )

    CloseMessageWindow()
    Jump("loc_167FE")

    label("loc_167A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_167D2")

    ChrTalk(
        0x103,
        "#12704F...Right back at you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_167FE")

    label("loc_167D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_167FE")

    ChrTalk(
        0x109,
        "#13009FAhaha, that's payback!\x02",
    )

    CloseMessageWindow()

    label("loc_167FE")


    ChrTalk(
        0x101,
        "#6P#12512FY-You got me!\x02",
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
            "#5P#13206F(Aww. KeA wants to play\x01",
            "with them too.)\x02\x03",
            "#13208F(Lloyd said it's dangerous,\x01",
            "but it looks like they're\x01",
            "just having fun...)\x02\x03",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16D11")
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
        "#12P#12605FHuh...\x02",
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
        "#12615F#4S─Eeeeeek!?!?\x02",
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

    def lambda_16C62():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_16C62)
    Sleep(1000)

    def lambda_16C7F():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C7F)

    ChrTalk(
        0x101,
        "#6P#12511FE-Elie!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x102,
        (
            "#12613FI-I'm fine... Chase\x01",
            "after the monster!!\x02",
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
    Jump("loc_1733A")

    label("loc_16D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1702A")
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
        "#12P#12705FHuh...\x02",
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
        "#12710F#4SKyah!?!?\x02",
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

    def lambda_16F81():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_16F81)
    Sleep(1000)

    def lambda_16F9E():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F9E)

    ChrTalk(
        0x101,
        "#6P#12511FT-Tio!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x103,
        (
            "#12701FI-I'm fine... Hurry, the\x01",
            "monster!!\x02",
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
    Jump("loc_1733A")

    label("loc_1702A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1733A")
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
        "#13014F#4SKyah!!??\x02",
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

    def lambda_1729B():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1729B)
    Sleep(1000)

    def lambda_172B8():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_172B8)

    ChrTalk(
        0x101,
        "#6P#12511FN-Noｱl!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x109,
        (
            "#13006FI-I'm all right... After\x01",
            "it!\x02",
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

    label("loc_1733A")


    def lambda_1733F():
        OP_95(0xFE, 34050, -6300, 8750, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1733F)
    Sleep(100)

    def lambda_1735C():
        OP_99(0xFE, 0xEF, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1735C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_173F5")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_17418")

    label("loc_173F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17409")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_17418")

    label("loc_17409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17418")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x52, 0xFF)

    label("loc_17418")


    def lambda_1741D():
        OP_95(0xFE, 9860, -6000, -21850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1741D)
    Sleep(2000)

    def lambda_1743A():
        OP_95(0xFE, 11690, -6000, -17960, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1743A)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(10060, -5780, -20380, 6000)
    MoveCamera(246, 22, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(12250, 6000)
    WaitChrThread(0x24, 1)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_174A5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_174A5)
    Sleep(1000)

    def lambda_174B5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_174B5)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00006F*pant, pant*... T-That's\x01",
            "far enough!\x02\x03",
            "#00001FHow dare you tear off\x01",
            "girl's swimsuits! You'll\x01",
            "pay for this!\x02",
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
        "#12P#00007FHere we go!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_110_15D7D end

    def Function_111_175D1(): pass

    label("Function_111_175D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_175FE")

    def lambda_175E1():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_175E1)
    WaitChrThread(0xFE, 2)
    Jump("Function_111_175D1")

    label("loc_175FE")

    Return()

    # Function_111_175D1 end

    def Function_112_175FF(): pass

    label("Function_112_175FF")

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

    # Function_112_175FF end

    def Function_113_176EE(): pass

    label("Function_113_176EE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17706")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_1772D")

    label("loc_17706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1771C")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_1772D")

    label("loc_1771C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1772D")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_1772D")

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
            "#12P#00000FHow do you like that?\x01",
            "Resign yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9490, -5480, -21070, 3000)

    def lambda_17906():
        OP_99(0xFE, 0x24, 0xBB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17906)
    Sleep(500)

    def lambda_1791D():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1791D)
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

    def lambda_179A3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_179A3)
    Sleep(100)

    def lambda_179B3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_179B3)

    ChrTalk(
        0x101,
        "#12P#00005FWhat!?\x02",
    )

    CloseMessageWindow()

    def lambda_179D7():
        OP_95(0xFE, 23660, -2000, -35810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_179D7)
    Sleep(100)

    def lambda_179F4():
        OP_95(0xFE, 24940, -2000, -35780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_179F4)
    Sleep(100)

    def lambda_17A11():
        OP_95(0xFE, 21250, -2000, -36870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_17A11)
    Sleep(100)

    def lambda_17A2E():
        OP_95(0xFE, 21590, -2000, -35820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_17A2E)
    Sleep(100)

    def lambda_17A4B():
        OP_95(0xFE, 23090, -2000, -36580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_17A4B)
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
        "#00011FT-There's more of them!?\x02",
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
        "#4SLloyd!\x02",
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

    def lambda_17DEC():
        OP_95(0xFE, 15180, -6000, -13330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_17DEC)

    def lambda_17E06():
        OP_95(0xFE, 15380, -6000, -15880, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17E06)

    def lambda_17E20():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_17E20)

    def lambda_17E2D():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_17E2D)

    def lambda_17E3A():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_17E3A)

    def lambda_17E47():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_17E47)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17ECC")
    Sound(805, 0, 100, 0)
    Jump("loc_17ED2")

    label("loc_17ECC")

    Sound(531, 0, 100, 0)

    label("loc_17ED2")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17F52")

    ChrTalk(
        0x101,
        (
            "#00005FElie, KeA! ...Are you\x01",
            "all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FW-We'll talk later!\x01",
            "Let's defeat the\x01",
            "monsters now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802A")

    label("loc_17F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17FB5")

    ChrTalk(
        0x101,
        "#00005FTio, KeA! You ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWe'll talk later! Let's\x01",
            "take them out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802A")

    label("loc_17FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1802A")

    ChrTalk(
        0x101,
        (
            "#00005FNoｱl, KeA! ...Are you\x01",
            "all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FY-Yes!! At any rate,\x01",
            "let's take them out now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1802A")


    ChrTalk(
        0x101,
        "#00000FRight, got it!\x02",
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

    # Function_113_176EE end

    def Function_114_1807B(): pass

    label("Function_114_1807B")

    OP_93(0x25, 0x13B, 0x1F4)
    OP_A1(0x25, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_114_1807B end

    def Function_115_1808E(): pass

    label("Function_115_1808E")

    OP_93(0x26, 0x13B, 0x1F4)
    OP_A1(0x26, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_115_1808E end

    def Function_116_180A1(): pass

    label("Function_116_180A1")

    OP_93(0x27, 0x13B, 0x1F4)
    OP_A1(0x27, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_116_180A1 end

    def Function_117_180B4(): pass

    label("Function_117_180B4")

    OP_93(0x28, 0x13B, 0x1F4)
    OP_A1(0x28, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_117_180B4 end

    def Function_118_180C7(): pass

    label("Function_118_180C7")

    OP_93(0x29, 0x13B, 0x1F4)
    OP_A1(0x29, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_118_180C7 end

    def Function_119_180DA(): pass

    label("Function_119_180DA")

    OP_A1(0x25, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x25, 0x50BE, 0xFFFFE890, 0xFFFF9A34, 0x7D0, 0x1388)
    OP_95(0x25, 10410, -6000, -16510, 5000, 0x0)
    TurnDirection(0x25, 0x101, 500)
    Return()

    # Function_119_180DA end

    def Function_120_1811A(): pass

    label("Function_120_1811A")

    OP_A1(0x26, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x26, 0x4C22, 0xFFFFE890, 0xFFFF952A, 0x7D0, 0x1388)
    OP_95(0x26, 8150, -6000, -20170, 5000, 0x0)
    TurnDirection(0x26, 0x101, 500)
    Return()

    # Function_120_1811A end

    def Function_121_1815A(): pass

    label("Function_121_1815A")

    OP_A1(0x27, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x27, 0x5942, 0xFFFFE890, 0xFFFF94DA, 0x7D0, 0x1388)
    OP_95(0x27, 12360, -6000, -15910, 5000, 0x0)
    TurnDirection(0x27, 0x101, 500)
    Return()

    # Function_121_1815A end

    def Function_122_1819A(): pass

    label("Function_122_1819A")

    OP_A1(0x28, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x28, 0x4A4C, 0xFFFFE890, 0xFFFF9098, 0x7D0, 0x1388)
    OP_95(0x28, 13700, -6000, -22060, 5000, 0x0)
    TurnDirection(0x28, 0x101, 500)
    Return()

    # Function_122_1819A end

    def Function_123_181DA(): pass

    label("Function_123_181DA")

    OP_A1(0x29, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x29, 0x51E0, 0xFFFFE890, 0xFFFF93CC, 0x7D0, 0x1388)
    OP_95(0x29, 14480, -6000, -18580, 5000, 0x0)
    TurnDirection(0x29, 0x101, 500)
    Return()

    # Function_123_181DA end

    def Function_124_1821A(): pass

    label("Function_124_1821A")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18225")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18243")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_18225")

    label("loc_18243")

    Return()

    # Function_124_1821A end

    def Function_125_18244(): pass

    label("Function_125_18244")

    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    Return()

    # Function_125_18244 end

    def Function_126_1825D(): pass

    label("Function_126_1825D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18301")
    Sound(531, 0, 100, 0)

    label("loc_18301")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006FPhew... Well that takes\x01",
            "care of that.\x02",
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

    def lambda_1836B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1836B)
    Sleep(100)

    def lambda_1837B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1837B)
    Sleep(500)

    ChrTalk(
        0x153,
        "#12P#01109FEhehe, nice one!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18502")

    ChrTalk(
        0x102,
        (
            "#6P#00104FIn any case, with this I\x01",
            "believe the case is\x01",
            "closed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008FUm, Elie.\x02\x03",
            "#00006FHow to say this... Sorry\x01",
            "I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x102,
        (
            "#6P#00112FE-Enough of that, don't\x01",
            "worry. I let my guard\x01",
            "down too...\x02\x03",
            "#00103FMore importantly, I\x01",
            "wonder why those monsters\x01",
            "appeared on the beach...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18797")

    label("loc_18502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18644")

    ChrTalk(
        0x103,
        (
            "#6P#00204FWith this, the case is\x01",
            "closed for now, huh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008FUm, Tio...\x02\x03",
            "#00006FHow to say this... Sorry\x01",
            "I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x103,
        (
            "#6P#00203FDon't worry about it. I\x01",
            "let my guard down.\x02\x03",
            "#00200FMore importantly, I\x01",
            "wonder why those monsters\x01",
            "appeared on the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18797")

    label("loc_18644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_18797")

    ChrTalk(
        0x109,
        (
            "#6P#10109FWith this, the case is\x01",
            "closed for now, right!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008FUm, Noｱl.\x02\x03",
            "#00006FHow to say this... Sorry\x01",
            "I couldn't protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x109,
        (
            "#6P#10112FD-Don't worry about it so\x01",
            "much! I let my guard down\x01",
            "too...\x02\x03",
            "#10105FMore importantly, why did\x01",
            "those monsters show up on\x01",
            "the beach, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18797")


    ChrTalk(
        0x101,
        (
            "#00006FWe can only guess. Most likely, it's\x01",
            "due to the impact of this area's\x01",
            "development.\x02\x03",
            "#00001FMonsters, having no place to go due to\x01",
            "development, started to retaliate\x01",
            "against people... That's my best guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_189A3")

    ChrTalk(
        0x102,
        (
            "#6P#00103FI see... That's possible.\x02\x03",
            "#00101FMaybe they were encouraged\x01",
            "after seeing the commotion they\x01",
            "caused by tearing swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FI feel kind of bad for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000FWell for now, let's go\x01",
            "report to Carmina and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYes, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C16")

    label("loc_189A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18AE2")

    ChrTalk(
        0x103,
        (
            "#6P#00203FI see... It's a possibility.\x02\x03",
            "#00200FI wonder if they were encouraged\x01",
            "after seeing the commotion they\x01",
            "caused by ripping swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FI feel kind of bad for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000FWell for now, let's go\x01",
            "report to Carmina and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C16")

    label("loc_18AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_18C16")

    ChrTalk(
        0x109,
        (
            "#6P#10103FI see... It's possible.\x02\x03",
            "#10101FThey must have been encouraged\x01",
            "after seeing the commotion they\x01",
            "caused by ripping swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FI feel kind of bad for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000FWell for now, let's go\x01",
            "report to Carmina and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYes, let's go!\x02",
    )

    CloseMessageWindow()

    label("loc_18C16")

    StopSound(136, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("t1320", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_126_1825D end

    SaveToFile()

Try(main)
