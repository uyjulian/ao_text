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
        "MWL Staff",              # 17
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
        "Function_4_E0D",          # 04, 4
        "Function_5_1065",         # 05, 5
        "Function_6_1113",         # 06, 6
        "Function_7_1255",         # 07, 7
        "Function_8_13E4",         # 08, 8
        "Function_9_156E",         # 09, 9
        "Function_10_165D",        # 0A, 10
        "Function_11_17F3",        # 0B, 11
        "Function_12_190B",        # 0C, 12
        "Function_13_19F0",        # 0D, 13
        "Function_14_1B0A",        # 0E, 14
        "Function_15_1C03",        # 0F, 15
        "Function_16_2194",        # 10, 16
        "Function_17_2228",        # 11, 17
        "Function_18_22C8",        # 12, 18
        "Function_19_2394",        # 13, 19
        "Function_20_257F",        # 14, 20
        "Function_21_2606",        # 15, 21
        "Function_22_2661",        # 16, 22
        "Function_23_26E9",        # 17, 23
        "Function_24_276A",        # 18, 24
        "Function_25_27B0",        # 19, 25
        "Function_26_2A67",        # 1A, 26
        "Function_27_2B5A",        # 1B, 27
        "Function_28_2C69",        # 1C, 28
        "Function_29_4812",        # 1D, 29
        "Function_30_4D01",        # 1E, 30
        "Function_31_4D18",        # 1F, 31
        "Function_32_4D8A",        # 20, 32
        "Function_33_53A2",        # 21, 33
        "Function_34_53C7",        # 22, 34
        "Function_35_58B4",        # 23, 35
        "Function_36_58E7",        # 24, 36
        "Function_37_591A",        # 25, 37
        "Function_38_594D",        # 26, 38
        "Function_39_5A64",        # 27, 39
        "Function_40_5B6D",        # 28, 40
        "Function_41_5BFE",        # 29, 41
        "Function_42_5C4A",        # 2A, 42
        "Function_43_6642",        # 2B, 43
        "Function_44_6E89",        # 2C, 44
        "Function_45_80B4",        # 2D, 45
        "Function_46_80D1",        # 2E, 46
        "Function_47_80EE",        # 2F, 47
        "Function_48_810B",        # 30, 48
        "Function_49_817E",        # 31, 49
        "Function_50_81F1",        # 32, 50
        "Function_51_8305",        # 33, 51
        "Function_52_8419",        # 34, 52
        "Function_53_8438",        # 35, 53
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D98")

    ChrTalk(
        0xE,
        (
            "#00102FHey Tio, look this way.\x02\x03",
            "I'll take your guys'\x01",
            "picture.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DB1")

    label("loc_D98")


    ChrTalk(
        0xE,
        "#00102FOk, cheeese!\x02",
    )

    CloseMessageWindow()

    label("loc_DB1")

    Jump("loc_E09")

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    Jump("loc_E09")

    label("loc_DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    Jump("loc_E09")

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF8")
    Jump("loc_E09")

    label("loc_DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E09")

    label("loc_E09")

    TalkEnd(0xFE)
    Return()

    # Function_3_D2F end

    def Function_4_E0D(): pass

    label("Function_4_E0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E33")
    Call(0, 5)
    Jump("loc_EA5")

    label("loc_E33")


    ChrTalk(
        0xF,
        (
            "#00204FI've finally, finally\x01",
            "made it to the theme\x01",
            "park...\x02\x03",
            "#00202F...Anyhow, I have to\x01",
            "shake Mishy's hand...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA5")

    Jump("loc_1061")

    label("loc_EAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC0")
    Jump("loc_1061")

    label("loc_EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED6")
    Jump("loc_1061")

    label("loc_ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    Jump("loc_1061")

    label("loc_EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDA")

    ChrTalk(
        0xF,
        (
            "#00203FWe can't stay here until\x01",
            "evening, can we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we have a dinner\x01",
            "party at the guest house\x01",
            "to attend this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00206F...*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(She looks\x01",
            "disappointed...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1061")

    label("loc_FDA")


    ChrTalk(
        0xF,
        (
            "#00200FIf possible, I would\x01",
            "have liked to see\x01",
            "Mishy's night parade.\x02\x03",
            "#00206F...Well, it seems I'll\x01",
            "have to save it for next\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1061")

    TalkEnd(0xFE)
    Return()

    # Function_4_E0D end

    def Function_5_1065(): pass

    label("Function_5_1065")

    OP_4B(0xF, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Yoo-hoo, young lady.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, are you having\x01",
            "fun?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#00201FIt's really Mishy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Haha, she really looks\x01",
            "happy.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_5_1065 end

    def Function_6_1113(): pass

    label("Function_6_1113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B8")

    ChrTalk(
        0x10,
        (
            "#00303FWeeell then, I guess\x01",
            "I'll pick myself up some\x01",
            "ladies.\x02\x03",
            "#00309FI wonder where a lady\x01",
            "who strikes my fancy\x01",
            "could be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_11F9")

    label("loc_11B8")


    ChrTalk(
        0x10,
        (
            "#00309FI wonder where a lady\x01",
            "who strikes my fancy\x01",
            "could be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F9")

    Jump("loc_1251")

    label("loc_11FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1214")
    Jump("loc_1251")

    label("loc_1214")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122A")
    Jump("loc_1251")

    label("loc_122A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1240")
    Jump("loc_1251")

    label("loc_1240")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")

    label("loc_1251")

    TalkEnd(0xFE)
    Return()

    # Function_6_1113 end

    def Function_7_1255(): pass

    label("Function_7_1255")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")
    Jump("loc_13E0")

    label("loc_126E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132F")

    ChrTalk(
        0x11,
        (
            "#10105FCome to think of it, I spotted\x01",
            "Mishy, but his little sister\x01",
            ""Mishette" is nowhere to be found.\x02\x03",
            "#10103FHmm. I wonder where she could be\x01",
            "hiding...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_139E")

    label("loc_132F")


    ChrTalk(
        0x11,
        (
            "#10100FI wonder where Mishy's\x01",
            "little sister "Mishette"\x01",
            "is?\x02\x03",
            "#10103FI think I'll find her\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139E")

    Jump("loc_13E0")

    label("loc_13A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B9")
    Jump("loc_13E0")

    label("loc_13B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CF")
    Jump("loc_13E0")

    label("loc_13CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E0")

    label("loc_13E0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1255 end

    def Function_8_13E4(): pass

    label("Function_8_13E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FD")
    Jump("loc_156A")

    label("loc_13FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(
        0x12,
        (
            "#10300FEarlier, Ilya dragged Cecil\x01",
            "out of the rest area.\x02\x03",
            "#10303FHehe, it seems that such a\x01",
            "forcible method is suitable\x01",
            "for inviting girls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1528")

    label("loc_14B1")


    ChrTalk(
        0x12,
        (
            "#10300FIt seems Ilya's forcible\x01",
            "method is suitable for\x01",
            "inviting girls.\x02\x03",
            "#10309FHehe. Why don't you give\x01",
            "it a try?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1528")

    Jump("loc_156A")

    label("loc_152D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1543")
    Jump("loc_156A")

    label("loc_1543")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1559")
    Jump("loc_156A")

    label("loc_1559")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156A")

    label("loc_156A")

    TalkEnd(0xFE)
    Return()

    # Function_8_13E4 end

    def Function_9_156E(): pass

    label("Function_9_156E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1587")
    Jump("loc_1659")

    label("loc_1587")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")
    Jump("loc_1659")

    label("loc_159D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")
    Jump("loc_1659")

    label("loc_15B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1648")

    ChrTalk(
        0x8,
        (
            "#01111FOh, right, I've got to\x01",
            "buy a Mishy souvenir for\x01",
            "Shizuku later.\x02\x03",
            "#01106FI wonder if my pocket\x01",
            "money will be enough?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1659")

    label("loc_1648")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1659")

    label("loc_1659")

    TalkEnd(0xFE)
    Return()

    # Function_9_156E end

    def Function_10_165D(): pass

    label("Function_10_165D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1676")
    Jump("loc_17EF")

    label("loc_1676")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168C")
    Jump("loc_17EF")

    label("loc_168C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A2")
    Jump("loc_17EF")

    label("loc_16A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1751")

    ChrTalk(
        0xA,
        (
            "#05900FI've already used up half\x01",
            "my tickets.\x02\x03",
            "#05902FHaha. It was quick, since I\x01",
            "tagged along with everyone\x01",
            "and rode many attractions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_17D9")

    label("loc_1751")


    ChrTalk(
        0xA,
        (
            "#05900FI've already used up half my\x01",
            "tickets.\x02\x03",
            "#05903FIt looks like it'll be\x01",
            "evening soon... I think I'll\x01",
            "go back to the rest area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D9")

    Jump("loc_17EF")

    label("loc_17DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EF")

    label("loc_17EF")

    TalkEnd(0xFE)
    Return()

    # Function_10_165D end

    def Function_11_17F3(): pass

    label("Function_11_17F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180C")
    Jump("loc_1907")

    label("loc_180C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1822")
    Jump("loc_1907")

    label("loc_1822")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1845")
    Call(0, 12)
    Jump("loc_18DB")

    label("loc_1845")


    ChrTalk(
        0xB,
        (
            "#01705FSay, wasn't there any\x01",
            "attraction you liked, I\x01",
            "wonder?\x02\x03",
            "#01702FI like hopping on the\x01",
            "thrilling ones one after the\x01",
            "next... Any suggestions?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DB")

    Jump("loc_1907")

    label("loc_18E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F6")
    Jump("loc_1907")

    label("loc_18F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1907")

    label("loc_1907")

    TalkEnd(0xFE)
    Return()

    # Function_11_17F3 end

    def Function_12_190B(): pass

    label("Function_12_190B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "#01700FRixia, Sully. Are you guys\x01",
            "having fun?\x02\x03",
            "#01709FChanges of pace are\x01",
            "important for artists too,\x01",
            "so go all out today, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01809FHaha, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#14003FH-Hmph, I already know\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_190B end

    def Function_13_19F0(): pass

    label("Function_13_19F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A09")
    Jump("loc_1B06")

    label("loc_1A09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1F")
    Jump("loc_1B06")

    label("loc_1A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A42")
    Call(0, 12)
    Jump("loc_1ADA")

    label("loc_1A42")


    ChrTalk(
        0xC,
        (
            "#01805FCome to think of it, you\x01",
            "can hear a lot of screams\x01",
            "near the horror coaster.\x02\x03",
            "#01803FThat seems like the kind\x01",
            "of thing you would like,\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADA")

    Jump("loc_1B06")

    label("loc_1ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF5")
    Jump("loc_1B06")

    label("loc_1AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B06")

    label("loc_1B06")

    TalkEnd(0xFE)
    Return()

    # Function_13_19F0 end

    def Function_14_1B0A(): pass

    label("Function_14_1B0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B23")
    Jump("loc_1BFF")

    label("loc_1B23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B39")
    Jump("loc_1BFF")

    label("loc_1B39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5C")
    Call(0, 12)
    Jump("loc_1BD3")

    label("loc_1B5C")


    ChrTalk(
        0xD,
        (
            "#14006FMore importantly, I've\x01",
            "gotten hungry for some\x01",
            "reason.\x02\x03",
            "#14000FWhy don't we get\x01",
            "something at the rest\x01",
            "area?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD3")

    Jump("loc_1BFF")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEE")
    Jump("loc_1BFF")

    label("loc_1BEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFF")

    label("loc_1BFF")

    TalkEnd(0xFE)
    Return()

    # Function_14_1B0A end

    def Function_15_1C03(): pass

    label("Function_15_1C03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C29")
    Call(0, 5)
    Jump("loc_1C77")

    label("loc_1C29")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, welcome to\x01",
            "Wonderland!☆\x07\x00\x02",
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

    label("loc_1C77")

    Jump("loc_2190")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C92")
    Jump("loc_2190")

    label("loc_1C92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA8")
    Jump("loc_2190")

    label("loc_1CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2050")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E59")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, I've heard\x01",
            "what's going on.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Do your best and try to\x01",
            "find my little sister\x01",
            "Mishette, ok?☆\x07\x00\x02",
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
            "[Don't Give Up]\x01",      # 0
            "[Give Up]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E51")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I see. Good luck, then☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I you can't figure where she\x01",
            "is, I'll personally tell\x01",
            "Mishette that you gave up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1E51")

    Call(0, 43)

    label("loc_1E54")

    Jump("loc_204B")

    label("loc_1E59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EF0")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "You won at hide and seek\x01",
            "against Mishette,\x01",
            "huh?0700}\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, that is a very\x01",
            "nice gift. Please take\x01",
            "good care of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204B")

    label("loc_1EF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1FB7")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Don't feel down just\x01",
            "because you lost at hide\x01",
            "and seek with Mishette.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Let's have fun at the attractions\x01",
            "all you want and blow away those\x01",
            "feelings of frustration!☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204B")

    label("loc_1FB7")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hey listen, have you\x01",
            "seen a pink girl who\x01",
            "looks exactly like me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "She's my little\x01",
            "sister... Hmm, I wonder\x01",
            "where she's gone off to?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204B")

    Jump("loc_2190")

    label("loc_2050")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2114")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, thank you!\x01",
            "I'll absolutely do my\x01",
            "best!\x07\x00\x02",
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
    Jump("loc_2190")

    label("loc_2114")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I like the children's\x01",
            "laughter the best.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, by the way, my\x01",
            "second favorite thing\x01",
            "are giant melons.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2190")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C03 end

    def Function_16_2194(): pass

    label("Function_16_2194")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AD")
    Jump("loc_2224")

    label("loc_21AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C3")
    Jump("loc_2224")

    label("loc_21C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D9")
    Jump("loc_2224")

    label("loc_21D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21EF")
    Jump("loc_2224")

    label("loc_21EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(
        0xFE,
        (
            "Aah... I'm really glad I\x01",
            "came.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2224")

    TalkEnd(0xFE)
    Return()

    # Function_16_2194 end

    def Function_17_2228(): pass

    label("Function_17_2228")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2241")
    Jump("loc_22C4")

    label("loc_2241")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2257")
    Jump("loc_22C4")

    label("loc_2257")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226D")
    Jump("loc_22C4")

    label("loc_226D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2283")
    Jump("loc_22C4")

    label("loc_2283")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C4")

    ChrTalk(
        0xFE,
        (
            "Haha... Look, honey.\x01",
            "Rimah looks so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C4")

    TalkEnd(0xFE)
    Return()

    # Function_17_2228 end

    def Function_18_22C8(): pass

    label("Function_18_22C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E1")
    Jump("loc_2390")

    label("loc_22E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F7")
    Jump("loc_2390")

    label("loc_22F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230D")
    Jump("loc_2390")

    label("loc_230D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2323")
    Jump("loc_2390")

    label("loc_2323")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2390")

    ChrTalk(
        0xFE,
        "Yaay, Mishy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rimah won't be around\x01",
            "tonight, but do your best\x01",
            "with the parade, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2390")

    TalkEnd(0xFE)
    Return()

    # Function_18_22C8 end

    def Function_19_2394(): pass

    label("Function_19_2394")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2413")
    OP_AF(0x6C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2576")

    label("loc_2413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2427")
    Jump("loc_2576")

    label("loc_2427")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_243F")
    TalkEnd(0xFE)
    Return()

    label("loc_243F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2576")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DD")

    ChrTalk(
        0x18,
        (
            "Welcome! We deal in a\x01",
            "great number of Mishy\x01",
            "goods here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Let's put on Mishy tails\x01",
            "and enjoy the park!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2576")

    label("loc_24DD")


    ChrTalk(
        0x18,
        (
            "How about a Mishy\x01",
            "souvenir to remember the\x01",
            "park by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "There are a surprising number of\x01",
            "people who return to Crossbell\x01",
            "City wearing a Mishy tail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2576")

    Jump("loc_23A1")

    label("loc_257B")

    TalkEnd(0xFE)
    Return()

    # Function_19_2394 end

    def Function_20_257F(): pass

    label("Function_20_257F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C8")

    ChrTalk(
        0xFE,
        (
            "Let's go to the new\x01",
            "attraction over there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2602")

    label("loc_25C8")


    ChrTalk(
        0xFE,
        (
            "Since we're here, let's\x01",
            "stay until the night\x01",
            "parade!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2602")

    TalkEnd(0xFE)
    Return()

    # Function_20_257F end

    def Function_21_2606(): pass

    label("Function_21_2606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263D")

    ChrTalk(
        0xFE,
        "Where are we going next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_265D")

    label("loc_263D")


    ChrTalk(
        0xFE,
        (
            "Are we going home\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_265D")

    TalkEnd(0xFE)
    Return()

    # Function_21_2606 end

    def Function_22_2661(): pass

    label("Function_22_2661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E5")

    ChrTalk(
        0xFE,
        (
            "We have a yearly pass\x01",
            "for the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "MWL is never boring, no\x01",
            "matter how many times we\x01",
            "come!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E5")

    label("loc_26E5")

    TalkEnd(0xFE)
    Return()

    # Function_22_2661 end

    def Function_23_26E9(): pass

    label("Function_23_26E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2766")

    ChrTalk(
        0xFE,
        (
            "My kid really likes\x01",
            "Mishy a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having come here many\x01",
            "times, I've fallen for\x01",
            "him myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2766")

    label("loc_2766")

    TalkEnd(0xFE)
    Return()

    # Function_23_26E9 end

    def Function_24_276A(): pass

    label("Function_24_276A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27AC")

    ChrTalk(
        0xFE,
        (
            "Buy me a plushie! Buy me\x01",
            "a plushie!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AC")

    label("loc_27AC")

    TalkEnd(0xFE)
    Return()

    # Function_24_276A end

    def Function_25_27B0(): pass

    label("Function_25_27B0")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286B")
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
    Jump("loc_2A66")

    label("loc_286B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BE")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -9350, 0, 6350, 135)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7930, 200, 8240, 135)
    SetChrChipByIndex(0x12, 0x18)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_2A66")

    label("loc_28BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2925")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8320, 0, -2390, 180)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -7690, 0, -3590, 270)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -9110, 0, -3590, 90)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2A66")

    label("loc_2925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E6")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_29B8")
    SetChrFlags(0x8, 0x80)
    Jump("loc_29C6")

    label("loc_29B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_29C6")
    SetChrFlags(0xA, 0x80)

    label("loc_29C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29E1")
    ClearChrFlags(0x29, 0x80)

    label("loc_29E1")

    Jump("loc_2A66")

    label("loc_29E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A66")
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

    label("loc_2A66")

    Return()

    # Function_25_27B0 end

    def Function_26_2A67(): pass

    label("Function_26_2A67")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000F◆The Ferris wheel and\x01",
            "rest area are ahead.\x01",
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
            "Cancel\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B0F"),
        (1, "loc_2B28"),
        (SWITCH_DEFAULT, "loc_2B41"),
    )


    label("loc_2B0F")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B59")

    label("loc_2B28")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B59")

    label("loc_2B41")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Jump("loc_2B59")

    label("loc_2B59")

    Return()

    # Function_26_2A67 end

    def Function_27_2B5A(): pass

    label("Function_27_2B5A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000F◆The horror coaster and\x01",
            "fortune-telling house are\x01",
            "ahead. Where should we go?\x02",
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
            "Cancel\x01",                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C1E"),
        (1, "loc_2C37"),
        (SWITCH_DEFAULT, "loc_2C50"),
    )


    label("loc_2C1E")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C68")

    label("loc_2C37")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C68")

    label("loc_2C50")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Jump("loc_2C68")

    label("loc_2C68")

    Return()

    # Function_27_2B5A end

    def Function_28_2C69(): pass

    label("Function_28_2C69")

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

    def lambda_2E6A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E6A)

    def lambda_2E7F():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E7F)
    Sleep(50)

    def lambda_2E97():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E97)

    def lambda_2EAC():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2EAC)
    Sleep(50)

    def lambda_2EC4():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2EC4)

    def lambda_2ED9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2ED9)

    def lambda_2EEE():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2EEE)
    Sleep(50)

    def lambda_2F06():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F06)

    def lambda_2F1B():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F1B)

    def lambda_2F30():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F30)
    Sleep(50)

    def lambda_2F48():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2F48)

    def lambda_2F5D():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F5D)

    def lambda_2F72():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F72)
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
        "#01109F#15A#4SUwaaah!\x02",
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
        (
            "#00002FSo this is Michelam\x01",
            "Wonderland...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00203F.........(*moved to\x01",
            "tears*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#14005F...A-Amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01705FWow. This is my first\x01",
            "time, but this looks\x01",
            "like a pretty fun place.\x02\x03",
            "#01709FThey've got plenty of\x01",
            "attractions, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00309FHonestly, there's so\x01",
            "many that you can't see\x01",
            "'em all in one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304FSeeing as how we spent\x01",
            "the morning at the\x01",
            "beach...\x02\x03",
            "#10302FIt seems best to focus\x01",
            "on the main ones for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05905FMain ones? Which are you\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06403FHmm. One of them must be the\x01",
            "Ferris wheel on the left\x01",
            "side. You can't miss it.\x02",
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
            "#10109FAnyway, the view is\x01",
            "great.\x02\x03",
            "#10102FMaybe we should save\x01",
            "that one for last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01702FYeah, yeah, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01809FHaha... I'm getting\x01",
            "excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00102FWhen it comes to main\x01",
            "attractions, the "castle" in\x01",
            "the center is a natural choice.\x02",
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
            "#00100FThe Castle of Mirror─ It's\x01",
            "like this theme park's\x01",
            "monument.\x02\x03",
            "#00104FI heard there's a "wish-\x01",
            "granting mirror" on the top\x01",
            "floor...\x02\x03",
            "#00102FThey say that, after ringing\x01",
            "the bell, wishes made before\x01",
            "the mirror will come true.\x02",
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
            "#00304FI bet it's popular with\x01",
            "couples and families.\x02\x03",
            "#00300FAfter all, there are\x01",
            "bell-ringing handles on\x01",
            "both sides of the bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FR-Right. Ringing it by\x01",
            "yourself looks\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01101FHey, hey!\x02",
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
            "#01110FDoes anyone live in that\x01",
            "mansion over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#14011FI-It looks awfully\x01",
            "eerie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00305FHuh? I don't know\x01",
            "either... Was it put in\x01",
            "recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06404FYes. It's this park's\x01",
            "latest attraction.\x02\x03",
            "#06402FIt's called "Horror\x01",
            "Coaster" and it seems to be\x01",
            "quite the thing, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00204FI looked into that as\x01",
            "well.\x02\x03",
            "#00202FIt seems to be a scary and\x01",
            "exciting attraction using\x01",
            "the latest technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00106FS-So they made something\x01",
            "like that, did they...\x02\x03",
            "#00111FThat Bell. She didn't\x01",
            "say a single word to me\x01",
            "about it...\x02",
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
            "#01709FYes, yes, very nice! I\x01",
            "can feel the tension\x01",
            "rising.\x02\x03",
            "#01700FAny other standbys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304F#6PIt's not an attraction, but\x01",
            "the "Fortune-Telling House" is\x01",
            "one of them.\x02\x03",
            "#10300FRumor has it that the fortune\x01",
            "teller who joined last year is\x01",
            "quite the master, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06403FI heard she can do anything,\x01",
            "from compatibility readings\x01",
            "to finding lost items.\x02\x03",
            "#06400FI also heard she's a\x01",
            "mysterious and exotic\x01",
            "beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01805F#12PThat... interests me a\x01",
            "little.\x02\x03",
            "#01808F(Could she be a diviner\x01",
            "of Eastern origin?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00203F...On that subject, you can't\x01",
            "miss chasing after "Mishy".\x02\x03",
            "#00201FThe idea is go around the\x01",
            "park, chasing after him.\x02\x03",
            "#00207FIf you're lucky, you can even\x01",
            "meet a character called\x01",
            ""Mishette", his little sister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00301F#6PPeTiote's serious...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#05905FBy the way...\x02\x03",
            "#05900FI wonder if there's a\x01",
            "place we can rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x13B, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#10105F#6PAh, there's a rest area\x01",
            "on the left in the\x01",
            "arcade district.\x02\x03",
            "#10100FI think they serve some\x01",
            "light food there too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1300, -9600, 1500)

    def lambda_3DD6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DD6)

    def lambda_3DE3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3DE3)
    Sleep(50)

    def lambda_3DF3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3DF3)

    def lambda_3E00():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3E00)
    Sleep(50)

    def lambda_3E10():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3E10)

    def lambda_3E1D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3E1D)
    Sleep(50)

    def lambda_3E2D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3E2D)

    def lambda_3E3A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3E3A)
    Sleep(50)

    def lambda_3E4A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3E4A)

    def lambda_3E57():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3E57)
    Sleep(50)

    def lambda_3E67():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3E67)

    def lambda_3E74():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3E74)

    def lambda_3E81():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3E81)
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
            "#05904FThen, I think we should make that our\x01",
            "meeting place.\x02\x03",
            "#05902FI'll try to be there as much as possible,\x01",
            "so don't hesitate to tell me if you have\x01",
            "anemia or are feeling bad, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PCecil, you don't have to\x01",
            "show your nurse spirit even\x01",
            "at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00108F#12PYes. It would be a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00303F#6P...But if you think about it,\x01",
            "it's the perfect chance to be\x01",
            "taken care of by Cecil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00211F#12PRandy, I think you should\x01",
            "refrain from doing what\x01",
            "you're really trying to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01706F#11PWell, have some fun too, ok?\x02\x03",
            "#01702FYou normally don't, so it's\x01",
            "especially important to enjoy\x01",
            "yourself at times like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05909FHaha, understood. Then,\x01",
            "I'll do as you say.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, -9600, 1500)
    Sleep(500)

    def lambda_419D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_419D)
    Sleep(50)

    def lambda_41AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_41AD)
    Sleep(50)

    def lambda_41BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_41BD)
    Sleep(50)

    def lambda_41CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_41CD)
    Sleep(50)

    def lambda_41DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_41DD)
    Sleep(50)

    def lambda_41ED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_41ED)
    Sleep(50)

    def lambda_41FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_41FD)
    Sleep(50)

    def lambda_420D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_420D)
    Sleep(50)

    def lambda_421D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_421D)
    Sleep(50)

    def lambda_422D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_422D)
    Sleep(50)

    def lambda_423D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_423D)
    Sleep(50)

    def lambda_424D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_424D)
    Sleep(50)

    def lambda_425D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_425D)
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
            "#00003F#11P─We have that dinner party, so we\x01",
            "can enjoy ourselves until evening.\x02\x03",
            "#00000FI'll distribute everyone's\x01",
            "tickets, so please feel free to do\x01",
            "whatever you like, starting now.\x02\x03",
            "#00002FIf there's an attraction you want\x01",
            "to enjoy, please form appropriate\x01",
            "groups...\x02\x03",
            "Is that all right with everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00109F#6PYes, I don't see why\x01",
            "not.\x02",
        )
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
        (
            "#10304F#6POh man, look at you\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x8, 0x87, 0x1F4)
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#01109F#5PHey, Sully! Wanna go\x01",
            "together!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xD, 0x13B, 0x1F4)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#14011F#12PI-I told you, don't\x01",
            "pull!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01709F#6PAhaha. That reminds me\x01",
            "of when we were in\x01",
            "school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05909F#6PHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01203F#6PGrrrowl... Woof.\x02",
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
            "At the theme park, you can enjoy the Ferris\x01",
            "Wheel, Mirror Castle, Fortune-telling House and\x01",
            "Horror Coaster.\x02\x03",
            "You can enjoy each attraction by selecting a\x01",
            "partner and consuming a ticket.\x02\x03",
            "The story will advance once all 5 tickets are\x01",
            "consumed, so please think carefully about which\x01",
            "attractions you want to enjoy and who with.\x07\x00\x02",
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

    # Function_28_2C69 end

    def Function_29_4812(): pass

    label("Function_29_4812")

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
            "#30WAnd so─ Their enjoyable\x01",
            "time passed in the blink\x01",
            "of an eye.\x07\x00\x02",
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
            "#35A#40WAfter feeling the pull of the theme\x01",
            "park's night operations starting...\x02\x03",
            "#35A#40WLloyd and the others briefly returned\x01",
            "to the hotel and decided to head to the\x01",
            "guest house for their dinner party.\x07\x00\x02",
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

    # Function_29_4812 end

    def Function_30_4D01(): pass

    label("Function_30_4D01")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
    Return()

    # Function_30_4D01 end

    def Function_31_4D18(): pass

    label("Function_31_4D18")

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

    # Function_31_4D18 end

    def Function_32_4D8A(): pass

    label("Function_32_4D8A")

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

    def lambda_4F9B():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F9B)
    Sleep(100)

    def lambda_4FB3():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4FB3)
    Sleep(100)

    def lambda_4FCB():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4FCB)
    Sleep(100)

    def lambda_4FE3():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4FE3)
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
        (
            "#00201F#6PMishy's flower bed\x01",
            "is...!\x02",
        )
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

    def lambda_517C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_517C)

    def lambda_518D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_518D)

    def lambda_519E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_519E)
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

    def lambda_520C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_520C)
    Sleep(50)

    def lambda_5224():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5224)
    Sleep(50)

    def lambda_523C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_523C)
    Sleep(50)

    def lambda_5254():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5254)
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
        (
            "#00107F#12P#NThe one that appeared at\x01",
            "the swamp...!\x02",
        )
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

    # Function_32_4D8A end

    def Function_33_53A2(): pass

    label("Function_33_53A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53C6")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_33_53A2")

    label("loc_53C6")

    Return()

    # Function_33_53A2 end

    def Function_34_53C7(): pass

    label("Function_34_53C7")

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

    def lambda_567D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_567D)

    def lambda_568E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_568E)

    def lambda_569F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_569F)
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
            "#00006F#5P...We ran into\x01",
            "Ouroboros' Campanella\x01",
            "here before...\x02\x03",
            "#00013FIf you think about it,\x01",
            "KeA must be waiting\x01",
            "ahead...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYes... I really wonder\x01",
            "what's there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PThinking about it won't\x01",
            "do any good... We've got\x01",
            "to go see for ourselves.\x02",
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

    # Function_34_53C7 end

    def Function_35_58B4(): pass

    label("Function_35_58B4")

    OP_74(0x1, 0xF)

    label("loc_58B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58E6")
    OP_71(0x1, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_58B8")

    label("loc_58E6")

    Return()

    # Function_35_58B4 end

    def Function_36_58E7(): pass

    label("Function_36_58E7")

    OP_74(0x2, 0xF)

    label("loc_58EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5919")
    OP_71(0x2, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x2)
    OP_71(0x2, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x2)
    Jump("loc_58EB")

    label("loc_5919")

    Return()

    # Function_36_58E7 end

    def Function_37_591A(): pass

    label("Function_37_591A")

    OP_74(0x3, 0xF)

    label("loc_591E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_594C")
    OP_71(0x3, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x3)
    OP_71(0x3, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x3)
    Jump("loc_591E")

    label("loc_594C")

    Return()

    # Function_37_591A end

    def Function_38_594D(): pass

    label("Function_38_594D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_596F")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    label("loc_596F")

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
            "#1KWhere do you want to go?\x07\x00\x02",
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
            "Cancel\x01",                     # 2
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
        (0, "loc_5A19"),
        (1, "loc_5A32"),
        (2, "loc_5A4B"),
        (SWITCH_DEFAULT, "loc_5A50"),
    )


    label("loc_5A19")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_5A50")

    label("loc_5A32")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_5A50")

    label("loc_5A4B")

    Jump("loc_5A50")

    label("loc_5A50")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    # Function_38_594D end

    def Function_39_5A64(): pass

    label("Function_39_5A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5A86")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    label("loc_5A86")

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
            "#1KWhere do you want to go?\x07\x00\x02",
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
            "Cancel\x01",            # 2
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
        (0, "loc_5B22"),
        (1, "loc_5B3B"),
        (2, "loc_5B54"),
        (SWITCH_DEFAULT, "loc_5B59"),
    )


    label("loc_5B22")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_5B59")

    label("loc_5B3B")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_5B59")

    label("loc_5B54")

    Jump("loc_5B59")

    label("loc_5B59")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    # Function_39_5A64 end

    def Function_40_5B6D(): pass

    label("Function_40_5B6D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, if I go this way\x01",
            "I'll exit the theme\x01",
            "park.\x02\x03",
            "I'm going to enjoy MWL\x01",
            "to the fullest with\x01",
            "everyone today.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 3000, -55560, 0)
    EventEnd(0x4)
    Return()

    # Function_40_5B6D end

    def Function_41_5BFE(): pass

    label("Function_41_5BFE")


    ChrTalk(
        0x101,
        (
            "#00000FWe have no business this\x01",
            "way right now. ...Let's\x01",
            "not go there.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_41_5BFE end

    def Function_42_5C4A(): pass

    label("Function_42_5C4A")

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
        (
            "#00005FOh, so you were in a\x01",
            "place like this, were\x01",
            "you?\x02",
        )
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
            "Mrr... Maybe I\x01",
            "underestimated you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "To have found me not two but even\x01",
            "three times means it's impossible\x01",
            "that you were just lucky, yes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well I don't know\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Aaalright. Now that\x01",
            "things have come to this,\x01",
            "I'll hide seriously!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you'll never\x01",
            "find me next time, you\x01",
            "hear~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F13():

        label("loc_5F13")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_5F13")

    QueueWorkItem2(0x101, 1, lambda_5F13)

    def lambda_5F25():

        label("loc_5F25")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_5F25")

    QueueWorkItem2(0xEF, 1, lambda_5F25)
    SetChrFlags(0x29, 0x1000)
    OP_95(0x29, -550, 0, 6760, 5000, 0x0)
    OP_95(0x29, -5830, 0, 4550, 5000, 0x0)

    def lambda_5F64():
        OP_95(0xFE, -10560, 0, 4110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5F64)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_6067")

    ChrTalk(
        0x102,
        (
            "#00100FHaha. We found her a\x01",
            "second time too,\x01",
            "somehow.\x02\x03",
            "#00103FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_6067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_60D6")

    ChrTalk(
        0x103,
        (
            "#00200FWe found her a second\x01",
            "time too.\x02\x03",
            "#00203FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_60D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_614E")

    ChrTalk(
        0x104,
        (
            "#00300FWe found her a second\x01",
            "time too, somehow.\x02\x03",
            "#00303FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_614E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_61CC")

    ChrTalk(
        0x109,
        (
            "#10100FHaha. We found her a\x01",
            "second time too,\x01",
            "somehow!\x02\x03",
            "#10103FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_61CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_624A")

    ChrTalk(
        0x105,
        (
            "#10300FHehe. We found her a\x01",
            "second time too,\x01",
            "somehow!\x02\x03",
            "#10303FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_624A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_62C5")

    ChrTalk(
        0x153,
        (
            "#01109FAaalright, with this\x01",
            "we've found her twice!\x02\x03",
            "#01111FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_62C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6343")

    ChrTalk(
        0x156,
        (
            "#06400FHaha. We found her a\x01",
            "second time too,\x01",
            "somehow.\x02\x03",
            "#06403FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_6343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_63C1")

    ChrTalk(
        0x14C,
        (
            "#05900FHaha. We found her a\x01",
            "second time too,\x01",
            "somehow.\x02\x03",
            "#05904FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_63C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_643F")

    ChrTalk(
        0x134,
        (
            "#01700FHuhu. The second time\x01",
            "was easy as pie too, eh?\x02\x03",
            "#01705FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_643F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_64BD")

    ChrTalk(
        0x135,
        (
            "#01802FHaha. We found her a\x01",
            "second time too,\x01",
            "somehow.\x02\x03",
            "#01805FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6527")

    label("loc_64BD")


    ChrTalk(
        0x166,
        (
            "#14000FWe found her a second\x01",
            "time too, somehow.\x02\x03",
            "#14006FShe said she'd get\x01",
            "serious next time,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_65A1")

    ChrTalk(
        0x101,
        (
            "#00006FI'm a little anxious,\x01",
            "but let's just look for\x01",
            "her.\x02\x03",
            "#00000FI wonder where she went\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660D")

    label("loc_65A1")


    ChrTalk(
        0x101,
        (
            "#00006FI'm a little anxious,\x01",
            "but let's just look for\x01",
            "her.\x02\x03",
            "#00000FI wonder where she went\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_660D")

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

    # Function_42_5C4A end

    def Function_43_6642(): pass

    label("Function_43_6642")

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
            "I see... Well, it can't\x01",
            "be helped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'll inform Mishette.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "You can go back to\x01",
            "enjoying yourselves, ok?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYeah, sorry. And thanks\x01",
            "for taking care of this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_67FE")

    ChrTalk(
        0x102,
        (
            "#00106FWell, we didn't find her\x01",
            "so there was nothing we\x01",
            "could do...\x02\x03",
            "#00100FThen, it's time for me\x01",
            "to be going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_67FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_687F")

    ChrTalk(
        0x103,
        (
            "#00206FWe couldn't find her no\x01",
            "matter what we did, so\x01",
            "it can't be helped...\x02\x03",
            "#00200FThen, I'll excuse\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_687F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_68FE")

    ChrTalk(
        0x104,
        (
            "#00306FWell, we couldn't find\x01",
            "her, so we had no\x01",
            "choice.\x02\x03",
            "#00300FThen, I guess it's time\x01",
            "for me to be going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_68FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_697C")

    ChrTalk(
        0x109,
        (
            "#10106FWell, we couldn't find\x01",
            "her, so there's nothing\x01",
            "we could do...\x02\x03",
            "#10100FThen, it's time for me\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_697C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_69EE")

    ChrTalk(
        0x105,
        (
            "#10306FWell, we didn't find\x01",
            "her, so it can't be\x01",
            "helped.\x02\x03",
            "#10300FThen, I'll excuse myself\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_69EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_6A6A")

    ChrTalk(
        0x153,
        (
            "#01106FBoo. We gave our best\x01",
            "but couldn't find her.\x02\x03",
            "#01100FWell, fine. KeA will go\x01",
            "play somewhere else!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_6A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6ADE")

    ChrTalk(
        0x156,
        (
            "#06406FWell, we couldn't find\x01",
            "her so it can't be\x01",
            "helped...\x02\x03",
            "#06400FThen, it's time for me\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_6ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_6B69")

    ChrTalk(
        0x14C,
        (
            "#05906FWell, we didn't find\x01",
            "her, so there's nothing\x01",
            "we could have done.\x02\x03",
            "#05900FThen, I suppose it's\x01",
            "time for me to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_6B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6BFB")

    ChrTalk(
        0x134,
        (
            "#01706FHmm, I wanted to find\x01",
            "her, but... Well, it's\x01",
            "no use I guess.\x02\x03",
            "#01702FThen, I guess I'll go\x01",
            "enjoy myself somewhere\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_6BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_6C91")

    ChrTalk(
        0x135,
        (
            "#01806FWell, we didn't find her...\x01",
            "It seems there's nothing we\x01",
            "could have done...\x02\x03",
            "#01802FThen, it's time for me to\x01",
            "excuse myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D03")

    label("loc_6C91")


    ChrTalk(
        0x166,
        (
            "#14006FWell, we didn't find\x01",
            "her... It can't be\x01",
            "helped, right?\x02\x03",
            "#14000FThen, I'll go have fun\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D03")

    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6D3C")

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D55")

    label("loc_6D3C")


    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_6D55")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_6D71")
    RemoveParty(0x1, 0xFF)
    Jump("loc_6E17")

    label("loc_6D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_6D82")
    RemoveParty(0x2, 0xFF)
    Jump("loc_6E17")

    label("loc_6D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_6D93")
    RemoveParty(0x3, 0xFF)
    Jump("loc_6E17")

    label("loc_6D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_6DA4")
    RemoveParty(0x8, 0xFF)
    Jump("loc_6E17")

    label("loc_6DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_6DB5")
    RemoveParty(0x4, 0xFF)
    Jump("loc_6E17")

    label("loc_6DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_6DCB")
    RemoveParty(0x52, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6E17")

    label("loc_6DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6DDC")
    RemoveParty(0x55, 0xFF)
    Jump("loc_6E17")

    label("loc_6DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_6DF2")
    RemoveParty(0x4B, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6E17")

    label("loc_6DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6E03")
    RemoveParty(0x33, 0xFF)
    Jump("loc_6E17")

    label("loc_6E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_6E14")
    RemoveParty(0x34, 0xFF)
    Jump("loc_6E17")

    label("loc_6E14")

    RemoveParty(0x65, 0xFF)

    label("loc_6E17")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Mishette's\x01",
            "Challenge]\x07\x00",
            " failed...\x02",
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

    # Function_43_6642 end

    def Function_44_6E89(): pass

    label("Function_44_6E89")

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
        (
            "Everyone, sorry to have\x01",
            "kept you waiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "The Mishy & Mishette\x01",
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
            "#05206F(...At last, it's the\x01",
            "dance show. Ooh, I'm so\x01",
            "tense...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F(You'll be fine. It seems\x01",
            "this dance is ad libbed\x01",
            "every time.)\x02\x03",
            "#05520F(The dance guidelines are\x01",
            "set, so I think you'll\x01",
            "get through it somehow.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(Guidelines, huh...)\x02\x03",
            "#05208F(That's right, I was\x01",
            "given the dance manual\x01",
            "before the job...)\x02\x03",
            "#05201F(If can remember it\x01",
            "somehow...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Alright... Let's enjoy\x01",
            "it together everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "Mishy & Mishette! Let's\x01",
            "get dancing!!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F(Here it is!)\x02\x03",
            "#05207F(...Let's go, Tio!!\x01",
            ""Passionately" and\x01",
            ""fancily!")\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05521F(Roger that!)\x07\x00\x02",
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
            "#05203F(Now, the final\x01",
            "signature phrase!)\x07\x00\x02",
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
            "Love is Mishy☆\x01",      # 0
            "Happy Mishy☆\x01",        # 1
            "Enjoy Mishy☆\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799D")
    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x177, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SEnjoy, Mishy☆\x07\x00\x02",
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
        "#4SEnjoy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMishy☆\x02",
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
            "#05522F(That was perfect! Nice\x01",
            "Lloyd!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E86")

    label("loc_799D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B62")

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SLove iiis, Mishy☆\x07\x00\x02",
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
        "#4SL-LOVE IIIS!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMishy☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7D0D")

    label("loc_7B62")


    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SHappy, Mishy☆\x07\x00\x02",
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
        "#4SH-HAPPYYY!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMishy☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7D0D")

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
            "#05206F(...D-Damn... Did I get\x01",
            "Mishy's catchphrase\x01",
            "wrong?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F(...*sigh*, at the very\x01",
            "very end.)\x02\x03",
            "#05531F(This requires\x01",
            "punishment.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E86")

    StopSound(821, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F82")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to Lloyd and Tio's\x01",
            "passionate dance, the show\x01",
            "ended in a great success.\x02\x03",
            "Having finished the dance,\x01",
            "Lloyd experienced a\x01",
            "mysterious feeling...\x02\x03",
            "He headed towards the rest\x01",
            "area with Tio.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x86, 0x1, 0x7)
    Jump("loc_80A7")

    label("loc_7F82")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to Lloyd and Tio's\x01",
            "passionate dance, the show\x01",
            "ended in a great success.\x02\x03",
            "Having finished the dance,\x01",
            "Lloyd headed toward the\x01",
            "rest area with Tio.\x02\x03",
            "But, along the way, he was\x01",
            "punished for messing up\x01",
            "Mishy's signature phrase.\x02",
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

    label("loc_80A7")

    SetScenarioFlags(0x22, 0)
    NewScene("t1370", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_6E89 end

    def Function_45_80B4(): pass

    label("Function_45_80B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_80D0")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_45_80B4")

    label("loc_80D0")

    Return()

    # Function_45_80B4 end

    def Function_46_80D1(): pass

    label("Function_46_80D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_80ED")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_46_80D1")

    label("loc_80ED")

    Return()

    # Function_46_80D1 end

    def Function_47_80EE(): pass

    label("Function_47_80EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_810A")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_47_80EE")

    label("loc_810A")

    Return()

    # Function_47_80EE end

    def Function_48_810B(): pass

    label("Function_48_810B")

    OP_96(0xFE, 0xFFFFF768, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFDD14, 0x7D0, 0x0)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_48_810B end

    def Function_49_817E(): pass

    label("Function_49_817E")

    OP_96(0xFE, 0x9C4, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFE4D0, 0x7D0, 0x0)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_49_817E end

    def Function_50_81F1(): pass

    label("Function_50_81F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8304")
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
    Jump("Function_50_81F1")

    label("loc_8304")

    Return()

    # Function_50_81F1 end

    def Function_51_8305(): pass

    label("Function_51_8305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8418")
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
    Jump("Function_51_8305")

    label("loc_8418")

    Return()

    # Function_51_8305 end

    def Function_52_8419(): pass

    label("Function_52_8419")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_52_8419 end

    def Function_53_8438(): pass

    label("Function_53_8438")

    Sleep(1000)

    label("loc_843B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_845D")
    Sound(918, 0, 50, 0)
    Sleep(2200)
    Sound(918, 0, 40, 0)
    Sleep(5000)
    Jump("loc_843B")

    label("loc_845D")

    Return()

    # Function_53_8438 end

    SaveToFile()

Try(main)
