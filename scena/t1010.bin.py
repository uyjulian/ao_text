from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1010.bin",                # FileName
        "t1010",                    # MapName
        "t1010",                    # Location
        0x0045,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1010",                  # 0
        "Emmy",                 # 1
        "Gel",                   # 2
        "Kabiran",               # 3
        "Loumann",             # 4
        "Mrs. Margaret",       # 5
        "Event monster",   # 6
        "Event monster",   # 7
        "Event monster",   # 8
        "Event monster",   # 9
        "Event monster",   # 10
        "Event monster",   # 11
        "Event monster",   # 12
        "Event monster",   # 13
        "bt1010",                 # 14
        "Directions to Kaikan",             # 15
        "Destination to Hotel · Delfinia",# 16
    ))

    ATBonus("ATBonus_2CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_38C", 8, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_380", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_384", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3AC", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86100.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, 0, 0, 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_36C", "ed7540", "ed7453", "ATBonus_2CC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22302.itc",                   # 00
        "chr/ch22202.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch44000.itc",                   # 04
    ))

    DeclNpc(2279,    4294963596, 4294954866, 180,  325,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(3660,    4294963596, 4294954866, 180,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   4294965296, 2200,    270,  257,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294965326, 4294965296, 34720,   180,  257,  0x0, 0,   3,   0,   0,   2,   0,   9,   255,  0)
    DeclNpc(4294961066, 4294965497, 0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  5.5,                   0.0,                   -3.0,                  400.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.375,                -0.0,                  0.5999999642372131,    1.0])

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "Directions to Kaikan")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "Destination to Hotel · Delfinia")

    ChipFrameInfo(1072, 0)                                       # 0

    ScpFunction((
        "Function_0_430",          # 00, 0
        "Function_1_4E8",          # 01, 1
        "Function_2_549",          # 02, 2
        "Function_3_5AA",          # 03, 3
        "Function_4_614",          # 04, 4
        "Function_5_6B2",          # 05, 5
        "Function_6_7D8",          # 06, 6
        "Function_7_A5C",          # 07, 7
        "Function_8_B82",          # 08, 8
        "Function_9_EEE",          # 09, 9
        "Function_10_118C",        # 0A, 10
        "Function_11_1270",        # 0B, 11
        "Function_12_194D",        # 0C, 12
        "Function_13_196C",        # 0D, 13
        "Function_14_198B",        # 0E, 14
        "Function_15_19A8",        # 0F, 15
    ))


    def Function_0_430(): pass

    label("Function_0_430")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_470"),
        (1, "loc_47C"),
        (2, "loc_488"),
        (3, "loc_494"),
        (4, "loc_4A0"),
        (5, "loc_4AC"),
        (6, "loc_4B8"),
        (SWITCH_DEFAULT, "loc_4C4"),
    )


    label("loc_470")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_47C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_488")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_494")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4E7")

    Return()

    # Function_0_430 end

    def Function_1_4E8(): pass

    label("Function_1_4E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_548")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_4E8")

    label("loc_548")

    Return()

    # Function_1_4E8 end

    def Function_2_549(): pass

    label("Function_2_549")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A9")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_549")

    label("loc_5A9")

    Return()

    # Function_2_549 end

    def Function_3_5AA(): pass

    label("Function_3_5AA")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)

    label("loc_613")

    Return()

    # Function_3_5AA end

    def Function_4_614(): pass

    label("Function_4_614")

    SetMapObjFrame(0xFF, "t1010_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_64A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_668")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_68F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_6B1")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6B1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_6B1")

    Return()

    # Function_4_614 end

    def Function_5_6B2(): pass

    label("Function_5_6B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6C3")
    Jump("loc_7D0")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    Call(0, 6)
    Jump("loc_745")

    label("loc_6DE")


    ChrTalk(
        0x8,
        "Do not get serious, do not worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To disgrace Lady,\x01",
            "It is a mere act as a gentleman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_745")

    Jump("loc_7D0")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765")
    Call(0, 6)
    Jump("loc_7D0")

    label("loc_765")


    ChrTalk(
        0x8,
        "Do not get serious, do not worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To become my wonderful husband,\x01",
            "I have to do that much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D0")

    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_5_6B2 end

    def Function_6_7D8(): pass

    label("Function_6_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(
        0x8,
        (
            "Good thing, Zel?\x01",
            "Because you are my marriage\x01",
            "I think that it is necessary to have an eye to look into the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"After all, Ichimitarou is the best ideal\"\x01",
            "Mom was saying … but what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ichihi minitaro … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…, and I do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Is it? Is it? Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4E")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A4E")

    ChrTalk(
        0x8,
        (
            "Good thing, Zel?\x01",
            "Because you are my marriage\x01",
            "I must be a cool person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am smart, I can do exercise,\x01",
            "And yet I'm friendly to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, even if such a thing is said ……\x01",
            "Specifically, what should I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, 100 times a day\x01",
            "Start push-ups and abs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, at the Sunday school test\x01",
            "Because I only allow full marks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Mu, do not say no … …\x02",
    )

    CloseMessageWindow()

    label("loc_A4E")

    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_6_7D8 end

    def Function_7_A5C(): pass

    label("Function_7_A5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A6D")
    Jump("loc_B7A")

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    Call(0, 6)
    Jump("loc_AE4")

    label("loc_A88")


    ChrTalk(
        0x9,
        (
            "What Emmy says\x01",
            "Sometimes I'm not sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ichihi minitaro …\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4")

    Jump("loc_B7A")

    label("loc_AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B04")
    Call(0, 6)
    Jump("loc_B7A")

    label("loc_B04")


    ChrTalk(
        0x9,
        "Emmy is too ideal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Only to be like life\x01",
            "Because it does not become so much\x01",
            "I wish I could raise a hurdle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7A")

    TalkEnd(0xFE)
    SetChrSubChip(0x9, 0x2)
    Return()

    # Function_7_A5C end

    def Function_8_B82(): pass

    label("Function_8_B82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B93")
    Jump("loc_EEA")

    label("loc_B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")

    ChrTalk(
        0xA,
        (
            "Fu, the common people in such a place\x01",
            "What on earth are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FWhether?\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    ChrTalk(
        0xA,
        "…… No, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it is nothing,\x01",
            "With such a carefree smile\x01",
            "Before you look at me ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Ha … … Ka'aa is invincible.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D31")

    label("loc_CCA")


    ChrTalk(
        0xA,
        "…… Go over there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm telling you something irritable\x01",
            "It's getting miserable …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D31")

    Jump("loc_EEA")

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(
        0xA,
        (
            "I went to the guesthouse before.\x01",
            "Girl with green hair,\x01",
            "It seems like a long time ago ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, when was it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEA")

    label("loc_DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8C")

    ChrTalk(
        0xA,
        "Oh my, what are you going to do here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This luxury villa area\x01",
            "I think it is a place unrelated to the common people … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Fu, that would be nice.\x01",
            "We, what are wealthy mansions,\x01",
            "You should bake your eyes at best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EEA")

    label("loc_E8C")


    ChrTalk(
        0xA,
        (
            "…… Fu, that would be nice.\x01",
            "We, what are wealthy mansions,\x01",
            "You should bake your eyes at best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")

    TalkEnd(0xFE)
    Return()

    # Function_8_B82 end

    def Function_9_EEE(): pass

    label("Function_9_EEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EFF")
    Jump("loc_1188")

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_FD3")

    ChrTalk(
        0xB,
        (
            "Since Hartmann's former chairman has failed,\x01",
            "A queen smelly people around here\x01",
            "There was almost nothing to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As that mansion became a guest guesthouse,\x01",
            "Eyes of security also became sharp.\x01",
            "The security has improved considerably.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1188")

    label("loc_FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(
        0xB,
        (
            "Mr. Hartmann's former chairman's residence,\x01",
            "I changed my appearance to the guesthouse a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even during the trade meeting this time,\x01",
            "To welcome the leaders of each country\x01",
            "It seems that it was in use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the time the queen smelly party was held\x01",
            "Compared to a really meaningful and healthy place\x01",
            "I can say that it has become.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1188")

    label("loc_10E5")


    ChrTalk(
        0xB,
        (
            "Mr. Hartmann's former chairman's residence,\x01",
            "I changed my appearance to the guesthouse a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the time the queen smelly party was held\x01",
            "Compared to a really meaningful and healthy place\x01",
            "I can say that it has become.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1188")

    TalkEnd(0xFE)
    Return()

    # Function_9_EEE end

    def Function_10_118C(): pass

    label("Function_10_118C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120F")

    ChrTalk(
        0xFE,
        (
            "The mansion in the brochure\x01",
            "It looks like this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Located overlooking the lake ……\x01",
            "It looks pretty good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_126C")

    label("loc_120F")


    ChrTalk(
        0xFE,
        (
            "Located overlooking the lake ……\x01",
            "It looks pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I decide to purchase again.\x02",
    )

    CloseMessageWindow()

    label("loc_126C")

    TalkEnd(0xFE)
    Return()

    # Function_10_118C end

    def Function_11_1270(): pass

    label("Function_11_1270")

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
    LoadChrToIndex("monster/ch82050.itc", 0x24)
    LoadChrToIndex("monster/ch82051.itc", 0x25)
    LoadChrToIndex("monster/ch86150.itc", 0x26)
    LoadChrToIndex("monster/ch86151.itc", 0x27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 5500, 0, 2000, 315)
    OP_90(0x104, 6500, 0, 2000, 315)
    OP_90(0x103, 6500, 0, 500, 315)
    OP_90(0x109, 5500, 0, 500, 315)
    OP_90(0x105, 7500, 0, 1250, 315)
    OP_90(0x106, 4500, 0, 1250, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrChipByIndex(0x10, 0x24)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 12)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 12)
    BeginChrThread(0x12, 0, 0, 14)
    SetChrPos(0xE, -1800, -2000, 19500, 180)
    SetChrPos(0xF, 0, -2000, 18500, 180)
    SetChrPos(0x10, 1800, -2000, 19500, 180)
    SetChrPos(0x12, 0, -2000, 22500, 180)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    FadeToBright(1000, 0)
    OP_68(2700, -500, 1500, 0)
    OP_68(0, -500, 4500, 2500)
    MoveCamera(315, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_1521():
        OP_95(0xFE, -1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1521)
    Sleep(50)

    def lambda_153E():
        OP_95(0xFE, -500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_153E)
    Sleep(50)

    def lambda_155B():
        OP_95(0xFE, 500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_155B)
    Sleep(50)

    def lambda_1578():
        OP_95(0xFE, -500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1578)
    Sleep(50)

    def lambda_1595():
        OP_95(0xFE, 500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1595)
    Sleep(50)

    def lambda_15B2():
        OP_95(0xFE, 1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15B2)
    Sleep(800)
    Sound(948, 0, 30, 0)
    Sound(911, 0, 100, 0)
    WaitChrThread(0x106, 1)

    def lambda_15DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_15DF)
    WaitChrThread(0x101, 1)

    def lambda_15F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15F0)
    WaitChrThread(0x104, 1)

    def lambda_1601():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1601)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 1)

    def lambda_16A8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16A8)
    WaitChrThread(0x103, 1)

    def lambda_16B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16B9)
    WaitChrThread(0x105, 1)

    def lambda_16CA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_16CA)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x12, 0x8)
    OP_68(150, -500, 18040, 2000)
    MoveCamera(321, 21, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#2PTch, more millitary dogs!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#2PThey're stronger - be careful!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -500, 8000, 1100)
    SetCameraDistance(18000, 1100)
    Sound(911, 0, 80, 0)
    Sound(948, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x25)
    BeginChrThread(0xE, 0, 0, 13)

    def lambda_17A0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_17A0)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x25)
    BeginChrThread(0xF, 0, 0, 13)

    def lambda_17C2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17C2)
    Sleep(50)
    SetChrChipByIndex(0x10, 0x25)
    BeginChrThread(0x10, 0, 0, 13)

    def lambda_17E4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17E4)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x27)
    BeginChrThread(0x12, 0, 0, 15)

    def lambda_1806():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1806)
    Sleep(50)
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
    Sleep(700)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(18000, 300)
    Sleep(300)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    Battle("BattleInfo_3AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
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
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x0, 0, -1800, 6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 7)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_1270 end

    def Function_12_194D(): pass

    label("Function_12_194D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_196B")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_12_194D")

    label("loc_196B")

    Return()

    # Function_12_194D end

    def Function_13_196C(): pass

    label("Function_13_196C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_198A")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_13_196C")

    label("loc_198A")

    Return()

    # Function_13_196C end

    def Function_14_198B(): pass

    label("Function_14_198B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19A7")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_14_198B")

    label("loc_19A7")

    Return()

    # Function_14_198B end

    def Function_15_19A8(): pass

    label("Function_15_19A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19C4")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_15_19A8")

    label("loc_19C4")

    Return()

    # Function_15_19A8 end

    SaveToFile()

Try(main)
