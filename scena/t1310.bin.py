from ScenarioHelper import *

def main():
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
        "Cecil",                 # 1
        "Lisha",               # 2
        "Erie",                 # 3
        "Tio",                 # 4
        "Franc",                 # 5
        "Zeit",               # 6
        "Keya",                 # 7
        "Shuri",                 # 8
        "Ilia",                 # 9
        "Randy",               # 10
        "Noel",                 # 11
        "Waji",                   # 12
        "ball",                 # 13
        "Mercapa",               # 14
        "Mercapa",               # 15
        "A hunter",                   # 16
        "A hunter",                   # 17
        "A hunter",                   # 18
        "A hunter",                   # 19
        "A hunter",                   # 20
        "A hunter",                   # 21
        "Military dog",                 # 22
        "Military dog",                 # 23
        "Military dog",                 # 24
        "Military dog",                 # 25
        "Elisabeth",           # 26
        "Tapper",               # 27
        "Watcher Wave",         # 28
        "Pengu",               # 29
        "Pengu",               # 30
        "Pengu",               # 31
        "Pengu",               # 32
        "Pengu",               # 33
        "Pengu",               # 34
        "SE control",                 # 35
        "bt1310",                 # 36
        "bt1310",                 # 37
        "bt1310",                 # 38
        "bt1320",                 # 39
        "Destination to Hotel · Delfinia",# 40
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

    PlaceName(-50.0, 0.0, 0.0, 0x0000, 0x0000, "Destination to Hotel · Delfinia")

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
        "Function_16_1717",        # 10, 16
        "Function_17_1BC7",        # 11, 17
        "Function_18_1EEA",        # 12, 18
        "Function_19_20ED",        # 13, 19
        "Function_20_233A",        # 14, 20
        "Function_21_245A",        # 15, 21
        "Function_22_25D5",        # 16, 22
        "Function_23_2719",        # 17, 23
        "Function_24_2B90",        # 18, 24
        "Function_25_2FA3",        # 19, 25
        "Function_26_3240",        # 1A, 26
        "Function_27_3406",        # 1B, 27
        "Function_28_346E",        # 1C, 28
        "Function_29_374E",        # 1D, 29
        "Function_30_3CA8",        # 1E, 30
        "Function_31_3DFA",        # 1F, 31
        "Function_32_421B",        # 20, 32
        "Function_33_4390",        # 21, 33
        "Function_34_4423",        # 22, 34
        "Function_35_448F",        # 23, 35
        "Function_36_44FB",        # 24, 36
        "Function_37_4554",        # 25, 37
        "Function_38_5A4A",        # 26, 38
        "Function_39_6E2F",        # 27, 39
        "Function_40_7505",        # 28, 40
        "Function_41_8232",        # 29, 41
        "Function_42_9D02",        # 2A, 42
        "Function_43_9D1A",        # 2B, 43
        "Function_44_A7F6",        # 2C, 44
        "Function_45_C706",        # 2D, 45
        "Function_46_C791",        # 2E, 46
        "Function_47_D114",        # 2F, 47
        "Function_48_D1B8",        # 30, 48
        "Function_49_D250",        # 31, 49
        "Function_50_D31F",        # 32, 50
        "Function_51_D3E1",        # 33, 51
        "Function_52_D4B0",        # 34, 52
        "Function_53_D799",        # 35, 53
        "Function_54_EA7C",        # 36, 54
        "Function_55_EBDF",        # 37, 55
        "Function_56_F3AE",        # 38, 56
        "Function_57_F6F1",        # 39, 57
        "Function_58_13416",       # 3A, 58
        "Function_59_134A5",       # 3B, 59
        "Function_60_134BD",       # 3C, 60
        "Function_61_134E8",       # 3D, 61
        "Function_62_13513",       # 3E, 62
        "Function_63_1353E",       # 3F, 63
        "Function_64_13569",       # 40, 64
        "Function_65_13594",       # 41, 65
        "Function_66_135BF",       # 42, 66
        "Function_67_135EA",       # 43, 67
        "Function_68_13615",       # 44, 68
        "Function_69_13640",       # 45, 69
        "Function_70_13657",       # 46, 70
        "Function_71_1366C",       # 47, 71
        "Function_72_13681",       # 48, 72
        "Function_73_13696",       # 49, 73
        "Function_74_13776",       # 4A, 74
        "Function_75_13859",       # 4B, 75
        "Function_76_13939",       # 4C, 76
        "Function_77_13A1C",       # 4D, 77
        "Function_78_13A80",       # 4E, 78
        "Function_79_13B10",       # 4F, 79
        "Function_80_13BA0",       # 50, 80
        "Function_81_13CF7",       # 51, 81
        "Function_82_14ADC",       # 52, 82
        "Function_83_14AFB",       # 53, 83
        "Function_84_14B5B",       # 54, 84
        "Function_85_14B92",       # 55, 85
        "Function_86_14C0C",       # 56, 86
        "Function_87_14C31",       # 57, 87
        "Function_88_14C96",       # 58, 88
        "Function_89_14CB2",       # 59, 89
        "Function_90_14DA3",       # 5A, 90
        "Function_91_14EC2",       # 5B, 91
        "Function_92_14EE9",       # 5C, 92
        "Function_93_14F10",       # 5D, 93
        "Function_94_14F2F",       # 5E, 94
        "Function_95_14F4E",       # 5F, 95
        "Function_96_14F86",       # 60, 96
        "Function_97_14FBE",       # 61, 97
        "Function_98_14FF6",       # 62, 98
        "Function_99_15010",       # 63, 99
        "Function_100_1535D",      # 64, 100
        "Function_101_153F7",      # 65, 101
        "Function_102_15A09",      # 66, 102
        "Function_103_15B59",      # 67, 103
        "Function_104_15C10",      # 68, 104
        "Function_105_15C20",      # 69, 105
        "Function_106_15C30",      # 6A, 106
        "Function_107_15EAD",      # 6B, 107
        "Function_108_15F47",      # 6C, 108
        "Function_109_16111",      # 6D, 109
        "Function_110_16214",      # 6E, 110
        "Function_111_17A92",      # 6F, 111
        "Function_112_17AC0",      # 70, 112
        "Function_113_17BAF",      # 71, 113
        "Function_114_18566",      # 72, 114
        "Function_115_18579",      # 73, 115
        "Function_116_1858C",      # 74, 116
        "Function_117_1859F",      # 75, 117
        "Function_118_185B2",      # 76, 118
        "Function_119_185C5",      # 77, 119
        "Function_120_18605",      # 78, 120
        "Function_121_18645",      # 79, 121
        "Function_122_18685",      # 7A, 122
        "Function_123_186C5",      # 7B, 123
        "Function_124_18705",      # 7C, 124
        "Function_125_1872F",      # 7D, 125
        "Function_126_18748",      # 7E, 126
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
    Jump("loc_1713")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AD")

    ChrTalk(
        0x22,
        (
            "You guys, we have beach today\x01",
            "Are you a guest who is making a charter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hey, envious.\x01",
            "I also work with such beautiful girls\x01",
            "I'd like to play in the water.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1713")

    label("loc_16AD")


    ChrTalk(
        0x22,
        (
            "Oh, the item of the shop\x01",
            "I am preparing a bit now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I'm sorry, but after a while\x01",
            "Will you come back again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1713")

    TalkEnd(0x22)
    Return()

    # Function_15_15E9 end

    def Function_16_1717(): pass

    label("Function_16_1717")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(
        0xFE,
        (
            "\"White stone\"\x01",
            "Sometimes found around here\x01",
            "It is a pure white and beautiful stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the beach of \"Whitehaven\"\x01",
            "It seems to be buried stone sometimes,\x01",
            "Perhaps they were brought together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are also looking for it,\x01",
            "Not only in the waterside,\x01",
            "You should also check out the sandy beach.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18E6")

    label("loc_183A")


    ChrTalk(
        0xFE,
        (
            "White stone originally\x01",
            "On the beach of \"Whitehaven\"\x01",
            "It seems to be a buried stone sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are also looking for it,\x01",
            "Not only in the waterside,\x01",
            "You should also check out the sandy beach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E6")

    Jump("loc_1BC3")

    label("loc_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(
        0xFE,
        (
            "But the rumor swimsuit ripper\x01",
            "It is said that it was such a devil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Am I definitely a stranger in a certain place\x01",
            "I thought something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for the moment it is settled and nothing more.\x01",
            "I give thanks to you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A33")

    label("loc_19B9")


    ChrTalk(
        0xFE,
        (
            "But the rumor swimsuit ripper\x01",
            "It is said that it was such a devil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for the moment it is settled and nothing more.\x01",
            "I give thanks to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A33")

    Jump("loc_1BC3")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B32")

    ChrTalk(
        0xFE,
        (
            "I, on this beach\x01",
            "To prevent dangerous things from happening,\x01",
            "I am shining my eye on monitoring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This area is still shallow,\x01",
            "It's a child if you go too far in the ocean\x01",
            "My legs are getting stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When playing in the water,\x01",
            "Do not go too far.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BC3")

    label("loc_1B32")


    ChrTalk(
        0xFE,
        (
            "This area is still shallow,\x01",
            "It's a child if you go too far in the ocean\x01",
            "My legs are getting stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When playing in the water,\x01",
            "Do not go too far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC3")

    TalkEnd(0xFE)
    Return()

    # Function_16_1717 end

    def Function_17_1BC7(): pass

    label("Function_17_1BC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEE")
    TalkEnd(0xFE)
    Call(0, 52)
    Return()

    label("loc_1BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")

    ChrTalk(
        0xA,
        (
            "#12613FAltogether anymore.\x01",
            "Suddenly in such a place\x01",
            "I do not want to get in … ….\x02\x03",
            "#12611FYou a little more\x01",
            "What delicacy is\x01",
            "You had better have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506FThat is, I have nothing to do ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CD7")

    label("loc_1CAB")


    ChrTalk(
        0xA,
        (
            "#12613FIndeed\x01",
            "Lloyd's ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD7")

    Jump("loc_1EE6")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF2")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E64")

    ChrTalk(
        0xA,
        (
            "#12600FHave the sunscreen painted\x01",
            "I appreciate it ….\x02\x03",
            "#12613FAnd, after all,\x01",
            "You are painted by your colleagues\x01",
            "I was a little embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FHahaha.\x01",
            "I was also shy about being honest.\x02\x03",
            "#12503F(Even so …. Gokuri.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612F… … Um, Lloyd?\x01",
            "So much so\x01",
            "I do not want you to see it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12511FGo, sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EE6")

    label("loc_1E64")


    ChrTalk(
        0xA,
        (
            "#12613FYou are painted by your colleagues\x01",
            "I was a little embarrassed.\x02\x03",
            "#12611Fまあ、Randyとかに塗られるより\x01",
            "I think that it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE6")

    TalkEnd(0xFE)
    Return()

    # Function_17_1BC7 end

    def Function_18_1EEA(): pass

    label("Function_18_1EEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0x8,
        (
            "#13305Fあらロイド、Keyaちゃんたちと\x01",
            "Are you looking for something?\x02\x03",
            "#13303FWhite stone ……?\x01",
            "Well, I have not seen it around here.\x01",
            "I am sorry I can not become a force.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E9")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAF")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208E")

    ChrTalk(
        0x8,
        (
            "#13304FHehe he was a good feeling.\x01",
            "Thank you, Lloyd.\x02\x03",
            "#13309F… Ah, that's right.\x01",
            "In return I went to Lloyd this time\x01",
            "Shall I paint sunscreen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FGood, good!\x01",
            "Cecil姉はゆっくり寝ててくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20E9")

    label("loc_208E")


    ChrTalk(
        0x8,
        (
            "#13304FIt feels good,\x01",
            "I hesitate to sleep like this.\x02\x03",
            "#13309FHuhu, please wake me up if there is something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E9")

    TalkEnd(0xFE)
    Return()

    # Function_18_1EEA end

    def Function_19_20ED(): pass

    label("Function_19_20ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2185")

    ChrTalk(
        0x9,
        (
            "#13505FWhite, round, beautiful stone … …?\x01",
            "No, I have not seen it.\x02\x03",
            "#13503FThis sand beach itself is white and beautiful,\x01",
            "It seems to be difficult to find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_2185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219B")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_219B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229C")

    ChrTalk(
        0x9,
        "#13508FFuu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12505F……Lisha？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13505FOh, no, I'm sorry.\x01",
            "I was thinking a bit.\x02\x03",
            "#13504FWell, Mr. Lloyd.\x01",
            "Thank you very much.\x02\x03",
            "#13502FHuhu, tentatively,\x01",
            "Worry about sunburn with this\x01",
            "You do not have to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2336")

    label("loc_229C")


    ChrTalk(
        0x9,
        (
            "#13504FTentatively,\x01",
            "Worry about sunburn with this\x01",
            "You do not have to do it.\x02\x03",
            "#13502FIliaさんやShuriちゃんも\x01",
            "I'm looking forward to it ……\x01",
            "Hehe, it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2336")

    TalkEnd(0xFE)
    Return()

    # Function_19_20ED end

    def Function_20_233A(): pass

    label("Function_20_233A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23A6")

    ChrTalk(
        0x11,
        (
            "#12805FWhy are you looking for a white stone?\x02\x03",
            "#12803FIt is unfortunate, but I have not seen it around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_23A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B5")
    Jump("loc_2456")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C7")
    Call(0, 21)
    Jump("loc_2456")

    label("loc_23C7")


    ChrTalk(
        0x11,
        (
            "#12800FAlthough it is surfing,\x01",
            "I did not rent out the board\x01",
            "It seems like it.\x02\x03",
            "#12806FShow a nice place for women\x01",
            "I wish I had a chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    TalkEnd(0xFE)
    Return()

    # Function_20_233A end

    def Function_21_245A(): pass

    label("Function_21_245A")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "#13002FAfter taking a break for a while,\x01",
            "I also want to do something different.\x02\x03",
            "#13004FWell, playing on the beach\x01",
            "What else was there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FThat's right, the classic on the beach\x01",
            "Although there is a feeling that I felt relieved, … …\x02\x03",
            "#12806FIf it is true, even to Nampa\x01",
            "I want to be stylish but the beach is reserved\x01",
            "Do not even encounter your sister ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006FSeniors, you are as usual …\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_245A end

    def Function_22_25D5(): pass

    label("Function_22_25D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266C")

    ChrTalk(
        0x12,
        (
            "#13000FIf you are looking for something,\x01",
            "Try changing the point of view\x01",
            "It might be nice.\x02\x03",
            "#13003FUnexpectedly unexpected place\x01",
            "It will be there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2715")

    label("loc_266C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")
    Jump("loc_2715")

    label("loc_267B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268D")
    Call(0, 21)
    Jump("loc_2715")

    label("loc_268D")


    ChrTalk(
        0x12,
        (
            "#13003FWell, playing on the beach\x01",
            "What else was there?\x02\x03",
            "#13000FMore so that you can enjoy it with a large group\x01",
            "I wish I had it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2715")

    TalkEnd(0xFE)
    Return()

    # Function_22_25D5 end

    def Function_23_2719(): pass

    label("Function_23_2719")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2856")

    ChrTalk(
        0x13,
        (
            "#12900FWhite stone? ….\x01",
            "Surely, with the sand of Whitehaven\x01",
            "I heard that it is the same material stone.\x02\x03",
            "#12904FOver the years, most\x01",
            "White stone turns into sand,\x01",
            "Sometimes, there seems to be a case where shapes remain beautifully.\x02\x03",
            "#12902FHuff, if you find a big one\x01",
            "You can think that it is pretty lucky.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2911")

    label("loc_2856")


    ChrTalk(
        0x13,
        (
            "#12904FOver the years, most\x01",
            "White stone turns into sand,\x01",
            "Sometimes, there seems to be a case where shapes remain beautifully.\x02\x03",
            "#12902FHuff, if you find a big one\x01",
            "You can think that it is pretty lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2911")

    Jump("loc_2B8C")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2925")
    Jump("loc_2B8C")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    ChrTalk(
        0x13,
        (
            "#12906FWell, unfamiliar play\x01",
            "I am completely tired.\x02\x03",
            "#12900FOriginally, the play that moves the body\x01",
            "I am not very good at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12503FWell then,\x01",
            "It seems that my breath is not disturbed … …\x02\x03",
            "#12502FI mean to rule\x01",
            "I felt it was fairly detailed,\x01",
            "Actually, you are pretty good at it, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FHuh, no way.\x01",
            "I am a genuinely urban child?\x02\x03",
            "#12900FEven the rules of beach volleyball,\x01",
            "In a magazine you read for killing time\x01",
            "I just remembered that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12503F(That makes me feel amazing with that … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2B8C")

    label("loc_2B04")


    ChrTalk(
        0x13,
        (
            "#12906FWell, unfamiliar play\x01",
            "I am completely tired.\x02\x03",
            "#12909Fフフ、僕もErieたちに混ざって\x01",
            "I'm going to stay elegantly on the deck chair.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    TalkEnd(0xFE)
    Return()

    # Function_23_2719 end

    def Function_24_2B90(): pass

    label("Function_24_2B90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C80")

    ChrTalk(
        0x10,
        (
            "#13400FKeyaちゃんはShuriと\x01",
            "You seem to be playing?\x02\x03",
            "#13404FHehe, that girl\x01",
            "Because there are no friends of the same age,\x01",
            "You are not used to being recollected.\x02\x03",
            "#13402FToday I may be able to see various new aspects.\x01",
            "Huh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2D0E")

    label("loc_2C80")


    ChrTalk(
        0x10,
        (
            "#13404FShuriってBecause there are no friends of the same age,\x01",
            "You are not used to being recollected.\x02\x03",
            "#13402FToday I may be able to see various new aspects.\x01",
            "Huh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0E")

    Jump("loc_2F9F")

    label("loc_2D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D22")
    Jump("loc_2F9F")

    label("loc_2D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0E")

    ChrTalk(
        0x10,
        (
            "#13409FWell, sometimes this\x01",
            "It's okay to encourage sports.\x02\x03",
            "#13402FPretty girls\x01",
            "You can also enjoy bathing suits ……\x01",
            "After all it was good.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12512FIliaさんって、実は\x01",
            "I wore the artist's skin\x01",
            "Oji-san …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406FOh, I will excuse you.\x02\x03",
            "#13402FHuhun, such a younger brother,\x01",
            "CecilやLishaたちの\x01",
            "Is not it nailed to swim suit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511FNo, with no comment.\x02\x03",
            "#12506F（というか、Iliaさんの水着が\x01",
            "I feel the greatest … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2F9F")

    label("loc_2F0E")


    ChrTalk(
        0x10,
        (
            "#13404FBy the way, except practice\x01",
            "I also moved my body like this\x01",
            "It may be a while ago ~.\x02\x03",
            "#13402FYes, of course\x01",
            "It was a great answer after receiving the invitation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9F")

    TalkEnd(0xFE)
    Return()

    # Function_24_2B90 end

    def Function_25_2FA3(): pass

    label("Function_25_2FA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3042")

    ChrTalk(
        0xB,
        (
            "#12705FWhite stone …\x01",
            "Such a thing on this sandy beach?\x02\x03",
            "#12703FOn the foundation of a sand castle\x01",
            "I used sand around here,\x01",
            "I have not seen such a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_3042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3058")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_3058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AF")

    ChrTalk(
        0xB,
        (
            "#12703FWith this sand material alone\x01",
            "It was half-trusting to make it … …\x02\x03",
            "#12702FRather, if you have sand\x01",
            "I even feel comfortable making anything.\x02\x03",
            "#12704Fふふ、今度はZeitの\x01",
            "You can also make your own house\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F（Zeitも、さすがに\x01",
            "I do not want sand … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01203FGuru …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_323C")

    label("loc_31AF")


    ChrTalk(
        0xB,
        (
            "#12704FNow, if you have sand\x01",
            "I even feel comfortable making anything.\x02\x03",
            "#12702Fふふ、今度はZeitの\x01",
            "You can also make your own house\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    TalkEnd(0xFE)
    Return()

    # Function_25_2FA3 end

    def Function_26_3240(): pass

    label("Function_26_3240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32C1")

    ChrTalk(
        0xC,
        (
            "#13105FWhat are you looking for ~ ~?\x02\x03",
            "#13103FWhite stone ……?\x01",
            "Well, I do not understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3402")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D7")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_32D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B2")

    ChrTalk(
        0xC,
        (
            "#13109FNo, really, a wonderful one\x01",
            "The castle was completed!\x02\x03",
            "#13106FIf you bring a camera\x01",
            "I was holding it in a photo … ….\x01",
            "Boo, it is regrettable ~.\x02\x03",
            "#13101FAt least, to the sensitive quartz of the heart\x01",
            "I have to bake firmly!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3402")

    label("loc_33B2")


    ChrTalk(
        0xC,
        (
            "#13101FThe appearance of this castle, to the sensitive quartz of the heart\x01",
            "I will burn firmly and return home ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3402")

    TalkEnd(0xFE)
    Return()

    # Function_26_3240 end

    def Function_27_3406(): pass

    label("Function_27_3406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3435")

    ChrTalk(
        0xD,
        "#01200F……won?\x02",
    )

    CloseMessageWindow()
    Jump("loc_346A")

    label("loc_3435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344B")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_344B")


    ChrTalk(
        0xD,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    label("loc_346A")

    TalkEnd(0xFE)
    Return()

    # Function_27_3406 end

    def Function_28_346E(): pass

    label("Function_28_346E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F9")

    ChrTalk(
        0xE,
        (
            "#13210FOh, Lloyd.\x01",
            "\"White stone\"\x01",
            "Have you found it any more?\x02\x03",
            "#13209FWell, my big brother\x01",
            "I wonder if there is anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374A")

    label("loc_34F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350F")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_END)), "loc_36DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3648")

    ChrTalk(
        0xE,
        (
            "#13210FThis white stone,\x01",
            "After all it was a big oh!\x02\x03",
            "#13209FIchiban at Michelin\x01",
            "Maybe I could have memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12509FHahaha, I just came\x01",
            "That's fast.\x02\x03",
            "#12504FBut if you are pleased that much\x01",
            "I will not be pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209FThank you, thank you.\x01",
            "I will cherish it! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_36D7")

    label("loc_3648")


    ChrTalk(
        0xE,
        (
            "#13202FEh, in Michelin Ichiban\x01",
            "Maybe I could have memories.\x02\x03",
            "#13209FThanks, Lloyd.\x01",
            "This \"white stone\",\x01",
            "I will cherish it! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D7")

    Jump("loc_374A")

    label("loc_36DC")


    ChrTalk(
        0xE,
        (
            "#13209FLooking for a white stone,\x01",
            "It was fun.\x02\x03",
            "#13204Fえへへ、後でZeitにも\x01",
            "I'll show it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374A")

    TalkEnd(0xFE)
    Return()

    # Function_28_346E end

    def Function_29_374E(): pass

    label("Function_29_374E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378A")
    Call(0, 30)
    Jump("loc_3A1C")

    label("loc_378A")

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
            "speak\x01",                          # 0
            "Show Whitestone\x01",      # 1
            "quit\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3800")
    Call(0, 30)
    Jump("loc_3A1C")

    label("loc_3800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0D")

    ChrTalk(
        0xF,
        (
            "#13605FMuu\x01",
            "\"White Stone\"\x01",
            "It seems I found it.\x02\x03",
            "#13600FQuickly our\x01",
            "\"White stone\" and\x01",
            "Do you compare the sizes?\x02",
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
            "Challenge a game\x01",          # 0
            "やっぱりquit\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399F")

    ChrTalk(
        0x101,
        "#12504FOh, let 's start a game quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13605FHmm, I feel confident.\x02\x03",
            "#13604FThen, I call Chibikko.\x01",
            "Huhun, are you barking later?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    Call(0, 53)
    Return()

    label("loc_399F")


    ChrTalk(
        0x101,
        "#12500FNo, wait a little more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606FShey, what is it.\x01",
            "If you are a man, decide it as a burn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A1C")

    label("loc_3A0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1C")

    label("loc_3A1C")

    Jump("loc_3CA4")

    label("loc_3A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A37")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 2)), scpexpr(EXPR_END)), "loc_3C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB5")

    ChrTalk(
        0xF,
        (
            "#13600FOh, that, uh … ….\x01",
            "Thank you for earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FDo you mean white stone?\x01",
            "Then do not worry about it.\x02\x03",
            "#12509FHaha, this time the alkane shell\x01",
            "You should show it to everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#13611FToo bad\x01",
            "Such a childish mane\x01",
            "I can do it!\x02\x03",
            "#13606FThink in common sense, at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F(The girls around the ages are hard … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3C0C")

    label("loc_3BB5")


    ChrTalk(
        0xF,
        (
            "#13603FAbout the white stone\x01",
            "Thank you.\x02\x03",
            "#13608F…… Fufun, that's it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0C")

    Jump("loc_3CA4")

    label("loc_3C11")


    ChrTalk(
        0xF,
        (
            "#13603FLooking for stones is nice too ….\x01",
            "I came to the beach,\x01",
            "I'd like to swim properly.\x02\x03",
            "#13602FせっかくだからLisha姉より\x01",
            "I wish I got better …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA4")

    TalkEnd(0xFE)
    Return()

    # Function_29_374E end

    def Function_30_3CA8(): pass

    label("Function_30_3CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D77")

    ChrTalk(
        0xF,
        (
            "#13600F\"White Stone\"\x01",
            "If you find it, tell me.\x02\x03",
            "Finally compare the sizes,\x01",
            "The one who had the biggest prize win.\x02\x03",
            "#13604FWell, I wish you something\x01",
            "I will not lose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3DF9")

    label("loc_3D77")


    ChrTalk(
        0xF,
        (
            "#13600FWhose \"white stone\" is\x01",
            "Is it the biggest, later it's a game.\x02\x03",
            "#13604FWell, I wish you something\x01",
            "I will not lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF9")

    Return()

    # Function_30_3CA8 end

    def Function_31_3DFA(): pass

    label("Function_31_3DFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3E0B")
    Jump("loc_4217")

    label("loc_3E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7B")

    ChrTalk(
        0x101,
        (
            "#12500FThat, this black cat … ….\x01",
            "I feel like I saw it somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alas …\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E8D")

    label("loc_3E7B")


    ChrTalk(
        0xFE,
        "Alas …\x02",
    )

    CloseMessageWindow()

    label("loc_3E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_40C6")

    ChrTalk(
        0x101,
        (
            "#12505FBy any chance\x01",
            "Are you hungry?\x02",
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
            "I will give you 'Nekomanma'\x01",      # 0
            "quit\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B2")

    ChrTalk(
        0x101,
        "#12500FDo not eat it if you like.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '猫食'),
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
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xFE,
        "Nyanaya ~ spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "GROUP\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509FWell, were you hungry so much?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Nyao journal\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝６卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝６卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FEr … … will you give me this book?\x02\x03",
            "#12500FThank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 5)
    SubItemNumber('猫食', 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40C1")

    label("loc_40B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C1")

    label("loc_40C1")

    Jump("loc_41FF")

    label("loc_40C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4179")

    ChrTalk(
        0x101,
        (
            "#12505FBy any chance\x01",
            "I wonder if your stomach is decreasing.\x02\x03",
            "#12503FIf you have \"Nekomanma\"\x01",
            "I could have given it … …\x02\x03",
            "#12512FUnfortunately I do not have any now.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41ED")

    label("loc_4179")


    ChrTalk(
        0x101,
        (
            "#12503FIf you have \"Nekomanma\"\x01",
            "I could have given it … …\x02\x03",
            "#12512FUnfortunately I do not have any now.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41ED")


    ChrTalk(
        0xFE,
        "Nyao\x02",
    )

    CloseMessageWindow()

    label("loc_41FF")

    SetScenarioFlags(0x1, 6)
    Jump("loc_4217")

    label("loc_4207")


    ChrTalk(
        0xFE,
        "Nyao journal\x02",
    )

    CloseMessageWindow()

    label("loc_4217")

    TalkEnd(0xFE)
    Return()

    # Function_31_3DFA end

    def Function_32_421B(): pass

    label("Function_32_421B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Attention on enjoying a lake bath\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "· Be sure to prepare exercise.\x01",
            "· Please do not enter water while wearing clothes.\x01",
            "(Swimwear is available for rent at the reception desk)\x01",
            "· Follow the instructions of the observer.\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "Let's keep good manners and have fun.\x01",
            "─ ─ From the Michelam Division\x07\x00\x02",
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

    # Function_32_421B end

    def Function_33_4390(): pass

    label("Function_33_4390")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FOops ……\x01",
            "This is in the building.\x02\x03",
            "Mr. Marível\x01",
            "He made it for me.\x01",
            "Now let's enjoy Lake Beach.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10330, -2000, -920, 90)
    EventEnd(0x4)
    Return()

    # Function_33_4390 end

    def Function_34_4423(): pass

    label("Function_34_4423")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500F\"White stone\"\x01",
            "It should be somewhere on the beach.\x01",
            "Let's search for more.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11580, -5080, -120, 90)
    EventEnd(0x4)
    Return()

    # Function_34_4423 end

    def Function_35_448F(): pass

    label("Function_35_448F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500F\"White stone\"\x01",
            "It should be somewhere on the beach.\x01",
            "Let's search for more.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11210, -4940, 46030, 90)
    EventEnd(0x4)
    Return()

    # Function_35_448F end

    def Function_36_44FB(): pass

    label("Function_36_44FB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FOops …… Beach volleyball\x01",
            "Let's find it out of the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 32500, -6000, -13500, 90)
    EventEnd(0x5)
    Return()

    # Function_36_44FB end

    def Function_37_4554(): pass

    label("Function_37_4554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4566")
    Call(0, 36)
    Return()

    label("loc_4566")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF4")
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
        "#13400F#11P── Alright ♪\x02",
    )

    CloseMessageWindow()

    def lambda_46C0():
        TurnDirection(0x13, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_46C0)
    Sleep(50)

    def lambda_46D0():
        TurnDirection(0x11, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_46D0)
    Sleep(50)

    def lambda_46E0():
        TurnDirection(0x12, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_46E0)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x11,
        "#12809F#5PKuu, fluffy smith …! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006F#6Pballが見えませんでした……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x10, 500)

    ChrTalk(
        0x13,
        (
            "#12902F#12PHuff, I used the whole body spring\x01",
            "It was a perfect spike.\x02\x03",
            "#12904FさすがはIlia・プラティエと\x01",
            "I told you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x13, 500)

    ChrTalk(
        0x10,
        "#13409F#5PHuh, you're welcome ♪\x02",
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
        "#12505F#6PThat's amazing …! It is!\x02",
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

    def lambda_48B0():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_48B0)
    Sleep(50)

    def lambda_48C0():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_48C0)
    Sleep(50)

    def lambda_48D0():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_48D0)
    Sleep(50)

    def lambda_48E0():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_48E0)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    ChrTalk(
        0x10,
        (
            "#13400F#11POh younger brother, were you watching?\x02\x03",
            "#13409FHuff, my deathblow technique\x01",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PIs that … Yes.\x01",
            "It was truly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PNo, it was seriously terrifying.\x02\x03",
            "#12804FAlso my spike\x01",
            "It will be received without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWaji君も、ここしかないって所に\x01",
            "トスしてIliaさんをアシストしてたし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#11PHuff, my raggedness.\x01",
            "Besides, you guys are pretty\x01",
            "It was a combination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PNo … honesty,\x01",
            "Everyone is too high level\x01",
            "I can not say any words.\x02\x03",
            "#12500FWhen you come into this tournament like this,\x01",
            "You can aim for the victory soon, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PHuh, well reality like that\x01",
            "It will not be easy, but,\x01",
            "It might be a nice way to go.\x02\x03",
            "#13409FThat's right, can not you mix the next game with your younger brother?\x01",
            "Let's enjoy the beach volleyball together ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15D, 2)
    Jump("loc_4D0A")

    label("loc_4BF4")

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
            "#13400F#11PIt's puzzy,\x01",
            "Does not your younger brother also mix the next game?\x02\x03",
            "#13409FLet's enjoy the beach volleyball together ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Join the beach volleyball\x01",      # 0
            "To give up\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C1")

    ChrTalk(
        0x101,
        (
            "#12500F#6PWell then, with your words\x01",
            "I will participate.\x02\x03",
            "#12506FEven so, the beach volley rule\x01",
            "I do not know much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F基本は普通のバレーballと同じですよ。\x02\x03",
            "#13004FRoughly speaking the difference,\x01",
            "The team is two pairs\x01",
            "Is it about to do on a sandy beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FAlso, actually, take 21 points first\x01",
            "I finally got one set victory … …\x02\x03",
            "In this time it will be easy to enjoy,\x01",
            "I'm doing it in an anomaly match of 12 games in one game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHmm, I see.\x01",
            "There is no problem for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12802F#5PWell, leave a detailed story\x01",
            "Let's go and part with the team right away.\x02\x03",
            "#12806FIf Lloyd enters, someone missing one person\x01",
            "You have to go to the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#6POh, I see.\x01",
            "Did I get in the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PHaha, you can do it.\x02\x03",
            "#13400FThen my younger brother, I want to join a team\x01",
            "Will you choose a partner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6POk, then, then …\x02",
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
            "#1KWho will you team up with?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Randy\x01",      # 0
            "Noel\x01",        # 1
            "Waji\x01",          # 2
            "Ilia\x01",        # 3
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
        (0, "loc_5161"),
        (1, "loc_5328"),
        (2, "loc_5504"),
        (3, "loc_56D3"),
        (SWITCH_DEFAULT, "loc_58A2"),
    )


    label("loc_5161")


    ChrTalk(
        0x101,
        "#12500F#6PRandy、Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12800F#5POkay, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13004F#5PWell then, with the rest of the team\x01",
            "Let's decide who will go to the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900FWell, this way fairly\x01",
            "Is not it ok for Janken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#11PHuh, I understand.\x01",
            "Let's decide quickly.\x02",
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
            "Janken's result\x01",
            "審判にはIliaが回り……\x07\x00\x02",
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
            "ロイド・Randyチームと\x01",
            "Waji・Noelチームの対戦が\x01",
            "It was time to open the curtain.\x07\x00\x02",
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
            "And ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 3)
    Call(1, 9)
    Jump("loc_58A2")

    label("loc_5328")


    ChrTalk(
        0x101,
        "#12500F#6PNoel、I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PI understand!\x01",
            "Let's do our best, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904FWell then, with the rest of the team\x01",
            "Shall decide who will go to the referee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13400F#11PWell, this way fairly\x01",
            "Is not it ok for Janken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#5PThat's right,\x01",
            "Let's decide quickly!\x02",
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
            "Janken's result\x01",
            "審判にはRandyが回り……\x07\x00\x02",
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
            "ロイド・Noelチームと\x01",
            "Ilia・Wajiチームの対戦が\x01",
            "It was time to open the curtain.\x07\x00\x02",
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
            "And ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 4)
    Call(1, 24)
    Jump("loc_58A2")

    label("loc_5504")


    ChrTalk(
        0x101,
        "#12500F#6PWaji、Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12900FHuh, I'm cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13404F#11PWell then, with the rest of the team\x01",
            "Let's decide who will go to the referee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800F#5PWell, this way fairly\x01",
            "Is not it good to be a Janken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#5PWell, decide by chance.\x01",
            "Let's start the game!\x02",
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
            "Janken's result\x01",
            "審判にはNoelが回り……\x07\x00\x02",
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
            "ロイド・Wajiチームと\x01",
            "Ilia・Randyチームの対戦が\x01",
            "It was time to open the curtain.\x07\x00\x02",
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
            "And ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 5)
    Call(1, 49)
    Jump("loc_58A2")

    label("loc_56D3")


    ChrTalk(
        0x101,
        "#12500F#6PIliaさん、お願いします。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#13400F#11POkay, thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12804F#5PWell then, with the rest of the team\x01",
            "Will you also decide who will go to the referee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13000F#5PWell, this way fairly\x01",
            "It looks good with a janken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902FHuh, that's right.\x01",
            "Well, let's decide early.\x02",
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
            "Janken's result\x01",
            "審判にはWajiが回り……\x07\x00\x02",
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
            "ロイド・Iliaチームと\x01",
            "Randy・Noelチームの対戦が\x01",
            "It was time to open the curtain.\x07\x00\x02",
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
            "And ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 6)
    Call(1, 69)
    Jump("loc_58A2")

    label("loc_58A2")

    Call(0, 38)
    Call(0, 39)
    Call(0, 45)
    SetChrPos(0x0, 20000, -6000, -15000, 0)
    Jump("loc_5A2F")

    label("loc_58C1")


    ChrTalk(
        0x101,
        "#12500F#6PWell, for a while now … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13405F#11POh yeah?\x01",
            "Well I will not say that.\x02\x03",
            "#13400FThen, when you want to participate\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A1E")
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

    label("loc_5A1E")

    SetChrPos(0x0, 32500, -6000, -13500, 90)

    label("loc_5A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A47")
    Call(0, 54)

    label("loc_5A47")

    EventEnd(0x5)
    Return()

    # Function_37_4554 end

    def Function_38_5A4A(): pass

    label("Function_38_5A4A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_5DF6")
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
            "#12809F#6PIs pretty\x01",
            "Was it a good game?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12902FHuh, it was certainly not bad.\x02",
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
            "#13401F#5PMu ~, it is awesome!\x01",
            "Let's just have fun with everyone.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C27():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C27)
    Sleep(50)

    def lambda_5C37():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5C37)
    Sleep(50)

    def lambda_5C47():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5C47)
    Sleep(50)

    def lambda_5C57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5C57)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x12,
        "#13005F#11Peh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#5PAs expected after all,\x01",
            "Just watching is unsatisfactory!\x02\x03",
            "#13409FRight next time I will mix\x01",
            "Let's play another game! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6PHaha, then this time\x01",
            "Shall I break it into another team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12809F#12PHa ha, is not it?\x02\x03",
            "#12800FWell then Lloyd,\x01",
            "I want to build a team next\x01",
            "Pick a partner.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5POh, I see. …\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_5DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_614D")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x12, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x12,
        "#13009F#6PHaa … … It was a hot game!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#13409F#11PYeah yeah, I got a nice sweat.\x02",
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
            "#12806F#5PMu … … as soon as Lloyd got in\x01",
            "Somehow it has gone hot.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F6F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F6F)
    Sleep(50)

    def lambda_5F7F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5F7F)
    Sleep(50)

    def lambda_5F8F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5F8F)
    Sleep(50)

    def lambda_5F9F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5F9F)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x13,
        "#12905F#12POh, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12803F#5PNo, after all I only\x01",
            "Even watching\x01",
            "Is it an unfair story?\x02\x03",
            "#12800FPlease mix me this time.\x01",
            "Well, let 's play another game!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6POh, then then\x01",
            "Shall we separate them into different teams?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13009F#12PYes, it looks good.\x02\x03",
            "#13000FThen, Mr. Lloyd,\x01",
            "I want to build a team next\x01",
            "Please choose a partner!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5POh, I see. …\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_614D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_6489")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x13, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x11, 27000, -6000, -14000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        "#12902F#6PHugh, it was fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12809F#11POh, it was a pretty good game.\x02",
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
            "#13001F#5P… … Um, everyone!\x01",
            "Why do not you play another game if you can! Is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62C3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62C3)
    Sleep(50)

    def lambda_62D3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_62D3)
    Sleep(50)

    def lambda_62E3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_62E3)
    Sleep(50)

    def lambda_62F3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_62F3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x10,
        "#13405F#11POh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006F#5PIf I were watching that game\x01",
            "It can not be suppressed anyhow … …\x02\x03",
            "#13002FNext time, please also enter me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#6POh, then then\x01",
            "Shall we separate them into different teams?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904F#12PHuh, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902F#12PWell then Lloyd,\x01",
            "I want to build a team next\x01",
            "You may choose a partner.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#12500F#5POh, I see. …\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_6489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_685B")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x10, 27000, -6000, -18000, 0)
    SetChrPos(0x11, 25000, -6000, -14000, 180)
    SetChrPos(0x12, 27000, -6000, -14000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        "#13409F#6PWell ~, it burns easily!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009F#11PYes, it was a lot of fun!\x02",
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
            "#12900F#5PHuh, then then in such a place\x01",
            "Is it a place to open?\x02\x03",
            "#12904FI am thirsty soon.\x02",
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
            "#12504F#12PNo … … Because it's no problem\x01",
            "Do you play one more game?\x02\x03",
            "#12500F今度はWajiも混ざってさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_667E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_667E)
    Sleep(50)

    def lambda_668E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_668E)
    Sleep(50)

    def lambda_669E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_669E)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)

    ChrTalk(
        0x11,
        (
            "#12800F#11POh, it looks good.\x01",
            "Wajiも審判じゃヒマだったろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#12906F#5PNo, I do not care\x01",
            "It feels good though ….\x02\x03",
            "#12900F…… Huh, I can not help it.\x01",
            "If you guys are nori\x01",
            "You can go out with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12PHuh, the story has been decided.\x02\x03",
            "#13400FWell then, my younger brother,\x01",
            "I want to build a team next\x01",
            "You may choose a partner.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12500F#6PYes, I understand.\x01",
            "Well then……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685B")

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
            "#1KWho will you team up with?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noel")
    MenuCmd(1, 0, "Waji")
    MenuCmd(1, 0, "Ilia")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_68C9")
    MenuCmd(3, 0, 0x0)

    label("loc_68C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_68D6")
    MenuCmd(3, 0, 0x1)

    label("loc_68D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_68E3")
    MenuCmd(3, 0, 0x2)

    label("loc_68E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_68F0")
    MenuCmd(3, 0, 0x3)

    label("loc_68F0")

    MenuCmd(2, 0, -1, 85, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6935"),
        (1, "loc_6A6D"),
        (2, "loc_6BBA"),
        (3, "loc_6CEC"),
        (SWITCH_DEFAULT, "loc_6E2E"),
    )


    label("loc_6935")

    TurnDirection(0x101, 0x11, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はRandy。\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x11, 0x101, 500)

    ChrTalk(
        0x11,
        "#12809F#5P#NOkay, leave it to me!\x02",
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
            "With Janken again done\x01",
            "To the referee of the second game\x01",
            "Iliaが選ばれ……\x07\x00\x02",
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
            "ロイド・Randyチームと\x01",
            "Waji・Noelチームの対戦が\x01",
            "It was to be done continuously.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 9)
    Jump("loc_6E2E")

    label("loc_6A6D")

    TurnDirection(0x101, 0x12, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はNoel。\x01",
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
            "#13009F#5P#NI understand!\x01",
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
            "With Janken again done\x01",
            "To the referee of the second game\x01",
            "Randyが選ばれ……\x07\x00\x02",
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
            "ロイド・Noelチームと\x01",
            "Ilia・Wajiチームの対戦が\x01",
            "It was to be done continuously.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 24)
    Jump("loc_6E2E")

    label("loc_6BBA")

    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はWaji。\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHuh, I'm cheap.\x02",
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
            "With Janken again done\x01",
            "To the referee of the second game\x01",
            "Noelが選ばれ……\x07\x00\x02",
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
            "ロイド・Wajiチームと\x01",
            "Ilia・Randyチームの対戦が\x01",
            "It was to be done continuously.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 49)
    Jump("loc_6E2E")

    label("loc_6CEC")

    TurnDirection(0x101, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はIliaさん。\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        "#13409F#5P#NOkay, thank you!\x02",
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
            "With Janken again done\x01",
            "To the referee of the second game\x01",
            "Wajiが選ばれ……\x07\x00\x02",
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
            "ロイド・Iliaチームと\x01",
            "Randy・Noelチームの対戦が\x01",
            "It was to be done continuously.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 69)
    Jump("loc_6E2E")

    label("loc_6E2E")

    Return()

    # Function_38_5A4A end

    def Function_39_6E2F(): pass

    label("Function_39_6E2F")

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
            "#6P#13409F…… Well, I enjoyed it!\x02\x03",
            "#13400FThanks to my brother's entrance\x01",
            "I also enjoyed various teams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FHaha, 2 games consecutive\x01",
            "It was pretty awful but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12803FOh, and to that … ….\x02\x03",
            "#12809FThe promised service scene is\x01",
            "It's a pity that you did not have it.\x02\x03",
            "#12806FNoelあたりが\x01",
            "I will tell you to chew\x01",
            "I wish I had expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#6P#13405FOh, certainly! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P#12904FJuhu, at the beach volleyball\x01",
            "You are getting involved.\x02",
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
            "#6P#13006Fせ、先輩にWaji君……\x01",
            "What are you saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FIliaさんの過剰反応も\x01",
            "I am worried … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12500FOh yeah, everyone.\x01",
            "Are you thirsty or thirsty?\x02\x03",
            "What is it, I was at a shop\x01",
            "I will buy some cold items though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FOops, it is attractive, my younger brother.\x01",
            "I wonder what is best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#12800FSurely, according to what I heard\x01",
            "Newly released to Michelin\x01",
            "It looks like you have juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6P#13000FOh, that's me too\x01",
            "I have heard of it.\x02\x03",
            "#13004F\"Belcora\" is said,\x01",
            "Shuwashwa and exhilarating\x01",
            "It seems to be a drink, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P#12902FHuh, it is\x01",
            "It looks pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FWell then,\x01",
            "Is it OK with everyone \"Belcora\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6P#13400FYes, thank you.\x02\x03",
            "#13404FWell, until now\x01",
            "I am not thirsty.\x01",
            "I do not have to hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500FOkay, I understand.\x01",
            "Well then I will bring it back later.\x02",
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

    # Function_39_6E2F end

    def Function_40_7505(): pass

    label("Function_40_7505")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8080")

    ChrTalk(
        0x8,
        "#5P#13302FOh, it is not Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13502FHello, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12504FCecil姉たちは日光浴か。\x02\x03",
            "#12500FIt seems that it is not in the lake yet,\x01",
            "Are you enjoying it properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FYeah, even if you just take it easy here\x01",
            "I am enjoying enough.\x02\x03",
            "#13309FErieさんやLishaさんとも\x01",
            "I can chat variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602FHaha, we also\x01",
            "It's fun, but ….\x01",
            "Occasionally I am in trouble for a while.\x02\x03",
            "#12606FCecilさんったら、さっきから\x01",
            "\"How about relationships with Lloyd? \"And,\x01",
            "I just listen to such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509FWell, yeah ….\x01",
            "I was slightly surprised.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#12506Fあ、あのなあCecil姉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FHuhu, would not it?\x02\x03",
            "My older sister, my brother's friendship relationship\x01",
            "I have to check it all the time.\x02\x03",
            "#13301FAnd who will be your future bride,\x01",
            "I have to put on per click!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12506FNo, no.\x01",
            "That's good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13500F（う〜ん、さすがIliaさんの\x01",
            "There is only a childhood friend … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#13302FYes, Lloyd.\x01",
            "I am lazy and you too\x01",
            "Why do not you sunbathe?\x02\x03",
            "#13309FThere is also space in the deck chair,\x01",
            "Let's talk a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12512FNo~……\x01",
            "As expected it is in the loop\x01",
            "It's kind of embarrassing ……\x02\x03",
            "#12500FI will hold back this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#13305FOh yeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12600FHuhuu, I feel shy now.\x01",
            "There will not be no thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13503FYes, that's right.\x01",
            "I also want to talk a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#12502FHaha, that's what I say\x01",
            "I appreciate it ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#5P#13303Fうーん……Well then……\x02\x03",
            "#13309FInstead,\x01",
            "We sunscreen\x01",
            "Will you paint me?\x02",
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
        "#12P#12505FHuh……………………\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0xC8, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#12511F#4SEeeeey yeah yeah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12605Fちょ、ちょっとCecilさん！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#13506FSure, that's kinda … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FHuhu, that's not okay.\x01",
            "I have no problem at all?\x02\x03",
            "#13304FErieさんもLishaさんも、\x01",
            "Try to avoid sunburn as much as possible\x01",
            "You said that a little while ago?\x02\x03",
            "#13309FBesides, \"I feel shy now.\x01",
            "There is no such thing as \"\x01",
            "Erieさんも言ってたし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12605FWell, that is … …\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12607FWow, I understand!\x02\x03",
            "#12613FWell then……\x01",
            "Lloyd, please.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        "#12P#12505Fエ、Erie……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12611FBecause, everyone else\x01",
            "Are you crazy about your own play?\x02\x03",
            "#12606FWant to avoid sunburn as much as possible\x01",
            "It's a real story ……\x02\x03",
            "#12613FRandyとかに塗られるよりは\x01",
            "I thought you better.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#13503FThat … … That's right.\x02\x03",
            "#13506FIliaさんも、ホテルの部屋で\x01",
            "I painted a sunscreen … …\x02\x03",
            "#13502FIf that is Lloyd's\x01",
            "There may be no resistance there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        "#12P#12511Fリ、Lishaまで！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FHuhu, here we are Lloyd.\x01",
            "These pretty kids and my sister\x01",
            "I'm asking for it.\x02\x03",
            "#13302FSunscreen, will you paint?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    SetScenarioFlags(0x15D, 0)
    Jump("loc_80C4")

    label("loc_8080")


    ChrTalk(
        0x8,
        (
            "#5P#13302FOh, Lloyd.\x01",
            "We sunscreen\x01",
            "Do you paint?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C4")

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
            "Cecilたちに日焼け止めを塗る\x01",      # 0
            "To give up\x01",                        # 1
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
        (0, "loc_813C"),
        (1, "loc_8144"),
        (SWITCH_DEFAULT, "loc_8231"),
    )


    label("loc_813C")

    Call(0, 41)
    Jump("loc_8231")

    label("loc_8144")


    ChrTalk(
        0x101,
        (
            "#12P#12511FWell, wait a moment.\x01",
            "My heart is ready … !.!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FOh … … Huhu, that can not be helped.\x01",
            "Well, come later.\x02\x03",
            "#13304FBut, hurry as possible.\x01",
            "Because it will get sunburned as it is.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 21500, -6000, 20700, 90)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearMapObjFlags(0x1, 0x1000)
    EventEnd(0x5)
    Jump("loc_8231")

    label("loc_8231")

    Return()

    # Function_40_7505 end

    def Function_41_8232(): pass

    label("Function_41_8232")

    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#12P#12501FI understood that … ….\x01",
            "Respectfully, I will paint it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12611FRespect! …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509FHaha …… Tension is\x01",
            "It is somewhat strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13300FHuhu, then immediately\x01",
            "Let me ask you.\x02\x03",
            "#13303F最初は誰にDo you paint?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#12506FLet me see……\x02",
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
            "#1KWho will paint sunscreen?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Erieから塗る\x01",        # 0
            "Cecilから塗る\x01",        # 1
            "Lishaから塗る\x01",      # 2
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
        (0, "loc_83FB"),
        (1, "loc_89EA"),
        (2, "loc_9057"),
        (SWITCH_DEFAULT, "loc_9725"),
    )


    label("loc_83FB")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FWell then……\x01",
            "Erieから塗らせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12612FWow, I! Is it?\x02\x03",
            "#12613FGood, good, but ….\x01",
            "Strange places, do not touch it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#12503FWell, I will do my best …\x02",
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
            "#11P#12501FWell then, please disappoint.\x02\x03",
            "#12503F(Pitto.)\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x64, 0xBB8, 0x12C)

    def lambda_85EC():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_85EC)

    ChrTalk(
        0xA,
        "#6P#12615F#4S… … Ha ha! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12505FGo, sorry! are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#12613FNo……\x01",
            "It was cold and just surprised me.\x02\x03",
            "#12602FIt's all right, please continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FWell, that's right, then …\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 9000)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(Ha, this is more than I expected\x01",
            "Bad for my heart …)\x02\x03",
            "#12508F（それにしてもErie、\x01",
            "It is really beautiful … …)\x02\x03",
            "#12503F(My skin is so white,\x01",
            "Pearl gray hair\x01",
            "I mean well shining … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#6P#12612F…, a little.\x01",
            "Do not be silent suddenly.\x02\x03",
            "#12611FNo way, what is nasty\x01",
            "You guessed it was not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FThere is no ruin!\x02\x03",
            "#12503F(If you are not good, Mr. Marybele\x01",
            "It really gets submerged at the bottom … …! It is! )\x02\x03",
            "#12501F(… … I will limit my heart to the end.\x01",
            "Anyway, to the absence of … …! )\x02",
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
            "#11P#N#13506FMr. Lloyd ……\x01",
            "Somehow like Jizo of Eastern Street\x01",
            "It looks like it has become a face.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P#13309FHehe, Lloyd.\x01",
            "Erieさんが終わったら\x01",
            "Please also our way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_9725")

    label("loc_89EA")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#12P#12500FWell then……\x01",
            "Cecil姉から塗らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13309FHuhu, I know.\x01",
            "Then you gotta ask me.\x02",
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
        "#11P#12500F……どうかな、Cecil姉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304FYes, that's it.\x01",
            "Please spread it thinly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12500FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#13304F…… Huhu, what are you doing like this\x01",
            "I remember the old days.\x02\x03",
            "#13302FWhen I was a child, sometimes I take a bath\x01",
            "I dropped Lloyd and my back.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511Fだあああっ、セ、Cecil姉ってば！！\x01",
            "What are you saying in front of everyone! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_63(0x8, 0xFFFFFE0C, 1700, 0x2, 0x7, 0x50, 0x1)

    def lambda_8CD1():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8CD1)

    ChrTalk(
        0x8,
        (
            "#6P#13306FCash!\x02\x03",
            "#13309F…… Huhu, if it is already Lloyd.\x01",
            "Do not touch strange places.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#12511FWow, sorry! It is!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    SetCameraDistance(13500, 9000)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(Oh, already ….\x01",
            "  Cecil姉は無防備すぎるよ！？）\x02\x03",
            "#12508F(Well, if you put your skin on\x01",
            "Outstanding destructive power … …)\x02\x03",
            "#12506F(…, it's useless!\x01",
            "  Cecil姉にそんなこと考えちゃ！）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#13305FLloyd, what's wrong?\x01",
            "Only the same place from a little while ago\x01",
            "It looks like I'm painting ….\x02\x03",
            "#13308F… … Maybe I am fat.\x02\x03",
            "#13306FPatients and chiefs\x01",
            "Because I often give sweets,\x01",
            "Hey hey hey hey hey … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FNo, no,\x01",
            "Because it is not such a thing at all! It is!\x01",
            "Even without worrying enough clean …\x02\x03",
            "#12506F…… Oh no, not! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#13309FHuh, thank you Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#12611F(Well ….\x01",
            "As usual it is unrelenting. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13509F(Haha ……\x01",
            "It looks like you heard the story. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9725")

    label("loc_9057")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#12500FWell then……\x01",
            "Lisha、君から塗らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#13505FWait!\x02\x03",
            "#13503FWell, that's a bad guy.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#12506F…… It's wrong something.\x02",
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
        "#11P#12502FYoda … how about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13503FOh, yes.\x01",
            "I think that it is such a thing.\x02\x03",
            "#13506FHaha, but I was really saved.\x01",
            "I am leaving the stage of the alkane shell\x01",
            "I can not do sunburn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FOh, is it so?\x02\x03",
            "#12505FOh, but …\x01",
            "Iliaさんの日焼け止めは\x01",
            "Did not you paint it?\x02\x03",
            "#12511FAt that time, if you paint alternately - ─\x01",
            "……, Ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#13509FWell, uh … … haha.\x01",
            "That is what it is.\x02\x03",
            "#13506FIliaさんにこんな無防備な\x01",
            "What will you do if you are exposed to the dress\x01",
            "I do not understand … ….\x02",
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
            "#11P#12512F（オジサン丸出しのIliaさんより\x01",
            "Is it that I am better?\x01",
            "That is also a complicated reason. )\x02\x03",
            "#12501F（……それにしてもLisha、\x01",
            "Although it is hard to understand as it looks\x01",
            "It is quite trained. )\x02\x03",
            "#12508F(While keeping this proportion\x01",
            "Physical ability to that extent ……\x01",
            "I guess this is also a talent. )\x02\x03",
            "#12503F(More than anything\x01",
            "With this height this is exactly\x01",
            "It's no exaggeration to say weapons … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#6P#13505FMr. Lloyd, Mr. Lloyd? That gaze … ….\x02",
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12511FWow, sorry!\x02\x03",
            "#12512FNo, that's different.\x01",
            "I thought you are not exercising after all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P#N#12611FHaa …… A boy\x01",
            "I wonder why this is the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13309FHehe, Lloyd.\x01",
            "Lishaさんが終わったら\x01",
            "Please also our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9725")

    label("loc_9725")

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
            "#6P#12506F(Oh, looking at it again\x01",
            "It's an amazing sight … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13304FHa … … Thank you, Lloyd.\x01",
            "It was very relaxing.\x02\x03",
            "#13309FUhufu, she seems to sleep like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1P#12606Fセ、Cecilさん。\x01",
            "I sleep in that shape variously\x01",
            "I think it is dangerous ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P#13509FHaha ……\x01",
            "It is a bit too much, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#13304FHuhu, even if it feels good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#12500FWell then, as I wake up\x01",
            "Shall I buy a cold drink for everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1P#12605FOh, is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12503F(In a sense, a dreamlike experience\x01",
            "You got me done … …)\x02\x03",
            "#12512F(To be honest, I have to do this\x01",
            "Punishment seems to come down from the goddess. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P#13505F…… Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12512FOh no, nothing.\x02\x03",
            "#12500FWell then, non alcoholic\x01",
            "Is it OK with a cocktail or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#13302FYeah, that's fine.\x02\x03",
            "#13309FOh, you do not have to hurry.\x01",
            "Lloyd is enjoying a lot, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#12500FOh, thank you.\x01",
            "Well then, later.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CEE")
    Call(0, 54)
    EventEnd(0x5)
    Jump("loc_9D01")

    label("loc_9CEE")

    SetChrPos(0x0, 21500, -6000, 20700, 90)
    EventEnd(0x5)

    label("loc_9D01")

    Return()

    # Function_41_8232 end

    def Function_42_9D02(): pass

    label("Function_42_9D02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D19")
    OP_A0(0xFE, 500, 0x0, 0x3)
    Jump("Function_42_9D02")

    label("loc_9D19")

    Return()

    # Function_42_9D02 end

    def Function_43_9D1A(): pass

    label("Function_43_9D1A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2CB")

    ChrTalk(
        0xC,
        "#6P#13101FScurrying\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12701FPetapeta …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#12505F(No, I'm concentrating somewhat … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200F… … Guru …… Won.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ED8")
    Jump("loc_9F22")

    label("loc_9ED8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EF8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F22")

    label("loc_9EF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F18")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F22")

    label("loc_9F18")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F22")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FD8")
    Jump("loc_A022")

    label("loc_9FD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FF8")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A022")

    label("loc_9FF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A018")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A022")

    label("loc_A018")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A022")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xB,
        "#12P#12705F…… Oh, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13100FWhat happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12512FHaha, I guess I got in the way.\x02\x03",
            "#12500FNo, like that\x01",
            "I thought what I was making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FNo no, it is unexpected.\x02\x03",
            "#13109FOnce, I made a castle with sand\x01",
            "Where am I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FIt is what is called \"sand craft\".\x02\x03",
            "#12706FHowever, it does not go very well …\x01",
            "It is repetition of breaking after making it from the previous time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FWell, it looks pretty difficult.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FThat's right,\x01",
            "Why do not you help Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12505FEr … … I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FYeah, you are right.\x01",
            "Work may progress.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 1)
    Jump("loc_A557")

    label("loc_A2CB")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A35C")
    Jump("loc_A3A6")

    label("loc_A35C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A37C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A6")

    label("loc_A37C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A39C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A6")

    label("loc_A39C")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3A6")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A45C")
    Jump("loc_A4A6")

    label("loc_A45C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A47C")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4A6")

    label("loc_A47C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A49C")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4A6")

    label("loc_A49C")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A4A6")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, Mr. Lloyd.\x01",
            "Help me make a sand castle\x01",
            "Are you giving up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FPlease do come.\x01",
            "Work may progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A557")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Helps to make a sand castle\x01",      # 0
            "To give up\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6E7")

    ChrTalk(
        0x101,
        (
            "#11P#12500FOh, I understand.\x01",
            "I'll be of assistance if you do not mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FHey Mr. Lloyd!\x01",
            "Thank you~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FAlthough it is said\x01",
            "I am a beginner but also a beginner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, they are all alike.\x02\x03",
            "#12704Fでは、早速Thank you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 44)
    Call(0, 45)
    Jump("loc_A7CA")

    label("loc_A6E7")


    ChrTalk(
        0x101,
        "#11P#12512FWell, now a bit … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#13106FWell, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FWell, if you feel like that\x01",
            "Please come call me.\x02\x03",
            "#12704FそれまでFrancさんと\x01",
            "Because I am working hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)

    label("loc_A7CA")

    SetChrPos(0x0, 29920, -6000, 8910, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7F3")
    Call(0, 54)

    label("loc_A7F3")

    EventEnd(0x5)
    Return()

    # Function_43_9D1A end

    def Function_44_A7F6(): pass

    label("Function_44_A7F6")

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
        "#6P#13100F…… Well, I can do it a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12700FYeah, a little more to completion ─\x02",
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
        "#01203F……won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P#12706F…. It is quite difficult, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FWell, maybe\x01",
            "There is a problem with the strength of sand\x01",
            "Maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105FIs it strength? …\x02\x03",
            "#13106FOnce, put sand and water in a bucket\x01",
            "I made the foundation firmly, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FStill, making it\x01",
            "The sand will dry out.\x02\x03",
            "#12504FIt would be better to do it while adding water,\x01",
            "I feel I've heard of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12705FI see……\x01",
            "It seems to be reasonable.\x02\x03",
            "#12702FWell then, how much water?\x01",
            "You had better add it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12503FWell, I guess so ….\x02",
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
            "#1KHow about the amount of water to add?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "plenty\x01",        # 0
            "Slightly more\x01",      # 1
            "Just a little\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACE3")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500FSure, just a little ……\x01",
            "I think that it was enough to wet it and it was OK.\x02\x03",
            "#12504FEven if you put too much water\x01",
            "On the contrary the strength will go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FCertainly, as I was told\x01",
            "I feel like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FThen, as Mr. Lloyd says\x01",
            "Let's try it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7A")

    label("loc_ACE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD86")

    ChrTalk(
        0x101,
        (
            "#11P#12500FI was drunk here,\x01",
            "Using plenty of water\x01",
            "You should do it better.\x02\x03",
            "#12504FThat person gains strength …\x01",
            "I feel like it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE08")

    label("loc_AD86")


    ChrTalk(
        0x101,
        (
            "#11P#12500FPerhaps, while using water a little more\x01",
            "You should do it better.\x02\x03",
            "#12504FThat person gains strength …\x01",
            "I feel like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE08")


    ChrTalk(
        0xC,
        "#6P#13105FIs not that something like that ~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12700FWell, as Lloyd's say\x01",
            "Let's try it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#12P#12702FIt is getting much closer to completion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13109FYeah, Mr. Lloyd's\x01",
            "Thanks for the advice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12502FHaha, I will be glad if you say so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702FHeh he … Finally,\x01",
            "Let's go into the finishing.\x02\x03",
            "Part of the main castle\x01",
            "Detail up, but ……\x01",
            "May I ask Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C2")

    label("loc_B01C")


    ChrTalk(
        0xB,
        "#12P#12700FIt is getting quite completed, but …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xC,
        "#6P#13105FIt is kinda scary of something ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12506F(Well, hmm … ….\x01",
            "After all too much water … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FWell, for now\x01",
            "There is no sign of collapse … ….\x01",
            "そろそろLet's go into the finishing.\x02\x03",
            "#12702FPart of the main castle\x01",
            "Detail up, but ……\x01",
            "May I ask Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C2")


    ChrTalk(
        0x101,
        (
            "#11P#12500FOh, I understand.\x01",
            "Leave it to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FEverything depends on Mr. Lloyd!\x01",
            "Thank you ~!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(Press pressure\x01",
            "I was hung up …\x01",
            "But, well, it can not be helped. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12501F(Well, with the water strength\x01",
            "Although it is heightening,\x01",
            "Material is sand to the last … ….)\x02\x03",
            "#12503F(Perhaps important,\x01",
            "It is speed and strength.\x01",
            "…… How can you proceed? )\x02",
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
            "#1KHow about speed and strength?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Slowly / delicately\x01",      # 0
            "Slowly / powerfully\x01",      # 1
            "Quickly & delicately\x01",        # 2
            "Quickly / powerfully\x01",        # 3
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
        (0, "loc_B428"),
        (1, "loc_B47B"),
        (2, "loc_B4CC"),
        (3, "loc_B527"),
        (SWITCH_DEFAULT, "loc_B576"),
    )


    label("loc_B428")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Okay … slowly with delicate power\x01",
            "Let's arrange the details! )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B47B")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright … slowly and powerfully,\x01",
            "Let's arrange the details! )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B4CC")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright …… With quick and delicate power\x01",
            "Let's arrange the details! )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B527")


    ChrTalk(
        0x101,
        (
            "#11P#12500F(Alright …… quickly and powerfully,\x01",
            "Let's arrange the details! )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B594")
    Jump("loc_B966")

    label("loc_B594")

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
        "#12P#12705FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh …… Haha.\x01",
            "You did it!\x02",
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
            "#11P#12505FNo, that something ….\x02\x03",
            "#12506F…… Sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F…… Well it can not be helped.\x02\x03",
            "#12700FTentatively, from 1 to the level\x01",
            "Shall I recycle it?\x02\x03",
            "ロイドさんは、私とFrancさんの\x01",
            "Please go to support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12512FRyo, OK.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FMr. Lloyd, please\x01",
            "Please do not be discouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B886")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(The water fluctuation was suitable\x01",
            "I suppose that … …)\x02\x03",
            "(Oh no … I do not have a position.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B966")

    label("loc_B886")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8FE")

    ChrTalk(
        0x101,
        (
            "#11P#12506F(The way of work was not wrong\x01",
            "I suppose that … …)\x02\x03",
            "(Oh no … I do not have a position.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B966")

    label("loc_B8FE")


    ChrTalk(
        0x101,
        (
            "#11P#12506F(How much water works and how to work,\x01",
            "I can only think that it was wrong … …)\x02\x03",
            "(Oh no … I do not have a position.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B966")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x2)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#12500FFu … … It is such a place.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#6P#13100Ffinally……\x01",
            "It was finally completed! It is!\x02\x03",
            "#13109FCare! I did it! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB23")
    OP_2C(0xA5, 0x1)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12704F…… It is feelingless.\x01",
            "Mr. Lloyd, cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12502FHaha … that kind of thing.\x01",
            "Thanks to the efforts of the two.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FNo, thanks to Mr. Lloyd!\x01",
            "thank you very much! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC05")

    label("loc_BB23")

    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F…… Anyway, it was good.\x01",
            "There were various things until completion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12506FSorry, that section was really sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13109FAhahahahaha, that's enough already ~.\x01",
            "In this way I finished it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC05")

    TurnDirection(0xB, 0xD, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12702F#5PZeitもお疲れ様でした。\x02\x03",
            "#12704FIn the final stage, supply of missing sand and water\x01",
            "He helped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        "#11P#12500F#5Pはは、さすがはZeitだよな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#12505FYes, that's right … …\x01",
            "Is this castle a name?\x02",
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
        "#6P#13105FName?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FNo, I made it with difficult time,\x01",
            "If you have something like that\x01",
            "I thought it would be memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12703FThere is a point.\x01",
            "Hmm, in that case …\x02\x03",
            "#12700F\"Missi Castle\",\x01",
            "How about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13105Fえ〜、Tioちゃんズルい！\x02\x03",
            "#13109FWell then I\x01",
            "I'd like \"Bang Bang Castle\"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12500FMitsushii are familiar but ……\x02\x03",
            "#12503FBang bang is,\x01",
            "Francのお気に入りの\x01",
            "It was a nuigurumi.\x02\x03",
            "#12509FHa ha …… Both are pretty\x01",
            "I have a hobby.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F…… But to the same castle\x01",
            "Two names can not be attached.\x02\x03",
            "#12700FIn this case, Lloyd says\x01",
            "Would you please decide which one to use?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, that might be good ~!\x02\x03",
            "#13109FIf Lloyd decides\x01",
            "There is no complaint and Vishitto\x01",
            "Please choose!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#12506F(No, it is seriously responsible for anything.\x02\x03",
            "#12500FWell, I guess so ….\x02",
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
            "#1KWhich is the name of the castle?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Missi Castle\x01",      # 0
            "Bang Bang Castle\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C2")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#5PThat's right.\x01",
            "It is that I came to the Michelin … …\x02\x03",
            "#12500FThis time \"Missi Castle\"\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        (
            "#6P#13106FWell, that's true if you tell me ~.\x02\x03",
            "#13102FIt can not be helped, this time\x01",
            "Tioちゃんにゆずってあげる！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        "#12P#12702FHehe … … Thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3FD")

    label("loc_C2C2")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#11P#12503F#11PThat's right, Mitsui\x01",
            "I will be able to meet as much as I can later … …\x02\x03",
            "#12500FThis time \"Bang Bang Castle\"\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703F…… Hmm, there is a point.\x02\x03",
            "#12702FOh well, this time\x01",
            "Francさん案ということで。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        "#6P#13109Fふふっ、ありがとうTioちゃん！\x02",
    )

    CloseMessageWindow()

    label("loc_C3FD")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#12509FIt seems that it fits round.\x02\x03",
            "#12505Fそうだ……Tio、Franc。\x01",
            "Have you been sitting on the beach for a long time and thirsty?\x02\x03",
            "#12500FIf you like, later\x01",
            "I will bring even cold things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12P#12703FI agree……\x02\x03",
            "#12700FI was at a shop\x01",
            "I would like to eat oyster ice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#13100FOh, I want to eat it too!\x02\x03",
            "#13109FMr. Lloyd, could I ask a favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#12509Fああ、Leave it to me.\x02\x03",
            "#12500FZeitには……\x01",
            "Francクフルトでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12P#12702FIt seems to have \"asked\".\x02\x03",
            "#12703F…… Oh, but without hurrying\x01",
            "Because it is fine.\x02\x03",
            "#12702FI am having a lot of trouble,\x01",
            "Please enjoy also Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#12502FHaha, OK.\x02",
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

    # Function_44_A7F6 end

    def Function_45_C706(): pass

    label("Function_45_C706")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_END)), "loc_C723")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_END)), "loc_C736")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_C749")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C749")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C790")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_C790")

    Return()

    # Function_45_C706 end

    def Function_46_C791(): pass

    label("Function_46_C791")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCCC")

    ChrTalk(
        0xE,
        (
            "#13209F#6PWow oh ……\x01",
            "Shuriのもキレーだね！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#11PHuh, it's not a big deal.\x02\x03",
            "#13600FEven so, this stone, until now\x01",
            "I have never seen it … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PDid they both come back?\x01",
            "…… What are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C911():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C911)
    Sleep(50)

    def lambda_C921():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_C921)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xE,
        (
            "#13210F#12POh, Lloyd.\x01",
            "Take a look at this -!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12PEh, are you beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5POh, it is round and pure white ……\x01",
            "It is a beautiful stone like a jewel.\x02\x03",
            "#12505FWhat's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13600F#12PA while ago, while swimming\x01",
            "This Civicco picked it up.\x02\x03",
            "#13604FSomehow, here and there\x01",
            "Because it seems to be falling\x01",
            "I was looking for it for a while.\x02\x03",
            "#13602FIf you ask a guardian,\x01",
            "Say \"white stone\"\x01",
            "It is a stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PHmm, sand here\x01",
            "She seems to have brought it from a foreign country … …\x02\x03",
            "#12503FPerhaps, what can be taken around there\x01",
            "I guess it was mixed.\x02\x03",
            "#12500FThat's it, it's quite big\x01",
            "It may be buried.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#13205F#12PHonto ー! Is it?\x02\x03",
            "#13200FHey, well then, everyone,\x01",
            "Let's find this white stone!\x02\x03",
            "#13209FSo at the end the biggest thing\x01",
            "People who have got to win! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#13602F#12PHuhun, it sounds interesting.\x02\x03",
            "#13604FOf course you do participate, do not you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 6)
    Jump("loc_CD70")

    label("loc_CCCC")


    def lambda_CCD1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_CCD1)
    Sleep(50)

    def lambda_CCE1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CCE1)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    ChrTalk(
        0xF,
        (
            "#13600F#12PI mean, you too\x01",
            "Do you want to mix?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13202F#12PTogether with Lloyd,\x01",
            "\"White Stone\"\x01",
            "Look for it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Start searching for white stones\x01",      # 0
            "To give up\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02F")

    ChrTalk(
        0x101,
        (
            "#12500F#5POh, it's okay\x01",
            "May I join you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12PIt's a rule!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13600F#12PThen, you too\x01",
            "Once you find \"White Stone\"\x01",
            "Please tell me.\x02\x03",
            "#13604FFinally compare the sizes,\x01",
            "The one who had the biggest prize win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509F#5POkay, that's OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13201F#12PWell …\x01",
            "Well then it's a start!\x02\x03",
            "#13200FKeya、ゼッタイ一番大きいのを\x01",
            "I will find it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13603F#12PHun, you guys\x01",
            "Would you like to lose?\x02",
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
    Jump("loc_D111")

    label("loc_D02F")


    ChrTalk(
        0x101,
        "#12512F#5PWell, I will stop now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13205F#12PEr, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13606F#12PWell, I guess it's bad.\x02\x03",
            "#13600FWell, please call me out if you feel like it.\x01",
            "Sometime I will mix.\x02",
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

    label("loc_D111")

    EventEnd(0x5)
    Return()

    # Function_46_C791 end

    def Function_47_D114(): pass

    label("Function_47_D114")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12503FWell, is it a bit small?\x02\x03",
            "There seems to be a bigger one … …\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x15C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_47_D114 end

    def Function_48_D1B8(): pass

    label("Function_48_D1B8")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FThere was … but it's small.\x02\x03",
            "Do you want to find out more?\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x15C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_48_D1B8 end

    def Function_49_D250(): pass

    label("Function_49_D250")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12500FCompletely in the palm of your hand\x01",
            "It is about the size to fit.\x02\x03",
            "#12503FKeyaもShuriもこのくらいは\x01",
            "I am trying to find it … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x15C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_D250 end

    def Function_50_D31F(): pass

    label("Function_50_D31F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12503F…… Is that so big?\x02\x03",
            "#12500FIf this is the case a good match\x01",
            "It might be possible, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x15C, 4)
    TalkEnd(0xFF)
    Return()

    # Function_50_D31F end

    def Function_51_D3E1(): pass

    label("Function_51_D3E1")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12505FHuh …! Is it?\x01",
            "It's like a crystal ball!\x02\x03",
            "#12509FHaha, if only this is great\x01",
            "First we will not lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x15C, 5)
    TalkEnd(0xFF)
    Return()

    # Function_51_D3E1 end

    def Function_52_D4B0(): pass

    label("Function_52_D4B0")

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
        "#12605FOh Lloyd, what are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12500Fああ、今はKeyaたちと……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#12505FWait, maybe ….\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd under the deck chair\x01",
            "I reached out my hand.\x07\x00\x02",
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
        "#12612FEr, a little, hey …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12502F── There was!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#6P#12500FIn such a place\x01",
            "To be buried ……\x02\x03",
            "#12504FBut it is quite big.\x01",
            "You should definitely win if this is the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12611FOh, you … hey ….\x01",
            "Suddenly I crawled into such a place,\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#12511FOh …… Go, sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12606FWell, quite anymore.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x15C, 6)
    EventEnd(0x5)
    Return()

    # Function_52_D4B0 end

    def Function_53_D799(): pass

    label("Function_53_D799")

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
            "#12P#13600FThen compare the sizes.\x02\x03",
            "#13603FIn \"I'm sorry,\"\x01",
            "I have it\x01",
            "Put out the biggest stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12500FOh, that's OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13210FPreparation It's okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13601FOK, then let's go …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12501FTake care\x02",
    )


    ChrTalk(
        0xE,
        "#3P#13201FWell, oh no …\x02",
    )


    ChrTalk(
        0xF,
        "#4P#13601FTake care\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12500F#4SOh!#3S\x02",
    )


    ChrTalk(
        0xE,
        "#3P#13200F#4SSure! It is!#3S\x02",
    )


    ChrTalk(
        0xF,
        "#4P#13600F#4SOh!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E427")
    OP_2C(0xA5, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13210FWow … ah! It is!\x01",
            "Lloyd's \"White Stone\"\x01",
            "Very big! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13601FKuu …… No way No way\x01",
            "I will not find it.\x02\x03",
            "#13606FAs expected,\x01",
            "It seems only to accept loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12502FHaha, then\x01",
            "It looks good with me that I win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13606FShe is a very popular person for children.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12506F… … as I said it\x01",
            "I do not have a position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12P#13200FBut it's really big and it's a kire.\x02\x03",
            "#13206FKeyaもそんなのが欲しかったなー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FI see …\x01",
            "I might as well look for it a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE97")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FHaha, then\x01",
            "この\"White stone\"\x01",
            "I will give it to two people.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12P#13210FReally! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13605FIs it okay?\x01",
            "And two of them …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FOh, just right\x01",
            "About the same size\x01",
            "I was picking up another one.\x02\x03",
            "#12509FせっかくI came to the beach,\x01",
            "You should make that memorable.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはKeyaとShuriに\x01",
            "大きな\"White Stone\"\x01",
            "I handed it one by one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#12P#13612FFun … … Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13209FWell, I will treasure it! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber('纯白之石', 2)
    Jump("loc_E422")

    label("loc_DE97")


    ChrTalk(
        0x101,
        (
            "#5P#12500F(Yes, it's nothing ……\x01",
            "Should I give you a present? )\x02",
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
            "#1KWhich gift do you want \"Whitestone\"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Keyaにあげる\x01",      # 0
            "Shuriにあげる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1E3")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FWell then,\x01",
            "この\"White stone\"\x01",
            "Keyaにプレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12P#13210FEr, Really good! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FOh, of course.\x02\x03",
            "#12509FせっかくI came to the beach,\x01",
            "You should make that memory.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはKeyaに\x01",
            "I handed out a big \"white stone\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        "#12P#13209FWell, I will treasure it! It is!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "#12P#13606F#11PWell, I do not mind ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500Fゴメンな、Shuri。\x01",
            "君はKeyaよりお姉さんだから、\x01",
            "I wonder if you will endure this time?\x02",
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
            "#12P#13612FBa, separately …\x01",
            "I did not want such a stone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber('纯白之石', 1)
    Jump("loc_E422")

    label("loc_E1E3")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#5P#12500FWell then,\x01",
            "この\"White stone\"\x01",
            "Shuriにプレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#12P#13605FEr … Is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FOh, of course.\x02\x03",
            "#12509FせっかくI came to the beach,\x01",
            "You should make that memory.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはShuriに\x01",
            "I handed out a big \"white stone\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#12P#13612FFun … … Thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#12P#13209F#6Pよかったねー、Shuri！\x01",
            "Let me touch you later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500Fゴメンな、Keya。\x01",
            "Instead, this time, even a new book\x01",
            "I will buy it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#12P#13200FOh, yes!\x01",
            "I'm looking forward to it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SubItemNumber('纯白之石', 1)

    label("loc_E422")

    Jump("loc_E73B")

    label("loc_E427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E556")
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13205FOh,\x01",
            "Everyone is about the same!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13600FOh …… None of the sizes\x01",
            "It seems that it will not change much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FWell then, this time\x01",
            "I guess it is a draw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13606FWell, it is a boring result.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#12512FHaha, do not say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E73B")

    label("loc_E556")

    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13200FWow, Lloyd's stone,\x01",
            "It's a little small and cute! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13600FOh … quite small.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12512FHahaha ……\x01",
            "It looks like I lost.\x02\x03",
            "#12500FKeyaとShuriのは\x01",
            "It seems to be about the same,\x01",
            "This time it is that 2 people won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13209FYay, yay! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13606FWell, somehow\x01",
            "Show me a margin.\x02\x03",
            "#13602FHuh, inside is pretty\x01",
            "I was regretful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12506FDamn\x01",
            "Well, that's not it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E73B")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#12500Fそうだ……Keya、Shuri。\x01",
            "Do not you need something cold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13200FWill you bring me Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12504FOh, I've been playing on the waters forever,\x01",
            "It is getting tired soon?\x02\x03",
            "#12500FIf there is something I want to eat or drink,\x01",
            "Please do not hesitate to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P#13600FHmm, it is nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#13204FWell … well then … …\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#12P#13210FOh, I was at a shop\x01",
            "I want to eat ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FIce cream? ….\x01",
            "Okay, I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12P#13604FWell then, I am with that too.\x02\x03",
            "#13600FOh, I want to play a little longer\x01",
            "Is it because you do not have to bring it right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#12500FOh, okay.\x01",
            "Well then again later.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA79")
    Call(0, 54)

    label("loc_EA79")

    EventEnd(0x5)
    Return()

    # Function_53_D799 end

    def Function_54_EA7C(): pass

    label("Function_54_EA7C")

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
            "#12500FEveryone played together,\x01",
            "It seems that I am nonsbilling now.\x02\x03",
            "#12503F…… Well, somehow I also\x01",
            "I am thirsty.\x02\x03",
            "#12500FI will buy a cold one for everyone\x01",
            "I promise you,\x01",
            "Will you go to a shop soon?\x02\x03",
            "The shop has just left the stairs.\x01",
            "…… Let's peek at a bit.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    SetScenarioFlags(0x15E, 3)
    Return()

    # Function_54_EA7C end

    def Function_55_EBDF(): pass

    label("Function_55_EBDF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEE7")

    ChrTalk(
        0x22,
        (
            "Hi, welcome.\x01",
            "Do you enjoy the charming beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12502F#12PHaha, I've enjoyed it all the way.\x02\x03",
            "Um, I got it all together\x01",
            "I'd like to place an order ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Oh, just a while ago\x01",
            "The item is ready.\x01",
            "Please order anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#12PWell, then …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F#12P……Ah.\x01",
            "That reminds me of a locker\x01",
            "I left a wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oh, the future is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "In the words of Mr. Mariebel.\x01",
            "Eating and drinking fare is available for you during the holiday period\x01",
            "It's all serviced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#12PWell, was that so! Is it?\x02\x03",
            "#12512FI mean whether it is full of … …\x01",
            "To Mariavel\x01",
            "My head can not rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "You should thank him enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Well then, would you like to order?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF46")

    label("loc_EEE7")


    ChrTalk(
        0x22,
        (
            "Eating and drinking fare is available for you during the holiday period\x01",
            "It's all serviced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Would you like to order something quickly?\x02",
    )

    CloseMessageWindow()

    label("loc_EF46")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you order a cool thing here\x01",
            "Event at Lake Beach\x01",
            "All ends.\x07\x00\x02",
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
            "【Order cold items】\x01",      # 0
            "【I will stop it】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F317")

    ChrTalk(
        0x101,
        (
            "#12500F#12Pええ、Thank you.\x02\x03",
            "#12503FWell, four Belcora,\x01",
            "Three non-alcoholic cocktails ……\x02\x03",
            "#12500FTwo ice creams,\x01",
            "Two oyster ice … …. Oh, and\x01",
            "Francクフルトを１つお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "Only it at a time\x01",
            "Are you going to have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Perhaps you …\x01",
            "Type of self-destruction too much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#12PNo, no …\x01",
            "I do not think there is such a thing.\x02",
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
            "─ ─ The pleasant time on the beach went by so.\x02\x03",
            "Then Lloyd's promised\x01",
            "After having enjoyed watermelon split etc. with everyone ─ ─\x02\x03",
            "The hotel delivered\x01",
            "While striking lunch boxes\x01",
            "It was a lot of excitement.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15E, 4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_END)), "loc_F2D4")
    SubItemNumber('纯白之石', 1)

    label("loc_F2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_END)), "loc_F2E2")
    SubItemNumber('纯白之石', 1)

    label("loc_F2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_END)), "loc_F2F0")
    SubItemNumber('纯白之石', 1)

    label("loc_F2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_END)), "loc_F2FE")
    SubItemNumber('纯白之石', 1)

    label("loc_F2FE")

    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_F396")

    label("loc_F317")


    ChrTalk(
        0x101,
        "#12500F#12PNo, it is still ok.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oops, is it so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Well, before the holiday period ends\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F396")

    SetChrPos(0x0, -6770, -1500, 8450, 90)
    OP_4C(0x22, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_55_EBDF end

    def Function_56_F3AE(): pass

    label("Function_56_F3AE")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3E0")
    SetScenarioFlags(0x31, 2)

    label("loc_F3E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F426")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_F420")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F415")
    Sound(2499, 255, 100, 0)
    Jump("loc_F41B")

    label("loc_F415")

    Sound(3537, 255, 100, 0)

    label("loc_F41B")

    Jump("loc_F426")

    label("loc_F420")

    Sound(3344, 255, 100, 0)

    label("loc_F426")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_F49F")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Mercapaに乗り込む")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F47F"),
        (SWITCH_DEFAULT, "loc_F490"),
    )


    label("loc_F47F")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_F49A")

    label("loc_F490")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F49A")

    Jump("loc_F6DE")

    label("loc_F49F")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F4D3")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_F4D3")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F507"),
        (1, "loc_F60B"),
        (2, "loc_F69C"),
        (SWITCH_DEFAULT, "loc_F6D4"),
    )


    label("loc_F507")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F538")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F548")

    label("loc_F538")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F548")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F59E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F59E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C1")
    Sound(461, 0, 100, 0)

    label("loc_F5C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5E1")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_F5F1")

    label("loc_F5E1")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_F5F1")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_F426")

    label("loc_F60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F67D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F640")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F658")

    label("loc_F640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F653")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F658")

    label("loc_F653")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F658")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F697")

    label("loc_F67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F68D")
    OP_AF(0xFB)
    Jump("loc_F697")

    label("loc_F68D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F697")

    Jump("loc_F6DE")

    label("loc_F69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F6CF")

    label("loc_F6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F6C5")
    OP_AF(0xFB)
    Jump("loc_F6CF")

    label("loc_F6C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6CF")

    Jump("loc_F6DE")

    label("loc_F6D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6DE")

    Jump("loc_F426")

    label("loc_F6E3")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_F3AE end

    def Function_57_F6F1(): pass

    label("Function_57_F6F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F70D")
    Jump("loc_11F20")

    label("loc_F70D")

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

    def lambda_FA72():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FA72)
    Sleep(0)

    def lambda_FA8A():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FA8A)
    Sleep(0)

    def lambda_FAA2():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FAA2)
    Sleep(0)
    Sleep(5500)
    Sound(2757, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#12809F#5P#10A#4SHugh! It is!\x02",
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
            "#12502F#5PAmazing, this is …\x02\x03",
            "#12509FAlthough it is the first time to beach\x01",
            "I did not think that it was such beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12904F#5POrdinary beach is by sea\x01",
            "I wonder if the sand is so white.\x02\x03",
            "#12902FProbably, it is in the middle eastern part of the continent\x01",
            "\"Whitehaven\" from the sandy beach\x01",
            "I guess they carried sand?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FC84():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FC84)
    Sleep(50)

    def lambda_FC94():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FC94)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12511F#12PAre they serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12806F#6PIt is impossible to have … …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12909F#5PHuff, once again IBC\x01",
            "We have a glimpse of asset strength.\x02\x03",
            "#12900FMore than that, before the women came\x01",
            "You had better prepare?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12800F#6POh, I see.\x02\x03",
            "#12809FAfter all, on the beach\x01",
            "Parasol and others are classic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#12PIndeed, magazines and even\x01",
            "I feel like there was such a picture.\x02\x03",
            "#12500FOK, are you going to set it up?\x02",
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
        "#12504F#12PWell, this is such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12800F#11POh, how about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12902F#6PGood news, good news.\x02\x03",
            "#12909FWell then,\x01",
            "I wonder if I will let you rest.\x02",
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
        "#12506F#12PYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#11PSomehow more than me.\x01",
            "Do not get used to playing …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xE, 0x80)
    Sound(3042, 255, 80, 0)

    NpcTalk(
        0xE,
        "Keyaの声",
        "#10ALloyd's!\x02",
    )

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#12502F#12PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12802F#11POh, you saw it came.\x02",
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
            "#13209F#11PSounds great!\x01",
            "It's straightforward!\x02",
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
            "#12705F#11Psurely……\x01",
            "This is a surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12602F#11PWhen the bell ……\x01",
            "Before I knew this stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#13109F#6PHey, older sister!\x01",
            "hurry, hurry~!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16000, -5000, -2500, 4000)

    def lambda_102A4():

        label("loc_102A4")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_102A4")

    QueueWorkItem2(0xE, 2, lambda_102A4)

    def lambda_102B6():

        label("loc_102B6")

        TurnDirection(0xFE, 0x12, 400)
        Yield()
        Jump("loc_102B6")

    QueueWorkItem2(0xA, 2, lambda_102B6)

    def lambda_102C8():

        label("loc_102C8")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_102C8")

    QueueWorkItem2(0xB, 2, lambda_102C8)

    def lambda_102DA():

        label("loc_102DA")

        TurnDirection(0xFE, 0x12, 600)
        Yield()
        Jump("loc_102DA")

    QueueWorkItem2(0xC, 2, lambda_102DA)
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
            "#13012F#5Pもう、Francったら。\x01",
            "The beach will not run away.\x02",
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

    def lambda_10483():
        OP_9B(0x0, 0xE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_10483)
    Sleep(50)

    def lambda_1049B():
        OP_9B(0x0, 0xC, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1049B)
    Sleep(50)

    def lambda_104B3():
        OP_9B(0x0, 0xA, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_104B3)
    Sleep(50)

    def lambda_104CB():
        OP_9B(0x0, 0xB, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_104CB)
    Sleep(50)

    def lambda_104E3():
        OP_9B(0x0, 0x12, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_104E3)
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
        "#3613V#30WWell, wait a minute.\x02",
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
            "#3395V#30WHuhu, bother selling umbrellas\x01",
            "Did you prepare?\x02",
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
        "#2677V#30WAs expected, you will like it.\x02",
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

    def lambda_10848():
        OP_98(0xFE, 0xFFFFFF9C, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10848)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_10877():
        OP_98(0xFE, 0xFFFFFF6A, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_10877)
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
            "#2716V#40WHey, sister.\x01",
            "#30WBecause it's so hard to go out\x01",
            "I have to appeal!\x02",
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
            "#3516V#30WWait a minute.\x01",
            "I should not push that!\x02",
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
        "#12505F#11P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2757, 255, 70, 0)
    Sleep(600)

    ChrTalk(
        0x104,
        (
            "#12809F#11PHo Ho!\x01",
            "It's nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12902F#11POh, everyone suits you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12609F#6PI wonder if that is the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12706F#6PI do not have much confidence … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13109F#5PHey, Mr. Lloyd.\x02\x03",
            "Who's swimming suit appearance\x01",
            "Which suits you best?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12511F#11PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13001F#6Pもう、Franc……！\x01",
            "I do not bother Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12902F#5PHuh, what's up?\x01",
            "I'm starting out from a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#12809F#5PHa ha ha ha.\x01",
            "Would it be awfully irritating?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#11PHa ha …\x01",
            "Yeah, it is a bit of an eye poison.\x02\x03",
            "#12502F#11P── Everyone, terribly\x01",
            "I was surprised to see you.\x02\x03",
            "#12509FGravure photograph as it is\x01",
            "It is not amusing to be taken.\x02",
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
        "#13209F#6PThank you very much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12612F#6PB, Lloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13014F#6POh, er …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#13106F#5PCuddly, Mr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12711F#6P…… I still have a bad taste.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12505F#11POh ……?\x02",
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
            "#12806F#5P(this guy……\x01",
            "Someday do not destroy yourself. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12902F#5P(Well, that is also a real boys' boss?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Female voice",
        "Okay, let me wait.\x02",
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
        "#13405F#11POw, this is amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#13309F#11PHehu ……\x01",
            "It is like heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PIt is completely blank … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#13605F#11P… …. …\x02",
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

    def lambda_112F5():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112F5)

    def lambda_1130A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1130A)

    def lambda_1131F():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1131F)

    def lambda_11334():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11334)

    def lambda_11349():

        label("loc_11349")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_11349")

    QueueWorkItem2(0xE, 2, lambda_11349)

    def lambda_1135B():

        label("loc_1135B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1135B")

    QueueWorkItem2(0xA, 2, lambda_1135B)

    def lambda_1136D():

        label("loc_1136D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1136D")

    QueueWorkItem2(0xB, 2, lambda_1136D)

    def lambda_1137F():

        label("loc_1137F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1137F")

    QueueWorkItem2(0x12, 2, lambda_1137F)

    def lambda_11391():

        label("loc_11391")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11391")

    QueueWorkItem2(0xC, 2, lambda_11391)
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
        "Huh, let me wait.\x02",
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
            "Oh, already pretty kids\x01",
            "It is surrounded by ~.\x02",
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
            "#3245V#30WOh, a parasol or something\x01",
            "You prepared, did not you?\x02",
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
            "Say it\x01",
            "I did it.\x02",
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
        "#12505F#6P#N#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#12807F#12P#N#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        "#13205F#5PBarking ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12606F#5P…… something ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13012F#11P#NIs not it beautiful ……\x01",
            "I guess they are overwhelmed ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#12706F#5PAura is different ……\x01",
            "…… It is such a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#13101F#11PIt is amazing!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13402F#6POh, you ladies too\x01",
            "I'm pretty cool.\x02\x03",
            "#13409FYeah yeah, eyuku Oshuku fuku\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#13304F#12PHehe, that's right.\x02\x03",
            "#13302FErieちゃんも思った通り\x01",
            "I'm sooo glamorous.\x02\x03",
            "#13309FKeyaちゃんもTioちゃんも\x01",
            "I'd rather hug you a cry\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12609F#5POh, haha ….\x01",
            "（Cecilさんの胸で言われても。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#5PWell, huh?\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#13509F#11PHuh … but,\x01",
            "It is a really beautiful beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#13604F#11PWell, maybe not bad ……\x02\x03",
            "#13601F─ ─ Anta,\x01",
            "How long will it take?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x10)
    OP_64(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11AF3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_11AF3)

    def lambda_11B00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11B00)

    def lambda_11B0D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11B0D)

    def lambda_11B1A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_11B1A)

    def lambda_11B27():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11B27)

    def lambda_11B34():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11B34)

    def lambda_11B41():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11B41)
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
        "#12511F#6P#NHappy\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12806F#12P#NAwesome …\x01",
            "I went to the world of momentarily tough.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#12711F#5PMan is simple.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#12PWell, compared to women\x01",
            "It is a simple creature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#13106F#11PMumumu ……\x01",
            "This may not be defeated.\x02\x03",
            "#13101FLady, let's do our best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13012F#5P#NMu, do not say no.\x02",
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
            "After that, after preparing for gymnastics\x01",
            "Each will be free at the beach … …\x02\x03",
            "ロイドはLishaと共に\x01",
            "KeyaとShuriに泳ぎの練習を\x01",
            "I will attach it.\x07\x00\x02",
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

    label("loc_11F20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1223E")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206F")
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
    Jump("loc_120CE")

    label("loc_1206F")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_120CE")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12135")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_1216D")

    label("loc_12135")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_1216D")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_121BE")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_12228")

    label("loc_121BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_121FA")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_12228")

    label("loc_121FA")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_12228")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_1223E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1229D")
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

    label("loc_1229D")

    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_122F3")
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

    label("loc_122F3")

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
            "#12502F#5Pお、いいなKeya。\x02\x03",
            "#12509FThat condition, its condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#13209F#12PWell, oh?\x02\x03",
            "#13201FAh……\x01",
            "I guessed somewhere.\x02\x03",
            "#13210FLloyd, release your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PIs not it okay?\x02\x03",
            "#12501FWell then …\x02",
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

    def lambda_1255E():

        label("loc_1255E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1255E")

    QueueWorkItem2(0x101, 2, lambda_1255E)
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
        "#13505F#11POh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12505F#5PHuh!\x02\x03",
            "#12502FKeya、やっぱり泳いだ事、\x01",
            "I thought it was a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13200F#12P#NWell, I do not know.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13605F#11POr, I'll do it … Tribe ……\x02\x03",
            "#13607FLisha姉！\x01",
            "Tell me also how to do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#5PHaha, yes yes.\x02\x03",
            "#13502FWell, to the upper body slightly\x01",
            "Because power is too much …\x02",
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

    def lambda_1271F():

        label("loc_1271F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1271F")

    QueueWorkItem2(0x9, 2, lambda_1271F)
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
            "#12509F#5PWhy, both of us\x01",
            "It was a blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13204F#12P#NElephant.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13612F#11P#NFun time.\x02\x03",
            "As I can do\x01",
            "I im nee you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#13210F#12P#Nねえねえ、Shuri！\x02\x03",
            "Swim as much as a rock!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#13611F#11P#NWhy, I ……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12509F#5PHaha, be careful.\x02\x03",
            "#12500FBoth of us, beyond the rock\x01",
            "Absolutely not going to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#13209F#12P#NLet's see!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#13607F#11P#NOh no!\x01",
            "You ought to go out with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(225, 20, 0, 5000)
    SetCameraDistance(13000, 5000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12971")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12988")
    Sleep(1)
    Jump("loc_12971")

    label("loc_12988")

    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xE, 64510, -7460, 28680, 75)
    SetChrPos(0xF, 62580, -7430, 29030, 75)

    def lambda_129CE():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_129CE)

    def lambda_129E3():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_129E3)
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
        "#12512F#11PWell, is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PHuhu, this neighborhood\x01",
            "It seems quite shallow\x01",
            "No problem.\x02\x03",
            "#13502FEven so ……\x01",
            "Keyaちゃん、凄いですね。\x02\x03",
            "A quick knack\x01",
            "I seem to have grabbed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12504F#6PYou can swim ahead of time\x01",
            "Maybe the body just remembered\x01",
            "I do not think so.\x02\x03",
            "#12500Fでも、Shuriも結構すごいよな？\x02\x03",
            "Ever before I've swam\x01",
            "I was saying it was not there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13504F#11PIn recent practice\x01",
            "The spring and suppleness of the body\x01",
            "It is reasonably trained.\x02\x03",
            "#13502FIf you teach a little trick\x01",
            "Was it in a flash?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PReally……\x01",
            "It seems that I am doing my best.\x02\x03",
            "#12505Fby the way……\x01",
            "The stage of the alkane shell,\x01",
            "Are you going to renew?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13505F#11PYes, even if it says renewal\x01",
            "\"Golden sun, silver moon\" is\x01",
            "It does not change, but ….\x02\x03",
            "#13502FShuriちゃんが新たな\x01",
            "Appear as the third \"princess\"\x01",
            "I arrange it.\x02\x03",
            "#13509FShe does not even have a main scene\x01",
            "It is added.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12F3B")

    ChrTalk(
        0x101,
        (
            "#12511F#6PThat's terrible …\x02\x03",
            "#12512FWhen I first saw you\x01",
            "To be active so quickly\x01",
            "I did not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13509F#11PHuh, you are right.\x02\x03",
            "#13510F多分、Iliaさんの導きと\x01",
            "Shuriちゃん自身の頑張りが\x01",
            "I think that it was because it was.\x02\x03",
            "#13508F…… I have been more than something ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13064")

    label("loc_12F3B")


    ChrTalk(
        0x101,
        (
            "#12505F#6PThat's terrible …\x02\x03",
            "#12501F何でも、最初はIliaさんに\x01",
            "Trying to raise an incident by repelling\x01",
            "You did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13504F#11PToo much exaggeration to the incident\x01",
            "It was not something ……\x02\x03",
            "#13510F多分、Iliaさんの導きと\x01",
            "Shuriちゃん自身の頑張りが\x01",
            "I think that it was because it was.\x02\x03",
            "#13508F…… I have been more than something ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13064")


    ChrTalk(
        0x101,
        "#12505F#6PHuh……?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#13509F#11PHaha, that's a big deal ….\x02\x03",
            "#13510FBecause I was a bit tired.\x01",
            "I am absent over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12504F#6PI see, I am tired.\x02\x03",
            "#12500FI still have time.\x01",
            "Let's enjoy non-birth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#13509F#11PYes……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57250, -5600, 29000, 6000)
    MoveCamera(235, 10, 0, 6000)
    SetCameraDistance(13500, 6000)
    OP_93(0x9, 0x10E, 0x1F4)

    def lambda_131A0():
        OP_9B(0x0, 0xFE, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_131A0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12503F#6P(Well, even so\x01",
            "Even though his spine is not that expensive ……)\x02\x03",
            "#12511F(Not ─ ─).\x02\x03",
            "#12500F(I still have time until noon,\x01",
            "Should I mix everyone? )\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_133DA")
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

    label("loc_133DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_133EF")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_133EF")

    OP_90(0x0, 40000, 0, 17000, 270)
    SetScenarioFlags(0x145, 0)
    OP_29(0xA5, 0x1, 0x3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_57_F6F1 end

    def Function_58_13416(): pass

    label("Function_58_13416")

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

    # Function_58_13416 end

    def Function_59_134A5(): pass

    label("Function_59_134A5")

    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x546, 0x5, 0x10, 0x11, 0x12, 0x13, 0x14)
    Sound(318, 0, 40, 0)
    Return()

    # Function_59_134A5 end

    def Function_60_134BD(): pass

    label("Function_60_134BD")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_60_134BD end

    def Function_61_134E8(): pass

    label("Function_61_134E8")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_61_134E8 end

    def Function_62_13513(): pass

    label("Function_62_13513")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6000, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_62_13513 end

    def Function_63_1353E(): pass

    label("Function_63_1353E")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_63_1353E end

    def Function_64_13569(): pass

    label("Function_64_13569")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4500, 0, -1500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_13569 end

    def Function_65_13594(): pass

    label("Function_65_13594")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_65_13594 end

    def Function_66_135BF(): pass

    label("Function_66_135BF")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_135BF end

    def Function_67_135EA(): pass

    label("Function_67_135EA")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 5500, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_67_135EA end

    def Function_68_13615(): pass

    label("Function_68_13615")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_13615 end

    def Function_69_13640(): pass

    label("Function_69_13640")

    OP_93(0xFE, 0xF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_69_13640 end

    def Function_70_13657(): pass

    label("Function_70_13657")

    OP_98(0xFE, 0x4B0, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_70_13657 end

    def Function_71_1366C(): pass

    label("Function_71_1366C")

    OP_98(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_71_1366C end

    def Function_72_13681(): pass

    label("Function_72_13681")

    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_72_13681 end

    def Function_73_13696(): pass

    label("Function_73_13696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13775")
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
    Jump("Function_73_13696")

    label("loc_13775")

    Return()

    # Function_73_13696 end

    def Function_74_13776(): pass

    label("Function_74_13776")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13858")
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
    Jump("Function_74_13776")

    label("loc_13858")

    Return()

    # Function_74_13776 end

    def Function_75_13859(): pass

    label("Function_75_13859")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13938")
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
    Jump("Function_75_13859")

    label("loc_13938")

    Return()

    # Function_75_13859 end

    def Function_76_13939(): pass

    label("Function_76_13939")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A1B")
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
    Jump("Function_76_13939")

    label("loc_13A1B")

    Return()

    # Function_76_13939 end

    def Function_77_13A1C(): pass

    label("Function_77_13A1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A7F")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60080, -6950, 27560)
    OP_9F(0x1, 61500, -6850, 28810)
    OP_9F(0x1, 60190, -7050, 30310)
    OP_9F(0x1, 58950, -7150, 29090)
    OP_9F(0x1, 59200, -7250, 28000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("Function_77_13A1C")

    label("loc_13A7F")

    Return()

    # Function_77_13A1C end

    def Function_78_13A80(): pass

    label("Function_78_13A80")

    SetChrPos(0xFE, 58250, -6850, 29000, 0)

    label("loc_13A91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AEA")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60250, -6750, 31000)
    OP_9F(0x1, 58250, -7200, 33000)
    OP_9F(0x1, 56250, -7250, 31000)
    OP_9F(0x1, 58250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("loc_13A91")

    label("loc_13AEA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Return()

    # Function_78_13A80 end

    def Function_79_13B10(): pass

    label("Function_79_13B10")

    SetChrPos(0xFE, 58250, -6950, 30000, 0)

    label("loc_13B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13B7A")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 59250, -6950, 31000)
    OP_9F(0x1, 58250, -7250, 32000)
    OP_9F(0x1, 57250, -7250, 31000)
    OP_9F(0x1, 58250, -6950, 30000)
    OP_9F(0x2, 0xFE, 1000, 0x6)
    Jump("loc_13B21")

    label("loc_13B7A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6950, 30000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_79_13B10 end

    def Function_80_13BA0(): pass

    label("Function_80_13BA0")

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
            "─ ─ So on the beach\x01",
            "A fun time passed.\x07\x00\x02",
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
            "Then Lloyd's promised\x01",
            "After having enjoyed watermelon splitting etc ──\x07\x00\x02",
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
            "The hotel delivered\x01",
            "While striking lunch boxes\x01",
            "It was a lot of excitement.\x07\x00\x02",
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

    # Function_80_13BA0 end

    def Function_81_13CF7(): pass

    label("Function_81_13CF7")

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

    def lambda_1412C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1412C)
    Sleep(30)

    def lambda_14144():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14144)
    Sleep(30)

    def lambda_1415C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1415C)
    Sleep(30)

    def lambda_14174():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14174)
    Sleep(30)

    def lambda_1418C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1418C)
    Sleep(30)

    def lambda_141A4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_141A4)
    Sleep(30)

    def lambda_141BC():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_141BC)
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
        "神狼Zeit",
        (
            "#01203F#3C#5PWell, I am a theme park\x01",
            "I will regret at best.\x02\x03",
            "#01200FI will signal it when I return to the original form\x01",
            "Pierce the gap and head to the mansion.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_142FB():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_142FB)
    Sleep(50)

    def lambda_1430B():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1430B)
    Sleep(50)

    def lambda_1431B():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1431B)
    Sleep(50)

    def lambda_1432B():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1432B)
    Sleep(50)

    def lambda_1433B():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1433B)
    Sleep(50)

    def lambda_1434B():
        TurnDirection(0x106, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1434B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#00013F#6PI understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PZeit……\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "神狼Zeit",
        (
            "#01200F#3C#5PHuh, you are also a nice guy.\x02\x03",
            "#01203FProtect the goddess.\x02",
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

    def lambda_1445B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1445B)

    def lambda_14468():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14468)

    def lambda_14475():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14475)

    def lambda_14482():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14482)

    def lambda_1448F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1448F)

    def lambda_1449C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1449C)
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
        "#10409F#11PHaha, I'm dependable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PWell, first of all,\x01",
            "Until the hotel's arcade ─\x02",
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
        "Voice of a man",
        "#2S#2PPleasure …!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Voice of a man",
        "#2S#2PBannings!\x02",
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

    def lambda_1466F():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1466F)
    Sleep(50)

    def lambda_1467F():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1467F)
    Sleep(50)

    def lambda_1468F():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1468F)
    Sleep(50)

    def lambda_1469F():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1469F)
    Sleep(50)

    def lambda_146AF():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_146AF)
    Sleep(50)

    def lambda_146BF():
        OP_93(0x106, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_146BF)
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
            "#00310F#11PChit\x01",
            "Have you come again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#11P敵A hunter３、軍用魔獣３！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#12PApparently quite\x01",
            "It seems to be elite ……!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00007F#11PPrepare for interception!\x01",
            "We will collaborate and destroy it!\x02",
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
        "#00307F#1K#1P#NHuh!\x02",
    )


    ChrTalk(
        0x105,
        "#10407F#1K#2P#NAh!\x02",
    )


    ChrTalk(
        0x109,
        "#10107F#1K#4P#NYes!\x02",
    )


    NpcTalk(
        0x101,
        "Lisha",
        "#10707F#1K#3P#NYes!\x02",
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

    def lambda_149E0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_149E0)

    def lambda_149F5():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_149F5)

    def lambda_14A0A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_14A0A)

    def lambda_14A1F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_14A1F)

    def lambda_14A34():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14A34)

    def lambda_14A49():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_14A49)
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

    # Function_81_13CF7 end

    def Function_82_14ADC(): pass

    label("Function_82_14ADC")

    BeginChrThread(0xFE, 0, 0, 86)
    OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_82_14ADC end

    def Function_83_14AFB(): pass

    label("Function_83_14AFB")


    def lambda_14B00():
        OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B00)
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

    # Function_83_14AFB end

    def Function_84_14B5B(): pass

    label("Function_84_14B5B")

    BeginChrThread(0xFE, 0, 0, 87)
    OP_75(0x2, 0x2, 0x0)
    SetChrPos(0xFE, 45000, -1000, 30000, 270)
    OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_84_14B5B end

    def Function_85_14B92(): pass

    label("Function_85_14B92")

    SetChrPos(0xFE, 45000, -1000, 30000, 270)

    def lambda_14BA8():
        OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BA8)
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

    # Function_85_14B92 end

    def Function_86_14C0C(): pass

    label("Function_86_14C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14C30")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_86_14C0C")

    label("loc_14C30")

    Return()

    # Function_86_14C0C end

    def Function_87_14C31(): pass

    label("Function_87_14C31")

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

    # Function_87_14C31 end

    def Function_88_14C96(): pass

    label("Function_88_14C96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14CB1")
    OP_A1(0xFE, 0xBB8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_88_14C96")

    label("loc_14CB1")

    Return()

    # Function_88_14C96 end

    def Function_89_14CB2(): pass

    label("Function_89_14CB2")

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

    # Function_89_14CB2 end

    def Function_90_14DA3(): pass

    label("Function_90_14DA3")

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

    # Function_90_14DA3 end

    def Function_91_14EC2(): pass

    label("Function_91_14EC2")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5DC0, 0x1388, 0x0)
    Return()

    # Function_91_14EC2 end

    def Function_92_14EE9(): pass

    label("Function_92_14EE9")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x4844, 0x1388, 0x0)
    Return()

    # Function_92_14EE9 end

    def Function_93_14F10(): pass

    label("Function_93_14F10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14F2E")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_93_14F10")

    label("loc_14F2E")

    Return()

    # Function_93_14F10 end

    def Function_94_14F2F(): pass

    label("Function_94_14F2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14F4D")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_94_14F2F")

    label("loc_14F4D")

    Return()

    # Function_94_14F2F end

    def Function_95_14F4E(): pass

    label("Function_95_14F4E")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x57E4, 0x1388, 0x0)
    Return()

    # Function_95_14F4E end

    def Function_96_14F86(): pass

    label("Function_96_14F86")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5208, 0x1388, 0x0)
    Return()

    # Function_96_14F86 end

    def Function_97_14FBE(): pass

    label("Function_97_14FBE")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x55F0, 0x1388, 0x0)
    Return()

    # Function_97_14FBE end

    def Function_98_14FF6(): pass

    label("Function_98_14FF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1500F")
    Sound(845, 0, 60, 0)
    Sleep(400)
    Jump("Function_98_14FF6")

    label("loc_1500F")

    Return()

    # Function_98_14FF6 end

    def Function_99_15010(): pass

    label("Function_99_15010")

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
            "#00010F#11PDamn\x01",
            "Truly a tough day …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PThey are the strongest class people!\x01",
            "You only have to go with all your power …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PLet's hurry … !.!\x01",
            "Zeitの陽動が始まります。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11POh, I'm going to arcade!\x02\x03",
            "Today all employees,\x01",
            "You ought to be leaving! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PYes, involve in battle\x01",
            "Do not worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PWell it's alright\x01",
            "It looks like we can meet each other …\x02",
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

    # Function_99_15010 end

    def Function_100_1535D(): pass

    label("Function_100_1535D")

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

    # Function_100_1535D end

    def Function_101_153F7(): pass

    label("Function_101_153F7")

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

    def lambda_158E1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_158E1)

    def lambda_158F6():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_158F6)

    def lambda_1590B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1590B)

    def lambda_15920():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_15920)

    def lambda_15935():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_15935)

    def lambda_1594A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1594A)

    def lambda_1595F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1595F)
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

    # Function_101_153F7 end

    def Function_102_15A09(): pass

    label("Function_102_15A09")

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

    # Function_102_15A09 end

    def Function_103_15B59(): pass

    label("Function_103_15B59")

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

    # Function_103_15B59 end

    def Function_104_15C10(): pass

    label("Function_104_15C10")

    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1770, 0x0)
    Return()

    # Function_104_15C10 end

    def Function_105_15C20(): pass

    label("Function_105_15C20")

    OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x1770, 0x0)
    Return()

    # Function_105_15C20 end

    def Function_106_15C30(): pass

    label("Function_106_15C30")

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
        "#00005F#11Pthis is……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PZeitの陽動です！\x02",
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

    # Function_106_15C30 end

    def Function_107_15EAD(): pass

    label("Function_107_15EAD")

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

    # Function_107_15EAD end

    def Function_108_15F47(): pass

    label("Function_108_15F47")

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
            "#10702F#11PAt the theme park\x01",
            "The battle seems to have begun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#5POK, in this gap\x01",
            "Go through the arcade!\x02",
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

    # Function_108_15F47 end

    def Function_109_16111(): pass

    label("Function_109_16111")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_1617D")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_16197")

    label("loc_1617D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16191")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_16197")

    label("loc_16191")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_16197")

    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87050.itc", 0x26)
    LoadChrToIndex("monster/ch87250.itc", 0x27)
    LoadChrToIndex("monster/ch87350.itc", 0x28)
    LoadChrToIndex("monster/ch87450.itc", 0x29)
    LoadChrToIndex("monster/ch87550.itc", 0x2A)
    Call(0, 113)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_161D8")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_161F2")

    label("loc_161D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_161EC")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_161F2")

    label("loc_161EC")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_161F2")

    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Call(0, 126)
    Return()

    # Function_109_16111 end

    def Function_110_16214(): pass

    label("Function_110_16214")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_162B5")
    SetChrChipByIndex(0xEF, 0x20)
    Jump("loc_162CB")

    label("loc_162B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_162C7")
    SetChrChipByIndex(0xEF, 0x21)
    Jump("loc_162CB")

    label("loc_162C7")

    SetChrChipByIndex(0xEF, 0x22)

    label("loc_162CB")

    SetChrPos(0x101, 40230, -6910, 1770, 135)
    SetChrPos(0x153, 42190, -7020, 1260, 270)
    SetChrPos(0xEF, 40720, -6970, -210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#12503FLet's start a strategy now.\x02\x03",
            "#12500FMay I explain as I said?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_164F4")

    ChrTalk(
        0x102,
        (
            "#6P#12600FYeah, playing with the beach\x01",
            "You are pricking a monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、Thank you.\x02\x03",
            "#12503FEven just for now\x01",
            "It is a monster with funny character.\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#12601FYeah, I know.\x02\x03",
            "#12603FTo eliminate demonic animals that cut through swimsuits,\x01",
            "I was surprised to be asked suddenly, but …\x02\x03",
            "#12600FIt is also for Bell,\x01",
            "I will cooperate by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、Erie！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16833")

    label("loc_164F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16692")

    ChrTalk(
        0x103,
        (
            "#6P#12700FYeah, playing with the beach\x01",
            "I am anxious about monsters.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、Thank you.\x02\x03",
            "#12503FEven just for now\x01",
            "It is a monster with funny character.\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#12700FYes, of course.\x02\x03",
            "#12703FExtermination of monsters slitting swimsuits,\x01",
            "I was surprised to be asked suddenly … …\x02\x03",
            "#12701FWickedness at Missi's knees,\x01",
            "I can not forgive it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、Tio！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16833")

    label("loc_16692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16833")

    ChrTalk(
        0x109,
        (
            "#6P#13000FYes, play with the beach\x01",
            "I am anxious about monsters!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、Thank you.\x02\x03",
            "#12503FEven just for now\x01",
            "It is a monster with funny character.\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#13000FYes, of course!\x02\x03",
            "#13003FTo eliminate demonic animals that cut through swimsuits,\x01",
            "I was surprised to be asked suddenly, but ……\x02\x03",
            "#13000FFor everyone who plays at the beach,\x01",
            "Let 's do our best and get rid of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、Noel！\x02",
    )

    CloseMessageWindow()

    label("loc_16833")

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
        "#6P#12500FThat.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16991")

    ChrTalk(
        0x102,
        "#12602FKyat, if it is already Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12606F…… Well, even a monstrous beast\x01",
            "It does not come out easily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A80")

    label("loc_16991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16A0A")

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
            "#12706F…… Anyway, with devils\x01",
            "It does not come out easily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A80")

    label("loc_16A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16A80")

    ChrTalk(
        0x109,
        "#13002FYou did it!\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x109,
        (
            "#13006F…… Well, even a monstrous beast\x01",
            "It does not come out easily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A80")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#12505FOh, maybe\x01",
            "警戒しているMaybe.\x02\x03",
            "#12503FHowever, there is no doubt that there are demons.\x01",
            "Look at the situation here ……\x02",
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
        "#6P#12511FWow!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16BB4")

    ChrTalk(
        0x102,
        "#12609FHuhu, give back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C0B")

    label("loc_16BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16BE1")

    ChrTalk(
        0x103,
        "#12704F… It is your wallkeeper.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C0B")

    label("loc_16BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16C0B")

    ChrTalk(
        0x109,
        "#13009FHaha, that is a return.\x02",
    )

    CloseMessageWindow()

    label("loc_16C0B")


    ChrTalk(
        0x101,
        "#6P#12512FOh, you did it …!\x02",
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
            "#5P#13206F（あーあ、Keyaも\x01",
            "I want to play with Lloyd's. )\x02\x03",
            "#13208F(Ked told me that it was dangerous,\x01",
            "It looks fun for us … …)\x02\x03",
            "#13205F(…… That?\x02",
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
        "#13205FAh……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17157")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4SErieっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#12605Feh……\x02",
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
        "#12615F#4S─ ─ Chaaaaaa! It is! Is it? Is it?\x02",
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

    def lambda_1708B():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1708B)
    Sleep(1000)

    def lambda_170A8():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_170A8)

    ChrTalk(
        0x101,
        "#6P#12511Fエ、Erieッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x102,
        (
            "#12613FHere, this is good … …\x01",
            "Follow the devil! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FWow, I understand! It is!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_177EA")

    label("loc_17157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_174A3")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4STioっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#12705FHuh……\x02",
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
        "#12710F#4S─ ─ cash …! It is! Is it? Is it?\x02",
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

    def lambda_173DB():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_173DB)
    Sleep(1000)

    def lambda_173F8():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_173F8)

    ChrTalk(
        0x101,
        "#6P#12511Fティ、Tioッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x103,
        (
            "#12701FHere, this is good … …\x01",
            "Hurry up, demons! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FWow, I understand! It is!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_177EA")

    label("loc_174A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_177EA")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#13207F#4SNoelっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#13005FHuh……\x02",
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
        "#13014F#4S── Haa … …! It is! Is it? Is it?\x02",
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

    def lambda_17727():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17727)
    Sleep(1000)

    def lambda_17744():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17744)

    ChrTalk(
        0x101,
        "#6P#12511Fノ、Noelッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    ChrTalk(
        0x109,
        (
            "#13006FHere, as this is good,\x01",
            "Track the monsters … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#12501FWow, I understand! It is!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x4, 0x3, 0x2)

    label("loc_177EA")


    def lambda_177EF():
        OP_95(0xFE, 34050, -6300, 8750, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_177EF)
    Sleep(100)

    def lambda_1780C():
        OP_99(0xFE, 0xEF, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1780C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_178A5")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_178C8")

    label("loc_178A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_178B9")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_178C8")

    label("loc_178B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_178C8")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x52, 0xFF)

    label("loc_178C8")


    def lambda_178CD():
        OP_95(0xFE, 9860, -6000, -21850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_178CD)
    Sleep(2000)

    def lambda_178EA():
        OP_95(0xFE, 11690, -6000, -17960, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_178EA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(10060, -5780, -20380, 6000)
    MoveCamera(246, 22, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(12250, 6000)
    WaitChrThread(0x24, 1)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_17955():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17955)
    Sleep(1000)

    def lambda_17965():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17965)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00006FHa ha, then …\x01",
            "O, I'm chasing you! It is!\x02\x03",
            "#00001FI do not want to slash the women's swimsuit\x01",
            "Sneaky act … … no more,\x01",
            "I can not forgive you!\x02",
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
        "#12P#00007FSleep! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_110_16214 end

    def Function_111_17A92(): pass

    label("Function_111_17A92")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17ABF")

    def lambda_17AA2():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17AA2)
    WaitChrThread(0xFE, 2)
    Jump("Function_111_17A92")

    label("loc_17ABF")

    Return()

    # Function_111_17A92 end

    def Function_112_17AC0(): pass

    label("Function_112_17AC0")

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

    # Function_112_17AC0 end

    def Function_113_17BAF(): pass

    label("Function_113_17BAF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17BC7")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_17BEE")

    label("loc_17BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17BDD")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_17BEE")

    label("loc_17BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17BEE")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_17BEE")

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
            "#12P#00000FHow is it …?\x01",
            "I will have an idea!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9490, -5480, -21070, 3000)

    def lambda_17DC0():
        OP_99(0xFE, 0x24, 0xBB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DC0)
    Sleep(500)

    def lambda_17DD7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17DD7)
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

    def lambda_17E5D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17E5D)
    Sleep(100)

    def lambda_17E6D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17E6D)

    ChrTalk(
        0x101,
        "#12P#00005Fwhat……! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_17E95():
        OP_95(0xFE, 23660, -2000, -35810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_17E95)
    Sleep(100)

    def lambda_17EB2():
        OP_95(0xFE, 24940, -2000, -35780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_17EB2)
    Sleep(100)

    def lambda_17ECF():
        OP_95(0xFE, 21250, -2000, -36870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_17ECF)
    Sleep(100)

    def lambda_17EEC():
        OP_95(0xFE, 21590, -2000, -35820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_17EEC)
    Sleep(100)

    def lambda_17F09():
        OP_95(0xFE, 23090, -2000, -36580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_17F09)
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
        "#00011FHey, there was a friend! Is it?\x02",
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
        "#11P#00010FDamn\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xEF, 0x80)
    ClearChrFlags(0x153, 0x80)

    NpcTalk(
        0x153,
        "Keyaの声",
        "#4SLloyd's! It is!\x02",
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

    def lambda_182B1():
        OP_95(0xFE, 15180, -6000, -13330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_182B1)

    def lambda_182CB():
        OP_95(0xFE, 15380, -6000, -15880, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_182CB)

    def lambda_182E5():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_182E5)

    def lambda_182F2():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_182F2)

    def lambda_182FF():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_182FF)

    def lambda_1830C():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1830C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18391")
    Sound(805, 0, 100, 0)
    Jump("loc_18397")

    label("loc_18391")

    Sound(531, 0, 100, 0)

    label("loc_18397")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18412")

    ChrTalk(
        0x101,
        (
            "#00005FErie、Keya！\x01",
            "……Are you OK! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FAfter the story!\x01",
            "Let's beat the monster now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1850A")

    label("loc_18412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1848E")

    ChrTalk(
        0x101,
        (
            "#00005FTio、Keya！\x01",
            "……Are you OK! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F… … The story is back!\x01",
            "Let's get rid of monsters now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1850A")

    label("loc_1848E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1850A")

    ChrTalk(
        0x101,
        (
            "#00005FNoel、Keya！\x01",
            "……Are you OK! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FYes, yes! It is!\x01",
            "Anyway now you can trash the monster\x01",
            "Let's get rid of!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1850A")


    ChrTalk(
        0x101,
        "#00000FOh, I understand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01107FBoth of you, Fight!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_98C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_113_17BAF end

    def Function_114_18566(): pass

    label("Function_114_18566")

    OP_93(0x25, 0x13B, 0x1F4)
    OP_A1(0x25, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_114_18566 end

    def Function_115_18579(): pass

    label("Function_115_18579")

    OP_93(0x26, 0x13B, 0x1F4)
    OP_A1(0x26, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_115_18579 end

    def Function_116_1858C(): pass

    label("Function_116_1858C")

    OP_93(0x27, 0x13B, 0x1F4)
    OP_A1(0x27, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_116_1858C end

    def Function_117_1859F(): pass

    label("Function_117_1859F")

    OP_93(0x28, 0x13B, 0x1F4)
    OP_A1(0x28, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_117_1859F end

    def Function_118_185B2(): pass

    label("Function_118_185B2")

    OP_93(0x29, 0x13B, 0x1F4)
    OP_A1(0x29, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_118_185B2 end

    def Function_119_185C5(): pass

    label("Function_119_185C5")

    OP_A1(0x25, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x25, 0x50BE, 0xFFFFE890, 0xFFFF9A34, 0x7D0, 0x1388)
    OP_95(0x25, 10410, -6000, -16510, 5000, 0x0)
    TurnDirection(0x25, 0x101, 500)
    Return()

    # Function_119_185C5 end

    def Function_120_18605(): pass

    label("Function_120_18605")

    OP_A1(0x26, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x26, 0x4C22, 0xFFFFE890, 0xFFFF952A, 0x7D0, 0x1388)
    OP_95(0x26, 8150, -6000, -20170, 5000, 0x0)
    TurnDirection(0x26, 0x101, 500)
    Return()

    # Function_120_18605 end

    def Function_121_18645(): pass

    label("Function_121_18645")

    OP_A1(0x27, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x27, 0x5942, 0xFFFFE890, 0xFFFF94DA, 0x7D0, 0x1388)
    OP_95(0x27, 12360, -6000, -15910, 5000, 0x0)
    TurnDirection(0x27, 0x101, 500)
    Return()

    # Function_121_18645 end

    def Function_122_18685(): pass

    label("Function_122_18685")

    OP_A1(0x28, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x28, 0x4A4C, 0xFFFFE890, 0xFFFF9098, 0x7D0, 0x1388)
    OP_95(0x28, 13700, -6000, -22060, 5000, 0x0)
    TurnDirection(0x28, 0x101, 500)
    Return()

    # Function_122_18685 end

    def Function_123_186C5(): pass

    label("Function_123_186C5")

    OP_A1(0x29, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x29, 0x51E0, 0xFFFFE890, 0xFFFF93CC, 0x7D0, 0x1388)
    OP_95(0x29, 14480, -6000, -18580, 5000, 0x0)
    TurnDirection(0x29, 0x101, 500)
    Return()

    # Function_123_186C5 end

    def Function_124_18705(): pass

    label("Function_124_18705")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1872E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_18710")

    label("loc_1872E")

    Return()

    # Function_124_18705 end

    def Function_125_1872F(): pass

    label("Function_125_1872F")

    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    Return()

    # Function_125_1872F end

    def Function_126_18748(): pass

    label("Function_126_18748")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_187EC")
    Sound(531, 0, 100, 0)

    label("loc_187EC")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006FFuu …\x01",
            "I managed to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FBoth of you, good tire.\x02",
    )

    CloseMessageWindow()

    def lambda_18855():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_18855)
    Sleep(100)

    def lambda_18865():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18865)
    Sleep(500)

    ChrTalk(
        0x153,
        "#12P#01109FGood evening to you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_189EA")

    ChrTalk(
        0x102,
        (
            "#6P#00104FFor now,\x01",
            "I feel like I'm feeling sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F……その、Erie。\x02\x03",
            "#00006FSomehow ……\x01",
            "守ってやれなくてI'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x102,
        (
            "#6P#00112FWell, please do not mind anymore.\x01",
            "I also had a place I was careless … …\x02\x03",
            "#00103FBesides that, why such a devil is\x01",
            "I wonder if it appeared on the beach ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C70")

    label("loc_189EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18B2F")

    ChrTalk(
        0x103,
        (
            "#6P#00204FFor now,\x01",
            "Are you feeling sorry for one case?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F……その、Tio。\x02\x03",
            "#00006FSomehow ……\x01",
            "守ってやれなくてI'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x103,
        (
            "#6P#00203F…… I do not notice.\x01",
            "I was also careless … …\x02\x03",
            "#00200FBesides that, why such a devil is\x01",
            "It probably appeared on the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C70")

    label("loc_18B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_18C70")

    ChrTalk(
        0x109,
        "#6P#10109FWith this, it is incorrectly postponed!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F……その、Noel。\x02\x03",
            "#00006FSomehow ……\x01",
            "守ってやれなくてI'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    ChrTalk(
        0x109,
        (
            "#6P#10112FDo not worry about that!\x01",
            "I also had a discontent … …\x02\x03",
            "#10105FBesides that, why such a devil is\x01",
            "It must have appeared on the beach, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C70")


    ChrTalk(
        0x101,
        (
            "#00006FThis is my speculation ….\x01",
            "Perhaps it is influence of development.\x02\x03",
            "#00001FA monster who lost his way in development,\x01",
            "I began harassing humans to hurry … …\x01",
            "The best thing comes down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18E78")

    ChrTalk(
        0x102,
        (
            "#6P#00103FIndeed … It seems likely.\x02\x03",
            "#00101FEven the bathing suit was torn down,\x01",
            "With that I saw a big fuss\x01",
            "I wonder if she has stopped taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F…… That way\x01",
            "It's kawaiisho.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCertainly …\x02\x03",
            "#00000F… Well, for now\x01",
            "To the Carminas\x01",
            "I will go report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FWell, let's do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1912D")

    label("loc_18E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18FD1")

    ChrTalk(
        0x103,
        (
            "#6P#00203FIndeed … It seems likely.\x02\x03",
            "#00200FEven the bathing suit was torn down,\x01",
            "With that I saw a big fuss\x01",
            "Does that mean you were tasting the taste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F…… That way\x01",
            "It's kawaiisho.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCertainly …\x02\x03",
            "#00000F… Well, for now\x01",
            "To the Carminas\x01",
            "I will go report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1912D")

    label("loc_18FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1912D")

    ChrTalk(
        0x109,
        (
            "#6P#10103FIndeed … It seems likely.\x02\x03",
            "#10101FEven the bathing suit was torn down,\x01",
            "With that I saw a big fuss\x01",
            "Is it a place that has stopped taste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108F…… That way\x01",
            "It's kawaiisho.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCertainly …\x02\x03",
            "#00000F… Well, for now\x01",
            "To the Carminas\x01",
            "I will go report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYes, let's go!\x02",
    )

    CloseMessageWindow()

    label("loc_1912D")

    StopSound(136, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("t1320", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_126_18748 end

    SaveToFile()

Try(main)
