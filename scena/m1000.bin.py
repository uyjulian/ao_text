from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1000.bin",                # FileName
        "m1000",                    # MapName
        "m1000",                    # Location
        0x006B,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 107, 0, 2, 0, 3],
    )

    BuildStringList((
        "m1000",                  # 0
        "Vanguard",           # 1
        "Vanguard",           # 2
        "Tsuyoshi's Ineness",         # 3
        "SE control",                 # 4
        "bm1080",                 # 5
        "Ursula intermittent way",       # 6
    ))

    ATBonus("ATBonus_34C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_40C", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_404", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_42C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_40C", "MonsterBattlePostion_3EC", "ed7451", "ed7453", "ATBonus_34C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "monster/ch80050.itc",               # 00
        "chr/ch43200.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
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

    DeclNpc(29950,   4294954097, 97660,   180,  453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(39959,   4294954097, 97639,   180,  453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(34990,   4294954097, 99489,   180,  453,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  35.0,                  94.5,                  -13.199999809265137,   10920.25,              [0.09090908616781235,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.05263157933950424,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.1818180084228516,   -4.973684310913086,    2.640000104904175,     1.0])
    DeclEvent(0x0000, 0, 14,  34.5,                  72.0,                  -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.450000047683716,    -24.0,                 2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 6,   6.940000057220459,     26.5,                  -3.880000114440918,    182.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.7711111307144165,   -8.833333015441895,    0.7760000228881836,    1.0])

    DeclActor(43800,   4294954096, 94690,   1200,    43800,   4294956096, 94690,   0x007C, 0,  4,  0x0000)
    DeclActor(45150,   4294954056, 95200,   1200,    45150,   4294956056, 95200,   0x007C, 0,  4,  0x0000)
    DeclActor(34360,   4294954096, 99420,   1200,    34360,   4294956096, 99420,   0x007C, 0,  21, 0x0000)

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "Ursula intermittent way")

    ChipFrameInfo(1224, 0)                                       # 0

    ScpFunction((
        "Function_0_4C8",          # 00, 0
        "Function_1_580",          # 01, 1
        "Function_2_630",          # 02, 2
        "Function_3_B7C",          # 03, 3
        "Function_4_D8F",          # 04, 4
        "Function_5_10D2",         # 05, 5
        "Function_6_1166",         # 06, 6
        "Function_7_119B",         # 07, 7
        "Function_8_1B11",         # 08, 8
        "Function_9_1EE4",         # 09, 9
        "Function_10_1F5B",        # 0A, 10
        "Function_11_22F6",        # 0B, 11
        "Function_12_23B4",        # 0C, 12
        "Function_13_23E9",        # 0D, 13
        "Function_14_2940",        # 0E, 14
        "Function_15_3573",        # 0F, 15
        "Function_16_358E",        # 10, 16
        "Function_17_35CA",        # 11, 17
        "Function_18_3617",        # 12, 18
        "Function_19_440B",        # 13, 19
        "Function_20_444F",        # 14, 20
        "Function_21_4468",        # 15, 21
    ))


    def Function_0_4C8(): pass

    label("Function_0_4C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_508"),
        (1, "loc_514"),
        (2, "loc_520"),
        (3, "loc_52C"),
        (4, "loc_538"),
        (5, "loc_544"),
        (6, "loc_550"),
        (SWITCH_DEFAULT, "loc_55C"),
    )


    label("loc_508")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_514")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_520")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_52C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_538")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_544")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_550")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_55C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_568")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_57F")

    Return()

    # Function_0_4C8 end

    def Function_1_580(): pass

    label("Function_1_580")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5B8"),
        (1, "loc_5C4"),
        (2, "loc_5D0"),
        (3, "loc_5DC"),
        (4, "loc_5E8"),
        (5, "loc_5F4"),
        (6, "loc_600"),
        (SWITCH_DEFAULT, "loc_60C"),
    )


    label("loc_5B8")

    OP_A0(0xFE, 1450, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5C4")

    OP_A0(0xFE, 1550, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5D0")

    OP_A0(0xFE, 1600, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5DC")

    OP_A0(0xFE, 1400, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5E8")

    OP_A0(0xFE, 1650, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5F4")

    OP_A0(0xFE, 1350, 0x0, 0x5)
    Jump("loc_618")

    label("loc_600")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_60C")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62F")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_62F")

    Return()

    # Function_1_580 end

    def Function_2_630(): pass

    label("Function_2_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)

    label("loc_65C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E9")
    SetScenarioFlags(0x38, 0)

    label("loc_6E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF")
    SetScenarioFlags(0x38, 1)

    label("loc_6FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    SetScenarioFlags(0x38, 2)

    label("loc_715")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    SetScenarioFlags(0x38, 3)

    label("loc_72B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741")
    SetScenarioFlags(0x38, 4)

    label("loc_741")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    SetScenarioFlags(0x38, 5)

    label("loc_757")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    SetScenarioFlags(0x38, 6)

    label("loc_76D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783")
    SetScenarioFlags(0x38, 7)

    label("loc_783")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799")
    SetScenarioFlags(0x39, 0)

    label("loc_799")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF")
    SetScenarioFlags(0x39, 1)

    label("loc_7AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5")
    SetScenarioFlags(0x39, 2)

    label("loc_7C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x39, 3)

    label("loc_7DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    SetScenarioFlags(0x39, 4)

    label("loc_7F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    SetScenarioFlags(0x39, 5)

    label("loc_807")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    SetScenarioFlags(0x39, 6)

    label("loc_81D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    SetScenarioFlags(0x39, 7)

    label("loc_833")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    SetScenarioFlags(0x3A, 0)

    label("loc_849")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    SetScenarioFlags(0x3A, 1)

    label("loc_85F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")
    SetScenarioFlags(0x3A, 2)

    label("loc_875")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    SetScenarioFlags(0x3A, 3)

    label("loc_88B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    SetScenarioFlags(0x3A, 4)

    label("loc_8A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B7")
    SetScenarioFlags(0x3A, 5)

    label("loc_8B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")
    SetScenarioFlags(0x3A, 6)

    label("loc_8CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3")
    SetScenarioFlags(0x3A, 7)

    label("loc_8E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9")
    SetScenarioFlags(0x3B, 0)

    label("loc_8F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    SetScenarioFlags(0x3B, 1)

    label("loc_90F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    SetScenarioFlags(0x3B, 2)

    label("loc_925")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    SetScenarioFlags(0x3B, 3)

    label("loc_93B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    SetScenarioFlags(0x3B, 4)

    label("loc_951")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")
    SetScenarioFlags(0x3B, 5)

    label("loc_967")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    SetScenarioFlags(0x3B, 6)

    label("loc_97D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    SetScenarioFlags(0x3B, 7)

    label("loc_993")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    SetScenarioFlags(0x3D, 5)

    label("loc_9A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    SetScenarioFlags(0x3D, 6)

    label("loc_9BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    SetScenarioFlags(0x3D, 7)

    label("loc_9D5")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A10")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_B00")

    label("loc_A10")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A33")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_B00")

    label("loc_A33")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_B00")

    label("loc_A56")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A79")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_B00")

    label("loc_A79")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9C")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_B00")

    label("loc_A9C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_B00")

    label("loc_ABF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_B00")

    label("loc_AE2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
    SetScenarioFlags(0x3C, 7)

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    SetChrPos(0x0, 42960, -13200, 94790, 260)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 5)

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B7B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    SetChrPos(0x0, 45150, -13240, 95200, 260)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B7B")

    Return()

    # Function_2_630 end

    def Function_3_B7C(): pass

    label("Function_3_B7C")

    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BBA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_C3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x12C, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "gray")

    label("loc_C75")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAB")
    SetMapObjFlags(0x7, 0x4)
    OP_65(0x2, 0x1)

    label("loc_CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD5")
    SetMapObjFlags(0x7, 0x4)
    OP_65(0x2, 0x1)

    label("loc_CD5")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEF")
    ClearMapObjFlags(0xB, 0x4)

    label("loc_CEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0D")
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0xA, 0x4)

    label("loc_D0D")

    MiniGame(0x2F, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D5E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D76")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_D76")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8E")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_D8E")

    Return()

    # Function_3_B7C end

    def Function_4_D8F(): pass

    label("Function_4_D8F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC1")
    SetScenarioFlags(0x31, 2)

    label("loc_DC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF6")
    Sound(2499, 255, 100, 0)
    Jump("loc_DFC")

    label("loc_DF6")

    Sound(3537, 255, 100, 0)

    label("loc_DFC")

    Jump("loc_E07")

    label("loc_E01")

    Sound(3344, 255, 100, 0)

    label("loc_E07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_E80")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E60"),
        (SWITCH_DEFAULT, "loc_E71"),
    )


    label("loc_E60")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_E7B")

    label("loc_E71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E7B")

    Jump("loc_10BF")

    label("loc_E80")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_EB4")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_EB4")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE8"),
        (1, "loc_FEC"),
        (2, "loc_107D"),
        (SWITCH_DEFAULT, "loc_10B5"),
    )


    label("loc_EE8")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F19")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F29")

    label("loc_F19")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F29")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA2")
    Sound(461, 0, 100, 0)

    label("loc_FA2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FC2")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_FD2")

    label("loc_FC2")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_FD2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_E07")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_105E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_1021")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1039")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1034")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1039")

    label("loc_1034")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1039")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1078")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_106E")
    OP_AF(0xFB)
    Jump("loc_1078")

    label("loc_106E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1078")

    Jump("loc_10BF")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1096")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B0")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_10A6")
    OP_AF(0xFB)
    Jump("loc_10B0")

    label("loc_10A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B0")

    Jump("loc_10BF")

    label("loc_10B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10BF")

    Jump("loc_E07")

    label("loc_10C4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_D8F end

    def Function_5_10D2(): pass

    label("Function_5_10D2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_112D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1122")
    Sound(2502, 255, 100, 0)
    Jump("loc_1128")

    label("loc_1122")

    Sound(2503, 255, 100, 0)

    label("loc_1128")

    Jump("loc_1151")

    label("loc_112D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_114B")
    Sound(3347, 255, 100, 0)
    Jump("loc_1151")

    label("loc_114B")

    Sound(3348, 255, 100, 0)

    label("loc_1151")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_10D2 end

    def Function_6_1166(): pass

    label("Function_6_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_1177")
    Call(0, 9)
    Jump("loc_118B")

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_1188")
    Call(0, 8)
    Jump("loc_118B")

    label("loc_1188")

    Call(0, 7)

    label("loc_118B")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    Return()

    # Function_6_1166 end

    def Function_7_119B(): pass

    label("Function_7_119B")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1892")

    AnonymousTalk(
        0x105,
        (
            "#10401F\"Eating snake#10RUroboros#\"Is it obeying … ….\x02\x03",
            "#10403FThe daughter of armored figure protecting the door,\x01",
            "It is one of the men of \"Steel's Saint\".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00013FThe puppet weapons on both sides are also big …\x01",
            "It's a type I've never seen before.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134D")

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw it in the database,\x01",
            "The association used it when Libert's strange change\x01",
            "It seems to be similar to type ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10401F《Vanguard》だったかな？\x01",
            "It should be a high-performance melee type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DB")

    label("loc_134D")


    AnonymousTalk(
        0x105,
        (
            "#10403FEven when that happens to Libert\x01",
            "It is said that the association used it,\x01",
            "It should be a high-performance melee type.\x02\x03",
            "#10400F確か、《Vanguard》だったかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DB")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(
        0x101,
        (
            "#00003F#6P…… Anyway, now\x01",
            "It looks good to take you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PEven so,\x01",
            "After all, about \"association\"\x01",
            "Does it seem to be detailed so much?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_148A")


    ChrTalk(
        0x101,
        (
            "#00003F#6P…… Anyway, now\x01",
            "It looks good to take you.\x02\x03",
            "#00005FEven so,\x01",
            "After all, about \"association\"\x01",
            "Does it seem to be detailed so much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1516")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E9")

    ChrTalk(
        0x105,
        (
            "#10404F#12PGiggle\x01",
            "Well, is that fairly detailed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3C\"Knights\" and \"association\" are\x01",
            "Occasionally in the shadows of history\x01",
            "There is a history of conflict.\x02\x03",
            "In that, knowing the other party\x01",
            "It will be the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B8")

    label("loc_15E9")


    ChrTalk(
        0x105,
        (
            "#10404F#6PGiggle\x01",
            "Well, is that fairly detailed?\x02\x03",
            "#10400F\"Knights\" and \"association\" are\x01",
            "Occasionally in the shadows of history\x01",
            "There is a conflict history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see … in that situation\x01",
            "It would be important to know the other party.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B8")


    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, \"Knights\" and \"Society\" as well\x01",
            "As the situation always changes,\x01",
            "It is honestly it is crazy.\x02\x03",
            "#10402FOops, when you say this lightly\x01",
            "Is Abbas getting angry?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B8")

    ChrTalk(
        0x109,
        "#10106F#6PWaa, you already are …\x02",
    )

    CloseMessageWindow()

    label("loc_17B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(
        0x106,
        (
            "#10709F#6POh, haha ….\x01",
            "Mr. Abbas seems to have had trouble too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P… … let's get out of here for the moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_183A")


    ChrTalk(
        0x101,
        (
            "#00006F#6PIt seems that Abbas has also struggled … …\x02\x03",
            "#00000F… … let's get out of here for the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188D")

    Jump("loc_1AC7")

    label("loc_1892")


    AnonymousTalk(
        0x101,
        "#00003F#6P\"Eating snake#10RUroboros#\"Is it obeying … ….\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00103F#6PI am standing there\x01",
            "\"Steal Saint\" was brought\x01",
            "I wonder if he was one of my subordinates.\x02\x03",
            "#00101FBesides, that white puppet weapon ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208F#6PI saw it in the database,\x01",
            "The association used it when Libert's strange change\x01",
            "It seems to be similar to type ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10101F#6PTo guess from arming\x01",
            "It looks like a melee battle type … ….\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00303F#6P…… Although it is not very much,\x01",
            "What is approaching Nokonoko is\x01",
            "It is a suicidal act.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00001F#6P…… Anyway, now\x01",
            "It seems better to withdraw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10700F#6PLet's get out of here for the moment.\x02",
    )

    CloseMessageWindow()

    label("loc_1AC7")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1AE1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1AE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1AFA")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1AFA")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_7_119B end

    def Function_8_1B11(): pass

    label("Function_8_1B11")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAE")

    AnonymousTalk(
        0x105,
        (
            "#10401FHere also \"snake snake#10RUroboros#Or\x02\x03",
            "#10403FThe daughter of armored figure protecting the door,\x01",
            "It is one of the men of \"Steel's Saint\".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C30")

    label("loc_1BAE")


    AnonymousTalk(
        0x106,
        (
            "#10701FHere also \"snake snake#10RUroboros#\"But……\x02\x03",
            "#10703FThe daughter of armored figure protecting the door,\x01",
            "It is one of the men of \"Steel's Saint\".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C30")


    AnonymousTalk(
        0x104,
        (
            "#00301FI am on both sides\x01",
            "Puppet weapons are also quite big …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw it in the database,\x01",
            "The association used it when Libert's strange change\x01",
            "It seems to be similar to type ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D2E")

    AnonymousTalk(
        0x105,
        (
            "#10401F《Vanguard》だったかな？\x01",
            "It should be a high-performance melee type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D6C")

    label("loc_1D2E")


    AnonymousTalk(
        0x109,
        (
            "#10101FTo guess from arming\x01",
            "It looks like a melee battle type … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6C")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CAfter all, it is not easy\x01",
            "It is not a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6POh, let's get out of here for the moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E64")

    label("loc_1DF6")


    ChrTalk(
        0x101,
        (
            "#00003F#6P…… After all, it is not easy\x01",
            "It seems better to stop it.\x02\x03",
            "#00000FLet's get out of here for the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(
        0x106,
        "#10701F#6PYes, let's do so.\x02",
    )

    CloseMessageWindow()

    label("loc_1E9A")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EB4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1EB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1ECD")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1ECD")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_8_1B11 end

    def Function_9_1EE4(): pass

    label("Function_9_1EE4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIn the future \"association\"\x01",
            "It seems to be protecting.\x02\x03",
            "#00001F…… It is better to withdraw\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6370, -3700, 23670, 19)
    EventEnd(0x4)
    Return()

    # Function_9_1EE4 end

    def Function_10_1F5B(): pass

    label("Function_10_1F5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F9D")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1F92():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F92)
    Sleep(50)

    label("loc_1F9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FDF")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1FD4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FD4)
    Sleep(50)

    label("loc_1FDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2016():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2016)
    Sleep(50)

    label("loc_2021")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206A")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0xA, 500)

    def lambda_205F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_205F)
    Sleep(50)

    label("loc_206A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20B3")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0xA, 500)

    def lambda_20A8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_20A8)
    Sleep(50)

    label("loc_20B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20FC")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0xA, 500)

    def lambda_20F1():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_20F1)
    Sleep(50)

    label("loc_20FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2145")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0xA, 500)

    def lambda_213A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_213A)
    Sleep(50)

    label("loc_2145")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_218E")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0xA, 500)

    def lambda_2183():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2183)
    Sleep(50)

    label("loc_218E")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThat is……\x02",
    )

    CloseMessageWindow()
    OP_68(12350, 300, 39810, 4000)
    Sleep(4000)
    Fade(500)
    OP_68(28680, -8700, 77510, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21940, 0)
    OP_68(29090, -8700, 89190, 7000)
    MoveCamera(30, 19, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(17870, 7000)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2241")
    SetChrPos(0x0, 6840, -3700, 25000, 20)

    label("loc_2241")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2261")
    SetChrPos(0x1, 5580, -3700, 24600, 20)

    label("loc_2261")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2281")
    SetChrPos(0x2, 8390, -3700, 25230, 20)

    label("loc_2281")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22A1")
    SetChrPos(0x3, 6770, -3700, 22930, 20)

    label("loc_22A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22CB")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, 8320, -3700, 23330, 20)

    label("loc_22CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22F5")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, 5820, -3700, 23330, 20)

    label("loc_22F5")

    Return()

    # Function_10_1F5B end

    def Function_11_22F6(): pass

    label("Function_11_22F6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2316")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_232B")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_232B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2340")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2355")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_236A")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_236A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_237F")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_237F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2394")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2394")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23A9")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_11_22F6 end

    def Function_12_23B4(): pass

    label("Function_12_23B4")

    Fade(500)
    OP_68(9400, -4400, 31020, 0)
    MoveCamera(20, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Return()

    # Function_12_23B4 end

    def Function_13_23E9(): pass

    label("Function_13_23E9")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(32640, -8500, 94450, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14430, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24B3")
    SetChrPos(0x101, 34720, -13200, 91570, 0)
    SetChrPos(0x102, 33350, -13200, 91570, 0)
    SetChrPos(0x103, 36070, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_2512")

    label("loc_24B3")

    SetChrPos(0x101, 33980, -13200, 91570, 0)
    SetChrPos(0x102, 35370, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2512")

    OP_68(32640, -9700, 94450, 3000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25E3")

    def lambda_2538():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2538)
    Sleep(50)

    def lambda_2555():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2555)
    Sleep(50)

    def lambda_2572():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2572)
    Sleep(50)

    def lambda_258F():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_258F)
    Sleep(50)

    def lambda_25AC():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_25AC)
    Sleep(50)

    def lambda_25C9():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_25C9)
    Jump("loc_2671")

    label("loc_25E3")


    def lambda_25E8():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E8)
    Sleep(50)

    def lambda_2605():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2605)
    Sleep(50)

    def lambda_2622():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2622)
    Sleep(50)

    def lambda_263F():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_263F)
    Sleep(50)

    def lambda_265C():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_265C)

    label("loc_2671")

    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#00000FI got to \"Tower of Hoshi\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I came after a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FWell, if you look closely\x01",
            "It's quite high.\x02\x03",
            "#10304FThere seems to be a quest for exploration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FBarricades are also removed,\x01",
            "I will be able to start exploring right away.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_286F")

    ChrTalk(
        0x104,
        "#00304FWell, let's go surprised ─ ─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FTo the extent not to be too careless\x01",
            "Let's proceed carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSewing\x01",
            "You are as ever, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHello, Tio is right.\x02\x03",
            "#00000FAll right, then\x01",
            "Would you like to enter it immediately?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E7")

    label("loc_286F")


    ChrTalk(
        0x104,
        "#00304FWell, let's say I'm going to go surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, yes.\x02\x03",
            "#00000FAll right, then\x01",
            "Would you like to enter it immediately?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2910")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_291A")

    label("loc_2910")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_291A")

    SetChrPos(0x0, 34460, -13200, 96070, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x2)
    SetScenarioFlags(0x153, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_23E9 end

    def Function_14_2940(): pass

    label("Function_14_2940")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2990")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_2990")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29A8")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_29A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29C0")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_29C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29D8")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_29D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29F0")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_29F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A08")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_2A08")

    LoadChrToIndex("monster/ch80051.itc", 0x24)
    LoadChrToIndex("monster/ch80052.itc", 0x25)
    SoundLoad(3895)
    SoundLoad(3896)
    SoundLoad(3897)
    SoundLoad(3898)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 35000, -13200, 81000, 0)
    SetChrPos(0x102, 35820, -13200, 80140, 0)
    SetChrPos(0x103, 34740, -13200, 79630, 0)
    SetChrPos(0x104, 35070, -13200, 78450, 0)
    SetChrPos(0xF4, 36480, -13200, 79110, 0)
    SetChrPos(0xF5, 33750, -13200, 79310, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, 32950, -13200, 100650, 180)
    SetChrPos(0x9, 36950, -13200, 100650, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(30780, 25100, 100030, 0)
    MoveCamera(23, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17090, 0)
    OP_68(32119, -10100, 99250, 10000)
    MoveCamera(33, 5, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(17090, 10000)
    PlaceName2(340, 40, "c_plac28", 0x0, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 1, 0, 17)
    OP_6F(0x79)
    Fade(500)
    OP_68(35000, -11500, 104000, 0)
    OP_68(35000, -11500, 94000, 6000)
    MoveCamera(40, 25, 0, 0)
    MoveCamera(40, 20, 0, 6000)
    OP_6E(600, 0)
    SetCameraDistance(24500, 0)
    Sleep(1500)

    def lambda_2BE7():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2BE7)
    Sleep(50)

    def lambda_2BFF():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2BFF)
    Sleep(50)

    def lambda_2C17():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2C17)
    Sleep(50)

    def lambda_2C2F():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2C2F)
    Sleep(50)

    def lambda_2C47():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2C47)
    Sleep(50)

    def lambda_2C5F():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2C5F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(34510, -12000, 90890, 0)
    MoveCamera(32, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00108F#12PWhite puppet weapon ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E39")

    ChrTalk(
        0x101,
        (
            "#00013F#12PIt's big …\x01",
            "It's a type I've never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PI saw it in the database,\x01",
            "The association used it due to an incident of Libert\x01",
            "It seems to be similar to type ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DF2")

    ChrTalk(
        0x105,
        (
            "#10401F#12P《Vanguard》だったかな？\x01",
            "It should be a high-performance melee type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E34")

    label("loc_2DF2")


    ChrTalk(
        0x109,
        (
            "#10101F#12PTo guess from arming\x01",
            "It looks like a melee battle type … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E34")

    Jump("loc_2F3E")

    label("loc_2E39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E8E")

    ChrTalk(
        0x105,
        (
            "#10401F#12PPuppet weapons handled by association\x01",
            "《Vanguard》みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2E8E")


    ChrTalk(
        0x109,
        (
            "#10101F#12PLooking closer,\x01",
            "The terrain is completely different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC8")


    ChrTalk(
        0x101,
        (
            "#00013F#12PBattlefield type and\x01",
            "I was to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PAfter all it is in the \"tower\"\x01",
            "The bone seems to break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3E")

    Sleep(300)
    StopBGM(0x1388)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3895V#30A#30WVanguardＦ３《スレイプニル》……\x02\x03",
            "#3896V#40A#30WOur \"iron fleet\" is operated\x01",
            "It is a specially adjusted aircraft.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
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
    Fade(1000)
    OP_68(34950, -10750, 104850, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(15500, 20000)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#3P#N#15Ayou……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3136")

    ChrTalk(
        0x106,
        "#10701F#6P#N#15A\"steel#2RGlasses#The saint of \"… …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3168")

    label("loc_3136")


    ChrTalk(
        0x109,
        "#10101F#6P#N#15A\"steel#2RGlasses#The saint of \"… …!\x02",
    )

    CloseMessageWindow()

    label("loc_3168")

    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("Voice of Ariane Road")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3897V#40A#30WSafely, protecting Campanella\x01",
            "You seem to break through.\x02\x03",
            "#3898V#45A#30WIn the tower of this practice\x01",
            "Let's be our partner.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_68(35000, -12000, 96500, 2000)
    MoveCamera(0, 23, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15500, 2000)
    Sleep(1300)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)
    Sound(905, 0, 100, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x8, 0x24)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    BeginChrThread(0x9, 0, 0, 15)

    def lambda_32C0():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32C0)

    def lambda_32D5():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32D5)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 1)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(35000, -12000, 92000, 0)
    MoveCamera(45, 15, 0, 0)
    MoveCamera(30, 15, 0, 10000)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#12PCut …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A8")
    Sound(540, 0, 50, 0)

    label("loc_33A8")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Voice of Ariane Road")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WFirst of all, they protect\x01",
            "Please break through.\x02\x03",
            "The story is then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00307F#12P#NHappy … It is superior!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#12PDefeat at full power!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    Sound(905, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 16)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_0D()
    Sleep(300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10500, 500)
    Sound(951, 0, 100, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    OP_68(35000, -12000, 87000, 1500)

    def lambda_3512():
        OP_9B(0x1, 0xFE, 0xFFFB, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3512)

    def lambda_3527():
        OP_9B(0x1, 0xFE, 0x5, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3527)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x2)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Battle("BattleInfo_42C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 18)
    Return()

    # Function_14_2940 end

    def Function_15_3573(): pass

    label("Function_15_3573")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_358D")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_15_3573")

    label("loc_358D")

    Return()

    # Function_15_3573 end

    def Function_16_358E(): pass

    label("Function_16_358E")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_35A6():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35A6)
    Sleep(100)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_358E end

    def Function_17_35CA(): pass

    label("Function_17_35CA")

    Sound(828, 2, 10, 0)
    Sound(132, 2, 40, 0)
    Sleep(100)
    OP_25(0x33C, 0xF)
    Sleep(100)
    OP_25(0x33C, 0x14)
    OP_25(0x84, 0x32)
    Sleep(100)
    OP_25(0x33C, 0x19)
    Sleep(100)
    OP_25(0x33C, 0x1E)
    OP_25(0x84, 0x3C)
    Sleep(100)
    OP_25(0x84, 0x46)
    Sound(1011, 0, 100, 0)
    Sleep(5000)
    StopSound(828, 2000, 20)
    StopSound(132, 2000, 60)
    Return()

    # Function_17_35CA end

    def Function_18_3617(): pass

    label("Function_18_3617")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3656")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_3656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_366E")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_366E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3686")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_3686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_369E")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_369E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36B6")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_36B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36CE")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_36CE")

    LoadEffect(0x0, "event/ev17029.eff")
    LoadEffect(0x1, "event\\ev14002.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 35000, -13200, 90000, 0)
    SetChrPos(0x102, 35820, -13200, 89140, 0)
    SetChrPos(0x103, 34740, -13200, 88630, 0)
    SetChrPos(0x104, 35070, -13200, 87450, 0)
    SetChrPos(0xF4, 36480, -13200, 88110, 0)
    SetChrPos(0xF5, 33750, -13200, 88310, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 32950, -13200, 95150, 180)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 36950, -13200, 95150, 180)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 1, 0, 20)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_387D():

        label("loc_387D")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_387D")

    QueueWorkItem2(0x8, 3, lambda_387D)

    def lambda_389B():

        label("loc_389B")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_389B")

    QueueWorkItem2(0x9, 3, lambda_389B)
    OP_68(34950, -11700, 95150, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11650, 0)
    FadeToBright(1000, 0)
    MoveCamera(50, 30, 0, 3000)
    SetCameraDistance(13650, 3000)
    OP_6F(0x79)
    OP_0D()
    SetCameraDistance(22000, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)

    def lambda_392D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_392D)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_3987():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3987)
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    CancelBlur(2500)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_6F(0x79)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Sleep(1800)
    Fade(1000)
    OP_68(34950, -10750, 104850, 0)
    MoveCamera(0, 21, 0, 0)
    MoveCamera(0, 12, 0, 3000)
    OP_6E(600, 0)
    SetCameraDistance(22650, 0)
    SetCameraDistance(16650, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0xA, 0x1, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 19)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("Voice of Ariane Road")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apparently\x01",
            "There seems to be \"qualification\".\x02\x03",
            "The main point of the tower is \"iron machine corps\"\x01",
            "The guards protect them.\x02\x03",
            "With preparedness and resolve\x01",
            "You should challenge.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(34950, -12250, 91600, 0)
    OP_68(34950, -12250, 89600, 2500)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B80")
    Sound(540, 0, 50, 0)

    label("loc_3B80")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    ChrTalk(
        0x101,
        (
            "#00008F#11P\"Iron Corps\" ……\x01",
            "Are they girls wearing armor?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CFD")

    ChrTalk(
        0x105,
        (
            "#10406F#12PAmong \"association\"\x01",
            "It is said to be the strongest combat unit.\x02\x03",
            "#10401FAs each person approaches the enforcer\x01",
            "Perhaps it is better to think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D87")

    label("loc_3CFD")


    ChrTalk(
        0x106,
        (
            "#10703F#12P…… That name in the back world\x01",
            "I have heard it.\x02\x03",
            "#10701FEvery person, masterclassmen#6RMaster class#of\x01",
            "\"Using weapons\" or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D87")


    ChrTalk(
        0x104,
        (
            "#00306F#12P…… certainly equivalent,\x01",
            "It was a daughter who seemed to be dangerous.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3E46():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E46)
    Sleep(50)

    def lambda_3E56():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E56)
    Sleep(50)

    def lambda_3E66():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3E66)
    Sleep(50)

    def lambda_3E76():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3E76)
    Sleep(50)

    def lambda_3E86():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3E86)
    Sleep(50)

    def lambda_3E96():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_3E96)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x103,
        "#00205F#6P… … Elly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PDo you have something to worry about?\x02",
    )

    CloseMessageWindow()
    OP_64(0x102)
    Sleep(500)
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106F#11POh, yes ….\x01",
            "It's not a big deal though.\x02\x03",
            "#00101F\"Steel's Saint\" … …\x01",
            "Although I was hiding my face with a helmet\x01",
            "I was wondering who he was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PThat's … … that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PBothering to hide your face\x01",
            "Is there any circumstance ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4087")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_402E")
    OP_FC(0xB)
    Jump("loc_4043")

    label("loc_402E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4043")
    OP_FC(0x6)

    label("loc_4043")


    ChrTalk(
        0x105,
        (
            "#10406F#13PWell, even the Knights of the Star Cup\x01",
            "I can not grasp the real face and feature.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4087")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_410A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40B1")
    OP_FC(0xB)
    Jump("loc_40C6")

    label("loc_40B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40C6")
    OP_FC(0x6)

    label("loc_40C6")


    ChrTalk(
        0x106,
        (
            "#10708F#13P…… Unlike me Gender\x01",
            "It's not fake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_418F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4134")
    OP_FC(0xB)
    Jump("loc_4149")

    label("loc_4134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4149")
    OP_FC(0x6)

    label("loc_4149")


    ChrTalk(
        0x109,
        (
            "#10108F#13PHe said that he had a criminal record\x01",
            "Even for simple reasons it does not seem to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418F")


    ChrTalk(
        0x101,
        (
            "#00003F#5P… … That's right.\x02\x03",
            "#00008FAlso in the confrontation with them\x01",
            "You may be able to see it.\x02\x03",
            "#00013F─ ─ It's not her words\x01",
            "Hold on to resolve and resolve!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PYeah … …!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4270")
    OP_FC(0xB)
    Jump("loc_4285")

    label("loc_4270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4285")
    OP_FC(0x6)

    label("loc_4285")


    ChrTalk(
        0x109,
        "#10107F#13PYes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_42ED")

    label("loc_42A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42BD")
    OP_FC(0xB)
    Jump("loc_42D2")

    label("loc_42BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42D2")
    OP_FC(0x6)

    label("loc_42D2")


    ChrTalk(
        0x106,
        "#10707F#13PYes……!\x02",
    )

    CloseMessageWindow()

    label("loc_42ED")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Upon completing the strategy of \"Tower of Hoshi\"\x01",
            "For a while, cross-border areas\x01",
            "You will not be able to come and go freely.\x02\x03",
            "Because you can not use terminals etc\x01",
            "be careful.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0xA, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, 34740, -13200, 89500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 6)
    OP_29(0xB0, 0x1, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    OP_24(0x9B)
    EventEnd(0x5)
    Return()

    # Function_18_3617 end

    def Function_19_440B(): pass

    label("Function_19_440B")

    Sound(116, 0, 100, 0)
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xBB8)
    ClearMapObjFlags(0x1, 0x10)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x0, 0xF, 0x0, 0x8)
    OP_79(0x1)
    OP_24(0x9B)
    Sound(149, 0, 80, 0)
    OP_74(0x1, 0x1E)
    Return()

    # Function_19_440B end

    def Function_20_444F(): pass

    label("Function_20_444F")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_20_444F end

    def Function_21_4468(): pass

    label("Function_21_4468")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ In the meantime, you are prohibited from entering without permission *\x01",
            "※ Crossbell Guard ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_21_4468 end

    SaveToFile()

Try(main)
