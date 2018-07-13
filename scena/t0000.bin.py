from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0000.bin",                # FileName
        "t0000",                    # MapName
        "t0000",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0000",                  # 0
        "Camille",                # 1
        "Elkin",                  # 2
        "Pooley",                 # 3
        "Stefan",                 # 4
        "Derrick",                # 5
        "Minneth",                # 6
        "Aretha",                 # 7
        "Sophia",                 # 8
        "Colin",                  # 9
        "Bracer Scott",           # 10
        "バス",                   # 11
        "Special Support Vehicle",# 12
        "メルカバ玖号機",         # 13
        "メルカバ光学迷彩",       # 14
        "メルカバ影",             # 15
        "Keith",                  # 16
        "Bracer Ling",            # 17
        "Bracer Eolia",           # 18
        "Ange",                   # 19
        "Gｷfan",                 # 20
        "Sealy",                  # 21
        "Village Chief Tolta",    # 22
        "Pete",                   # 23
        "Harold",                 # 24
        "猫型魔獣",               # 25
        "猫型魔獣",               # 26
        "猫型魔獣",               # 27
        "猫型魔獣",               # 28
        "猫型魔獣",               # 29
        "Black Transport",        # 30
        "Alm",                    # 31
        "Aerie",                  # 32
        "SE制御",                 # 33
        "bt0000",                 # 34
        "bt0000",                 # 35
        "Armorica Old Road",      # 36
    ))

    ATBonus("ATBonus_6B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_6D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_758", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_75C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_760", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_764", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_768", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_76C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_774", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32000.dat", "ms32100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7451", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7B8", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32001.dat", "ms32101.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7452", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24600.itc",                   # 00
        "chr/ch24400.itc",                   # 01
        "chr/ch24700.itc",                   # 02
        "chr/ch20600.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch45200.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch09400.itc",                   # 07
        "chr/ch07200.itc",                   # 08
        "chr/ch27200.itc",                   # 09
        "chr/ch46300.itc",                   # 0A
        "chr/ch46200.itc",                   # 0B
    ))

    DeclNpc(4294960427, 0,       24790,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8409,    0,       4294954817, 17,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294961186, 0,       23270,   315,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294959467, 0,       23860,   107,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(12779,   3500,    40220,   298,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294966796, 500,     6000,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11369,   0,       19389,   280,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10010,   0,       19659,   280,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294958597, 0,       25250,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3170,    0,       14229,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2119,    0,       13670,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 33,  8.40999984741211,      -12.479999542236328,   -1.0,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -1.6820000410079956,   2.496000051498413,     0.3333333432674408,    1.0])
    DeclEvent(0x0000, 0, 34,  -2.130000114440918,    12.520000457763672,    -1.100000023841858,    270.27362060546875,    [0.24330902099609375,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1250000149011612,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333730697632,    0.0,                   0.5182482600212097,    -1.565000295639038,    0.366666704416275,     1.0])
    DeclEvent(0x0000, 0, 64,  0.5400000214576721,    -8.800000190734863,    -0.0,                  144.0,                 [0.16666655242443085,  0.10825320333242416,   -0.0,                  0.0,                   -0.2886752188205719,   0.06249995902180672,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -2.6303420066833496,   0.49154290556907654,   -0.0,                  1.0])

    DeclActor(4294965296, 0,       4294952296, 1500,    4294965296, 1500,    4294952296, 0x007C, 0,  23, 0x0000)
    DeclActor(11740,   0,       3950,    1200,    10890,   4294965846, 1210,    0x007C, 0,  24, 0x0000)
    DeclActor(15990,   0,       4294947856, 1200,    15990,   2000,    4294947856, 0x007C, 0,  22, 0x0000)
    DeclActor(4294949996, 3500,    63700,   1500,    4294926296, 1000,    91000,   0x007C, 0,  22, 0x0000)
    DeclActor(15550,   3520,    47700,   1200,    15550,   4520,    47700,   0x007C, 0,  65, 0x0000)

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "Armorica Old Road")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2404, 0)                                       # 0

    ScpFunction((
        "Function_0_964",          # 00, 0
        "Function_1_A1C",          # 01, 1
        "Function_2_12CF",         # 02, 2
        "Function_3_175B",         # 03, 3
        "Function_4_185E",         # 04, 4
        "Function_5_1971",         # 05, 5
        "Function_6_19A7",         # 06, 6
        "Function_7_19F8",         # 07, 7
        "Function_8_1A8C",         # 08, 8
        "Function_9_348D",         # 09, 9
        "Function_10_4003",        # 0A, 10
        "Function_11_42A4",        # 0B, 11
        "Function_12_4891",        # 0C, 12
        "Function_13_50EF",        # 0D, 13
        "Function_14_5A78",        # 0E, 14
        "Function_15_5B9B",        # 0F, 15
        "Function_16_5C5E",        # 10, 16
        "Function_17_5E2D",        # 11, 17
        "Function_18_5EFA",        # 12, 18
        "Function_19_5FA0",        # 13, 19
        "Function_20_63A5",        # 14, 20
        "Function_21_6520",        # 15, 21
        "Function_22_6616",        # 16, 22
        "Function_23_694F",        # 17, 23
        "Function_24_69A3",        # 18, 24
        "Function_25_6A68",        # 19, 25
        "Function_26_6CAA",        # 1A, 26
        "Function_27_7F8B",        # 1B, 27
        "Function_28_94C3",        # 1C, 28
        "Function_29_968F",        # 1D, 29
        "Function_30_C44F",        # 1E, 30
        "Function_31_C563",        # 1F, 31
        "Function_32_C580",        # 20, 32
        "Function_33_CA50",        # 21, 33
        "Function_34_D4A8",        # 22, 34
        "Function_35_13B1C",       # 23, 35
        "Function_36_13B50",       # 24, 36
        "Function_37_13B84",       # 25, 37
        "Function_38_13BB8",       # 26, 38
        "Function_39_13BEC",       # 27, 39
        "Function_40_13C20",       # 28, 40
        "Function_41_13C54",       # 29, 41
        "Function_42_13C88",       # 2A, 42
        "Function_43_13CBC",       # 2B, 43
        "Function_44_13CF0",       # 2C, 44
        "Function_45_13D24",       # 2D, 45
        "Function_46_13D58",       # 2E, 46
        "Function_47_13D8C",       # 2F, 47
        "Function_48_13DC0",       # 30, 48
        "Function_49_13DF4",       # 31, 49
        "Function_50_13E28",       # 32, 50
        "Function_51_13E50",       # 33, 51
        "Function_52_13E73",       # 34, 52
        "Function_53_13EE8",       # 35, 53
        "Function_54_13F71",       # 36, 54
        "Function_55_13FE6",       # 37, 55
        "Function_56_1406F",       # 38, 56
        "Function_57_140E4",       # 39, 57
        "Function_58_1412F",       # 3A, 58
        "Function_59_1417A",       # 3B, 59
        "Function_60_141C5",       # 3C, 60
        "Function_61_14210",       # 3D, 61
        "Function_62_1425B",       # 3E, 62
        "Function_63_142BA",       # 3F, 63
        "Function_64_142D4",       # 40, 64
        "Function_65_145D8",       # 41, 65
        "Function_66_14AB9",       # 42, 66
        "Function_67_15142",       # 43, 67
        "Function_68_15170",       # 44, 68
        "Function_69_151B2",       # 45, 69
        "Function_70_151F4",       # 46, 70
        "Function_71_15236",       # 47, 71
        "Function_72_15278",       # 48, 72
        "Function_73_152BA",       # 49, 73
        "Function_74_152FC",       # 4A, 74
        "Function_75_159D7",       # 4B, 75
        "Function_76_15A19",       # 4C, 76
        "Function_77_16B05",       # 4D, 77
        "Function_78_170B1",       # 4E, 78
        "Function_79_170F6",       # 4F, 79
        "Function_80_17144",       # 50, 80
        "Function_81_171A9",       # 51, 81
        "Function_82_174AB",       # 52, 82
        "Function_83_174D6",       # 53, 83
        "Function_84_17501",       # 54, 84
        "Function_85_1752C",       # 55, 85
        "Function_86_1755B",       # 56, 86
        "Function_87_1837C",       # 57, 87
        "Function_88_1845D",       # 58, 88
        "Function_89_18473",       # 59, 89
    ))


    def Function_0_964(): pass

    label("Function_0_964")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9A4"),
        (1, "loc_9B0"),
        (2, "loc_9BC"),
        (3, "loc_9C8"),
        (4, "loc_9D4"),
        (5, "loc_9E0"),
        (6, "loc_9EC"),
        (SWITCH_DEFAULT, "loc_9F8"),
    )


    label("loc_9A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A1B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A1B")

    Return()

    # Function_0_964 end

    def Function_1_A1C(): pass

    label("Function_1_A1C")

    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A5B")
    SetChrPos(0x9, 11050, 0, -22040, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -19420, 3500, 60540, 330)
    Jump("loc_C7C")

    label("loc_A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ADA")
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrPos(0xB, -6700, 0, 25250, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5850, 0, 15680, 175)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_AD5")

    Jump("loc_C7C")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AFE")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18860, 3500, 52530, 240)
    Jump("loc_C7C")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B66")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 7300, 0, -11420, 135)
    TurnDirection(0x9, 0xC, 0)
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B61")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_B61")

    Jump("loc_C7C")

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B74")
    Jump("loc_C7C")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B96")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_C7C")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BA4")
    Jump("loc_C7C")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_END)), "loc_BBB")
    SetChrFlags(0x9, 0x10)

    label("loc_BBB")

    Jump("loc_C7C")

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE2")
    SetChrFlags(0x9, 0x80)

    label("loc_BE2")

    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C13")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_C7C")

    label("loc_C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C30")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C52")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C65")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C73")
    Jump("loc_C7C")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7C")

    label("loc_C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D09")
    SetScenarioFlags(0x38, 0)

    label("loc_D09")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    SetScenarioFlags(0x38, 1)

    label("loc_D1F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    SetScenarioFlags(0x38, 2)

    label("loc_D35")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    SetScenarioFlags(0x38, 3)

    label("loc_D4B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x38, 4)

    label("loc_D61")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    SetScenarioFlags(0x38, 5)

    label("loc_D77")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8D")
    SetScenarioFlags(0x38, 6)

    label("loc_D8D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA3")
    SetScenarioFlags(0x38, 7)

    label("loc_DA3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    SetScenarioFlags(0x39, 0)

    label("loc_DB9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    SetScenarioFlags(0x39, 1)

    label("loc_DCF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5")
    SetScenarioFlags(0x39, 2)

    label("loc_DE5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFB")
    SetScenarioFlags(0x39, 3)

    label("loc_DFB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E11")
    SetScenarioFlags(0x39, 4)

    label("loc_E11")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    SetScenarioFlags(0x39, 5)

    label("loc_E27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D")
    SetScenarioFlags(0x39, 6)

    label("loc_E3D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E53")
    SetScenarioFlags(0x39, 7)

    label("loc_E53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E69")
    SetScenarioFlags(0x3A, 0)

    label("loc_E69")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")
    SetScenarioFlags(0x3A, 1)

    label("loc_E7F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E95")
    SetScenarioFlags(0x3A, 2)

    label("loc_E95")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB")
    SetScenarioFlags(0x3A, 3)

    label("loc_EAB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC1")
    SetScenarioFlags(0x3A, 4)

    label("loc_EC1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED7")
    SetScenarioFlags(0x3A, 5)

    label("loc_ED7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EED")
    SetScenarioFlags(0x3A, 6)

    label("loc_EED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F03")
    SetScenarioFlags(0x3A, 7)

    label("loc_F03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    SetScenarioFlags(0x3B, 0)

    label("loc_F19")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2F")
    SetScenarioFlags(0x3B, 1)

    label("loc_F2F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F45")
    SetScenarioFlags(0x3B, 2)

    label("loc_F45")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5B")
    SetScenarioFlags(0x3B, 3)

    label("loc_F5B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F71")
    SetScenarioFlags(0x3B, 4)

    label("loc_F71")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F87")
    SetScenarioFlags(0x3B, 5)

    label("loc_F87")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9D")
    SetScenarioFlags(0x3B, 6)

    label("loc_F9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB3")
    SetScenarioFlags(0x3B, 7)

    label("loc_FB3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC9")
    SetScenarioFlags(0x3D, 5)

    label("loc_FC9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    SetScenarioFlags(0x3D, 6)

    label("loc_FDF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF5")
    SetScenarioFlags(0x3D, 7)

    label("loc_FF5")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1030")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1120")

    label("loc_1030")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1053")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1120")

    label("loc_1053")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1120")

    label("loc_1076")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1120")

    label("loc_1099")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BC")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1120")

    label("loc_10BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1120")

    label("loc_10DF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1120")

    label("loc_1102")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    SetScenarioFlags(0x3C, 7)

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1136")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117E")
    SetChrPos(0x0, 15150, 0, -19900, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 7)

    label("loc_117E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_11B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B1")
    SetChrPos(0x0, -17300, 3500, 63700, 150)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_11DB")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D8")
    Event(0, 86)
    Jump("loc_11DB")

    label("loc_11D8")

    Event(0, 6)

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F2")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 25)
    Jump("loc_1232")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1209")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 4)
    Event(0, 66)
    Jump("loc_1232")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1220")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 4)
    Event(0, 74)
    Jump("loc_1232")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1232")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 76)

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1248")
    Event(0, 77)
    Jump("loc_12CE")

    label("loc_1248")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1267")
    Event(0, 81)
    Jump("loc_12CE")

    label("loc_1267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129C")
    Event(0, 32)
    Jump("loc_12CE")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CE")
    SetMapFlags(0x10000000)
    Event(0, 86)

    label("loc_12CE")

    Return()

    # Function_1_A1C end

    def Function_2_12CF(): pass

    label("Function_2_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_12E1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_12F5")
    OP_24(0x7B)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_132B")

    label("loc_12F5")

    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1346")
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_1346")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1366")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_14FA")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1393")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13C0")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D4")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_14FA")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1454")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144F")
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x25)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    OP_74(0xD, 0x1E)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 13000, 0, -11540, 20)
    OP_D5(0x25, 0x0, 0x4E20, 0x0, 0x0)

    label("loc_144F")

    Jump("loc_14FA")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1492")
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147A")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_147A")

    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14A6")
    ClearMapObjFlags(0xD, 0x4)
    Jump("loc_14FA")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_14FA")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14C2")
    Jump("loc_14FA")

    label("loc_14C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14E3")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_14E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14F1")
    Jump("loc_14FA")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14FA")

    label("loc_14FA")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151B")
    OP_66(0x4, 0x1)

    label("loc_151B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_154A")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_157C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1686")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "flower00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x1, 0x1)
    Jump("loc_16C6")

    label("loc_1686")

    SetMapObjFrame(0xFF, "flower00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x0, 0x1)

    label("loc_16C6")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_16FD")
    ClearMapObjFlags(0x11, 0x4)

    label("loc_16FD")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 10890, -1450, 1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175A")
    OP_1B(0x0, 0x0, 0x59)

    label("loc_175A")

    Return()

    # Function_2_12CF end

    def Function_3_175B(): pass

    label("Function_3_175B")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Entrance\x01",      # 0
            "Tangram Gate\x01",                      # 1
            "Bus Stop (Fork in the Road)\x01",       # 2
            "Quit\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1811")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1856")

    label("loc_1811")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1836")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1856")

    label("loc_1836")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1856")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_1856")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_3_175B end

    def Function_4_185E(): pass

    label("Function_4_185E")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_196D")
    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -400, 0, -15300, 135)
    SetChrPos(0x1, -1230, 0, -15500, 135)
    SetChrPos(0x2, -2000, 0, -15700, 135)
    SetChrPos(0x3, -2750, 0, -15900, 135)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_196D")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_4_185E end

    def Function_5_1971(): pass

    label("Function_5_1971")

    OP_95(0x12, 10630, 0, -20520, 4000, 0x0)
    OP_9E(0x12, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xFA0, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_5_1971 end

    def Function_6_19A7(): pass

    label("Function_6_19A7")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -700, 0, -13900, 135)
    OP_31(0x1)
    OP_68(-690, 1500, -13900, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    EventEnd(0x5)
    Return()

    # Function_6_19A7 end

    def Function_7_19F8(): pass

    label("Function_7_19F8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1A53")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A48")
    Sound(2502, 255, 100, 0)
    Jump("loc_1A4E")

    label("loc_1A48")

    Sound(2503, 255, 100, 0)

    label("loc_1A4E")

    Jump("loc_1A77")

    label("loc_1A53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A71")
    Sound(3347, 255, 100, 0)
    Jump("loc_1A77")

    label("loc_1A71")

    Sound(3348, 255, 100, 0)

    label("loc_1A77")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19F8 end

    def Function_8_1A8C(): pass

    label("Function_8_1A8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA0")

    ChrTalk(
        0x9,
        (
            "H-How shocking... \x01",
            "Just what is that big tree!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter how you think about it, something\x01",
            "like that appearing all of a sudden is not normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You mean to tell me my enjoyable, peaceful\x01",
            "days of driving can't come back anymore...!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C5A")

    label("loc_1BA0")


    ChrTalk(
        0x9,
        (
            "Something like that appeared all of a sudden...\x01",
            "What's going to happen to Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You mean to tell me my enjoyable, peaceful\x01",
            "days of driving can't come back anymore...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5A")

    Jump("loc_3489")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7D")

    ChrTalk(
        0x9,
        (
            "There was that independence\x01",
            "declaration of invalidity, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly, I prefer the old Crossbell where\x01",
            "I could enjoy my drives unrestrained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I didn't understand things like\x01",
            "independence. I just hope everything\x01",
            "goes back to how it used to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E67")

    label("loc_1D7D")


    ChrTalk(
        0x9,
        (
            "More than an independent state,\x01",
            "I prefer the old Crossbell where\x01",
            "I could enjoy my drives unrestrained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems there was an independence declaration\x01",
            "of invalidity, but I just hope everything\x01",
            "goes back to how it used to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E67")

    Jump("loc_3489")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")

    ChrTalk(
        0x9,
        (
            "With the highway movement restrictions,\x01",
            "hardly any buses or cars come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the State Guard armored vehicles\x01",
            "that sometimes come here are cool but...\x01",
            "Honestly, I'm tired of looking at them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because "Cryptids" have appeared,\x01",
            "I can't even drive as I please...\x01",
            "How long is this going to go on!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_208B")

    label("loc_1FC0")


    ChrTalk(
        0x9,
        (
            "With the highway movement restrictions, \x01",
            "only State Guard armored vehicles\x01",
            "pass by every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because "Cryptids" have\x01",
            "appeared, I can't even drive...\x01",
            "How long is this going to go on!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208B")

    Jump("loc_3489")

    label("loc_2090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2134")

    ChrTalk(
        0xFE,
        (
            "There was that raid incident and I'm \x01",
            "scared to go out on the highway, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these that\x01",
            "we have to protect the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3489")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2142")
    Jump("loc_3489")

    label("loc_2142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(
        0xFE,
        (
            "It seems Derrick and Mr. Minneth's\x01",
            "plan is building to a climax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just how will this village develop? \x01",
            "...Uh uh, I'm looking\x01",
            "forward to seeing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248E")

    ChrTalk(
        0xFE,
        (
            "Wow. To think Mr. Minneth\x01",
            "was a swindler...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say, everyone. This truck\x01",
            "that I bought from him...\x01",
            "What should I do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FIf I recall, you said earlier you\x01",
            "bought this orbal truck for 50,000\x01",
            "mira and market price is 500,000.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FH-Hmm... This is a tricky\x01",
            "problem, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FFor now, it might be best\x01",
            "to hand it to the police\x01",
            "and let them decide.\x02\x03",
            "#00104FYou purchased it in an official transaction,\x01",
            "I think it'll be returned immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat is right. It is best if they investigate\x01",
            "whether the vehicle itself is illegal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see... Well, I guess I'll\x01",
            "contact the police, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 7)
    Jump("loc_24F0")

    label("loc_248E")


    ChrTalk(
        0xFE,
        (
            "I bought this new\x01",
            "truck from a swindler...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I guess I'll contact the police, then.\x02",
    )

    CloseMessageWindow()

    label("loc_24F0")

    Jump("loc_3489")

    label("loc_24F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_280E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261C")

    ChrTalk(
        0xFE,
        (
            "If you are looking for Derrick,\x01",
            "he's still in the city meeting\x01",
            "with Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should be talking at the\x01",
            "Entertainment District hotel around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Now then, seeing as how I've\x01",
            "got the latest model, I've got\x01",
            "to maintain it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_269E")

    label("loc_261C")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Derrick, I wonder\x01",
            "if he isn't talking with Mr. Minneth at the\x01",
            "Entertainment District hotel around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269E")

    Jump("loc_2809")

    label("loc_26A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277A")

    ChrTalk(
        0xFE,
        (
            "Mr. Minneth is really a\x01",
            "very generous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of one who works\x01",
            "for Quincy Company, one of the\x01",
            "largest confectionery makers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I support his and\x01",
            "Derrick's plan\x01",
            "wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2809")

    label("loc_277A")


    ChrTalk(
        0xFE,
        (
            "Mr. Minneth is really a\x01",
            "very generous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of one who works\x01",
            "for Quincy Company, one of the\x01",
            "largest confectionery makers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2809")

    Jump("loc_3489")

    label("loc_280E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_END)), "loc_2A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2912")

    ChrTalk(
        0xFE,
        (
            "Huh... The lock on our private\x01",
            "property was open, you say!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow... So there's someone\x01",
            "out there that would do\x01",
            "such a thing, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for telling me.\x01",
            "I'll head over there in my\x01",
            "truck later to lock it up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A1B")

    label("loc_2912")


    ChrTalk(
        0xFE,
        (
            "I'll have to head over to\x01",
            "the private property later\x01",
            "in my truck and lock it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, the truck's been\x01",
            "showing its age lately.\x01",
            "Driving it isn't fun anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the village doesn't have\x01",
            "the budget for a new one...\x01",
            "I'll have to make do somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1B")

    Jump("loc_2C6B")

    label("loc_2A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4A")

    ChrTalk(
        0xFE,
        (
            "Midway down Armorica Old Road, there's a\x01",
            "private property managed by the village.\x01",
            "I actually just got back from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got tools and supplies\x01",
            "there, so you can't go in\x01",
            "there whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think it'll be\x01",
            "fine. We have it locked\x01",
            "so no one goes in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C6B")

    label("loc_2B4A")


    ChrTalk(
        0xFE,
        (
            "Midway down Armorica Old Road, there's a\x01",
            "private property managed by the village.\x01",
            "I actually just got back from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Come to think of it, there's a\x01",
            "foreign visitor in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if this black transport belongs to\x01",
            "him. Looks like a very expensive car, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6B")

    Jump("loc_3489")

    label("loc_2C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3D")

    ChrTalk(
        0x9,
        (
            "I saw the special training.\x01",
            "That move I just saw was\x01",
            "one amazing technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, that match before you know,\x01",
            "I wasn't expecting nothing less from Bracers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DDB")

    label("loc_2D3D")


    ChrTalk(
        0x9,
        (
            "Wow. I saw that match earlier, and my\x01",
            "excitement still hasn't died down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh. I'd like to spectate another\x01",
            "match with the Bracers again sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDB")

    Jump("loc_2F8F")

    label("loc_2DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F1F")

    ChrTalk(
        0x9,
        (
            "When I get excited,\x01",
            "my accent comes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm not a young man anymore, \x01",
            "so I'd like to fix it if possible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I consulted my sister, Miria, about it,\x01",
            "she said "Don't worry about it."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, acting like it's none of her business...\x01",
            "At this rate, I'll be exposed as a bumpkin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F8F")

    label("loc_2F1F")


    ChrTalk(
        0xFE,
        (
            "My sister, Miria, told me not\x01",
            "to worry about my accent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tch, acting like it's none of her business...\x02",
    )

    CloseMessageWindow()

    label("loc_2F8F")

    Jump("loc_3489")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3489")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3322")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3181")

    ChrTalk(
        0x9,
        "Hey, welcome to Armorica Village.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Wait... W-What'ss with\x01",
            "that orbal car!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It'ss not a Verne or Reinford\x01",
            "model... It'ss the firsst time\x01",
            "I've ever sseen anything like it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FUh uh, this one was manufactured by ZCF.\x02\x03",
            "#10102FBecause it's equipped with a\x01",
            "new engine, it's top speed\x01",
            "is 1,500 selge per hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whoooa... That'ss great. \x01",
            "Ssimply amazing!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Noｱl's really proud of it...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 5)
    Jump("loc_331D")

    label("loc_3181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3269")

    ChrTalk(
        0x9,
        (
            "A top sspeed of 1,500 sselge...\x01",
            "Sso even ZCF can make amazing\x01",
            "thingss like thiss...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Good, good!\x01",
            "It makess me want a new\x01",
            "orbal truck mysself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...*ahem*. Man, I\x01",
            "got excited and my\x01",
            "accent slipped out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_331D")

    label("loc_3269")


    ChrTalk(
        0x9,
        (
            "...That reminds me, I wonder who those\x01",
            "suspicious people the other day were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I guess I don't really care, as long as\x01",
            "they don't hindrance my orbal car lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331D")

    Jump("loc_3489")

    label("loc_3322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D5")

    ChrTalk(
        0x9,
        "Hey, welcome to Armorica Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We raise bees, crops and\x01",
            "livestock in this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The views are scenic too. If\x01",
            "you like, why not stay awhile?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3489")

    label("loc_33D5")


    ChrTalk(
        0x9,
        (
            "...That reminds me, I wonder who those\x01",
            "suspicious people the other day were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I guess I don't really care, as long as\x01",
            "they don't hindrance my orbal car lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3489")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A8C end

    def Function_9_348D(): pass

    label("Function_9_348D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_35BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352C")

    ChrTalk(
        0x8,
        (
            "Those adults sure are noisy, but...\x01",
            "That tree really is amaaazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Climbing a tree that big\x01",
            "would be super-fun, I bet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35B8")

    label("loc_352C")


    ChrTalk(
        0x8,
        (
            "Climbing a tree that big\x01",
            "would be super-fun, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if there's huge rhinoceros beetle\x01",
            "or something in its branches, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B8")

    Jump("loc_3FFF")

    label("loc_35BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_377B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B7")

    ChrTalk(
        0x8,
        (
            "Alright, let's play\x01",
            "Kick-the-can today!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03805F"Kick the caaan"?\x01",
            "What's thaaat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh, you don't know Kick-the-\x01",
            "can!? It can't be helped, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Umm, you see, it's basically\x01",
            "hide-and-seek, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0x10, 0xFF)
    Jump("loc_3776")

    label("loc_36B7")


    ChrTalk(
        0x8,
        (
            "You see, because there's no one \x01",
            "to be "it", you take this can and...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03809FI know. You crush it and\x01",
            "throw it in the trash, riiight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I-I'm telling you, that's not it!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_3776")

    Jump("loc_3FFF")

    label("loc_377B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_38AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3843")

    ChrTalk(
        0x8,
        (
            "Mr. Harold came with\x01",
            "this kid the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. So this must be what it's\x01",
            "like to have a little brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm older, so I've got to\x01",
            "look after him properly!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38A6")

    label("loc_3843")


    ChrTalk(
        0x8,
        (
            "I hope Mr. Harold\x01",
            "moves here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It he does, I'll be able to\x01",
            "play with Colin every day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A6")

    Jump("loc_3FFF")

    label("loc_38AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AA")

    ChrTalk(
        0x8,
        (
            "I heard some scary guys rampaged\x01",
            "in Crossbell City the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because this village is boring,\x01",
            "I often thought why can't an\x01",
            "incident happen or something, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I never wished for something\x01",
            "like a raid attack.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A2A")

    label("loc_39AA")


    ChrTalk(
        0x8,
        (
            "I've always thought it's too peaceful\x01",
            "and boring in this village, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's possible that\x01",
            "it's actually a blessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A2A")

    Jump("loc_3FFF")

    label("loc_3A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A3D")
    Jump("loc_3FFF")

    label("loc_3A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3BFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(
        0x8,
        "Aww, today's boooring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if some big incident will\x01",
            "happen to wake everyone up around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF5")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8E")

    ChrTalk(
        0x8,
        (
            "Hey, wasn't that amazing back there!\x01",
            "Those huge kitties came out like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe that man was\x01",
            "a tamer at some\x01",
            "circus somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan, I shoul've gotten\x01",
            "his autograph!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BF5")

    label("loc_3B8E")


    ChrTalk(
        0x8,
        (
            "Maybe that man was\x01",
            "a tamer at some\x01",
            "circus somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan, I shoul've gotten\x01",
            "his autograph!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF5")

    Jump("loc_3FFF")

    label("loc_3BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD2")

    ChrTalk(
        0x8,
        (
            "Recently a foreigner\x01",
            "that often comes to our\x01",
            "village gave us sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since we were rude, we\x01",
            "thought we'd be scolded, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, there're kind people\x01",
            "in this world for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D5B")

    label("loc_3CD2")


    ChrTalk(
        0x8,
        (
            "We did something rude to\x01",
            "the foreigner but he gave us\x01",
            "candy instead of getting mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Although my mom\x01",
            " scolded us after that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5B")

    Jump("loc_3FFF")

    label("loc_3D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7B")
    Call(0, 10)
    Jump("loc_3E14")

    label("loc_3D7B")


    ChrTalk(
        0x8,
        (
            "Hmm, it's the same as "high demon",\x01",
            "but the rules seem slightly different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then today, it's going to be Stefan's\x01",
            "Crossbell-style "high demon"!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E14")

    Jump("loc_3FFF")

    label("loc_3E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E34")
    Call(0, 10)
    Jump("loc_3E96")

    label("loc_3E34")


    ChrTalk(
        0x8,
        (
            "That's right, there's that\x01",
            "huge building in town, huuuh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I want to explore it sometime.\x02",
    )

    CloseMessageWindow()

    label("loc_3E96")

    Jump("loc_3FFF")

    label("loc_3E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F90")

    ChrTalk(
        0x8,
        (
            "Tch, it's too peaceful and\x01",
            "boring in this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to hear about recent news,\x01",
            "it's nothing but "Our cow gave\x01",
            "birth", and other stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Aww, I wonder if some\x01",
            "big incident will occur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FFF")

    label("loc_3F90")


    ChrTalk(
        0x8,
        (
            "Well, the cow's calf\x01",
            "was cute, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The big incident I'm\x01",
            "wishing for is not\x01",
            "such a peaceful thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFF")

    TalkEnd(0xFE)
    Return()

    # Function_9_348D end

    def Function_10_4003(): pass

    label("Function_10_4003")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4152")

    ChrTalk(
        0x8,
        (
            "Alright then, let's\x01",
            "play "high demon"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The demon absolutely\x01",
            "can't go to high places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Pooley wants to be the demon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh? So you're fine\x01",
            "standing on a high spot\x01",
            "in less than 3 seconds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...What's that? That's\x01",
            "the first I've heard of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey, HEY! Pooley\x01",
            "wants to be the demon!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4294")

    label("loc_4152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4294")

    ChrTalk(
        0xB,
        (
            "That reminds me, they had\x01",
            "the Orchis Tower\x01",
            "unveiling ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Orchis Tower?\x01",
            "What's that? Can you eat it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "A snack?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "N-No, no. It's a\x01",
            "really huge building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "According to rumors, you\x01",
            "can see all of Crossbell\x01",
            "from its roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, amazing! I want\x01",
            "to go there sometime.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)

    label("loc_4294")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_4003 end

    def Function_11_42A4(): pass

    label("Function_11_42A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4316")

    ChrTalk(
        0xA,
        (
            "Colin left for\x01",
            "the city with\x01",
            "Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He promised he'll come\x01",
            "to play with me again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488D")

    label("loc_4316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_44C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4420")

    ChrTalk(
        0xA,
        (
            "My brother only\x01",
            "cared about Colin\x01",
            "and I was bored, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mom says that Pooley has \x01",
            "to be a little patient since \x01",
            "she's like a big sister.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Pooley will have patience.\x01",
            "...'Cause she's a big sister♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44BD")

    label("loc_4420")


    ChrTalk(
        0xA,
        (
            "Pooley is a little of a\x01",
            "big sister to Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if he takes away bro's attention,\x01",
            "Pooley will have some patience.\x01",
            "...'Cause she's a big sister♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44BD")

    Jump("loc_488D")

    label("loc_44C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4529")

    ChrTalk(
        0xA,
        (
            "Lately, all my\x01",
            "bro cares\x01",
            "about is Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But he's \x01",
            "Pooley's bro...\x01",
            "How unfair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488D")

    label("loc_4529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A7")

    ChrTalk(
        0xA,
        (
            "Looks like Stefan returned\x01",
            "to the village some time agooo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope he comes to play soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_460E")

    label("loc_45A7")


    ChrTalk(
        0xA,
        (
            "Lately, I've been\x01",
            "playing this whole\x01",
            "time with my bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But it's really more\x01",
            "fun with Stefan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460E")

    Jump("loc_488D")

    label("loc_4613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4621")
    Jump("loc_488D")

    label("loc_4621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465E")

    ChrTalk(
        0xA,
        (
            "Pooley wants to\x01",
            "play Bracer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EC")

    label("loc_465E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C4")

    ChrTalk(
        0xA,
        (
            "Nyaa, nyaa. \x01",
            "What huge kitties they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "They weren't that cute, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46EC")

    label("loc_46C4")


    ChrTalk(
        0xA,
        (
            "Pooley really likes\x01",
            "small kitties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EC")

    Jump("loc_488D")

    label("loc_46F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4764")

    ChrTalk(
        0xA,
        (
            "My bro got a\x01",
            "spanking from my\x01",
            "mom the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*pffft*. His butt\x01",
            "was as red\x01",
            "as an apple.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488D")

    label("loc_4764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477F")
    Call(0, 10)
    Jump("loc_47A9")

    label("loc_477F")


    ChrTalk(
        0xA,
        (
            "Pooley is fine to\x01",
            "be the d-e-m-o-n!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A9")

    Jump("loc_488D")

    label("loc_47AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C9")
    Call(0, 10)
    Jump("loc_4813")

    label("loc_47C9")


    ChrTalk(
        0xA,
        (
            "When bro gives me a\x01",
            "piggy-back ride, I wonder\x01",
            "which of us is taller?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4813")

    Jump("loc_488D")

    label("loc_4818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_488D")

    ChrTalk(
        0xA,
        (
            "Pooley isn't bored\x01",
            "at all since her\x01",
            "bro's around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Lately, it's been fun\x01",
            "playing with Stefan, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488D")

    TalkEnd(0xFE)
    Return()

    # Function_11_42A4 end

    def Function_12_4891(): pass

    label("Function_12_4891")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499A")

    ChrTalk(
        0xB,
        (
            "Hmm. I think it's an unexpectedly\x01",
            "major incident, but... I wonder if\x01",
            "it's all right to be this carefree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, it's true that this is one\x01",
            "of their redeeming qualities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to be ready for\x01",
            "when anything does happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A47")

    label("loc_499A")


    ChrTalk(
        0xB,
        (
            "Being always carefree is one of\x01",
            "these two's redeeming qualities, but...\x01",
            "As expected, this is a major incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to be ready for\x01",
            "when anything does happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A47")

    Jump("loc_50EB")

    label("loc_4A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B05")

    ChrTalk(
        0xB,
        (
            "Colin is a bit\x01",
            "irresponsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Earlier too, he went out on the highway,\x01",
            "saying those Azure Flowers are pretty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We've got to watch him properly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B4E")

    label("loc_4B05")


    ChrTalk(
        0xB,
        (
            "Colin is a bit\x01",
            "irresponsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We've got to watch him properly.\x02",
    )

    CloseMessageWindow()

    label("loc_4B4E")

    Jump("loc_50EB")

    label("loc_4B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C12")

    ChrTalk(
        0xB,
        (
            "Mr. Harold and his family are staying\x01",
            "at the "Ash Tree" for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They helped my mother and I when\x01",
            "we moved here. The people of this\x01",
            "village are really openhearted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50EB")

    label("loc_4C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C20")
    Jump("loc_50EB")

    label("loc_4C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C2E")
    Jump("loc_50EB")

    label("loc_4C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C75")

    ChrTalk(
        0xB,
        (
            "I'm already tired of\x01",
            "playing Bracer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D71")

    label("loc_4C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D01")

    ChrTalk(
        0xB,
        (
            "I knew that mister\x01",
            "was rotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't believe he'd release\x01",
            "monsters in town... I thought\x01",
            "I was gonna be eaten.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D71")

    label("loc_4D01")


    ChrTalk(
        0xB,
        (
            "Even so, these brother and sister\x01",
            "were about to be attacked, and yet...\x01",
            "These two are carefree for sure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D71")

    Jump("loc_50EB")

    label("loc_4D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4DFD")

    ChrTalk(
        0xB,
        (
            "That mister doesn't sit well\x01",
            "with me for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He smiles and looks\x01",
            "nice, but his eyes\x01",
            "aren't smiling...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50EB")

    label("loc_4DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E18")
    Call(0, 10)
    Jump("loc_4E9C")

    label("loc_4E18")


    ChrTalk(
        0xB,
        (
            "In Crossbell City it's fine\x01",
            "if the demon gets to a\x01",
            "high spot within 3 seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Could this be what they\x01",
            "call a local rule?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E9C")

    Jump("loc_50EB")

    label("loc_4EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBC")
    Call(0, 10)
    Jump("loc_4F62")

    label("loc_4EBC")


    ChrTalk(
        0xB,
        (
            "Hmmm, I see.\x01",
            "It's been under a big curtain until now,\x01",
            "so it's no wonder you don't know it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that that curtain\x01",
            "has come down, the\x01",
            "whole city's excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F62")

    Jump("loc_50EB")

    label("loc_4F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5066")

    ChrTalk(
        0xB,
        (
            "Before, I lived with\x01",
            "my mother in Crossbell\x01",
            "City, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that we're living in\x01",
            "Armorica Village, every\x01",
            "day seems fresh somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even I don't understand\x01",
            "why I hated the idea of\x01",
            "coming here at first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0x6B, 0x0)
    Jump("loc_50EB")

    label("loc_5066")


    ChrTalk(
        0xB,
        (
            "I think that a cow giving\x01",
            "birth near you is pretty\x01",
            "amazing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I guess if you live here,\x01",
            "it becomes something natural.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50EB")

    TalkEnd(0xFE)
    Return()

    # Function_12_4891 end

    def Function_13_50EF(): pass

    label("Function_13_50EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5100")
    Jump("loc_5A74")

    label("loc_5100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_52EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5264")

    ChrTalk(
        0xC,
        (
            "The state independence declaration of invalidity...\x01",
            "It won't have hardly any influence on this village\x01",
            "that was weakly involved with that from the start, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, there are no small number of villagers who feel\x01",
            "anxious about sudden changes in the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I thought, I need to \x01",
            "visit each villager's home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_52EA")

    label("loc_5264")


    ChrTalk(
        0xC,
        (
            "There're many villagers worried about\x01",
            "sudden changes in the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I thought, I need to \x01",
            "visit each villager's home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EA")

    Jump("loc_5A74")

    label("loc_52EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_54CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_540B")

    ChrTalk(
        0xC,
        (
            "Those strange Azure Flowers...\x01",
            "A little while ago, they started\x01",
            "blooming in the lotus fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They have an effect on the lotuses growth,\x01",
            "so I want to weed them out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn. No matter how many times I\x01",
            "pull them out, they grow right back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54C7")

    label("loc_540B")


    ChrTalk(
        0xC,
        (
            "These lotus fields are precious to the\x01",
            "village, so I want to do something\x01",
            "about those Azure Flowers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn. No matter how many times I\x01",
            "pull them out, they grow right back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C7")

    Jump("loc_5A74")

    label("loc_54CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5660")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E7")

    ChrTalk(
        0xC,
        (
            "Ever since the raid attack\x01",
            "on the city, we've started\x01",
            "patrolling near the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now that that has happened,\x01",
            "it wouldn't be strange for\x01",
            "something to occur elsewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, we have to do everything we\x01",
            "can for the safety of the village.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_565B")

    label("loc_55E7")


    ChrTalk(
        0xC,
        (
            "We've started patrolling\x01",
            "near the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have to do everything we can\x01",
            "for the safety of the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_565B")

    Jump("loc_5A74")

    label("loc_5660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_566E")
    Jump("loc_5A74")

    label("loc_566E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_567C")
    Jump("loc_5A74")

    label("loc_567C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_568A")
    Jump("loc_5A74")

    label("loc_568A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5698")
    Jump("loc_5A74")

    label("loc_5698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_589D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D1")

    ChrTalk(
        0xC,
        (
            "For the continued existence of Armorica\x01",
            "Village, I gave the chief several\x01",
            "reform proposals yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, they were all\x01",
            "rejected, and we had the\x01",
            "same usual arguments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father, the Village Chief...\x01",
            "Can't he sense the danger in\x01",
            "maintaining the status quo?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5898")

    label("loc_57D1")


    ChrTalk(
        0xC,
        (
            "I offered several reform\x01",
            "proposals yesterday, but..\x01",
            "The Village Chief didn't \x01",
            "approve a single one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father, the Village Chief...\x01",
            "Can't he sense the danger in\x01",
            "maintaining the status quo?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5898")

    Jump("loc_5A74")

    label("loc_589D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D8")

    ChrTalk(
        0xC,
        (
            "I can't say our agriculture and livestock\x01",
            "have been doing well lately. \x01",
            "The village's finances are in poor shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But my father, the Village Chief... \x01",
            "He hasn't yet changed his\x01",
            "conservative ways of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...As the next Village Chief,\x01",
            "I've got to do something about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A74")

    label("loc_59D8")


    ChrTalk(
        0xC,
        (
            "For the continued existence\x01",
            "of Armorica Village, we\x01",
            "can't be bound by tradition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...As the next Village Chief,\x01",
            "I've got to do something about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A74")

    TalkEnd(0xFE)
    Return()

    # Function_13_50EF end

    def Function_14_5A78(): pass

    label("Function_14_5A78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B28")

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "This is Armorica Village...\x01",
            "As I had heard,\x01",
            "it's a pretty nice place.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "Uh uh. I'll begin\x01",
            "work at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B97")

    label("loc_5B28")


    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "I'll begin work\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        "Now then, the Village Chief's house is...\x02",
    )

    CloseMessageWindow()

    label("loc_5B97")

    TalkEnd(0xFE)
    Return()

    # Function_14_5A78 end

    def Function_15_5B9B(): pass

    label("Function_15_5B9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BAC")
    Jump("loc_5C5A")

    label("loc_5BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BC7")
    Call(0, 16)
    Jump("loc_5C4C")

    label("loc_5BC7")


    ChrTalk(
        0xE,
        (
            "Uh uh, Mrs. Sophia\x01",
            "really does worry too\x01",
            "much about Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But it's all right.\x01",
            "Children grow after\x01",
            "each injury, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C4C")

    Jump("loc_5C5A")

    label("loc_5C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5C5A")

    label("loc_5C5A")

    TalkEnd(0xFE)
    Return()

    # Function_15_5B9B end

    def Function_16_5C5E(): pass

    label("Function_16_5C5E")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "#03708FColin, I wonder if he'll be all right...\x01",
            "(*fidget fidget*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh, Mrs. Sophia. It'll be all right.\x01",
            "You don't have to worry so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "At first, I was worried\x01",
            "because my Stefan\x01",
            "was a weakling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In order for children to grow well,\x01",
            "I think you have to let them play\x01",
            "some mischievous games a bit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)

    ChrTalk(
        0xF,
        (
            "#03700FY-You're right. If I'm too\x01",
            "overprotective, Colin won't\x01",
            "be able to enjoy himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0x118, 0x0)
    Return()

    # Function_16_5C5E end

    def Function_17_5E2D(): pass

    label("Function_17_5E2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E3E")
    Jump("loc_5EF6")

    label("loc_5E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5EDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E59")
    Call(0, 16)
    Jump("loc_5EDA")

    label("loc_5E59")


    ChrTalk(
        0xF,
        (
            "#03700F...I feel the same. It's not\x01",
            "good if I'm too overprotective.\x02\x03",
            "#03709FI mean, Colin looks like\x01",
            "is having so much fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EDA")

    Jump("loc_5EF6")

    label("loc_5EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5EED")
    Jump("loc_5EF6")

    label("loc_5EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5EF6")

    label("loc_5EF6")

    TalkEnd(0xFE)
    Return()

    # Function_17_5E2D end

    def Function_18_5EFA(): pass

    label("Function_18_5EFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F0B")
    Jump("loc_5F9C")

    label("loc_5F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5F85")

    ChrTalk(
        0x10,
        (
            "#03800FIt's fun playing with\x01",
            "so many frieeends!\x02\x03",
            "#03809FI wonder if we can take\x01",
            "Sunita here next time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5F93")
    Jump("loc_5F9C")

    label("loc_5F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F9C")

    label("loc_5F9C")

    TalkEnd(0xFE)
    Return()

    # Function_18_5EFA end

    def Function_19_5FA0(): pass

    label("Function_19_5FA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E5")

    ChrTalk(
        0xFE,
        (
            "I'm looking for a way to do something about\x01",
            "the "Pleroma Grass" in these lotus fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you pull them out, they grow back immediately...\x01",
            "I'd like to exterminate them somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... They're the cause of\x01",
            ""Cryptid" appearances, so dealing\x01",
            "with them is a top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well for now, I'll try everything I can think of.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right, there's something\x01",
            "I'd like you all to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've decided to marry\x01",
            "my fiancｳe, Pearl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the situation though,\x01",
            "please keep it a secret from her...\x01",
            "I've already started the preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FMy... \x01",
            "*giggle*, congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. It's precisely because\x01",
            "of this situation that I\x01",
            "wanted something to protect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I've decided on a date\x01",
            "for the ceremony, I'll invite\x01",
            "you all, so please come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 1)
    Jump("loc_63A1")

    label("loc_62E5")


    ChrTalk(
        0xFE,
        (
            "I've kept Pearl waiting\x01",
            "long enough already... \x01",
            "I'll marry her before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect her as well, I've got to\x01",
            "focus more than ever on being the\x01",
            "best Crossbell Bracer I can be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A1")

    TalkEnd(0xFE)
    Return()

    # Function_19_5FA0 end

    def Function_20_63A5(): pass

    label("Function_20_63A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_648C")

    ChrTalk(
        0x26,
        (
            "We'll see the sights\x01",
            "here for awhile, then\x01",
            "return to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "No matter how many times I thanked\x01",
            "you guys, it wouldn't be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Allow me to thank you once again\x01",
            "for reuniting me with my father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_651C")

    label("loc_648C")


    ChrTalk(
        0x26,
        (
            "No matter how many times I thanked\x01",
            "you guys, it wouldn't be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Allow me to thank you once again\x01",
            "for reuniting me with my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651C")

    TalkEnd(0xFE)
    Return()

    # Function_20_63A5 end

    def Function_21_6520(): pass

    label("Function_21_6520")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65B4")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, Almin looks\x01",
            "happy to see his\x01",
            "father-in-law too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There, there. Isn't\x01",
            "that great, Almin㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "*goo, goo*.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_6612")

    label("loc_65B4")


    ChrTalk(
        0xFE,
        (
            "There, there, let's go say hello\x01",
            "to grandfather again later, hm?㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "*goo, goo*.\x02",
    )

    CloseMessageWindow()

    label("loc_6612")

    TalkEnd(0xFE)
    Return()

    # Function_21_6520 end

    def Function_22_6616(): pass

    label("Function_22_6616")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6648")
    SetScenarioFlags(0x31, 2)

    label("loc_6648")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_668E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6688")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_667D")
    Sound(2499, 255, 100, 0)
    Jump("loc_6683")

    label("loc_667D")

    Sound(3537, 255, 100, 0)

    label("loc_6683")

    Jump("loc_668E")

    label("loc_6688")

    Sound(3344, 255, 100, 0)

    label("loc_668E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6701")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66E1"),
        (SWITCH_DEFAULT, "loc_66F2"),
    )


    label("loc_66E1")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_66FC")

    label("loc_66F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66FC")

    Jump("loc_693C")

    label("loc_6701")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6733")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_6733")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6765"),
        (1, "loc_6869"),
        (2, "loc_68FA"),
        (SWITCH_DEFAULT, "loc_6932"),
    )


    label("loc_6765")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6796")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_67A6")

    label("loc_6796")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_67A6")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67FC")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681F")
    Sound(461, 0, 100, 0)

    label("loc_681F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_683F")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_684F")

    label("loc_683F")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_684F")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_668E")

    label("loc_6869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_68DB")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_689E")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_68B6")

    label("loc_689E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_68B1")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_68B6")

    label("loc_68B1")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_68B6")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68F5")

    label("loc_68DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_68EB")
    OP_AF(0xFB)
    Jump("loc_68F5")

    label("loc_68EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68F5")

    Jump("loc_693C")

    label("loc_68FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6913")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_692D")

    label("loc_6913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6923")
    OP_AF(0xFB)
    Jump("loc_692D")

    label("loc_6923")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_692D")

    Jump("loc_693C")

    label("loc_6932")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_693C")

    Jump("loc_668E")

    label("loc_6941")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_6616 end

    def Function_23_694F(): pass

    label("Function_23_694F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_699F")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_699F")

    Call(0, 3)
    Return()

    # Function_23_694F end

    def Function_24_69A3(): pass

    label("Function_24_69A3")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(11620, 1500, 1410, 1500)
    MoveCamera(328, 26, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16250, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A63")
    OP_E2(0x2)
    MiniGame(0x6, 0x1B, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_6A63")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_69A3 end

    def Function_25_6A68(): pass

    label("Function_25_6A68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    Call(0, 26)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadEffect(0x0, "event/ev12020.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    Call(0, 27)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadChrToIndex("chr/ch00052.itc", 0x33)
    LoadChrToIndex("chr/ch00057.itc", 0x34)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    LoadEffect(0x4, "battle\\cr000500.eff")
    LoadEffect(0x5, "battle\\cr000501.eff")
    LoadEffect(0x6, "battle\\cr000102.eff")
    Call(0, 29)
    Return()

    # Function_25_6A68 end

    def Function_26_6CAA(): pass

    label("Function_26_6CAA")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7840, 2500, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    SetChrPos(0x101, 7290, 0, -20490, 46)
    SetChrPos(0x102, 8520, 0, -22110, 46)
    SetChrPos(0x104, 8230, 0, -23660, 46)
    SetChrPos(0x109, 6700, 0, -22920, 46)
    SetChrPos(0x105, 6010, 0, -21490, 46)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(7840, 1200, -21280, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWow... Look at all\x01",
            "the spectators.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EEB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EEB)
    Sleep(50)

    def lambda_6EFB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6EFB)

    def lambda_6F08():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F08)
    Sleep(50)

    def lambda_6F18():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6F18)

    def lambda_6F25():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F25)
    Sleep(50)

    def lambda_6F35():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F35)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#12PYeah, it seems word's\x01",
            "gotten around.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1500, -14100, 3000)
    MoveCamera(7, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16620, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#5PHehe, Bracers are invincible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe police 'll be\x01",
            "a piece of cake.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#11PPiece of cake?\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "#5PUh, basically they\x01",
            "don't stand a chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x96, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#5PBut I wonder...\x01",
            "I think the SSS members\x01",
            "are pretty strong too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x96, 0x1F4)

    ChrTalk(
        0x9,
        "#5POoh, things are heating up!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1D, 500)

    ChrTalk(
        0x9,
        (
            "#11PSo who's your money on,\x01",
            "Village Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PHmm, let me see... Both\x01",
            "of them have helped me\x01",
            "out in the past, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x9, 0x96, 0x1F4)
    Fade(500)
    OP_68(7840, 1200, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#12P#00106FE-Even the Village Chief's here...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x19,
        (
            "#12PRather, I only told\x01",
            "the Village Chief\x01",
            "about our match...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHu hu, I'd expect no less of a rural village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FYeah. Information spreads terrifyingly fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FAhaha... \x01",
            "I'm getting nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12PUh uh. Well, having an audience\x01",
            "is good every once in awhile.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0xEE, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#11PAlright, I want to\x01",
            "get into our match.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7338():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7338)
    Sleep(50)

    def lambda_7348():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7348)

    def lambda_7355():
        OP_93(0xFE, 0xEE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7355)
    Sleep(50)

    def lambda_7365():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7365)
    Sleep(50)

    def lambda_7375():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7375)
    Sleep(50)

    def lambda_7385():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7385)
    Sleep(300)

    ChrTalk(
        0x18,
        "#11PFirst, we'll need to pick the format.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm... There are different ways\x01",
            "I can see doing this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PI think a two-on-\x01",
            "two is best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PYeah, I was\x01",
            "thinking that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PIs that ok with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FWell, you two put in the request,\x01",
            "so I don't have a problem with it...\x02\x03",
            "#00000FCan we pick who\x01",
            "gets to fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PBut you have\x01",
            "to fight, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHa ha, it's not that\x01",
            "surprising, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIt's not like we\x01",
            "wanted to see your\x01",
            "personal strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThe unity of the SSS that\x01",
            "you're the center of...\x01",
            "That's what we want to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Yeah, yeah! Without\x01",
            "the leader, there'd\x01",
            "be no point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FDamn, just look at this guy!\x02\x03",
            "To be in demand like this\x01",
            "from these lovely ladies...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, I see. So this is the rumored\x01",
            "younger brother bourgeois, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FSomehow I feel like I heard\x01",
            "some improper comments,\x01",
            "but... Whatever.\x02\x03",
            "#00000FIf that's how it's going\x01",
            "to be, that's just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThen, who's\x01",
            "going to be your\x01",
            "partner, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FHmm, let me think...\x02",
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
        0,
        (
            "Fight with Elie\x01",       # 0
            "Fight with Randy\x01",      # 1
            "Fight with Noｱl\x01",      # 2
            "Fight with Wazy\x01",       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7978")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FElie, can I ask you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00104F*giggle*, of course.\x02\x03",
            "#00102FLet's show them our\x01",
            "combined strength.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB1")

    label("loc_7978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A3A")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x2)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FRandy, can I ask you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00309FYeah, 'course!\x02\x03",
            "#00300FLet's use our combination attacks...\x01",
            "To hit these ladies hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB1")

    label("loc_7A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AEF")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00000FNoｱl, can I ask you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, of course!\x02\x03",
            "#10100FLet's use our Combi Craft...\x01",
            "And knock them down!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB1")

    label("loc_7AEF")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x4)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00000FWazy, care to fight with me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, if it's your wish, I would love to.\x02\x03",
            "#10302FLet's startle these ladies\x01",
            "with our "duet", hm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFA, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BEA")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_7C42")

    label("loc_7BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0E")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_7C42")

    label("loc_7C0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C32")
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_7C42")

    label("loc_7C32")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_7C42")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(8610, 1700, -21420, 0)
    MoveCamera(4, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12790, 0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE3")
    SetChrPos(0x104, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7DD7")

    label("loc_7CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D3B")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7DD7")

    label("loc_7D3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D93")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7DD7")

    label("loc_7D93")

    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x109, 13100, 0, -12850, 225)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7DD7")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#11PAlright!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYou too, ready your weapons.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10960, 1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E57")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_7E9D")

    label("loc_7E57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E73")
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_7E9D")

    label("loc_7E73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E95")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_7E9D")

    label("loc_7E95")

    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_7E9D")

    OP_0D()
    Fade(500)
    Sound(812, 0, 100, 0)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    ChrTalk(
        0x18,
        "#4S#11POk, here we go!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F07")
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7F5C")

    label("loc_7F07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2A")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7F5C")

    label("loc_7F2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4D")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7F5C")

    label("loc_7F4D")

    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)

    label("loc_7F5C")

    Battle("BattleInfo_774", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x109, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    Return()

    # Function_26_6CAA end

    def Function_27_7F8B(): pass

    label("Function_27_7F8B")

    EventBegin(0x0)
    SoundLoad(832)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8190")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x3)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_829C")

    label("loc_8190")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F0")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_829C")

    label("loc_81F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8250")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_829C")

    label("loc_8250")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x3)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_829C")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00006F*pant, pant*... It's no good!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_831E")

    ChrTalk(
        0x102,
        (
            "#6P#00106FNo way...\x01",
            "They weren't even serious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E2")

    label("loc_831E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_836F")

    ChrTalk(
        0x104,
        (
            "#6P#00306FGuh, and that's not\x01",
            "even their full power...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E2")

    label("loc_836F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B5")

    ChrTalk(
        0x109,
        (
            "#6P#10106FGuh... \x01",
            "We misread their moves...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E2")

    label("loc_83B5")


    ChrTalk(
        0x105,
        "#6P#10306FOh boy... We were careless...\x02",
    )

    CloseMessageWindow()

    label("loc_83E2")


    ChrTalk(
        0x18,
        (
            "#11P*sigh*, I can't believe this is all you've got...\x01",
            "I'm a little disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm, I was thinking you\x01",
            "could have done a little better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, I'd say their battle\x01",
            "teamwork has a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, fine. Next, we'll\x01",
            "face your whole team.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85AB")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Jump("loc_8627")

    label("loc_85AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85DB")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Jump("loc_8627")

    label("loc_85DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860B")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Jump("loc_8627")

    label("loc_860B")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    label("loc_8627")

    Jump("loc_8C63")

    label("loc_862C")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A5")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_87B1")

    label("loc_86A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8705")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_87B1")

    label("loc_8705")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8765")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_87B1")

    label("loc_8765")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_87B1")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00000F*pant*... Did we do it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8852")

    ChrTalk(
        0x102,
        (
            "#6P#00102FI would say yes...\x01",
            "But it appears they\x01",
            "were holding back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_895B")

    label("loc_8852")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88BC")

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, it looks like that\x01",
            "wasn't their full power.\x01",
            "Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_895B")

    label("loc_88BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8919")

    ChrTalk(
        0x109,
        (
            "#6P#10104FYes... But it appears\x01",
            "our opponents were\x01",
            "holding back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_895B")

    label("loc_8919")


    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, although\x01",
            "it appears they\x01",
            "weren't serious.\x02",
        )
    )

    OP_57(0x0)
    OP_5A()
    CloseMessageWindow()

    label("loc_895B")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#11PUh uh, I'm surprised. \x01",
            "You guys are pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah, you guys had better\x01",
            "teamwork than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FAhaha... It seems you were fine, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHa ha, while it's true we were\x01",
            "holding back, it wasn't that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell anyway, that\x01",
            "was a good showing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUmm... Is this the end\x01",
            "of the training, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PUh uh.\x01",
            "Now now, not so fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah, yeah. That wasn't enough\x01",
            "for you guys either, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FT-That's not true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PHa ha, what're you being modest for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI know! Next, I want\x01",
            "to try us versus the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_8C63")


    def lambda_8C68():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C68)
    Sleep(50)

    def lambda_8C78():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C78)
    Sleep(50)

    def lambda_8C88():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C88)
    Sleep(50)

    def lambda_8C98():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C98)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FA-All five of us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWon't it be tough with just\x01",
            "you two against all of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PUh uh, that's exactly why\x01",
            "this is a training practice!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        "#11P#4SHA!!\x02",
    )

    CloseMessageWindow()
    Sound(620, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 9600, 0, -18150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x102,
        "#6P#00105FAmazing... She's radiating energy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FAn art from the east called "qigong", I believe.\x02\x03",
            "#00301F...She'll be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYou're well informed, aren't you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PEolia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8EA0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EA0)
    Sleep(50)

    def lambda_8EB0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8EB0)
    Sleep(50)

    def lambda_8EC0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8EC0)
    Sleep(50)

    def lambda_8ED0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8ED0)
    Sleep(50)
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        "#6P#10105FThis is..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FUh uh, so everyone has made\x01",
            "a full recovery, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PNow we can fight without holding anything back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, guys!\x01",
            "Don't just stand there and get ready!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10960, 1000)
    Fade(500)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#6P#00300F*sigh*, looks like we have no choice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLloyd... \x01",
            "Who's on support?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FYeah...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Elie on Support\x01",       # 0
            "Randy on Support\x01",      # 1
            "Noｱl on Support\x01",      # 2
            "Wazy on Support\x01",       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_913D")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_9195")

    label("loc_913D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9161")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_9195")

    label("loc_9161")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9185")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_9195")

    label("loc_9185")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_9195")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9230")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_9324")

    label("loc_9230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9288")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_9324")

    label("loc_9288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92E0")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_9324")

    label("loc_92E0")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_9324")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_938A")

    ChrTalk(
        0x101,
        "#6P#00000FElie, handle the support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FAlright, roger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9488")

    label("loc_938A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93DE")

    ChrTalk(
        0x101,
        "#6P#00000FRandy, you're on support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FGotcha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9488")

    label("loc_93DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943E")

    ChrTalk(
        0x101,
        "#6P#00000FNoｱl, I'm leaving the support to you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYessir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9488")

    label("loc_943E")


    ChrTalk(
        0x101,
        "#6P#00000FWazy, you're on support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHu hu, understood!\x02",
    )

    CloseMessageWindow()

    label("loc_9488")


    ChrTalk(
        0x18,
        "#4S#11PHere we come!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_7B8", 0x30200011, 0x0, 0x100, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    Return()

    # Function_27_7F8B end

    def Function_28_94C3(): pass

    label("Function_28_94C3")

    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    Sound(357, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x19, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x1, 0x2)
    Sound(280, 0, 30, 0)
    PlayEffect(0x2, 0x2, 0x19, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x3)
    Sleep(500)
    Sound(226, 0, 80, 0)
    PlayEffect(0x3, 0xFF, 0x101, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x102, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x104, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x109, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x4)
    Sleep(2000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_28_94C3 end

    def Function_29_968F(): pass

    label("Function_29_968F")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98A9")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_99FD")

    label("loc_98A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9921")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_99FD")

    label("loc_9921")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9999")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_99FD")

    label("loc_9999")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)

    label("loc_99FD")

    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00006F*pant*, *pant*, *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FDamn... I can't believe even all\x01",
            "of us were no match for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FWe lost...completely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P*sigh*... \x01",
            "And I thought we wouldn't\x01",
            "have pulled it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYes. We picked up\x01",
            "the win, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PMaybe it's a difference in experience?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00002FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThe damage I took earlier\x01",
            "is completely gone...\x02\x03",
            "#00102FThat's an amazing recovery technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FBut you beat us, and now\x01",
            "you're healing us...\x02\x03",
            "#00306F*sigh*, I'm a failure of a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PSorry. \x01",
            "Maybe I did something I shouldn't have?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00309FNo no, that's not it!\x02\x03",
            "#00300FTo be healed by Miss Eolia's warm\x01",
            "Arts like this... I wouldn't\x01",
            "have it any other way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FS-Senior Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHa ha. Where did your pride\x01",
            "from earlier go, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*, seriously...\x01",
            "I guess all the\x01",
            "tension went away...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4AE")

    label("loc_9E1E")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EAF")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_A003")

    label("loc_9EAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F27")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_A003")

    label("loc_9F27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F9F")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_A003")

    label("loc_9F9F")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)

    label("loc_A003")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*pant, pant*...\x01",
            "I-Is it over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, somehow.\x02\x03",
            "#00302FBut they lasted this long\x01",
            "against all five of us.\x01",
            "They're really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FYes, truly... They didn't let down\x01",
            "their guard until the bitter end.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#11P*sigh*... No good,\x01",
            "as expected, huh.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#11PIt would have gone a little better\x01",
            "if we did things differently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PNo matter what excuses we\x01",
            "make, a loss is a loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYou guys are really strong.\x01",
            "You're the winners, this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FAmazing...\x02\x03",
            "I feel like all the damage\x01",
            "from before is gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FTo be healed by Miss Eolia\x01",
            "even twice in one day... \x01",
            "It's like I've gone to heaven...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PThank you, Randy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#11PThen, do you want to go another round\x01",
            "so I can heal you for a third time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FUgh, give me a break!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu. I think you might go to heaven in the\x01",
            "real sense during the match next time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*, seriously...\x01",
            "I guess all the\x01",
            "tension went away...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    label("loc_A4AE")


    ChrTalk(
        0x18,
        (
            "#11PHa ha, you guys are the best. \x01",
            "I never get tired of watching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FT-Thanks.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(5620, 1500, -16800, 3000)
    MoveCamera(9, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18740, 3000)
    TurnDirection(0x18, 0x1D, 500)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x18,
        (
            "#12PAlright, alright, this\x01",
            "concludes our match.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#12PYeah. Nothing further\x01",
            "to see here, everyone.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A5DC():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5DC)
    Sleep(50)

    def lambda_A5EC():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A5EC)
    Sleep(50)

    def lambda_A5FC():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A5FC)
    Sleep(50)

    def lambda_A60C():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A60C)
    Sleep(50)

    def lambda_A61C():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A61C)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#5PHmm, then I suppose it's time\x01",
            "to end this little event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PThere's work to do, everyone.\x01",
            "C'mon, break time's over.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#11PHa ha, got it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#11PCome on everyone, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PMan, that was a great fight!\x02",
    )

    CloseMessageWindow()
    OP_68(7360, 1500, -16890, 5000)
    MoveCamera(20, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16070, 5000)

    def lambda_A751():
        OP_95(0xFE, 8600, 0, -6460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A751)
    Sleep(50)

    def lambda_A76E():
        OP_95(0xFE, -2960, 0, -6890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A76E)
    Sleep(50)

    def lambda_A78B():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A78B)
    Sleep(1000)

    def lambda_A7A8():
        OP_95(0xFE, 1980, 0, -8140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A7A8)
    Sleep(50)

    def lambda_A7C5():
        OP_95(0xFE, -470, 0, -11050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A7C5)
    Sleep(50)

    def lambda_A7E2():
        OP_95(0xFE, 280, 0, -10190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A7E2)
    Sleep(50)

    def lambda_A7FF():
        OP_95(0xFE, 1220, 0, -9620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A7FF)
    Sleep(1200)

    def lambda_A81C():
        OP_95(0xFE, 3110, 0, -9910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A81C)
    WaitChrThread(0x9, 1)

    def lambda_A83A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A83A)
    WaitChrThread(0x8, 1)

    def lambda_A84B():
        OP_95(0xFE, -5810, 0, -6140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A84B)
    WaitChrThread(0xA, 1)

    def lambda_A869():
        OP_95(0xFE, -5250, 0, -4930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A869)
    WaitChrThread(0xB, 1)

    def lambda_A887():
        OP_95(0xFE, -4680, 0, -3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A887)
    WaitChrThread(0x1A, 1)

    def lambda_A8A5():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A8A5)
    WaitChrThread(0x1B, 1)

    def lambda_A8C3():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A8C3)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6F(0x1)

    ChrTalk(
        0x18,
        (
            "#12PYeah, and Village Chief,\x01",
            "thanks for letting\x01",
            "us use this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#12PThanks to you, we could have a good training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PWell, it's not like we didn't\x01",
            "also benefit from that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PYou're always helping us out.\x01",
            "You can ask me anything again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PGoodbye, then.\x02",
    )

    CloseMessageWindow()

    def lambda_AA23():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AA23)
    Sleep(2000)
    Fade(500)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00009FHa ha, to\x01",
            "think they'd\x01",
            "be so happy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut Miss Ling...\x01",
            "What was this match\x01",
            "even for, anyway?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB03():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AB03)
    Sleep(50)

    def lambda_AB13():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_AB13)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB6C")

    def lambda_AB2F():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB2F)
    Sleep(50)

    def lambda_AB3F():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AB3F)
    Sleep(50)

    def lambda_AB4F():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB4F)
    Sleep(50)

    def lambda_AB5F():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB5F)
    Jump("loc_AC4B")

    label("loc_AB6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABBD")

    def lambda_AB80():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AB80)
    Sleep(50)

    def lambda_AB90():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB90)
    Sleep(50)

    def lambda_ABA0():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABA0)
    Sleep(50)

    def lambda_ABB0():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABB0)
    Jump("loc_AC4B")

    label("loc_ABBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC0E")

    def lambda_ABD1():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABD1)
    Sleep(50)

    def lambda_ABE1():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABE1)
    Sleep(50)

    def lambda_ABF1():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ABF1)
    Sleep(50)

    def lambda_AC01():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC01)
    Jump("loc_AC4B")

    label("loc_AC0E")


    def lambda_AC13():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC13)
    Sleep(50)

    def lambda_AC23():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC23)
    Sleep(50)

    def lambda_AC33():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC33)
    Sleep(50)

    def lambda_AC43():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AC43)

    label("loc_AC4B")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADE0")
    OP_2C(0x75, 0x2)
    OP_29(0x75, 0x1, 0x5)

    ChrTalk(
        0x18,
        (
            "#11PWell, you guys were \x01",
            "stronger than I thought.\x01",
            "I'm surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PI guess you could say it's the result of all your training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PUh uh, but we're not\x01",
            "interested in losing again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWe'll have our\x01",
            "revenge someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I'd love to do this again\x01",
            "if there's another opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FAnytime's ok if you ask me㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFC6")

    label("loc_ADE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEF3")
    OP_29(0x75, 0x1, 0x6)

    ChrTalk(
        0x18,
        (
            "#11PThat's right. If you had held out a littler longer,\x01",
            "I would've been an even more nice training, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm. I'm a little\x01",
            "unsatisfied, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FI-I have no excuses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell, even so, we got some result.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFC6")

    label("loc_AEF3")

    OP_2C(0x75, 0x1)
    OP_29(0x75, 0x1, 0x7)

    ChrTalk(
        0x18,
        (
            "#11PYeah. You all did your best,\x01",
            "and that's enough for training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PThat's right. If there's a chance,\x01",
            "I'd like to do this again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes. We'd love to take up your offer again.\x02",
    )

    CloseMessageWindow()

    label("loc_AFC6")

    OP_29(0x75, 0x1, 0x8)

    ChrTalk(
        0x18,
        (
            "#11PWhat we need to do now is\x01",
            "integrate what we've seen of\x01",
            "your various combat styles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PEspecially yours, Lloyd.\x01",
            "I'm very interested in\x01",
            "your tonfas techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI think the police teach those\x01",
            "disabling techniques, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I'm impressed you know.\x02\x03",
            "#00005FBut, what's so interesting about it...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x18, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell tonfas are originally\x01",
            "from the East, right?\x02\x03",
            "#00305FCan you use them too, Miss Ling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, a little bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWhen I was learning martial arts, I got a\x01",
            "feel for Eastern weapons including the\x01",
            "chakram and the three-section staff, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PFrom that point of view, let me say this,\x01",
            "Lloyd, your spin technique might\x01",
            "be a little old.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FOld you say... Are you saying you\x01",
            "can make my technique stronger?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell in the end, it's just a possibility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIf you like, I can\x01",
            "instruct you here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWant to try it out?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00002FYou'll teach me? Of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PYou're lucky, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PIt's rare for Ling to be\x01",
            "teaching anyone anything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x19, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00309FI'd like you to teach me a\x01",
            "few things too, Miss Eolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PHmm? Pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F*destroyed*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FSenior Randy, you never learn, do you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FSorry everyone...\x02\x03",
            "#00000FAs you have heard... Do you mind\x01",
            "if I take a little more of our time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B54B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B54B)
    Sleep(50)

    def lambda_B55B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B55B)
    Sleep(50)

    def lambda_B56B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B56B)
    Sleep(50)

    def lambda_B57B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B57B)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FNot at all. You won't get many chances\x01",
            "like this. You should take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, allow us to\x01",
            "watch and learn, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FDo your best, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FYeah, give it your all for me too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHa ha, well then\x01",
            "let's get started.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00000FPlease do!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7680, 1400, -21510, 0)
    MoveCamera(7, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12760, 0)
    SetChrPos(0x101, 7680, 0, -20400, 45)
    SetChrPos(0x102, 3320, 0, -22300, 45)
    SetChrPos(0x104, 4550, 0, -24210, 45)
    SetChrPos(0x109, 2930, 0, -19450, 90)
    SetChrPos(0x105, 7610, 0, -25120, 0)
    SetChrPos(0x18, 10880, 0, -16800, 225)
    SetChrPos(0x19, 12130, 0, -18530, 225)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 30)
    WaitChrThread(0x101, 3)
    TurnDirection(0x101, 0x18, 0)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI-I felt like\x01",
            "I got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, you pass.\x02",
    )

    CloseMessageWindow()
    OP_68(7310, 1400, -21350, 2000)
    MoveCamera(12, 19, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14340, 2000)

    def lambda_B866():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B866)
    Sleep(50)

    def lambda_B87E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B87E)
    Sleep(50)

    def lambda_B896():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B896)

    def lambda_B8AB():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B8AB)
    Sleep(50)

    def lambda_B8C3():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B8C3)
    Sleep(50)

    def lambda_B8DB():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8DB)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    ChrTalk(
        0x18,
        (
            "#11PAfter this, if you just use it in actual combat, \x01",
            "you'll be able to make it your own.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000F*sigh*, thank goodness...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100F*giggle*, you did it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FNice work, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0xFA, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, thanks.\x02\x03",
            "#00003FBut it's amazing... To think\x01",
            "that with this method  the\x01",
            "output power changes too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PUh uh. The spin move I just\x01",
            "taught you is commonly known\x01",
            "as a "spiral"-type attack.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x3A, 0x1F4)

    ChrTalk(
        0x18,
        (
            "#11PIt's a form of the "Eight\x01",
            "Leaves One Blade" style\x01",
            "Mr. Arios uses, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThe number of moves you can derive\x01",
            "from those fundamentals is as\x01",
            "countless as the stars in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHe who masters the "spiral" and \x01",
            ""nothingness" is said to have reached the\x01",
            ""truth", the ultimate point of all martial arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FFrom spiral to nothingness and\x01",
            "then to "truth", you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, that's as much as\x01",
            "I understand, so that's\x01",
            "all for the lecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIn short, "truth" is something like\x01",
            "a state ordinary people cannot reach\x01",
            "even if they spend their whole lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIt's said that only a handful\x01",
            "of people on the continent\x01",
            "have ever reached that state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FJ-Just a handful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FI've heard rumors about that sort of\x01",
            "thing before. It's pretty crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PHa ha, yeah, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell I obviously won't tell you to go all the way\x01",
            "to "truth", but you should keep working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYes, understood!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#11PWhoops. Now that we're through with\x01",
            "that, it's about time for our next job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah. Both of us\x01",
            "have to hurry.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF3A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BF3A)
    Sleep(50)

    def lambda_BF4A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF4A)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00100FI thought you two were rather busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PYeah. Especially now with the Trade\x01",
            "Conference, we have a tight schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PMichel's shifts are\x01",
            "critical but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PNow he has them cut up in blocks\x01",
            "of just a few minutes each.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FT-That's ridiculous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PUh uh, I say that, but there's\x01",
            "some time set aside for rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, we'll be going.\x01",
            "Keep up the good work, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PSee you later, Lloyd, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16340, 3000)

    def lambda_C159():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_C159)
    Sleep(50)

    def lambda_C176():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C176)

    def lambda_C190():

        label("loc_C190")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_C190")

    QueueWorkItem2(0x101, 1, lambda_C190)
    Sleep(50)

    def lambda_C1A5():

        label("loc_C1A5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_C1A5")

    QueueWorkItem2(0x102, 1, lambda_C1A5)
    Sleep(50)

    def lambda_C1BA():

        label("loc_C1BA")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_C1BA")

    QueueWorkItem2(0x104, 1, lambda_C1BA)
    Sleep(50)

    def lambda_C1CF():

        label("loc_C1CF")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_C1CF")

    QueueWorkItem2(0x109, 1, lambda_C1CF)
    Sleep(50)

    def lambda_C1E4():

        label("loc_C1E4")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_C1E4")

    QueueWorkItem2(0x105, 1, lambda_C1E4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd learned\x01",
            ""Raging Spin".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's Craft "Accel Rush" was strengthened\x01",
            "and became "Raging Spin".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attack power has increased and it affects\x01",
            "enemies in a wider range. Furthermore, \x01",
            "it is possible to draw them in one place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddCraft(0x0, 0x9B)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Taking Part in Bracer Training] complete!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x9, 8410, 0, -12480, 17)
    SetChrPos(0x8, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    SetChrPos(0xB, -7830, 0, 23860, 107)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    SetChrPos(0x0, 8140, 0, -18700, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    OP_29(0x75, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_29_968F end

    def Function_30_C44F(): pass

    label("Function_30_C44F")

    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    Sound(257, 0, 40, 0)
    Sound(252, 0, 80, 0)
    PlayEffect(0x4, 0x4, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    StopEffect(0x4, 0x2)
    Sleep(300)
    StopEffect(0x6, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x33)
    SetChrSubChip(0x101, 0x0)
    SetChrChip(0x0, 0xFE, 0xF, 0x12C)
    Sound(253, 0, 100, 0)
    PlayEffect(0x5, 0x5, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    SetScenarioFlags(0x1, 1)

    def lambda_C532():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2EE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C532)
    BeginChrThread(0x101, 0, 0, 31)
    WaitChrThread(0x101, 1)
    StopEffect(0x5, 0x2)
    ClearScenarioFlags(0x1, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_C44F end

    def Function_31_C563(): pass

    label("Function_31_C563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_C57F")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_31_C563")

    label("loc_C57F")

    Return()

    # Function_31_C563 end

    def Function_32_C580(): pass

    label("Function_32_C580")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3060, 1800, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    SetChrPos(0x101, -2630, 0, 25660, 180)
    SetChrPos(0x102, -820, 0, 25800, 225)
    SetChrPos(0x103, -360, 0, 23860, 270)
    SetChrPos(0x104, -3500, 0, 24030, 90)
    SetChrPos(0x109, -2890, 0, 22410, 0)
    SetChrPos(0x105, -970, 0, 22610, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3060, 700, 24920, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWe talked to everyone...\x01",
            "And we got many information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FHis name is "Minneth"...\x01",
            "And he appears to be\x01",
            "some kind of trader.\x02\x03",
            "#00101FAnd unexpectedly,\x01",
            "he's good-natured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FPolite, kind to children...\x01",
            "That sort of thing.\x02\x03",
            "#10304FHu hu, conversely, his coming\x01",
            "here makes him suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAt present, his\x01",
            "objective is unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIt really worries me\x01",
            "what he talked with the\x01",
            "Village Chief's son about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... I think it's\x01",
            "best to continue\x01",
            "these inquiries.\x02\x03",
            "#00005FUmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    ClearChrFlags(0x9, 0x80)
    Fade(500)
    OP_68(8510, 1500, -12620, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    SetCameraDistance(15000, 3000)
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)

    def lambda_C8F3():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8F3)

    def lambda_C900():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C900)

    def lambda_C90D():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C90D)

    def lambda_C91A():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C91A)

    def lambda_C927():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C927)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(-3060, 700, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FThat person... What about\x01",
            "the person with whom Mr.\x01",
            "Derrick went to the city?\x02\x03",
            "#00003FLooks like he just got\x01",
            "back... Let's have a\x01",
            "little chat with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(1, 0, 0x80)
    SetScenarioFlags(0x174, 4)
    OP_29(0x82, 0x1, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2850, 0, 24480, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_C580 end

    def Function_33_CA50(): pass

    label("Function_33_CA50")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7300, 1800, -12910, 0)
    MoveCamera(349, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13740, 0)
    SetChrPos(0x101, 6500, 0, -11950, 135)
    SetChrPos(0x102, 6210, 0, -13080, 90)
    SetChrPos(0x103, 5100, 0, -12190, 90)
    SetChrPos(0x104, 5560, 0, -10540, 135)
    SetChrPos(0x109, 6300, 0, -9770, 135)
    SetChrPos(0x105, 4430, 0, -10630, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "Hm, hm, hmm...♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me, are\x01",
            "you Mr. Elkin?\x02\x03",
            "I'd like to ask you a\x01",
            "little something...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "Oh, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe you wanted to\x01",
            "ask me about this\x01",
            "new orbal truck?\x02",
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
            "#00012FN-No, no...\x01",
            "That's not it.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Tch, no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I got it cheap from Mr.\x01",
            "Minneth, and it's Verne\x01",
            "Corp.'s latest model...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FWhat...?\x02\x03",
            "#00101FYou mean Mr. Minneth, the\x01",
            "foreigner who's been coming\x01",
            "to the village recently...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FC-Cheap, you said...\x01",
            "How much was it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uhuhuh, it was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My goodness, a\x01",
            "mere 50,000 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FF-50,000 mira!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FBuying a new truck\x01",
            "for such a price...\x01",
            "H-How nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhoa, hey there. This is\x01",
            "no time to feel envious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FI-I suppose you're right. Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F*ahem*, anyway.\x02\x03",
            "#00200FConsidering the fact that it is new,\x01",
            "it should cost around 500,000 mira...\x01",
            "That is exceptionally cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSo 90% off. \x01",
            "That's exceptionally\x01",
            "generous of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Saying that it was to make\x01",
            "our work become smoother,\x01",
            "he gave it me for cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems his plan with Derrick\x01",
            "is progressing in many ways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, I've got to give my\x01",
            "hat off to Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FPlan...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "W-Whoops. \x01",
            "Derrick forbade \x01",
            "me to speak of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well anyway...\x01",
            "I think Mr. Minneth\x01",
            "is a trustworthy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00005F...Huh? Come to think of it...\x01",
            "You're alone, Mr. Elkin?\x02\x03",
            "The Village Chief said you headed\x01",
            "to the city with Mr. Derrick...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, Derrick said he was\x01",
            "coming back by bus later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seemed like he had business at\x01",
            "the Entertainment District hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think he had an appointment\x01",
            "to meet with Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FHey Lloyd, this is...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FYeah. We might be able to\x01",
            "ask Mr. Minneth directly.\x02\x03",
            "#00001FIt's worth checking out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#00000FThank you very much for your cooperation.\x01",
            "That was really helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Not at all, you're very welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't really get it,\x01",
            "but good luck.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 5)
    OP_29(0x82, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 6100, 0, -11400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_CA50 end

    def Function_34_D4A8(): pass

    label("Function_34_D4A8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1470, 1500, 10410, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("monster/ch82050.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    LoadChrToIndex("chr/ch00051.itc", 0x28)
    LoadChrToIndex("chr/ch00151.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00351.itc", 0x2B)
    LoadChrToIndex("chr/ch02951.itc", 0x2C)
    LoadChrToIndex("chr/ch03051.itc", 0x2D)
    LoadChrToIndex("monster/ch82051.itc", 0x2E)
    LoadChrToIndex("monster/ch82052.itc", 0x2F)
    SoundLoad(325)
    SoundLoad(948)
    SoundLoad(809)
    SoundLoad(805)
    SoundLoad(531)
    SoundLoad(494)
    SoundLoad(487)
    SoundLoad(486)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x101, -1320, 0, 11720, 90)
    SetChrPos(0x102, -2330, 0, 11520, 90)
    SetChrPos(0x103, -1550, 0, 10520, 90)
    SetChrPos(0x104, -2360, 60, 10120, 90)
    SetChrPos(0x109, -1360, 200, 9200, 90)
    SetChrPos(0x105, -2510, 260, 8760, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x105, 0x1000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0xC, 12240, 0, 17850, 180)
    SetChrPos(0xD, 12050, 0, 16440, 0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    OP_68(12280, 1500, 16050, 5000)
    OP_6F(0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#N#1P#00010FDamn... Did he already\x01",
            "finish the deal...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_D806():
        OP_95(0xFE, 3850, 0, 19250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D806)
    Sleep(100)

    def lambda_D823():
        OP_95(0xFE, 4270, 0, 18270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D823)
    OP_68(3150, 1500, 17270, 5000)
    MoveCamera(293, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(13200, 5000)
    BeginChrThread(0x101, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 36)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 39)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 40)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D8CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D8CE)
    Sleep(100)

    def lambda_D8DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D8DE)
    Sleep(300)

    ChrTalk(
        0xD,
        "Oh, you guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMr. Derrick, Mr. Minneth...\x01",
            "Can I ask what kind of deal you\x01",
            "two were conducting today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmph, my father put you up to this again, did he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, well why\x01",
            "not, Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our plan will begin\x01",
            "very soon, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhat do you mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "──Just now, I concluded my\x01",
            "final deal with Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It is decided that work will start\x01",
            "on expansion of the lotus fields I\x01",
            "borrowed from everyone in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, the "Quincy Company"\x01",
            "I work for will take over\x01",
            "their management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FSo you basically handed over\x01",
            "almost all of the village's\x01",
            "agriculture to this man...\x02\x03",
            "#10300FMr. Derrick, are you\x01",
            "really ok with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, I'm just transferring\x01",
            "management of the fields to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With my company harvesting the\x01",
            "honey, we'll be able to operate the\x01",
            "confectionery business efficiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For that to happen, it's most\x01",
            "efficient to temporarily transfer\x01",
            "the rights to my company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F(Tch...this guy\x01",
            "is cunnin'.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(It seems the plan has\x01",
            "entered its final stage.)\x02\x03",
            "#00208F(And that means...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Uh uh, well then, Mr. Derrick. \x01",
            "I will be delivering this contract\x01",
            "to the main office.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "I think I will have some good\x01",
            "news for you tomorrow, so\x01",
            "please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Alright. I'll be waiting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10101F(M-Mr. Lloyd...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah... We can't\x01",
            "let him get away!)\x02\x03",
            "#00001F──Mr. Minneth, before that...\x01",
            "We have a few more questions for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DFE6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DFE6)
    Sleep(100)

    def lambda_DFF6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DFF6)
    Sleep(300)

    ChrTalk(
        0xD,
        "Oh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What might you\x01",
            "want to know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, you see...\x01",
            "It's about certain suspicions\x01",
            "surrounding you.\x02\x03",
            "#00001FThat's right...\x01",
            "I'm talking about\x01",
            "suspicions of fraud.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Wha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "D-Don't be ridiculous!\x01",
            "That's rude to Mr. Minneth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh... Now, now.\x01",
            "Please calm down, Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Mr. Minneth...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You said you are the Special\x01",
            "Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why on earth would you suspect\x01",
            "me of being a crook...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You can of course\x01",
            "explain that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How interesting...\x01",
            "In that case, \x01",
            "let's hear about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But before that...\x01",
            "Don't forget that I am\x01",
            "an Imperial citizen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the case you have no clear\x01",
            "basis for calling me a crook...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even though you are an\x01",
            "officer, I'll do whatever I\x01",
            "must to settle the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...That's fine with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FLloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It's all right. I'll handle this.)\x02\x03",
            "(Based on our investigation\x01",
            "results, it's obvious Minneth\x01",
            "is committing fraud...)\x02\x03",
            "#00001F(I'll expose Minneth's\x01",
            "true colors, and open\x01",
            "Mr. Derrick's eyes!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, very well...\x01",
            "If you are that prepared, I\x01",
            "will answer anything you like.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0xD,
        (
            "...So, what will we\x01",
            "be discussing first?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F──First, your actions\x01",
            "in Crossbell...\x02\x03",
            "#00001FI want to ask you about a contradiction\x01",
            "between those and what you said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "A contradiction, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ever since I came to Crossbell,\x01",
            "I have been working with Mr.\x01",
            "Derrick on furthering this plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The plan to launch "Armorica\x01",
            "Honey Company" in Armorica\x01",
            "Village as a "Quincy" subsidiary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For a confectionery business using the village's\x01",
            "quality honey, if you apply my company's know-\x01",
            "how, I'm sure it will be profitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've already registered with the city,\x01",
            "and our business is practically in the\x01",
            "process of starting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What is so contradictory\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, about that "plan"\x01",
            "you just mentioned...\x02\x03",
            "#00001FAccording to information we've obtained,\x01",
            "there's a clear, contradictory point.\x02\x03",
            "#00003FYes, that contradictory point is...\x02",
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
            "#1KWhat is the contradictory point\x01",
            "about Minneth's "plan"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Confectionery Know-How\x01",       # 0
            "Moving the Plan Forward\x01",      # 1
            "Plan's Prospects\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9BF")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWhen we checked what you told\x01",
            "us against IBC records, I could\x01",
            "see a contradictory point.\x02\x03",
            "#00001FThat "plan" you mentioned...\x02\x03",
            "In actuality, it hasn't\x01",
            "progressed at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x6)
    Jump("loc_ED6C")

    label("loc_E9BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB11")

    ChrTalk(
        0x101,
        (
            "#00003FThat "plan" you mentioned...\x02\x03",
            "#00001FActually, you don't know a\x01",
            "single thing about how to\x01",
            "make confectioneries, do you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh...? \x01",
            "An interesting opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, what proof do\x01",
            "you have of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F...U-Umm, that's...\x02\x03",
            "#00006F(Damn...\x01",
            "Even if I'm suspecting him,\x01",
            "I must think more carefully.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC5F")

    label("loc_EB11")


    ChrTalk(
        0x101,
        (
            "#00003FThat "plan" you mentioned...\x02\x03",
            "#00001FActually, there's almost\x01",
            "no possibility of\x01",
            "success, isn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh...? \x01",
            "An interesting opinion,\x01",
            "but slightly rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And what do you have that\x01",
            "makes you say that?\x01",
            "I am talking evidence here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F...U-Umm, that's...\x02\x03",
            "#00006F(Damn... I should have\x01",
            "changed my approach.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC5F")


    ChrTalk(
        0x102,
        (
            "#00105FUmm... I might know.\x02\x03",
            "#00100FWe checked IBC's\x01",
            "information and noticed\x01",
            "an inconsistency.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F...That's right!\x02\x03",
            "#00001FMr. Minneth... That "plan" you\x01",
            "mentioned... In actuality, it hasn't\x01",
            "progressed at all. Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x7)

    label("loc_ED6C")

    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "IBC...? W-What\x01",
            "do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPlease think about it. If "Quincy\x01",
            "Company" was intended to further\x01",
            "its plan in Crossbell...\x02\x03",
            "#00001FIt would need a loan from IBC for factory\x01",
            "construction and subsidiary development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For registering the company with the city,\x01",
            "I prepared a proper corporate account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F──You "only" prepared the\x01",
            "account. Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe "Honey Company" account\x01",
            "had the minimum balance\x01",
            "needed to open an account.\x02\x03",
            "Though we didn't learn the exact amount, it was\x01",
            "on the level of some tens of thousands of mira...\x02\x03",
            "#00001FDo you really think you can\x01",
            "construct a factory and operate a\x01",
            "business starting with that amount...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...You looked into\x01",
            "my IBC account...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "M-Mr. Minneth...\x01",
            "Does this mean...!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Oh, please don't misunderstand.\x01",
            "I am not admitting they have a\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I only thought they\x01",
            "were impolite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FB-But... There was\x01",
            "hardly any money\x01",
            "in the account!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "As an employee, I have\x01",
            "to be careful with how\x01",
            "I throw money around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't take out a loan in\x01",
            "the name of the "Quincy\x01",
            "Company", you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Of course, I'll think about discussing\x01",
            "a loan from IBC once I have secured\x01",
            "permission from the main office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh...n-now I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(...A skillful dodge.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No... \x01",
            "I can sense that Mr.\x01",
            "Minneth is flustered.)\x02\x03",
            "#00001F(I'll press the attack and shove\x01",
            "more evidence in his face...!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The look on your face says you\x01",
            "have something else to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYes, of course.\x02\x03",
            "#00004FThat's not the only suspicion\x01",
            "about you, Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "At a time like this you're still...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "No, no, it is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I want to put\x01",
            "you at ease too,\x01",
            "Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...I'd like to ask\x01",
            "about your profile,\x01",
            "Mr. Minneth.\x02\x03",
            "#00003FYou called yourself\x01",
            "a "Quincy Company"\x01",
            "employee, but...\x02\x03",
            "#00013FIs that really true?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Wait... \x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are you saying that\x01",
            "Mr. Minneth isn't with\x01",
            "the "Quincy Company"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, that's what\x01",
            "we believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hehe... Ha ha ha! And I was thinking\x01",
            "what you might have said, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In that case, why don't I show you my\x01",
            "business card or employee ID card?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Even if you have them,\x01",
            "you may have forged them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe found some evidence that\x01",
            "trumps either of those.\x02\x03",
            "#00000FIt was in nothing other than\x01",
            "a Quincy Company pamphlet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "A Quincy Company pamphlet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FThat stuff in milady's room...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWe have its main points written\x01",
            "in our Detective Notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt was ordered directly from the Quincy Company\x01",
            "main office. There shouldn't be any doubt as to\x01",
            "the authenticity of its information.\x02\x03",
            "#00003FAnd, there was a clear\x01",
            "difference between the material\x01",
            "and what you told us yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "W-What I told you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA point you told us that\x01",
            "is contrary to you being\x01",
            "an "employee". That is...\x02",
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
            "#1KWhat is the contradiction between Minneth's\x01",
            "statements yesterday and the material?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Creation of Subsidiary\x01",      # 0
            "Sales Career\x01",                # 1
            "Dislike of Sweets\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFD1")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003F──Yesterday,\x01",
            "you told us this.\x02\x03",
            ""Although I am an employee,\x01",
            "I actually don't like sweet things"...\x02\x03",
            "#00013FDo you deny these words?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_FC0C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC0C)
    Sleep(50)

    def lambda_FC1C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FC1C)
    Sleep(50)

    def lambda_FC2C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FC2C)
    Sleep(50)

    def lambda_FC3C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FC3C)
    Sleep(50)

    def lambda_FC4C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FC4C)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FL-Lloyd...? \x01",
            "Umm, I don't get it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Indeed, I don't like sweet things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, but what\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            ""A man with a dislike of sweets can't possibly\x01",
            "be a confectionery company employee"... \x01",
            "...Is that what you are trying to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FThat's exactly it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-What're you on about...? \x01",
            "Have you no shame as a policem──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F──This was written in the\x01",
            "Quincy Company pamphlet.\x02\x03",
            "#00003F"At Quincy, employees themselves sample\x01",
            "developmental products, and impartially\x01",
            "judge whether they are worthy of sale...".\x02\x03",
            "#00013FThat's basically what it said.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FEA8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEA8)
    Sleep(50)

    def lambda_FEB8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FEB8)
    Sleep(50)

    def lambda_FEC8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FEC8)
    Sleep(50)

    def lambda_FED8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FED8)
    Sleep(50)

    def lambda_FEE8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FEE8)
    Sleep(300)

    ChrTalk(
        0xD,
        "............!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What do you...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S......Ah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt's unnatural for someone like Mr.\x01",
            "Minneth who "dislikes sweets" to be\x01",
            "employed at Quincy Company.\x02\x03",
            "#00013F...Am I wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x8)
    Jump("loc_10695")

    label("loc_FFD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10067")

    ChrTalk(
        0x101,
        (
            "#00003F──Mr. Minneth. \x01",
            "Yesterday, you said this.\x02\x03",
            ""I will create a subsidiary in Armorica\x01",
            "Village", regarding your plan...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10103")

    label("loc_10067")


    ChrTalk(
        0x101,
        (
            "#00003F──Mr. Minneth. \x01",
            "Yesterday, you said this.\x02\x03",
            ""Due to my efforts in the sales field,\x01",
            "I have been recognized and\x01",
            "achieved my current position"...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10103")


    ChrTalk(
        0xD,
        (
            "...I did say that,\x01",
            "but what of it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00011F(D-Damn... \x01",
            "No retorts come to mind!\x01",
            "Did I make a mistake...?)\x02\x03",
            "#00012FU-Umm. That just now\x01",
            "was a little mistake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F──I see. I finally\x01",
            "remembered it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh.\x02",
    )

    CloseMessageWindow()

    def lambda_10209():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10209)
    Sleep(50)

    def lambda_10219():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10219)
    Sleep(50)

    def lambda_10229():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10229)
    Sleep(50)

    def lambda_10239():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10239)
    Sleep(50)

    def lambda_10249():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10249)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F"Although I am an employee,\x01",
            "I actually don't like sweet things"...\x02\x03",
            "#10302FYou said that yesterday,\x01",
            "Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FW-Wazy...? \x01",
            "Umm, I don't get...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Indeed, I don't like sweet things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, but what\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            ""A man with a dislike of sweets can't possibly\x01",
            "be a confectionery company employee"... \x01",
            "...Is that what you are trying to say?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_103D0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_103D0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00203F...Exactly.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10309FHu hu. I looks like you've realized it too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-What're these false accusations!? You all\x01",
            "should be ashamed to call yourselves policem──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F──In the Quincy Company\x01",
            "pamphlet, this was written.\x02\x03",
            ""At Quincy, employees themselves sample\x01",
            "developmental products, and impartially\x01",
            "judge whether they are worthy of sale...".\x02\x03",
            "#10302FThat's basically what it said.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10581():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10581)
    Sleep(50)

    def lambda_10591():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10591)
    Sleep(50)

    def lambda_105A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_105A1)
    Sleep(50)

    def lambda_105B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_105B1)
    Sleep(300)

    ChrTalk(
        0xD,
        "............!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What do you...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S......Ah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt's unnatural for someone like Mr.\x01",
            "Minneth who "dislikes sweets" to be\x01",
            "employed at Quincy Company.\x02\x03",
            "#00201F...Am I wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x9)

    label("loc_10695")


    ChrTalk(
        0xD,
        (
            "...T-That is... \x01",
            "You're misremembering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's not going to work.\x02\x03",
            "#00001F...You just now\x01",
            "admitted that you\x01",
            "don't like sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIf that's the case, then tell us.\x01",
            "Why did you pretend to be a\x01",
            "Quincy Company employee?\x02\x03",
            "#00001FI'll tell you why── It was to gain\x01",
            "Mr. Derrick's trust─ For the purpose\x01",
            "of defrauding him.\x02\x03",
            "#00003FBased on the evidence we have, that's the\x01",
            "only possibility I can think of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAnd the confectionery business\x01",
            "making use of Armorica's honey...\x02\x03",
            "#00101FThe "Quincy Company" name was\x01",
            "a convenient one for using that\x01",
            "idea to gain Mr. Derrick's trust.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "M-Mr. Minneth...\x01",
            "What's the meaning\x01",
            "of this!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You really...\x01",
            "Tricked me!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "...He...Hehe... Mr. Derrick.\x01",
            "You yourself mustn't be\x01",
            "deceived by these people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FW-What did you say?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "Uh uh... Am I not right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As for me coming to Armorica\x01",
            "Village and suggesting this \x01",
            ""Honey Company" plan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If I concede that, if I had an ulterior objective\x01",
            "to come here and deceive Mr. Derrick...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "What exactly are you saying that objective was?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you've no proof of that, you've\x01",
            "got no right to call me a crook!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FA proof you say...\x01",
            "There really was that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003FYour objective── I actually\x01",
            "do have an idea about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10C92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10C92)
    Sleep(50)

    def lambda_10CA2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10CA2)
    Sleep(50)

    def lambda_10CB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10CB2)
    Sleep(50)

    def lambda_10CC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10CC2)
    Sleep(50)

    def lambda_10CD2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10CD2)
    Sleep(50)

    def lambda_10CE2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10CE2)
    Sleep(300)

    ChrTalk(
        0xD,
        "Wh...What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(L-Lloyd, are you sure...!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(I-I have no\x01",
            "idea at all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No... I've definitely got this.)\x02\x03",
            "(Just before we came here,\x01",
            ""that person" searched for us\x01",
            "a "certain piece of evidence"...)\x02\x03",
            "#00001F(Yes, the final clue as to\x01",
            "Minneth's objective...!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What're you mumbling about!? \x01",
            "...Out with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe true reason you\x01",
            "committed fraud in\x01",
            "the village. That is...\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10EA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110C3")
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
            "#1KThe true purpose of Minneth's\x01",
            "Armorica Village fraud is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Seizing Land\x01",                # 0
            "Monopolize Honey Sales\x01",      # 1
            "Sell Fake Orbal Cars\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F8A")
    OP_2C(0x87, 0x1)

    label("loc_10F8A")


    ChrTalk(
        0x101,
        (
            "#00003FYou true objective is...\x02\x03",
            "#00013FOwnership of the "land"\x01",
            "of Armorica Village itself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110BE")

    label("loc_10FF0")


    ChrTalk(
        0x101,
        (
            "#00006F(No... that's wrong.\x01",
            "It's not something\x01",
            "on such a small scale.)\x02\x03",
            "#00001F(He spent all this time\x01",
            "preparing... His aim has\x01",
            "to be something bigger.)\x02\x03",
            "#00003F(Minneth's true\x01",
            "object... That's...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_110BE")

    Jump("loc_10EA4")

    label("loc_110C3")


    ChrTalk(
        0xD,
        "...W...ha...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FMr. Harold, a trader we know, \x01",
            "got some information for us\x01",
            "regarding you.\x02\x03",
            "#00000FMr. Minneth, right after you arrived in\x01",
            "Crossbell, it seems you were looking\x01",
            "into land prices of all the areas.\x02\x03",
            "#00003FIf you were a "Quincy Company" employee\x01",
            "looking for new business opportunities,\x01",
            "that would not be necessary.\x02\x03",
            "So why, then? There's only one\x01",
            "possibility I can think of.\x02\x03",
            "#00013FIt was because your objective\x01",
            "is to seize the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FR-Really...!?\x01",
            "I-I would've never\x01",
            "expected that.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FAnd that's not all.\x02\x03",
            "#00002FLike you can see, Armorica Village\x01",
            "is surrounded by nature's beauty.\x01",
            "It's a prime location.\x02\x03",
            "#00004FSuppose you transferred it to a third\x01",
            "party for managing villas... How much\x01",
            "do you think you could get for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThere're people who would\x01",
            "pay tens of millions of mira \x01",
            "for something like this.\x02\x03",
            "#00101FI don't think the villagers\x01",
            "would ever agree to it...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FYeah. That's exactly\x01",
            "why he was able to make\x01",
            "this whole scheme work.\x02\x03",
            "#00001FIf we assume your objective\x01",
            "was the land itself, it would\x01",
            "explain all of your actions.\x02\x03",
            "You'd obtain the deeds for\x01",
            "the vast lotus fields, a lot of\x01",
            "farmland, the private property...\x02\x03",
            "And under the pretext of\x01",
            "returning to the main office,\x01",
            "you'd disappear from Crossbell.\x02\x03",
            "#00003FThen, you'd sell the deeds\x01",
            "through the black market and\x01",
            "make a huge sum of mira...\x02\x03",
            "#00013FThat's your true objective...\x01",
            "Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11671():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11671)
    Sleep(50)

    def lambda_11681():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11681)
    Sleep(50)

    def lambda_11691():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11691)
    Sleep(50)

    def lambda_116A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116A1)
    Sleep(50)

    def lambda_116B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_116B1)
    Sleep(300)

    ChrTalk(
        0xD,
        "...U...gh...gh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Mr.... Minneth...\x01",
            "No way...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1F, -1730, 390, 7230, 225)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    NpcTalk(
        0x1F,
        "Man's Voice",
        "──Mr. Lloyd...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_117E9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117E9)
    Sleep(50)

    def lambda_117F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117F9)
    Sleep(50)

    def lambda_11809():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11809)
    Sleep(50)

    def lambda_11819():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11819)
    Sleep(50)

    def lambda_11829():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11829)
    Sleep(50)

    def lambda_11839():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11839)
    Sleep(50)

    def lambda_11849():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11849)
    Sleep(50)

    def lambda_11859():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_11859)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FThis voice is...\x02",
    )

    CloseMessageWindow()
    OP_68(2080, 1500, 14610, 3000)
    MoveCamera(288, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16200, 3000)
    SetChrPos(0x1D, -1100, 450, 5260, 45)
    SetChrPos(0x1F, -2810, 450, 5340, 45)
    SetChrPos(0x1E, -2009, 420, 6880, 45)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    OP_0D()
    BeginChrThread(0x1E, 3, 0, 49)
    BeginChrThread(0x1F, 3, 0, 48)
    Sleep(200)
    BeginChrThread(0x1D, 3, 0, 47)
    WaitChrThread(0x1E, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        "#03600FThank goodness, it seems we made it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Derrick...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Father, Mr. Harold...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAnd you... I'm sure you're\x01",
            "from the law office...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm Lawyer Ian's\x01",
            "assistant, Pete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Normally Mr. Grimwood would come, but\x01",
            "he had to leave for something related\x01",
            "to the constitution drafting process...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FIs that...evidence?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03603FYes. Mr. Grimwood called\x01",
            "it "insurance" earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Please take a look at this, everyone.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pete produced a single photograph\x01",
            "and everyone examined it.\x02\x03",
            "A man with the air of a trader, and with the\x01",
            "same face as Minneth, was depicted therein.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FT-The man appearing in the picture...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "W-Why...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why do you guys have\x01",
            "such a photograph!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Lawyer Ian got this photograph\x01",
            "a long time ago from a reporter\x01",
            "he knew in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "But the name on the\x01",
            "photograph isn't "Minneth"... \x01",
            "It's "Ridner".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FRidner...? I think we\x01",
            "heard that name\x01",
            "somewhere recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F...Ah!\x01",
            "That's it...!\x02\x03",
            "#00101FIt's the name of the man who\x01",
            "stole that Imperial Baron's family\x01",
            "land Lawyer Ian told us about!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FOh yeah, that was his name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03601FYes... I asked Lawyer Ian\x01",
            "about it once again and he\x01",
            "said there's no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHmm... If that's the case, then\x01",
            "it seems a pretty interesting\x01",
            "truth is now revealed to us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FLloyd, tell him...tell Minneth\x01",
            "what this means, hm?\x02\x03",
            "#10304FThe meaning of this photo, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Yeah, got it.\x02",
    )

    CloseMessageWindow()
    OP_68(2020, 1500, 16370, 3000)

    def lambda_1207B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1207B)
    Sleep(50)

    def lambda_1208B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1208B)
    Sleep(50)

    def lambda_1209B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1209B)
    Sleep(50)

    def lambda_120AB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_120AB)
    Sleep(50)

    def lambda_120BB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_120BB)
    Sleep(50)

    def lambda_120CB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_120CB)
    Sleep(50)

    def lambda_120DB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_120DB)
    Sleep(50)

    def lambda_120EB():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_120EB)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00001FThe reason that "Ridner" in the\x01",
            "photo and "Minneth" standing before\x01",
            "us have the same face, that is...\x02",
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
            "#1KThe reason Ridner and Minneth\x01",
            "have the same face is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Twins\x01",            # 0
            "Disguise\x01",         # 1
            "Same Person\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122BE")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FMinneth and Ridner are the same\x01",
            "person... That's the only possibility.\x02\x03",
            "#00013FAnd because they're the same person,\x01",
            "even the modus operandi is similar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1254B")

    label("loc_122BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12325")

    ChrTalk(
        0x101,
        (
            "#00003FMinneth and Ridner are... twins.\x01",
            "That's the only thing I can think of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1236E")

    label("loc_12325")


    ChrTalk(
        0x101,
        (
            "#00003FMinneth is... Ridner in disguise.\x01",
            "That's all I can think of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1236E")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_64(0x1D)
    OP_64(0x1F)
    OP_64(0x1E)

    ChrTalk(
        0x105,
        (
            "#10306F...Aren't you reading\x01",
            "too much into it?\x02\x03",
            "#10302FNo matter how you slice it,\x01",
            "Minneth and Ridner\x01",
            "are the same person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-I overthought it, huh...)\x02\x03",
            "#00013F*ahem*, and so...\x01",
            "because they're the same person,\x01",
            "even the modus operandi is similar.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1254B")


    ChrTalk(
        0x1D,
        "Lawyer Ian said as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Most likely, he's\x01",
            "proud of his\x01",
            "fraud technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA "crook"── That's what you're, Minneth. \x01",
            "A charge of fraud is obvious.\x02\x03",
            "#00013FOn top of that, it's likely you're the same\x01",
            "person who committed fraud in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf you search hard enough you're bound to find the\x01",
            "skeletons in their closet, ain't what they say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWe would definitely love to\x01",
            "hear the details... \x01",
            "In the police HQ interrogation room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Y... You...\x01",
            "Damn youuuu...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Doing... Doing a perfect\x01",
            "job is my creed, however...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xD,
        "#4SThese... THESE GREENHORNS!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "M-Mr. Minneth...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1194)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "...Hmph, well I wouldn't be so\x01",
            "full of myself if I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sorry, but I haven't the\x01",
            "slightest intention of being\x01",
            "caught over something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat...!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "──Come, beasts!\x02",
    )

    CloseMessageWindow()
    Sound(325, 0, 70, 0)
    WaitBGM()
    PlayBGM("ed7561", 0)
    Sleep(500)
    Fade(500)
    OP_68(10120, 700, -16210, 0)
    MoveCamera(326, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x22, 0x20)
    SetChrFlags(0x23, 0x20)
    SetChrFlags(0x24, 0x20)
    SetChrPos(0x20, 11900, 200, -14590, 180)
    SetChrPos(0x21, 11900, 200, -14590, 180)
    SetChrPos(0x22, 11900, 200, -14590, 180)
    SetChrPos(0x23, 11900, 200, -14590, 180)
    SetChrPos(0x24, 11900, 200, -14590, 180)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    OP_0D()
    OP_71(0xD, 0xF1, 0x10E, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_79(0xD)
    Sound(948, 0, 100, 0)
    Sleep(1000)
    Sleep(500)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x20, 3, 0, 52)
    Sleep(700)
    BeginChrThread(0x28, 1, 0, 63)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x21, 3, 0, 53)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x22, 3, 0, 54)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x23, 3, 0, 55)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x24, 3, 0, 56)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x28, 0x1)
    OP_68(620, 700, 17350, 0)
    MoveCamera(294, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0xC, 4960, 0, 19520, 270)
    SetChrPos(0xD, 5370, 0, 18730, 225)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x20, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x20, -6100, 0, 14940, 135)
    SetChrPos(0x21, -3890, 0, 18870, 135)
    SetChrPos(0x22, -620, 0, 21820, 180)
    SetChrPos(0x23, 3420, 0, 20140, 225)
    SetChrPos(0x24, 3620, 0, 23850, 180)
    BeginChrThread(0x20, 3, 0, 50)
    BeginChrThread(0x21, 3, 0, 50)
    BeginChrThread(0x22, 3, 0, 50)
    BeginChrThread(0x23, 3, 0, 50)
    BeginChrThread(0x24, 3, 0, 50)
    SetChrPos(0x101, 1560, 10, 17040, 0)
    SetChrPos(0x102, 2380, 0, 16239, 0)
    SetChrPos(0x103, 1370, 10, 15400, 0)
    SetChrPos(0x104, 60, 10, 17000, 315)
    SetChrPos(0x109, -290, 0, 15050, 315)
    SetChrPos(0x105, -1310, 10, 16350, 315)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "W-Whaaaa!?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010FM-Monsters!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAnd they look\x01",
            "well-trained....!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F(These guys, don't tell me that...!?)\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xC, 0xB4, 0x3E8, 0x3E8, 0x0)
    Sleep(100)

    ChrTalk(
        0xC,
        "...Ugh... Ah...\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x1D, 0x0, 0x1F4, 0x1388, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "D-Derrick!!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x87, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x1F,
        "#03605FV-Village Chief, it's dangerous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107FYou... \x01",
            "Do you have any idea\x01",
            "what you're doing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, I know exactly what I'm doing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, don't you think even for mistake\x01",
            "to try to fight or stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Unless you want me to hurt\x01",
            "Mr. Derrick or the villagers, eh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, out of my way, please.\x02",
    )

    CloseMessageWindow()
    OP_68(-480, 1500, 13490, 5000)
    MoveCamera(333, 20, 0, 5000)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_1306E():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1306E)

    def lambda_1307B():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1307B)

    def lambda_13088():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13088)

    def lambda_13095():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13095)

    def lambda_130A2():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_130A2)

    def lambda_130AF():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_130AF)

    def lambda_130BC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_130BC)

    def lambda_130C9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_130C9)

    def lambda_130D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_130D6)
    WaitChrThread(0x105, 1)

    def lambda_130E7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_130E7)
    Sleep(50)

    def lambda_130FF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_130FF)
    Sleep(50)

    def lambda_13117():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13117)
    Sleep(50)

    def lambda_1312F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1312F)
    Sleep(50)

    def lambda_13147():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13147)
    Sleep(50)

    def lambda_1315F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1315F)
    Sleep(50)

    def lambda_13177():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_13177)
    Sleep(50)

    def lambda_1318F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1318F)
    Sleep(50)

    def lambda_131A7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_131A7)
    Sleep(50)

    def lambda_131BF():
        OP_95(0xFE, -1910, 0, 11190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_131BF)
    WaitChrThread(0x1F, 1)

    def lambda_131DD():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_131DD)
    WaitChrThread(0x1D, 1)

    def lambda_131EE():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_131EE)
    WaitChrThread(0x1E, 1)

    def lambda_131FF():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_131FF)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(2000)
    OP_93(0x23, 0xB4, 0x0)

    def lambda_1325E():

        label("loc_1325E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1325E")

    QueueWorkItem2(0x101, 1, lambda_1325E)
    Sleep(50)

    def lambda_13273():

        label("loc_13273")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_13273")

    QueueWorkItem2(0x102, 1, lambda_13273)
    Sleep(50)

    def lambda_13288():

        label("loc_13288")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_13288")

    QueueWorkItem2(0x103, 1, lambda_13288)
    Sleep(50)

    def lambda_1329D():

        label("loc_1329D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1329D")

    QueueWorkItem2(0x104, 1, lambda_1329D)
    Sleep(50)

    def lambda_132B2():

        label("loc_132B2")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_132B2")

    QueueWorkItem2(0x105, 1, lambda_132B2)
    Sleep(50)

    def lambda_132C7():

        label("loc_132C7")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_132C7")

    QueueWorkItem2(0xC, 1, lambda_132C7)
    Sleep(50)

    def lambda_132DC():

        label("loc_132DC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_132DC")

    QueueWorkItem2(0x1D, 1, lambda_132DC)
    Sleep(50)

    def lambda_132F1():

        label("loc_132F1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_132F1")

    QueueWorkItem2(0x1F, 1, lambda_132F1)
    Sleep(50)

    def lambda_13306():

        label("loc_13306")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_13306")

    QueueWorkItem2(0x1E, 1, lambda_13306)
    Sleep(100)

    def lambda_1331B():

        label("loc_1331B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1331B")

    QueueWorkItem2(0x109, 1, lambda_1331B)
    Sleep(50)

    def lambda_13330():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13330)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    def lambda_1337C():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1337C)
    Sleep(50)

    def lambda_13394():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_13394)
    Sleep(50)

    def lambda_133AC():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_133AC)
    Sleep(500)

    ChrTalk(
        0xD,
        "Uh uh, farewell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "We won't ever meet again.\x02",
    )

    CloseMessageWindow()

    def lambda_133F9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_133F9)
    Sleep(3000)
    BeginChrThread(0x28, 1, 0, 63)
    BeginChrThread(0x20, 3, 0, 57)
    Sleep(500)
    BeginChrThread(0x21, 3, 0, 58)
    Sleep(500)
    BeginChrThread(0x22, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x23, 3, 0, 60)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 61)
    Sleep(3000)
    Fade(500)
    OP_68(1180, 1500, 16250, 0)
    MoveCamera(337, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x1D, -170, 0, 13620, 45)
    SetChrPos(0x1F, -880, 0, 12290, 45)
    SetChrPos(0x1E, -2560, 0, 13500, 45)
    SetChrPos(0x101, -2100, 0, 15860, 180)
    SetChrPos(0x102, -1230, 0, 16850, 180)
    SetChrPos(0x103, -600, 0, 18000, 180)
    SetChrPos(0x104, -3190, 0, 16370, 180)
    SetChrPos(0x109, -2640, 0, 17580, 180)
    SetChrPos(0x105, -1830, 0, 18600, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    OP_0D()
    EndChrThread(0x28, 0x1)

    ChrTalk(
        0x1D,
        "D-Derrick...!!\x02",
    )

    CloseMessageWindow()

    def lambda_1354C():
        OP_95(0xFE, 5240, 0, 18260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1354C)
    Sleep(100)

    def lambda_13569():
        OP_95(0xFE, 3790, 0, 19250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_13569)
    Sleep(100)

    def lambda_13586():
        OP_95(0xFE, 3560, 0, 17530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_13586)
    WaitChrThread(0x1D, 1)

    def lambda_135A4():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_135A4)
    WaitChrThread(0x1F, 1)

    def lambda_135B5():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_135B5)
    WaitChrThread(0x1E, 1)

    def lambda_135C6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_135C6)
    WaitChrThread(0x1E, 1)

    ChrTalk(
        0xC,
        "Ooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FDamn, as if I'd let him get away...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FLet's go...!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_1365D():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1365D)
    Sleep(100)

    def lambda_1367A():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1367A)
    Sleep(100)

    def lambda_13697():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13697)
    Sleep(100)

    def lambda_136B4():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_136B4)
    Sleep(100)

    def lambda_136D1():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_136D1)
    Sleep(100)

    def lambda_136EE():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_136EE)
    Sleep(500)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(8750, 1500, -17760, 0)
    MoveCamera(345, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, -1860, 0, -3290, 180)
    SetChrPos(0x102, -3230, 0, -2980, 180)
    SetChrPos(0x103, -930, 0, -2320, 180)
    SetChrPos(0x104, -2380, 0, -1730, 180)
    SetChrPos(0x109, -1370, 0, -940, 180)
    SetChrPos(0x105, -3640, 0, -1220, 180)
    OP_0D()
    OP_71(0xD, 0x10F, 0x12C, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 42)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 43)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 46)
    Sleep(500)
    OP_71(0xD, 0x3C, 0x5A, 0x0, 0x0)
    Sound(494, 0, 100, 0)
    Sleep(500)
    OP_68(6900, 1500, -19750, 3000)
    MoveCamera(345, 24, 0, 3000)
    BeginChrThread(0x25, 1, 0, 62)
    OP_71(0xD, 0x79, 0xB4, 0x1, 0x20)
    Sleep(800)
    OP_6F(0x79)
    OP_68(6820, 1500, -15790, 3000)
    SetCameraDistance(15150, 3000)
    WaitChrThread(0x101, 3)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 3)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 3)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 3)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 3)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 3)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00105FYeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FIt seems like\x01",
            "he got away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOoh... This is so aggravating!\x01",
            "To think we couldn't catch\x01",
            "a coward like that...!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006F...Anyway, I'm glad no\x01",
            "harm came to the villagers.\x02\x03",
            "#00000FI think that can be considered\x01",
            "an acceptable result too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy. I guess we'll need to look\x01",
            "forward to capturing him next time.\x02\x03",
            "#10300FFor now, let's meet with the Village Chief and\x01",
            "the others to report the details of this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(............)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_D4A8 end

    def Function_35_13B1C(): pass

    label("Function_35_13B1C")

    OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 2060, 0, 16660, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_35_13B1C end

    def Function_36_13B50(): pass

    label("Function_36_13B50")

    OP_97(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 1450, 0, 17650, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_36_13B50 end

    def Function_37_13B84(): pass

    label("Function_37_13B84")

    OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2050, 0, 15310, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_37_13B84 end

    def Function_38_13BB8(): pass

    label("Function_38_13BB8")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 420, 0, 18380, 2000, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_38_13BB8 end

    def Function_39_13BEC(): pass

    label("Function_39_13BEC")

    OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 870, 0, 16059, 2000, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)
    Return()

    # Function_39_13BEC end

    def Function_40_13C20(): pass

    label("Function_40_13C20")

    OP_97(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 170, 0, 17060, 2000, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_40_13C20 end

    def Function_41_13C54(): pass

    label("Function_41_13C54")

    OP_97(0x101, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 7230, 0, -14950, 3500, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_41_13C54 end

    def Function_42_13C88(): pass

    label("Function_42_13C88")

    OP_97(0x102, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 5740, 0, -15440, 3500, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_42_13C88 end

    def Function_43_13CBC(): pass

    label("Function_43_13CBC")

    OP_97(0x103, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 7140, 0, -13390, 3500, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_43_13CBC end

    def Function_44_13CF0(): pass

    label("Function_44_13CF0")

    OP_97(0x104, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 5860, 0, -14270, 3500, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_44_13CF0 end

    def Function_45_13D24(): pass

    label("Function_45_13D24")

    OP_97(0x109, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 5870, 0, -12970, 3500, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_45_13D24 end

    def Function_46_13D58(): pass

    label("Function_46_13D58")

    OP_97(0x105, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 4340, 0, -14470, 3500, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_46_13D58 end

    def Function_47_13D8C(): pass

    label("Function_47_13D8C")

    OP_97(0x1D, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1D, 1)
    OP_95(0x1D, -1530, 0, 11680, 2000, 0x0)
    OP_93(0x1D, 0x2D, 0x1F4)
    Return()

    # Function_47_13D8C end

    def Function_48_13DC0(): pass

    label("Function_48_13DC0")

    OP_97(0x1F, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1F, 1)
    OP_95(0x1F, -2380, 0, 13280, 2000, 0x0)
    OP_93(0x1F, 0x2D, 0x1F4)
    Return()

    # Function_48_13DC0 end

    def Function_49_13DF4(): pass

    label("Function_49_13DF4")

    OP_97(0x1E, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1E, 1)
    OP_95(0x1E, -720, 0, 12970, 2000, 0x0)
    OP_93(0x1E, 0x2D, 0x1F4)
    Return()

    # Function_49_13DF4 end

    def Function_50_13E28(): pass

    label("Function_50_13E28")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E4F")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_13E33")

    label("loc_13E4F")

    Return()

    # Function_50_13E28 end

    def Function_51_13E50(): pass

    label("Function_51_13E50")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E72")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_13E5B")

    label("loc_13E72")

    Return()

    # Function_51_13E50 end

    def Function_52_13E73(): pass

    label("Function_52_13E73")


    def lambda_13E78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_13E78)

    def lambda_13E89():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_13E89)
    WaitChrThread(0x20, 1)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0x20, 4710, 0, -15670, 6000, 0x0)
    OP_95(0x20, -2120, 0, -1730, 6000, 0x0)
    OP_95(0x20, -2120, 0, 14270, 6000, 0x0)
    Return()

    # Function_52_13E73 end

    def Function_53_13EE8(): pass

    label("Function_53_13EE8")


    def lambda_13EED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_13EED)

    def lambda_13EFE():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13EFE)
    WaitChrThread(0x21, 1)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0x21, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x21, 830, 0, -10410, 7000, 0x0)
    OP_95(0x21, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x21, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_53_13EE8 end

    def Function_54_13F71(): pass

    label("Function_54_13F71")


    def lambda_13F76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_13F76)

    def lambda_13F87():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_13F87)
    WaitChrThread(0x22, 1)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0x22, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x22, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x22, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_54_13F71 end

    def Function_55_13FE6(): pass

    label("Function_55_13FE6")


    def lambda_13FEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_13FEB)

    def lambda_13FFC():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_13FFC)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0x23, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x23, 830, 0, -10410, 7000, 0x0)
    OP_95(0x23, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x23, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_55_13FE6 end

    def Function_56_1406F(): pass

    label("Function_56_1406F")


    def lambda_14074():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_14074)

    def lambda_14085():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_14085)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0x24, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x24, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x24, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_56_1406F end

    def Function_57_140E4(): pass

    label("Function_57_140E4")

    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_57_140E4 end

    def Function_58_1412F(): pass

    label("Function_58_1412F")

    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_58_1412F end

    def Function_59_1417A(): pass

    label("Function_59_1417A")

    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_59_1417A end

    def Function_60_141C5(): pass

    label("Function_60_141C5")

    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_60_141C5 end

    def Function_61_14210(): pass

    label("Function_61_14210")

    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_61_14210 end

    def Function_62_1425B(): pass

    label("Function_62_1425B")

    OP_9E(0xFE, 0x316, 0xFFFFE642, 0xEA60, 0x1B58, 0x4)
    Sound(487, 0, 100, 0)
    Sleep(500)
    Sleep(200)
    Sound(486, 0, 100, 0)
    OP_9F(0x0, 0x25)
    OP_9F(0x1, 12190, 0, -23580)
    OP_9F(0x1, 16760, 0, -26550)
    OP_9F(0x1, 23260, 0, -32810)
    OP_9F(0x2, 0x25, 9000, 0x6)
    Return()

    # Function_62_1425B end

    def Function_63_142BA(): pass

    label("Function_63_142BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_142D3")
    Sound(845, 0, 80, 0)
    Sleep(350)
    Jump("Function_63_142BA")

    label("loc_142D3")

    Return()

    # Function_63_142BA end

    def Function_64_142D4(): pass

    label("Function_64_142D4")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1720, 1500, -10600, 0)
    MoveCamera(344, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, 720, 0, -10290, 325)
    SetChrPos(0x102, 1980, 0, -9830, 325)
    SetChrPos(0x103, 740, 0, -11540, 325)
    SetChrPos(0x104, 2190, 0, -11320, 325)
    SetChrPos(0x109, 2210, 0, -12700, 325)
    SetChrPos(0x105, 3580, 0, -11240, 325)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_1438E():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1438E)
    Sleep(50)

    def lambda_143A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_143A6)
    Sleep(50)

    def lambda_143BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_143BE)
    Sleep(50)

    def lambda_143D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_143D6)
    Sleep(50)

    def lambda_143EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_143EE)
    Sleep(50)

    def lambda_14406():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14406)
    OP_68(1050, 1500, -9540, 3000)
    SetCameraDistance(17450, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1443F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1443F)
    WaitChrThread(0x101, 1)

    def lambda_14450():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14450)
    WaitChrThread(0x102, 1)

    def lambda_14461():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14461)
    WaitChrThread(0x103, 1)

    def lambda_14472():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14472)
    WaitChrThread(0x104, 1)

    def lambda_14483():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14483)
    WaitChrThread(0x109, 1)

    def lambda_14494():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14494)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000FWe arrived at Armorica Village, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhere could Mr. Geval be in this village...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAnyway, let's try searchin'\x01",
            "suspicious places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt might be a good idea to\x01",
            "speak with the villagers, too.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19D, 2)
    ModifyEventFlags(0, 2, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1810, 0, -3210, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x90, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_64_142D4 end

    def Function_65_145D8(): pass

    label("Function_65_145D8")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_1467B")

    ChrTalk(
        0x101,
        (
            "#00000F...Let's try speaking with the Village\x01",
            "Chief. He may know something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146FD")

    label("loc_1467B")


    ChrTalk(
        0x101,
        (
            "#00003FThere's the presence of someone inside...\x02\x03",
            "#00000FAnyway, let's keep asking\x01",
            "around. The villagers may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146FD")

    TalkEnd(0xFF)
    Return()

    label("loc_14701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14713")
    TalkEnd(0xFF)
    Jump("loc_14AB8")

    label("loc_14713")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15660, 5000, 47180, 0)
    MoveCamera(313, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 15740, 3500, 47460, 0)
    SetChrPos(0x102, 15140, 3500, 46070, 0)
    SetChrPos(0x103, 16540, 3500, 46260, 0)
    SetChrPos(0x104, 15130, 3500, 44850, 0)
    SetChrPos(0x109, 16950, 3500, 45060, 0)
    SetChrPos(0x105, 16149, 3500, 43850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FLloyd, is this place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWas it locked when\x01",
            "we came here before...?\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 80, 0)
    Sleep(400)
    Sound(811, 0, 50, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FThat sound just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...There's someone inside. For sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, I think so too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu. It's plainly suspicious.\x02",
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_14A12")

    ChrTalk(
        0x101,
        "#00003FCould it be...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F...Let's try speaking with the village\x01",
            "chief. He may know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_14A7F")

    label("loc_14A12")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F...Anyway, for\x01",
            "now, let's keep\x01",
            "getting info.\x02\x03",
            "#00001FThe villagers may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 16100, 3500, 45380, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_14AB8")

    Return()

    # Function_65_145D8 end

    def Function_66_14AB9(): pass

    label("Function_66_14AB9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(16250, 5000, 46160, 0)
    MoveCamera(318, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15440, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 15770, 3500, 47280, 0)
    SetChrPos(0x101, 16040, 3500, 45180, 0)
    SetChrPos(0x102, 15140, 3500, 44440, 0)
    SetChrPos(0x103, 17030, 3500, 44510, 0)
    SetChrPos(0x104, 16260, 3500, 43520, 0)
    SetChrPos(0x109, 15070, 3500, 42860, 0)
    SetChrPos(0x105, 17520, 3500, 43210, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            "...This is the Village Chief, Tolta.\x01",
            "May I have a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "There're some people here\x01",
            "who want to speak with you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "......!\x02\x03",
            "C-Can you do me the favor\x01",
            "and tell them to go away?\x02\x03",
            "I'm sure I'm causing you trouble,\x01",
            "but I would like to not see\x01",
            "anyone for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "...Please relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "The ones who came to see you\x01",
            "aren't your son and his wife.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "H-How do you know that...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FMr. Geval, can you hear me?\x02\x03",
            "#00000FCrossbell Police,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P-Police...!?\x02\x03",
            "W-What do you want with me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Sorry for showing up all of a sudden.\x02\x03",
            "#00000FWe accepted a request from\x01",
            "Mr. Alm and Mrs. Aerie,\x01",
            "and we were looking for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wha...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe don't intend to take you\x01",
            "away with force. We don't\x01",
            "even have that authority.\x02\x03",
            "#00004FIf you insist, we'll explain\x01",
            "things to Mr. Alm and Mrs.\x01",
            "Aerie and abandon the request.\x02\x03",
            "#00000FPlease, will you at\x01",
            "least hear us out?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "............\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00100FIt looks like he unlocked it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah...\x01",
            "Then, let's go inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x1F4)
    OP_9B(0x1, 0x1D, 0xB4, 0x3E8, 0x7D0, 0x0)
    OP_95(0x101, 15770, 3500, 47280, 2000, 0x0)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 67)
    BeginChrThread(0x102, 3, 0, 68)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 69)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 71)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 72)
    WaitChrThread(0x105, 3)
    BeginChrThread(0x1D, 3, 0, 73)
    WaitChrThread(0x1D, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_14AB9 end

    def Function_67_15142(): pass

    label("Function_67_15142")

    OP_93(0x101, 0x0, 0x0)

    def lambda_1514E():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1514E)

    def lambda_15163():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15163)
    Return()

    # Function_67_15142 end

    def Function_68_15170(): pass

    label("Function_68_15170")

    OP_95(0x102, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x0)

    def lambda_15190():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15190)

    def lambda_151A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_151A5)
    Return()

    # Function_68_15170 end

    def Function_69_151B2(): pass

    label("Function_69_151B2")

    OP_95(0x103, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x103, 0x0, 0x0)

    def lambda_151D2():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_151D2)

    def lambda_151E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_151E7)
    Return()

    # Function_69_151B2 end

    def Function_70_151F4(): pass

    label("Function_70_151F4")

    OP_95(0x104, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_15214():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15214)

    def lambda_15229():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15229)
    Return()

    # Function_70_151F4 end

    def Function_71_15236(): pass

    label("Function_71_15236")

    OP_95(0x109, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x109, 0x0, 0x0)

    def lambda_15256():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15256)

    def lambda_1526B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1526B)
    Return()

    # Function_71_15236 end

    def Function_72_15278(): pass

    label("Function_72_15278")

    OP_95(0x105, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x105, 0x0, 0x0)

    def lambda_15298():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15298)

    def lambda_152AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_152AD)
    Return()

    # Function_72_15278 end

    def Function_73_152BA(): pass

    label("Function_73_152BA")

    OP_95(0x1D, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x0)

    def lambda_152DA():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_152DA)

    def lambda_152EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_152EF)
    Return()

    # Function_73_152BA end

    def Function_74_152FC(): pass

    label("Function_74_152FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(15430, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x26,
        "My father is in there, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes. There's no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHe even promised he'd\x01",
            "see both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Oh, thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "I honestly don't know why he's\x01",
            "hiding in a place like that, but...\x01",
            "You guys really did it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        (
            "Uh uh, that's great, Alm.\x01",
            "I'll finally get to meet\x01",
            "my father-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "We'll need to apologize\x01",
            "for not inviting him to\x01",
            "our wedding, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Oh, Aerie...\x01",
            "Why is your\x01",
            "heart so pure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Your heart is as clear as fresh snow.\x01",
            "That's why I love you so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Oh, Alm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#4SPlease get in the shed.\x02",
    )

    CloseMessageWindow()

    def lambda_15679():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15679)
    Sleep(50)

    def lambda_15689():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15689)
    Sleep(300)

    ChrTalk(
        0x26,
        "Huh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhuhu, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "You too, Almin.\x01",
            "S-o-r-r-y.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "Baby",
        "*goo*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Well done.\x02",
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
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10106F(T-This is tiring...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "A-Anyway, Mr. Geval's\x01",
            "waiting for you inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu... Please,\x01",
            "take as long\x01",
            "as you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Sure, we'll do just that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Let's go, Aerie.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yes, Alm.\x02",
    )

    CloseMessageWindow()

    def lambda_15895():
        OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15895)
    Sleep(300)

    def lambda_158B2():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_158B2)

    def lambda_158C7():

        label("loc_158C7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_158C7")

    QueueWorkItem2(0x101, 1, lambda_158C7)
    Sleep(50)

    def lambda_158DC():

        label("loc_158DC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_158DC")

    QueueWorkItem2(0x102, 1, lambda_158DC)
    Sleep(50)

    def lambda_158F1():

        label("loc_158F1")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_158F1")

    QueueWorkItem2(0x103, 1, lambda_158F1)
    Sleep(50)

    def lambda_15906():

        label("loc_15906")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15906")

    QueueWorkItem2(0x104, 1, lambda_15906)
    Sleep(50)

    def lambda_1591B():

        label("loc_1591B")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_1591B")

    QueueWorkItem2(0x109, 1, lambda_1591B)
    Sleep(50)

    def lambda_15930():

        label("loc_15930")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15930")

    QueueWorkItem2(0x105, 1, lambda_15930)
    Sleep(50)

    def lambda_15945():

        label("loc_15945")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15945")

    QueueWorkItem2(0x1D, 1, lambda_15945)
    WaitChrThread(0x26, 1)
    OP_93(0x26, 0x0, 0x1F4)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x26, 3, 0, 75)
    Sleep(500)
    BeginChrThread(0x27, 3, 0, 75)
    Sleep(500)
    WaitChrThread(0x27, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_152FC end

    def Function_75_159D7(): pass

    label("Function_75_159D7")

    OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x0)

    def lambda_159F7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_159F7)

    def lambda_15A0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15A0C)
    Return()

    # Function_75_159D7 end

    def Function_76_15A19(): pass

    label("Function_76_15A19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x26,
        "Thank you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Thanks to you, I got to see my father again. \x01",
            "I got to introduce Aerie and Almin to him, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Uh uh, my father-in-law\x01",
            "looked very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, I'm just glad we could help.\x02\x03",
            "#00005FUmm, about Mr. Geval...\x01",
            "Is he still in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Yes, he said he had something to think\x01",
            "about and will return home later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "When we were talking to him, he turned away\x01",
            "from us suddenly and wouldn't show his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "I wonder why though...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FEven the eyes of a corrupt congressman\x01",
            "are capable of cryin', I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FI am surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, well this\x01",
            "is a hard moment\x01",
            "for a man.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, well I'm sure everything will\x01",
            "be all right. Please don't worry.\x02\x03",
            "#00000FWhat will you guys do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Since I was able to\x01",
            "reunite with father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "We'll have to talk\x01",
            "about how we can\x01",
            "keep in touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Because of my mother-\x01",
            "in-law it might not be\x01",
            "that simple, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "I plan on having him visit\x01",
            "us in Liberl someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FI see... \x01",
            "Uh uh, I hope it goes well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "It seems he quit being a\x01",
            "congressman, so I think\x01",
            "he'll eventually visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Yes... A bright future is\x01",
            "waiting for all of us!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Isn't that right, Aerie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yes, Alm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "When we first held this\x01",
            "child, both of us swore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Let's give Almin here lots of\x01",
            "little brothers and sisters, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "...You and I, and lots\x01",
            "of lovable children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Together, we'll make the best family on\x01",
            "the continent. ...That's what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Oh, I love you so, Aerie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "So do I, Alm!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
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
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Really, we didn't need\x01",
            "to hear all of that, but...\x01",
            "Well, whatever...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo, request\x01",
            "complete, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_163A2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_163A2)
    Sleep(50)

    def lambda_163B2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_163B2)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Yes, you really helped us out.\x01",
            "I don't know how we\x01",
            "can ever thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "We'll be returning home to\x01",
            "Liberl in a little while. Thank\x01",
            "you so much for all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FPlease have a safe trip.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Aerie, since we're\x01",
            "here, why not go\x01",
            "sightseeing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "I agree, Alm. Let's.\x02",
    )

    CloseMessageWindow()
    OP_93(0x27, 0x87, 0x0)

    def lambda_164FD():
        OP_9B(0x1, 0xFE, 0xB4, 0x262, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_164FD)
    Sleep(100)

    def lambda_16515():
        OP_95(0xFE, 13050, 3500, 45510, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_16515)
    WaitChrThread(0x26, 1)
    OP_93(0x27, 0xE1, 0x1F4)
    Sleep(500)
    OP_68(12010, 5000, 41990, 4000)
    MoveCamera(340, 27, 0, 4000)
    OP_6E(600, 4000)

    def lambda_16562():
        OP_95(0xFE, 7890, 3500, 42250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_16562)

    def lambda_1657C():
        OP_95(0xFE, 6900, 3500, 42860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1657C)

    def lambda_16596():

        label("loc_16596")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_16596")

    QueueWorkItem2(0x101, 1, lambda_16596)
    Sleep(50)

    def lambda_165AB():

        label("loc_165AB")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_165AB")

    QueueWorkItem2(0x102, 1, lambda_165AB)
    Sleep(50)

    def lambda_165C0():

        label("loc_165C0")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_165C0")

    QueueWorkItem2(0x103, 1, lambda_165C0)
    Sleep(50)

    def lambda_165D5():

        label("loc_165D5")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_165D5")

    QueueWorkItem2(0x104, 1, lambda_165D5)
    Sleep(50)

    def lambda_165EA():

        label("loc_165EA")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_165EA")

    QueueWorkItem2(0x109, 1, lambda_165EA)
    Sleep(50)

    def lambda_165FF():

        label("loc_165FF")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_165FF")

    QueueWorkItem2(0x105, 1, lambda_165FF)
    Sleep(50)

    def lambda_16614():

        label("loc_16614")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_16614")

    QueueWorkItem2(0x1D, 1, lambda_16614)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)

    def lambda_1662E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1662E)

    def lambda_1663B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1663B)
    OP_6F(0x79)

    def lambda_1664A():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1664A)

    def lambda_16657():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_16657)
    Sleep(500)

    ChrTalk(
        0x26,
        "Ahaha, Aerie㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhuhu, oh dear㈱\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "Baby",
        "*goo goo*.\x02",
    )

    CloseMessageWindow()

    def lambda_166A6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_166A6)

    def lambda_166B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_166B3)
    Sleep(300)

    def lambda_166C3():
        OP_95(0xFE, 4830, 2000, 38020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_166C3)

    def lambda_166DD():
        OP_95(0xFE, 4470, 2000, 39100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_166DD)
    Sleep(1000)
    OP_68(15240, 5000, 43490, 5000)
    MoveCamera(5, 29, 0, 5000)
    OP_6E(600, 5000)
    WaitChrThread(0x26, 1)

    def lambda_16723():
        OP_95(0xFE, 1480, 2000, 40200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_16723)
    Sleep(100)

    def lambda_16740():
        OP_95(0xFE, 1940, 2000, 41000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_16740)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F...They made a huge\x01",
            "impact from beginning\x01",
            "to end, didn't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, indeed. \x01",
            "I didn't expect to be jealous\x01",
            "of them, though.\x02\x03",
            "#00104FIt has been awhile, and I too feel\x01",
            "like I want to visit my parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FMiss Elie...\x02\x03",
            "#10109FUh uh, I know. \x01",
            "I have a lot of\x01",
            "respect for my mother.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Please accept my\x01",
            "thanks as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_168E9():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_168E9)
    Sleep(50)

    def lambda_168F9():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_168F9)
    Sleep(50)

    def lambda_16909():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16909)
    Sleep(50)

    def lambda_16919():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16919)
    Sleep(50)

    def lambda_16929():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16929)
    Sleep(50)

    def lambda_16939():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16939)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "I'll look after Mr. Geval\x01",
            "until he makes it\x01",
            "back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes. Thank you for\x01",
            "your cooperation.\x02\x03",
            "#00000FIt's time for us to be going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Search for Long Lost Father]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x90, 0x1, 0x7)
    OP_29(0x90, 0x1, 0x8)
    OP_29(0x90, 0x4, 0x10)
    SetChrFlags(0x1D, 0x80)
    OP_D7(0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x26, 0xFF)
    OP_4C(0x27, 0xFF)
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x4, 0x1)
    SetChrPos(0x0, 15390, 3500, 43000, 315)
    SetChrPos(0x26, 3170, 0, 14230, 135)
    SetChrPos(0x27, 2120, 0, 13670, 135)
    OP_69(0xFF, 0x0)
    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)
    EventEnd(0x5)
    Return()

    # Function_76_15A19 end

    def Function_77_16B05(): pass

    label("Function_77_16B05")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x14, 0x80)
    OP_78(0xE, 0x14)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_75(0xE, 0x1, 0x0)
    OP_71(0xE, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0xE, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0x15, 0x80)
    OP_78(0xF, 0x15)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0xF, 0x307, 0x307, 0x307)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x10, 0x16)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    OP_75(0x10, 0x1, 0x0)
    OP_FF(0x10, 0x2EE, 0x2EE, 0x2EE)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x14, -46000, 16400, 90000, 260)
    OP_D5(0x14, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x15, -46000, 16400, 90000, 260)
    OP_D5(0x15, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x16, -46000, 0, 90000, 260)
    OP_D5(0x16, 0x0, 0x3F7A0, 0x0, 0x0)

    def lambda_16C3A():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16C3A)

    def lambda_16C54():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_16C54)
    OP_82(0x32, 0x32, 0xBB8, 0x1F40)
    BeginChrThread(0x14, 0, 0, 78)
    OP_68(-26000, 5600, 70000, 0)
    MoveCamera(330, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(80000, 0)
    OP_68(-46000, 6900, 90000, 10000)
    MoveCamera(330, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(70000, 10000)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, -18430, 3500, 62180, 330)
    SetChrPos(0x103, -17200, 3500, 62670, 324)
    SetChrPos(0x105, -18600, 3500, 60920, 324)
    SetChrPos(0x107, -15340, 3500, 61450, 277)
    SetChrSubChip(0x107, 0x5)
    OP_68(-24740, 5600, 71790, 0)
    MoveCamera(324, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24190, 0)
    OP_68(-18990, 5600, 64470, 5000)

    def lambda_16DB2():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16DB2)

    def lambda_16DCC():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_16DCC)
    BeginChrThread(0x14, 0, 0, 80)
    BeginChrThread(0x15, 0, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 90)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x0)
    OP_68(-17780, 5600, 62410, 0)
    MoveCamera(323, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16850, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10406F#6PWe got down here safely, but...\x02\x03",
            "#10408F...Isn't this the\x01",
            "village lotus fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PYeah... It looks very\x01",
            "different, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PThis is probably due to\x01",
            "KeA's awakening too.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-17020, 5600, 61730, 1000)
    TurnDirection(0x103, 0x107, 400)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00201F#5PZeit. Any sign\x01",
            "of Cryptids?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16F64():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16F64)
    Sleep(0)

    def lambda_16F74():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_16F74)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C#NHmm. I don't sense\x01",
            "any for now.\x02\x03",
            "#01200FIt also seems there won't be any problem\x01",
            "about relying on that magic circle.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5PRoger.\x02\x03",
            "#00001FFor now, I think we should\x01",
            "go greet Village Chief Tolta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11PYes.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17100, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    OP_24(0x3B6)
    SetScenarioFlags(0x22, 0)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_77_16B05 end

    def Function_78_170B1(): pass

    label("Function_78_170B1")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0xE, 0x2, 0x7D0)
    OP_75(0x10, 0x2, 0x7D0)
    Sleep(1000)
    OP_79(0xF)
    Return()

    # Function_78_170B1 end

    def Function_79_170F6(): pass

    label("Function_79_170F6")

    OP_75(0xE, 0x1, 0x7D0)
    OP_75(0x10, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_79(0xF)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_79_170F6 end

    def Function_80_17144(): pass

    label("Function_80_17144")

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

    # Function_80_17144 end

    def Function_81_171A9(): pass

    label("Function_81_171A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 19200, 500, 21050, 200)
    SetChrPos(0x103, 19200, 500, 21050, 200)
    SetChrPos(0x105, 19200, 500, 21050, 200)
    SetChrPos(0x107, 19200, 500, 21050, 200)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(19200, 1500, 21050, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(17950, 1000, 16250, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_172AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_172AB)
    BeginChrThread(0x101, 1, 0, 82)
    Sleep(1000)

    def lambda_172C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_172C5)
    BeginChrThread(0x103, 1, 0, 83)
    Sleep(1000)

    def lambda_172DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_172DF)
    BeginChrThread(0x105, 1, 0, 84)
    Sleep(1000)

    def lambda_172F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_172F9)
    BeginChrThread(0x107, 1, 0, 85)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10404F#12POk then──\x02\x03",
            "#10400FAre we going to the\x01",
            "Ancient Battlefield?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. Even though we don't\x01",
            "know who the rebel force is.\x02\x03",
            "#00001FI'd like to cooperate with\x01",
            "them, if at all possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PI agree... I think there is\x01",
            "value in looking for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#11P#3CIn that case, let us head over there.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 17950, 0, 16250, 180)
    SetScenarioFlags(0x1A1, 5)
    OP_29(0xAF, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_81_171A9 end

    def Function_82_174AB(): pass

    label("Function_82_174AB")

    OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x101, 17500, 0, 14850, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_82_174AB end

    def Function_83_174D6(): pass

    label("Function_83_174D6")

    OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x103, 16900, 0, 16550, 2000, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_83_174D6 end

    def Function_84_17501(): pass

    label("Function_84_17501")

    OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x105, 18950, 0, 16100, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_84_17501 end

    def Function_85_1752C(): pass

    label("Function_85_1752C")

    OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x107, 18000, 0, 17750, 2000, 0x0)
    OP_93(0x107, 0xB4, 0x1F4)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_85_1752C end

    def Function_86_1755B(): pass

    label("Function_86_1755B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    Call(0, 87)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1781C")
    Fade(500)
    OP_68(15510, 1350, -23710, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17721")
    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x105, 23130, 0, -30790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x103, 20790, 0, -30560, 315)
    SetChrPos(0x109, 22200, 0, -31420, 315)

    def lambda_17658():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17658)

    def lambda_17672():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17672)

    def lambda_1768C():
        OP_95(0xFE, 16930, 0, -24390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1768C)

    def lambda_176A6():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_176A6)

    def lambda_176C0():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_176C0)

    def lambda_176DA():
        OP_95(0xFE, 15900, 0, -25220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_176DA)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_17817")

    label("loc_17721")

    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x109, 21290, 0, -30060, 315)
    SetChrPos(0x105, 22810, 0, -31000, 315)

    def lambda_1777B():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1777B)

    def lambda_17795():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17795)

    def lambda_177AF():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_177AF)

    def lambda_177C9():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_177C9)

    def lambda_177E3():
        OP_95(0xFE, 16410, 0, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_177E3)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    label("loc_17817")

    Jump("loc_17C8D")

    label("loc_1781C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A71")
    Fade(500)
    OP_68(17090, 1500, -25640, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x8, 0x13)
    OP_49()
    SetChrPos(0x13, 27180, 0, -35450, 315)
    OP_D5(0x13, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_0D()
    OP_49()
    BeginChrThread(0x28, 1, 0, 88)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_178CB():
        OP_95(0xFE, 15110, 0, -21470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_178CB)
    Sleep(3500)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x13, 0x1)
    SetChrPos(0x13, 16500, 0, -18100, 135)
    OP_D5(0x13, 0x0, 0x20F58, 0x0, 0x0)
    OP_71(0x8, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x8)
    SetMapObjFlags(0x8, 0x2)
    OP_66(0x2, 0x1)
    OP_68(12290, 1200, -19990, 0)
    MoveCamera(7, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15300, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A03")
    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x105, 13690, 0, -20980, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x103, 11800, 0, -20300, 315)
    SetChrPos(0x109, 12760, 0, -21810, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_17A62")

    label("loc_17A03")

    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x109, 11800, 0, -20300, 315)
    SetChrPos(0x105, 13220, 0, -21400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17A62")

    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_17C8D")

    label("loc_17A71")

    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapObjFlags(0x7, 0x4)
    OP_68(1610, 1500, -14250, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, 250, 0, -13500, 0)
    SetChrPos(0x102, 1250, 0, -13500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17C24")
    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x105, 2850, 0, -14980, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x103, 960, 0, -14300, 0)
    SetChrPos(0x109, 1920, 0, -15810, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_17C83")

    label("loc_17C24")

    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x109, 960, 0, -14300, 0)
    SetChrPos(0x105, 2380, 0, -15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17C83")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_17C8D")


    ChrTalk(
        0x105,
        (
            "#12P#10302FWow, what a nice scenic place.\x02\x03",
            "#10304FThis is "Armorica Village", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, that's right.\x02\x03",
            "#00104FBeekeeping, agriculture and\x01",
            "livestock are the main industries...\x02\x03",
            "#00102FEven now, a small number of the\x01",
            "legendary "Divine Wolves" remain here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThat's right... This was the place\x01",
            "we conducted our first activity\x01",
            "outside the city, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FThe incident with the mafia's military\x01",
            "dogs... It really takes me back.\x02\x03",
            "#10103FBack then, I remember our\x01",
            "investigation being handed\x01",
            "over to your Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that was also the fault of that\x01",
            "incompetent former Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, and Zeit has been with\x01",
            "us ever since that incident.\x02\x03",
            "#00104FHe came to our aid when we were in grave danger,\x01",
            "and the incident was resolved thanks to him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18062")

    ChrTalk(
        0x101,
        (
            "#00009FZeit has been helping\x01",
            "us out ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYes, and not just in combat.\x01",
            "He supports us in various\x01",
            "situations, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180EE")

    label("loc_18062")


    ChrTalk(
        0x101,
        (
            "#00009FAnd Zeit has been helping\x01",
            "us out ever since.\x02\x03",
            "#00004FNot just in combat, either.\x01",
            "He supports us in various\x01",
            "situations, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180EE")


    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, well, I get the feeling \x01",
            "Zeit isn't just helping out.\x02\x03",
            "#10309FRather, isn't he always stealing\x01",
            "the Support Section's thunder?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18188():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18188)

    def lambda_18195():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18195)

    def lambda_181A2():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_181A2)

    def lambda_181AF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_181AF)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1824C")

    def lambda_1822C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1822C)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1824C")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FDamn, you stabbed where it hurts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well anyway... \x01",
            "We've been growing too and\x01",
            "we'll continue to work on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x14E, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18317")
    SetChrPos(0x0, 15500, 0, -23930, 315)
    Jump("loc_1834C")

    label("loc_18317")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1833B")
    SetChrPos(0x0, 11350, 0, -18420, 315)
    Jump("loc_1834C")

    label("loc_1833B")

    SetChrPos(0x0, 890, 0, -13080, 315)

    label("loc_1834C")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18370")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_18370")

    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_86_1755B end

    def Function_87_1837C(): pass

    label("Function_87_1837C")

    OP_68(-37350, 1500, 69780, 0)
    MoveCamera(338, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(53190, 0)
    OP_68(-21000, 1500, 74410, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(7400, 1500, 48380, 0)
    MoveCamera(323, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37470, 0)
    OP_68(-12130, 1500, 35080, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(-1020, 5100, 4110, 0)
    MoveCamera(338, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44250, 0)
    PlaceName2(340, 40, "c_plac14", 0x0, 3000)
    OP_68(-1020, 2800, 4110, 7000)
    OP_6F(0x1)
    Return()

    # Function_87_1837C end

    def Function_88_1845D(): pass

    label("Function_88_1845D")

    Sleep(500)
    Sound(459, 0, 100, 0)
    Sleep(1200)
    Sleep(1500)
    Sound(492, 0, 90, 0)
    Return()

    # Function_88_1845D end

    def Function_89_18473(): pass

    label("Function_89_18473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187BE")
    EventBegin(0x0)
    Fade(1000)
    OP_68(16470, 1500, -26270, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x13, 12610, 0, -12660, 0)
    SetChrPos(0x101, 16690, 0, -26040, 135)
    SetChrPos(0x103, 17490, 0, -25240, 135)
    SetChrPos(0x105, 15690, 0, -25040, 135)
    SetChrPos(0x107, 16490, 0, -24240, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_18561():
        OP_93(0x107, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_18561)
    Sleep(0)

    def lambda_18571():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18571)
    Sleep(0)

    def lambda_18581():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18581)
    Sleep(0)

    def lambda_18591():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18591)
    Sleep(0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(12070, 1100, -16020, 0)
    MoveCamera(359, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 12450, 0, -17250, 0)
    SetChrPos(0x103, 11450, 0, -17250, 0)
    SetChrPos(0x105, 12950, 0, -18450, 0)
    SetChrPos(0x107, 10950, 0, -18450, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThis orbal car...\x01",
            "It's Mr. Harold's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt is a Verne Corp. model...\x01",
            "We have ridden in it before,\x01",
            "if I am not mistaken.\x02\x03",
            "#00203FThe Village Chief said he is\x01",
            "staying on the 2nd floor at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FRight now, we need information.\x02\x03",
            "#10400FIt's best if we ask around before\x01",
            "heading out on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's try it.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11950, 0, -17850, 0)
    EventEnd(0x5)
    Jump("loc_1883D")

    label("loc_187BE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like Mr. Harold\x01",
            "is staying here.\x02\x03",
            "Before heading out,\x01",
            "let's visit him at the inn.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)

    label("loc_1883D")

    Return()

    # Function_89_18473 end

    SaveToFile()

Try(main)
