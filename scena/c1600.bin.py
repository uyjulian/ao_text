from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1600.bin",                # FileName
        "c1600",                    # MapName
        "c1600",                    # Location
        0x00B2,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 178, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1600",                  # 0
        "Joey",               # 1
        "Suzuku",                 # 2
        "Yona",                   # 3
        "Roberts boss",           # 4
        "Mayor of Dieter",         # 5
        "Kibun Sigmund",         # 6
        "Charlie",             # 7
        "Wald",               # 8
        "Keya",                 # 9
        "Marybele",             # 10
        "Ariane Road",         # 11
        "Dr. Novartis",       # 12
        "Clown Campanella",     # 13
        "Sergey Manager",           # 14
        "Airborne",                 # 15
        "Airborne",                 # 16
        "Airborne shadow",               # 17
        "Airborne shadow",               # 18
        "Imperial terrorist",       # 19
        "Imperial terrorist",       # 20
        "Imperial terrorist",       # 21
        "Imperial terrorist",       # 22
        "Imperial terrorist",       # 23
        "Imperial terrorist",       # 24
        "Imperial terrorist",       # 25
        "Republic-based terrorists",     # 26
        "Republic-based terrorists",     # 27
        "Republic-based terrorists",     # 28
        "Republic-based terrorists",     # 29
        "Republic-based terrorists",     # 30
        "Republic-based terrorists",     # 31
        "Republic-based terrorists",     # 32
        "Iron",             # 33
        "Iron",             # 34
        "Iron",             # 35
        "Mercapa",               # 36
        "Image",                   # 37
        "Image",                   # 38
        "Image",                   # 39
        "Image",                   # 40
        "Image",                   # 41
        "Image",                   # 42
        "SE control",                 # 43
        "bc1600",                 # 44
    ))

    ATBonus("ATBonus_6D4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_794", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_778", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_77C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_780", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_784", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_788", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_78C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_790", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7B4", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bc1600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_794", "MonsterBattlePostion_774", "ed7554", "ed7554", "ATBonus_6D4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch27600.itc",                   # 02
        "apl/ch51731.itc",                   # 03
        "chr/ch05410.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
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

    DeclNpc(4294967177, 0,       22069,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(8680,    0,       4294950817, 135,  389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32200,   4294962896, 4294939446, 75,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28399,   4294962896, 4294939546, 45,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 34,  22.0,                  -23.0,                 -5.400000095367432,    625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.363961219787598,    0.07070967555046082,   1.0800000429153442,    1.0])
    DeclEvent(0x0000, 0, 62,  0.0,                   -22.0,                 -1.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  4.400000095367432,     0.20000000298023224,   1.0])

    DeclActor(0,       0,       0,       1500,    0,       1500,    0,       0x007C, 0,  93, 0x0000)

    ChipFrameInfo(2420, 0)                                       # 0

    ScpFunction((
        "Function_0_974",          # 00, 0
        "Function_1_A24",          # 01, 1
        "Function_2_B80",          # 02, 2
        "Function_3_D5F",          # 03, 3
        "Function_4_1334",         # 04, 4
        "Function_5_1597",         # 05, 5
        "Function_6_16E2",         # 06, 6
        "Function_7_1960",         # 07, 7
        "Function_8_2075",         # 08, 8
        "Function_9_23BF",         # 09, 9
        "Function_10_2FD3",        # 0A, 10
        "Function_11_3028",        # 0B, 11
        "Function_12_307D",        # 0C, 12
        "Function_13_30D2",        # 0D, 13
        "Function_14_3142",        # 0E, 14
        "Function_15_3197",        # 0F, 15
        "Function_16_31EC",        # 10, 16
        "Function_17_321C",        # 11, 17
        "Function_18_3284",        # 12, 18
        "Function_19_32C1",        # 13, 19
        "Function_20_3305",        # 14, 20
        "Function_21_3349",        # 15, 21
        "Function_22_338D",        # 16, 22
        "Function_23_33D1",        # 17, 23
        "Function_24_3415",        # 18, 24
        "Function_25_3459",        # 19, 25
        "Function_26_349D",        # 1A, 26
        "Function_27_3A24",        # 1B, 27
        "Function_28_3A84",        # 1C, 28
        "Function_29_3AE4",        # 1D, 29
        "Function_30_3C07",        # 1E, 30
        "Function_31_3D13",        # 1F, 31
        "Function_32_3DE2",        # 20, 32
        "Function_33_3EB1",        # 21, 33
        "Function_34_429F",        # 22, 34
        "Function_35_59C8",        # 23, 35
        "Function_36_5AC0",        # 24, 36
        "Function_37_5ADF",        # 25, 37
        "Function_38_5AFE",        # 26, 38
        "Function_39_5B5D",        # 27, 39
        "Function_40_5B7C",        # 28, 40
        "Function_41_5BC4",        # 29, 41
        "Function_42_5C11",        # 2A, 42
        "Function_43_70D9",        # 2B, 43
        "Function_44_73F6",        # 2C, 44
        "Function_45_74AA",        # 2D, 45
        "Function_46_74FA",        # 2E, 46
        "Function_47_7550",        # 2F, 47
        "Function_48_760A",        # 30, 48
        "Function_49_76B3",        # 31, 49
        "Function_50_779E",        # 32, 50
        "Function_51_77DE",        # 33, 51
        "Function_52_7861",        # 34, 52
        "Function_53_80CC",        # 35, 53
        "Function_54_8859",        # 36, 54
        "Function_55_8970",        # 37, 55
        "Function_56_91CA",        # 38, 56
        "Function_57_933E",        # 39, 57
        "Function_58_937D",        # 3A, 58
        "Function_59_9815",        # 3B, 59
        "Function_60_9844",        # 3C, 60
        "Function_61_98E1",        # 3D, 61
        "Function_62_98F8",        # 3E, 62
        "Function_63_C2C9",        # 3F, 63
        "Function_64_C2F7",        # 40, 64
        "Function_65_C358",        # 41, 65
        "Function_66_C3B9",        # 42, 66
        "Function_67_C3DE",        # 43, 67
        "Function_68_CEBE",        # 44, 68
        "Function_69_CED1",        # 45, 69
        "Function_70_CF06",        # 46, 70
        "Function_71_11240",       # 47, 71
        "Function_72_11265",       # 48, 72
        "Function_73_112CC",       # 49, 73
        "Function_74_11333",       # 4A, 74
        "Function_75_1139A",       # 4B, 75
        "Function_76_11401",       # 4C, 76
        "Function_77_11468",       # 4D, 77
        "Function_78_114AA",       # 4E, 78
        "Function_79_114CC",       # 4F, 79
        "Function_80_114E8",       # 50, 80
        "Function_81_11504",       # 51, 81
        "Function_82_11520",       # 52, 82
        "Function_83_1153C",       # 53, 83
        "Function_84_11558",       # 54, 84
        "Function_85_1157C",       # 55, 85
        "Function_86_11587",       # 56, 86
        "Function_87_11592",       # 57, 87
        "Function_88_1159D",       # 58, 88
        "Function_89_115A8",       # 59, 89
        "Function_90_115B3",       # 5A, 90
        "Function_91_115BE",       # 5B, 91
        "Function_92_11639",       # 5C, 92
        "Function_93_11651",       # 5D, 93
        "Function_94_116B2",       # 5E, 94
    ))


    def Function_0_974(): pass

    label("Function_0_974")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9AC"),
        (1, "loc_9B8"),
        (2, "loc_9C4"),
        (3, "loc_9D0"),
        (4, "loc_9DC"),
        (5, "loc_9E8"),
        (6, "loc_9F4"),
        (SWITCH_DEFAULT, "loc_A00"),
    )


    label("loc_9AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A00")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A23")

    Return()

    # Function_0_974 end

    def Function_1_A24(): pass

    label("Function_1_A24")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AB7")
    ClearMapObjFlags(0x6, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_AC6")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_AE1")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_AF0")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_B0B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_B70")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_B7F")
    ClearMapObjFlags(0x16, 0x2000000)

    label("loc_B7F")

    Return()

    # Function_1_A24 end

    def Function_2_B80(): pass

    label("Function_2_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "President Dieter")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_BDD")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_C43")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C11")
    Jump("loc_C43")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C29")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_C43")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C43")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_93(0x8, 0x13B, 0x0)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C57")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_D48")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C6B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 9)
    Jump("loc_D48")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C7F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_D48")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_C96")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 5)
    Event(0, 42)
    Jump("loc_D48")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_CAA")
    ClearScenarioFlags(0x22, 4)
    Event(0, 52)
    Jump("loc_D48")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_CBE")
    ClearScenarioFlags(0x22, 5)
    Event(0, 53)
    Jump("loc_D48")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_CD2")
    ClearScenarioFlags(0x22, 6)
    Event(0, 54)
    Jump("loc_D48")

    label("loc_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_CE6")
    ClearScenarioFlags(0x22, 7)
    Event(0, 55)
    Jump("loc_D48")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_CFA")
    ClearScenarioFlags(0x23, 0)
    Event(0, 56)
    Jump("loc_D48")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_D0E")
    ClearScenarioFlags(0x23, 1)
    Event(0, 58)
    Jump("loc_D48")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_D22")
    ClearScenarioFlags(0x23, 2)
    Event(0, 67)
    Jump("loc_D48")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_D39")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 70)
    Jump("loc_D48")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_D48")
    ClearScenarioFlags(0x23, 4)
    Event(0, 94)

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5E")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_D5E")

    Return()

    # Function_2_B80 end

    def Function_3_D5F(): pass

    label("Function_3_D5F")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x4B0)
    OP_F3(100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9C")
    SetMapObjFrame(0xFF, "CS00", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CS01", 0x1, 0x2)
    Jump("loc_DA8")

    label("loc_D9C")

    SetMapObjFrame(0xFF, "CS02", 0x1, 0x2)

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DBF")
    Sound(132, 1, 50, 0)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_DDE")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD8")
    Sound(132, 1, 50, 0)
    Jump("loc_DDE")

    label("loc_DD8")

    Sound(132, 1, 100, 0)

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_E26")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E14")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E26")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E26")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E26")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E3E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E56")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB8")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x0, 0x1)

    label("loc_EB8")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1012")
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    Jump("loc_1136")

    label("loc_1012")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1159")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x20)
    OP_70(0x8, 0x2)
    Jump("loc_115F")

    label("loc_1159")

    SetMapObjFlags(0x8, 0x4)

    label("loc_115F")

    SetMapObjFrame(0xFF, "last", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1235")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x42E)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CF")
    LoadEffect(0x9, "map/mprain01.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1333")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_1333")

    Return()

    # Function_3_D5F end

    def Function_4_1334(): pass

    label("Function_4_1334")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1345")
    Jump("loc_1593")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1469")

    ChrTalk(
        0xFE,
        (
            "Fuu … after all\x01",
            "I can crowd this place many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today I decided to read a book here\x01",
            "I thought, but with this scenery alone\x01",
            "My heart is full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not mind, this book,\x01",
            "You guys call me.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝10卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝10卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 1)
    Jump("loc_14EC")

    label("loc_1469")


    ChrTalk(
        0xFE,
        (
            "Fuu … after all\x01",
            "I can crowd this place many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking at the scenery here,\x01",
            "The fear of that raid incident is also\x01",
            "I feel like calming down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EC")

    Jump("loc_1593")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0xFE,
        (
            "I can not see it at all from here,\x01",
            "Now in the direction of the guard the guard\x01",
            "You are fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even with such a beautiful scenery ……\x01",
            "It is truly a sad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    TalkEnd(0xFE)
    Return()

    # Function_4_1334 end

    def Function_5_1597(): pass

    label("Function_5_1597")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_164D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B9")
    TalkEnd(0xFE)
    Call(0, 7)
    Return()

    label("loc_15B9")


    ChrTalk(
        0x9,
        (
            "#11223F…… If you guys,\x01",
            "I think that it will be okay.\x02\x03",
            "#11222FPlease, Kea-chan ……\x01",
            "My precious friends,\x01",
            "Thank you……!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DE")

    label("loc_164D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1668")
    Call(0, 6)
    Jump("loc_16DE")

    label("loc_1668")


    ChrTalk(
        0x9,
        (
            "#11228FEveryone, please have a father ……\x01",
            "Kea-chan\x01",
            "Thank you.\x02\x03",
            "#11223FI will be waiting here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    TalkEnd(0xFE)
    Return()

    # Function_5_1597 end

    def Function_6_16E2(): pass

    label("Function_6_16E2")

    OP_93(0x9, 0x87, 0x0)

    ChrTalk(
        0x9,
        "#11221FDad, Kea-chan ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FShizuoka … ….\x01",
            "Were you in such a place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#11220FEveryone……\x01",
            "Yes, that \"Taiki\"\x01",
            "I was watching.\x02\x03",
            "#11230FDad and Ka'aa,\x01",
            "Really in such a place …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F…… Yes, there is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWhere is \"Taiki\" is\x01",
            "I do not know yet ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11223FIs that so………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Shizuku-chan, please wait.\x02\x03",
            "#00001FArios and Kia,\x01",
            "Absolutely we will take it back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FOh, so do not worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11223F……Yes.\x02\x03",
            "#11221FEveryone, please have a father ……\x01",
            "Kea-chan\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x0)
    SetScenarioFlags(0x1AF, 2)
    Return()

    # Function_6_16E2 end

    def Function_7_1960(): pass

    label("Function_7_1960")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(7690, 1100, -15570, 0)
    MoveCamera(110, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 7530, 0, -15000, 135)
    SetChrPos(0x1, 9360, 0, -14520, 180)
    SetChrPos(0x2, 6860, 0, -16500, 90)
    SetChrPos(0x3, 8570, 0, -13930, 180)
    SetChrPos(0x4, 5900, 0, -15300, 110)
    SetChrPos(0x5, 7050, 0, -13540, 155)
    OP_93(0x9, 0x13B, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's,\x01",
            "To beat Arios … …\x02\x03",
            "And the real criminal of killing Guy\x01",
            "What was not Arios\x01",
            "I explained to Shizuku.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11225F……Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F……Ah.\x02\x03",
            "#00000FArios also, surely later\x01",
            "To Suzuku-chan ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11233F… …. Guru ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11234FUgh … … it was good …\x02\x03",
            "#11233FMy father has important friends ……\x01",
            "Lloyd's older brother\x01",
            "I did not mean to put it on my hand … …\x02\x03",
            "#11234FIf really it was,\x01",
            "Dad, absolutely backtracking\x01",
            "I can not do it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FShizuoka … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00002FHa … … I told you?\x01",
            "I can not turn back,\x01",
            "There is not such a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D63")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F… Wait a while.\x01",
            "McRae afterwards surely\x01",
            "I promise to bring you back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1D63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(
        0x109,
        (
            "#6P#10102FPlease wait.\x01",
            "Mr. Arios surely later\x01",
            "Because I will bring them back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E12")

    ChrTalk(
        0x105,
        (
            "#6P#10402FMr. Arios\x01",
            "I will definitely take back later.\x01",
            "Huh, I promise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E12")


    ChrTalk(
        0x9,
        "#11222FRubbing … … Yes! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F…… After this,\x01",
            "Just to get back Ka'aa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FOh, Shizuku-chan\x01",
            "To make you smile!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0x105,
        (
            "#6P#10409FHuff, when it comes\x01",
            "I have to accomplish anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F54")

    ChrTalk(
        0x109,
        (
            "#6P#10109FWhen it comes to this,\x01",
            "Let's do anything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FAC")

    ChrTalk(
        0x106,
        (
            "#6P#10709FWhen it comes to this,\x01",
            "I have to accomplish anything\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAC")


    ChrTalk(
        0x9,
        (
            "#11223F… … If everyone who won the father,\x01",
            "I think that it will be okay.\x02\x03",
            "#11227FPlease, Kea-chan ……\x01",
            "My precious friends,\x01",
            "Thank you……!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x87, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x1AF, 1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_7_1960 end

    def Function_8_2075(): pass

    label("Function_8_2075")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(23800, -43600, 6100, 0)
    MoveCamera(305, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 23800, -44600, 6100, 90)
    SetChrPos(0x102, 23800, -44600, 7200, 90)
    SetChrPos(0x109, 23000, -44600, 7000, 90)
    SetChrPos(0x103, 23000, -44600, 5900, 90)
    SetChrPos(0x104, 22200, -44600, 5700, 90)
    SetChrPos(0x105, 23600, -44600, 5100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 20800, -44600, 7500, 90)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    MoveCamera(305, 23, 0, 6000)
    OP_6E(1100, 6000)
    SetCameraDistance(82000, 6000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, -53600, -25000, 0)
    MoveCamera(315, -15, 15, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0xC, 0x8)
    OP_68(0, -73600, -75000, 11000)
    MoveCamera(215, 30, 15, 11000)
    SetCameraDistance(180000, 11000)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2075 end

    def Function_9_23BF(): pass

    label("Function_9_23BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("apl/ch51259.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -19000, -6000, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0xC, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x109,
        "#11P#10109FWow …!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x105,
        (
            "#11P#10302Fthis is……\x01",
            "It is truly superb.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_68(0, 0, 0, 9000)
    MoveCamera(225, 13, 0, 9000)
    OP_6E(900, 9000)
    SetCameraDistance(130000, 9000)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(900)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 17)
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -19700, -4400, -20300, 180)
    SetChrPos(0x102, -20300, -4400, -19700, 180)
    SetChrPos(0x103, -20000, -4400, -20000, 180)
    SetChrPos(0x104, -19700, -4400, -20300, 180)
    SetChrPos(0x109, -20300, -4400, -19700, 180)
    SetChrPos(0x105, -20000, -4400, -20000, 180)
    SetChrPos(0xC, -20000, -4400, -20000, 180)
    BeginChrThread(0x101, 0, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(-29000, -3900, -29000, 0)
    MoveCamera(225, 17, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24400, -3900, -38800, 6000)
    MoveCamera(205, 19, 0, 6000)
    SetCameraDistance(23500, 6000)
    OP_6F(0x79)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#11Pmy mother……\x01",
            "I do not even have words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PYeah, well … …\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x103,
        (
            "#00202F#11P…… the city is like a doll\x01",
            "model#4RMiniature#It looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PNo, ~ at night\x01",
            "I guess it's a scenery!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-28800, -3300, -31300, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#12P#02809FHaha, this place is\x01",
            "To the citizens as observatory\x01",
            "I am planning to open it.\x02\x03",
            "#02800FOnly government officials monopolize\x01",
            "It's too good for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28EF():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28EF)
    Sleep(50)

    def lambda_28FF():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28FF)
    Sleep(50)

    def lambda_290F():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_290F)
    Sleep(50)

    def lambda_291F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_291F)
    Sleep(50)

    def lambda_292F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_292F)
    Sleep(50)

    def lambda_293F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_293F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_2964():

        label("loc_2964")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2964")

    QueueWorkItem2(0x101, 2, lambda_2964)

    def lambda_2976():

        label("loc_2976")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2976")

    QueueWorkItem2(0x102, 2, lambda_2976)

    def lambda_2988():

        label("loc_2988")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2988")

    QueueWorkItem2(0x103, 2, lambda_2988)

    def lambda_299A():

        label("loc_299A")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_299A")

    QueueWorkItem2(0x109, 2, lambda_299A)

    def lambda_29AC():

        label("loc_29AC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29AC")

    QueueWorkItem2(0x105, 2, lambda_29AC)

    def lambda_29BE():

        label("loc_29BE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29BE")

    QueueWorkItem2(0x104, 2, lambda_29BE)

    ChrTalk(
        0x101,
        "#00002F#5POh, that is nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PHuhu, Ka'aa also\x01",
            "I want to bring you here.\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#12P#02805FOops, rude.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    OP_0D()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11P#02801FOh, it's me.\x02\x03",
            "#02803FI see, I understand.\x01",
            "Let's head right there.\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#12P#02800FApparently the leaders\x01",
            "It seems that you have arrived at the tower.\x02\x03",
            "I am sorry but\x01",
            "I will be rude with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PIs that so……\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PWell, it was really fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#5PI had a good experience!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02804FHaha, this is it.\x01",
            "I had a nice change of mind.\x02\x03",
            "#02800FWell then, see you later.\x01",
            "Please guard the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PWell, the recommended amount is\x01",
            "May I do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P── Goddess#4REidos#Protect yourself.\x01",
            "I am praying for the meeting's success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P#02809FHaha, I am also praying.\x02",
    )

    CloseMessageWindow()
    OP_92(0xC, 0xFFFFADF8, 0xFFFFADF8, 0x1F4)
    OP_68(-25800, -3300, -28300, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_2DB9():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DB9)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0xC, 0x80)
    Fade(500)
    OP_68(-28350, -3300, -32000, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#5PWell, we also\x01",
            "Will you go to Mr. Dudley?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E6F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E6F)
    Sleep(50)

    def lambda_2E7F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E7F)
    Sleep(50)

    def lambda_2E8F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E8F)
    Sleep(50)

    def lambda_2E9F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E9F)
    Sleep(50)

    def lambda_2EAF():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EAF)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00202FCertainly 34F\x01",
            "It was a security office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FBut this way\x01",
            "I do not need to get anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FWell, really, ….\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    StopSound(132, 1000, 100)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_23BF end

    def Function_10_2FD3(): pass

    label("Function_10_2FD3")


    def lambda_2FD8():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FD8)

    def lambda_2FF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FF2)
    WaitChrThread(0xFE, 1)

    def lambda_3007():
        OP_95(0xFE, -23500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3007)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_2FD3 end

    def Function_11_3028(): pass

    label("Function_11_3028")


    def lambda_302D():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_302D)

    def lambda_3047():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3047)
    WaitChrThread(0xFE, 1)

    def lambda_305C():
        OP_95(0xFE, -23500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_305C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_11_3028 end

    def Function_12_307D(): pass

    label("Function_12_307D")


    def lambda_3082():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3082)

    def lambda_309C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_309C)
    WaitChrThread(0xFE, 1)

    def lambda_30B1():
        OP_95(0xFE, -21500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30B1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_12_307D end

    def Function_13_30D2(): pass

    label("Function_13_30D2")


    def lambda_30D7():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30D7)

    def lambda_30F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30F1)
    WaitChrThread(0xFE, 1)

    def lambda_3106():
        OP_95(0xFE, -21500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3106)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_13_30D2 end

    def Function_14_3142(): pass

    label("Function_14_3142")


    def lambda_3147():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3147)

    def lambda_3161():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3161)
    WaitChrThread(0xFE, 1)

    def lambda_3176():
        OP_95(0xFE, -22500, -6000, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3176)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_14_3142 end

    def Function_15_3197(): pass

    label("Function_15_3197")


    def lambda_319C():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_319C)

    def lambda_31B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31B6)
    WaitChrThread(0xFE, 1)

    def lambda_31CB():
        OP_95(0xFE, -22500, -6000, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31CB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_3197 end

    def Function_16_31EC(): pass

    label("Function_16_31EC")


    def lambda_31F1():
        OP_95(0xFE, -25000, -6000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31F1)

    def lambda_320B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_320B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_31EC end

    def Function_17_321C(): pass

    label("Function_17_321C")

    OP_92(0xFE, 0xFFFF9FE8, 0xFFFFD8F0, 0x1F4)

    def lambda_322E():
        OP_95(0xFE, -24600, -6000, -10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322E)
    WaitChrThread(0xFE, 1)

    def lambda_324C():
        OP_95(0xFE, -21000, -4400, -18600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_324C)
    WaitChrThread(0xFE, 1)

    def lambda_326A():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_326A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_321C end

    def Function_18_3284(): pass

    label("Function_18_3284")

    BeginChrThread(0xC, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 21)
    Return()

    # Function_18_3284 end

    def Function_19_32C1(): pass

    label("Function_19_32C1")


    def lambda_32C6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C6)
    WaitChrThread(0xFE, 1)

    def lambda_32E4():
        OP_95(0xFE, -28000, -4400, -32600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32E4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_19_32C1 end

    def Function_20_3305(): pass

    label("Function_20_3305")


    def lambda_330A():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_330A)
    WaitChrThread(0xFE, 1)

    def lambda_3328():
        OP_95(0xFE, -29800, -4400, -32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_20_3305 end

    def Function_21_3349(): pass

    label("Function_21_3349")


    def lambda_334E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_334E)
    WaitChrThread(0xFE, 1)

    def lambda_336C():
        OP_95(0xFE, -28700, -4400, -31400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_336C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_21_3349 end

    def Function_22_338D(): pass

    label("Function_22_338D")


    def lambda_3392():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3392)
    WaitChrThread(0xFE, 1)

    def lambda_33B0():
        OP_95(0xFE, -26400, -4400, -31800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_22_338D end

    def Function_23_33D1(): pass

    label("Function_23_33D1")


    def lambda_33D6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33D6)
    WaitChrThread(0xFE, 1)

    def lambda_33F4():
        OP_95(0xFE, -30700, -4400, -31900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xBE, 0x1F4)
    Return()

    # Function_23_33D1 end

    def Function_24_3415(): pass

    label("Function_24_3415")


    def lambda_341A():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_341A)
    WaitChrThread(0xFE, 1)

    def lambda_3438():
        OP_95(0xFE, -27100, -4400, -30600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3438)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_24_3415 end

    def Function_25_3459(): pass

    label("Function_25_3459")


    def lambda_345E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_345E)
    WaitChrThread(0xFE, 1)

    def lambda_347C():
        OP_95(0xFE, -29400, -4400, -28800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_347C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_25_3459 end

    def Function_26_349D(): pass

    label("Function_26_349D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    LoadChrToIndex("chr/ch42250.itc", 0x1E)
    LoadChrToIndex("chr/ch42251.itc", 0x1F)
    LoadChrToIndex("chr/ch42350.itc", 0x20)
    LoadChrToIndex("chr/ch42351.itc", 0x21)
    LoadChrToIndex("chr/ch42550.itc", 0x22)
    LoadChrToIndex("chr/ch42551.itc", 0x23)
    SoundLoad(497)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -10600, 3300, -3000, 270)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -10600, 3300, -3000, 270)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -10600, 3300, -3000, 270)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -10600, 3300, -3000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10600, 3300, -3000, 270)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -10600, 3300, -3000, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -10600, 3300, -3000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x7, 0x16)
    OP_49()
    SetChrPos(0x16, 11000, 60000, 0, 170)
    OP_D5(0x16, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x3D)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x6, 0x17)
    OP_49()
    SetChrPos(0x17, -11000, 62000, 0, 190)
    OP_D5(0x17, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x3D)
    OP_71(0x6, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xC, 0x18)
    OP_78(0xB, 0x19)
    OP_49()
    SetChrPos(0x18, 10000, 100, 0, 170)
    OP_D5(0x18, 0x0, 0x29810, 0x0, 0x0)
    SetChrPos(0x19, -10000, 100, 0, 190)
    OP_D5(0x19, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 28000, 0, 0)
    MoveCamera(165, -35, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(190000, 0)

    def lambda_382F():
        OP_96(0xFE, 0x2AF8, 0x9C40, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_382F)

    def lambda_3849():
        OP_96(0xFE, 0xFFFFD508, 0xA410, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3849)
    Sound(497, 2, 100, 0)
    MoveCamera(15, -35, 0, 9000)
    SetCameraDistance(110000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x17, 0xFF)
    SetChrPos(0x17, -10000, 22000, 0, 190)
    SetChrPos(0x16, 10000, 20000, 0, 170)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(0, 9000, 0, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 2000, 0, 5000)
    MoveCamera(35, 17, 0, 5000)
    SetCameraDistance(35000, 5000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    WaitChrThread(0x16, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    WaitChrThread(0x17, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    StopSound(497, 1000, 100)
    Sleep(300)
    Sound(105, 0, 100, 0)
    OP_71(0x6, 0x12D, 0x168, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 27)
    Sleep(1500)
    BeginChrThread(0x16, 3, 0, 28)
    Sleep(2500)
    Fade(500)
    OP_68(0, -1500, 0, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_0D()
    OP_68(0, -5000, 0, 10000)
    MoveCamera(90, 3, 0, 10000)
    SetCameraDistance(39000, 10000)
    Sleep(7000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    SetScenarioFlags(0x22, 6)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_349D end

    def Function_27_3A24(): pass

    label("Function_27_3A24")

    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x21, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x23, 0x80)
    BeginChrThread(0x23, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x24, 0x80)
    BeginChrThread(0x24, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x25, 0x80)
    BeginChrThread(0x25, 3, 0, 29)
    Sleep(4000)
    ClearChrFlags(0x26, 0x80)
    BeginChrThread(0x26, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 29)
    Return()

    # Function_27_3A24 end

    def Function_28_3A84(): pass

    label("Function_28_3A84")

    ClearChrFlags(0x1A, 0x80)
    BeginChrThread(0x1A, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1B, 0x80)
    BeginChrThread(0x1B, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    BeginChrThread(0x1D, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1E, 0x80)
    BeginChrThread(0x1E, 3, 0, 30)
    Sleep(2500)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x1F, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x20, 0x80)
    BeginChrThread(0x20, 3, 0, 30)
    Return()

    # Function_28_3A84 end

    def Function_29_3AE4(): pass

    label("Function_29_3AE4")


    def lambda_3AE9():
        OP_95(0xFE, -12600, 3300, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AE9)

    def lambda_3B03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B03)
    WaitChrThread(0xFE, 1)

    def lambda_3B18():
        OP_95(0xFE, -12000, 3300, -4800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B18)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 30, 0)

    def lambda_3B47():
        OP_9D(0xFE, 0xFFFFD440, 0x0, 0xFFFFDA80, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B47)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B79():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B79)
    WaitChrThread(0xFE, 1)

    def lambda_3B97():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B97)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3BBA():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BBA)
    WaitChrThread(0xFE, 1)

    def lambda_3BD9():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BD9)
    Sleep(500)

    def lambda_3BF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BF6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_3AE4 end

    def Function_30_3C07(): pass

    label("Function_30_3C07")


    def lambda_3C0C():
        OP_95(0xFE, 8400, 4000, 4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C0C)
    WaitChrThread(0xFE, 1)

    def lambda_3C2A():
        OP_95(0xFE, 6800, 4000, -1300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C2A)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C53():
        OP_9D(0xFE, 0x11F8, 0x0, 0xFFFFE890, 0xBE, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C53)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C85():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C85)
    WaitChrThread(0xFE, 1)

    def lambda_3CA3():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA3)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3CC6():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC6)
    WaitChrThread(0xFE, 1)

    def lambda_3CE5():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CE5)
    Sleep(500)

    def lambda_3D02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D02)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_3C07 end

    def Function_31_3D13(): pass

    label("Function_31_3D13")


    def lambda_3D18():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D18)

    def lambda_3D31():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3D31)

    def lambda_3D4A():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D4A)
    Sleep(2800)

    def lambda_3D67():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D67)
    Sleep(300)

    def lambda_3D84():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D84)
    Sleep(300)

    def lambda_3DA1():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA1)
    Sleep(300)

    def lambda_3DBE():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DBE)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x7, 0x20)
    OP_74(0x7, 0x0)
    Return()

    # Function_31_3D13 end

    def Function_32_3DE2(): pass

    label("Function_32_3DE2")


    def lambda_3DE7():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DE7)

    def lambda_3E00():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3E00)

    def lambda_3E19():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E19)
    Sleep(2500)

    def lambda_3E36():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E36)
    Sleep(300)

    def lambda_3E53():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E53)
    Sleep(300)

    def lambda_3E70():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E70)
    Sleep(300)

    def lambda_3E8D():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E8D)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x6, 0x20)
    OP_74(0x6, 0x0)
    Return()

    # Function_32_3DE2 end

    def Function_33_3EB1(): pass

    label("Function_33_3EB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#00105FOh……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_68(-25000, -4500, 0, 2500)
    MoveCamera(335, 17, 0, 2500)
    SetCameraDistance(14500, 2500)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10102FA bit of rain\x01",
            "You seem to have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh … and even so\x01",
            "As usual the landscape is Suge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FOh, it's a sunny day\x01",
            "I guess it is even a superb view … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#11P#00005FJonah and the boss\x01",
            "Where is he?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41B0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41B0)
    Sleep(50)

    def lambda_41C0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41C0)
    Sleep(50)

    def lambda_41D0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41D0)
    Sleep(50)

    def lambda_41E0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41E0)
    Sleep(50)

    def lambda_41F0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41F0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00204FProbably, on a corner of the roof\x01",
            "I wonder if there is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FLet's search for it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22000, -6000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_3EB1 end

    def Function_34_429F(): pass

    label("Function_34_429F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadChrToIndex("apl/ch51405.itc", 0x20)
    LoadChrToIndex("chr/ch29300.itc", 0x21)
    SoundLoad(2280)
    SoundLoad(2683)
    SoundLoad(2281)
    SoundLoad(943)
    SoundLoad(938)
    SoundLoad(852)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    LoadEffect(0x2, "event/ev14010.eff")
    LoadEffect(0x3, "event/ev14026.eff")
    LoadEffect(0x4, "event/ev14027.eff")
    LoadEffect(0x5, "event/ev14028.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis328.itp")
    CreatePortrait(1, 308, 154, 340, 186, 0, 0, 32, 36, 0, 0, 32, 32, 0xFFFFFF, 0x0, "c_vis329.itp")
    SetChrPos(0x101, 22400, -4400, -22300, 135)
    SetChrPos(0x103, 21700, -4400, -23000, 135)
    SetChrPos(0x102, 20700, -4400, -22300, 135)
    SetChrPos(0x104, 21700, -4400, -21300, 135)
    SetChrPos(0x109, 19700, -4400, -21900, 135)
    SetChrPos(0x105, 20700, -4400, -20900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 28400, -4400, -27750, 45)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    BeginChrThread(0xA, 2, 0, 36)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    OP_68(21700, -3200, -22650, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1200)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_44F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_44F5)

    NpcTalk(
        0xB,
        "Voice of Roberts Director",
        "Hey, I was waiting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x32, 1, 0, 41)
    OP_68(29300, -3200, -26900, 2000)
    MoveCamera(15, 17, 0, 2000)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(27740, -3200, -26940, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0xA, 32200, -4400, -27850, 75)

    def lambda_4614():
        OP_97(0x101, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4614)
    Sleep(100)

    def lambda_4631():
        OP_97(0x103, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4631)
    Sleep(100)

    def lambda_464E():
        OP_97(0x104, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_464E)
    Sleep(100)

    def lambda_466B():
        OP_97(0x102, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_466B)
    Sleep(100)

    def lambda_4688():
        OP_97(0x105, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4688)
    Sleep(100)

    def lambda_46A5():
        OP_97(0x109, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46A5)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#5PThis generates an alert signal\x01",
            "Is it a device for sensing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12POh, but this way\x01",
            "Only within the radius 10 serge\x01",
            "I can not perceive it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PThat's where Tio's turn comes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FThis person has no problem.\x02\x03",
            "#00200FHowever……\x01",
            "Is the influence of rain OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PWell, it got pretty rainy.\x01",
            "I think that it does not have much influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PBut this thing like this\x01",
            "I will not bear to expose it to the rain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PThat's right, Tio\x01",
            "While the sensor is running\x01",
            "I got an umbrella …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FNo thank you.\x01",
            "Because I am distracted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PShun\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)

    ChrTalk(
        0xA,
        (
            "#02303F#5P─ ─ Yoshi.\x01",
            "I am ready for this too.\x02\x03",
            "#02300FAlways with Aion\x01",
            "It's okay to start it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FLet's get started.\x02\x03",
            "#00200FMr. Lynn's Enigma\x01",
            "Do you have entered the solid number?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12POh, properly from the guild\x01",
            "I heard the number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PI have already entered it into the measuring instrument.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00202FOK.\x02",
    )

    CloseMessageWindow()

    def lambda_4AC2():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AC2)
    Sleep(50)

    def lambda_4AD2():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4AD2)
    Sleep(50)

    def lambda_4AE2():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4AE2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_4AFE():

        label("loc_4AFE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4AFE")

    QueueWorkItem2(0x101, 2, lambda_4AFE)

    def lambda_4B10():

        label("loc_4B10")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B10")

    QueueWorkItem2(0x102, 2, lambda_4B10)

    def lambda_4B22():

        label("loc_4B22")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B22")

    QueueWorkItem2(0x109, 2, lambda_4B22)

    def lambda_4B34():

        label("loc_4B34")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B34")

    QueueWorkItem2(0x105, 2, lambda_4B34)

    def lambda_4B46():

        label("loc_4B46")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B46")

    QueueWorkItem2(0x104, 2, lambda_4B46)

    def lambda_4B58():

        label("loc_4B58")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B58")

    QueueWorkItem2(0xB, 2, lambda_4B58)
    Sleep(150)

    ChrTalk(
        0x101,
        "#11P#00001FThio, I beg you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PLynn's place of residence,\x01",
            "Please locate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x15E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_92(0x103, 0x6C98, 0xFFFF8C60, 0x1F4)
    OP_68(28160, -3400, -29390, 2000)

    def lambda_4C25():
        OP_95(0xFE, 27800, -4400, -29600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C25)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x103, 0x87, 0x1F4)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_4C76():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4C76)
    Sleep(500)
    Sound(2280, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            "#5P#00203F#30W─ ─ Aion system started.\x02\x03",
            "#00201F#30WDepending on the matrix system\x01",
            "Interlocking with measuring instruments#4RLink#Start …\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x8E8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    MoveCamera(346, 20, 0, 18000)
    SetCameraDistance(15950, 18000)
    Sound(852, 2, 100, 0)
    Sound(943, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0xA, 0x29, 0x0, 0x0)
    OP_79(0x8)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sound(938, 2, 50, 0)
    BeginChrThread(0xA, 2, 0, 36)

    ChrTalk(
        0xA,
        (
            "#02304F#6PLinked#4RLink#confirm.\x02\x03",
            "#02302FEven if it keeps going down\x01",
            "It does not seem to be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSupply supply to measuring instruments\x01",
            "It is likely to stabilize at a high level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PThio, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FYes\x01",
            "Well then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#5P#00201F#2683V#40W#20ASensor function release ……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#5P#00203F#2281V#20A#40WAion system ─#800W─\x01",
            "#30W#00207F#4SCancellation of restriction#8RLimit break#It is!\x02",
        )
    )

    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    MoveCamera(333, 19, -5, 4000)
    SetCameraDistance(22000, 4000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(27800, -3300, -29600, 0)
    MoveCamera(100, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    BeginChrThread(0xA, 2, 0, 37)
    OP_68(34800, -2800, -36600, 7000)
    MoveCamera(100, 10, -15, 7000)
    SetCameraDistance(36000, 7000)
    BeginChrThread(0xB, 3, 0, 35)
    OP_6F(0x79)
    WaitChrThread(0xB, 3)

    ChrTalk(
        0x104,
        "#00305F#6PHuh …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FWell, now ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PSomething like a \"wave\"\x01",
            "It seems that it has spread … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(28060, -3400, -29350, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    BeginChrThread(0xA, 2, 0, 36)
    OP_0D()
    OP_71(0x8, 0x5A, 0x64, 0x0, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(852, 500, 90)
    StopSound(943, 500, 40)
    EndChrThread(0x103, 0x3)
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    StopBGM(0x1770)
    Sleep(500)

    ChrTalk(
        0x103,
        "#6P#00206F… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYeah yeah, it looks like success.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(27400, -3200, -27000, 1200)

    def lambda_51D8():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51D8)
    Sleep(50)

    def lambda_51E8():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51E8)
    Sleep(50)

    def lambda_51F8():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51F8)
    Sleep(50)

    def lambda_5208():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5208)
    Sleep(50)

    def lambda_5218():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5218)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P#00007Freally……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PLynn's place is where\x01",
            "Did you understand? Is it?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12PYeah, well exactly\x01",
            "It is a place of Enigma.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203FTwo alert signals\x01",
            "I also sensed it.\x02\x03",
            "#00201FIt is quite south from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02302F#6PSo, analyze the incoming information\x01",
            "When outputting to map information …\x02\x03",
            "#02309F(Kata kata) ── Hora, it came out.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(2000)
    SetMessageWindowPos(10, 40, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FHuh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 80, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10101Fhere……\x01",
            "South side of Lake Elm … ….! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 20, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FWhat is this … ….\x01",
            "Did something happen in such a place?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 80, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FWow, as far as I know\x01",
            "There is not even a person's hand entered\x01",
            "I think it is a wetland area, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 20, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10301FIn such a place, that wreck fighter\x01",
            "Whether there are older sisters ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 180, -1, -1)

    AnonymousTalk(
        0xA,
        (
            "#02305FI do not know well,\x01",
            "Is not it thing stuff?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 60, -1, -1)

    AnonymousTalk(
        0xB,
        "Well, I'm worried about it …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    AnonymousTalk(
        0x103,
        "#00208FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 40, -1, -1)

    AnonymousTalk(
        0x101,
        "#00008F….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    OP_68(31000, -3300, -28800, 0)
    MoveCamera(13, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, 30300, -4400, -29500, 55)
    SetChrPos(0x103, 30800, -4400, -30900, 15)
    SetChrPos(0x102, 29600, -4400, -28800, 55)
    SetChrPos(0x104, 28600, -4400, -28300, 100)
    SetChrPos(0x109, 28600, -4400, -30000, 55)
    SetChrPos(0x105, 29300, -4400, -30700, 55)
    SetChrPos(0xB, 30400, -4400, -26800, 100)
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    OP_70(0x8, 0x2)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_93(0x101, 0xF0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00003FTentatively, for the time being\x01",
            "Let's return to Michelle's place.\x02\x03",
            "#00001FAlso, just to be sure the police headquarters\x01",
            "Those who had the boat arranged\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5795():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5795)
    Sleep(50)

    def lambda_57A5():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_57A5)
    Sleep(50)

    def lambda_57B5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_57B5)
    Sleep(50)

    def lambda_57C5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57C5)
    Sleep(50)

    def lambda_57D5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_57D5)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00106F#5PI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FYeah, considering the situation\x01",
            "It seems better to hurry!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5850():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5850)
    Sleep(50)

    def lambda_5860():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5860)
    Sleep(50)

    def lambda_5870():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5870)
    Sleep(50)

    def lambda_5880():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5880)
    Sleep(50)

    def lambda_5890():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5890)
    Sleep(50)

    def lambda_58A0():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_58A0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00000FJonah to Roberts as chief\x01",
            "Thank you for cooperation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5906():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_5906)
    Sleep(50)

    def lambda_5916():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5916)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0xB,
        (
            "#5PWhat kind of?\x01",
            "Please leave it up after cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02302F#11PWell, please be careful at least ~.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3AF)
    OP_24(0x3AA)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_429F end

    def Function_35_59C8(): pass

    label("Function_35_59C8")

    Sleep(2600)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 29400, -2900, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1014, 0, 100, 0)
    Sleep(1000)
    Sound(895, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x103, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(998, 0, 100, 0)
    Sound(922, 0, 100, 0)
    Sound(833, 0, 40, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0x103, 0x1, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1000)
    CancelBlur(1500)
    Sleep(2000)
    Return()

    # Function_35_59C8 end

    def Function_36_5AC0(): pass

    label("Function_36_5AC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5ADE")
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Jump("Function_36_5AC0")

    label("loc_5ADE")

    Return()

    # Function_36_5AC0 end

    def Function_37_5ADF(): pass

    label("Function_37_5ADF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AFD")
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    Jump("Function_37_5ADF")

    label("loc_5AFD")

    Return()

    # Function_37_5ADF end

    def Function_38_5AFE(): pass

    label("Function_38_5AFE")

    Sound(943, 2, 50, 0)
    OP_71(0x8, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x8)
    Sound(311, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 29400, -4400, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0x32, 0x59, 0x0, 0x20)
    Return()

    # Function_38_5AFE end

    def Function_39_5B5D(): pass

    label("Function_39_5B5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7B")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_39_5B5D")

    label("loc_5B7B")

    Return()

    # Function_39_5B5D end

    def Function_40_5B7C(): pass

    label("Function_40_5B7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BC3")
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_40_5B7C")

    label("loc_5BC3")

    Return()

    # Function_40_5B7C end

    def Function_41_5BC4(): pass

    label("Function_41_5BC4")

    Sound(938, 2, 0, 0)
    Sleep(200)
    OP_25(0x3AA, 0x5)
    Sleep(200)
    OP_25(0x3AA, 0xA)
    Sleep(200)
    OP_25(0x3AA, 0xF)
    Sleep(200)
    OP_25(0x3AA, 0x14)
    Sleep(200)
    OP_25(0x3AA, 0x19)
    Sleep(200)
    OP_25(0x3AA, 0x1E)
    Sleep(200)
    OP_25(0x3AA, 0x23)
    Sleep(200)
    OP_25(0x3AA, 0x28)
    Sleep(200)
    OP_25(0x3AA, 0x2D)
    Sleep(200)
    OP_25(0x3AA, 0x32)
    Return()

    # Function_41_5BC4 end

    def Function_42_5C11(): pass

    label("Function_42_5C11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51548.itc", 0x27)
    LoadChrToIndex("apl/ch51543.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev10005.eff")
    LoadEffect(0x2, "event/ev10001.eff")
    LoadEffect(0x4, "event/ev15071.eff")
    LoadEffect(0x5, "event/ev17022.eff")
    LoadEffect(0x6, "event/ev10008.eff")
    LoadEffect(0x7, "event/eva03_01.eff")
    SoundLoad(832)
    SoundLoad(852)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -1000, 180)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1600, 0, -5000, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -5000, 0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1200, 0, 400, 180)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -2400, 0, 400, 180)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 400, 0, 1000, 180)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 90)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -2900, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 90)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x9, 0x29)
    OP_D5(0x29, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    OP_78(0xA, 0x2A)
    OP_D5(0x2A, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetChrFlags(0x2A, 0x1)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 0, 0, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(100000, 0)
    MoveCamera(45, 15, 0, 10000)
    OP_68(0, 1000, 0, 10000)
    SetCameraDistance(12000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1300, -3000, 0)
    MoveCamera(120, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 5000)
    OP_0D()
    BeginChrThread(0x32, 1, 0, 50)
    BeginChrThread(0x10, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x11, 3, 0, 45)
    Sleep(1100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x10, 3)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#11302F#6POh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#04500F#6PLaw\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01605F#6PChestnut, oh, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04602F#6P#NWow ~.\x01",
            "Sounds like that, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(190, 1300, -3970, 1500)
    OP_95(0xC, -60, 0, -2170, 1200, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#11304F#6PKaea - no,\x01",
            "Following the cult, \"Son#4RMiko#With your house\x01",
            "Let me call it.\x02\x03",
            "#11302FOh well, once again,\x01",
            "It appears in this world#2RAppear#It was done.\x02\x03",
            "As the current owner of the Clois family\x01",
            "It is an honor to be greeted.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W…right\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x11,
        (
            "#10804F#11PHuh, your father.\x01",
            "The greeting is that.\x02\x03",
            "#10802FIt is time for them\x01",
            "I will not accept a gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11305F#6POh, I was.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, finally my efforts too\x01",
            "It seems to bear fruit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2000, 1300, -4300, 2000)
    MoveCamera(45, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Sound(977, 0, 100, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0x13, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x12, 3, 0, 46)

    def lambda_662C():
        TurnDirection(0xC, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_662C)
    Sleep(50)

    def lambda_663C():
        TurnDirection(0x11, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_663C)
    Sleep(50)

    def lambda_664C():
        TurnDirection(0x10, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_664C)
    Sleep(50)

    def lambda_665C():
        TurnDirection(0xD, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_665C)
    Sleep(50)

    def lambda_666C():
        TurnDirection(0xE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_666C)
    Sleep(50)

    def lambda_667C():
        TurnDirection(0xF, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_667C)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x12, 3)
    OP_68(-2500, 1300, -4300, 1700)
    Sleep(1700)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x2)
    Sleep(120)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x14, 0x1)
    Sleep(400)
    OP_6F(0x79)
    StopSound(832, 500, 100)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#6P#04900F#3CThose who inherit great treasure … …\x02\x03",
            "In lieu of the ally of \"snobber snake\"\x01",
            "Lifestyle of yourself#2RPurity#I will do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#6PHuh, modestly\x01",
            "We prepared a \"devoted item\".\x02\x03",
            "#04700FPlease accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#11P……Thank you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Fade(500)
    OP_68(0, 1700, -5000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x2)
    Sound(812, 0, 100, 0)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x1)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(10500, 800)

    def lambda_6877():
        TurnDirection(0xC, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6877)
    Sleep(0)

    def lambda_6887():
        TurnDirection(0xD, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6887)
    Sleep(0)

    def lambda_6897():
        TurnDirection(0xE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6897)
    Sleep(0)

    def lambda_68A7():
        TurnDirection(0xF, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_68A7)
    Sleep(0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(0, 7000, -5000, 4000)
    MoveCamera(0, -5, 0, 4000)
    Sleep(2000)
    StopSound(132, 2000, 40)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_06.pmf", 0x229, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0xC, 0x0, 0x1F4)
    OP_93(0xF, 0x2D, 0x1F4)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_93(0x11, 0x0, 0x1F4)
    OP_93(0x13, 0x0, 0x1F4)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x12, 0x0, 0x1F4)
    BeginChrThread(0x28, 3, 0, 47)
    BeginChrThread(0x29, 3, 0, 48)
    BeginChrThread(0x2A, 3, 0, 49)
    OP_68(0, 19000, 1000, 0)
    MoveCamera(215, 40, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 3000, 1000, 8500)
    MoveCamera(135, 27, 0, 8500)
    SetCameraDistance(20000, 8500)
    SoundLoad(979)
    Sound(852, 2, 100, 0)
    Sound(132, 2, 100, 0)
    Sound(979, 2, 100, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 0, 51)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0x3, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    CancelBlur(0)
    Fade(500)
    OP_68(0, 4500, 6500, 0)
    MoveCamera(0, -23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(9500, 0)
    SetChrFlags(0xF, 0x8)
    OP_68(0, 3000, 6500, 1500)
    MoveCamera(0, -13, 0, 1500)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 3000, 6500, 0)
    MoveCamera(23, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x10, 0xFF)
    OP_68(0, 1900, 3000, 4000)
    MoveCamera(33, 9, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    WaitChrThread(0x2A, 3)
    Sleep(300)

    ChrTalk(
        0xF,
        "#01607F#6PHere, this is …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04612F#12PWow ah!\x01",
            "That's cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#04502F#12PHaha\x01",
            "It's a nice toy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#10804F#12P#N\"The shrine machine Iron\" … …\x02\x03",
            "#10800F\"Treasure\" to wreak a miracle\x01",
            "Three interfaces ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(0, 1000, -1000, 0)
    MoveCamera(24, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xC,
        "#11P#11304F#12P… … It's finished more than I expected.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 500)

    ChrTalk(
        0xC,
        (
            "#11P#11300FMen of \"association\".\x01",
            "You seem to have borrowed it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D73():
        TurnDirection(0x13, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6D73)
    Sleep(50)

    def lambda_6D83():
        TurnDirection(0x12, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6D83)
    Sleep(50)

    def lambda_6D93():
        TurnDirection(0x14, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6D93)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)

    def lambda_6DAF():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6DAF)

    ChrTalk(
        0x13,
        (
            "#5P#04709F#6PHa ha, this is also funded\x01",
            "I am always being saved.\x02\x03",
            "#04702FGOLDIES grade operational data\x01",
            "It was great to be able to use it altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04900F#3C#6P#NAnd for this case\x01",
            "It is suitable also for \"the owner\"#2RWonder#Something …\x02\x03",
            "You do not have to think to borrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#10809F#11PUfufu …\x01",
            "It's pretty heavy.\x02\x03",
            "#10802F── Kaoru.\x01",
            "Would you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#12PO.K. I understand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    Sound(802, 0, 50, 0)
    OP_4B(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x2)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)
    OP_68(0, 1900, 3000, 2000)
    MoveCamera(33, 9, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(273, 0, 70, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -7000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 9000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7028():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7028)
    Sleep(50)

    def lambda_7038():
        OP_93(0x11, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7038)
    Sleep(50)

    def lambda_7048():
        OP_93(0x13, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7048)
    Sleep(50)

    def lambda_7058():
        OP_93(0x12, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7058)
    Sleep(50)

    def lambda_7068():
        OP_93(0x14, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7068)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x29, 3, 0, 43)
    BeginChrThread(0x2A, 3, 0, 44)
    WaitChrThread(0x29, 3)
    Sleep(2000)
    StopSound(979, 2000, 100)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    CancelBlur(0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x24, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_5C11 end

    def Function_43_70D9(): pass

    label("Function_43_70D9")

    OP_68(0, 2900, 3000, 1500)
    SetCameraDistance(23000, 1500)
    Sound(935, 0, 100, 0)

    def lambda_70FE():
        OP_96(0xFE, 0xFFFFE4A8, 0x7D0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_70FE)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x14A, 0x15E, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xA)
    OP_71(0x9, 0xA, 0x32, 0x0, 0x20)
    WaitChrThread(0x29, 1)
    OP_6F(0x79)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0x65, 0x6E, 0x15E, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x6F, 0x96, 0x0, 0x20)
    OP_68(0, 3900, -3000, 2500)
    MoveCamera(60, 7, 15, 2500)
    SetCameraDistance(40000, 6500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 500, 3000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1000, 3000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1500, 3000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 50, 0)
    Sound(499, 0, 100, 0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0x29)
    OP_9F(0x1, 8000, 3000, -4000)
    OP_9F(0x1, 20000, 4000, -7000)
    OP_9F(0x1, 500000, 7000, -8000)

    def lambda_73C9():
        OP_9F(0x2, 0x29, 20000, 0x6)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_73C9)
    Sleep(1000)

    def lambda_73DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_73DB)
    Sleep(300)

    def lambda_73EB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_73EB)
    OP_6F(0x41)
    Return()

    # Function_43_70D9 end

    def Function_44_73F6(): pass

    label("Function_44_73F6")

    Sound(978, 0, 50, 0)
    OP_25(0x3D3, 0x64)
    OP_71(0xA, 0x5A, 0x33, 0x0, 0x0)

    def lambda_7411():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7411)
    WaitChrThread(0x2A, 1)
    OP_79(0xA)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)
    Sleep(2000)
    OP_9F(0x0, 0x2A)
    OP_9F(0x1, -5000, 3000, -3000)
    OP_9F(0x1, -20000, 4000, -6000)
    OP_9F(0x1, -200000, 7000, -7000)

    def lambda_746F():
        OP_9F(0x2, 0x2A, 10000, 0x6)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_746F)
    Sleep(1000)

    def lambda_7481():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7481)
    Sleep(100)

    def lambda_7491():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7491)
    Sleep(100)

    def lambda_74A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_74A1)
    Return()

    # Function_44_73F6 end

    def Function_45_74AA(): pass

    label("Function_45_74AA")

    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1800)

    def lambda_74E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_74E9)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_45_74AA end

    def Function_46_74FA(): pass

    label("Function_46_74FA")

    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 80, 0)

    def lambda_753F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_753F)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_46_74FA end

    def Function_47_7550(): pass

    label("Function_47_7550")

    SetChrPos(0x28, 0, 20000, 7000, 180)
    OP_71(0x5, 0x5B, 0x82, 0x0, 0x20)

    def lambda_7572():
        OP_96(0xFE, 0x0, 0x1F4, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7572)
    WaitChrThread(0xFE, 1)
    OP_71(0x5, 0x83, 0x96, 0x0, 0x0)

    def lambda_759C():
        OP_96(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759C)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_7550 end

    def Function_48_760A(): pass

    label("Function_48_760A")

    SetChrPos(0x29, -7000, 25000, 2000, 135)
    OP_71(0x9, 0xB, 0x32, 0x0, 0x20)

    def lambda_762C():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_762C)
    Sleep(13000)
    Sound(905, 0, 70, 0)
    OP_71(0x9, 0x122, 0x136, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xF)
    OP_71(0x9, 0x136, 0x14A, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_760A end

    def Function_49_76B3(): pass

    label("Function_49_76B3")

    SetChrPos(0x2A, 9000, 28000, 2000, 225)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)

    def lambda_76D5():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76D5)
    WaitChrThread(0xFE, 1)
    OP_71(0xA, 0x33, 0x5A, 0x0, 0x0)

    def lambda_76FF():
        OP_96(0xFE, 0x2328, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76FF)
    WaitChrThread(0xFE, 1)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_25(0x3D3, 0x1E)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 9000, 0, 2000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2BC, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_79(0xA)
    OP_71(0xA, 0x172, 0x19A, 0x3E8, 0x20)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_49_76B3 end

    def Function_50_779E(): pass

    label("Function_50_779E")

    Sound(921, 0, 100, 0)
    Sound(922, 0, 50, 0)
    Sound(977, 0, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(700)
    Sound(922, 0, 40, 0)
    Sound(977, 0, 60, 0)
    Sleep(800)
    Sound(936, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 80, 0)
    StopSound(832, 1000, 100)
    Return()

    # Function_50_779E end

    def Function_51_77DE(): pass

    label("Function_51_77DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7860")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780E")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_7858")

    label("loc_780E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7833")
    OP_82(0x4B, 0x96, 0x1388, 0x1F4)
    Jump("loc_7858")

    label("loc_7833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7858")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_7858")

    label("loc_7858")

    Sleep(500)
    Jump("Function_51_77DE")

    label("loc_7860")

    Return()

    # Function_51_77DE end

    def Function_52_7861(): pass

    label("Function_52_7861")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51532.itc", 0x27)
    LoadEffect(0x0, "event/ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3978)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1500, 0, -2000, 270)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -600, 0, -6300, 270)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -4900, 270)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3700, 0, -700, 270)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -4100, 0, 400, 270)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1900, 0, -200, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 270)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -3300, 270)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 270)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(-7500, 2200, -4000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    Sound(852, 2, 100, 0)
    OP_68(-2800, 1200, -3040, 3000)
    SetCameraDistance(13500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0xE,
        "#04612F#3978V#5S#11P#13AHappy New Year! It is!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0xF,
        "#11P#01611F…… Nah, what is it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#04809FAhaha, this is terrible!\x02\x03",
            "#04802F\"zero#2Rzero#The treasure of \"… ….\x01",
            "You said well, are not you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#04702FKuku, Goldias grade final mold\x01",
            "At the same time three body …!\x02\x03",
            "And as a substitute for \"miracle\"\x01",
            "To be made autonomous … …!\x02\x03",
            "#04709FHaha, this is also to that person\x01",
            "It is going to be a good report!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12P#04900F#3C#30W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#04504FHun …\x01",
            "It is certainly a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12P#10811FHuh, well if it is first\x01",
            "I wonder if this is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#40W….\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        (
            "#11P#11309FJuffu\x01",
            "#4SHa ha ha ha ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1650, 1200, -2100, 1500)
    MoveCamera(90, 21, 0, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)
    SetCameraDistance(12000, 10000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sleep(110)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11304F#30W── Now, with this moment\x01",
            "Crossbell became \"sacred place\"!\x02\x03",
            "#11302FRejecting the empire and republic strength,\x01",
            "A new order across the continent\x01",
            "To the base to bring … ….!\x02\x03",
            "Ideal and justice of our Clois family\x01",
            "At the center for spreading to the world …!\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)

    ChrTalk(
        0xC,
        "#11309F#5S#40W#30AHa ha ha ha ha ha ha!\x02",
    )

    Sleep(2000)
    StopSound(132, 2000, 100)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_7861 end

    def Function_53_80CC(): pass

    label("Function_53_80CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch03600.itc", 0x20)
    LoadChrToIndex("chr/ch04200.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12300, -33620, 23500, 0)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 6900, 0, -14700, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 5700, 0, -15500, 135)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7500, 0, -16200, 135)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 0, 180)
    OP_D5(0x28, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x406)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(0, 6500, 0, 0)
    MoveCamera(147, -3, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 3500, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(6800, 1200, -16300, 4000)
    MoveCamera(90, 13, 0, 4000)
    SetCameraDistance(12500, 4000)
    OP_6F(0x79)
    SetCameraDistance(11500, 30000)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#6P#04804FWell, already,#4RNuclear power plant#Plan\x01",
            "I moved the stage to the empire … …\x02\x03",
            "#04802FFrom here, as planned,\x01",
            "What is it like waiting for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04923FYes, it does.\x02\x03",
            "#04921FUntil the stage towards the Empire progresses\x01",
            "Let's get involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#5PHuh, the power of \"Zero's treasure\" at the present moment\x01",
            "It is comparable to the disappearing \"phantom treasure\".\x02\x03",
            "In addition, the original did not have\x01",
            "Even latent ability#4RI am glad#Showing ……\x02\x03",
            "#04702FKuku, how far can it evolve,\x01",
            "Could you see the hands of the Clois family?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x14,
        (
            "#12P#04809FUhufu …\x01",
            "Dr., I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#6P#04805FBy the way, people of \"\x01",
            "You seem to have finally started moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04924FLet's rather be a good opportunity.\x02\x03",
            "#04922FDifference in standing position with us ……\x01",
            "Should I clarify it for the future as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04700F#5PHuh, I'll leave it to you.\x02\x03",
            "#04704FI am here, \"the treasure of zero\"\x01",
            "Have the data continue …\x02\x03",
            "#04702F── The ultimate link between people and God\x01",
            "Whether to get an interface or not!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6800, -800, -16300, 3000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(12300, -32820, 23400, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(15000, 9000)
    Sound(132, 2, 50, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_80CC end

    def Function_54_8859(): pass

    label("Function_54_8859")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch04200.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 17450, 0, -5600, 225)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 16250, 0, -8350, 45)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_894F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8962")
    Sleep(1)
    Jump("loc_894F")

    label("loc_8962")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_54_8859 end

    def Function_55_8970(): pass

    label("Function_55_8970")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch11600.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(3634)
    SoundLoad(3635)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -22000, -4400, -22000, 225)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -27500, -4400, -32600, 150)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xAF, 0x9B, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    OP_68(-22300, -3300, -44000, 0)
    MoveCamera(195, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    OP_68(-27500, -3300, -32600, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W….\x07\x00\x02",
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
    ClearChrFlags(0x11, 0x80)

    NpcTalk(
        0x11,
        "Voice of Maria Bell",
        (
            "Giggle\x01",
            "You guessed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-24000, -3300, -24000, 0)
    MoveCamera(180, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(-27350, -3300, -31200, 5000)
    MoveCamera(150, 17, 0, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_8C7F():
        OP_95(0xFE, -26500, -4400, -26500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C7F)
    WaitChrThread(0x11, 1)

    def lambda_8C9D():
        OP_95(0xFE, -27000, -4400, -29500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C9D)
    WaitChrThread(0x11, 1)
    TurnDirection(0x10, 0x11, 400)
    OP_6F(0x79)
    SetCameraDistance(11500, 50000)
    Sleep(150)

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12300FBelle…\x02\x03",
            "#12308FIt seems that Dieter is looking for it\x01",
            "Do not you have to go?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x11,
        (
            "Uhufu, to the father a little more\x01",
            "Let's get rushed.\x02\x03",
            "After all, there is no resonance of \"bell\"\x01",
            "Is deployment of \"barrier\" difficult?\x02",
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

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30WYes… As I am now\x02\x03",
            "#12308FThat girl#6RIron#We can move, but\x01",
            "I wonder if I can use the power of \"sky\" ……\x02\x03",
            "#12315FLloyd is coming…\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#02913FEhe, that's a problem\x02\x03",
            "It only moves as planned\x01",
            "It will be gone.\x02\x03",
            "#02911FAccording to \"His\" plan\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W….\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#02902FEverything is up to Mr. Kea … …\x01",
            "We just follow.\x02\x03",
            "#02903FWill you get off here?\x01",
            "Or can you make it all#14R噵 噵 噵 噵 噵 噵 噵#.\x02\x03",
            "#02912FIt's time to decide \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#40W…right\x02\x03",
            "#12302FFrom the beginning, there is no other way\x01",
            "I knew Ka'a … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x73, 0x1F4)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#3634V#40W#55ALloyd and Eli, Tio and Randy,\x01",
            "Even for Suzuku and everyone ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(11000, 2000)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3635V#40W#45AI'll definitley make it all come true.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_8970 end

    def Function_56_91CA(): pass

    label("Function_56_91CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17031.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-570, 2100, -8640, 0)
    MoveCamera(144, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(130610, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(3650, 11100, 4520, 10000)
    MoveCamera(133, -7, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(54000, 10000)
    BeginChrThread(0x29, 0, 0, 57)
    OP_0D()
    Sleep(7000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x2)
    SetScenarioFlags(0x23, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_91CA end

    def Function_57_933E(): pass

    label("Function_57_933E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_937C")
    Sleep(600)
    OP_98(0xFE, 0x0, 0xFFFFF8F8, 0x0, 0x258, 0x1)
    Sleep(600)
    OP_98(0xFE, 0x0, 0x708, 0x0, 0x258, 0x1)
    Jump("Function_57_933E")

    label("loc_937C")

    Return()

    # Function_57_933E end

    def Function_58_937D(): pass

    label("Function_58_937D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    LoadEffect(0x0, "event/ev17031.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    OP_78(0x9, 0x29)
    OP_49()
    SetChrPos(0x29, -15000, 10200, 60080, 0)
    OP_93(0x29, 0xB4, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0xDD)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x13, 0x2B)
    OP_49()
    SetChrPos(0x2B, 200000, 45000, -200000, 0)
    OP_93(0x2B, 0x13B, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x13, 0x96, 0x96, 0x96)
    OP_75(0x13, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(5000, 9900, 1500, 0)
    MoveCamera(154, 2, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(42350, 0)
    OP_68(5000, 9900, 1500, 5000)
    MoveCamera(136, 3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(42350, 5000)
    OP_0D()
    Sleep(1500)
    OP_75(0x13, 0x2, 0x0)
    OP_93(0x29, 0xA1, 0x28)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 60)
    BeginChrThread(0x29, 1, 0, 61)
    Sleep(500)
    Sound(499, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sleep(4000)
    OP_6F(0x79)
    OP_FF(0x13, 0x3E8, 0x3E8, 0x3E8)
    SetMapObjFlags(0x13, 0x4)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(999, 0, 100, 0)
    OP_68(133720, 25300, -151690, 0)
    MoveCamera(323, 6, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(107240, 0)
    Fade(500)
    OP_0D()
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    EndChrThread(0x29, 0x0)
    OP_6F(0x79)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_937D end

    def Function_59_9815(): pass

    label("Function_59_9815")

    ClearMapObjFlags(0x9, 0x20)
    OP_79(0x9)
    Sound(982, 0, 100, 0)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0xC9, 0xDC, 0x0, 0x0)
    Sleep(300)
    Sleep(1000)
    OP_79(0x9)
    OP_70(0x9, 0xDD)
    Return()

    # Function_59_9815 end

    def Function_60_9844(): pass

    label("Function_60_9844")

    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x2EE0, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5500, 10200, 3080)
    OP_9F(0x1, 50000, 10200, -120000)
    OP_9F(0x1, 72000, 14200, -155000)
    OP_9F(0x1, 95000, 18200, -180000)
    OP_9F(0x1, 120000, 22200, -200000)
    OP_9F(0x1, 150000, 25200, -215000)
    OP_9F(0x1, 203000, 33200, -225000)
    OP_9F(0x2, 0xFE, 65000, 0x2)
    Return()

    # Function_60_9844 end

    def Function_61_98E1(): pass

    label("Function_61_98E1")

    Sleep(2000)
    OP_74(0x9, 0x3)
    OP_71(0x9, 0x104, 0x103, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_61_98E1 end

    def Function_62_98F8(): pass

    label("Function_62_98F8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17050.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(943)
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(950)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "President Dieter")
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -600, 0, -20000, 0)
    SetChrPos(0x102, 600, 0, -20000, 0)
    SetChrPos(0x103, -1100, 0, -21100, 0)
    SetChrPos(0x104, 1100, 0, -21100, 0)
    SetChrPos(0xF4, -600, 0, -22200, 0)
    SetChrPos(0xF5, 600, 0, -22200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1100, -20000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(500, 0)
    OP_0D()

    NpcTalk(
        0xC,
        "Male voice",
        (
            "… …. Good luck.\x01",
            "Up to now guests who have not been invited\x01",
            "What is it that I will follow?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7356", 0)
    OP_68(0, 2500, -2000, 3000)
    MoveCamera(0, 9, 0, 3000)
    SetCameraDistance(13000, 3000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x102,
        "#2P#00107F#NSir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#1P#00007F#NDieter!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1300, -5000, 0)
    MoveCamera(34, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -500, 0, -15500, 0)
    SetChrPos(0x102, 500, 0, -15500, 0)
    SetChrPos(0x103, -1000, 0, -17000, 0)
    SetChrPos(0x104, 1000, 0, -17000, 0)
    SetChrPos(0xF4, 0, 0, -16700, 0)
    SetChrPos(0xF5, 0, 0, -17700, 0)
    SetCameraDistance(18000, 2000)

    def lambda_9D04():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D04)
    Sleep(50)

    def lambda_9D21():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D21)
    Sleep(50)

    def lambda_9D3E():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9D3E)
    Sleep(50)

    def lambda_9D5B():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D5B)

    def lambda_9D75():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D75)

    def lambda_9D8F():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFD5D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9D8F)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 30000)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "Giggle\x01",
            "Long time no see, you guys.\x02\x03",
            "But lunch#4Rlunch#I promised\x01",
            "I do not remember … …\x02\x03",
            "Perhaps the date and time\x01",
            "Have you made a mistake?\x02",
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
            "#00003F#12PVisit without appointment,\x01",
            "I'm sorry.\x02\x03",
            "#00001F── However, also here\x01",
            "There are circumstances that can not be handed over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#N#00206FCancellation of an independent country,\x01",
            "And magic soldiers in the city etc\x01",
            "There are various … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#12PFirst and foremost\x01",
            "Shall I return the keeper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#11304FOh, that's fine\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#11300FHuh, what are you guys,\x01",
            "You seem to be misunderstanding.\x02\x03",
            "Apart from that, we forced Ka'a,\x01",
            "I am not cooperating.\x02\x03",
            "#11303FSurrounding this crossbell,\x01",
            "Extraordinary difficulty ……\x02\x03",
            "#11301FTo solve it\x01",
            "She cooperated with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#N#00208FThat is…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P─ ─ It was also that I also directed it,\x01",
            "It is supposed that the uncle.\x02\x03",
            "#00108FShadow the hunting corps,\x01",
            "By causing Crossbell City to attack,\x01",
            "Fired a citizen's independence mind … …\x02\x03",
            "#00101FBy freezing the assets of the Empire and the Republic\x01",
            "Directed the crisis of autonomous state survival … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D9")

    ChrTalk(
        0x10A,
        (
            "#00606F#12P#N…… Regardless of the truth or falsehood,\x01",
            "It is not a permissible job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A386")

    label("loc_A2D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A332")

    ChrTalk(
        0x105,
        (
            "#10404F#12P#NWell, match pump,\x01",
            "It feels like being extremely rude here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A386")

    label("loc_A332")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A386")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#N…… Regardless of the truth or falsehood,\x01",
            "I think that I can not forgive it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A386")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3EB")

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NAnd that situation\x01",
            "Pounding on Keia-chan\x01",
            "I approached a decision …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B0")

    label("loc_A3EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A455")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NAnd that situation\x01",
            "Pounding on Keia-chan\x01",
            "I approached the decision …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B0")

    label("loc_A455")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4B0")

    ChrTalk(
        0x105,
        (
            "#10408F#12P#NAnd that situation\x01",
            "Attack to that girl\x01",
            "That's why he approached the decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4B0")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PThe white tooth should be a nice middle for selling\x01",
            "Are not you doing too much Eguchi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PPresident Dieter ……\x01",
            "No, with Dieter\x01",
            "I will call you.\x02\x03",
            "#00013FIs that the \"Justice\" you spoke of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#11304FYes. That's correct\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 10, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(37, 11, 0, 50000)
    SetCameraDistance(19000, 50000)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#5P#11303FThe real politics\x01",
            "Not only beautiful things.\x02\x03",
            "With that degree of political work\x01",
            "It would rather be lukewarm.\x02\x03",
            "#11301FTwelve years ago, the empire to Libert\x01",
            "Tragedy caused when invading\x01",
            "Do you guys know?\x02\x03",
            "Or when the republic democratizes\x01",
            "What was the blood purged purged that was done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12P#NAnd so what!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#NWhat the uncle's doing is\x01",
            "Even if it is justified …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11304FJustification is not \"done\".\x01",
            "It is \"to do\" with strength and will.\x02\x03",
            "#11300FI am the head of the Clois family,\x01",
            "Originally about the mission of the clan\x01",
            "I was not very keen on it.\x02\x03",
            "Rather,\x01",
            "Because my daughter is in detail.\x02\x03",
            "#11303F─ ─ But, the founder dreamed of it\x01",
            "The birth of a new \"treasure\"\x01",
            "When it turns out feasible ……\x02\x03",
            "I'm crazy and croised\x01",
            "I appreciate being born.\x02\x03",
            "#11302FTo rule this turbulent era,\x01",
            "The power to spread \"justice\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P#NJustice…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00011F#12P#NSo then you are…\x02\x03",
            "#00006FEven for their own benefit,\x01",
            "It is not due to the desire for control … …\x02\x03",
            "#00010FTo realize \"justice\"\x01",
            "When I did things so far … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11309FHaha, besides that\x01",
            "What kind of reasons are you saying?\x02\x03",
            "#11300FTen years ago, the assets of IBC\x01",
            "At the time of reaching the Continental 1\x01",
            "It is no longer necessary to seek wealth.\x02\x03",
            "To dominate the continent,\x01",
            "I am not interested in erotic illusions.\x02\x03",
            "#11306FI couldn't be patient anymore\x02\x03",
            "Prisoned in the framework of \"state\"\x01",
            "To this world that will fight uselessly.\x02\x03",
            "#11303FIn that sense it is called \"independent country\"\x01",
            "It is not even concerned with the form.\x02\x03",
            "As McDowell declared,\x01",
            "I do not mind being invalid.\x02\x03",
            "#11301F─ ─ Ideal \"justice\" is\x01",
            "Widespread in the world#2RAmane#If it spreads widely …\x02\x03",
            "#11302FOrder is kept by \"justice\"\x01",
            "If a peaceful world is to be built!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACF7")

    ChrTalk(
        0x10A,
        "#00610F#12P#NStupidity\x02",
    )

    CloseMessageWindow()

    label("loc_ACF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD28")

    ChrTalk(
        0x105,
        "#10401F#12P#NAre you serious?\x02",
    )

    CloseMessageWindow()

    label("loc_AD28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD72")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#NKoshi, I can not sympathize with you\x01",
            "I do not have it … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD72")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADC3")

    ChrTalk(
        0x106,
        (
            "#10706F#12P#N… for me\x01",
            "I can only hear it as a picture sketch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC3")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NHow old are you … here\x01",
            "I never thought it was a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N… …. But the illusion of that \"justice\" too\x01",
            "It will be realized to some extent …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#NWell, Ka'a-chan\x01",
            "\"If there is a treasure of zero\" …\x02\x03",
            "#00108F…… There is no existing political thought,\x01",
            "It is a circumstance setting to say even as a foul.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P#N#30W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(147, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, 500, 0, -9700, 0)
    SetChrPos(0xF5, -500, 0, -10700, 0)
    MoveCamera(151, 13, 0, 30000)
    SetCameraDistance(19000, 30000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11PDieter.\x02\x03",
            "I … … In your opinion\x01",
            "I studied variously.\x02\x03",
            "#00001FBut about your \"justice\" ……\x01",
            "It seems that it was a bit overrated.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#6P#11301F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FWe are policemen,\x01",
            "Moreover, I belong to the Special Affairs Support Division.\x02\x03",
            "#00003FIn accordance with the rule of law,\x01",
            "Embodying \"justice\" in a cuddling manner with citizens.\x02\x03",
            "#00001Fbut……\x01",
            "There is no guarantee that there will always be correct answers,\x01",
            "There are many things to get lost.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1E2")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F…… Of course.\x01",
            "Security maintenance and security\x01",
            "There is not a correct answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E2")


    ChrTalk(
        0x102,
        (
            "#11P#00106F… That's right.\x01",
            "If the position is different, the way of \"justice\"\x01",
            "It is changing things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00204FWhile hesitating, although sometimes failing\x01",
            "I will pursue \"justice\" …\x02\x03",
            "#00202FOnce upon Mr. Dieter\x01",
            "It is also what I was told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FSomehow, the speech at that time\x01",
            "I feel like it is completely different?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11303F…… That power and will\x01",
            "In a situation that is not sufficient\x01",
            "I talked about methodology.\x02\x03",
            "In a situation where both of them are complete\x01",
            "Do not exercise \"justice\" …\x02\x03",
            "#11301FIs that not \"laziness\"?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00013F#4S#11PNo!\x02",
    )

    CloseMessageWindow()

    def lambda_B3FD():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE2B4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3FD)
    WaitChrThread(0x101, 1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#11P\"Justice\" is easy to shift,\x01",
            "The shape is not fixed …!\x02\x03",
            "In keeping pursuing it,\x01",
            "Worth everyone … …!\x02\x03",
            "#00007FWhat you are trying to do is\x01",
            "\"Justice\" is put in a mold and standardized,\x01",
            "It's only to press it …!\x02\x03",
            "Such a thing really\x01",
            "Do you want \"justice\"! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11310FUgh…\x02\x03",
            "#11307FIn fact I\x01",
            "Open the wind holes in the political situation of Crossbell\x01",
            "We have accomplished several reforms!\x02\x03",
            "Do you deny that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FThat is a different matter\x02\x03",
            "#00108FAll of my uncle\x01",
            "I do not intend to deny it,\x01",
            "It is true that there were many places to learn.\x02\x03",
            "#00101FThat's why … … that fraud#4RGinka#When\x01",
            "There is no choice but to point out a misunderstanding.\x02\x03",
            "#00107FAs a person who respected you … …\x01",
            "Even in the meaning that you want you to notice the mistake!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#6P#11302F#4SVery well!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, 2000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, -500, 0, -9700, 0)
    SetChrPos(0xF5, 500, 0, -10700, 0)
    OP_0D()
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    OP_68(0, 1100, -4000, 1500)
    MoveCamera(0, 21, 0, 1500)
    SetCameraDistance(27000, 1500)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 66)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "move")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B85A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B85A)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_B87F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B87F)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6P#NWhat!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10, 1300, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x103, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    MoveCamera(45, 13, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_0D()
    SetMessageWindowPos(250, 250, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B99A")

    AnonymousTalk(
        0x105,
        (
            "#10407Fthis is……\x01",
            "Power of \"magic\" …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA19")

    label("loc_B99A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9DB")

    AnonymousTalk(
        0x106,
        (
            "#10707Fthis is……\x01",
            "Power of \"magic\" …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA19")

    label("loc_B9DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA19")

    AnonymousTalk(
        0x109,
        (
            "#10107FGuiding magic ……\x01",
            "─ ─ No, not! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA19")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(0, 250, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FBe careful!\x02\x03",
            "From Orchise Tower\x01",
            "Huge spiritual power centered on him\x01",
            "We are gathering … ….!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#11304FIt is not as good as Huff, Bell\x01",
            "As the owner of the Clois family\x01",
            "This degree is favorite#2RTaste#Please do it …\x02\x03",
            "#11300FAnd this Orkis Tower\x01",
            "If you use \"Reiko conversion function\" -\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0xC,
        "#11307F#4S#12AThen I can even do this!\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(950, 2, 40, 0)
    Sound(935, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BBCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BBCE)
    StopEffect(0x0, 0x2)
    WaitChrThread(0xC, 2)
    OP_68(0, 4000, 5000, 3000)
    SetChrFlags(0xC, 0x20)

    def lambda_BBFC():
        OP_96(0xFE, 0x0, 0xFA0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BBFC)
    WaitChrThread(0xC, 1)
    StopEffect(0x1, 0x2)
    Sound(930, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(950, 1000, 40)
    OP_6F(0x79)
    Sleep(1500)
    StopSound(927, 1000, 100)

    ChrTalk(
        0x102,
        "#00105FAh\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC82")

    ChrTalk(
        0x10A,
        "#00605FHe went inside?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCED")

    label("loc_BC82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCBC")

    ChrTalk(
        0x109,
        "#10111FSucked in … …! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCED")

    label("loc_BCBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCED")

    ChrTalk(
        0x106,
        "#10712FI was inhaled …! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_BCED")

    OP_68(0, 4000, 5000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(12500, 6000)
    Sound(140, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Sleep(1000)
    BeginChrThread(0x28, 3, 0, 63)
    Sleep(2000)
    OP_6F(0x79)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WVisibility and control are nominal\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WWhile receiving the power of \"treasure\"\x01",
            "It seems to be able to manipulate freely.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x28, 3)
    StopBGM(0xBB8)
    OP_68(0, 2500, -7500, 2500)
    MoveCamera(0, 5, 0, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(2000)

    def lambda_BDFC():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDFC)
    Sleep(50)

    def lambda_BE19():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BE19)
    Sleep(50)

    def lambda_BE36():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BE36)
    Sleep(50)

    def lambda_BE53():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE53)
    Sleep(50)

    def lambda_BE70():
        OP_97(0xF4, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BE70)
    Sleep(50)

    def lambda_BE8D():
        OP_97(0xF5, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BE8D)
    OP_6F(0x79)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00107F#12P#NS-sir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x101,
        "Tio",
        (
            "#00207F#6P#NPuppet weapons from spiritual topological space\x01",
            "I am controlling …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#12P#NOi oi, is that even possible!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7554", 0)
    Fade(250)
    OP_68(0, 4000, 5000, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    OP_71(0x5, 0x492, 0x4BA, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x4BA, 0x4CE, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    Sleep(100)
    Sound(833, 0, 100, 0)
    Sound(859, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 2000, -1000, 12000)
    MoveCamera(35, 5, 0, 12000)
    SetCameraDistance(17000, 12000)
    Sleep(1000)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#18AHaha, this embodies \"justice\"\x01",
            "A white aircraft to let the world know …\x02",
        )
    )

    CloseMessageWindow()
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4CE, 0x4E2, 0x0, 0x0)
    OP_79(0x5)
    Sound(951, 0, 100, 0)
    OP_71(0x5, 0x335, 0x348, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x349, 0x352, 0x0, 0x20)
    Sound(833, 0, 100, 0)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#16ANow\x01",
            "Let 's prove it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#20AMy \"justice\" and your \"justice\" … …\x01",
            "Let's see which one is right!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C233")
    Sound(540, 0, 50, 0)

    label("loc_C233")

    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00010F#12P#NUgh.. That's perfect\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#NWith full power\x01",
            "I will challenge you …!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x3B6)
    OP_24(0x39F)
    OP_24(0x3A5)
    OP_24(0x3AF)
    Battle("BattleInfo_7B4", 0x30200011, 0x0, 0x100, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 67)
    Return()

    # Function_62_98F8 end

    def Function_63_C2C9(): pass

    label("Function_63_C2C9")

    OP_71(0x5, 0x442, 0x492, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(1000)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Return()

    # Function_63_C2C9 end

    def Function_64_C2F7(): pass

    label("Function_64_C2F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C30F")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C30F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C327")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C33F")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_C33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C357")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_C357")

    Return()

    # Function_64_C2F7 end

    def Function_65_C358(): pass

    label("Function_65_C358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C370")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_C370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C388")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_C388")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3A0")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_C3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3B8")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_C3B8")

    Return()

    # Function_65_C358 end

    def Function_66_C3B9(): pass

    label("Function_66_C3B9")

    Sound(922, 0, 100, 0)
    Sound(927, 2, 100, 0)
    Sound(933, 2, 100, 0)
    Sound(943, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Return()

    # Function_66_C3B9 end

    def Function_67_C3DE(): pass

    label("Function_67_C3DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51769.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17052.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(943)
    SoundLoad(950)
    SoundLoad(579)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 2000, 5500, 180)
    OP_8E(0xC, "President Dieter")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x3A2)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "open")
    OP_68(0, 3500, -1000, 0)
    MoveCamera(35, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x32, 1, 0, 69)
    OP_68(0, 1500, -1000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000F#12PW-we did it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12PSo somehow…\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7554", 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(930, 0, 80, 0)
    Sound(933, 2, 100, 0)
    Sound(927, 2, 100, 0)
    EndChrThread(0x32, 0x1)
    Sleep(1000)
    SetMapObjFlags(0x18, 0x4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00207F#12PReiko energy,\x01",
            "It is filled again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#12PNo way!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2000, -1000, 2000)
    Sound(905, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WHuff, \"The treasure of zero\"\x01",
            "This aircraft gains unlimited power.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WUnless it is decisively destroyed,\x01",
            "There is no defeat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#12P#NUgh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C908")

    ChrTalk(
        0x10A,
        "#00610F#12P#NIs that right\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C946")

    ChrTalk(
        0x105,
        "#10410F#12P#NIt is too foul to the contrary …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C946")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C984")

    ChrTalk(
        0x109,
        "#10110F#12P#NKuu …… Anything ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C984")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9C8")

    ChrTalk(
        0x106,
        "#10708F#12P#NWe need to find a weakness\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C9C8")

    Sleep(500)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WHuh, I guess your life\x01",
            "I'm going to take away my head.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WSurrendering adultly,\x01",
            "If you cooperate with my ideals - ─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    Sound(954, 0, 100, 0)
    Sound(922, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(927, 1000, 100)
    Fade(250)
    ClearMapObjFlags(0x5, 0x20)
    OP_70(0x5, 0xB)
    OP_0D()
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Voice of Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SIt is! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Sound(955, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What's this\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_70(0x14, 0xB)
    Fade(1000)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    Sleep(1500)

    ChrTalk(
        0x104,
        "#00301F#12P#NWhat happened\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#NReiko energy supply\x01",
            "Ceased …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x14, 0x564, 0x58C, 0x0, 0x0)
    Sound(905, 0, 100, 0)
    Sound(954, 0, 100, 0)
    OP_79(0x14)
    Sound(902, 0, 100, 0)
    OP_68(0, 1000, -1000, 2000)
    MoveCamera(35, 19, 0, 2000)
    SetCameraDistance(35000, 2000)
    Sleep(1500)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 68)
    Sound(927, 2, 100, 0)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    OP_0D()
    SetMapObjFrame(0xFF, "futa00", 0x2, "move2")
    Sleep(1300)
    Fade(500)
    OP_68(50000, -4500, -50000, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    OP_68(0, -4500, -10000, 9000)
    MoveCamera(0, 33, 0, 9000)
    SetCameraDistance(115000, 9000)
    OP_71(0x1, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x2, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x3, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x4, 0x12C, 0x0, 0x0, 0x0)
    Sleep(2000)
    Sound(579, 2, 30, 0)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    OP_79(0x4)
    StopSound(927, 500, 100)
    StopSound(579, 500, 20)
    Sound(954, 0, 100, 0)
    Sound(143, 0, 30, 0)
    SetMapObjFrame(0xFF, "futa01", 0x2, "move2")
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    Sleep(1500)
    Fade(500)
    OP_68(0, 2000, 5500, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_68(0, 2000, 3500, 3500)
    MoveCamera(35, 11, 0, 3500)
    SetCameraDistance(17000, 3500)
    Sound(930, 0, 100, 0)
    Sound(950, 2, 40, 0)
    Sound(933, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CE1F():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CE1F)
    WaitChrThread(0xC, 1)

    def lambda_CE3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_CE3D)
    WaitChrThread(0xC, 2)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 30)
    StopSound(933, 1000, 100)
    Sound(935, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)

    ChrTalk(
        0xC,
        "#11310F#5PN-no way!\x02",
    )

    CloseMessageWindow()
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x39F)
    OP_24(0x3B6)
    OP_24(0x243)
    OP_24(0x3AF)
    SetScenarioFlags(0x24, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_67_C3DE end

    def Function_68_CEBE(): pass

    label("Function_68_CEBE")

    Sound(943, 2, 50, 0)
    Sleep(1500)
    OP_24(0x3AF)
    Sound(143, 0, 60, 0)
    Return()

    # Function_68_CEBE end

    def Function_69_CED1(): pass

    label("Function_69_CED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF05")
    Sound(203, 0, 50, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Sleep(1100)
    Sound(203, 0, 50, 0)
    Sleep(800)
    Sound(203, 0, 40, 0)
    Sleep(1000)
    Jump("Function_69_CED1")

    label("loc_CF05")

    Return()

    # Function_69_CED1 end

    def Function_70_CF06(): pass

    label("Function_70_CF06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF44")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_CF44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF5C")
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 1)

    label("loc_CF5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF74")
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_CF74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF8C")
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 3)

    label("loc_CF8C")

    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    LoadChrToIndex("apl/ch51732.itc", 0x21)
    LoadChrToIndex("apl/ch51113.itc", 0x22)
    LoadChrToIndex("apl/ch51734.itc", 0x23)
    LoadEffect(0x0, "event/ev10000.eff")
    LoadEffect(0x1, "event/ev10001.eff")
    LoadEffect(0x2, "event/ev17054.eff")
    SoundLoad(3787)
    SoundLoad(112)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 10000, 0, 1500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 100, 0, -6700, 0)
    SetChrPos(0xF5, -100, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xD, 0x2C)
    OP_78(0xE, 0x2D)
    OP_78(0xF, 0x2E)
    OP_78(0x10, 0x2F)
    OP_78(0x11, 0x30)
    OP_78(0x12, 0x31)
    OP_49()
    SetChrPos(0x2C, 15000, 6000, -3000, 0)
    SetChrPos(0x2D, 15100, 7000, -7500, 0)
    SetChrPos(0x2E, 15100, 7000, 1500, 0)
    SetChrPos(0x2F, 15200, 5000, 5000, 0)
    SetChrPos(0x30, 15200, 5000, -11000, 0)
    SetChrPos(0x31, 15000, 6000, -3000, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x12, 0x1000)
    OP_FF(0xD, 0x168, 0x168, 0x168)
    OP_FF(0xE, 0x140, 0x140, 0x140)
    OP_FF(0xF, 0x140, 0x140, 0x140)
    OP_FF(0x10, 0x140, 0x140, 0x140)
    OP_FF(0x11, 0x140, 0x140, 0x140)
    OP_FF(0x12, 0x17C, 0x17C, 0x17C)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x15, 0x2B)
    OP_49()
    SetChrPos(0x2B, 0, 15000, 6000, 180)
    OP_D5(0x2B, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x17, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 15000, 6000, 180)
    OP_D5(0x18, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_68(210, 2500, 5500, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(210, 1500, 5500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#12P#11307FW-what is this!?\x02\x03",
            "Why is supply from \"treasure\"\x01",
            "Suddenly it stops … …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 40, -1, -1)
    SetChrName("Creepy voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I have time to do extra things\x01",
            "I guess it's because it's gone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrFlags(0x102, 0x8)
    OP_68(10000, 1000, 1500, 2000)
    SetCameraDistance(14000, 2000)
    TurnDirection(0xC, 0x13, 500)
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x103, 0x13, 0)
    TurnDirection(0x104, 0x13, 0)
    TurnDirection(0xF4, 0x13, 0)
    TurnDirection(0xF5, 0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x102, 0x8)
    SetCameraDistance(13000, 2000)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    ClearChrFlags(0x13, 0x80)

    def lambda_D70C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D70C)
    WaitChrThread(0x13, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013FFrom the Organization!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D77B")

    ChrTalk(
        0x105,
        (
            "#10407F\"Thirteen Studio\"\x01",
            "F · Novartis … …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D79E")

    label("loc_D77B")


    ChrTalk(
        0x103,
        "#00207FDr. Novaltisse!\x02",
    )

    CloseMessageWindow()

    label("loc_D79E")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5960, 1000, 1210, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#6P#11310FDr. Novartis … ….\x01",
            "What on earth is that! Is it?\x02\x03",
            "No way, \"association\" to the aircraft\x01",
            "Were you trying to do something! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        (
            "Huff, as I said before\x01",
            "To the end this time helping.\x02\x03",
            "It is that we got good data,\x01",
            "I will be rude soon.\x02\x03",
            "According to our contract. And along with that final unit\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(200)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#6P#11307FContract!?\x02\x03",
            "Stupid, this airplane is here\x01",
            "I bought it from \"Society\"!\x02\x03",
            "You have no right to take it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#04704FNo, actually it is in the contract contents\x01",
            "There was a little change.\x02\x03",
            "The aircraft that became obsolete\x01",
            "To get it collected here,\x01",
            "He took care of me.\x02\x03",
            "#04702F── Your highest daughter,\x01",
            "Miss Maria Bell Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#11305FHuh\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(260, 10, -1, -1)
    SetChrName("Daughter's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3787V#30W#30AAhaha, that's exactly right\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00011F#6P#NThis voice is\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107FBell#6P#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(500)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(62, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0xF4, 0x5A, 0x0)
    OP_93(0xF5, 0x5A, 0x0)
    SetCameraDistance(16000, 3000)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2C, 3, 0, 79)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#11310F#6P#NBelle… what is this\x02\x03",
            "#11307FAnd where are you!?\x02\x03",
            "You aren't in the Orchis Tower!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, I have already long\x01",
            "I will leave that there.\x02\x03",
            "I am with KeA and the others now\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#6P#NHuh!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#6P#NTo be sure, on any floor\x01",
            "It seems I did not exist ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(57, -5, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2D, 3, 0, 80)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2E, 3, 0, 81)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2F, 3, 0, 82)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 83)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00007F#6P#NArios!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE9D")

    ChrTalk(
        0x10A,
        "#00610F#6P#NMacClaine!\x02",
    )

    CloseMessageWindow()

    label("loc_DE9D")


    ChrTalk(
        0x104,
        (
            "#00307F#6P#NUncle Takashi ……!\x01",
            "Shirley …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0A")

    ChrTalk(
        0x106,
        "#10701F#6P#NBloody Shirley!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF0A")


    ChrTalk(
        0x103,
        "#00201F#6P#NAnd even Wald\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF6E")

    ChrTalk(
        0x105,
        "#10401F#6P#NWas it with them either …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF6E")

    Sleep(150)
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well!\x01",
            "It is getting excited!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tch\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#11310F#6P#NWhat is the meaning of this!\x02\x03",
            "#11307Fyou guys……\x01",
            "You betrayed me! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mr. President, I apologize\x02\x03",
            "But I was originally planning for your plan\x01",
            "It was not cooperating.\x02\x03",
            "\"Teacher\" to Mary Maribell 's plan\x01",
            "I just cooperated.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#11305F#30W#6P#NSensei…\x02\x03",
            "#11310FNo way…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes. That's correct\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(90, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    OP_FF(0xD, 0x140, 0x140, 0x140)
    SetChrPos(0x2C, 15100, 5000, -7000, 0)
    SetChrPos(0x2D, 15200, 7500, -10000, 0)
    SetChrPos(0x30, 15300, 4000, -12000, 0)
    SetChrPos(0x2E, 15100, 7500, 2000, 0)
    SetChrPos(0x2F, 15200, 4000, 4000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_0D()
    Sound(922, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(500)
    CancelBlur(1000)
    SetCameraDistance(17500, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2B4")
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#12P#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E2B4")


    ChrTalk(
        0x102,
        "#00105F#12P#NAh….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#12P#N….?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00305F#12P#NThis is a lie right\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E360")

    ChrTalk(
        0x10A,
        "#00605F#12P#NI-Ian-Sensei\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E38E")

    ChrTalk(
        0x109,
        "#10111F#12P#NSounds like that … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C8")

    ChrTalk(
        0x105,
        "#10410F#12P#NNo way … … I do not think so.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E5BD")

    ChrTalk(
        0x101,
        "#00013F#12P#N…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm, in its appearance\x01",
            "Lloyd is my involvement\x01",
            "I wonder if I was aware …?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#N…. Yeah.\x01",
            "A reporter named Nielsen\x01",
            "I gave you a hint.\x02\x03",
            "#00008FAnd Pete and the old man of grave protection …\x01",
            "Kirika and Rector pointed out … …\x02\x03",
            "#00013FAll fragments#4RFragment#Finally\x01",
            "I pointed to your involvement.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehu, apparently perfectly\x01",
            "You seem to have caught up with Guy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E5BD")

    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#6P#11310F#NMr. Grimwood ……\x01",
            "What does this mean …! Is it?\x02\x03",
            "Yes, it certainly comes to my teacher\x01",
            "I asked for consultation … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh … you really\x01",
            "It was a teaching student.\x02\x03",
            "As a manager it is super class,\x01",
            "I was not as bad as a politician.\x02\x03",
            "I am too dreamer#12R噵 噵 噵 噵 噵 噵#That,\x01",
            "Save the fatal shortcomings.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(50)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        "#6P#11305F#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, your father in your opinion\x01",
            "All carried well\x01",
            "It seems I thought … …\x02\x03",
            "In fact, the schedule prepared by the teacher#4Rscenario#Into\x01",
            "I was just being guided.\x02\x03",
            "Treatment of cults, arrangements of trade councils,\x01",
            "From Crossbell City Raid to Declaration of Independence ……\x02\x03",
            "First of all, to the father of the idea\x01",
            "Who was whispering?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        "#6P#11310F#30W#N…Ah…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As long as you can go well\x01",
            "I did not mean to appear on the table … …\x02\x03",
            "Apparently the masterpiece#4RFixer#As only,\x01",
            "It seems I can not stay.\x02\x03",
            "\"Plan for Aiki zero\",\x01",
            "I will carry on like this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        "#6P#11310F#NBeautiful#2RBlue#き … …. zero#2Rzero#……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#6P#NWhat is that!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe, the complete form of the Master of Zero\x02\x03",
            "Dominate space-time and reorganize causality\x01",
            "\"A big blue tree\" ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SIt is the celebration of its birth!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(929, 0, 40, 0)
    Sound(934, 0, 40, 0)
    Sound(112, 2, 100, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    OP_68(8000, 3000, -6000, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_EBF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EBF7)

    def lambda_EC04():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_EC04)

    def lambda_EC11():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EC11)
    Sleep(50)

    def lambda_EC21():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EC21)
    Sleep(50)

    def lambda_EC31():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EC31)
    Sleep(50)

    def lambda_EC41():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EC41)
    Sleep(50)

    def lambda_EC51():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_EC51)
    Sleep(50)

    def lambda_EC61():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_EC61)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00305F#5PThis light is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PA blue light…!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5P…… South south west!\x01",
            "It is around wetlands!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PThat is-\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7555", 0)
    OP_68(8000, 3000, -7000, 2000)
    SetCameraDistance(24500, 2000)
    StopSound(132, 1000, 40)
    StopSound(112, 1000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_07a.pmf", 0x22B, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x16, 0x4)
    StopEffect(0x0, 0x0)
    OP_68(0, 2000, -20000, 0)
    MoveCamera(150, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    Sound(132, 2, 50, 0)
    Sound(112, 2, 80, 0)
    OP_68(0, 2000, -13000, 4000)
    MoveCamera(145, 9, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x7D0)

    ChrTalk(
        0x101,
        "#5P#00010F#6P#N…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE5D")

    ChrTalk(
        0x109,
        "#5P#10111F#6P#NHey ah … …!! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EE5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE8D")

    ChrTalk(
        0x105,
        "#5P#10410F#6P#NTh-This is……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EE8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEBD")

    ChrTalk(
        0x10A,
        "#5P#00610F#6P#NAre you stupid?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EEBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEED")

    ChrTalk(
        0x106,
        "#5P#10701F#6P#N… …. Taiki … …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EEED")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    Sleep(500)

    NpcTalk(
        0x104,
        "Dr. Novartis",
        (
            "#04702F#5P#NKuku - That's great!\x02\x03",
            "The very product of singular point …\x01",
            "Beyond that \"salt pile\" far beyond\x01",
            "Should I say \"an unplanned miracle\"!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#11305F#6P#N…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(112, 2000, 70)
    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#4S#6P#NWait, wait!\x02\x03",
            "#00010F#3SThat huge tree\x01",
            "The completed form of \"Zero's treasure\" …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_F06E():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F06E)
    Sleep(30)

    def lambda_F07E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F07E)
    Sleep(30)

    def lambda_F08E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F08E)
    Sleep(30)

    def lambda_F09E():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F09E)
    Sleep(30)

    def lambda_F0AE():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F0AE)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#00107F#6P#NKa'aa …\x01",
            "…… Where the hell are you! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I wonder what he is saying.\x02\x03",
            "If you are Kea-san,\x01",
            "You can see from there too?\x02\x03",
            "That \"Big Big Tree\" is\x01",
            "Kaea itself#8R噵 噵 噵 噵#Is not it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    SetMessageWindowPos(300, 70, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… Her mind and body are\x01",
            "It was not lost.\x02\x03",
            "Do not worry around that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Ian lawyer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But, from this, she\x01",
            "It becomes all \"mediators\" -\x02\x03",
            "For her and for you too\x01",
            "It should not be a bad result.\x02\x03",
            "I want you to watch it if possible.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00206F#6P#NWhat, exactly what ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#6P#NWe do not understand well … …\x02",
    )

    CloseMessageWindow()
    OP_68(15000, 5000, -5000, 1600)
    MoveCamera(69, -5, 0, 1600)
    SetCameraDistance(19500, 1600)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4AF")
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems like it really is not it.\x02\x03",
            "But if it's fun\x01",
            "Is not it okay?\x02\x03",
            "Ressha jet\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x106,
        "#10701F#6P#N…………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_F509")

    label("loc_F4AF")

    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems like it really is not it.\x02\x03",
            "But if it's fun\x01",
            "Is not it okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F509")

    SetMessageWindowPos(10, 110, -1, -1)

    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kuku, if you're going to get in the way\x01",
            "Do not hesitate to make an opponent.\x02\x03",
            "This is also within the contract.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F638")
    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… These plans are\x01",
            "I do not know it, but …\x02\x03",
            "If you come, this time\x01",
            "I'll crush it thoroughly ….\x02\x03",
            "Hey, Wadi … ….?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10401F#6P#N…… Wald.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_F6B3")

    label("loc_F638")

    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… These plans are\x01",
            "I do not know it, but …\x02\x03",
            "If you come, this time\x01",
            "I'll crush it thoroughly … ….?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F6B3")

    SetMessageWindowPos(160, 150, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhufu …\x01",
            "Well then, everyone, I'm so glad.\x02\x03",
            "── That and my father.\x01",
            "I am indebted to you.\x02\x03",
            "Simple, in romantic\x01",
            "I was silly, but ……\x02\x03",
            "I, that of your father\x01",
            "I never dislike it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x2C, 3, 0, 85)
    Sleep(200)
    BeginChrThread(0x2D, 3, 0, 86)
    Sleep(200)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x2E, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2F, 3, 0, 88)
    Sleep(200)
    BeginChrThread(0x30, 3, 0, 89)
    WaitChrThread(0x30, 3)
    Fade(500)
    OP_68(5000, 1500, -1000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2000, 1500, -1000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    ChrTalk(
        0xC,
        "#5P#11311F#40W………… Bell ……………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    Sleep(1000)

    def lambda_F8F3():
        OP_A6(0xFE, 0x0, 0x1E, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F8F3)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(500)
    TurnDirection(0x13, 0xC, 500)

    ChrTalk(
        0x13,
        (
            "#04704FHuff, if there is no role\x01",
            "I will go out with you until the end … …\x02\x03",
            "#04700FWell, at most in the distant land\x01",
            "Lets say you have a follow - up report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(901, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_0D()
    OP_68(0, 2000, -1000, 2000)
    MoveCamera(31, 5, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sound(980, 2, 30, 0)
    BeginChrThread(0x28, 3, 0, 77)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_FAAC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FAAC)
    Sleep(50)

    def lambda_FABC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FABC)
    Sleep(50)

    def lambda_FACC():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FACC)
    Sleep(50)

    def lambda_FADC():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FADC)
    Sleep(50)

    def lambda_FAEC():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_FAEC)
    Sleep(50)

    def lambda_FAFC():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_FAFC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F#12P#N……Ah………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 78)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)

    def lambda_FB92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FB92)
    WaitChrThread(0x13, 2)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    OP_D3(0x13, 0x5, "Null_hand_l(63)")
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(310, 4200, 5930, 2000)
    MoveCamera(31, 7, 0, 2000)
    SetCameraDistance(15000, 2000)
    Sleep(500)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1900, 3900, 4750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_FC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FC42)
    WaitChrThread(0x13, 2)
    Sound(936, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x13,
        (
            "#5P#04709FHaha, then, I will excuse myself.\x02\x03",
            "#04704FI think that it is useless\x01",
            "Please try to scratch at most.\x02\x03",
            "#04702FSignificant data\x01",
            "It is not meaning to have it left.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(955, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 4900, 6000, 700)
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x51E, 0x532, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x532, 0x55A, 0x0, 0x20)
    OP_6F(0x79)
    MoveCamera(25, 15, 0, 3000)
    SetCameraDistance(22000, 3000)
    Sound(223, 0, 100, 0)
    Sound(919, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    StopSound(980, 1000, 30)
    OP_75(0x5, 0x1, 0x1F4)

    def lambda_FD9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_FD9F)

    def lambda_FDB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FDB0)
    WaitChrThread(0x13, 2)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 2000, -1000, 0)
    MoveCamera(31, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#00201F#30W#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#30W#11PJust scratch and scratch it\x01",
            "I wonder why …\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x6, 0, 0, -21000, 0)
    SetChrPos(0x7, 0, 0, -22000, 0)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    StopBGM(0x1770)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FEDF")

    NpcTalk(
        0x105,
        "Voice of Wadi",
        "Everyone, are you safe …?! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF40")

    label("loc_FEDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF16")

    NpcTalk(
        0x109,
        "Noel's voice",
        "Everyone … Is it alright! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF40")

    label("loc_FF16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FF40")

    NpcTalk(
        0x10A,
        "Dudley's voice",
        "Is it ok? Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_FF40")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1200, -10000, 2250)
    MoveCamera(55, 13, 0, 2250)
    OP_6E(600, 2250)
    SetCameraDistance(15000, 2250)

    def lambda_FFE8():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FFE8)
    Sleep(50)

    def lambda_FFF8():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FFF8)
    Sleep(50)

    def lambda_10008():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10008)
    Sleep(50)

    def lambda_10018():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10018)
    Sleep(50)

    def lambda_10028():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_10028)
    Sleep(50)

    def lambda_10038():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_10038)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_1005D():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x6, 1, lambda_1005D)
    Sleep(200)

    def lambda_1007A():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x7, 1, lambda_1007A)
    WaitChrThread(0x6, 1)
    WaitChrThread(0x7, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008FBoth of us …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10111")

    ChrTalk(
        0x106,
        (
            "#10708F#12PIt is one thing ……\x02\x03",
            "#10707FAnd that huge\x01",
            "Things like trees ……! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D8")

    label("loc_10111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10176")

    ChrTalk(
        0x10A,
        (
            "#00610F#12PIt is one thing ……\x02\x03",
            "#00607FAnd that huge tree\x01",
            "What is such thing …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D8")

    label("loc_10176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101D8")

    ChrTalk(
        0x109,
        (
            "#10108F#12PWell, now is it ……\x02\x03",
            "#10107FWell, that huge\x01",
            "Things like trees ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101D8")


    ChrTalk(
        0x102,
        "#5P#00106FThat's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00206FWhat to say … …\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -8500, -2000, -20000, 90)

    NpcTalk(
        0x15,
        "Sergei's voice",
        (
            "Apparently still\x01",
            "It looks like it is not the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    OP_68(0, 1000, -21800, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x6, -1200, 0, -12500, 0)
    SetChrPos(0x7, 1200, 0, -12500, 0)

    def lambda_10370():
        OP_95(0xFE, -2200, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10370)
    Sleep(500)
    Sound(112, 2, 50, 0)
    WaitChrThread(0x15, 1)

    def lambda_10397():
        OP_95(0xFE, 0, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10397)
    WaitChrThread(0x15, 1)
    OP_68(0, 1000, -10000, 4000)
    MoveCamera(145, 15, 0, 4000)

    def lambda_103D1():
        OP_95(0xFE, 0, 0, -11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_103D1)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00005FManager……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PIs the lower person okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01003FOh, the magical soldiers disappeared\x01",
            "I got on the tower safely.\x02\x03",
            "#01001FHowever……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(900)
    OP_68(-450, 1500, -5360, 1500)
    SetCameraDistance(18700, 1500)
    OP_93(0x15, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        "#11311F#40W#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01006F…… On the whole,\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PYes……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F#6P……that is……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18200, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrPos(0x101, -450, 0, -9600, 180)
    SetChrPos(0x102, 450, 0, -9100, 180)
    SetChrPos(0x103, -1500, 0, -9600, 135)
    SetChrPos(0x104, 1500, 0, -9600, 225)
    SetChrPos(0xF4, -1050, 0, -8000, 180)
    SetChrPos(0xF5, 1050, 0, -8000, 180)
    SetChrPos(0x6, -1750, 0, -11400, 45)
    SetChrPos(0x7, 1750, 0, -11400, 315)
    SetChrPos(0x15, 0, 0, -12900, 0)
    OP_68(-120, 1100, -11660, 0)
    MoveCamera(143, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds explained to the section chief about the circumstances.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(14500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_106EA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C3")

    ChrTalk(
        0x106,
        "#11P#10712FWell, that's … …\x02",
    )

    Jump("loc_106E4")

    label("loc_106C3")


    ChrTalk(
        0x106,
        "#5P#10712FWell, that's … …\x02",
    )


    label("loc_106E4")

    CloseMessageWindow()
    Jump("loc_107C7")

    label("loc_106EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10757")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1072E")

    ChrTalk(
        0x109,
        "#11P#10106FWell, that's like that ….\x02",
    )

    Jump("loc_10751")

    label("loc_1072E")


    ChrTalk(
        0x106,
        "#5P#10706FWell, that's like that ….\x02",
    )


    label("loc_10751")

    CloseMessageWindow()
    Jump("loc_107C7")

    label("loc_10757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_107C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1079F")

    ChrTalk(
        0x105,
        "#11P#10406FIt's surprisingly surprised …\x02",
    )

    Jump("loc_107C6")

    label("loc_1079F")


    ChrTalk(
        0x105,
        "#5P#10406FIt's surprisingly surprised …\x02",
    )


    label("loc_107C6")

    CloseMessageWindow()

    label("loc_107C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10862")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10822")

    ChrTalk(
        0x10A,
        (
            "#11P#00608FNo way, Professor Ian\x01",
            "It is said that it was one of the masterpieces … …\x02",
        )
    )

    Jump("loc_1085C")

    label("loc_10822")


    ChrTalk(
        0x10A,
        (
            "#5P#00608FNo way, Professor Ian\x01",
            "It is said that it was one of the masterpieces … …\x02",
        )
    )


    label("loc_1085C")

    CloseMessageWindow()
    Jump("loc_1098B")

    label("loc_10862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_108F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_108B9")

    ChrTalk(
        0x105,
        (
            "#11P#10403FThat bear beard teacher\x01",
            "It is not like one of the masterpieces … …\x02",
        )
    )

    Jump("loc_108EF")

    label("loc_108B9")


    ChrTalk(
        0x105,
        (
            "#5P#10403FThat bear beard teacher\x01",
            "It is not like one of the masterpieces … …\x02",
        )
    )


    label("loc_108EF")

    CloseMessageWindow()
    Jump("loc_1098B")

    label("loc_108F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1098B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10950")

    ChrTalk(
        0x109,
        (
            "#11P#10108FThat Ian sensei\x01",
            "It was one of the blacklights … …\x02",
        )
    )

    Jump("loc_1098A")

    label("loc_10950")


    ChrTalk(
        0x109,
        (
            "#5P#10108FThat Ian sensei\x01",
            "It was one of the blacklights … …\x02",
        )
    )


    label("loc_1098A")

    CloseMessageWindow()

    label("loc_1098B")


    ChrTalk(
        0x15,
        (
            "#11P#01006F……got it.\x02\x03",
            "#01001FInternational situation in political and business world, guilds to police,\x01",
            "Is it a person who is also familiar with various back circumstances?\x02\x03",
            "#01003FIf that teacher feels that way\x01",
            "It surely could have set everything.\x02\x03",
            "#01000FThe problem is a motivation, but …\x01",
            "It seems not to be right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYes……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)
    SetChrName("")
    BeginChrThread(0x101, 0, 0, 74)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x101,
        (
            "#13P#00001F── Wadi.\x01",
            "Can you call Mercava?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        "#13P#10402FHuh, I thought he would say so.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x4)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    Sleep(500)
    SetChrSubChip(0x105, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x15,
        "#11P#01000FAre you going?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B88")

    def lambda_10B80():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x6, 2, lambda_10B80)

    label("loc_10B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BA7")

    def lambda_10B9F():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x7, 2, lambda_10B9F)

    label("loc_10BA7")

    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00003F#6PYes, the work of the police is no longer\x01",
            "It may not be possible to say …\x02\x03",
            "#00013FBut, Ka'ah and all the truth\x01",
            "Beyond waiting over there,\x01",
            "I can not leave it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P……me too.\x01",
            "I have to stop the bell …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PWell, if you come this far\x01",
            "It is natural that I would like you to be one lotus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PYour uncle yours too\x01",
            "I guess you are waiting.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 0, 0, 72)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#6P#10107Fme too……\x01",
            "I will go out with you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x105, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x105, 0x15, 500)
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, I will offer Mercapa,\x01",
            "I will get involved too.\x02\x03",
            "#10400FThe settlement with Wald also\x01",
            "It seems necessary to add.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x106, 0, 0, 75)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x106,
        (
            "#6P#10703F…… I am also \"with her\"\x01",
            "It is necessary to settle.\x02\x03",
            "#10708FEven for my own rush ……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x10A, 0, 0, 76)
    WaitChrThread(0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#6P#00603F… with McLaughn\x01",
            "Regarding Mr. Ian's name\x01",
            "There is also need for detailed circumstance hearing.\x02\x03",
            "#00601FI am going to accompany it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01004FHaha\x01",
            "It seems useless to stop it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x32, 1, 0, 91)
    OP_68(1020, 1900, -13060, 3000)
    MoveCamera(143, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x2B, 0, 60000, -10000, 0)
    OP_D5(0x2B, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)

    def lambda_10F99():
        OP_96(0x2B, 0x0, 0x2710, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_10F99)
    BeginChrThread(0x2B, 3, 0, 71)
    OP_68(0, 45000, 0, 0)
    MoveCamera(231, -60, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    MoveCamera(211, -30, 0, 7000)
    SetCameraDistance(45000, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetChrPos(0x18, 11000, 0, -2000, 200)
    OP_D5(0x18, 0x0, 0x30D40, 0x0, 0x0)
    OP_75(0x17, 0x2, 0xBB8)
    OP_68(1020, 1900, -13060, 0)
    MoveCamera(143, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-240, 1100, -11750, 3000)
    MoveCamera(143, 17, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x15,
        (
            "#11P#01003F── Including the President's position,\x01",
            "Leave the city and the tower.\x02\x03",
            "#01001FYou guys are with you\x01",
            "Come until you are satisfied.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x15,
        (
            "#01007F#11PAs a \"mission support section\" ……\x01",
            "More than anything as yourself!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Lloyd's")

    AnonymousTalk(
        0xFF,
        "#4SYes……!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    StopSound(132, 490, 40)
    StopSound(112, 490, 40)
    FadeToDark(2000, 0, -1)
    Sleep(500)
    StopSound(497, 1500, 50)
    StopSound(496, 1500, 50)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x84)
    OP_24(0x70)
    Sleep(2000)
    OP_29(0xB1, 0x1, 0xF)
    OP_29(0xB1, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_11231")
    OP_E0(0x33, 0x0)
    OP_E0(0x80, 0x0)
    Sleep(500)

    label("loc_11231")

    OP_E5(0x3)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_CF06 end

    def Function_71_11240(): pass

    label("Function_71_11240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11264")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_71_11240")

    label("loc_11264")

    Return()

    # Function_71_11240 end

    def Function_72_11265(): pass

    label("Function_72_11265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1127F")
    OP_FC(0x1)
    Jump("loc_112C8")

    label("loc_1127F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11299")
    OP_FC(0x2)
    Jump("loc_112C8")

    label("loc_11299")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112B3")
    OP_FC(0x1)
    Jump("loc_112C8")

    label("loc_112B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112C8")
    OP_FC(0x2)

    label("loc_112C8")

    Sleep(1)
    Return()

    # Function_72_11265 end

    def Function_73_112CC(): pass

    label("Function_73_112CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112E6")
    OP_FC(0x6)
    Jump("loc_1132F")

    label("loc_112E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11300")
    OP_FC(0x6)
    Jump("loc_1132F")

    label("loc_11300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1131A")
    OP_FC(0xB)
    Jump("loc_1132F")

    label("loc_1131A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1132F")
    OP_FC(0x5)

    label("loc_1132F")

    Sleep(1)
    Return()

    # Function_73_112CC end

    def Function_74_11333(): pass

    label("Function_74_11333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1134D")
    OP_FC(0xB)
    Jump("loc_11396")

    label("loc_1134D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11367")
    OP_FC(0xB)
    Jump("loc_11396")

    label("loc_11367")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11381")
    OP_FC(0x6)
    Jump("loc_11396")

    label("loc_11381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11396")
    OP_FC(0x6)

    label("loc_11396")

    Sleep(1)
    Return()

    # Function_74_11333 end

    def Function_75_1139A(): pass

    label("Function_75_1139A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113B4")
    OP_FC(0x1)
    Jump("loc_113FD")

    label("loc_113B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113CE")
    OP_FC(0x2)
    Jump("loc_113FD")

    label("loc_113CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113E8")
    OP_FC(0x1)
    Jump("loc_113FD")

    label("loc_113E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_113FD")
    OP_FC(0x2)

    label("loc_113FD")

    Sleep(1)
    Return()

    # Function_75_1139A end

    def Function_76_11401(): pass

    label("Function_76_11401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1141B")
    OP_FC(0x1)
    Jump("loc_11464")

    label("loc_1141B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11435")
    OP_FC(0x2)
    Jump("loc_11464")

    label("loc_11435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1144F")
    OP_FC(0x1)
    Jump("loc_11464")

    label("loc_1144F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11464")
    OP_FC(0x2)

    label("loc_11464")

    Sleep(1)
    Return()

    # Function_76_11401 end

    def Function_77_11468(): pass

    label("Function_77_11468")

    Sound(905, 0, 100, 0)
    Sound(904, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x0)
    Sound(951, 0, 100, 0)
    OP_24(0x388)
    Return()

    # Function_77_11468 end

    def Function_78_114AA(): pass

    label("Function_78_114AA")

    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4E2, 0x4F6, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x4F6, 0x51E, 0x0, 0x20)
    Return()

    # Function_78_114AA end

    def Function_79_114CC(): pass

    label("Function_79_114CC")

    OP_71(0xD, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xD)
    OP_71(0xD, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_79_114CC end

    def Function_80_114E8(): pass

    label("Function_80_114E8")

    OP_71(0xE, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_80_114E8 end

    def Function_81_11504(): pass

    label("Function_81_11504")

    OP_71(0xF, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xF)
    OP_71(0xF, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_81_11504 end

    def Function_82_11520(): pass

    label("Function_82_11520")

    OP_71(0x10, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_82_11520 end

    def Function_83_1153C(): pass

    label("Function_83_1153C")

    OP_71(0x11, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x11)
    OP_71(0x11, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_83_1153C end

    def Function_84_11558(): pass

    label("Function_84_11558")

    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x12)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_84_11558 end

    def Function_85_1157C(): pass

    label("Function_85_1157C")

    OP_75(0xD, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_85_1157C end

    def Function_86_11587(): pass

    label("Function_86_11587")

    OP_75(0xE, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_86_11587 end

    def Function_87_11592(): pass

    label("Function_87_11592")

    OP_75(0xF, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_87_11592 end

    def Function_88_1159D(): pass

    label("Function_88_1159D")

    OP_75(0x10, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_88_1159D end

    def Function_89_115A8(): pass

    label("Function_89_115A8")

    OP_75(0x11, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_89_115A8 end

    def Function_90_115B3(): pass

    label("Function_90_115B3")

    OP_75(0x12, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_90_115B3 end

    def Function_91_115BE(): pass

    label("Function_91_115BE")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(200)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(200)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(200)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_91_115BE end

    def Function_92_11639(): pass

    label("Function_92_11639")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EventEnd(0x5)
    SetCameraDistance(13000, 0)
    Return()

    # Function_92_11639 end

    def Function_93_11651(): pass

    label("Function_93_11651")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 0)
    OP_65(0x0, 0x1)
    EventEnd(0x3)
    Return()

    # Function_93_11651 end

    def Function_94_116B2(): pass

    label("Function_94_116B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch30000.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -800, 0, -16900, 180)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 800, 0, -16900, 180)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -1800, 0, -19500, 45)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 3700, 0, -17500, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -17000, 180)
    ClearMapObjFlags(0x16, 0x4)
    OP_68(0, 900, -19000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_94_116B2 end

    SaveToFile()

Try(main)
