from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1400.bin",                # FileName
        "t1400",                    # MapName
        "t1400",                    # Location
        0x00BB,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -30000, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1400",                  # 0
        "Elie",                   # 1
        "Randy",                  # 2
        "Noｱl",                  # 3
        "Wazy",                   # 4
        "KeA",                    # 5
        "Fran",                   # 6
        "Cecil",                  # 7
        "Ilya",                   # 8
        "Rixia",                  # 9
        "Sully",                  # 10
        "Michey",                 # 11
        "Melson",                 # 12
        "Corona",                 # 13
        "Rimah",                  # 14
        "M. W. L. Staff",         # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Cryptid",                # 21
        "Miichie",                # 22
        "Boy",                    # 23
        "Boy",                    # 24
        "SE制御",                 # 25
        "bt1450",                 # 26
        "To Wonderland Entrance", # 27
    ))

    ATBonus("ATBonus_490", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_550", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_534", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_538", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_53C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_540", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_544", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_548", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_570", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1450", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_530", "ed7454", "ed7000", "ATBonus_490"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00300.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08200.itc",                   # 04
        "chr/ch08500.itc",                   # 05
        "chr/ch07500.itc",                   # 06
        "chr/ch05100.itc",                   # 07
        "chr/ch05200.itc",                   # 08
        "chr/ch10100.itc",                   # 09
        "chr/ch10200.itc",                   # 0A
        "chr/ch26200.itc",                   # 0B
        "chr/ch22700.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
        "chr/ch44500.itc",                   # 0E
        "chr/ch27600.itc",                   # 0F
        "chr/ch20300.itc",                   # 10
        "chr/ch22300.itc",                   # 11
        "chr/ch33100.itc",                   # 12
        "chr/ch33300.itc",                   # 13
        "chr/ch45400.itc",                   # 14
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

    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2609,    2220,    4294901176, 222,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1679,    2299,    4294900237, 42,   389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2549,    2309,    4294900057, 312,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1200,    2289,    4294900286, 42,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2240,    2200,    4294901447, 222,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294965546, 0,       4294940106, 231,  389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294964546, 0,       4294939536, 90,   389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294965487, 9,       4294938786, 336,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       1600,    4294944147, 180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294964967, 6010,    4294876877, 0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294964527, 5590,    4294878686, 148,  389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294966027, 5690,    4294878227, 234,  389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(889,     509,     4294922227, 270,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294967187, 509,     4294922227, 90,   389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(5420,    9,       4294945346, 180,  389,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  0.0,                   -71.0,                 1.7000000476837158,    625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  14.199999809265137,    -0.3400000035762787,   1.0])

    DeclActor(3680,    1460,    4294944676, 1000,    5420,    1500,    4294945346, 0x007E, 0,  36, 0x0000)

    PlaceName(-0.05999999865889549, 0.0, -140.4499969482422, 0x0000, 0x0000, "To Wonderland Entrance")

    ChipFrameInfo(1620, 0)                                       # 0

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_7A7",          # 02, 2
        "Function_3_94F",          # 03, 3
        "Function_4_A64",          # 04, 4
        "Function_5_C4E",          # 05, 5
        "Function_6_D7B",          # 06, 6
        "Function_7_E83",          # 07, 7
        "Function_8_F9B",          # 08, 8
        "Function_9_1048",         # 09, 9
        "Function_10_10E4",        # 0A, 10
        "Function_11_119D",        # 0B, 11
        "Function_12_1319",        # 0C, 12
        "Function_13_143C",        # 0D, 13
        "Function_14_151D",        # 0E, 14
        "Function_15_177C",        # 0F, 15
        "Function_16_184E",        # 10, 16
        "Function_17_1944",        # 11, 17
        "Function_18_1A1C",        # 12, 18
        "Function_19_1B0A",        # 13, 19
        "Function_20_1BEB",        # 14, 20
        "Function_21_1D2E",        # 15, 21
        "Function_22_1D9C",        # 16, 22
        "Function_23_1E02",        # 17, 23
        "Function_24_1E5A",        # 18, 24
        "Function_25_1F19",        # 19, 25
        "Function_26_1FFC",        # 1A, 26
        "Function_27_2168",        # 1B, 27
        "Function_28_2A3D",        # 1C, 28
        "Function_29_2A62",        # 1D, 29
        "Function_30_2B0D",        # 1E, 30
        "Function_31_2B2D",        # 1F, 31
        "Function_32_2DF7",        # 20, 32
        "Function_33_2E1B",        # 21, 33
        "Function_34_374A",        # 22, 34
        "Function_35_40AB",        # 23, 35
        "Function_36_40EB",        # 24, 36
        "Function_37_4EEB",        # 25, 37
        "Function_38_6194",        # 26, 38
        "Function_39_61CF",        # 27, 39
    ))


    def Function_0_654(): pass

    label("Function_0_654")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_694"),
        (1, "loc_6A0"),
        (2, "loc_6AC"),
        (3, "loc_6B8"),
        (4, "loc_6C4"),
        (5, "loc_6D0"),
        (6, "loc_6DC"),
        (SWITCH_DEFAULT, "loc_6E8"),
    )


    label("loc_694")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_70B")

    Return()

    # Function_0_654 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_71A")
    Jump("loc_788")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_728")
    Jump("loc_788")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_736")
    Jump("loc_788")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_747")
    Call(0, 26)
    Jump("loc_788")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_755")
    Jump("loc_788")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_763")
    Jump("loc_788")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_771")
    Jump("loc_788")

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_77F")
    Jump("loc_788")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_788")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_797")
    ClearScenarioFlags(0x22, 0)
    Event(0, 37)

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7A6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)

    label("loc_7A6")

    Return()

    # Function_1_70C end

    def Function_2_7A7(): pass

    label("Function_2_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D8")
    OP_24(0x335)
    SoundLoad(918)
    BeginChrThread(0x20, 3, 0, 39)
    Jump("loc_7EF")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_7E9")
    OP_24(0x335)
    Jump("loc_7EF")

    label("loc_7E9")

    Sound(821, 1, 50, 0)

    label("loc_7EF")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A")
    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "main", 0x2, "loop_off")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89B")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_8C4")

    label("loc_89B")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8EB")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)
    Jump("loc_90D")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_90D")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_921")
    ClearMapObjFlags(0x0, 0x10)

    label("loc_921")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94E")
    OP_66(0x0, 0x1)

    label("loc_94E")

    Return()

    # Function_2_7A7 end

    def Function_3_94F(): pass

    label("Function_3_94F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_A60")

    label("loc_968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_A60")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_A60")

    label("loc_994")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F")

    ChrTalk(
        0x8,
        (
            "#00100FJust before I heard the pretty sound\x01",
            "of a bell coming from the castle direction.\x02\x03",
            "#00109F*giggle*, I believe some couple\x01",
            "is making a wish to the mirror.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A60")

    label("loc_A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")

    label("loc_A60")

    TalkEnd(0xFE)
    Return()

    # Function_3_94F end

    def Function_4_A64(): pass

    label("Function_4_A64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D")
    Jump("loc_C4A")

    label("loc_A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A93")
    Jump("loc_C4A")

    label("loc_A93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9")
    Jump("loc_C4A")

    label("loc_AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABF")
    Jump("loc_C4A")

    label("loc_ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(
        0x9,
        (
            "#00302FIt seems that mirror castle is litten\x01",
            "during the night part too.\x02\x03",
            "#00304FTogether with the fireworks and parade,\x01",
            "it really feels like the closin' on one \x01",
            "day at the theme park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C4A")

    label("loc_B9F")


    ChrTalk(
        0x9,
        (
            "#00302FSince it's rare to be here, I wanted\x01",
            "to spend the night part with a\x01",
            "beautiful lady, but...\x02\x03",
            "#00306FWell, we've got the dinner party,\x01",
            "so there's no helpin' it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4A")

    TalkEnd(0xFE)
    Return()

    # Function_4_A64 end

    def Function_5_C4E(): pass

    label("Function_5_C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    Jump("loc_D77")

    label("loc_C67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    Jump("loc_D77")

    label("loc_C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C93")
    Jump("loc_D77")

    label("loc_C93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(
        0xA,
        (
            "#10103FRumors of a "Wish-Granting Mirror"...\x01",
            "Will the wishes really come true?\x02\x03",
            "#10100FI'm really looking forward a little\x01",
            "to it, since they say that "where's\x01",
            "a smoke there's a fire".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D77")

    label("loc_D66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")

    label("loc_D77")

    TalkEnd(0xFE)
    Return()

    # Function_5_C4E end

    def Function_6_D7B(): pass

    label("Function_6_D7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D94")
    Jump("loc_E7F")

    label("loc_D94")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAA")
    Jump("loc_E7F")

    label("loc_DAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCD")
    Call(0, 7)
    Jump("loc_E53")

    label("loc_DCD")


    ChrTalk(
        0xB,
        (
            "#10302FIf you don't believe it's not fun...eh?\x01",
            "Hu hu, it's indeed like that.\x02\x03",
            "#10304FWell, I believe I'll have\x01",
            "a lot of fun too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E53")

    Jump("loc_E7F")

    label("loc_E58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6E")
    Jump("loc_E7F")

    label("loc_E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")

    label("loc_E7F")

    TalkEnd(0xFE)
    Return()

    # Function_6_D7B end

    def Function_7_E83(): pass

    label("Function_7_E83")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "#10300FA "Wish-Granting Mirror""...\x02\x03",
            "#10302FDo you think the wish\x01",
            "will really come true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#06409FOf course!\x02\x03",
            "#06400FAfter all, if you don't\x01",
            "believe it, the attraction\x01",
            "too is no fun, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#10300FHu hu, I see.\x01",
            "It's indeed like you say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_E83 end

    def Function_8_F9B(): pass

    label("Function_8_F9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC1")
    Call(0, 9)
    Jump("loc_FEC")

    label("loc_FC1")


    ChrTalk(
        0xC,
        "#01109FMirror Castle is really biiig!\x02",
    )

    CloseMessageWindow()

    label("loc_FEC")

    Jump("loc_1044")

    label("loc_FF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    Jump("loc_1044")

    label("loc_1007")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101D")
    Jump("loc_1044")

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1033")
    Jump("loc_1044")

    label("loc_1033")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1044")

    label("loc_1044")

    TalkEnd(0xFE)
    Return()

    # Function_8_F9B end

    def Function_9_1048(): pass

    label("Function_9_1048")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01109FWoooow...\x01",
            "Mirror Castle is really biiig!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#14005FYeah...looking at it from up\x01",
            "close it's totally different...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_1048 end

    def Function_10_10E4(): pass

    label("Function_10_10E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FD")
    Jump("loc_1199")

    label("loc_10FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1113")
    Jump("loc_1199")

    label("loc_1113")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")
    Call(0, 7)
    Jump("loc_116D")

    label("loc_1136")


    ChrTalk(
        0xD,
        (
            "#06409FThe theme park attractions\x01",
            "are really fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116D")

    Jump("loc_1199")

    label("loc_1172")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1188")
    Jump("loc_1199")

    label("loc_1188")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1199")

    label("loc_1199")

    TalkEnd(0xFE)
    Return()

    # Function_10_10E4 end

    def Function_11_119D(): pass

    label("Function_11_119D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B6")
    Jump("loc_1315")

    label("loc_11B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1279")

    ChrTalk(
        0xE,
        (
            "#05900FUh uh, the popular Michey and\x01",
            "Ilya the big star, together...\x01",
            "It's quite the unusual sight.\x02\x03",
            "#05909FIt could be an unintentionally\x01",
            "amazing two shot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12D3")

    label("loc_1279")


    ChrTalk(
        0xE,
        (
            "#05909FMichey and Ilya together could make for \x01",
            "an unintentionally amazing two shot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_1315")

    label("loc_12D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EE")
    Jump("loc_1315")

    label("loc_12EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1304")
    Jump("loc_1315")

    label("loc_1304")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1315")

    label("loc_1315")

    TalkEnd(0xFE)
    Return()

    # Function_11_119D end

    def Function_12_1319(): pass

    label("Function_12_1319")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1332")
    Jump("loc_1438")

    label("loc_1332")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1355")
    Call(0, 13)
    Jump("loc_13F6")

    label("loc_1355")


    ChrTalk(
        0xF,
        (
            "#01705FOh, if we stay together for too long,\x01",
            "it seems that people will come gathering.\x02\x03",
            "#01702FI'll excuse myself here, \x01",
            "because I came with friends today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F6")

    Jump("loc_1438")

    label("loc_13FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1411")
    Jump("loc_1438")

    label("loc_1411")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1427")
    Jump("loc_1438")

    label("loc_1427")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1438")

    label("loc_1438")

    TalkEnd(0xFE)
    Return()

    # Function_12_1319 end

    def Function_13_143C(): pass

    label("Function_13_143C")

    OP_4B(0xF, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Ah, could you be...\x01",
            "Miss Ilya from\x01",
            "the Arc-en-ciel?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, I've been always\x01",
            "cheering for you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01700FUh uh, I too see you\x01",
            "in the city quite a lot.\x02\x03",
            "#01709FLet's both do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_143C end

    def Function_14_151D(): pass

    label("Function_14_151D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1536")
    Jump("loc_1778")

    label("loc_1536")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154C")
    Jump("loc_1778")

    label("loc_154C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1562")
    Jump("loc_1778")

    label("loc_1562")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1578")
    Jump("loc_1778")

    label("loc_1578")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A8")

    ChrTalk(
        0x10,
        (
            "#01802FAround here, when night comes,\x01",
            "it fills up with couples.\x02\x03",
            "#01804FIt seems there'll be a full moon tonight...\x01",
            "It'll be a very pretty scenery with\x01",
            "the moonlight reflecting on the lake.\x02\x03",
            "#01809FUh uh, it somehow put you into a\x01",
            "romantic mood just imagining it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1778")

    label("loc_16A8")


    ChrTalk(
        0x10,
        (
            "#01802FIt seems there'll be a full moon tonight...\x01",
            "It should be a very pretty scenery with\x01",
            "the moonlight reflecting on the lake.\x02\x03",
            "#01809FUh uh, it somehow put you into a\x01",
            "romantic mood just imagining it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1778")

    TalkEnd(0xFE)
    Return()

    # Function_14_151D end

    def Function_15_177C(): pass

    label("Function_15_177C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")
    Call(0, 9)
    Jump("loc_17F2")

    label("loc_17A2")


    ChrTalk(
        0x11,
        (
            "#14005FLooking at it from up close, it's this big...\x01",
            "Somehow I feel dizzy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F2")

    Jump("loc_184A")

    label("loc_17F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180D")
    Jump("loc_184A")

    label("loc_180D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1823")
    Jump("loc_184A")

    label("loc_1823")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1839")
    Jump("loc_184A")

    label("loc_1839")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184A")

    label("loc_184A")

    TalkEnd(0xFE)
    Return()

    # Function_15_177C end

    def Function_16_184E(): pass

    label("Function_16_184E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1867")
    Jump("loc_1940")

    label("loc_1867")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188A")
    Call(0, 13)
    Jump("loc_18FE")

    label("loc_188A")


    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'm moved for having been\x01",
            "able to meet Miss Ilya.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, then, enjoy\x01",
            "your stay at the fullest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FE")

    Jump("loc_1940")

    label("loc_1903")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1919")
    Jump("loc_1940")

    label("loc_1919")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192F")
    Jump("loc_1940")

    label("loc_192F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")

    label("loc_1940")

    TalkEnd(0xFE)
    Return()

    # Function_16_184E end

    def Function_17_1944(): pass

    label("Function_17_1944")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195D")
    Jump("loc_1A18")

    label("loc_195D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1973")
    Jump("loc_1A18")

    label("loc_1973")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1989")
    Jump("loc_1A18")

    label("loc_1989")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A07")

    ChrTalk(
        0x13,
        (
            "It was really fantastic\x01",
            "inside the mirror castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I felt again that I came\x01",
            "to the theme park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1A07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A18")

    label("loc_1A18")

    TalkEnd(0xFE)
    Return()

    # Function_17_1944 end

    def Function_18_1A1C(): pass

    label("Function_18_1A1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A35")
    Jump("loc_1B06")

    label("loc_1A35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4B")
    Jump("loc_1B06")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A61")
    Jump("loc_1B06")

    label("loc_1A61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF5")

    ChrTalk(
        0x14,
        (
            "Going up and down those long\x01",
            "stairs was a little tiresome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "However, Rimah was happy \x01",
            "so it was worth climbing them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B06")

    label("loc_1AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B06")

    label("loc_1B06")

    TalkEnd(0xFE)
    Return()

    # Function_18_1A1C end

    def Function_19_1B0A(): pass

    label("Function_19_1B0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B23")
    Jump("loc_1BE7")

    label("loc_1B23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B39")
    Jump("loc_1BE7")

    label("loc_1B39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4F")
    Jump("loc_1BE7")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD6")

    ChrTalk(
        0x15,
        (
            "I rang the bell at the\x01",
            "castle with papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Eheheh, I wished to\x01",
            "come back all together\x01",
            "again to have fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE7")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE7")

    label("loc_1BE7")

    TalkEnd(0xFE)
    Return()

    # Function_19_1B0A end

    def Function_20_1BEB(): pass

    label("Function_20_1BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2A")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Welcome to "Mirror Castle".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is an attraction where you explore the\x01",
            "castle interior aiming for the top floor\x01",
            "where the "Wish-Granting Mirror" is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm playing hide and seek wih Miichie...\x01",
            "I'll refrain from having a good time with\x01",
            "the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1D2D")

    label("loc_1D2A")

    Call(0, 33)

    label("loc_1D2D")

    Return()

    # Function_20_1BEB end

    def Function_21_1D2E(): pass

    label("Function_21_1D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(
        0xFE,
        (
            "Climbing to the top of\x01",
            "that big castle...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...It looks quite tiresome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D98")

    label("loc_1D98")

    TalkEnd(0xFE)
    Return()

    # Function_21_1D2E end

    def Function_22_1D9C(): pass

    label("Function_22_1D9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DFE")

    ChrTalk(
        0xFE,
        (
            "For this child's sake,\x01",
            "I must do my best like\x01",
            "my husband and climb.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFE")

    label("loc_1DFE")

    TalkEnd(0xFE)
    Return()

    # Function_22_1D9C end

    def Function_23_1E02(): pass

    label("Function_23_1E02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E56")

    ChrTalk(
        0xFE,
        (
            "*thum thump*...\x01",
            "What should I wish to the mirror for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E56")

    label("loc_1E56")

    TalkEnd(0xFE)
    Return()

    # Function_23_1E02 end

    def Function_24_1E5A(): pass

    label("Function_24_1E5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC7")

    ChrTalk(
        0xFE,
        "Come on, let's enter the castle now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, we'll spend time\x01",
            "romantically.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F15")

    label("loc_1EC7")


    ChrTalk(
        0xFE,
        "The night part starts now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, let's enjoy\x01",
            "an eccentric night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F15")

    TalkEnd(0xFE)
    Return()

    # Function_24_1E5A end

    def Function_25_1F19(): pass

    label("Function_25_1F19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(
        0xFE,
        "Uh uh, what a very lovely castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like I came to the\x01",
            "world of fairytales.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF8")

    label("loc_1F8B")


    ChrTalk(
        0xFE,
        (
            "I spent a romantic\x01",
            "time with him at the\x01",
            "mirror castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I can't wait for the night part too.\x02",
    )

    CloseMessageWindow()

    label("loc_1FF8")

    TalkEnd(0xFE)
    Return()

    # Function_25_1F19 end

    def Function_26_1FFC(): pass

    label("Function_26_1FFC")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2053")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_2167")

    label("loc_2053")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2082")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_2167")

    label("loc_2082")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AC")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2167")

    label("loc_20AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2133")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_2105")
    SetChrFlags(0x8, 0x80)
    Jump("loc_2113")

    label("loc_2105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2113")
    SetChrFlags(0xA, 0x80)

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212E")
    ClearChrFlags(0x1D, 0x80)

    label("loc_212E")

    Jump("loc_2167")

    label("loc_2133")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2167")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)

    label("loc_2167")

    Return()

    # Function_26_1FFC end

    def Function_27_2168(): pass

    label("Function_27_2168")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadEffect(0x0, "battle\\cr036301.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    OP_90(0x101, 100, 5000, -73000, 0)
    OP_90(0x102, -800, 5000, -74100, 0)
    OP_90(0x103, 750, 5000, -73900, 0)
    OP_90(0x104, -100, 5000, -75000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 3400, -68000, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 3000)

    def lambda_22F3():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22F3)
    Sleep(50)

    def lambda_230B():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_230B)
    Sleep(50)

    def lambda_2323():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2323)
    Sleep(50)

    def lambda_233B():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_233B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(0, 42000, -7500, 0)
    MoveCamera(0, -25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_11(0x47, 0x99, 0xF3, 0x4B, 0x12C, 0x2710)
    OP_68(0, 24000, -7500, 10000)
    MoveCamera(335, 20, 0, 10000)
    SetCameraDistance(100000, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 3500, -68000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(12500, 2500)
    OP_90(0x102, -800, 5000, -67650, 0)
    OP_90(0x103, 750, 5000, -68350, 0)
    OP_90(0x104, 0, 5000, -69100, 0)
    OP_11(0x47, 0x99, 0xF3, 0x14, 0x12C, 0x0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00303F#6P"Mirror Castle"...\x02\x03",
            "#00301FI thought it was a simple \x01",
            "structure of the theme park, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P...The spirit pressure is clearly\x01",
            "rising from that castle.\x02\x03",
            "#00201FAnd probably, from the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5P...I'm sure I heard that the\x01",
            "castle was built because\x01",
            ""she" proposed it...\x02\x03",
            "#00108FBut, don't tell me that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...In any case, let's go inside.\x02\x03",
            "#00001FIf we're lucky, at the top floor we──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x1C, 0, 0, 28)
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
    Fade(250)
    OP_68(0, 9500, -56000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    MoveCamera(315, 0, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x1C, 0x0, 0, 8500, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1C, 3, 0, 29)

    def lambda_2738():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2738)
    OP_75(0x1, 0x2, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(0, 5100, -56000, 1000)
    MoveCamera(330, 5, 0, 1000)
    OP_6E(650, 1000)
    SetCameraDistance(20000, 1000)
    OP_6F(0x79)
    Sleep(700)
    OP_68(-1350, 4700, -62800, 2000)
    MoveCamera(317, 5, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(20000, 2000)
    OP_90(0x102, -700, 5000, -67450, 0)
    OP_90(0x103, 1000, 5000, -68850, 0)
    OP_90(0x104, -100, 5000, -69300, 0)
    Sleep(1000)

    def lambda_2800():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2800)
    Sleep(50)

    def lambda_2818():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2818)
    Sleep(50)

    def lambda_2830():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2830)
    Sleep(50)

    def lambda_2848():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2848)
    WaitChrThread(0x104, 1)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00110F#1PThe old mine's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#1PTch...! Is it the\x01",
            "castle's gate watcher!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#1P──Prepare to fight!\x01",
            "We'll crush it with everything we've got!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(60, 80, -1, -1)
    SetChrName("Comrades")

    AnonymousTalk(
        0xFF,
        "#4S#5PYeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2220, 5100, -59370, 1500)
    SetCameraDistance(11500, 1500)

    def lambda_299E():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_299E)

    def lambda_29B3():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29B3)

    def lambda_29C8():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29C8)

    def lambda_29DD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29DD)
    EndChrThread(0x1C, 0x3)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(400)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Battle("BattleInfo_570", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 31)
    Return()

    # Function_27_2168 end

    def Function_28_2A3D(): pass

    label("Function_28_2A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A61")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_28_2A3D")

    label("loc_2A61")

    Return()

    # Function_28_2A3D end

    def Function_29_2A62(): pass

    label("Function_29_2A62")

    OP_74(0x1, 0x5)

    label("loc_2A66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A98")
    OP_71(0x1, 0x137, 0x13C, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x13C, 0x137, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_2A66")

    label("loc_2A98")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x137, 0x14E, 0x0, 0x8)
    Sleep(550)
    PlayEffect(0x1, 0xFF, 0x1C, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x1C2, 0x96, 0x1388, 0x226)
    OP_79(0x1)
    OP_74(0x1, 0x19)
    OP_71(0x1, 0xA, 0x2F, 0x15E, 0x20)
    Return()

    # Function_29_2A62 end

    def Function_30_2B0D(): pass

    label("Function_30_2B0D")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x78, 0x8C, 0x12C, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_30_2B0D end

    def Function_31_2B2D(): pass

    label("Function_31_2B2D")

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
    OP_90(0x101, 0, 5000, -63000, 0)
    OP_90(0x102, -600, 5000, -64000, 0)
    OP_90(0x103, 600, 5000, -64000, 0)
    OP_90(0x104, 0, 5000, -65000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 12000, -56000, 0)
    MoveCamera(315, -10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 8500, -56000, 3000)
    MoveCamera(0, 15, 0, 3000)
    SetCameraDistance(35000, 3000)
    BeginChrThread(0x1C, 0, 0, 28)
    BeginChrThread(0x1C, 3, 0, 32)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_2D5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2D5F)
    OP_75(0x1, 0x1, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1C, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0x1C, 0x80)
    Sleep(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_90(0x0, 0, 5000, -63000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_2B2D end

    def Function_32_2DF7(): pass

    label("Function_32_2DF7")

    OP_74(0x1, 0x19)
    OP_71(0x1, 0x50, 0x5A, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x6D, 0x0, 0x20)
    Return()

    # Function_32_2DF7 end

    def Function_33_2E1B(): pass

    label("Function_33_2E1B")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 2500, -23700, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x101, 0, 1210, -24340, 0)
    OP_0D()

    ChrTalk(
        0x16,
        "Welcome to "Mirror Castle".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It is an attraction where you explore the\x01",
            "castle interior aiming for the top floor\x01",
            "where the "Wish-Granting Mirror" is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I suggest you to enter together\x01",
            "with someone, if you want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(...Who should I invite?)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho will you invite?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "KeA")
    MenuCmd(1, 0, "Fran")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilya")
    MenuCmd(1, 0, "Rixia")
    MenuCmd(1, 0, "Sully")
    MenuCmd(1, 0, "Quit")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3028")
    MenuCmd(3, 0, 0x0)

    label("loc_3028")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_303A")
    MenuCmd(3, 0, 0x1)

    label("loc_303A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_304C")
    MenuCmd(3, 0, 0x2)

    label("loc_304C")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_305E")
    MenuCmd(3, 0, 0x3)

    label("loc_305E")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3070")
    MenuCmd(3, 0, 0x4)

    label("loc_3070")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3082")
    MenuCmd(3, 0, 0x5)

    label("loc_3082")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3094")
    MenuCmd(3, 0, 0x6)

    label("loc_3094")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_30A6")
    MenuCmd(3, 0, 0x7)

    label("loc_30A6")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_30B8")
    MenuCmd(3, 0, 0x8)

    label("loc_30B8")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_30CA")
    MenuCmd(3, 0, 0x9)

    label("loc_30CA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_30DC")
    MenuCmd(3, 0, 0xA)

    label("loc_30DC")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E9")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3176"),
        (1, "loc_31B8"),
        (2, "loc_31F9"),
        (3, "loc_323C"),
        (4, "loc_327E"),
        (5, "loc_32C0"),
        (6, "loc_3301"),
        (7, "loc_3343"),
        (8, "loc_338D"),
        (9, "loc_33D4"),
        (10, "loc_3417"),
        (SWITCH_DEFAULT, "loc_345A"),
    )


    label("loc_3176")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Elie.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_31B8")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Tio.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_31F9")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Randy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_323C")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Noｱl.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_327E")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Wazy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_32C0")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite KeA.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_3301")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Fran.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_3343")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite sister Cecil.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_338D")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Miss Ilya.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_33D4")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Rixia.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_3417")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Sully.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_345A")

    label("loc_345A")

    FadeToDark(500, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34B1"),
        (1, "loc_34BA"),
        (2, "loc_34C3"),
        (3, "loc_34CC"),
        (4, "loc_34D5"),
        (5, "loc_34DE"),
        (6, "loc_34E7"),
        (7, "loc_34F0"),
        (8, "loc_34F9"),
        (9, "loc_3502"),
        (10, "loc_350B"),
        (SWITCH_DEFAULT, "loc_3514"),
    )


    label("loc_34B1")

    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34BA")

    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34C3")

    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34CC")

    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34D5")

    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34DE")

    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34E7")

    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34F0")

    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_34F9")

    AddParty(0x33, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_3502")

    AddParty(0x34, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_350B")

    AddParty(0x65, 0xEF, 0xFF)
    Jump("loc_3514")

    label("loc_3514")

    SetChrPos(0x101, -500, 1030, -24600, 0)
    SetChrPos(0xEF, 500, 1030, -24600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x16,
        "Then, I'll take your ticket.\x02",
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed 1 ticket to the staff.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x16,
        "Alright, I got your ticket.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please enjoy the exploration of\x01",
            "the fantastic "Mirror Castle"...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x16, 0x0, 0x1F4)
    OP_9B(0x0, 0x16, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(116, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_3660():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3660)
    OP_93(0x16, 0x5A, 0x1F4)
    WaitChrThread(0x16, 1)
    Sleep(300)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)

    def lambda_369E():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_369E)
    Sleep(50)

    def lambda_36B6():
        OP_9B(0x0, 0xEF, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_36B6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1401", 0, 0, 0)
    IdleLoop()
    Jump("loc_3732")

    label("loc_36E9")


    ChrTalk(
        0x16,
        "Oh, are you not entering?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We will wait for\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3732")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -28000, 180)
    EventEnd(0x5)
    Return()

    # Function_33_2E1B end

    def Function_34_374A(): pass

    label("Function_34_374A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -600, 1030, -24600, 90)
    SetChrPos(0xEF, 600, 1030, -24600, 270)
    OP_4B(0x16, 0xFF)
    FadeToBright(1000, 0)
    OP_68(0, 3000, -23700, 0)
    OP_68(0, 2500, -23700, 2500)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3812"),
        (1, "loc_38C1"),
        (2, "loc_3971"),
        (3, "loc_3A16"),
        (4, "loc_3ABB"),
        (5, "loc_3B6C"),
        (6, "loc_3C2C"),
        (7, "loc_3CCE"),
        (8, "loc_3D81"),
        (9, "loc_3E27"),
        (10, "loc_3ED5"),
        (SWITCH_DEFAULT, "loc_3F67"),
    )


    label("loc_3812")


    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, I had a lot of fun\x01",
            "walking the castle together.\x02\x03",
            "#00100FThen, it's time\x01",
            "for me to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_38C1")


    ChrTalk(
        0x103,
        (
            "#00202FThe Mirror Castle...\x01",
            "It was fun touring it together.\x02\x03",
            "#00202FThen, I will excuse myself for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, later then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3971")


    ChrTalk(
        0x104,
        (
            "#00302FHa ha, even if we're two guys,\x01",
            "it was quite fun.\x02\x03",
            "#00300FThen, I'm goin' somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, laters.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3A16")


    ChrTalk(
        0x109,
        (
            "#10109FThe Mirror Castle was pretty fun.\x02\x03",
            "#10100FThen, I will excuse myself here for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, see you later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3ABB")


    ChrTalk(
        0x105,
        (
            "#10304FThe Mirror Castle...\x01",
            "It was quite interesting.\x02\x03",
            "#10300FWell then, I believe I'll\x01",
            "tour another place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3B6C")


    ChrTalk(
        0x153,
        (
            "#01109F*haah*, it was a big castle, eh?\x01",
            "It was really fun!\x02\x03",
            "#01100FThen, KeA will go\x01",
            "to a different place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FEheheh, see you later, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3C2C")


    ChrTalk(
        0x156,
        (
            "#06409FUh uh, the Mirror Castle...\x01",
            "It was really fun!\x02\x03",
            "#06400FThen, I'll excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06400FYes, see you then!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3CCE")


    ChrTalk(
        0x14C,
        (
            "#05902FUh uh, it was really fun to\x01",
            "see the big mirror and bell.\x02\x03",
            "#05900FThen, I will go to a\x01",
            "different place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3D81")


    ChrTalk(
        0x134,
        (
            "#01709FUh uh, it was a pretty\x01",
            "impressive castle, eh?\x02\x03",
            "#01700FWell then, I'll go\x01",
            "to another place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01700FYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3E27")


    ChrTalk(
        0x135,
        (
            "#01809FUh uh, it was really fun walking\x01",
            "around a pretty castle.\x02\x03",
            "#01802FThen, I'll excuse myself here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FYes, see you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3ED5")


    ChrTalk(
        0x166,
        (
            "#14002F...Walking around the castle\x01",
            "wasn't that bad.\x02\x03",
            "#14000FThen, I'm going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14000FYes, see ya.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3F67")

    BeginChrThread(0xEF, 3, 0, 35)
    WaitChrThread(0xEF, 3)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3FBC"),
        (1, "loc_3FCA"),
        (2, "loc_3FD8"),
        (3, "loc_3FE6"),
        (4, "loc_3FF4"),
        (5, "loc_4002"),
        (6, "loc_4010"),
        (7, "loc_401E"),
        (8, "loc_402C"),
        (9, "loc_403A"),
        (10, "loc_4048"),
        (SWITCH_DEFAULT, "loc_4056"),
    )


    label("loc_3FBC")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_3FCA")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_3FD8")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_3FE6")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_3FF4")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_4002")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_4010")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_401E")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_402C")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_403A")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_4048")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4056")

    label("loc_4056")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4093")
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_4093")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -29000, 180)
    EventEnd(0x5)
    Return()

    # Function_34_374A end

    def Function_35_40AB(): pass

    label("Function_35_40AB")


    def lambda_40B0():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40B0)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_40C4():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40C4)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xFE, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_35_40AB end

    def Function_36_40EB(): pass

    label("Function_36_40EB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0x0)
    OP_68(6540, 5060, -25400, 0)
    MoveCamera(320, 41, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, 2560, 1600, -22190, 90)
    SetChrPos(0xEF, 2590, 1290, -23560, 90)
    OP_4B(0x1D, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FFound her...!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1D, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1D, 0x101, 500)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're amazing, mister!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2110, 3600, -34340, 0)
    MoveCamera(30, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10310, 0)
    SetChrPos(0x1D, 80, 0, -29860, 180)
    SetChrPos(0x101, -500, 0, -31500, 0)
    SetChrPos(0xEF, 500, 0, -31500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I can't believe you found me even five\x01",
            "times in such a short amount of time...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, this is\x01",
            "my total defeat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mister, you truly are the\x01",
            "King of Hide-and-Seek☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4365")
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_43DD")

    label("loc_4365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4385")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_43DD")

    label("loc_4385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_43A5")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_43DD")

    label("loc_43A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_43C5")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_43DD")

    label("loc_43C5")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_43DD")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FK-King of Hide-and-Seek...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4448")

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, you got a\x01",
            "strange title, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_4448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4491")

    ChrTalk(
        0x103,
        (
            "#00202FAs expected from Miichie...\x01",
            "Loose and relaxed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_4491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_44C7")

    ChrTalk(
        0x104,
        (
            "#00302FYou got a weird\x01",
            "title, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_44C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4507")

    ChrTalk(
        0x109,
        (
            "#10102FAhaha...she gave\x01",
            "you a strange title.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_4507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_454E")

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, you earned quite\x01",
            "a cool popular name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_454E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_457F")

    ChrTalk(
        0x153,
        "#01109FLloyd, that's so cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_457F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_45B7")

    ChrTalk(
        0x156,
        (
            "#06409FUh uh, you got\x01",
            "a funny title!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_45B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_45F2")

    ChrTalk(
        0x14C,
        "#05902FUh uh, what a cute popular name.\x02",
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_45F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4629")

    ChrTalk(
        0x134,
        "#01702FHu hu, isn't it pretty good?\x02",
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_4629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4671")

    ChrTalk(
        0x135,
        (
            "#01802FA-Ahaha...\x01",
            "It's quite the very strange title.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469E")

    label("loc_4671")


    ChrTalk(
        0x166,
        (
            "#14002FAhaha, you've\x01",
            "got a weird title.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469E")


    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Also, I will give you all\x01",
            "this premium as a reward\x01",
            "for having found me☆\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x54),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x54, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FAh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're welcome☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Then, it's time\x01",
            "for me to leave.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Make a lot of good memories at Wonderland\x01",
            "for the rest of the day, ok?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47F7():

        label("loc_47F7")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_47F7")

    QueueWorkItem2(0x101, 1, lambda_47F7)

    def lambda_4809():

        label("loc_4809")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_4809")

    QueueWorkItem2(0xEF, 1, lambda_4809)
    OP_95(0x1D, -1420, 0, -29670, 2000, 0x0)
    OP_95(0x1D, -1630, 230, -38320, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)

    def lambda_484B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_484B)
    Sleep(50)

    def lambda_485B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_485B)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_48C5")

    ChrTalk(
        0x101,
        (
            "#00012FHa ha...\x01",
            "Michey's younger sister too is\x01",
            "quite the intense character.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491A")

    label("loc_48C5")


    ChrTalk(
        0x101,
        (
            "#00012FHa ha...\x01",
            "Michey's younger sister too is\x01",
            "quite the intense character, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491A")

    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_497D")

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, you're right.\x02\x03",
            "#00100FThen, it's time for\x01",
            "me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_497D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4A0C")

    ChrTalk(
        0x103,
        (
            "#00204FUh uh, you are right.\x01",
            "It was a nicer character than rumors go.\x02\x03",
            "#00200FThen, it is time for me\x01",
            "to excuse myself too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4A6C")

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, you said it.\x02\x03",
            "#00300FThen, I guess it's time\x01",
            "for me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4AC5")

    ChrTalk(
        0x109,
        (
            "#10109FUh uh, you're right.\x02\x03",
            "#10100FThen, it's time\x01",
            "for me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4B18")

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, right.\x02\x03",
            "#10300FThen, I'll excuse\x01",
            "myself here too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4B81")

    ChrTalk(
        0x153,
        (
            "#01109FEheheh, I wanna see her again.\x02\x03",
            "#01104FAlright, then KeA\x01",
            "too will go have fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4BD4")

    ChrTalk(
        0x156,
        (
            "#06409FUh uh, really.\x02\x03",
            "#06400FThen, it's time for\x01",
            "me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4C32")

    ChrTalk(
        0x14C,
        (
            "#05904FUh uh, really.\x02\x03",
            "#05900FThen, I believe it is\x01",
            "time for me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4C9E")

    ChrTalk(
        0x134,
        (
            "#01709FUh uh, she was good.\x02\x03",
            "#01700FThen, I guess I'll go have\x01",
            "fun at another place too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4CFD")

    ChrTalk(
        0x135,
        (
            "#01809FUh uh, indeed.\x02\x03",
            "#01802FThen, it's time for me to\x01",
            "excuse myself here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4CFD")


    ChrTalk(
        0x166,
        (
            "#14006FTrue, she was a weirdo.\x02\x03",
            "#14000FThen, I'm gonna have fun\x01",
            "at a different place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D58")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4D8D")

    ChrTalk(
        0x101,
        "#00000FYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DAE")

    label("loc_4D8D")


    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    label("loc_4DAE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4DCF")
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_4E70")

    label("loc_4DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4DE0")
    RemoveParty(0x2, 0xFF)
    Jump("loc_4E70")

    label("loc_4DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4DF1")
    RemoveParty(0x3, 0xFF)
    Jump("loc_4E70")

    label("loc_4DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4E07")
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_4E70")

    label("loc_4E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4E18")
    RemoveParty(0x4, 0xFF)
    Jump("loc_4E70")

    label("loc_4E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4E29")
    RemoveParty(0x52, 0xFF)
    Jump("loc_4E70")

    label("loc_4E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4E3A")
    RemoveParty(0x55, 0xFF)
    Jump("loc_4E70")

    label("loc_4E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4E4B")
    RemoveParty(0x4B, 0xFF)
    Jump("loc_4E70")

    label("loc_4E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4E5C")
    RemoveParty(0x33, 0xFF)
    Jump("loc_4E70")

    label("loc_4E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4E6D")
    RemoveParty(0x34, 0xFF)
    Jump("loc_4E70")

    label("loc_4E6D")

    RemoveParty(0x65, 0xFF)

    label("loc_4E70")

    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Miichie's Challenge]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0xF)
    OP_29(0x7F, 0x4, 0x10)
    SetScenarioFlags(0x1C9, 7)
    OP_65(0x0, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x0, 10, 150, -36180, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_40EB end

    def Function_37_4EEB(): pass

    label("Function_37_4EEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("chr/ch23000.itc", 0x21)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x1E, 0x1000)
    SetChrFlags(0x1F, 0x1000)
    OP_68(1270, 2520, -36760, 0)
    MoveCamera(51, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11430, 0)
    SetChrPos(0x101, -300, 300, -43880, 0)
    SetChrPos(0x103, 770, 340, -44750, 0)
    SetChrPos(0x109, 3940, 150, -36320, 0)
    SetChrPos(0x105, 3870, 50, -34830, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_68(1110, 2520, -36960, 3000)
    SetCameraDistance(13230, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_5014():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5014)
    Sleep(50)

    def lambda_5031():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5031)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_50AE():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50AE)
    Sleep(50)

    def lambda_50BE():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_50BE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHey, Noｱl, Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50EF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_50EF)
    Sleep(50)

    def lambda_50FF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50FF)
    Sleep(300)

    def lambda_510F():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_510F)
    Sleep(50)

    def lambda_512C():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_512C)
    WaitChrThread(0x101, 1)

    def lambda_514A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_514A)
    Sleep(50)

    def lambda_515A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_515A)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10300FHu hu, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAh, please listen,\x01",
            "Mr. Lloyd!\x02\x03",
            "#10103FThat Wazy, as soon as\x01",
            "I avert my eyes from him he\x01",
            "immediately goes to have fun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, I'm not causing any\x01",
            "serious incidents, right?\x02\x03",
            "#10304FThen, don't you think\x01",
            "it's better to patrol\x01",
            "while having fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FDon't I think?\x01",
            "That's not the problem here, honestly...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    OP_79(0x0)
    Fade(250)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1E, -760, 1600, -21700, 180)
    SetChrPos(0x1F, 650, 1600, -21700, 180)
    OP_0D()
    TurnDirection(0x103, 0x1F, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FAh...\x01",
            "Mr. Lloyd, children.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's Voice")

    AnonymousTalk(
        0xFF,
        "#4SIt's Micheeey!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4SAh, and there's\x01",
            "Miichie too...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_53E5():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53E5)
    Sleep(50)

    def lambda_53F5():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_53F5)
    Sleep(50)

    def lambda_5405():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5405)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_70(0x0, 0x0)
    OP_68(-800, 2520, -37470, 3000)
    MoveCamera(43, 32, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(11660, 3000)

    def lambda_5498():
        OP_95(0xFE, -440, 60, -35850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5498)
    Sleep(100)

    def lambda_54B5():
        OP_95(0xFE, 710, 10, -34740, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_54B5)

    def lambda_54CF():

        label("loc_54CF")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_54CF")

    QueueWorkItem2(0x109, 1, lambda_54CF)

    def lambda_54E1():

        label("loc_54E1")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_54E1")

    QueueWorkItem2(0x105, 1, lambda_54E1)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    def lambda_54FF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_54FF)
    Sleep(50)

    def lambda_550F():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_550F)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05528F(...I failed to hide.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Hiya, kick!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    BeginChrThread(0x1E, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x1F, 3, 0, 38)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F(Wait a...!?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FPfft...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FW-Wait, you can't do that!\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Big sis, you don't know?\x01",
            "If you kick Michey,\x01",
            "you'll get lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "They say luck is\x01",
            "packed in his butt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Kyah ha ha ha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F(L-Luck...I never heard about it!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    WaitChrThread(0x1E, 3)
    OP_64(0x101)

    def lambda_5697():
        TurnDirection(0x1E, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_5697)
    Sleep(50)
    TurnDirection(0x1F, 0x103, 500)

    ChrTalk(
        0x1F,
        "I wonder if I can kick her too?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F(......!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(W-What do I do?\x01",
            "I must do something about this...)\x07\x00\x02",
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
            "Scold Them Harshly\x01",      # 0
            "Tickle Them\x01",             # 1
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
        (0, "loc_57B6"),
        (1, "loc_5884"),
        (SWITCH_DEFAULT, "loc_5997"),
    )


    label("loc_57B6")

    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "H-Heey!\x01",
            "No more than this!\x02\x03",
            "Even I won't forgive you, \x01",
            "you know!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "Uwaaah, Michey's got mad!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Run awaaay!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x3)
    Jump("loc_5997")

    label("loc_5884")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 6)
    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "To the kids who do that...\x01",
            "I do thiiis!\x02\x03",
            "*tickle tickle tickle*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_9C(0x1E, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    OP_63(0x1E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x1E,
        (
            "Eeek...\x01",
            "Kyah ha ha ha ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Yaay, it's Michey's\x01",
            "counterattack!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Run awaaay!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x4)
    Jump("loc_5997")

    label("loc_5997")


    def lambda_599C():
        OP_97(0xFE, 0xFFFFF95C, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_599C)
    Sleep(100)

    def lambda_59B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_59B9)
    WaitChrThread(0x1F, 1)

    def lambda_59D7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_59D7)

    def lambda_59F1():

        label("loc_59F1")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_59F1")

    QueueWorkItem2(0x101, 1, lambda_59F1)

    def lambda_5A03():

        label("loc_5A03")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5A03")

    QueueWorkItem2(0x103, 1, lambda_5A03)

    def lambda_5A15():

        label("loc_5A15")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5A15")

    QueueWorkItem2(0x109, 1, lambda_5A15)

    def lambda_5A27():

        label("loc_5A27")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5A27")

    QueueWorkItem2(0x105, 1, lambda_5A27)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_93(0x105, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x109, 0xB4, 0x1F4)
    OP_0D()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F*sigh*, they went away, eh?\x02\x03",
            "#05206FI can't believe I was kicked out of the blue...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5AD1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AD1)
    Sleep(50)

    def lambda_5AE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5AE1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FIt seems that recently\x01",
            "that thing is in vogue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FAhaha...how unlucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203FBut...was it all right, I wonder?\x01",
            "I unintentionally did such a thing...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD3")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F...I think it was better\x01",
            "than yelling at them.\x02\x03",
            "#05520FMichey is a soothing being,\x01",
            "so you can't choose a measure\x01",
            "like driving them away.\x02\x03",
            "#05522FMr. Lloyd, I wouldn't have expected\x01",
            "any less from your judgment ability.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202FHa ha...\x01",
            "Thanks.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E51")

    label("loc_5CD3")

    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 700, 450, -35880, 315, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Sound(2031, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FAck!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)
    Sound(2681, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F...No good at all.\x02\x03",
            "#05526FMichey is a soothing being,\x01",
            "so you can't choose a measure\x01",
            "like driving them away.\x02\x03",
            "#05520FYou should've chosen a more...\x01",
            "Peaceful way to drive them away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FT-That's complex...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E51")


    ChrTalk(
        0x109,
        (
            "#10100FWell, I'm glad that they\x01",
            "didn't kicked Tio too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, just like a knight protecting\x01",
            "his little sister, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FAlthough it doesn't\x01",
            "match this outfit...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FIncidentally, I heard that Michey's\x01",
            "butt is sturdy, so even if kicked\x01",
            "you should be all right.\x02\x03",
            "#05520FIt hurt less than expected, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FI-Indeed, that's true...\x02\x03",
            "#05203F(There's cushioning or something inside.\x01",
            "It's no wonder it's stiff...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F...Ah, Mr. Lloyd.\x01",
            "It is time we must go\x01",
            "to the next area.\x02\x03",
            "#05524FThe morning schedule\x01",
            "is very tight.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FG-Got it.\x01",
            "...Then, see you later,\x01",
            "Noｱl, Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FPlease, do your best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, see you later.\x02",
    )

    CloseMessageWindow()

    def lambda_6127():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6127)
    Sleep(1000)

    def lambda_6144():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6144)
    Sleep(50)

    def lambda_6161():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6161)
    Sleep(50)

    def lambda_6171():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6171)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1330", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4EEB end

    def Function_38_6194(): pass

    label("Function_38_6194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_61CE")
    OP_99(0xFE, 0x101, 0xFA, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    Sound(862, 0, 20, 0)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Jump("Function_38_6194")

    label("loc_61CE")

    Return()

    # Function_38_6194 end

    def Function_39_61CF(): pass

    label("Function_39_61CF")

    Sleep(1000)

    label("loc_61D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F4")
    Sound(918, 0, 70, 0)
    Sleep(2200)
    Sound(918, 0, 60, 0)
    Sleep(5000)
    Jump("loc_61D2")

    label("loc_61F4")

    Return()

    # Function_39_61CF end

    SaveToFile()

Try(main)
