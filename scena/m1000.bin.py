from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Vanguard",               # 1
        "Vanguard",               # 2
        "Aines the Stout",        # 3
        "SE制御",                 # 4
        "bm1080",                 # 5
        "To St. Ursula Byroad",   # 6
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

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "To St. Ursula Byroad")

    ChipFrameInfo(1224, 0)                                       # 0

    ScpFunction((
        "Function_0_4C8",          # 00, 0
        "Function_1_580",          # 01, 1
        "Function_2_630",          # 02, 2
        "Function_3_B7C",          # 03, 3
        "Function_4_D8F",          # 04, 4
        "Function_5_10CC",         # 05, 5
        "Function_6_1160",         # 06, 6
        "Function_7_1195",         # 07, 7
        "Function_8_1BF0",         # 08, 8
        "Function_9_201A",         # 09, 9
        "Function_10_209F",        # 0A, 10
        "Function_11_243C",        # 0B, 11
        "Function_12_24FA",        # 0C, 12
        "Function_13_252F",        # 0D, 13
        "Function_14_2ABE",        # 0E, 14
        "Function_15_37CE",        # 0F, 15
        "Function_16_37E9",        # 10, 16
        "Function_17_3825",        # 11, 17
        "Function_18_3872",        # 12, 18
        "Function_19_4738",        # 13, 19
        "Function_20_477C",        # 14, 20
        "Function_21_4795",        # 15, 21
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_E7C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E5C"),
        (SWITCH_DEFAULT, "loc_E6D"),
    )


    label("loc_E5C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_E77")

    label("loc_E6D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E77")

    Jump("loc_10B9")

    label("loc_E7C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_EAE")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_EAE")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE2"),
        (1, "loc_FE6"),
        (2, "loc_1077"),
        (SWITCH_DEFAULT, "loc_10AF"),
    )


    label("loc_EE2")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F13")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F23")

    label("loc_F13")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F23")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F79")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9C")
    Sound(461, 0, 100, 0)

    label("loc_F9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FBC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_FCC")

    label("loc_FBC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_FCC")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_E07")

    label("loc_FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1058")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_101B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1033")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_102E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1033")

    label("loc_102E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1033")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1072")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1068")
    OP_AF(0xFB)
    Jump("loc_1072")

    label("loc_1068")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1072")

    Jump("loc_10B9")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1090")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10AA")

    label("loc_1090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_10A0")
    OP_AF(0xFB)
    Jump("loc_10AA")

    label("loc_10A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10AA")

    Jump("loc_10B9")

    label("loc_10AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B9")

    Jump("loc_E07")

    label("loc_10BE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_D8F end

    def Function_5_10CC(): pass

    label("Function_5_10CC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1127")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_111C")
    Sound(2502, 255, 100, 0)
    Jump("loc_1122")

    label("loc_111C")

    Sound(2503, 255, 100, 0)

    label("loc_1122")

    Jump("loc_114B")

    label("loc_1127")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1145")
    Sound(3347, 255, 100, 0)
    Jump("loc_114B")

    label("loc_1145")

    Sound(3348, 255, 100, 0)

    label("loc_114B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_10CC end

    def Function_6_1160(): pass

    label("Function_6_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_1171")
    Call(0, 9)
    Jump("loc_1185")

    label("loc_1171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_1182")
    Call(0, 8)
    Jump("loc_1185")

    label("loc_1182")

    Call(0, 7)

    label("loc_1185")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    Return()

    # Function_6_1160 end

    def Function_7_1195(): pass

    label("Function_7_1195")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1963")

    AnonymousTalk(
        0x105,
        (
            "#10401FOuroboros is protecting it,\x01",
            "eh?\x02\x03",
            "#10403FThe armored girl guarding\x01",
            "the door is one of the Steel\x01",
            "Maiden's subordinates.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00013FAnd those archaisms on either\x01",
            "side of her are huge... and of\x01",
            "a type I've never seen before.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1383")

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw them in the database. They look\x01",
            "similar to a model was used by Ouroboros\x01",
            "during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10401FThe Vanguard, I think it was?\x01",
            "A highly efficient model for\x01",
            "hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_1383")


    AnonymousTalk(
        0x105,
        (
            "#10403FThose are a highly efficient model for\x01",
            "hand-to-hand combat, used by Ouroboros\x01",
            "during the Liberl phenomenon.\x02\x03",
            "#10400FThe Vanguard, I believe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141C")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(
        0x101,
        (
            "#00003F#6P...At any rate, I think\x01",
            "it's best to pull out\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PEven so, it looks like you\x01",
            "know quite a bit about\x01",
            "Ouroboros, don't you Wazy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1575")

    label("loc_14DA")


    ChrTalk(
        0x101,
        (
            "#00003F#6P...At any rate, I think\x01",
            "it's best to pull out for\x01",
            "now.\x02\x03",
            "#00005FEven so, it looks like you\x01",
            "know quite a bit about\x01",
            "Ouroboros, don't you Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1575")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1670")

    ChrTalk(
        0x105,
        (
            "#10404F#12PHaha... Well, a fair\x01",
            "amount, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CThe Gralsritter and Ouroboros\x01",
            "have clashed many times in\x01",
            "the shadows of history.\x02\x03",
            "During those clashes,\x01",
            "knowledge of one's enemy is\x01",
            "of the utmost importance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1758")

    label("loc_1670")


    ChrTalk(
        0x105,
        (
            "#10404F#6PHaha... Well, a fair amount, I\x01",
            "guess?\x02\x03",
            "#10400FIt's because Gralsritter and\x01",
            "Ouroboros have clashed many\x01",
            "times in the shadows of history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see... In that case,\x01",
            "knowledge of one's enemy\x01",
            "must be critical.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")


    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, the situation on both our and\x01",
            "Ouroboros' sides are ever changing.\x01",
            "To be honest, it's a vicious circle.\x02\x03",
            "#10402FWhoops. If I carelessly tell you\x01",
            "things like this, I wonder if Abbas\x01",
            "would get mad at me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1881")

    ChrTalk(
        0x109,
        "#10106F#6PG-Geez, Wazy...\x02",
    )

    CloseMessageWindow()

    label("loc_1881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1903")

    ChrTalk(
        0x106,
        (
            "#10709F#6PA-Ahaha... Abbas seems\x01",
            "to have it hard too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6P...Let's leave this\x01",
            "place for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_195E")

    label("loc_1903")


    ChrTalk(
        0x101,
        (
            "#00006F#6PAbbas seems to have it\x01",
            "hard too.\x02\x03",
            "#00000F...Let's leave this\x01",
            "place for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195E")

    Jump("loc_1BA6")

    label("loc_1963")


    AnonymousTalk(
        0x101,
        (
            "#00003F#6POuroboros is protecting\x01",
            "it, eh?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00103F#6PI wonder if the person\x01",
            "standing there is one of the\x01",
            "Steel Maiden's subordinates.\x02\x03",
            "#00101FAnd, as for those white\x01",
            "archaisms...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208F#6PI saw them in the database. They look\x01",
            "similar to a model was used by Ouroboros\x01",
            "during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10101F#6PBased on its weapons, it\x01",
            "looks like a hand-to-\x01",
            "hand combat type...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00303F#6P...Just getting close to\x01",
            "them would be suicide.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00001F#6P...Anyhow, let's pull\x01",
            "out for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10700F#6PYes, let's leave this\x01",
            "place for the time\x01",
            "being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA6")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BC0")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1BC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BD9")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1BD9")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_7_1195 end

    def Function_8_1BF0(): pass

    label("Function_8_1BF0")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C8A")

    AnonymousTalk(
        0x105,
        (
            "#10401FOuroboros is here too, eh?\x02\x03",
            "#10403FThe armored girl guarding\x01",
            "the door is one of the Steel\x01",
            "Maiden's subordinates.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0A")

    label("loc_1C8A")


    AnonymousTalk(
        0x106,
        (
            "#10701FOuroboros is here too,\x01",
            "huh...\x02\x03",
            "#10703FThe armored girl guarding\x01",
            "the door is one of the Steel\x01",
            "Maiden's subordinates.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0A")


    AnonymousTalk(
        0x104,
        (
            "#00301FAnd those archaisms on\x01",
            "either side of her are\x01",
            "huge...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw them in the database. They look\x01",
            "similar to a model was used by Ouroboros\x01",
            "during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E38")

    AnonymousTalk(
        0x105,
        (
            "#10401FThe Vanguard, I think it was?\x01",
            "A highly efficient model for\x01",
            "hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E87")

    label("loc_1E38")


    AnonymousTalk(
        0x109,
        (
            "#10101FBased on its weapons, it\x01",
            "looks like a hand-to-\x01",
            "hand combat type...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E87")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F2F")

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CCarelessly picking a\x01",
            "fight with them doesn't\x01",
            "sound like a good plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, let's leave this\x01",
            "place for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1F2F")


    ChrTalk(
        0x101,
        (
            "#00003F#6P...I think it's best to\x01",
            "pass on carelessly\x01",
            "fighting with them.\x02\x03",
            "#00000FLet's leave this place\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(
        0x106,
        "#10701F#6PYes, let's.\x02",
    )

    CloseMessageWindow()

    label("loc_1FD0")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FEA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1FEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2003")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2003")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_8_1BF0 end

    def Function_9_201A(): pass

    label("Function_9_201A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIt looks like Ouroboros\x01",
            "is guarding further\x01",
            "ahead.\x02\x03",
            "#00001F...It seems best to step\x01",
            "away for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6370, -3700, 23670, 19)
    EventEnd(0x4)
    Return()

    # Function_9_201A end

    def Function_10_209F(): pass

    label("Function_10_209F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20E1")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_20D6():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20D6)
    Sleep(50)

    label("loc_20E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2123")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2118():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2118)
    Sleep(50)

    label("loc_2123")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2165")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_215A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_215A)
    Sleep(50)

    label("loc_2165")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21AE")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0xA, 500)

    def lambda_21A3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21A3)
    Sleep(50)

    label("loc_21AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F7")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0xA, 500)

    def lambda_21EC():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21EC)
    Sleep(50)

    label("loc_21F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2240")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0xA, 500)

    def lambda_2235():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2235)
    Sleep(50)

    label("loc_2240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2289")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0xA, 500)

    def lambda_227E():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_227E)
    Sleep(50)

    label("loc_2289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D2")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0xA, 500)

    def lambda_22C7():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_22C7)
    Sleep(50)

    label("loc_22D2")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThose are...\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2387")
    SetChrPos(0x0, 6840, -3700, 25000, 20)

    label("loc_2387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23A7")
    SetChrPos(0x1, 5580, -3700, 24600, 20)

    label("loc_23A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23C7")
    SetChrPos(0x2, 8390, -3700, 25230, 20)

    label("loc_23C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23E7")
    SetChrPos(0x3, 6770, -3700, 22930, 20)

    label("loc_23E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2411")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, 8320, -3700, 23330, 20)

    label("loc_2411")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_243B")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, 5820, -3700, 23330, 20)

    label("loc_243B")

    Return()

    # Function_10_209F end

    def Function_11_243C(): pass

    label("Function_11_243C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_245C")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_245C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2471")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2471")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2486")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2486")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_249B")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_249B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24B0")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24C5")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24DA")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24EF")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24EF")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_11_243C end

    def Function_12_24FA(): pass

    label("Function_12_24FA")

    Fade(500)
    OP_68(9400, -4400, 31020, 0)
    MoveCamera(20, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Return()

    # Function_12_24FA end

    def Function_13_252F(): pass

    label("Function_13_252F")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(32640, -8500, 94450, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14430, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25F9")
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
    Jump("loc_2658")

    label("loc_25F9")

    SetChrPos(0x101, 33980, -13200, 91570, 0)
    SetChrPos(0x102, 35370, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2658")

    OP_68(32640, -9700, 94450, 3000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2729")

    def lambda_267E():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_267E)
    Sleep(50)

    def lambda_269B():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_269B)
    Sleep(50)

    def lambda_26B8():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26B8)
    Sleep(50)

    def lambda_26D5():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26D5)
    Sleep(50)

    def lambda_26F2():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_26F2)
    Sleep(50)

    def lambda_270F():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_270F)
    Jump("loc_27B7")

    label("loc_2729")


    def lambda_272E():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_272E)
    Sleep(50)

    def lambda_274B():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_274B)
    Sleep(50)

    def lambda_2768():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2768)
    Sleep(50)

    def lambda_2785():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2785)
    Sleep(50)

    def lambda_27A2():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_27A2)

    label("loc_27B7")

    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWe've arrived at the\x01",
            "Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, it's been a while\x01",
            "since we were last here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FHmm. Looking at it from\x01",
            "up close, it's quite\x01",
            "tall.\x02\x03",
            "#10304FLooks worthy of\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThe barricade's been\x01",
            "removed, so we can begin our\x01",
            "investigation immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29FA")

    ChrTalk(
        0x104,
        (
            "#00304FWell, let's move in\x01",
            "caref─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FLet's proceed taking\x01",
            "care not to let our\x01",
            "guard down too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FMrr... How typical of\x01",
            "you, PeTiote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, what Tio said.\x02\x03",
            "#00000FAlright then. Shall we\x01",
            "get started?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A65")

    label("loc_29FA")


    ChrTalk(
        0x104,
        "#00304FLet's move in carefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, agreed.\x02\x03",
            "#00000FAlright then. Shall we\x01",
            "get started?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A8E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_2A98")

    label("loc_2A8E")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2A98")

    SetChrPos(0x0, 34460, -13200, 96070, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x2)
    SetScenarioFlags(0x153, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_252F end

    def Function_14_2ABE(): pass

    label("Function_14_2ABE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B0E")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_2B0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B26")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_2B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B3E")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_2B3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B56")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_2B56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B6E")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_2B6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B86")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_2B86")

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

    def lambda_2D65():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D65)
    Sleep(50)

    def lambda_2D7D():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D7D)
    Sleep(50)

    def lambda_2D95():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2D95)
    Sleep(50)

    def lambda_2DAD():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DAD)
    Sleep(50)

    def lambda_2DC5():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2DC5)
    Sleep(50)

    def lambda_2DDD():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2DDD)
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
        "#00108F#12PWhite archaisms...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    ChrTalk(
        0x101,
        (
            "#00013F#12PThey're big... and a\x01",
            "type I've never seen\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PI saw them in the database. They look\x01",
            "like a model that was used by Ouroboros\x01",
            "during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FA6")

    ChrTalk(
        0x105,
        (
            "#10401F#12PThe Vanguard, was it? It\x01",
            "should be a highly efficient\x01",
            "model for hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3006")

    label("loc_2FA6")


    ChrTalk(
        0x109,
        (
            "#10101F#12PThe Vanguard, I think it was?\x01",
            "A highly efficient model for\x01",
            "hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3006")

    Jump("loc_3177")

    label("loc_300B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3073")

    ChrTalk(
        0x105,
        (
            "#10401F#12PBased on its weapons, it\x01",
            "looks like a hand-to-\x01",
            "hand combat type...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C3")

    label("loc_3073")


    ChrTalk(
        0x109,
        (
            "#10101F#12PLooking at them closely,\x01",
            "it's obvious how\x01",
            "threatening they are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C3")


    ChrTalk(
        0x101,
        (
            "#00013F#12PThey're of a model used\x01",
            "for hand-to-hand combat,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PIt appears that gaining access\x01",
            "to the tower is going to require\x01",
            "more effort that I thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3177")

    Sleep(300)
    StopBGM(0x1388)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3895V#30A#30WVanguard F3 Sleipnir...\x02\x03",
            "#3896V#40A#30WA machine specially\x01",
            "tuned for use by my\x01",
            "Stahlritter.\x07\x00\x02",
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
        "#00007F#3P#N#15AYou're...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3357")

    ChrTalk(
        0x106,
        "#10701F#6P#N#15AThe Steel Maiden!\x02",
    )

    CloseMessageWindow()
    Jump("loc_337E")

    label("loc_3357")


    ChrTalk(
        0x109,
        "#10101F#6P#N#15AThe Steel Maiden!\x02",
    )

    CloseMessageWindow()

    label("loc_337E")

    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("Arianrhod's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3897V#40A#30WIt appears you broke\x01",
            "through Campanella's\x01",
            "defenses with ease.\x02\x03",
            "#3898V#45A#30WIn this tower of fate,\x01",
            "my squad shall be your\x01",
            "opponents.\x07\x00\x02",
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

    def lambda_34EE():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34EE)

    def lambda_3503():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3503)
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
        "#00010F#12PKh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35D2")
    Sound(540, 0, 50, 0)

    label("loc_35D2")

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
    SetChrName("Arianrhod's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WFirst, show me you are\x01",
            "capable of breaking\x01",
            "through their defenses.\x02\x03",
            "Then, we shall talk.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00307F#12P#NHah! Bring it on!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#12PWe'll crush them with\x01",
            "all our might!\x02",
        )
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

    def lambda_376D():
        OP_9B(0x1, 0xFE, 0xFFFB, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_376D)

    def lambda_3782():
        OP_9B(0x1, 0xFE, 0x5, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3782)
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

    # Function_14_2ABE end

    def Function_15_37CE(): pass

    label("Function_15_37CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37E8")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_15_37CE")

    label("loc_37E8")

    Return()

    # Function_15_37CE end

    def Function_16_37E9(): pass

    label("Function_16_37E9")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3801():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3801)
    Sleep(100)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_37E9 end

    def Function_17_3825(): pass

    label("Function_17_3825")

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

    # Function_17_3825 end

    def Function_18_3872(): pass

    label("Function_18_3872")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38B1")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_38B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38C9")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_38C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38E1")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_38E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38F9")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_38F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3911")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_3911")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3929")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_3929")

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

    def lambda_3AD8():

        label("loc_3AD8")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_3AD8")

    QueueWorkItem2(0x8, 3, lambda_3AD8)

    def lambda_3AF6():

        label("loc_3AF6")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_3AF6")

    QueueWorkItem2(0x9, 3, lambda_3AF6)
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

    def lambda_3B88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3B88)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_3BE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3BE2)
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
    SetChrName("Arianrhod's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─It appears you are\x01",
            "qualified.\x02\x03",
            "The Stahlritter soldiers\x01",
            "guard the tower's\x01",
            "important positions.\x02\x03",
            "Challenge them with\x01",
            "resolve and\x01",
            "determination.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DE9")
    Sound(540, 0, 50, 0)

    label("loc_3DE9")

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
            "#00008F#11PThe Stahlritter... Those\x01",
            "armor-clad girls, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F9C")

    ChrTalk(
        0x105,
        (
            "#10406F#12PA fighting squad said to be the\x01",
            "strongest even within\x01",
            "Ouroboros.\x02\x03",
            "#10401FIt seems best to assume each of\x01",
            "them has strength approaching\x01",
            "that of an enforcer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FFE")

    label("loc_3F9C")


    ChrTalk(
        0x106,
        (
            "#10703F#12PI've heard that name in\x01",
            "the underworld.\x02\x03",
            "#10701FEach of them is a master\x01",
            "warrior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFE")


    ChrTalk(
        0x104,
        (
            "#00306F#12PIndeed, they looked like\x01",
            "quite a dangerous group\x01",
            "of girls.\x02",
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

    def lambda_40CC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40CC)
    Sleep(50)

    def lambda_40DC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_40DC)
    Sleep(50)

    def lambda_40EC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_40EC)
    Sleep(50)

    def lambda_40FC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_40FC)
    Sleep(50)

    def lambda_410C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_410C)
    Sleep(50)

    def lambda_411C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_411C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x103,
        "#00205F#6P...Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PAre you worried about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x102)
    Sleep(500)
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106F#11PAh, yes, but... It's nothing so\x01",
            "important.\x02\x03",
            "#00101FThe Steel Maiden... I was wondering\x01",
            "what kind of person she is, since she\x01",
            "hides her face under that helmet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12PWell... You've got a\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PCould there be some\x01",
            "reason she goes out of\x01",
            "her way to hide her face?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4356")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42EA")
    OP_FC(0xB)
    Jump("loc_42FF")

    label("loc_42EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42FF")
    OP_FC(0x6)

    label("loc_42FF")


    ChrTalk(
        0x105,
        (
            "#10406F#13PEven the Gralsritter\x01",
            "can't seem to get a hold\x01",
            "of her face and origins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4356")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4380")
    OP_FC(0xB)
    Jump("loc_4395")

    label("loc_4380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4395")
    OP_FC(0x6)

    label("loc_4395")


    ChrTalk(
        0x106,
        (
            "#10708F#13PUnlike me, she doesn't\x01",
            "hide her gender...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4463")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43F9")
    OP_FC(0xB)
    Jump("loc_440E")

    label("loc_43F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_440E")
    OP_FC(0x6)

    label("loc_440E")


    ChrTalk(
        0x109,
        (
            "#10108F#13PIt doesn't even seem like\x01",
            "a simple reason, like her\x01",
            "criminal record.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4463")


    ChrTalk(
        0x101,
        (
            "#00003F#5PI wonder...\x02\x03",
            "#00008FMaybe we will discover that\x01",
            "while confronting those girls.\x02\x03",
            "#00013F─I don't want to use her words,\x01",
            "but let's face them with\x01",
            "resolve and determination!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PRight!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4593")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_455F")
    OP_FC(0xB)
    Jump("loc_4574")

    label("loc_455F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4574")
    OP_FC(0x6)

    label("loc_4574")


    ChrTalk(
        0x109,
        "#10107F#13PYes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45D9")

    label("loc_4593")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45AD")
    OP_FC(0xB)
    Jump("loc_45C2")

    label("loc_45AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45C2")
    OP_FC(0x6)

    label("loc_45C2")


    ChrTalk(
        0x106,
        "#10707F#13PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_45D9")

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
            "Until you finish exploring the Tower of\x01",
            "Stargaze, you will not be able to freely\x01",
            "move throughout Crossbell for a while.\x02\x03",
            "You will not be able to use the terminal\x01",
            "and other functions as well, so please\x01",
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

    # Function_18_3872 end

    def Function_19_4738(): pass

    label("Function_19_4738")

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

    # Function_19_4738 end

    def Function_20_477C(): pass

    label("Function_20_477C")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_20_477C end

    def Function_21_4795(): pass

    label("Function_21_4795")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　Authorised Personnel Only    ※\x01",
            "※　　　　Crossbell CGF　　　  ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_21_4795 end

    SaveToFile()

Try(main)
