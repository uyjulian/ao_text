from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1300.bin",                # FileName
        "t1300",                    # MapName
        "t1300",                    # Location
        0x00B6,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -10000, 0, 0, 1, 182, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1300",                  # 0
        "KeA",                    # 1
        "Fran",                   # 2
        "Cecil",                  # 3
        "Ilya",                   # 4
        "Rixia",                  # 5
        "Sully",                  # 6
        "Elie",                   # 7
        "Tio",                    # 8
        "Randy",                  # 9
        "Noｱl",                  # 10
        "Wazy",                   # 11
        "Zeit",                   # 12
        "Michey",                 # 13
        "Melson",                 # 14
        "Corona",                 # 15
        "Rimah",                  # 16
        "M. W. L. Staff",         # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Staffer Hanks",          # 23
        "Spectator",              # 24
        "Spectator",              # 25
        "Spectator",              # 26
        "Spectator",              # 27
        "Spectator",              # 28
        "Spectator",              # 29
        "Spectator",              # 30
        "Spectator",              # 31
        "Spectator",              # 32
        "Spectator",              # 33
        "Miichie",                # 34
        "Cryptid",                # 35
        "Cryptid",                # 36
        "Cryptid",                # 37
        "SE制御",                 # 38
        "bt1300",                 # 39
        "To Mirror Castle",       # 40
        "To Ferris Wheel",        # 41
        "To Haunted Coaster",     # 42
        "To Hotel Delphinia",     # 43
    ))

    ATBonus("ATBonus_64C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_70C", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_700", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_72C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88701.dat", "ms88801.dat", "ms88801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_70C", "MonsterBattlePostion_6EC", "ed7454", "ed7453", "ATBonus_64C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10100.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch00300.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch03000.itc",                   # 0A
        "chr/ch02710.itc",                   # 0B
        "chr/ch10200.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
        "chr/ch22700.itc",                   # 0E
        "chr/ch20700.itc",                   # 0F
        "chr/ch44500.itc",                   # 10
        "chr/ch24400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20200.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch23000.itc",                   # 15
        "apl/ch50387.itc",                   # 16
        "chr/ch00202.itc",                   # 17
        "chr/ch03002.itc",                   # 18
        "chr/ch07502.itc",                   # 19
        "chr/ch45400.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294963157, 0,       5000,    0,    389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294962307, 0,       4989,    0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294962597, 0,       7539,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(8369,    0,       5630,    225,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(500,     0,       4294956996, 270,  389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294966796, 0,       4294956996, 90,   389,  0x0, 0,   18,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5309,    0,       6300,    180,  389,  0x0, 0,   19,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(5119,    0,       4349,    45,   389,  0x0, 0,   20,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6190,    0,       5000,    270,  389,  0x0, 0,   21,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2029,    0,       3349,    180,  389,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 32,  0.0,                   -17.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.6666669845581055,    0.20000000298023224,   1.0])

    DeclActor(3030,    0,       3660,    1000,    2029,    1500,    3350,    0x007E, 0,  42, 0x0000)

    PlaceName(0.0, 0.0, 30.0, 0x0000, 0x0000, "To Mirror Castle")
    PlaceName(-40.0, 0.0, 10.0, 0x0000, 0x0000, "To Ferris Wheel")
    PlaceName(60.0, 0.0, 10.0, 0x0000, 0x0000, "To Haunted Coaster")
    PlaceName(0.0, 0.0, -80.0, 0x0000, 0x0000, "To Hotel Delphinia")
    PlaceName(10.0, 0.0, 10.0, 0x0000, 0x0053, "")

    ChipFrameInfo(2120, 0)                                       # 0

    ScpFunction((
        "Function_0_848",          # 00, 0
        "Function_1_900",          # 01, 1
        "Function_2_9BD",          # 02, 2
        "Function_3_D2F",          # 03, 3
        "Function_4_E0B",          # 04, 4
        "Function_5_109D",         # 05, 5
        "Function_6_114D",         # 06, 6
        "Function_7_1296",         # 07, 7
        "Function_8_1430",         # 08, 8
        "Function_9_15D7",         # 09, 9
        "Function_10_16D0",        # 0A, 10
        "Function_11_187F",        # 0B, 11
        "Function_12_199B",        # 0C, 12
        "Function_13_1A88",        # 0D, 13
        "Function_14_1BB6",        # 0E, 14
        "Function_15_1CA4",        # 0F, 15
        "Function_16_2247",        # 10, 16
        "Function_17_22DA",        # 11, 17
        "Function_18_237A",        # 12, 18
        "Function_19_245A",        # 13, 19
        "Function_20_2651",        # 14, 20
        "Function_21_26EC",        # 15, 21
        "Function_22_2746",        # 16, 22
        "Function_23_27D9",        # 17, 23
        "Function_24_2864",        # 18, 24
        "Function_25_28A8",        # 19, 25
        "Function_26_2B5F",        # 1A, 26
        "Function_27_2C50",        # 1B, 27
        "Function_28_2D66",        # 1C, 28
        "Function_29_4A61",        # 1D, 29
        "Function_30_4F60",        # 1E, 30
        "Function_31_4F77",        # 1F, 31
        "Function_32_4FE9",        # 20, 32
        "Function_33_55FF",        # 21, 33
        "Function_34_5624",        # 22, 34
        "Function_35_5B21",        # 23, 35
        "Function_36_5B54",        # 24, 36
        "Function_37_5B87",        # 25, 37
        "Function_38_5BBA",        # 26, 38
        "Function_39_5CD4",        # 27, 39
        "Function_40_5DE0",        # 28, 40
        "Function_41_5E7F",        # 29, 41
        "Function_42_5EBE",        # 2A, 42
        "Function_43_69A8",        # 2B, 43
        "Function_44_7191",        # 2C, 44
        "Function_45_8426",        # 2D, 45
        "Function_46_8443",        # 2E, 46
        "Function_47_8460",        # 2F, 47
        "Function_48_847D",        # 30, 48
        "Function_49_84F0",        # 31, 49
        "Function_50_8563",        # 32, 50
        "Function_51_8677",        # 33, 51
        "Function_52_878B",        # 34, 52
        "Function_53_87AA",        # 35, 53
    ))


    def Function_0_848(): pass

    label("Function_0_848")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_888"),
        (1, "loc_894"),
        (2, "loc_8A0"),
        (3, "loc_8AC"),
        (4, "loc_8B8"),
        (5, "loc_8C4"),
        (6, "loc_8D0"),
        (SWITCH_DEFAULT, "loc_8DC"),
    )


    label("loc_888")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_894")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8FF")

    Return()

    # Function_0_848 end

    def Function_1_900(): pass

    label("Function_1_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_90E")
    Jump("loc_97C")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_97C")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_97C")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_93B")
    Call(0, 25)
    Jump("loc_97C")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_949")
    Jump("loc_97C")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_97C")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_965")
    Jump("loc_97C")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_973")
    Jump("loc_97C")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_97C")

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_990")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_9BC")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_9AA")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 29)
    Jump("loc_9BC")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_9BC")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 5)
    Event(0, 44)

    label("loc_9BC")

    Return()

    # Function_1_900 end

    def Function_2_9BD(): pass

    label("Function_2_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)
    Jump("loc_9E9")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_A00")
    OP_24(0x7E)
    OP_24(0x335)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_ACB")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A1A")
    Sound(821, 1, 60, 0)
    OP_24(0x7E)
    ClearScenarioFlags(0x1, 5)
    Jump("loc_ACB")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A62")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    SoundLoad(918)
    BeginChrThread(0x2D, 3, 0, 53)
    Jump("loc_ACB")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A9C")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    Jump("loc_ACB")

    label("loc_A9C")

    Sound(821, 1, 60, 0)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)

    label("loc_ACB")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8E")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_C39")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_C39")

    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "back00", 0x2, "loop_off")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_CE8")

    label("loc_CBF")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_CE8")

    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x2, 0x0, 0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")
    OP_1B(0x0, 0x0, 0x28)

    label("loc_D01")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2E")
    OP_66(0x0, 0x1)

    label("loc_D2E")

    Return()

    # Function_2_9BD end

    def Function_3_D2F(): pass

    label("Function_3_D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D96")

    ChrTalk(
        0xE,
        (
            "#00102FHey Tio, \x01",
            "turn around.\x02\x03",
            "I'll take you a\x01",
            "picture now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DAF")

    label("loc_D96")


    ChrTalk(
        0xE,
        "#00102FOk, cheeese!\x02",
    )

    CloseMessageWindow()

    label("loc_DAF")

    Jump("loc_E07")

    label("loc_DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCA")
    Jump("loc_E07")

    label("loc_DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE0")
    Jump("loc_E07")

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF6")
    Jump("loc_E07")

    label("loc_DF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")

    label("loc_E07")

    TalkEnd(0xFE)
    Return()

    # Function_3_D2F end

    def Function_4_E0B(): pass

    label("Function_4_E0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E31")
    Call(0, 5)
    Jump("loc_EA8")

    label("loc_E31")


    ChrTalk(
        0xF,
        (
            "#00204FI have finally,\x01",
            "finally come to\x01",
            "the theme park...\x02\x03",
            "#00202F...In any case, I have to\x01",
            "shake Michey's hand...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA8")

    Jump("loc_1099")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC3")
    Jump("loc_1099")

    label("loc_EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED9")
    Jump("loc_1099")

    label("loc_ED9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEF")
    Jump("loc_1099")

    label("loc_EEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(
        0xF,
        (
            "#00203FWe can't stay here until\x01",
            "the night performance, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, in the evening we are to attend\x01",
            "the dinner party at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00206F...*haah*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(She looks disappointed...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1099")

    label("loc_FED")


    ChrTalk(
        0xF,
        (
            "#00200FIf possible, I would have\x01",
            "liked to see the Michey's\x01",
            "parade at the night performance.\x02\x03",
            "#00206F...Well, it seems I will have to\x01",
            "save it for the next time I come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    TalkEnd(0xFE)
    Return()

    # Function_4_E0B end

    def Function_5_109D(): pass

    label("Function_5_109D")

    OP_4B(0xF, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Yoo-hoo, young miss.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, are you having fun?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00201FThe real Michey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F(Ha ha, she really looks happy.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_5_109D end

    def Function_6_114D(): pass

    label("Function_6_114D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(
        0x10,
        (
            "#00303FWeeell then, I guess I'll treat myself\x01",
            "to pick up some ladies.\x02\x03",
            "#00309FI wonder where a lady who\x01",
            "suits my fancy could be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_123A")

    label("loc_11F9")


    ChrTalk(
        0x10,
        (
            "#00309FI wonder where a lady who\x01",
            "strikes my fancy could be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    Jump("loc_1292")

    label("loc_123F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    Jump("loc_1292")

    label("loc_1255")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    Jump("loc_1292")

    label("loc_126B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    Jump("loc_1292")

    label("loc_1281")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1292")

    label("loc_1292")

    TalkEnd(0xFE)
    Return()

    # Function_6_114D end

    def Function_7_1296(): pass

    label("Function_7_1296")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AF")
    Jump("loc_142C")

    label("loc_12AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136E")

    ChrTalk(
        0x11,
        (
            "#10105FNow that I think about it,\x01",
            "I spotted Michey but his little\x01",
            "sister "Miichie" is not around.\x02\x03",
            "#10103FUhhm, I wonder where\x01",
            "could she be hiding...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_13EA")

    label("loc_136E")


    ChrTalk(
        0x11,
        (
            "#10100FI wonder where "Miichie", \x01",
            "Michey's little sister, is?\x02\x03",
            "#10103FI wonder if I'll be able to find her eventually?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EA")

    Jump("loc_142C")

    label("loc_13EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1405")
    Jump("loc_142C")

    label("loc_1405")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141B")
    Jump("loc_142C")

    label("loc_141B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142C")

    label("loc_142C")

    TalkEnd(0xFE)
    Return()

    # Function_7_1296 end

    def Function_8_1430(): pass

    label("Function_8_1430")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1449")
    Jump("loc_15D3")

    label("loc_1449")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(
        0x12,
        (
            "#10300FJust before, Miss Ilya was dragging on\x01",
            "Miss Cecil from the rest area.\x02\x03",
            "#10303FHu hu, it seems that such a forcible method\x01",
            "is suitable for inviting girls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1591")

    label("loc_1512")


    ChrTalk(
        0x12,
        (
            "#10300FIt seems that Miss Ilya's forcible method\x01",
            "is suitable for inviting girls.\x02\x03",
            "#10309FHu hu, why don't you try it too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1591")

    Jump("loc_15D3")

    label("loc_1596")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AC")
    Jump("loc_15D3")

    label("loc_15AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    Jump("loc_15D3")

    label("loc_15C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D3")

    label("loc_15D3")

    TalkEnd(0xFE)
    Return()

    # Function_8_1430 end

    def Function_9_15D7(): pass

    label("Function_9_15D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_16CC")

    label("loc_15F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1606")
    Jump("loc_16CC")

    label("loc_1606")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    Jump("loc_16CC")

    label("loc_161C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BB")

    ChrTalk(
        0x8,
        (
            "#01111FOh, right, I must go\x01",
            "to buy Michey's goods\x01",
            "as present for Shizuku later.\x02\x03",
            "#01106FI wonder if my pocket money will be enough?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CC")

    label("loc_16CC")

    TalkEnd(0xFE)
    Return()

    # Function_9_15D7 end

    def Function_10_16D0(): pass

    label("Function_10_16D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E9")
    Jump("loc_187B")

    label("loc_16E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FF")
    Jump("loc_187B")

    label("loc_16FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1715")
    Jump("loc_187B")

    label("loc_1715")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CF")

    ChrTalk(
        0xA,
        (
            "#05900FI ran out of half of the\x01",
            "tickets I had already.\x02\x03",
            "#05902FUh uh, it was quick, since I tagged along\x01",
            "with everyone and rode many attractions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1865")

    label("loc_17CF")


    ChrTalk(
        0xA,
        (
            "#05900FI ran out of half of the\x01",
            "tickets I had already.\x02\x03",
            "#05903FIt looks like it will soon be evening...\x01",
            "I think I will go back to the rest area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1865")

    Jump("loc_187B")

    label("loc_186A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187B")

    label("loc_187B")

    TalkEnd(0xFE)
    Return()

    # Function_10_16D0 end

    def Function_11_187F(): pass

    label("Function_11_187F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1898")
    Jump("loc_1997")

    label("loc_1898")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AE")
    Jump("loc_1997")

    label("loc_18AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D1")
    Call(0, 12)
    Jump("loc_196B")

    label("loc_18D1")


    ChrTalk(
        0xB,
        (
            "#01705FSay, wasn't there any\x01",
            "attraction you liked,\x01",
            "I wonder?\x02\x03",
            "#01702FI like hopping on the thrilling\x01",
            "ones one after the other...\x01",
            "Got any suggestion?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196B")

    Jump("loc_1997")

    label("loc_1970")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1986")
    Jump("loc_1997")

    label("loc_1986")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1997")

    label("loc_1997")

    TalkEnd(0xFE)
    Return()

    # Function_11_187F end

    def Function_12_199B(): pass

    label("Function_12_199B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "#01700FRixia, Sully.\x01",
            "Are you having fun too?\x02\x03",
            "#01709FChanges of pace are \x01",
            "important for artists too, \x01",
            "so go all out today, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01809FHu hu, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#14003FH-Hmph, you don't\x01",
            "have to tell me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_199B end

    def Function_13_1A88(): pass

    label("Function_13_1A88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA1")
    Jump("loc_1BB2")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB7")
    Jump("loc_1BB2")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADA")
    Call(0, 12)
    Jump("loc_1B86")

    label("loc_1ADA")


    ChrTalk(
        0xC,
        (
            "#01805FNow that you mention it, nearby\x01",
            "the Horror Coaster you can\x01",
            "here many screams.\x02\x03",
            "#01803FCould there be something there\x01",
            "that could suit your tastes, Miss Ilya...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B86")

    Jump("loc_1BB2")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA1")
    Jump("loc_1BB2")

    label("loc_1BA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB2")

    label("loc_1BB2")

    TalkEnd(0xFE)
    Return()

    # Function_13_1A88 end

    def Function_14_1BB6(): pass

    label("Function_14_1BB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCF")
    Jump("loc_1CA0")

    label("loc_1BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE5")
    Jump("loc_1CA0")

    label("loc_1BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C08")
    Call(0, 12)
    Jump("loc_1C74")

    label("loc_1C08")


    ChrTalk(
        0xD,
        (
            "#14006FMore importantly,\x01",
            "somehow I've got hungry.\x02\x03",
            "#14000FWhy don't we get something at the rest area?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C74")

    Jump("loc_1CA0")

    label("loc_1C79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8F")
    Jump("loc_1CA0")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA0")

    label("loc_1CA0")

    TalkEnd(0xFE)
    Return()

    # Function_14_1BB6 end

    def Function_15_1CA4(): pass

    label("Function_15_1CA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCA")
    Call(0, 5)
    Jump("loc_1D18")

    label("loc_1CCA")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, welcome\x01",
            "to Wonderland!☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Have fun too, young man!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D18")

    Jump("loc_2243")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D33")
    Jump("loc_2243")

    label("loc_1D33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D49")
    Jump("loc_2243")

    label("loc_1D49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF8")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, I've heard what's going on.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Do your best and try to find\x01",
            "my little sister Miichie, ok?☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "...Or are you giving up?\x07\x00\x02",
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
            "[Don't give up]\x01",      # 0
            "[Give up]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF0")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I see.\x01",
            "Good luck, then☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I you can't figure where she is,\x01",
            "I'll personally tell Miichie\x01",
            "that you gave up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF3")

    label("loc_1EF0")

    Call(0, 43)

    label("loc_1EF3")

    Jump("loc_20ED")

    label("loc_1EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "You won at hide and seek\x01",
            "against Miichie, eh?0700}\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, that gift is\x01",
            "quite a nice thing,\x01",
            "please treasure it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20ED")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2055")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Don't feel down just\x01",
            "because you've lost at\x01",
            "hide and seek with Miichie.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Let's have fun with the attractions to your heart's\x01",
            "content and blow off the vexing feeling!☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20ED")

    label("loc_2055")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hey listen, haven't you seen a pink\x01",
            "colored girl who looks exactly like me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "She's my little sister...\x01",
            "Hmm, I wonder where she's gone?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20ED")

    Jump("loc_2243")

    label("loc_20F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B6")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, thank you!\x01",
            "I'll absolutely do my best!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Because there's still a little\x01",
            "time before evening, please\x01",
            "enjoy yourself until the end!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 0)
    Jump("loc_2243")

    label("loc_21B6")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "What I like the most is\x01",
            "the children's laughter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, incidentally,\x01",
            "what I like the most after\x01",
            "that are giant melons.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2243")

    TalkEnd(0xFE)
    Return()

    # Function_15_1CA4 end

    def Function_16_2247(): pass

    label("Function_16_2247")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2260")
    Jump("loc_22D6")

    label("loc_2260")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2276")
    Jump("loc_22D6")

    label("loc_2276")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228C")
    Jump("loc_22D6")

    label("loc_228C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A2")
    Jump("loc_22D6")

    label("loc_22A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(
        0xFE,
        "Aah...I'm really glad I came.\x02",
    )

    CloseMessageWindow()

    label("loc_22D6")

    TalkEnd(0xFE)
    Return()

    # Function_16_2247 end

    def Function_17_22DA(): pass

    label("Function_17_22DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F3")
    Jump("loc_2376")

    label("loc_22F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2309")
    Jump("loc_2376")

    label("loc_2309")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231F")
    Jump("loc_2376")

    label("loc_231F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2335")
    Jump("loc_2376")

    label("loc_2335")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(
        0xFE,
        (
            "Uh uh...look, honey.\x01",
            "Rimah looks so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2376")

    TalkEnd(0xFE)
    Return()

    # Function_17_22DA end

    def Function_18_237A(): pass

    label("Function_18_237A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2393")
    Jump("loc_2456")

    label("loc_2393")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A9")
    Jump("loc_2456")

    label("loc_23A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BF")
    Jump("loc_2456")

    label("loc_23BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D5")
    Jump("loc_2456")

    label("loc_23D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2456")

    ChrTalk(
        0xFE,
        "Yaay, Michey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rimah won't be around for the night performance, \x01",
            "but do your best with the parade, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    TalkEnd(0xFE)
    Return()

    # Function_18_237A end

    def Function_19_245A(): pass

    label("Function_19_245A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_24B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D7")
    OP_AF(0x6C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2648")

    label("loc_24D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EB")
    Jump("loc_2648")

    label("loc_24EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2503")
    TalkEnd(0xFE)
    Return()

    label("loc_2503")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2648")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B1")

    ChrTalk(
        0x18,
        (
            "Welcome!\x01",
            "Here we deal in a great number\x01",
            "of Michey's goods!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "You too, put on a Michey's tail\x01",
            "and enjoy the theme park!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2648")

    label("loc_25B1")


    ChrTalk(
        0x18,
        (
            "What about a Michey's goods\x01",
            "as a theme park's memory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "The people who return to\x01",
            "Crossbell City with a Michey's\x01",
            "tail on are surprisingly many.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2648")

    Jump("loc_2467")

    label("loc_264D")

    TalkEnd(0xFE)
    Return()

    # Function_19_245A end

    def Function_20_2651(): pass

    label("Function_20_2651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26A9")

    ChrTalk(
        0xFE,
        (
            "Let's go to the new attraction\x01",
            "they have made over there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E8")

    label("loc_26A9")


    ChrTalk(
        0xFE,
        (
            "Since we're here, let's stay\x01",
            "until the night performance!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E8")

    TalkEnd(0xFE)
    Return()

    # Function_20_2651 end

    def Function_21_26EC(): pass

    label("Function_21_26EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2722")

    ChrTalk(
        0xFE,
        "Where're we going next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_2722")


    ChrTalk(
        0xFE,
        "Are we going home already?\x02",
    )

    CloseMessageWindow()

    label("loc_2742")

    TalkEnd(0xFE)
    Return()

    # Function_21_26EC end

    def Function_22_2746(): pass

    label("Function_22_2746")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D5")

    ChrTalk(
        0xFE,
        (
            "We have a yearly free\x01",
            "pass for the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "M. W. L. is never boring, no matter \x01",
            "how many times we come!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_27D5")

    TalkEnd(0xFE)
    Return()

    # Function_22_2746 end

    def Function_23_27D9(): pass

    label("Function_23_27D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2860")

    ChrTalk(
        0xFE,
        (
            "This child really likes\x01",
            "Michey a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Coming many times here,\x01",
            "I too got completely addicted to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2860")

    label("loc_2860")

    TalkEnd(0xFE)
    Return()

    # Function_23_27D9 end

    def Function_24_2864(): pass

    label("Function_24_2864")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A4")

    ChrTalk(
        0xFE,
        (
            "Buy me, buy me,\x01",
            "buy me a plushie!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A4")

    label("loc_28A4")

    TalkEnd(0xFE)
    Return()

    # Function_24_2864 end

    def Function_25_28A8(): pass

    label("Function_25_28A8")

    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    SetChrFlags(0x29, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2963")
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xE, 0x16)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -5160, 0, 3100, 315)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7100, 0, 4400, 315)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6000, 0, -150, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -8010, 0, 5260, 135)
    SetChrFlags(0x14, 0x10)
    Jump("loc_2B5E")

    label("loc_2963")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B6")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -9350, 0, 6350, 135)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7930, 200, 8240, 135)
    SetChrChipByIndex(0x12, 0x18)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_2B5E")

    label("loc_29B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8320, 0, -2390, 180)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -7690, 0, -3590, 270)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -9110, 0, -3590, 90)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2B5E")

    label("loc_2A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7600, 0, -360, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xA, 0x19)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 0, -6210, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2AB0")
    SetChrFlags(0x8, 0x80)
    Jump("loc_2ABE")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_2ABE")
    SetChrFlags(0xA, 0x80)

    label("loc_2ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD9")
    ClearChrFlags(0x29, 0x80)

    label("loc_2AD9")

    Jump("loc_2B5E")

    label("loc_2ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5E")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xF, 0x17)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -4700, 0, 8680, 180)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)

    label("loc_2B5E")

    Return()

    # Function_25_28A8 end

    def Function_26_2B5F(): pass

    label("Function_26_2B5F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000F◆The ferris wheel and rest area are ahead.\x01",
            "Where should we go?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "Head to the Ferris Wheel\x01",      # 0
            "Head to the Rest Area\x01",         # 1
            "Quit\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C05"),
        (1, "loc_2C1E"),
        (SWITCH_DEFAULT, "loc_2C37"),
    )


    label("loc_2C05")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C4F")

    label("loc_2C1E")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C4F")

    label("loc_2C37")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Jump("loc_2C4F")

    label("loc_2C4F")

    Return()

    # Function_26_2B5F end

    def Function_27_2C50(): pass

    label("Function_27_2C50")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000F◆The Horror Coaster and fortune-telling \x01",
            "house are further ahead.\x01",
            "Where should we go?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "Head to the Horror Coaster\x01",             # 0
            "Head to the Fortune-telling House\x01",      # 1
            "Quit\x01",                                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D1B"),
        (1, "loc_2D34"),
        (SWITCH_DEFAULT, "loc_2D4D"),
    )


    label("loc_2D1B")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D65")

    label("loc_2D34")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D65")

    label("loc_2D4D")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Jump("loc_2D65")

    label("loc_2D65")

    Return()

    # Function_27_2C50 end

    def Function_28_2D66(): pass

    label("Function_28_2D66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x101, 0, 5000, -27000, 0)
    OP_90(0x8, -1280, 5000, -27940, 0)
    OP_90(0xF, 200, 5000, -28510, 0)
    OP_90(0xE, 1130, 5000, -28360, 0)
    OP_90(0xA, -1730, 5000, -29480, 0)
    OP_90(0xB, -650, 5000, -29360, 0)
    OP_90(0xD, 580, 5000, -29850, 0)
    OP_90(0xC, 1700, 5000, -29810, 0)
    OP_90(0x11, -340, 5000, -30690, 0)
    OP_90(0x9, -1340, 5000, -30960, 0)
    OP_90(0x12, 1010, 5000, -31210, 0)
    OP_90(0x10, -850, 5000, -32340, 0)
    OP_90(0x13, 400, 5000, -32700, 0)
    OP_68(0, 1800, -24500, 0)
    MoveCamera(0, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 9000, -500, 9000)
    MoveCamera(0, 3, 0, 9000)
    SetCameraDistance(66000, 9000)
    PlaceName2(340, 200, "c_plac46", 0x0, 5000)

    def lambda_2F67():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F67)

    def lambda_2F7C():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F7C)
    Sleep(50)

    def lambda_2F94():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2F94)

    def lambda_2FA9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2FA9)
    Sleep(50)

    def lambda_2FC1():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2FC1)

    def lambda_2FD6():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FD6)

    def lambda_2FEB():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2FEB)
    Sleep(50)

    def lambda_3003():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3003)

    def lambda_3018():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3018)

    def lambda_302D():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_302D)
    Sleep(50)

    def lambda_3045():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3045)

    def lambda_305A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_305A)

    def lambda_306F():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_306F)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, 0, 0)
    OP_68(0, 1000, -8000, 5500)
    MoveCamera(0, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 1)
    Sleep(300)
    Sound(3033, 255, 100, 0)

    ChrTalk(
        0x8,
        "#01109F#15A#4SWoooooow...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00002FSo this is M.W.L. (Michelam Wonderland)...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00203F.........(*moved to tears*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#14005F...A-Awesome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01705FEeh, it's the first time for me too...\x01",
            "It looks like we can have quite the fun, eh?\x02\x03",
            "#01709FThere's also quite a number\x01",
            "of attractions, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00309FWell, honestly there're so many that\x01",
            "you can't tour 'em all in just one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304FToday we spent time a the \x01",
            "beach until past noon...\x02\x03",
            "#10302FIt would seem better to go around\x01",
            "focusing on the representative ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05905FWhat could the representative\x01",
            "ones be, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06403FUhhm, as you can imagine, we can't leave out\x01",
            "the ferris wheel we can see on the left side...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(325, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#06409FIt's popular with both\x01",
            "families and couples.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#10109FAnd generally speaking, the view is great.\x02\x03",
            "#10102FIt could be a nice place even\x01",
            "if left for last as closing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01702FHm hm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01809FUh uh...\x01",
            "I'm feeling excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00102FAs for a representative one...\x01",
            "It seems to be the central "castle" for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        (
            "#00100FThe "Mirror Castle"──it seems it's \x01",
            "this theme park's monument-like place.\x02\x03",
            "#00104FThey say that a "Wish-Granting Mirror"\x01",
            "has been placed at the top floor...\x02\x03",
            "#00102FIt's said that when you ring the bell and stand\x01",
            "in front of the mirror, it grants your wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05909FMy, how romantic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00304FWell, it's expected it's visited\x01",
            "by many couples and families.\x02\x03",
            "#00300FAfter all, there're two handles there\x01",
            "on the left and right to ring that bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FI-It really sounds painful\x01",
            "to ring it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01101FHey hey!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(35, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#01110FIs anyone living on that\x01",
            "mansion you can see over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#14011FS-Somehow it's a very\x01",
            "eerie-looking mansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00305FI don't know that one too...\x01",
            "An attraction they recently made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06404FYes, it seems to be the newest\x01",
            "facility in the theme park.\x02\x03",
            "#06402FIt's the "Horror Coaster" and they\x01",
            "say it's quite the thing, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00204FI made some research about\x01",
            "that information too.\x02\x03",
            "#00202FIt seems to be a scary but exciting\x01",
            "attraction which takes full advantage\x01",
            "of the latest technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00106FT-They came up\x01",
            "with such a thing...\x02\x03",
            "#00111F...That Bell, she didn't tell\x01",
            "me anything about it...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -300, 0, -7000, 180)
    SetChrPos(0x8, -1280, 0, -7940, 135)
    SetChrPos(0xF, 200, 0, -8510, 180)
    SetChrPos(0xE, 1130, 0, -8360, 225)
    SetChrPos(0xA, -1730, 0, -9280, 90)
    SetChrPos(0xB, -750, 0, -9360, 90)
    SetChrPos(0xD, 580, 0, -9850, 270)
    SetChrPos(0xC, 1700, 0, -9810, 270)
    SetChrPos(0x11, -340, 0, -10940, 0)
    SetChrPos(0x9, -1340, 0, -10960, 45)
    SetChrPos(0x12, 1010, 0, -11210, 315)
    SetChrPos(0x10, -850, 0, -12340, 0)
    SetChrPos(0x13, 400, 0, -12700, 0)
    OP_68(0, 1500, -9600, 0)
    OP_68(0, 1000, -9600, 2000)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#01709FYes, yes, that's nice!\x01",
            "Now I'm excited.\x02\x03",
            "#01700FAny other staples I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304F#6PIt's not an attraction, but a staple one\x01",
            "is the "fortune-telling house" too.\x02\x03",
            "#10300FRumor goes that the fortune teller who joined\x01",
            "last year is quite remarkable, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06403FThe story goes that she does everything, from\x01",
            "affinity divination to looking for lost articles.\x02\x03",
            "#06400FThey say that she's an exotic,\x01",
            "mysterious and beautiful fortune teller.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01805F#12PThat...\x01",
            "Interests me a little.\x02\x03",
            "#01808F(Could she be a diviner of Eastern origins...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00203F...If you say that, then I\x01",
            "think that the chasing after\x01",
            ""Michey" can't be left out too.\x02\x03",
            "#00201FThe idea is to chase him while\x01",
            "he goes around the park.\x02\x03",
            "#00207FIf you are lucky, you can even \x01",
            "encounter a character called \x01",
            ""Miichie" who is his little sister...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00301F#6PPeTiote's eyes are serious...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#05905FBy the way...\x02\x03",
            "#05900FI wonder where could be\x01",
            "a place where we can rest?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x13B, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#10105F#6PAh, there's a rest area\x01",
            "to the left of the arcade.\x02\x03",
            "#10100FI think they serve\x01",
            "some light food too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1300, -9600, 1500)

    def lambda_4041():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4041)

    def lambda_404E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_404E)
    Sleep(50)

    def lambda_405E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_405E)

    def lambda_406B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_406B)
    Sleep(50)

    def lambda_407B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_407B)

    def lambda_4088():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4088)
    Sleep(50)

    def lambda_4098():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4098)

    def lambda_40A5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_40A5)
    Sleep(50)

    def lambda_40B5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_40B5)

    def lambda_40C2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_40C2)
    Sleep(50)

    def lambda_40D2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_40D2)

    def lambda_40DF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_40DF)

    def lambda_40EC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_40EC)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#05904FThen it could be good to keep\x01",
            "that as the center where to gather.\x02\x03",
            "#05902FBecause I will be around as much as\x01",
            "possible, come without hesitation\x01",
            "if you have anemia or feel bad, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PSister Cecil, you don't have to show\x01",
            "your nurse spirit even at such a time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00108F#12PYes, it would be a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00303F#6P...Still, thinkin' about it,\x01",
            "it could be the perfect chance\x01",
            "to get nursed by Miss Cecil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00211F#12PMr. Randy.\x01",
            "To be honest, you should hold back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01706F#11PWell, have some fun too, ok?\x01\x02\x03",
            "#01702FYou usually don't, so that's why you\x01",
            "must make merry on times like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05909FUh uh, I understand.\x01",
            "Then, I will do as you say.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, -9600, 1500)
    Sleep(500)

    def lambda_43F0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43F0)
    Sleep(50)

    def lambda_4400():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4400)
    Sleep(50)

    def lambda_4410():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4410)
    Sleep(50)

    def lambda_4420():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4420)
    Sleep(50)

    def lambda_4430():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4430)
    Sleep(50)

    def lambda_4440():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4440)
    Sleep(50)

    def lambda_4450():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4450)
    Sleep(50)

    def lambda_4460():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4460)
    Sleep(50)

    def lambda_4470():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4470)
    Sleep(50)

    def lambda_4480():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4480)
    Sleep(50)

    def lambda_4490():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_4490)
    Sleep(50)

    def lambda_44A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_44A0)
    Sleep(50)

    def lambda_44B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_44B0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#11P──Because we have the dinner party,\x01",
            "we can play around until evening...\x02\x03",
            "#00000FEveryone, I'll hand over your tickets\x01",
            "so from now on we move on our own.\x02\x03",
            "#00002FIf there's an attraction you want to enjoy,\x01",
            "everyone can enter with someone...\x02\x03",
            "What do you say about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00109F#6PYes, why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00204F#6PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01802F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00309F#6PAlright, let's party!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06409F#6PI'm so excited!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#10112F#6PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#10304F#6POh boy, so lively, eh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x8, 0x87, 0x1F4)
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#01109F#5PHey, Sully!\x01",
            "Why don't we go around together!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xD, 0x13B, 0x1F4)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        "#14011F#12PD-Don't pull already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01709F#6PAhaha, somehow it reminds\x01",
            "me when we were in school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05909F#6PUh uh, you are right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01203F#6PGrrrowl...woof.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x35D, 5)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At the theme park, you can enjoy\x01",
            "the "ferris wheel", "Mirror Castle",\x01",
            ""fortune-telling house" and "Horror Coaster".\x02\x03",
            "You can enjoy the attraction by selecting\x01",
            "a partner at each of their receptions and\x01",
            "spending 1 ticket.\x02\x03",
            "Please think well with whom and what\x01",
            "attractions you want to enjoy since the\x01",
            "story will advance after using all 5 tickets.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, -6750, 0)
    SetScenarioFlags(0x145, 4)
    OP_29(0xA5, 0x1, 0x6)
    EndChrThread(0x13, 0x3)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    OP_49()
    OP_D7(0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Call(0, 25)
    EventEnd(0x5)
    Return()

    # Function_28_2D66 end

    def Function_29_4A61(): pass

    label("Function_29_4A61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x8, 0, 0, -10000, 0)
    SetChrPos(0xF, -1000, 0, -10000, 0)
    SetChrPos(0x9, 1000, 0, -10000, 0)
    SetChrPos(0xA, -1500, 0, -11250, 0)
    SetChrPos(0xB, -500, 0, -11250, 0)
    SetChrPos(0xD, 500, 0, -11250, 0)
    SetChrPos(0xC, 1500, 0, -11250, 0)
    SetChrPos(0x11, -1000, 0, -12500, 0)
    SetChrPos(0xE, 0, 0, -12500, 0)
    SetChrPos(0x12, 1000, 0, -12500, 0)
    SetChrPos(0x10, -500, 0, -13750, 0)
    SetChrPos(0x101, 500, 0, -13750, 0)
    SetChrPos(0x13, -1500, 0, -15000, 0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrFlags(0xF, 0x8000)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, -7500, 180)
    OP_4B(0x18, 0xFF)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 1000, 0, -7000, 180)
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WThus──the fun time passed\x01",
            "in the blink of an eye.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-870, 1030, -9460, 0)
    MoveCamera(310, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    PlayBGM("ed7514", 0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x14, 0x0, 2300, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    SetCameraDistance(25000, 15000)
    OP_68(0, 1500, -12000, 15000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x10, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x11, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xA, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0xC, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 30)
    Sleep(250)
    BeginChrThread(0x9, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xF, 3, 0, 31)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#35A#40WLeaving reluctantly with the memory of the \x01",
            "night performance starting at the theme park...\x02\x03",
            "#35A#40WLloyd and the others briefly returned\x01",
            "to the hotel and decided to head to the \x01",
            "guest house where the dinner party was.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4A61 end

    def Function_30_4F60(): pass

    label("Function_30_4F60")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
    Return()

    # Function_30_4F60 end

    def Function_31_4F77(): pass

    label("Function_31_4F77")

    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x32C8, 0x7D0, 0x0)
    Return()

    # Function_31_4F77 end

    def Function_32_4FE9(): pass

    label("Function_32_4FE9")

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
    SetChrPos(0x101, 100, 0, -21000, 0)
    SetChrPos(0x102, 800, 0, -22100, 0)
    SetChrPos(0x103, -750, 0, -21900, 0)
    SetChrPos(0x104, -100, 0, -23000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x1, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x1, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20000, 4000)
    OP_6F(0x79)
    OP_68(0, 1000, -12000, 4500)
    MoveCamera(0, 20, 0, 4500)
    SetCameraDistance(15000, 4500)

    def lambda_51FA():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51FA)
    Sleep(100)

    def lambda_5212():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5212)
    Sleep(100)

    def lambda_522A():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_522A)
    Sleep(100)

    def lambda_5242():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5242)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#6PPleroma Grass...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PMichey's flower bed...!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x2A, 0, 0, 33)
    Sleep(1000)
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
    Sleep(300)
    Fade(1000)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(30, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(17500, 4000)
    MoveCamera(0, 20, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x2A, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_53D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_53D9)

    def lambda_53EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_53EA)

    def lambda_53FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_53FB)
    OP_75(0x1, 0x2, 0x3E8)
    OP_75(0x2, 0x2, 0x3E8)
    OP_75(0x3, 0x2, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x0)
    OP_6F(0x79)
    OP_68(0, 1600, -10150, 3000)
    MoveCamera(0, 14, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(1000)

    def lambda_5469():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5469)
    Sleep(50)

    def lambda_5481():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5481)
    Sleep(50)

    def lambda_5499():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5499)
    Sleep(50)

    def lambda_54B1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54B1)
    WaitChrThread(0x104, 1)
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
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00107F#12P#NThe one that appeared at the swamp...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#6P#NHah! Let's beat it!\x02",
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_74(0x2, 0x14)
    OP_74(0x3, 0x14)
    OP_71(0x1, 0x5B, 0x69, 0xFA, 0x8)
    OP_71(0x2, 0x8D, 0xA0, 0xFA, 0x8)
    OP_71(0x3, 0x8D, 0xA0, 0xFA, 0x8)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(8000, 1000)
    OP_74(0x1, 0x1E)
    OP_74(0x2, 0x1E)
    OP_74(0x3, 0x1E)
    OP_71(0x1, 0x69, 0x73, 0x0, 0x8)
    OP_71(0x2, 0xA1, 0xAA, 0x0, 0x8)
    OP_71(0x3, 0xA1, 0xAA, 0x0, 0x8)
    Sleep(500)
    Battle("BattleInfo_72C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 34)
    Return()

    # Function_32_4FE9 end

    def Function_33_55FF(): pass

    label("Function_33_55FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5623")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_33_55FF")

    label("loc_5623")

    Return()

    # Function_33_55FF end

    def Function_34_5624(): pass

    label("Function_34_5624")

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
    SetChrPos(0x101, 100, 0, -13000, 0)
    SetChrPos(0x102, 800, 0, -14100, 0)
    SetChrPos(0x103, -750, 0, -13900, 0)
    SetChrPos(0x104, -100, 0, -15000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x2, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x2, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(330, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    MoveCamera(0, 20, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0x2A, 0, 0, 33)
    BeginChrThread(0x2A, 3, 0, 35)
    BeginChrThread(0x2B, 3, 0, 36)
    BeginChrThread(0x2C, 3, 0, 37)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_58DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_58DA)

    def lambda_58EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_58EB)

    def lambda_58FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_58FC)
    OP_75(0x1, 0x1, 0x3E8)
    OP_75(0x2, 0x1, 0x3E8)
    OP_75(0x3, 0x1, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2C, 0x3)
    EndChrThread(0x2A, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    Sleep(500)
    OP_68(0, 1000, -11400, 3000)
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
        0x101,
        (
            "#00006F#5P...We encountered Campanella from\x01",
            "the "Society" before in this place...\x01\x02\x03",
            "#00013FThinking about it, KeA\x01",
            "too is just up ahead...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYes...\x01",
            "Maybe there's really something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PIt's useless to think about it...\x01",
            "We can only go and see for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PYes, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 0, 0, -10000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 7)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_34_5624 end

    def Function_35_5B21(): pass

    label("Function_35_5B21")

    OP_74(0x1, 0xF)

    label("loc_5B25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B53")
    OP_71(0x1, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_5B25")

    label("loc_5B53")

    Return()

    # Function_35_5B21 end

    def Function_36_5B54(): pass

    label("Function_36_5B54")

    OP_74(0x2, 0xF)

    label("loc_5B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B86")
    OP_71(0x2, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x2)
    OP_71(0x2, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x2)
    Jump("loc_5B58")

    label("loc_5B86")

    Return()

    # Function_36_5B54 end

    def Function_37_5B87(): pass

    label("Function_37_5B87")

    OP_74(0x3, 0xF)

    label("loc_5B8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BB9")
    OP_71(0x3, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x3)
    OP_71(0x3, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x3)
    Jump("loc_5B8B")

    label("loc_5BB9")

    Return()

    # Function_37_5B87 end

    def Function_38_5BBA(): pass

    label("Function_38_5BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5BDC")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    label("loc_5BDC")

    EventBegin(0x1)
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
            "#1KWhere do you want to move to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Horror Coaster\x01",             # 0
            "Fortune-telling House\x01",      # 1
            "Quit\x01",                       # 2
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
        (0, "loc_5C89"),
        (1, "loc_5CA2"),
        (2, "loc_5CBB"),
        (SWITCH_DEFAULT, "loc_5CC0"),
    )


    label("loc_5C89")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_5CC0")

    label("loc_5CA2")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_5CC0")

    label("loc_5CBB")

    Jump("loc_5CC0")

    label("loc_5CC0")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    # Function_38_5BBA end

    def Function_39_5CD4(): pass

    label("Function_39_5CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5CF6")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    label("loc_5CF6")

    EventBegin(0x1)
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
            "#1KWhere do you want to move to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Ferris Wheel\x01",      # 0
            "Rest Area\x01",         # 1
            "Quit\x01",              # 2
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
        (0, "loc_5D95"),
        (1, "loc_5DAE"),
        (2, "loc_5DC7"),
        (SWITCH_DEFAULT, "loc_5DCC"),
    )


    label("loc_5D95")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_5DCC")

    label("loc_5DAE")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_5DCC")

    label("loc_5DC7")

    Jump("loc_5DCC")

    label("loc_5DCC")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    # Function_39_5CD4 end

    def Function_40_5DE0(): pass

    label("Function_40_5DE0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, if I go this way\x01",
            "I'll exit out the theme park.\x02\x03",
            "Today I'll fully enjoy to my heart's\x01",
            "content M. W. L. with everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 3000, -55560, 0)
    EventEnd(0x4)
    Return()

    # Function_40_5DE0 end

    def Function_41_5E7F(): pass

    label("Function_41_5E7F")


    ChrTalk(
        0x101,
        (
            "#00000FWe have nothing to do there now.\x01",
            "...Let's not go.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_41_5E7F end

    def Function_42_5EBE(): pass

    label("Function_42_5EBE")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4930, 2500, 2360, 0)
    MoveCamera(323, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x101, 2160, 0, 5860, 180)
    SetChrPos(0xEF, 3750, 0, 5560, 225)
    OP_4B(0x29, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005FOh, you were here?\x02",
    )

    CloseMessageWindow()
    OP_9C(0x29, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x29, 0x101, 500)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4410, 2500, 5160, 0)
    MoveCamera(333, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x29, 2800, 0, 5760, 0)
    SetChrPos(0x101, 2970, 0, 8380, 180)
    SetChrPos(0xEF, 4120, 0, 7980, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mrr...maybe I have\x01",
            "underestimated you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "To have found me out not two but\x01",
            "even three times means that it's\x01",
            "impossible you were just lucky, yes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well...\x01",
            "Not really, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Aaalright. Now that things have come to this,\x01",
            "I'll hide seriously!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you won't be absolutely\x01",
            "able to find me next time!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6179():

        label("loc_6179")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_6179")

    QueueWorkItem2(0x101, 1, lambda_6179)

    def lambda_618B():

        label("loc_618B")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_618B")

    QueueWorkItem2(0xEF, 1, lambda_618B)
    SetChrFlags(0x29, 0x1000)
    OP_95(0x29, -550, 0, 6760, 5000, 0x0)
    OP_95(0x29, -5830, 0, 4550, 5000, 0x0)

    def lambda_61CA():
        OP_95(0xFE, -10560, 0, 4110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_61CA)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(3360, 2500, 6680, 0)
    MoveCamera(297, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12170, 0)
    SetChrPos(0x101, 1880, 0, 6910, 270)
    SetChrPos(0xEF, 2170, 0, 8550, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_62E7")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, somehow we could\x01",
            "find her for the second time.\x02\x03",
            "#00103FIt seems she said that she'll\x01",
            "do this seriously next time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_62E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_6370")

    ChrTalk(
        0x103,
        (
            "#00200FSomehow we could find her\x01",
            "for the second time too.\x02\x03",
            "#00203FShe said that she'll do this\x01",
            "seriously next time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_6402")

    ChrTalk(
        0x104,
        (
            "#00300FSomehow we could find her\x01",
            "for the second time too.\x02\x03",
            "#00303FIt seems she said that she'll\x01",
            "do this seriously next time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_6496")

    ChrTalk(
        0x109,
        (
            "#10100FUh uh, somehow we could\x01",
            "find her for the second time!\x02\x03",
            "#10103FShe said that she'll do this\x01",
            "seriously next time, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_6528")

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, somehow we could\x01",
            "find her for the second time.\x02\x03",
            "#10303FShe said that she'll do this\x01",
            "seriously next time, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_65C1")

    ChrTalk(
        0x153,
        (
            "#01109FAaalright, now we found\x01",
            "her for the second time!\x02\x03",
            "#01111FAlthough it seems she said that\x01",
            "next time she'll do this seriously...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_65C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6663")

    ChrTalk(
        0x156,
        (
            "#06400FUh uh, somehow we could\x01",
            "find her for the second time too.\x02\x03",
            "#06403FAlthough it seems she said that\x01",
            "next time she'll do this seriously...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_66FA")

    ChrTalk(
        0x14C,
        (
            "#05900FUh uh, somehow we could\x01",
            "find her for the second time.\x02\x03",
            "#05904FAlthough she said that she\x01",
            "will do this seriously next time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6787")

    ChrTalk(
        0x134,
        (
            "#01700FHu hu, the second time too\x01",
            "was as easy as pie.\x02\x03",
            "#01705FShe said that she'll do this\x01",
            "seriously next time, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_6787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_681F")

    ChrTalk(
        0x135,
        (
            "#01802FUh uh, somehow we could\x01",
            "find her for the second time too.\x02\x03",
            "#01805FShe said that she'll do this\x01",
            "seriously next time, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689F")

    label("loc_681F")


    ChrTalk(
        0x166,
        (
            "#14000FSomehow we could find\x01",
            "her for the second time too.\x02\x03",
            "#14006FShe said that she'll do this\x01",
            "seriously next time, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_689F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6910")

    ChrTalk(
        0x101,
        (
            "#00006FI feel a little uneasy,\x01",
            "but let's look for her.\x02\x03",
            "#00000FI wonder where she went now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6973")

    label("loc_6910")


    ChrTalk(
        0x101,
        (
            "#00006FI feel a little uneasy,\x01",
            "but let's look for her.\x02\x03",
            "#00000FI wonder where she went now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6973")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xC)
    SetScenarioFlags(0x1C9, 4)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -20, 0, 8600, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_42_5EBE end

    def Function_43_69A8(): pass

    label("Function_43_69A8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1060, 2500, -8580, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    OP_93(0x14, 0xB4, 0x0)
    SetChrPos(0x101, -510, 0, -7920, 0)
    SetChrPos(0xEF, 530, 0, -7970, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I see...well, it can't be helped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'll inform Miichie.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "You can go back to\x01",
            "enjoy yourselves, ok?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FYeah, sorry about it, but we leave it to you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_6B47")

    ChrTalk(
        0x102,
        (
            "#00106FWell, we didn't find her so\x01",
            "there's nothing we can do...\x02\x03",
            "#00100FThen, I'm going.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_6BC4")

    ChrTalk(
        0x103,
        (
            "#00206FWe couldn't find her no matter what,\x01",
            "so it can't be helped...\x02\x03",
            "#00200FThen, I will excuse myself.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_6C31")

    ChrTalk(
        0x104,
        (
            "#00306FWell, we couldn't find her,\x01",
            "so it can't be helped.\x02\x03",
            "#00300FThen, I guess I'll go.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_6CA6")

    ChrTalk(
        0x109,
        (
            "#10106FWell, we couldn't find her,\x01",
            "so there's nothing to do about it...\x02\x03",
            "#10100FThen, I'm going.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_6D0F")

    ChrTalk(
        0x105,
        (
            "#10306FWell, we didn't find her,\x01",
            "so it can't be helped.\x02\x03",
            "#10300FThen, I too will go.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_6D8D")

    ChrTalk(
        0x153,
        (
            "#01106FBoo, we gave our best\x01",
            "but couldn't find her.\x02\x03",
            "#01100FWell, fine.\x01",
            "KeA will go play at another place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6E02")

    ChrTalk(
        0x156,
        (
            "#06406FWell, we couldn't find her\x01",
            "so it can't be helped...\x02\x03",
            "#06400FThen, it's time for me to go.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_6E7C")

    ChrTalk(
        0x14C,
        (
            "#05906FWell, we didn't find her, so\x01",
            "we can't do anything about it.\x02\x03",
            "#05900FThen, I believe I will go.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6F0C")

    ChrTalk(
        0x134,
        (
            "#01706FHmm, I wanted to find her, but...\x01",
            "Well, it's no use I guess.\x02\x03",
            "#01702FThen, I guess I'll go have\x01",
            "fun at another place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_6F95")

    ChrTalk(
        0x135,
        (
            "#01806FWell, we didn't find her...\x01",
            "It seems there's nothing to do...\x02\x03",
            "#01802FThen, it's time for me\x01",
            "to excuse myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7004")

    label("loc_6F95")


    ChrTalk(
        0x166,
        (
            "#14006FWell, we didn't find her...\x01",
            "Can't help it, right?\x02\x03",
            "#14000FThen, I'll go have fun\x01",
            "at another place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7004")

    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_703C")

    ChrTalk(
        0x101,
        "#00000FYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7055")

    label("loc_703C")


    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_7055")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_7071")
    RemoveParty(0x1, 0xFF)
    Jump("loc_7117")

    label("loc_7071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_7082")
    RemoveParty(0x2, 0xFF)
    Jump("loc_7117")

    label("loc_7082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_7093")
    RemoveParty(0x3, 0xFF)
    Jump("loc_7117")

    label("loc_7093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_70A4")
    RemoveParty(0x8, 0xFF)
    Jump("loc_7117")

    label("loc_70A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_70B5")
    RemoveParty(0x4, 0xFF)
    Jump("loc_7117")

    label("loc_70B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_70CB")
    RemoveParty(0x52, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_7117")

    label("loc_70CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_70DC")
    RemoveParty(0x55, 0xFF)
    Jump("loc_7117")

    label("loc_70DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_70F2")
    RemoveParty(0x4B, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_7117")

    label("loc_70F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_7103")
    RemoveParty(0x33, 0xFF)
    Jump("loc_7117")

    label("loc_7103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_7114")
    RemoveParty(0x34, 0xFF)
    Jump("loc_7117")

    label("loc_7114")

    RemoveParty(0x65, 0xFF)

    label("loc_7117")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Miichie's Challenge]\x07\x00",
            " has been failed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0x10)
    OP_29(0x7F, 0x4, 0x40)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -30, 0, -8310, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_43_69A8 end

    def Function_44_7191(): pass

    label("Function_44_7191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch45400.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch20600.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch33000.itc", 0x22)
    LoadChrToIndex("chr/ch23700.itc", 0x23)
    LoadChrToIndex("chr/ch24400.itc", 0x24)
    LoadChrToIndex("chr/ch20700.itc", 0x25)
    LoadChrToIndex("chr/ch22200.itc", 0x26)
    LoadChrToIndex("chr/ch22100.itc", 0x27)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch32400.itc", 0x29)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(820)
    SoundLoad(819)
    SoundLoad(501)
    SoundLoad(626)
    SetChrChipByIndex(0x101, 0xC)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x21, 0x22)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x22, 0x23)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x23, 0x24)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x24, 0x25)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x25, 0x26)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x26, 0x27)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x27, 0x28)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    SetChrChipByIndex(0x28, 0x29)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    OP_68(170, 2200, -8360, 0)
    MoveCamera(358, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16680, 0)
    SetChrPos(0x101, -700, 0, -7790, 180)
    SetChrPos(0x103, 1000, 0, -7790, 180)
    SetChrPos(0x1E, 3550, 0, -7790, 180)
    SetChrPos(0x1F, 990, 0, -11190, 0)
    SetChrPos(0x20, 50, 0, -12810, 0)
    SetChrPos(0x21, -2600, 0, -10830, 0)
    SetChrPos(0x22, 3350, 0, -9980, 0)
    SetChrPos(0x23, -1650, 0, -13660, 0)
    SetChrPos(0x24, -700, 0, -10910, 0)
    SetChrPos(0x25, 2320, 0, -11400, 0)
    SetChrPos(0x26, -4090, 0, -7750, 45)
    SetChrPos(0x27, 4430, 0, -8039, 315)
    SetChrPos(0x28, 1880, 0, -13990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(170, 1000, -8360, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x1E,
        "Everyone, sorry to have kept you waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "The Michey & Miichie's\x01",
            "dance show begins now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Waaah, Micheeey!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Cuuute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(...At last, it's the dance show.\x01",
            "Uuh, I'm so tense...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F(It s fine.\x01",
            "It seems that this dance\x01",
            "is ad libbed every time.)\x02\x03",
            "#05520F(Even the dance guidelines\x01",
            "are set, so you will do it \x01",
            "in a way or another.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(Guidelines, eh...?)\x02\x03",
            "#05208F(By the way, I was\x01",
            "given a dance manual\x01",
            "before the job...)\x02\x03",
            "#05201F(If I somehow remembered that...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Then...\x01",
            "Everyone, please enjoy it with us!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "Michey & Miichie!\x01",
            "Let's dancing!!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F(Here it is...!)\x02\x03",
            "#05207F(...Let's go, Tio!!\x01",
            ""Enthusiastically" and "fancily!")\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05521F(Roger that...!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    PlayBGM("ed7589", 0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    BeginChrThread(0x101, 1, 0, 50)
    BeginChrThread(0x103, 1, 0, 51)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 48)
    BeginChrThread(0x103, 2, 0, 49)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    ClearScenarioFlags(0x1, 2)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 51)
    BeginChrThread(0x103, 1, 0, 50)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 49)
    BeginChrThread(0x103, 2, 0, 48)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 1)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(Now, the final signature phrase!)\x07\x00\x02",
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
            "Love is Michey☆\x01",      # 0
            "Happy Michey☆\x01",        # 1
            "Enjoy Michey☆\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CD6")
    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x177, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SEnjoooy, Michey☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SEnjoooy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMicheeeey☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F(What a sense of solidarity...\x01",
            "As expected from Mr. Lloyd!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81CB")

    label("loc_7CD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA1")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SLove iiis, Michey☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SL-Love iiiis!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMicheeeey☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_8051")

    label("loc_7EA1")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SHappy, Michey☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SH-Happyyy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMicheeeey☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8051")

    Sound(819, 0, 66, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F(...D-Damn...\x01",
            "DId I get the signature phrase wrong?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F(...*sigh*, at the very very end.)\x02\x03",
            "#05531F(This requires punishment.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81CB")

    StopSound(821, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to Lloyd and Tio's\x01",
            "enthusiastic dance, the\x01",
            "show ended in a great success.\x02\x03",
            "While surrounded in a happy lingering memory,\x01",
            "Lloyd, who danced until the end with no mistakes...\x02\x03",
            "Headed towards the\x01",
            "rest area with Tio.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x86, 0x1, 0x7)
    Jump("loc_8419")

    label("loc_82E3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to Lloyd and Tio's\x01",
            "enthusiastic dance, the\x01",
            "show ended in a great success.\x02\x03",
            "After dancing until the end,\x01",
            "Lloyd headed to the rest\x01",
            "area with Tio, however...\x02\x03",
            "Along the way, he received punishment for \x01",
            "having mistaken the signature phrase.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(501, 0, 80, 0)
    Sound(815, 0, 40, 0)
    Sleep(800)
    Sound(3319, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F#NACK!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x86, 0x1, 0x8)

    label("loc_8419")

    SetScenarioFlags(0x22, 0)
    NewScene("t1370", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7191 end

    def Function_45_8426(): pass

    label("Function_45_8426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8442")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_45_8426")

    label("loc_8442")

    Return()

    # Function_45_8426 end

    def Function_46_8443(): pass

    label("Function_46_8443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_845F")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_46_8443")

    label("loc_845F")

    Return()

    # Function_46_8443 end

    def Function_47_8460(): pass

    label("Function_47_8460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_847C")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_47_8460")

    label("loc_847C")

    Return()

    # Function_47_8460 end

    def Function_48_847D(): pass

    label("Function_48_847D")

    OP_96(0xFE, 0xFFFFF768, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFDD14, 0x7D0, 0x0)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_48_847D end

    def Function_49_84F0(): pass

    label("Function_49_84F0")

    OP_96(0xFE, 0x9C4, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFE4D0, 0x7D0, 0x0)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_49_84F0 end

    def Function_50_8563(): pass

    label("Function_50_8563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8676")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_50_8563")

    label("loc_8676")

    Return()

    # Function_50_8563 end

    def Function_51_8677(): pass

    label("Function_51_8677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_878A")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_51_8677")

    label("loc_878A")

    Return()

    # Function_51_8677 end

    def Function_52_878B(): pass

    label("Function_52_878B")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_52_878B end

    def Function_53_87AA(): pass

    label("Function_53_87AA")

    Sleep(1000)

    label("loc_87AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87CF")
    Sound(918, 0, 50, 0)
    Sleep(2200)
    Sound(918, 0, 40, 0)
    Sleep(5000)
    Jump("loc_87AD")

    label("loc_87CF")

    Return()

    # Function_53_87AA end

    SaveToFile()

Try(main)
