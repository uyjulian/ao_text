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
        "M. W. L. Staff",         # 5
        "M. W. L. Staff",         # 6
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
        "Function_5_CE4",          # 05, 5
        "Function_6_D5F",          # 06, 6
        "Function_7_1024",         # 07, 7
        "Function_8_11FD",         # 08, 8
        "Function_9_1498",         # 09, 9
        "Function_10_15A3",        # 0A, 10
        "Function_11_1648",        # 0B, 11
        "Function_12_16E1",        # 0C, 12
        "Function_13_1794",        # 0D, 13
        "Function_14_185F",        # 0E, 14
        "Function_15_18D9",        # 0F, 15
        "Function_16_1A51",        # 10, 16
        "Function_17_1AF7",        # 11, 17
        "Function_18_1BAA",        # 12, 18
        "Function_19_1BB1",        # 13, 19
        "Function_20_27FA",        # 14, 20
        "Function_21_2DAB",        # 15, 21
        "Function_22_2DD0",        # 16, 22
        "Function_23_328C",        # 17, 23
        "Function_24_32A8",        # 18, 24
        "Function_25_3A77",        # 19, 25
        "Function_26_3B76",        # 1A, 26
        "Function_27_3D57",        # 1B, 27
        "Function_28_3D88",        # 1C, 28
        "Function_29_3DB4",        # 1D, 29
        "Function_30_4115",        # 1E, 30
        "Function_31_4EA3",        # 1F, 31
        "Function_32_5947",        # 20, 32
        "Function_33_5970",        # 21, 33
        "Function_34_5999",        # 22, 34
        "Function_35_59C2",        # 23, 35
        "Function_36_59C3",        # 24, 36
        "Function_37_59C4",        # 25, 37
        "Function_38_59EA",        # 26, 38
        "Function_39_5C4D",        # 27, 39
        "Function_40_5CE6",        # 28, 40
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
    Jump("loc_CE0")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C71")
    Jump("loc_CE0")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C7F")
    Jump("loc_CE0")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_CAD")

    ChrTalk(
        0x9,
        "#01200F......Grrrowl......\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CBB")
    Jump("loc_CE0")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_CC9")
    Jump("loc_CE0")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CD7")
    Jump("loc_CE0")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_CE0")

    label("loc_CE0")

    TalkEnd(0xFE)
    Return()

    # Function_4_C3B end

    def Function_5_CE4(): pass

    label("Function_5_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFB")
    Call(0, 19)
    Return()

    label("loc_CFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D0C")
    Jump("loc_D5B")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D1A")
    Jump("loc_D5B")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D28")
    Jump("loc_D5B")

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D36")
    Jump("loc_D5B")

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D44")
    Jump("loc_D5B")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_D52")
    Jump("loc_D5B")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D5B")

    label("loc_D5B")

    TalkEnd(0xFE)
    Return()

    # Function_5_CE4 end

    def Function_6_D5F(): pass

    label("Function_6_D5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D70")
    Jump("loc_1020")

    label("loc_D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D7E")
    Jump("loc_1020")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9C")

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hello!\x01",
            "Welcome to Wonderland.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun, alright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOoh, it's Michey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, we should've taken\x01",
            "peTiote with us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, we'll come again in the afternoon,\x01",
            "so won't she be looking forward to it?\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1020")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAA")

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "By the way, mister,\x01",
            "did you come with only men?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "It's fine though!\x01",
            "I'm sure you'll enjoy Wonderland\x01",
            "even if you don't have a girlfriend♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun, alright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(...Somehow it'll be\x01",
            "extremely sad, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1020")

    label("loc_FAA")


    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'm sure you'll enjoy Wonderland\x01",
            "even if you don't have a girlfriend♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun, alright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1020")

    TalkEnd(0xFE)
    Return()

    # Function_6_D5F end

    def Function_7_1024(): pass

    label("Function_7_1024")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1035")
    Jump("loc_11F9")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10F1")

    ChrTalk(
        0xC,
        (
            "The kids in front of the guide plate over\x01",
            "there seem to be talking lively about\x01",
            "Michey since some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uh uh, it somehow makes me\x01",
            "happy as a Wonderland Staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F9")

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")

    ChrTalk(
        0xC,
        (
            "Welcome to the theme park,\x01",
            "Michelam's pride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The latest newly introduced\x01",
            "attraction is greatly popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't miss it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11F9")

    label("loc_1192")


    ChrTalk(
        0xC,
        (
            "At the theme park,\x01",
            "The latest newly introduced\x01",
            "attraction is greatly popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't miss it!\x02",
    )

    CloseMessageWindow()

    label("loc_11F9")

    TalkEnd(0xFE)
    Return()

    # Function_7_1024 end

    def Function_8_11FD(): pass

    label("Function_8_11FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_120E")
    Jump("loc_1494")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(
        0xD,
        (
            "Michey? \x01",
            "He's currently wandering\x01",
            "around inside the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you see him, please feel free\x01",
            "to ask him for a picture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140D")

    ChrTalk(
        0xD,
        (
            "Lately, among the children\x01",
            "kicking Michey's butt is\x01",
            "in vogue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It started as a trivial prank, but lately it\x01",
            "seems there's even a rumor going around\x01",
            "saying that "if you kick him, you'll get lucky".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, by all means,\x01",
            "please let your little\x01",
            "child kick Michey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-In short, even the staff\x01",
            "is all in for this...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1494")

    label("loc_140D")


    ChrTalk(
        0xD,
        (
            "Lately, among the children\x01",
            "kicking Michey's butt is\x01",
            "in vogue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, by all means,\x01",
            "please let your little\x01",
            "child kick Michey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    TalkEnd(0xFE)
    Return()

    # Function_8_11FD end

    def Function_9_1498(): pass

    label("Function_9_1498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14A9")
    Jump("loc_159F")

    label("loc_14A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1501")

    ChrTalk(
        0xE,
        "Wooow, this is M.W.L...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I guess I'll enter now and party hard!\x02",
    )

    CloseMessageWindow()
    Jump("loc_159F")

    label("loc_1501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_159F")

    ChrTalk(
        0xE,
        (
            "As expected, planning is\x01",
            "important to tour the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My girlfriend and I must\x01",
            "come up with a solid plan\x01",
            "to tour as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1498 end

    def Function_10_15A3(): pass

    label("Function_10_15A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15B4")
    Jump("loc_1644")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15C2")
    Jump("loc_1644")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1644")

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
            "While we stay here like this, our\x01",
            "party time steadily decreases.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1644")

    TalkEnd(0xFE)
    Return()

    # Function_10_15A3 end

    def Function_11_1648(): pass

    label("Function_11_1648")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1659")
    Jump("loc_16DD")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1667")
    Jump("loc_16DD")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16DD")

    ChrTalk(
        0x10,
        (
            "Ooh, isn't it Michey\x01",
            "the one over there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Nice, dad will take\x01",
            "a picture for you,\x01",
            "so go near him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DD")

    TalkEnd(0xFE)
    Return()

    # Function_11_1648 end

    def Function_12_16E1(): pass

    label("Function_12_16E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16F2")
    Jump("loc_1790")

    label("loc_16F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1787")

    ChrTalk(
        0x11,
        (
            "It seems that Michey has\x01",
            "entered the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Ook, when things are like this,\x01",
            "mom will get fired up too and look for him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1790")

    label("loc_1787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1790")

    label("loc_1790")

    TalkEnd(0xFE)
    Return()

    # Function_12_16E1 end

    def Function_13_1794(): pass

    label("Function_13_1794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17A5")
    Jump("loc_185B")

    label("loc_17A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1829")

    ChrTalk(
        0x12,
        (
            "I...today I'll be kicking\x01",
            "Michey's for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you do that, you'll get lucky, they say.\x01",
            "Michey is amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185B")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_185B")

    ChrTalk(
        0x12,
        (
            "Yaay, it's Michey!\x01",
            "The real Michey!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185B")

    TalkEnd(0xFE)
    Return()

    # Function_13_1794 end

    def Function_14_185F(): pass

    label("Function_14_185F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1870")
    Jump("loc_18D5")

    label("loc_1870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(
        0x13,
        (
            "Noo, kicking him...\x01",
            "Poor Michey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If they'll let you do it,\x01",
            "I won't!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D5")

    label("loc_18CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_18D5")

    label("loc_18D5")

    TalkEnd(0xFE)
    Return()

    # Function_14_185F end

    def Function_15_18D9(): pass

    label("Function_15_18D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_18EA")
    Jump("loc_1A4D")

    label("loc_18EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_18F8")
    Jump("loc_1A4D")

    label("loc_18F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1906")
    Jump("loc_1A4D")

    label("loc_1906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A5")
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x14,
        "Well then, we're finally here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Ook, Rimah, Corona.\x01",
            "Should we enter the\x01",
            "theme park immediately?\x02",
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
    Jump("loc_1A3F")

    label("loc_19A5")


    ChrTalk(
        0x14,
        (
            "I bought all day long\x01",
            "valid passes for today.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I must make Rimah and Corona\x01",
            "have plenty of fun to compensate\x01",
            "for all I always put them through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3F")

    Jump("loc_1A4D")

    label("loc_1A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1A4D")

    label("loc_1A4D")

    TalkEnd(0xFE)
    Return()

    # Function_15_18D9 end

    def Function_16_1A51(): pass

    label("Function_16_1A51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1A62")
    Jump("loc_1AF3")

    label("loc_1A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A70")
    Jump("loc_1AF3")

    label("loc_1A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A7E")
    Jump("loc_1AF3")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1AEA")

    ChrTalk(
        0x15,
        (
            "I wonder what's going on\x01",
            "inside the theme park...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Uh uh, I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AF3")

    label("loc_1AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1AF3")

    label("loc_1AF3")

    TalkEnd(0xFE)
    Return()

    # Function_16_1A51 end

    def Function_17_1AF7(): pass

    label("Function_17_1AF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1B08")
    Jump("loc_1BA6")

    label("loc_1B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1B16")
    Jump("loc_1BA6")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1B24")
    Jump("loc_1BA6")

    label("loc_1B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B9D")

    ChrTalk(
        0x16,
        (
            "Today you see, I'll play all day long\x01",
            "at the theme park with papa and mama!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Uh uh, I can't wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA6")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1BA6")

    label("loc_1BA6")

    TalkEnd(0xFE)
    Return()

    # Function_17_1AF7 end

    def Function_18_1BAA(): pass

    label("Function_18_1BAA")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_18_1BAA end

    def Function_19_1BB1(): pass

    label("Function_19_1BB1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BC")

    ChrTalk(
        0x153,
        "#01110F#6PEheheh, sorry for the wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00202F#11PMr. Lloyd, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14000F#11P...Hi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#11PWoof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(
        0x101,
        (
            "#00009F#6PTio, you're here already?\x02\x03",
            "#00002FThank you for before.\x01",
            "You were a lifesaver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00211F#11P...I felt more or less\x01",
            "embarrassed, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PUgh...my apologies.\x01",
            "It's because I didn't put enough effort in it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00203F#11PNo, you don't have to \x01",
            "apologize at all, Mr. Lloyd.\x02\x03",
            "#00202FIt turned all right in the end,\x01",
            "so please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04205F#5PBy the way, it seemed to me\x01",
            "you were going to the beach before...\x01",
            "Has something happened there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No, ha ha ha...\x02\x03",
            "#00000FM-More importantly, it seems that\x01",
            "the others haven't gathered yet...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PYes, we ended up coming\x01",
            "a little earlier.\x02\x03",
            "#00202FI was just teaching Miss Sully\x01",
            "about Michey's cuteness.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#14011F#5PN-No, that's not it, you know!?\x02\x03",
            "#14012FI don't think he's cute\x01",
            "in the slightest──\x02\x03",
            "#14006FWait, don't change the subject!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2187")

    label("loc_202C")


    ChrTalk(
        0x101,
        (
            "#00009F#6PHi, did you come first?\x02\x03",
            "#00002FIt seems that the others\x01",
            "haven't gathered yet...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00204F#11PYes, we ended up coming\x01",
            "a little earlier.\x02\x03",
            "#00202FI was just teaching Miss Sully\x01",
            "about Michey's cuteness.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#14011F#5PN-No, that's not it, you know!?\x02\x03",
            "#14012FI don't think he's cute\x01",
            "in the slightest──\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2187")

    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#00203F#12PIt is no use even if you try to deceive.\x02\x03",
            "#00202FJust before I completely\x01",
            "sensed Miss Sully's\x01",
            ""it interests me aura".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14011F#5PWhat's that "aura" supposed to be!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109F#6PEheheh, you sure get along well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P(Uhm, I guess I'll wait\x01",
            "here for the others?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x145, 3)
    Jump("loc_23C1")

    label("loc_22BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_232E")

    ChrTalk(
        0x8,
        (
            "#00202F#11P...Thank you for all your\x01",
            "hard work before.\x02\x03",
            "Will you wait for\x01",
            "the others here too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_232E")


    ChrTalk(
        0x8,
        (
            "#00200F#11PWill you wait for\x01",
            "the others here too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2365")


    ChrTalk(
        0xA,
        "#14000F#11PYou're already here, so make us company.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P(Uuhm, what to do?)\x02",
    )

    CloseMessageWindow()

    label("loc_23C1")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[I Still Have Things to Do]\x01",      # 0
            "[Wait Here for the Others]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2438"),
        (0, "loc_2708"),
        (SWITCH_DEFAULT, "loc_27F9"),
    )


    label("loc_2438")


    def lambda_243D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_243D)
    Sleep(50)

    def lambda_244D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_244D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x8,
        (
            "#00203F#11PThen, I will tell\x01",
            "to you two too...\x02\x03",
            "#00201FHow Michey is indeed \x01",
            "contributing to Zemuria's \x01",
            "peace with his cuteness...!\x02",
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
        "#14011F#5PY-You're still going on!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#14007F#11PHey, don't just watch,\x01",
            "stop her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Well, just give up.\x02\x03",
            "#00012FTio is completely taken up\x01",
            "by Michey, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14006F#11PYou're in give up mode already!?\x02",
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
            "Soon, the others who were\x01",
            "enjoying shopping and the likes,\x01",
            "arrived at the meeting place.\x02\x03",
            "Lloyd and the others showed\x01",
            "their entry passes at the reception\x01",
            "and stepped into the theme park.\x07\x00\x02",
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
    Jump("loc_27F9")

    label("loc_2708")


    def lambda_270D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_270D)
    Sleep(50)

    def lambda_271D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_271D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x8,
        (
            "#00200F#11PPlease return quickly after you finish\x01",
            "your business, since there is not much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003F#11PHmph...\x01",
            "Come back immediately, got it?\x02",
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
    Jump("loc_27F9")

    label("loc_27F9")

    Return()

    # Function_19_1BB1 end

    def Function_20_27FA(): pass

    label("Function_20_27FA")

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

    def lambda_2955():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2955)
    Sleep(100)

    def lambda_296D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_296D)
    Sleep(100)

    def lambda_2985():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2985)
    Sleep(100)

    def lambda_299D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_299D)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00207F#6P──Perceiving spiritual pressure rising!\x01",
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

    def lambda_2AD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2AD8)
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
        "#00307F#5PThe monster that appeared in the Marshlands!?\x02",
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
            "#00207F#5PConfirmed the three higher\x01",
            "elements at work too...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#5PNo time to hesitate!\x01",
            "Let's attack it!\x02",
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

    def lambda_2D6E():
        OP_9D(0xFE, 0xFFFFF6D2, 0xB40, 0xFFFFA6FA, 0x708, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2D6E)
    Sleep(600)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_694", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_20_27FA end

    def Function_21_2DAB(): pass

    label("Function_21_2DAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DCF")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_21_2DAB")

    label("loc_2DCF")

    Return()

    # Function_21_2DAB end

    def Function_22_2DD0(): pass

    label("Function_22_2DD0")

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

    def lambda_2FEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2FEB)
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
            "#00310F#6PTch...why did a "Cryptid"\x01",
            "show up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PI don't know...\x02\x03",
            "#00201FHowever, I think this spiritual\x01",
            "pressure rising is connected to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PAlso, like with the "Temple",\x01",
            "it could be related to the\x01",
            "bell sounds too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PKeA and Mr. Arios\x01",
            "are in such a place...\x02\x03",
            "#00013FIn any case, let's go inside!\x02",
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

    # Function_22_2DD0 end

    def Function_23_328C(): pass

    label("Function_23_328C")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_23_328C end

    def Function_24_32A8(): pass

    label("Function_24_32A8")

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
        "#11PThe "Divine Wolf" of the report!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PDon't falter!\x01",
            "Let's cooperate and "hunt" him!\x02",
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
        "#2953V#3C#4S#40W#35AHm──impertinent, but fine.\x02",
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
            "#2954V#3C#5S#30W#40AIf that's the case,\x01",
            "I won't hold back too!\x02",
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

    # Function_24_32A8 end

    def Function_25_3A77(): pass

    label("Function_25_3A77")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)

    label("loc_3AA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B75")
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    Sleep(1000)
    Jump("loc_3AA5")

    label("loc_3B75")

    Return()

    # Function_25_3A77 end

    def Function_26_3B76(): pass

    label("Function_26_3B76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D56")
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
    Jump("Function_26_3B76")

    label("loc_3D56")

    Return()

    # Function_26_3B76 end

    def Function_27_3D57(): pass

    label("Function_27_3D57")


    def lambda_3D5C():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFF6F78, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D5C)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x1EA, 0x1EF, 0x64, 0x8)
    OP_79(0x1)
    Return()

    # Function_27_3D57 end

    def Function_28_3D88(): pass

    label("Function_28_3D88")

    Sleep(1200)
    Sound(861, 2, 60, 0)

    label("loc_3D91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB3")
    Sound(865, 2, 60, 0)
    Sleep(1000)
    StopSound(865, 200, 50)
    Sleep(400)
    Jump("loc_3D91")

    label("loc_3DB3")

    Return()

    # Function_28_3D88 end

    def Function_29_3DB4(): pass

    label("Function_29_3DB4")

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

    def lambda_3E58():
        OP_95(0xFE, 600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E58)

    def lambda_3E72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E72)
    Sleep(200)

    def lambda_3E86():
        OP_95(0xFE, -600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3E86)

    def lambda_3EA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_3EA0)
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
        "#01102FWow...!\x02",
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
        "#01109F#5P...Lloyd, somehow it seems amazing!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PYeah, I'm feeling a\x01",
            "little excited too.\x02\x03",
            "#00000FWell then...\x01",
            "Perhaps everyone\x01",
            "is already here.\x02\x03",
            "In any case, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#5PYup!\x02",
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

    # Function_29_3DB4 end

    def Function_30_4115(): pass

    label("Function_30_4115")

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

    def lambda_4255():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4255)
    Sleep(50)

    def lambda_4272():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4272)
    Sleep(50)

    def lambda_428F():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_428F)
    Sleep(50)

    def lambda_42AC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42AC)
    Sleep(50)

    def lambda_42C9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42C9)
    Sleep(50)

    def lambda_42E6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42E6)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, excuse us.\x01",
            "We're from the Special Support Section.\x02\x03",
            "We saw your request and came to inquire...\x01",
            "Are you Mr. Hanks?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "Ooh, ooh!\x01",
            "You're the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Hm, yes, hm hm...\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "...Yes, your physique seems\x01",
            "to perfectly match!\x02",
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
            "#6P#00100FExcuse us, could you tell us the\x01",
            "circumstances, if you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Ah, that's right!\x01",
            "How careless of me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...I'm sure you\x01",
            "know "Michey".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FYes, as much as anyone else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FPeTiote is probably\x01",
            "at the enthusiast level...\x02\x03",
            "#00300FWell, if you live in Crossbell,\x01",
            "I think there's hardly anyone\x01",
            "who doesn't know him, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHas something happened\x01",
            "to that Michey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Yeah, actually...\x01",
            "We got a certain call this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "The actor who has been playing\x01",
            "Michey since the founding can't\x01",
            "come due to some reason.\x02",
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
            "#6P#10105FReason...\x01",
            "Was there any problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "A sudden stomach ache, it seems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "It seems he'll be able to\x01",
            "come after receiving some\x01",
            "medicine at St. Ursula Hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But it seems he won't \x01",
            "make it in time at all for\x01",
            "the morning performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "And so, I want you...\x01",
            "To put on Michey's costume\x01",
            "and be a substitute-actor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMichey's substitute-actor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FEeh...\x01",
            "Sounds fun, huh?\x02\x03",
            "#00304FAlright, then I'll──!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Weeell, you don't\x01",
            "fit the size, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I think the serious-looking\x01",
            "one there should be almost\x01",
            "a perfect fit.\x02",
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
        "#6P#10112FThat's quite the pretext...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Then...\x01",
            "Are you accepting\x01",
            "the sidejob?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAll right,\x01",
            "I accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "*sigh*, thank you.\x01",
            "Then, let's...\x02",
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
            "#12P#00105F...Tio?\x01",
            "What's wrong? You've been silent...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4ADB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ADB)
    Sleep(50)

    def lambda_4AEB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4AEB)
    Sleep(50)

    def lambda_4AFB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4AFB)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00205F...Costume...a person inside...\x01",
            "...a stomach ache...medicine...\x02",
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
            "#6P#10111F(S-Somehow she's\x01",
            "acting strange...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F(Well, wouldn't it be normally\x01",
            "a shock being forced to hear\x01",
            "this much of an inside story?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00011F(I-I guess so...)\x02\x03",
            "#00012F...U-Uhm...Tio?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203F...It is nothing.\x02\x03",
            "#00201FIf it is for Michey's sake,\x01",
            "I will gladly cooperate too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHa ha, that's the spirit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006F(I wonder is she's really fine...)\x02",
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
            "Then, I'll guide you\x01",
            "to the locker room.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DB8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DB8)
    Sleep(50)

    def lambda_4DC8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4DC8)
    Sleep(50)

    def lambda_4DD8():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4DD8)
    Sleep(50)

    def lambda_4DE8():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DE8)
    Sleep(50)

    def lambda_4DF8():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4DF8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00012FAh...\x01",
            "Y-Yes, please.\x02",
        )
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
            "Quest [Theme Park Sidejob]\x07\x00",
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

    # Function_30_4115 end

    def Function_31_4EA3(): pass

    label("Function_31_4EA3")

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
            "#05206F*sigh*...\x01",
            "It's finally started, eh?\x01",
            "I wonder how things will go...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F──Ah.\x01",
            "One came at once.\x07\x00\x02",
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

    def lambda_50C6():
        OP_95(0xFE, 130, 4000, -16840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_50C6)
    Sleep(50)

    def lambda_50E3():
        OP_95(0xFE, -470, 4000, -18440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_50E3)
    Sleep(50)

    def lambda_5100():
        OP_95(0xFE, 980, 4000, -18640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5100)
    Sleep(50)

    def lambda_511D():
        OP_95(0xFE, -7890, 4000, -16239, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_511D)
    WaitChrThread(0x103, 1)

    def lambda_513B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_513B)
    WaitChrThread(0x23, 1)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x23,
        "Wow, it's Michey!\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "Hey, it's Michey!\x01",
            "Is he the real one!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Ha ha, yes, indeed he is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Uh uh, if you are so\x01",
            "in high spirits now,\x01",
            "you will get tired.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x0, 0x3E8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    ChrTalk(
        0x23,
        (
            "Yaay, yaay!\x01",
            "Michey, Michey!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(E-Eehm...\x01",
            "How would Michey reply\x01",
            "in such a situation?)\x07\x00\x02",
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
            "Mishishi, have fun, alright?♪\x01",                    # 0
            "Buy your entry ticket over there, alright?♪\x01",      # 1
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
        (0, "loc_535D"),
        (1, "loc_53B5"),
        (SWITCH_DEFAULT, "loc_5424"),
    )


    label("loc_535D")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 5)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun, alright?♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Yes, thank you, Michey!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x1)
    Jump("loc_5424")

    label("loc_53B5")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, have fun, alright?♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x23,
        (
            "Y-Yes...\x01",
            "Thank you, Michey.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x2)
    Jump("loc_5424")

    label("loc_5424")

    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "Father, mother, let's\x01",
            "go inside, fast...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Ha ha, alright, alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Let's have fun all day long.\x02",
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

    def lambda_54EA():

        label("loc_54EA")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_54EA")

    QueueWorkItem2(0x101, 1, lambda_54EA)
    Sleep(300)

    def lambda_54FF():
        OP_95(0xFE, -1060, 4140, -15840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54FF)
    WaitChrThread(0x103, 1)

    def lambda_551D():

        label("loc_551D")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_551D")

    QueueWorkItem2(0x103, 1, lambda_551D)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x21, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5700")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F*phew*, did it work somehow?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FNice, Mr. Lloyd.\x02\x03",
            "#05522FMichey's laugh was\x01",
            "quite natural too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FI-It's only a little\x01",
            "embarrassing, though.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05529FMishishi♪\x02\x03",
            "#05526F...*cough*.\x01",
            "When you get used to it,\x01",
            "it is no big deal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FI-I had underestimated you.\x01",
            "(I see, she's usually cute...)\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FLet's keep it up like this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_592F")

    label("loc_5700")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F*phew*, did it work someh...\x07\x00\x02",
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
            "#05531F...No it didn't.\x02\x03",
            "#05526FMr. Lloyd, Michey\x01",
            "is not an employee...\x01",
            "There is no "entry ticket", right?\x02\x03",
            "#05521FAs an existence that ushers you\x01",
            "in the world of dreams with a smile,\x01",
            "that expression is at a taboo level.\x07\x00\x02",
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
            "#05206FI-I'm sorry.\x01",
            "(She has frowned...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526FHonestly...\x01",
            "Please do it properly next time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_592F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4EA3 end

    def Function_32_5947(): pass

    label("Function_32_5947")

    OP_97(0x21, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x21, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_32_5947 end

    def Function_33_5970(): pass

    label("Function_33_5970")

    OP_97(0x22, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x22, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_33_5970 end

    def Function_34_5999(): pass

    label("Function_34_5999")

    OP_97(0x23, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x23, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_34_5999 end

    def Function_35_59C2(): pass

    label("Function_35_59C2")

    Return()

    # Function_35_59C2 end

    def Function_36_59C3(): pass

    label("Function_36_59C3")

    Return()

    # Function_36_59C3 end

    def Function_37_59C4(): pass

    label("Function_37_59C4")

    Sleep(1000)

    label("loc_59C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59E9")
    Sound(918, 0, 40, 0)
    Sleep(2200)
    Sound(918, 0, 30, 0)
    Sleep(5000)
    Jump("loc_59C7")

    label("loc_59E9")

    Return()

    # Function_37_59C4 end

    def Function_38_59EA(): pass

    label("Function_38_59EA")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ACC")

    ChrTalk(
        0x101,
        "#00000FThe theme park is over there, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, no need to be impatient,\x01",
            "we're going to have fun there in the afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, for now let's\x01",
            "head to the beach!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5B1A")

    label("loc_5ACC")


    ChrTalk(
        0x101,
        (
            "#00000FThe theme park is for the afternoon.\x01",
            "Let's head to the beach now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD7")

    ChrTalk(
        0x153,
        (
            "#01105FSay, Lloyd.\x01",
            "Are we going in first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, sorry. We can't steal\x01",
            "a march on the others.\x02\x03",
            "#00004FLet's wait for them before going inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5C38")

    label("loc_5BD7")


    ChrTalk(
        0x101,
        (
            "#00000FOops, we can't steal a march on the others.\x01",
            "Let's wait for them before going inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C38")

    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_38_59EA end

    def Function_39_5C4D(): pass

    label("Function_39_5C4D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a theme park\x01",
            "sketch drawn.\x02\x03",
            "It seems there are many kinds\x01",
            "of amusements attractions one\x01",
            "near the other on the large site.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_39_5C4D end

    def Function_40_5CE6(): pass

    label("Function_40_5CE6")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～To The Park Visitors～\x01\x01",
            "In this theme park, we firmly\x01",
            "do not accept acts of violence and\x01",
            "possession of dangerous materials.\x01\x01",
            "Also, we kindly ask that children must\x01",
            "be accompanied by their guardians.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_40_5CE6 end

    SaveToFile()

Try(main)
