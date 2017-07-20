from ScenarioHelper import *

def main():
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
        "Erie",                 # 1
        "Randy",               # 2
        "Noel",                 # 3
        "Waji",                   # 4
        "Keya",                 # 5
        "Franc",                 # 6
        "Cecil",                 # 7
        "Ilia",                 # 8
        "Lisha",               # 9
        "Shuri",                 # 10
        "Missi",               # 11
        "Marsun",               # 12
        "corona",                 # 13
        "Lima",                   # 14
        "MWL staff",         # 15
        "tourist",                 # 16
        "tourist",                 # 17
        "tourist",                 # 18
        "tourist",                 # 19
        "tourist",                 # 20
        "Eidolon",                   # 21
        "Misee",               # 22
        "boy",                 # 23
        "boy",                 # 24
        "SE control",                 # 25
        "bt1450",                 # 26
        "Directions to Wonderland entrance square",# 27
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

    PlaceName(-0.05999999865889549, 0.0, -140.4499969482422, 0x0000, 0x0000, "Directions to Wonderland entrance square")

    ChipFrameInfo(1620, 0)                                       # 0

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_7A7",          # 02, 2
        "Function_3_94F",          # 03, 3
        "Function_4_A3D",          # 04, 4
        "Function_5_BD3",          # 05, 5
        "Function_6_CE6",          # 06, 6
        "Function_7_DD6",          # 07, 7
        "Function_8_EE1",          # 08, 8
        "Function_9_F8A",          # 09, 9
        "Function_10_1014",        # 0A, 10
        "Function_11_10DA",        # 0B, 11
        "Function_12_1255",        # 0C, 12
        "Function_13_1355",        # 0D, 13
        "Function_14_143F",        # 0E, 14
        "Function_15_164F",        # 0F, 15
        "Function_16_171D",        # 10, 16
        "Function_17_1811",        # 11, 17
        "Function_18_18DF",        # 12, 18
        "Function_19_19C7",        # 13, 19
        "Function_20_1ABC",        # 14, 20
        "Function_21_1BCE",        # 15, 21
        "Function_22_1C3A",        # 16, 22
        "Function_23_1C9B",        # 17, 23
        "Function_24_1CED",        # 18, 24
        "Function_25_1DAA",        # 19, 25
        "Function_26_1E7A",        # 1A, 26
        "Function_27_1FE6",        # 1B, 27
        "Function_28_284C",        # 1C, 28
        "Function_29_2871",        # 1D, 29
        "Function_30_291C",        # 1E, 30
        "Function_31_293C",        # 1F, 31
        "Function_32_2C06",        # 20, 32
        "Function_33_2C2A",        # 21, 33
        "Function_34_353B",        # 22, 34
        "Function_35_3E3B",        # 23, 35
        "Function_36_3E7B",        # 24, 36
        "Function_37_4CD8",        # 25, 37
        "Function_38_5EFD",        # 26, 38
        "Function_39_5F38",        # 27, 39
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89B")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_A39")

    label("loc_968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_A39")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_A39")

    label("loc_994")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28")

    ChrTalk(
        0x8,
        (
            "#00100FA little while ago from the castle\x01",
            "I heard the sound of a beautiful bell.\x02\x03",
            "#00109FHuhuu, somewhere couple\x01",
            "I wonder if I am wishing a mirror.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A39")

    label("loc_A28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A39")

    label("loc_A39")

    TalkEnd(0xFE)
    Return()

    # Function_3_94F end

    def Function_4_A3D(): pass

    label("Function_4_A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56")
    Jump("loc_BCF")

    label("loc_A56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    Jump("loc_BCF")

    label("loc_A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A82")
    Jump("loc_BCF")

    label("loc_A82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A98")
    Jump("loc_BCF")

    label("loc_A98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(
        0x9,
        (
            "#00302FIn the night, the castle of that mirror is also\x01",
            "It seems to be lighted up.\x02\x03",
            "#00304FTogether with fireworks and parades,\x01",
            "Just at the theme park day\x01",
            "It seems that I feel like finishing off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BCF")

    label("loc_B58")


    ChrTalk(
        0x9,
        (
            "#00302FBecause it's a corner, I will have a night section\x01",
            "With a beautiful older sister\x01",
            "I wanted to spend it … …\x02\x03",
            "#00306FWell, I have a dinner party\x01",
            "See you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCF")

    TalkEnd(0xFE)
    Return()

    # Function_4_A3D end

    def Function_5_BD3(): pass

    label("Function_5_BD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEC")
    Jump("loc_CE2")

    label("loc_BEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C02")
    Jump("loc_CE2")

    label("loc_C02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C18")
    Jump("loc_CE2")

    label("loc_C18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1")

    ChrTalk(
        0xA,
        (
            "#10103FRumors of \"mirror that wishes wishes\" …\x01",
            "Does your wish really come true?\x02\x03",
            "#10100F\"There is no smoke without fire\"\x01",
            "I will also say, after all a bit\x01",
            "I expect it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE2")

    label("loc_CD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE2")

    label("loc_CE2")

    TalkEnd(0xFE)
    Return()

    # Function_5_BD3 end

    def Function_6_CE6(): pass

    label("Function_6_CE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFF")
    Jump("loc_DD2")

    label("loc_CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D15")
    Jump("loc_DD2")

    label("loc_D15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38")
    Call(0, 7)
    Jump("loc_DA6")

    label("loc_D38")


    ChrTalk(
        0xB,
        (
            "#10302FDo not believe it is not fun ….?\x01",
            "Huff, it is indeed true.\x02\x03",
            "#10304FWell, I also at best\x01",
            "I guess it will be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA6")

    Jump("loc_DD2")

    label("loc_DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    Jump("loc_DD2")

    label("loc_DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD2")

    label("loc_DD2")

    TalkEnd(0xFE)
    Return()

    # Function_6_CE6 end

    def Function_7_DD6(): pass

    label("Function_7_DD6")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "#10300F\"Mirror that fulfills wishes\" …\x02\x03",
            "#10302FReally,\x01",
            "Do you think the wish will come true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#06409FOf course!\x02\x03",
            "#06400FBecause, if you do not believe so\x01",
            "Also attractions\x01",
            "It is not fun ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#10300FHuh, I see.\x01",
            "That's true.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_DD6 end

    def Function_8_EE1(): pass

    label("Function_8_EE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F07")
    Call(0, 9)
    Jump("loc_F2E")

    label("loc_F07")


    ChrTalk(
        0xC,
        "#01109FMirror castle, it is really big!\x02",
    )

    CloseMessageWindow()

    label("loc_F2E")

    Jump("loc_F86")

    label("loc_F33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F49")
    Jump("loc_F86")

    label("loc_F49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F")
    Jump("loc_F86")

    label("loc_F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F75")
    Jump("loc_F86")

    label("loc_F75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F86")

    label("loc_F86")

    TalkEnd(0xFE)
    Return()

    # Function_8_EE1 end

    def Function_9_F8A(): pass

    label("Function_9_F8A")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01109FWow ah ……\x01",
            "Mirror castle, it is really big!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#14005FOh …… Looking closer\x01",
            "Zen is different …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_F8A end

    def Function_10_1014(): pass

    label("Function_10_1014")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102D")
    Jump("loc_10D6")

    label("loc_102D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1043")
    Jump("loc_10D6")

    label("loc_1043")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1066")
    Call(0, 7)
    Jump("loc_10AA")

    label("loc_1066")


    ChrTalk(
        0xD,
        (
            "#06409FThe theme park attraction is\x01",
            "Have fun and be a Nambo ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_10D6")

    label("loc_10AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C5")
    Jump("loc_10D6")

    label("loc_10C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D6")

    label("loc_10D6")

    TalkEnd(0xFE)
    Return()

    # Function_10_1014 end

    def Function_11_10DA(): pass

    label("Function_11_10DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_1251")

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BF")

    ChrTalk(
        0xE,
        (
            "#05900FHuhu, only popular people\x01",
            "To be with big star ia,\x01",
            "It is a sight that is hard to see.\x02\x03",
            "#05909FPerhaps, what mind is amazing\x01",
            "I wonder if it is two-shot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_120F")

    label("loc_11BF")


    ChrTalk(
        0xE,
        (
            "#05909FMr. and Mr. Iria are together,\x01",
            "What a damn two-shot what?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120F")

    Jump("loc_1251")

    label("loc_1214")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122A")
    Jump("loc_1251")

    label("loc_122A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1240")
    Jump("loc_1251")

    label("loc_1240")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")

    label("loc_1251")

    TalkEnd(0xFE)
    Return()

    # Function_11_10DA end

    def Function_12_1255(): pass

    label("Function_12_1255")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")
    Jump("loc_1351")

    label("loc_126E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1291")
    Call(0, 13)
    Jump("loc_130F")

    label("loc_1291")


    ChrTalk(
        0xF,
        (
            "#01705FAnd, as long as you are together\x01",
            "People are gonna get together.\x02\x03",
            "#01702FToday I am with my friends,\x01",
            "I will be rude here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130F")

    Jump("loc_1351")

    label("loc_1314")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132A")
    Jump("loc_1351")

    label("loc_132A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1340")
    Jump("loc_1351")

    label("loc_1340")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1351")

    label("loc_1351")

    TalkEnd(0xFE)
    Return()

    # Function_12_1255 end

    def Function_13_1355(): pass

    label("Function_13_1355")

    OP_4B(0xF, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Oh, maybe ….\x01",
            "Of alkane shell\x01",
            "Is not it ilia ~?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, from before\x01",
            "I'm supposed to support you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01700FHuh, I guess well\x01",
            "I will see you in the city.\x02\x03",
            "#01709FLet 's keep trying each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_1355 end

    def Function_14_143F(): pass

    label("Function_14_143F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1458")
    Jump("loc_164B")

    label("loc_1458")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146E")
    Jump("loc_164B")

    label("loc_146E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1484")
    Jump("loc_164B")

    label("loc_1484")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149A")
    Jump("loc_164B")

    label("loc_149A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A6")

    ChrTalk(
        0x10,
        (
            "#01802FWhen around this time at night\x01",
            "They are filled with couples.\x02\x03",
            "#01804FIt seems to be a full moon tonight … …\x01",
            "The moonlight reflected on the lake\x01",
            "It will be a beautiful landscape.\x02\x03",
            "#01809FHuhu, just by imagining\x01",
            "You will feel romantic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_164B")

    label("loc_15A6")


    ChrTalk(
        0x10,
        (
            "#01802FIt seems to be a full moon tonight … …\x01",
            "The moonlight reflected on the lake\x01",
            "The neighborhood should be very beautiful.\x02\x03",
            "#01809FHuhu, just by imagining\x01",
            "You will feel romantic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    TalkEnd(0xFE)
    Return()

    # Function_14_143F end

    def Function_15_164F(): pass

    label("Function_15_164F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")
    Call(0, 9)
    Jump("loc_16C1")

    label("loc_1675")


    ChrTalk(
        0x11,
        (
            "#14005FIs it so big to see nearby …?\x01",
            "I was feeling sluggish somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C1")

    Jump("loc_1719")

    label("loc_16C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DC")
    Jump("loc_1719")

    label("loc_16DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F2")
    Jump("loc_1719")

    label("loc_16F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1708")
    Jump("loc_1719")

    label("loc_1708")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1719")

    label("loc_1719")

    TalkEnd(0xFE)
    Return()

    # Function_15_164F end

    def Function_16_171D(): pass

    label("Function_16_171D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1736")
    Jump("loc_180D")

    label("loc_1736")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1759")
    Call(0, 13)
    Jump("loc_17CB")

    label("loc_1759")


    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I saw Iria,\x01",
            "I'm impressed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, then\x01",
            "Enjoying it quite well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CB")

    Jump("loc_180D")

    label("loc_17D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E6")
    Jump("loc_180D")

    label("loc_17E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FC")
    Jump("loc_180D")

    label("loc_17FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180D")

    label("loc_180D")

    TalkEnd(0xFE)
    Return()

    # Function_16_171D end

    def Function_17_1811(): pass

    label("Function_17_1811")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182A")
    Jump("loc_18DB")

    label("loc_182A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1840")
    Jump("loc_18DB")

    label("loc_1840")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1856")
    Jump("loc_18DB")

    label("loc_1856")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CA")

    ChrTalk(
        0x13,
        (
            "Inside the mirror's castle\x01",
            "It was very fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Again, at the theme park\x01",
            "I felt like I came.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DB")

    label("loc_18CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DB")

    label("loc_18DB")

    TalkEnd(0xFE)
    Return()

    # Function_17_1811 end

    def Function_18_18DF(): pass

    label("Function_18_18DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F8")
    Jump("loc_19C3")

    label("loc_18F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190E")
    Jump("loc_19C3")

    label("loc_190E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1924")
    Jump("loc_19C3")

    label("loc_1924")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B2")

    ChrTalk(
        0x14,
        (
            "The ascending and descending of that long staircase\x01",
            "I was a little tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But, Lima was pleased as well\x01",
            "It was worth having trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C3")

    label("loc_19B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C3")

    label("loc_19C3")

    TalkEnd(0xFE)
    Return()

    # Function_18_18DF end

    def Function_19_19C7(): pass

    label("Function_19_19C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E0")
    Jump("loc_1AB8")

    label("loc_19E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F6")
    Jump("loc_1AB8")

    label("loc_19F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0C")
    Jump("loc_1AB8")

    label("loc_1A0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA7")

    ChrTalk(
        0x15,
        (
            "I was in a castle with my dad.\x01",
            "I rang the bell ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, \"Everyone else\x01",
            "Let's play together\x01",
            "I asked for your wishes ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB8")

    label("loc_1AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB8")

    label("loc_1AB8")

    TalkEnd(0xFE)
    Return()

    # Function_19_19C7 end

    def Function_20_1ABC(): pass

    label("Function_20_1ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BCA")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Welcome to \"Mirror Castle\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here, there is a \"mirror that can fulfill wishes\"\x01",
            "Explore the castle, aiming for the top floor\x01",
            "It is an attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Mika and hide and seek in … …\x01",
            "What I am playing at attractions now\x01",
            "Let's stop it. )\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1BCD")

    label("loc_1BCA")

    Call(0, 33)

    label("loc_1BCD")

    Return()

    # Function_20_1ABC end

    def Function_21_1BCE(): pass

    label("Function_21_1BCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C36")

    ChrTalk(
        0xFE,
        (
            "Of that big castle\x01",
            "Do you climb up to the top …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… It looks quite tense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C36")

    label("loc_1C36")

    TalkEnd(0xFE)
    Return()

    # Function_21_1BCE end

    def Function_22_1C3A(): pass

    label("Function_22_1C3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C97")

    ChrTalk(
        0xFE,
        (
            "This child is for something,\x01",
            "Hang on to her husband too\x01",
            "I have to climb.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C97")

    label("loc_1C97")

    TalkEnd(0xFE)
    Return()

    # Function_22_1C3A end

    def Function_23_1C9B(): pass

    label("Function_23_1C9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE9")

    ChrTalk(
        0xFE,
        (
            "It's exciting!\x01",
            "What shall I ask Kagami?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE9")

    label("loc_1CE9")

    TalkEnd(0xFE)
    Return()

    # Function_23_1C9B end

    def Function_24_1CED(): pass

    label("Function_24_1CED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D55")

    ChrTalk(
        0xFE,
        "Now, let's enter the castle at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And romantically\x01",
            "Let's spend it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA6")

    label("loc_1D55")


    ChrTalk(
        0xFE,
        "It is the night's part from now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, have an eccentric night.\x01",
            "Let's have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA6")

    TalkEnd(0xFE)
    Return()

    # Function_24_1CED end

    def Function_25_1DAA(): pass

    label("Function_25_1DAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E12")

    ChrTalk(
        0xFE,
        "Hehe, it is a very nice castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow in a fairy tale world\x01",
            "It seems they came.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E76")

    label("loc_1E12")


    ChrTalk(
        0xFE,
        (
            "In the castle of the mirror, with him\x01",
            "A romantic time\x01",
            "I had you spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I'm looking forward to the night.\x02",
    )

    CloseMessageWindow()

    label("loc_1E76")

    TalkEnd(0xFE)
    Return()

    # Function_25_1DAA end

    def Function_26_1E7A(): pass

    label("Function_26_1E7A")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED1")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_1FE5")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F00")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_1FE5")

    label("loc_1F00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2A")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_1FE5")

    label("loc_1F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB1")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_1F83")
    SetChrFlags(0x8, 0x80)
    Jump("loc_1F91")

    label("loc_1F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_1F91")
    SetChrFlags(0xA, 0x80)

    label("loc_1F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FAC")
    ClearChrFlags(0x1D, 0x80)

    label("loc_1FAC")

    Jump("loc_1FE5")

    label("loc_1FB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE5")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)

    label("loc_1FE5")

    Return()

    # Function_26_1E7A end

    def Function_27_1FE6(): pass

    label("Function_27_1FE6")

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

    def lambda_2171():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2171)
    Sleep(50)

    def lambda_2189():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2189)
    Sleep(50)

    def lambda_21A1():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_21A1)
    Sleep(50)

    def lambda_21B9():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21B9)
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
            "#00303F#6PThe Castle of Mirrors\x02\x03",
            "#00301FJust a theme park\x01",
            "I thought it was a monument … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P… … clearly spirit pressure\x01",
            "It is rising from this castle.\x02\x03",
            "#00201FMost likely on the top floor \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5P…… Could it be this Castle?\x01",
            "It was built with the proposal of \"her\"\x01",
            "I've heard of it … ….\x02\x03",
            "#00108FBut it couldn't be…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PAnyway let's head in\x02\x03",
            "#00001FIf we're lucky we can get to the top floor-\x02",
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

    def lambda_2570():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2570)
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

    def lambda_2638():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2638)
    Sleep(50)

    def lambda_2650():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2650)
    Sleep(50)

    def lambda_2668():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2668)
    Sleep(50)

    def lambda_2680():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2680)
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
        "#00110F#1PThe one from the old mine\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#1PTits …!\x01",
            "Are you going to be the gatekeeper of the castle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#1P─ ─ Battle preparation!\x01",
            "Defeat at full power!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(60, 80, -1, -1)
    SetChrName("Friends")

    AnonymousTalk(
        0xFF,
        "#4S#5PRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2220, 5100, -59370, 1500)
    SetCameraDistance(11500, 1500)

    def lambda_27AD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27AD)

    def lambda_27C2():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27C2)

    def lambda_27D7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D7)

    def lambda_27EC():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27EC)
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

    # Function_27_1FE6 end

    def Function_28_284C(): pass

    label("Function_28_284C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2870")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_28_284C")

    label("loc_2870")

    Return()

    # Function_28_284C end

    def Function_29_2871(): pass

    label("Function_29_2871")

    OP_74(0x1, 0x5)

    label("loc_2875")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A7")
    OP_71(0x1, 0x137, 0x13C, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x13C, 0x137, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_2875")

    label("loc_28A7")

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

    # Function_29_2871 end

    def Function_30_291C(): pass

    label("Function_30_291C")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x78, 0x8C, 0x12C, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_30_291C end

    def Function_31_293C(): pass

    label("Function_31_293C")

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

    def lambda_2B6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2B6E)
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

    # Function_31_293C end

    def Function_32_2C06(): pass

    label("Function_32_2C06")

    OP_74(0x1, 0x19)
    OP_71(0x1, 0x50, 0x5A, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x6D, 0x0, 0x20)
    Return()

    # Function_32_2C06 end

    def Function_33_2C2A(): pass

    label("Function_33_2C2A")

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
        "Welcome to \"Mirror Castle\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Here, there is a \"mirror that can fulfill wishes\"\x01",
            "Explore the castle, aiming for the top floor\x01",
            "It is an attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If it's okay, with someone\x01",
            "Although we recommend you to enter the entrance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(… … Who should I invite?)\x02",
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
            "#1KWho invites you?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Erie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noel")
    MenuCmd(1, 0, "Waji")
    MenuCmd(1, 0, "Keya")
    MenuCmd(1, 0, "Franc")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilia")
    MenuCmd(1, 0, "Lisha")
    MenuCmd(1, 0, "Shuri")
    MenuCmd(1, 0, "quit")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E33")
    MenuCmd(3, 0, 0x0)

    label("loc_2E33")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E45")
    MenuCmd(3, 0, 0x1)

    label("loc_2E45")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E57")
    MenuCmd(3, 0, 0x2)

    label("loc_2E57")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E69")
    MenuCmd(3, 0, 0x3)

    label("loc_2E69")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E7B")
    MenuCmd(3, 0, 0x4)

    label("loc_2E7B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E8D")
    MenuCmd(3, 0, 0x5)

    label("loc_2E8D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E9F")
    MenuCmd(3, 0, 0x6)

    label("loc_2E9F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EB1")
    MenuCmd(3, 0, 0x7)

    label("loc_2EB1")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EC3")
    MenuCmd(3, 0, 0x8)

    label("loc_2EC3")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2ED5")
    MenuCmd(3, 0, 0x9)

    label("loc_2ED5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2EE7")
    MenuCmd(3, 0, 0xA)

    label("loc_2EE7")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D7")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F81"),
        (1, "loc_2FC1"),
        (2, "loc_3001"),
        (3, "loc_3043"),
        (4, "loc_3083"),
        (5, "loc_30C1"),
        (6, "loc_3101"),
        (7, "loc_3141"),
        (8, "loc_3183"),
        (9, "loc_31C7"),
        (10, "loc_3209"),
        (SWITCH_DEFAULT, "loc_3249"),
    )


    label("loc_2F81")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Ellie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_2FC1")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Tio.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3001")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Randy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3043")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Noel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3083")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Wazi.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_30C1")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Ka'a.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3101")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite the franc.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3141")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Cecil 's older sister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3183")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Iria.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_31C7")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Leisha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3209")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Sri.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3249")

    FadeToDark(500, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32A0"),
        (1, "loc_32A9"),
        (2, "loc_32B2"),
        (3, "loc_32BB"),
        (4, "loc_32C4"),
        (5, "loc_32CD"),
        (6, "loc_32D6"),
        (7, "loc_32DF"),
        (8, "loc_32E8"),
        (9, "loc_32F1"),
        (10, "loc_32FA"),
        (SWITCH_DEFAULT, "loc_3303"),
    )


    label("loc_32A0")

    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32A9")

    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32B2")

    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32BB")

    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32C4")

    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32CD")

    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32D6")

    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32DF")

    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32E8")

    AddParty(0x33, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32F1")

    AddParty(0x34, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_32FA")

    AddParty(0x65, 0xEF, 0xFF)
    Jump("loc_3303")

    label("loc_3303")

    SetChrPos(0x101, -500, 1030, -24600, 0)
    SetChrPos(0xEF, 500, 1030, -24600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x16,
        "Well, we will keep your tickets.\x02",
    )

    CloseMessageWindow()
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I handed one ticket to the staff.\x07\x00\x02",
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
        "Certainly, I kept you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Exploring the fantastic \"Mirror Castle\"\x01",
            "Please please enjoy … …\x02",
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

    def lambda_344E():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_344E)
    OP_93(0x16, 0x5A, 0x1F4)
    WaitChrThread(0x16, 1)
    Sleep(300)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)

    def lambda_348C():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_348C)
    Sleep(50)

    def lambda_34A4():
        OP_9B(0x0, 0xEF, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_34A4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1401", 0, 0, 0)
    IdleLoop()
    Jump("loc_3523")

    label("loc_34D7")


    ChrTalk(
        0x16,
        "Oh, will you stop it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Welcoming your visit\x01",
            "I am waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3523")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -28000, 180)
    EventEnd(0x5)
    Return()

    # Function_33_2C2A end

    def Function_34_353B(): pass

    label("Function_34_353B")

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
        (0, "loc_3603"),
        (1, "loc_36A4"),
        (2, "loc_373E"),
        (3, "loc_37D6"),
        (4, "loc_386B"),
        (5, "loc_3910"),
        (6, "loc_39C7"),
        (7, "loc_3A63"),
        (8, "loc_3B0C"),
        (9, "loc_3BC1"),
        (10, "loc_3C61"),
        (SWITCH_DEFAULT, "loc_3CF7"),
    )


    label("loc_3603")


    ChrTalk(
        0x102,
        (
            "#00102FHuhu, walk along the castle together\x01",
            "It was a lot of fun.\x02\x03",
            "#00100FWell then,\x01",
            "I will go soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuhu, also.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_36A4")


    ChrTalk(
        0x103,
        (
            "#00202FCastle of the mirror …\x01",
            "It was fun to turn around.\x02\x03",
            "#00202FWell then, I will excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWell, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_373E")


    ChrTalk(
        0x104,
        (
            "#00302FHaha, even two men\x01",
            "I enjoyed pretty much.\x02\x03",
            "#00300FOkay, I'm going else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_37D6")


    ChrTalk(
        0x109,
        (
            "#10109FThe castle of the mirror, it was fun.\x02\x03",
            "#10100FThen, I will excuse myself here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, I will come back later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_386B")


    ChrTalk(
        0x105,
        (
            "#10304FCastle of the mirror …\x01",
            "It was quite interesting.\x02\x03",
            "#10300FWell then, then I\x01",
            "I guess it's going to turn around elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, and more.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3910")


    ChrTalk(
        0x153,
        (
            "#01109FWow, it was a big castle.\x01",
            "It was a lot of fun!\x02\x03",
            "#01100FWell then,\x01",
            "I will go to another tokoro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FWell, see you again Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_39C7")


    ChrTalk(
        0x156,
        (
            "#06409FHehe, the castle of the mirror …\x01",
            "it was very fun!\x02\x03",
            "#06400FWell then, I will excuse ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06400FYes, but also!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3A63")


    ChrTalk(
        0x14C,
        (
            "#05902FHuhu, big mirrors and bells are seen\x01",
            "It was a lot of fun.\x02\x03",
            "#05900FWell, I'm in another place\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FWell then, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3B0C")


    ChrTalk(
        0x134,
        (
            "#01709FHuhu, quite\x01",
            "It was a wonderful castle.\x02\x03",
            "#01700FWell then, then I\x01",
            "I have gone to other Toko.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01700FWell, that's it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3BC1")


    ChrTalk(
        0x135,
        (
            "#01809FHehe, walking through a beautiful castle is\x01",
            "it was very fun.\x02\x03",
            "#01802FWell then, I am with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3C61")


    ChrTalk(
        0x166,
        (
            "#14002F…… I walked the castle\x01",
            "It was pretty fun.\x02\x03",
            "#14000FOkay, I will go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14000FYeah, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3CF7")

    BeginChrThread(0xEF, 3, 0, 35)
    WaitChrThread(0xEF, 3)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3D4C"),
        (1, "loc_3D5A"),
        (2, "loc_3D68"),
        (3, "loc_3D76"),
        (4, "loc_3D84"),
        (5, "loc_3D92"),
        (6, "loc_3DA0"),
        (7, "loc_3DAE"),
        (8, "loc_3DBC"),
        (9, "loc_3DCA"),
        (10, "loc_3DD8"),
        (SWITCH_DEFAULT, "loc_3DE6"),
    )


    label("loc_3D4C")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3D5A")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3D68")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3D76")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3D84")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3D92")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DA0")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DAE")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DBC")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DCA")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DD8")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3DE6")

    label("loc_3DE6")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E23")
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3E23")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -29000, 180)
    EventEnd(0x5)
    Return()

    # Function_34_353B end

    def Function_35_3E3B(): pass

    label("Function_35_3E3B")


    def lambda_3E40():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E40)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3E54():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E54)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xFE, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_35_3E3B end

    def Function_36_3E7B(): pass

    label("Function_36_3E7B")

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
        "#00000FI found it……!\x02",
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
            "Kyat, I found it ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, sir, my wonderful ne ~!\x07\x00\x02",
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
            "In this short period this me\x01",
            "I will not find five times ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, this is perfectly\x01",
            "It is my defeat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "This is exactly what the father is\x01",
            "King of hide and seekyo yo ~ ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_40F6")
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_416E")

    label("loc_40F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4116")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_416E")

    label("loc_4116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4136")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_416E")

    label("loc_4136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4156")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_416E")

    label("loc_4156")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_416E")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FKing, of hide and se …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_41E2")

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, a magical title\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_41E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_421E")

    ChrTalk(
        0x103,
        (
            "#00202FThinkingly ……\x01",
            "It is loose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_421E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_425C")

    ChrTalk(
        0x104,
        (
            "#00302FA funny title\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_425C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_42A4")

    ChrTalk(
        0x109,
        (
            "#10102FHaha … … Have a funny title\x01",
            "You got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_42A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_42F0")

    ChrTalk(
        0x105,
        (
            "#10309FHugh, it's pretty cool\x01",
            "You can name it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_42F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_431F")

    ChrTalk(
        0x153,
        "#01109FLloyd, cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_431F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4369")

    ChrTalk(
        0x156,
        (
            "#06409FHuh, you have an interesting title\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_4369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_439C")

    ChrTalk(
        0x14C,
        "#05902FHehe, this is a cute name.\x02",
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_439C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_43D3")

    ChrTalk(
        0x134,
        "#01702FHuh, it's quite nice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_43D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4419")

    ChrTalk(
        0x135,
        (
            "#01802FOh, haha ….\x01",
            "What a fancy title.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_4419")


    ChrTalk(
        0x166,
        (
            "#14002FHaha,\x01",
            "I got a strange name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444D")


    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Also, to the elders\x01",
            "To the reward that found me,\x01",
            "I give this prize Yo ~ ☆\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '咪雪挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('咪雪挂饰', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, you're welcome ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Well then, I guess so.\x01",
            "I want you to break away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "The rest of the day, in Wonderland\x01",
            "Make good memories well!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45C4():

        label("loc_45C4")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_45C4")

    QueueWorkItem2(0x101, 1, lambda_45C4)

    def lambda_45D6():

        label("loc_45D6")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_45D6")

    QueueWorkItem2(0xEF, 1, lambda_45D6)
    OP_95(0x1D, -1420, 0, -29670, 2000, 0x0)
    OP_95(0x1D, -1630, 230, -38320, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)

    def lambda_4618():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4618)
    Sleep(50)

    def lambda_4628():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4628)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_468E")

    ChrTalk(
        0x101,
        (
            "#00012Fmy mother……\x01",
            "Mihichi's sister is also said\x01",
            "It was quite a strong character.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46DB")

    label("loc_468E")


    ChrTalk(
        0x101,
        (
            "#00012Fmy mother……\x01",
            "Mihichi's sister is also said\x01",
            "It was quite intense character.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46DB")

    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4741")

    ChrTalk(
        0x102,
        (
            "#00104FHehe, that's right.\x02\x03",
            "#00100FWell then, I'm almost done.\x01",
            "I will let you go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_47BF")

    ChrTalk(
        0x103,
        (
            "#00204FHehe, it is.\x01",
            "It was a good character beyond rumors.\x02\x03",
            "#00200FWell then, I will soon\x01",
            "I will excuse myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_47BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4822")

    ChrTalk(
        0x104,
        (
            "#00309FHaha, that's right.\x02\x03",
            "#00300FThen, I'll be around soon.\x01",
            "I will let you go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4887")

    ChrTalk(
        0x109,
        (
            "#10109FHehe, it is.\x02\x03",
            "#10100FWell, I'm almost at it\x01",
            "I will go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_48E6")

    ChrTalk(
        0x105,
        (
            "#10309FHuh, that's right.\x02\x03",
            "#10300FWell then, I will also be around here\x01",
            "I will be rude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_48E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_494D")

    ChrTalk(
        0x153,
        (
            "#01109FWell, I want to see you again.\x02\x03",
            "#01104FOkay then Ka'aa\x01",
            "I'm going to play!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_494D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_49B4")

    ChrTalk(
        0x156,
        (
            "#06409FHehe, it is true.\x02\x03",
            "#06400FWell then, I'm almost done.\x01",
            "I will let you go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_49B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4A17")

    ChrTalk(
        0x14C,
        (
            "#05904FHehe, really.\x02\x03",
            "#05900FWell then, I'm almost done.\x01",
            "I'm gonna let you go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4A82")

    ChrTalk(
        0x134,
        (
            "#01709FHuh, it was good.\x02\x03",
            "#01700FWell then, me too\x01",
            "I'm going to play in another place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4AE5")

    ChrTalk(
        0x135,
        (
            "#01809FHehu, indeed.\x02\x03",
            "#01802FWell then, I will soon\x01",
            "I will be rude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4A")

    label("loc_4AE5")


    ChrTalk(
        0x166,
        (
            "#14006FCertainly it was a funny guy.\x02\x03",
            "#14000FThen, I'm in another place.\x01",
            "I will go play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4A")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4B7C")

    ChrTalk(
        0x101,
        "#00000FWell, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B9B")

    label("loc_4B7C")


    ChrTalk(
        0x101,
        "#00000FOh, later.\x02",
    )

    CloseMessageWindow()

    label("loc_4B9B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4BBC")
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_4C5D")

    label("loc_4BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4BCD")
    RemoveParty(0x2, 0xFF)
    Jump("loc_4C5D")

    label("loc_4BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4BDE")
    RemoveParty(0x3, 0xFF)
    Jump("loc_4C5D")

    label("loc_4BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4BF4")
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_4C5D")

    label("loc_4BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4C05")
    RemoveParty(0x4, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4C16")
    RemoveParty(0x52, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4C27")
    RemoveParty(0x55, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4C38")
    RemoveParty(0x4B, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4C49")
    RemoveParty(0x33, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4C5A")
    RemoveParty(0x34, 0xFF)
    Jump("loc_4C5D")

    label("loc_4C5A")

    RemoveParty(0x65, 0xFF)

    label("loc_4C5D")

    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Mie's Challenge】\x07\x00",
            "Achieved!\x02",
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

    # Function_36_3E7B end

    def Function_37_4CD8(): pass

    label("Function_37_4CD8")

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

    def lambda_4E01():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E01)
    Sleep(50)

    def lambda_4E1E():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4E1E)
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

    def lambda_4E9B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E9B)
    Sleep(50)

    def lambda_4EAB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4EAB)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHi, Waji to Noel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EE0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4EE0)
    Sleep(50)

    def lambda_4EF0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4EF0)
    Sleep(300)

    def lambda_4F00():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F00)
    Sleep(50)

    def lambda_4F1D():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F1D)
    WaitChrThread(0x101, 1)

    def lambda_4F3B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F3B)
    Sleep(50)

    def lambda_4F4B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F4B)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10300FHuh, why not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FOh, please listen to me.\x01",
            "Mr. Lloyd!\x02\x03",
            "#10103FWadi Kimu,\x01",
            "As soon as I take my eyes off\x01",
            "To play with hulafula ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuff, a big incident\x01",
            "I can not get up.\x02\x03",
            "#10304FWell, it's a patrol\x01",
            "Whoever did it while playing it properly\x01",
            "Do not you think it's good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FDo not think?\x01",
            "It is not at all …\x07\x00\x02",
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
            "#05520FAh……\x01",
            "Mr. Lloyd is children.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's voice")

    AnonymousTalk(
        0xFF,
        "#4SMiss you!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's voice")

    AnonymousTalk(
        0xFF,
        (
            "#4SOh, here you are\x01",
            "There are also some people -?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_51A8():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51A8)
    Sleep(50)

    def lambda_51B8():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51B8)
    Sleep(50)

    def lambda_51C8():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51C8)
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

    def lambda_525B():
        OP_95(0xFE, -440, 60, -35850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_525B)
    Sleep(100)

    def lambda_5278():
        OP_95(0xFE, 710, 10, -34740, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5278)

    def lambda_5292():

        label("loc_5292")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5292")

    QueueWorkItem2(0x109, 1, lambda_5292)

    def lambda_52A4():

        label("loc_52A4")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_52A4")

    QueueWorkItem2(0x105, 1, lambda_52A4)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    def lambda_52C2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_52C2)
    Sleep(50)

    def lambda_52D2():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_52D2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05528F(… … I've gone hidden.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Eiya, Keek!\x02",
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
            "#05211F(Hey …… !?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FPetit\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWait a minute, you guys.\x01",
            "You can not do such a thing ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "My sister, you do not know ~?\x01",
            "When you kick Michishi\x01",
            "You can be happy ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Happy for the buttocks\x01",
            "I suppose they are clogged ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F(And, I am happy … I have not heard!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    WaitChrThread(0x1E, 3)
    OP_64(0x101)

    def lambda_549C():
        TurnDirection(0x1E, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_549C)
    Sleep(50)
    TurnDirection(0x1F, 0x103, 500)

    ChrTalk(
        0x1F,
        "I wonder if I can kick this way too?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F(……!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(What do you do?\x01",
            "I have to deal with something ……)\x07\x00\x02",
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
            "To scold\x01",      # 0
            "tickle\x01",        # 1
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
        (0, "loc_55AA"),
        (1, "loc_5688"),
        (SWITCH_DEFAULT, "loc_5794"),
    )


    label("loc_55AA")

    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Here, come on!\x01",
            "No more no more!\x02\x03",
            "No matter how much it is\x01",
            "I will not forgive Zoe! Is it?\x07\x00\x02",
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
        "Wow, Michi got angry! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Run away!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x3)
    Jump("loc_5794")

    label("loc_5688")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 6)
    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "A child who does such a thing ……\x01",
            "Here it is!\x02\x03",
            "Chilling … …\x07\x00\x02",
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
            "Cash …\x01",
            "Hahahahahahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Wow, Misi's\x01",
            "Gakushou!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Escape!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x4)
    Jump("loc_5794")

    label("loc_5794")


    def lambda_5799():
        OP_97(0xFE, 0xFFFFF95C, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5799)
    Sleep(100)

    def lambda_57B6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_57B6)
    WaitChrThread(0x1F, 1)

    def lambda_57D4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_57D4)

    def lambda_57EE():

        label("loc_57EE")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_57EE")

    QueueWorkItem2(0x101, 1, lambda_57EE)

    def lambda_5800():

        label("loc_5800")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5800")

    QueueWorkItem2(0x103, 1, lambda_5800)

    def lambda_5812():

        label("loc_5812")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5812")

    QueueWorkItem2(0x109, 1, lambda_5812)

    def lambda_5824():

        label("loc_5824")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5824")

    QueueWorkItem2(0x105, 1, lambda_5824)
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
            "#05200FWere you going?\x02\x03",
            "#05206FNo way to suddenly be kicked …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58AE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58AE)
    Sleep(50)

    def lambda_58BE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58BE)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FRecently, that kind of\x01",
            "It seems to be in fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FHaha … … It was a disaster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203FBut … I wonder if it was okay.\x01",
            "I just thought like that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A75")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F… … rather than shouting\x01",
            "I think it's good.\x02\x03",
            "#05520FMissi is a healing system,\x01",
            "Will you drive out the way\x01",
            "I have to choose it.\x02\x03",
            "#05522FMr. Lloyd,\x01",
            "It is truly judgmental power.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202Fmy mother……\x01",
            "Thank you very much.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD8")

    label("loc_5A75")

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
            "#05211FNegative! Is it?\x07\x00\x02",
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
            "#05531F…… It is a bad day.\x02\x03",
            "#05526FMissi is a healing system,\x01",
            "Will you drive out the way\x01",
            "I have to choose it.\x02\x03",
            "#05520FMore like this, peaceful\x01",
            "I have to choose a way to repel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FThat's difficult ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD8")


    ChrTalk(
        0x109,
        (
            "#10100FWell, until Tio\x01",
            "It was nice to have been kicked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FJuff, like I guard my sister\x01",
            "It's like a knight.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FEven if this dress is told\x01",
            "It does not come nicely, but …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FBy the way, Missie's buttocks\x01",
            "It's okay to be kicked\x01",
            "I heard that it is sturdy.\x02\x03",
            "#05520FDid not it hurt than I thought?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FWell, indeed …\x02\x03",
            "#05203F(I also put cushioning materials.\x01",
            "It's reasonable and it's gooey … …)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FAh, Lloyd.\x01",
            "It is almost time for the next section\x01",
            "I have to go.\x02\x03",
            "#05524FMorning schedule is\x01",
            "Because it's a funny thing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FI understand.\x01",
            "… Well then,\x01",
            "Noel is a wadi.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FPlease do your best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, see you later.\x02",
    )

    CloseMessageWindow()

    def lambda_5E90():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E90)
    Sleep(1000)

    def lambda_5EAD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EAD)
    Sleep(50)

    def lambda_5ECA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5ECA)
    Sleep(50)

    def lambda_5EDA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EDA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1330", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4CD8 end

    def Function_38_5EFD(): pass

    label("Function_38_5EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5F37")
    OP_99(0xFE, 0x101, 0xFA, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    Sound(862, 0, 20, 0)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Jump("Function_38_5EFD")

    label("loc_5F37")

    Return()

    # Function_38_5EFD end

    def Function_39_5F38(): pass

    label("Function_39_5F38")

    Sleep(1000)

    label("loc_5F3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F5D")
    Sound(918, 0, 70, 0)
    Sleep(2200)
    Sound(918, 0, 60, 0)
    Sleep(5000)
    Jump("loc_5F3B")

    label("loc_5F5D")

    Return()

    # Function_39_5F38 end

    SaveToFile()

Try(main)
