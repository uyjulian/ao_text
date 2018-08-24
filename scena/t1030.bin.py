from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "Tio",                    # 1
        "Zeit",                   # 2
        "Sully",                  # 3
        "Michey",                 # 4
        "MWL Staff",              # 5
        "MWL Staff",              # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Melson",                 # 13
        "Corona",                 # 14
        "Rimah",                  # 15
        "Staffer Hanks",          # 16
        "Divine Wolf Zeit",       # 17
        "Jaeger",                 # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Jaeger",                 # 21
        "Jaeger",                 # 22
        "Jaeger",                 # 23
        "Jaeger",                 # 24
        "Jaeger",                 # 25
        "Father",                 # 26
        "Mother",                 # 27
        "Boy",                    # 28
        "Cryptid",                # 29
        "SE制御",                 # 30
        "bt1030",                 # 31
        "To Hotel Delphinia",     # 32
        "To Theme Park",          # 33
    ))

    ATBonus("ATBonus_5B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_674", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_658", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_65C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_660", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_664", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_668", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_66C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_694", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bt1030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_674", "MonsterBattlePostion_654", "ed7454", "ed7453", "ATBonus_5B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02702.itc",                   # 01
        "chr/ch10100.itc",                   # 02
        "chr/ch28100.itc",                   # 03
        "chr/ch10200.itc",                   # 04
        "chr/ch44500.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32400.itc",                   # 07
        "chr/ch24200.itc",                   # 08
        "chr/ch24300.itc",                   # 09
        "chr/ch24600.itc",                   # 0A
        "chr/ch24700.itc",                   # 0B
        "chr/ch26200.itc",                   # 0C
        "chr/ch22700.itc",                   # 0D
        "chr/ch20700.itc",                   # 0E
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(360,     4159,    4294951456, 180,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294963296, 4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4750,    4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294953796, 4000,    4294960796, 270,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294953796, 4000,    4294961796, 180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294961157, 4000,    4294951956, 90,   389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       4159,    4294951456, 180,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966247, 4000,    4294950526, 45,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(600,     4000,    4294950067, 315,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(7699,    4000,    4294965777, 135,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9159,    4000,    4294965537, 270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(7889,    4000,    4294964227, 0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294959026, 4000,    389,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 20,  0.0,                   -28.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  9.333333969116211,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 38,  0.0,                   2.5,                   3.4000000953674316,    100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -1.25,                 -0.6800000071525574,   1.0])

    DeclActor(4294953126, 4000,    4294961256, 1200,    4294953126, 5500,    4294961256, 0x007C, 0,  39, 0x0000)
    DeclActor(4294960646, 4000,    1550,    1200,    4294960646, 5500,    1550,    0x007C, 0,  40, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "To Hotel Delphinia")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "To Theme Park")

    ChipFrameInfo(1916, 0)                                       # 0

    ScpFunction((
        "Function_0_77C",          # 00, 0
        "Function_1_82C",          # 01, 1
        "Function_2_A27",          # 02, 2
        "Function_3_BA2",          # 03, 3
        "Function_4_C3B",          # 04, 4
        "Function_5_CDD",          # 05, 5
        "Function_6_D58",          # 06, 6
        "Function_7_1007",         # 07, 7
        "Function_8_11A4",         # 08, 8
        "Function_9_1436",         # 09, 9
        "Function_10_1535",        # 0A, 10
        "Function_11_15DF",        # 0B, 11
        "Function_12_1675",        # 0C, 12
        "Function_13_171D",        # 0D, 13
        "Function_14_17DD",        # 0E, 14
        "Function_15_185B",        # 0F, 15
        "Function_16_19DD",        # 10, 16
        "Function_17_1A7B",        # 11, 17
        "Function_18_1B1F",        # 12, 18
        "Function_19_1B26",        # 13, 19
        "Function_20_26EA",        # 14, 20
        "Function_21_2C91",        # 15, 21
        "Function_22_2CB6",        # 16, 22
        "Function_23_316D",        # 17, 23
        "Function_24_3189",        # 18, 24
        "Function_25_3962",        # 19, 25
        "Function_26_3A61",        # 1A, 26
        "Function_27_3C42",        # 1B, 27
        "Function_28_3C73",        # 1C, 28
        "Function_29_3C9F",        # 1D, 29
        "Function_30_3FF0",        # 1E, 30
        "Function_31_4D68",        # 1F, 31
        "Function_32_581C",        # 20, 32
        "Function_33_5845",        # 21, 33
        "Function_34_586E",        # 22, 34
        "Function_35_5897",        # 23, 35
        "Function_36_5898",        # 24, 36
        "Function_37_5899",        # 25, 37
        "Function_38_58BF",        # 26, 38
        "Function_39_5B33",        # 27, 39
        "Function_40_5BAF",        # 28, 40
    ))


    def Function_0_77C(): pass

    label("Function_0_77C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7B4"),
        (1, "loc_7C0"),
        (2, "loc_7CC"),
        (3, "loc_7D8"),
        (4, "loc_7E4"),
        (5, "loc_7F0"),
        (6, "loc_7FC"),
        (SWITCH_DEFAULT, "loc_808"),
    )


    label("loc_7B4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7C0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7CC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7D8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7E4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7F0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_808")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_814")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_82B")

    Return()

    # Function_0_77C end

    def Function_1_82C(): pass

    label("Function_1_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_840")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)
    Jump("loc_886")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_857")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 1)
    Event(0, 31)
    Jump("loc_886")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_86B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 30)
    Jump("loc_886")

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_886")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_886")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AC")
    ClearChrFlags(0x17, 0x80)

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_A26")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_8C8")
    Jump("loc_A26")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_A26")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8E4")
    Jump("loc_A26")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_968")
    SetChrPos(0x8, -7400, 4000, -11000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -6400, 4000, -10000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -8600, 4000, -11000, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -3940, 1730, -25670, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A26")

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9AA")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 1910, -25230, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A26")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9B8")
    Jump("loc_A26")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A1D")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -6040, 4000, -16340, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_A26")

    label("loc_A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A26")

    label("loc_A26")

    Return()

    # Function_1_82C end

    def Function_2_A27(): pass

    label("Function_2_A27")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A65")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)
    Jump("loc_A77")

    label("loc_A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A77")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A77")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB1")
    SetMapObjFrame(0xFF, "t1030_water", 0x2, "loop_off")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEC")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    SoundLoad(918)
    BeginChrThread(0x25, 3, 0, 37)
    Jump("loc_B1F")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B19")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    Jump("loc_B1F")

    label("loc_B19")

    Sound(821, 1, 40, 0)

    label("loc_B1F")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B58")
    ModifyEventFlags(0, 1, 0x80)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B7F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_BA1")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BA1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_BA1")

    Return()

    # Function_2_A27 end

    def Function_3_BA2(): pass

    label("Function_3_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB9")
    Call(0, 19)
    Return()

    label("loc_BB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BCA")
    Jump("loc_C37")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_C37")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BE6")
    Jump("loc_C37")

    label("loc_BE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_BF6")
    Jump("loc_C37")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C04")
    Jump("loc_C37")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C12")
    Jump("loc_C37")

    label("loc_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_C37")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C2E")
    Jump("loc_C37")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_C37")

    label("loc_C37")

    TalkEnd(0xFE)
    Return()

    # Function_3_BA2 end

    def Function_4_C3B(): pass

    label("Function_4_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C52")
    Call(0, 19)
    Return()

    label("loc_C52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C63")
    Jump("loc_CD9")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C71")
    Jump("loc_CD9")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C7F")
    Jump("loc_CD9")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_CA6")

    ChrTalk(
        0x9,
        "#01200F...Grrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD9")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CB4")
    Jump("loc_CD9")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_CC2")
    Jump("loc_CD9")

    label("loc_CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CD0")
    Jump("loc_CD9")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_CD9")

    label("loc_CD9")

    TalkEnd(0xFE)
    Return()

    # Function_4_C3B end

    def Function_5_CDD(): pass

    label("Function_5_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF4")
    Call(0, 19)
    Return()

    label("loc_CF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D05")
    Jump("loc_D54")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D13")
    Jump("loc_D54")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D21")
    Jump("loc_D54")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D2F")
    Jump("loc_D54")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D3D")
    Jump("loc_D54")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_D4B")
    Jump("loc_D54")

    label("loc_D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D54")

    label("loc_D54")

    TalkEnd(0xFE)
    Return()

    # Function_5_CDD end

    def Function_6_D58(): pass

    label("Function_6_D58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D69")
    Jump("loc_1003")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D77")
    Jump("loc_1003")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E83")

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hello! Welcome to\x01",
            "Wonderland.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi. Have fun,\x01",
            "okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOh, it's Mishy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWe should've brought\x01",
            "PeTiote huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, we'll be here again\x01",
            "this afternoon, so won't she\x01",
            "be looking forward to it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1003")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F90")

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "By the way, mister, is\x01",
            "it just you boys today?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "It's fine though! I'm sure\x01",
            "you'll enjoy Wonderland even if\x01",
            "you don't have a girlfriend♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi. Have fun,\x01",
            "okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(...Somehow, that makes\x01",
            "me extremely sad,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1003")

    label("loc_F90")


    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'm sure you'll enjoy\x01",
            "Wonderland even if you\x01",
            "don't have a girlfriend♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi. Have fun,\x01",
            "okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1003")

    TalkEnd(0xFE)
    Return()

    # Function_6_D58 end

    def Function_7_1007(): pass

    label("Function_7_1007")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1018")
    Jump("loc_11A0")

    label("loc_1018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10CE")

    ChrTalk(
        0xC,
        (
            "The kids in front of the signboard\x01",
            "over there seem to have been talking\x01",
            "about Mishy for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. As Wonderland\x01",
            "staff member, that makes\x01",
            "me happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A0")

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1160")

    ChrTalk(
        0xC,
        (
            "Welcome to the theme\x01",
            "park, the pride of\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Our latest attraction is\x01",
            "very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't miss it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11A0")

    label("loc_1160")


    ChrTalk(
        0xC,
        (
            "Our latest attraction is\x01",
            "very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't miss it!\x02",
    )

    CloseMessageWindow()

    label("loc_11A0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1007 end

    def Function_8_11A4(): pass

    label("Function_8_11A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11B5")
    Jump("loc_1432")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1256")

    ChrTalk(
        0xD,
        (
            "If you're looking for Mishy,\x01",
            "he's currently wandering\x01",
            "around inside the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you see him, please\x01",
            "feel free to ask him for\x01",
            "a picture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1432")

    label("loc_1256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")

    ChrTalk(
        0xD,
        (
            "Lately, kicking Mishy's\x01",
            "butt is in vogue among\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It started as a trivial prank, but lately it\x01",
            "seems there's even a rumor going around\x01",
            "saying, "If you kick him, you'll get lucky."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha. By all means,\x01",
            "please let your little\x01",
            "child kick Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-In short, even the\x01",
            "staff is in on this...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1432")

    label("loc_13B2")


    ChrTalk(
        0xD,
        (
            "Lately, kicking Mishy's\x01",
            "butt is in vogue among\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha. By all means,\x01",
            "please let your little\x01",
            "child kick Mishy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1432")

    TalkEnd(0xFE)
    Return()

    # Function_8_11A4 end

    def Function_9_1436(): pass

    label("Function_9_1436")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1447")
    Jump("loc_1531")

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(
        0xE,
        "Wooow, this is M.W.L...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I guess I'll enter now\x01",
            "and party hard!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1531")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1531")

    ChrTalk(
        0xE,
        (
            "Planning is important\x01",
            "when touring the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My girlfriend and I have to\x01",
            "come up with a solid plan\x01",
            "to see as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1531")

    TalkEnd(0xFE)
    Return()

    # Function_9_1436 end

    def Function_10_1535(): pass

    label("Function_10_1535")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1546")
    Jump("loc_15DB")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1554")
    Jump("loc_15DB")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15DB")

    ChrTalk(
        0xF,
        (
            "Geez, enough of that,\x01",
            "can't we go in already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The longer we stay here,\x01",
            "the less time we'll have\x01",
            "to enjoy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DB")

    TalkEnd(0xFE)
    Return()

    # Function_10_1535 end

    def Function_11_15DF(): pass

    label("Function_11_15DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_1671")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15FE")
    Jump("loc_1671")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1671")

    ChrTalk(
        0x10,
        (
            "Oh, isn't that Mishy\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Alright, daddy will take\x01",
            "a picture for you, so\x01",
            "stand near him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1671")

    TalkEnd(0xFE)
    Return()

    # Function_11_15DF end

    def Function_12_1675(): pass

    label("Function_12_1675")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1686")
    Jump("loc_1719")

    label("loc_1686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1710")

    ChrTalk(
        0x11,
        (
            "It looks like Mishy\x01",
            "entered the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Alllright. If that's how\x01",
            "it is, mom will get fired\x01",
            "up and look for him too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1719")

    label("loc_1710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1719")

    label("loc_1719")

    TalkEnd(0xFE)
    Return()

    # Function_12_1675 end

    def Function_13_171D(): pass

    label("Function_13_171D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_172E")
    Jump("loc_17D9")

    label("loc_172E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17A9")

    ChrTalk(
        0x12,
        (
            "I... Today I'll kick\x01",
            "Mishy for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you do that, you'll\x01",
            "get lucky, they say.\x01",
            "Mishy is amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D9")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_17D9")

    ChrTalk(
        0x12,
        (
            "Yaay, it's Mishy! The\x01",
            "real Mishy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D9")

    TalkEnd(0xFE)
    Return()

    # Function_13_171D end

    def Function_14_17DD(): pass

    label("Function_14_17DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17EE")
    Jump("loc_1857")

    label("loc_17EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_184E")

    ChrTalk(
        0x13,
        (
            "Noo, kicking him... Poor\x01",
            "Mishy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Even if they'll let you\x01",
            "do it, I won't!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_184E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1857")

    label("loc_1857")

    TalkEnd(0xFE)
    Return()

    # Function_14_17DD end

    def Function_15_185B(): pass

    label("Function_15_185B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_186C")
    Jump("loc_19D9")

    label("loc_186C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_187A")
    Jump("loc_19D9")

    label("loc_187A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1888")
    Jump("loc_19D9")

    label("loc_1888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_19D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192D")
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x14,
        (
            "Well then, we're finally\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Alright Rimah and Corona.\x01",
            "Should we enter the theme\x01",
            "park immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Agreeed!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0x16, 0xFF)
    Jump("loc_19CB")

    label("loc_192D")


    ChrTalk(
        0x14,
        (
            "I bought day passes for\x01",
            "us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I've got to give Rimah and Corona plenty\x01",
            "of fun today to make up for the trouble\x01",
            "I'm always putting them through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CB")

    Jump("loc_19D9")

    label("loc_19D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_19D9")

    label("loc_19D9")

    TalkEnd(0xFE)
    Return()

    # Function_15_185B end

    def Function_16_19DD(): pass

    label("Function_16_19DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19EE")
    Jump("loc_1A77")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_19FC")
    Jump("loc_1A77")

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A0A")
    Jump("loc_1A77")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1A6E")

    ChrTalk(
        0x15,
        (
            "I wonder what it's like\x01",
            "inside the park...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, I'm looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_1A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1A77")

    label("loc_1A77")

    TalkEnd(0xFE)
    Return()

    # Function_16_19DD end

    def Function_17_1A7B(): pass

    label("Function_17_1A7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1A8C")
    Jump("loc_1B1B")

    label("loc_1A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A9A")
    Jump("loc_1B1B")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1AA8")
    Jump("loc_1B1B")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B12")

    ChrTalk(
        0x16,
        (
            "Today you'll see, I'm\x01",
            "gonna play with mama and\x01",
            "papa all day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Haha. I can't wait!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B1B")

    label("loc_1B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1B1B")

    label("loc_1B1B")

    TalkEnd(0xFE)
    Return()

    # Function_17_1A7B end

    def Function_18_1B1F(): pass

    label("Function_18_1B1F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_18_1B1F end

    def Function_19_1B26(): pass

    label("Function_19_1B26")

    EventBegin(0x0)
    Fade(500)
    OP_68(-8000, 5000, -11750, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(24000, 1500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrPos(0x101, -8600, 4000, -12500, 0)
    SetChrPos(0x153, -7400, 4000, -12500, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")

    ChrTalk(
        0x153,
        (
            "#01110F#6PEhehe, sorry for the\x01",
            "wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00202F#11PLloyd, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14000F#11P...Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PWoof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1F60")

    ChrTalk(
        0x101,
        (
            "#00009F#6PTio, you're here\x01",
            "already?\x02\x03",
            "#00002FThanks for your help\x01",
            "back there. You were a\x01",
            "lifesaver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00211F#11PI was a little\x01",
            "embarrassed, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PUgh, that was my fault.\x01",
            "I wasn't strong\x01",
            "enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00203F#11PNo, you don't need to\x01",
            "apologize.\x02\x03",
            "#00202FIt turned out all right\x01",
            "in the end, so please\x01",
            "don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04205F#5POh yeah, it seems like you guys\x01",
            "went to the beach just now...\x01",
            "What was that all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PI-It was nothing.\x01",
            "Hahaha...\x02\x03",
            "#00000FT-That aside, it looks\x01",
            "like there's no one else\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PYes, we came a little\x01",
            "early.\x02\x03",
            "#00202FI was just lecturing\x01",
            "Sully on Mishy's\x01",
            "cuteness.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#14011F#5PN-No, that's not it, you\x01",
            "know!?\x02\x03",
            "#14012FI don't think he's cute\x01",
            "in the slightest─\x02\x03",
            "#14006FHey, don't change the\x01",
            "subject!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A8")

    label("loc_1F60")


    ChrTalk(
        0x101,
        (
            "#00009F#6PHey, so you got here\x01",
            "first.\x02\x03",
            "#00002FIt looks like no one\x01",
            "else is here yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PIt's because we're here\x01",
            "a little early.\x02\x03",
            "#00202FI was just lecturing\x01",
            "Sully on Mishy's\x01",
            "cuteness.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#14011F#5PN-No, that's not it, you\x01",
            "know!?\x02\x03",
            "#14012FI don't think he's cute\x01",
            "in the slightest─\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A8")

    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#00203F#12PEven if you try to deceive\x01",
            "me, it's useless.\x02\x03",
            "#00202FI've been detecting a certain\x01",
            ""aura of interest" from you\x01",
            "for quite a while, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14011F#5PWhat aura are you\x01",
            "talking about!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#6PEhehe, they're getting\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P(Hmm. Should I wait here\x01",
            "for the others?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x145, 3)
    Jump("loc_22EB")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_2252")

    ChrTalk(
        0x8,
        (
            "#00202F#11P...Thanks for your help\x01",
            "earlier.\x02\x03",
            "Will you guys wait here\x01",
            "for the others?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228A")

    label("loc_2252")


    ChrTalk(
        0x8,
        (
            "#00200F#11PWill you guys wait here\x01",
            "for the others?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228A")


    ChrTalk(
        0xA,
        (
            "#14000F#11PYou're already here, so\x01",
            "keep us company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P(Hmm. What should I do?)\x02",
    )

    CloseMessageWindow()

    label("loc_22EB")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[I Have Other Things to Do]\x01",      # 0
            "[Wait Here for the Others]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2362"),
        (0, "loc_2616"),
        (SWITCH_DEFAULT, "loc_26E9"),
    )


    label("loc_2362")


    def lambda_2367():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2367)
    Sleep(50)

    def lambda_2377():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2377)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x8,
        (
            "#00203F#11PIn that case, I'll explain\x01",
            "it to you guys too.\x02\x03",
            "#00201FJust how much Mishy's\x01",
            "adorableness has contributed\x01",
            "to continental peace!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F#6PYeah!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)

    ChrTalk(
        0xA,
        "#14011F#5PT-There's more!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#14007F#11PHey, don't just watch!\x01",
            "Stop her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Just give up.\x02\x03",
            "#00012FTio is completely taken\x01",
            "in by Mishy, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14006F#11PYou're in give up mode\x01",
            "already!?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Soon, the others who enjoyed\x01",
            "their shopping arrived at the\x01",
            "meeting place.\x02\x03",
            "Lloyd and the others showed their\x01",
            "entry passes to the receptionist\x01",
            "and entered the theme park.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x52, 0xFF)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_26E9")

    label("loc_2616")


    def lambda_261B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_261B)
    Sleep(50)

    def lambda_262B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_262B)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x8,
        (
            "#00200F#11PThere's not much time,\x01",
            "so hurry back after you\x01",
            "finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003F#11PHmph... Get back here\x01",
            "quick, alright?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -8000, 4000, -12500, 0)
    EventEnd(0x5)
    Jump("loc_26E9")

    label("loc_26E9")

    Return()

    # Function_19_1B26 end

    def Function_20_26EA(): pass

    label("Function_20_26EA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\cr036301.eff")
    OP_90(0x101, -4000, 5000, -30300, 0)
    OP_90(0x102, -4900, 5000, -31000, 0)
    OP_90(0x103, -3100, 5000, -31200, 0)
    OP_90(0x104, -4000, 5000, -32000, 0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x1, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4000, 3000, -26000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(16500, 2500)

    def lambda_2845():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2845)
    Sleep(100)

    def lambda_285D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_285D)
    Sleep(100)

    def lambda_2875():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2875)
    Sleep(100)

    def lambda_288D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_288D)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00207F#6P─Rising spiritual\x01",
            "pressure detected!\x01",
            "Please watch out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PWhat...!?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(0, 6150, -17000, 2500)
    MoveCamera(330, 20, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetCameraDistance(17500, 3000)
    Sound(919, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x24, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)

    def lambda_29C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_29C4)
    OP_75(0x0, 0x2, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x0)
    OP_6F(0x79)
    OP_68(-760, 4750, -26040, 2000)
    MoveCamera(336, 3, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(16870, 2000)
    Sleep(1500)
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00110F#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PThe monster that\x01",
            "appeared in the\x01",
            "Marshlands!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_71(0x0, 0x40, 0x63, 0x0, 0x8)
    Sound(842, 0, 100, 0)
    OP_82(0x64, 0x64, 0x1F40, 0x3E8)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    CancelBlur(1000)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Sleep(800)

    ChrTalk(
        0x103,
        (
            "#00207F#5PPresence of the higher\x01",
            "elements confirmed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#5PNo time to hesitate!\x01",
            "Let's take it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PAye sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#5PRoger!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x8)
    OP_79(0x0)
    ClearChrFlags(0x24, 0x1)
    BlurSwitch(0x2BC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1850, 3450, -26400, 800)
    SetCameraDistance(13000, 750)
    Sound(809, 0, 100, 0)
    Sound(251, 0, 100, 0)
    OP_74(0x0, 0x10)
    OP_71(0x0, 0xE5, 0xF8, 0x0, 0x8)

    def lambda_2C54():
        OP_9D(0xFE, 0xFFFFF6D2, 0xB40, 0xFFFFA6FA, 0x708, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2C54)
    Sleep(600)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_694", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_20_26EA end

    def Function_21_2C91(): pass

    label("Function_21_2C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB5")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_21_2C91")

    label("loc_2CB5")

    Return()

    # Function_21_2C91 end

    def Function_22_2CB6(): pass

    label("Function_22_2CB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\bs000000.eff")
    LoadEffect(0x1, "battle\\bs000001.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, -4000, 5000, -21000, 45)
    OP_90(0x102, -5000, 5000, -22000, 45)
    OP_90(0x103, -3000, 5000, -22000, 45)
    OP_90(0x104, -4000, 5000, -23000, 45)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x2, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 6150, -17000, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    MoveCamera(330, 20, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BeginChrThread(0x24, 3, 0, 23)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_2ED1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2ED1)
    OP_75(0x0, 0x1, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0x24, 0x80)
    Sleep(500)
    OP_68(-4000, 4400, -22000, 3000)
    MoveCamera(0, 20, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)
    Fade(250)
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
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00310F#6PTch... Why did a Cryptid\x01",
            "show up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PI don't know...\x02\x03",
            "#00201FHowever, I think this\x01",
            "rising spiritual pressure\x01",
            "is connected to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PAlso, like with the Temple,\x01",
            "it might be related sound\x01",
            "of the bell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PKeA and Arios came to a\x01",
            "place like this...?\x02\x03",
            "#00013FIn any case, let's go\x01",
            "inside!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#1K#1PYes!\x02",
    )


    ChrTalk(
        0x103,
        "#00201F#1K#2PYes!\x02",
    )


    ChrTalk(
        0x104,
        "#00307F#1K#6PYeah!\x02",
    )

    Sound(2153, 255, 100, 0)
    Sound(2249, 255, 100, 1)
    Sound(2343, 255, 100, 2)
    OP_57(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -4000, 4000, -19000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 6)
    OP_29(0xAD, 0x1, 0x3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_22_2CB6 end

    def Function_23_316D(): pass

    label("Function_23_316D")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_23_316D end

    def Function_24_3189(): pass

    label("Function_24_3189")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41950.itc", 0x1E)
    LoadChrToIndex("chr/ch41951.itc", 0x1F)
    LoadChrToIndex("chr/ch41952.itc", 0x20)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(2953)
    SoundLoad(2954)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x106, 0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x19, -2500, 0, -32000, 0)
    SetChrPos(0x1A, -3300, 0, -33500, 0)
    SetChrPos(0x1B, -4100, 0, -31500, 0)
    SetChrPos(0x1C, -4900, 0, -33000, 0)
    SetChrPos(0x1D, 2500, 0, -33500, 315)
    SetChrPos(0x1E, 3300, 0, -32000, 315)
    SetChrPos(0x1F, 4100, 0, -33000, 315)
    SetChrPos(0x20, 4900, 0, -31500, 315)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_D5(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    OP_68(0, 8500, -17000, 0)
    MoveCamera(40, 38, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 7000, -17000, 2500)
    MoveCamera(0, -3, 0, 2500)
    SetCameraDistance(24000, 2500)
    Sound(913, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    BlurSwitch(0x5DC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x65, 0x8C, 0x0, 0x8)
    OP_79(0x1)
    CancelBlur(500)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x18, 0, 3900, -17000, 180)
    OP_68(0, 4550, -30000, 0)
    OP_68(0, 3550, -30000, 1500)
    MoveCamera(335, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    Sleep(500)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#5PUwooh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#11PThe Divine Wolf from the\x01",
            "report!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PDon't falter! Let's\x01",
            "cooperate and hunt him\x01",
            "down!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(180, 100, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetChrName("Jaegers")

    AnonymousTalk(
        0xFF,
        "#4SJaー!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_82(0x0, 0x64, 0xBB8, 0x1770)
    OP_68(0, 4550, -25000, 6000)
    MoveCamera(25, 0, 0, 6000)
    BeginChrThread(0x25, 1, 0, 28)
    BeginChrThread(0x19, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1A, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1B, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1C, 3, 0, 25)
    Sleep(50)
    OP_93(0x1D, 0x0, 0x0)
    BeginChrThread(0x1D, 3, 0, 25)
    Sleep(50)
    OP_93(0x1E, 0x0, 0x0)
    BeginChrThread(0x1E, 3, 0, 25)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 25)
    Sleep(50)
    OP_93(0x20, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x18, 0, 0, 26)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_68(-670, 8200, -20260, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Fade(250)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x1, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(40, 150, -1, -1)
    SetChrName("Divine Wolf Zeit")

    AnonymousTalk(
        0xFF,
        (
            "#2953V#3C#4S#40W#35AHm─ Impertinent, but\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetCameraDistance(11500, 500)
    Sleep(1000)
    SetMessageWindowPos(20, 150, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetChrName("Divine Wolf Zeit")

    AnonymousTalk(
        0xFF,
        (
            "#2954V#3C#5S#30W#40AIf that is the case, I\x01",
            "shall not hold back\x01",
            "either!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 7500, -20000, 1000)
    MoveCamera(25, 9, 0, 1000)
    SetCameraDistance(15000, 1000)
    EndChrThread(0x25, 0x1)
    Sound(913, 0, 100, 0)
    OP_82(0x0, 0x32, 0x1388, 0x3E8)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1E0, 0x1EA, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x118, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    OP_6F(0x79)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2000)
    OP_68(0, 7500, -28000, 500)
    MoveCamera(15, 0, 0, 500)
    SetCameraDistance(22000, 500)
    ClearChrFlags(0x18, 0x1)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x18, 3, 0, 27)
    Sleep(500)
    FadeToDark(500, 0, -1)
    StopSound(861, 1000, 50)
    StopSound(865, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3189 end

    def Function_25_3962(): pass

    label("Function_25_3962")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)

    label("loc_3990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A60")
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    Sleep(1000)
    Jump("loc_3990")

    label("loc_3A60")

    Return()

    # Function_25_3962 end

    def Function_26_3A61(): pass

    label("Function_26_3A61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C41")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3620, 4000, -18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 380, 2970, -22580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1120, 3400, -21510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3740, 4000, -18570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5270, 3340, -21650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 4550, 2940, -22640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3250, 4160, -14820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6190, 4000, -15970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_26_3A61")

    label("loc_3C41")

    Return()

    # Function_26_3A61 end

    def Function_27_3C42(): pass

    label("Function_27_3C42")


    def lambda_3C47():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFF6F78, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C47)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x1EA, 0x1EF, 0x64, 0x8)
    OP_79(0x1)
    Return()

    # Function_27_3C42 end

    def Function_28_3C73(): pass

    label("Function_28_3C73")

    Sleep(1200)
    Sound(861, 2, 60, 0)

    label("loc_3C7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C9E")
    Sound(865, 2, 60, 0)
    Sleep(1000)
    StopSound(865, 200, 50)
    Sleep(400)
    Jump("loc_3C7C")

    label("loc_3C9E")

    Return()

    # Function_28_3C73 end

    def Function_29_3C9F(): pass

    label("Function_29_3C9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 600, 0, -62250, 0)
    SetChrPos(0x153, -600, 0, -62250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3D43():
        OP_95(0xFE, 600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D43)

    def lambda_3D5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D5D)
    Sleep(200)

    def lambda_3D71():
        OP_95(0xFE, -600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3D71)

    def lambda_3D8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_3D8B)
    Sound(107, 0, 100, 0)
    SetCameraDistance(25000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x153, 2)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x153,
        "#01102FUwah!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    OP_25(0x335, 0x50)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_25(0x335, 0x28)
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#01109F#5PLloyd, this place is\x01",
            "amazing!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PYeah. I'm a little\x01",
            "excited too.\x02\x03",
            "#00000FNow then... Someone else\x01",
            "should be here too.\x02\x03",
            "In any case, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#5PYeah!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15B, 1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_29_3C9F end

    def Function_30_3FF0(): pass

    label("Function_30_3FF0")

    EventBegin(0x0)
    OP_4B(0x17, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5830, 7000, -1410, 0)
    MoveCamera(306, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -8720, 4000, -6130, 0)
    SetChrPos(0x102, -7550, 4000, -6410, 0)
    SetChrPos(0x103, -9480, 4000, -6890, 0)
    SetChrPos(0x104, -7960, 4000, -7290, 0)
    SetChrPos(0x109, -8800, 4000, -8240, 0)
    SetChrPos(0x105, -7400, 4000, -8240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            "#11P*sigh*, how troublesome.\x01",
            "And there's the morning\x01",
            "schedule too...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-6020, 6700, -2510, 3000)
    MoveCamera(310, 29, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20870, 3000)

    def lambda_4130():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4130)
    Sleep(50)

    def lambda_414D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_414D)
    Sleep(50)

    def lambda_416A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_416A)
    Sleep(50)

    def lambda_4187():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4187)
    Sleep(50)

    def lambda_41A4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41A4)
    Sleep(50)

    def lambda_41C1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41C1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000FUmm, excuse us. We're\x01",
            "the Special Support\x01",
            "Section.\x02\x03",
            "We saw your request and\x01",
            "came to inquire... Are\x01",
            "you Mr. Hanks?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "Oh, ohhh! You're the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Hmm, yes, hmm, hmm...\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "...Yes, your physique\x01",
            "seems to perfectly\x01",
            "match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FP-Physique...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FUmm, if you don't mind,\x01",
            "could you explain the\x01",
            "situation for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Ah, that's right! How\x01",
            "careless of me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...I'm sure you know\x01",
            ""Mishy".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes, as much as anyone\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FPeTiote is probably at the\x01",
            "enthusiast level...\x02\x03",
            "#00300FWell, I think there's hardly\x01",
            "anyone in Crossbell who\x01",
            "doesn't know him, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHas something happened\x01",
            "to that Mishy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Yeah, actually... We got\x01",
            "a certain call this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "The actor who has been playing\x01",
            "Mishy since the founding can't\x01",
            "come for some reason.\x02",
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
        0x109,
        (
            "#6P#10105F"Some reason"...? Was\x01",
            "there some kind of\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "A sudden stomach ache,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "He'll be able to come after\x01",
            "receiving some medicine at\x01",
            "St. Ursula Hospital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But it seems he'll never\x01",
            "make it in time for this\x01",
            "morning's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "And so, I want you all...\x01",
            "To put on Mishy's costume\x01",
            "and substitute for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FA substitute for\x01",
            "Mishy...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FWow... Sounds fun, huh?\x02\x03",
            "#00304FAlright, then I'll─!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Weeell, you won't quite\x01",
            "fit, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I think the serious-\x01",
            "looking one there will be\x01",
            "an almost perfect fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FM-Me!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#4S#00307F*ack*!!\x02\x03",
            "#00306FMy plan to flirt with\x01",
            "the tourist girls...!!\x02\x03",
            "#00310FDamn you, Lloyd...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FH-Hey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FThat's quite the\x01",
            "pretext...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Then... Are you taking\x01",
            "the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAll right, I accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "*sigh*, thank you. Then,\x01",
            "let's...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x103)
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00105F...Tio? What's wrong?\x01",
            "You've been silent...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49A4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49A4)
    Sleep(50)

    def lambda_49B4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49B4)
    Sleep(50)

    def lambda_49C4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_49C4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00205F...Costume... a person\x01",
            "inside... ...stomach\x01",
            "ache... ...medicine...\x02",
        )
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

    ChrTalk(
        0x109,
        (
            "#6P#10111F(She's acting\x01",
            "strange...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F(Well, I guess it's normal to\x01",
            "be shocked after hearing\x01",
            "backstage details like this?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00011F(I-I guess so...)\x02\x03",
            "#00012F...U-Umm... Tio?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203F...It's nothing.\x02\x03",
            "#00201FIf it is for Mishy's\x01",
            "sake, I will gladly\x01",
            "cooperate as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHaha, that's the spirit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F(I wonder is she's\x01",
            "really fine...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Are you done talking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Then, I'll guide you to\x01",
            "the locker room.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C76():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C76)
    Sleep(50)

    def lambda_4C86():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C86)
    Sleep(50)

    def lambda_4C96():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4C96)
    Sleep(50)

    def lambda_4CA6():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4CA6)
    Sleep(50)

    def lambda_4CB6():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4CB6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00012FAh... Y-Yes, please.\x02",
    )

    CloseMessageWindow()
    StopSound(821, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Theme Park Part-\x01",
            "Time Job]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x176, 4)
    SetScenarioFlags(0x22, 0)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_3FF0 end

    def Function_31_4D68(): pass

    label("Function_31_4D68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch20200.itc", 0x20)
    LoadChrToIndex("chr/ch20300.itc", 0x21)
    LoadChrToIndex("chr/ch23800.itc", 0x22)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x21)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x22)
    SetChrFlags(0x23, 0x8000)
    OP_52(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(3220, 7060, -19270, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19020, 0)
    SetChrPos(0x101, 360, 4160, -15840, 180)
    SetChrPos(0x103, -1060, 4140, -15840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)
    SetCameraDistance(17900, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F*sigh*... It's finally\x01",
            "started, eh? I wonder\x01",
            "how things will go...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F─Ah. Our first guests\x01",
            "are already here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3750, 7160, -21000, 5000)
    SetCameraDistance(19340, 5000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x21, -470, 480, -28790, 0)
    SetChrPos(0x22, 980, 480, -28800, 0)
    SetChrPos(0x23, 130, 1110, -27230, 0)

    def lambda_4F9A():
        OP_95(0xFE, 130, 4000, -16840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_4F9A)
    Sleep(50)

    def lambda_4FB7():
        OP_95(0xFE, -470, 4000, -18440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4FB7)
    Sleep(50)

    def lambda_4FD4():
        OP_95(0xFE, 980, 4000, -18640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4FD4)
    Sleep(50)

    def lambda_4FF1():
        OP_95(0xFE, -7890, 4000, -16239, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FF1)
    WaitChrThread(0x103, 1)

    def lambda_500F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_500F)
    WaitChrThread(0x23, 1)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x23,
        "Wow, it's Mishy!\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "Hey, it's Mishy! Is he\x01",
            "the real deal!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Haha, indeed he is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. If you're this\x01",
            "excited already, you\x01",
            "won't last, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x0, 0x3E8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    ChrTalk(
        0x23,
        (
            "Yaay, yaay! Mishy,\x01",
            "Mishy!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(U-Umm... How would\x01",
            "Mishy reply in this\x01",
            "situation?)\x07\x00\x02",
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
        0,
        (
            "Mishishi, have fun, alright?♪\x01",                        # 0
            "Buy your admission ticket over there, alright?♪\x01",      # 1
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
        (0, "loc_522A"),
        (1, "loc_5281"),
        (SWITCH_DEFAULT, "loc_52EF"),
    )


    label("loc_522A")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 5)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun,\x01",
            "alright?♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Yes, thank you, Mishy!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x1)
    Jump("loc_52EF")

    label("loc_5281")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun,\x01",
            "alright?♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x23,
        (
            "Y-Yes... Thank you,\x01",
            "Mishy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x2)
    Jump("loc_52EF")

    label("loc_52EF")

    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "Mom, dad! Let's go\x01",
            "inside already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Haha, alright, alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Let's have fun all day\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3220, 7060, -19270, 3000)
    MoveCamera(315, 20, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19020, 3000)
    BeginChrThread(0x23, 3, 0, 34)
    Sleep(50)
    BeginChrThread(0x22, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x21, 3, 0, 32)
    Sleep(50)

    def lambda_53B0():

        label("loc_53B0")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_53B0")

    QueueWorkItem2(0x101, 1, lambda_53B0)
    Sleep(300)

    def lambda_53C5():
        OP_95(0xFE, -1060, 4140, -15840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53C5)
    WaitChrThread(0x103, 1)

    def lambda_53E3():

        label("loc_53E3")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_53E3")

    QueueWorkItem2(0x103, 1, lambda_53E3)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x21, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D2")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202FPhew, I guess I got\x01",
            "through that one\x01",
            "somehow.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FNice, Lloyd.\x02\x03",
            "#05522FMishy's laugh was quite\x01",
            "natural too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FI-It's a little\x01",
            "embarrassing, though.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05529FMishishi♪\x02\x03",
            "#05526F...*cough*. When you get\x01",
            "used to it, it is no big\x01",
            "deal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FI-I underestimated you.\x01",
            "(I see, she's cute if\x01",
            "she acts normally...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FLet's keep up this pace.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5804")

    label("loc_55D2")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202FPhew, got through that\x01",
            "one somehow...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 360, 4300, -15840, 90, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Sound(2030, 255, 70, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FUgh!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x7EE)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F...No, you didn't.\x02\x03",
            "#05526FLloyd, Mishy is not an employee...\x01",
            "There is no "admission ticket",\x01",
            "right?\x02\x03",
            "#05521FAs a smiling character who invites\x01",
            "you into a dream world, that\x01",
            "expression is at a taboo level.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI-I'm sorry. (This sure\x01",
            "is tough...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FHonestly... Please do it\x01",
            "properly next time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5804")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4D68 end

    def Function_32_581C(): pass

    label("Function_32_581C")

    OP_97(0x21, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x21, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_32_581C end

    def Function_33_5845(): pass

    label("Function_33_5845")

    OP_97(0x22, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x22, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_33_5845 end

    def Function_34_586E(): pass

    label("Function_34_586E")

    OP_97(0x23, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x23, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_34_586E end

    def Function_35_5897(): pass

    label("Function_35_5897")

    Return()

    # Function_35_5897 end

    def Function_36_5898(): pass

    label("Function_36_5898")

    Return()

    # Function_36_5898 end

    def Function_37_5899(): pass

    label("Function_37_5899")

    Sleep(1000)

    label("loc_589C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58BE")
    Sound(918, 0, 40, 0)
    Sleep(2200)
    Sound(918, 0, 30, 0)
    Sleep(5000)
    Jump("loc_589C")

    label("loc_58BE")

    Return()

    # Function_37_5899 end

    def Function_38_58BF(): pass

    label("Function_38_58BF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599E")

    ChrTalk(
        0x101,
        (
            "#00000FThis is the way to the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, no need to be so\x01",
            "impatient. We're going there\x01",
            "this afternoon, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, for now let's head\x01",
            "to the beach!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A03")

    label("loc_599E")


    ChrTalk(
        0x101,
        (
            "#00000FWe're scheduled to visit the\x01",
            "theme park this afternoon. Let's\x01",
            "head to the beach for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC3")

    ChrTalk(
        0x153,
        (
            "#01105FSay, Lloyd. Are we going\x01",
            "ahead of everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, sorry. We can't\x01",
            "leave everyone behind.\x02\x03",
            "#00004FLet's wait for them\x01",
            "before going inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5B1E")

    label("loc_5AC3")


    ChrTalk(
        0x101,
        (
            "#00000FOops, we can't leave everyone\x01",
            "behind. Let's wait for them\x01",
            "before going inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B1E")

    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_38_58BF end

    def Function_39_5B33(): pass

    label("Function_39_5B33")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sketch map of the\x01",
            "theme park.\x02\x03",
            "There are various\x01",
            "attractions lined up\x01",
            "across its vast grounds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_39_5B33 end

    def Function_40_5BAF(): pass

    label("Function_40_5BAF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～To Park Visitors～\x01",
            "In this theme park, reckless behavior and possession\x01",
            "of dangerous materials are prohibited. Also, we kindly\x01",
            "ask that children be accompanied by their guardians.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_40_5BAF end

    SaveToFile()

Try(main)
