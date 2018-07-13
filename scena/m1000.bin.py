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
        "Function_5_10C8",         # 05, 5
        "Function_6_115C",         # 06, 6
        "Function_7_1191",         # 07, 7
        "Function_8_1C9C",         # 08, 8
        "Function_9_210A",         # 09, 9
        "Function_10_21A7",        # 0A, 10
        "Function_11_2544",        # 0B, 11
        "Function_12_2602",        # 0C, 12
        "Function_13_2637",        # 0D, 13
        "Function_14_2BE8",        # 0E, 14
        "Function_15_38FC",        # 0F, 15
        "Function_16_3917",        # 10, 16
        "Function_17_3953",        # 11, 17
        "Function_18_39A0",        # 12, 18
        "Function_19_487A",        # 13, 19
        "Function_20_48BE",        # 14, 20
        "Function_21_48D7",        # 15, 21
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_E7A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E5A"),
        (SWITCH_DEFAULT, "loc_E6B"),
    )


    label("loc_E5A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_E75")

    label("loc_E6B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E75")

    Jump("loc_10B5")

    label("loc_E7A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_EAC")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_EAC")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EDE"),
        (1, "loc_FE2"),
        (2, "loc_1073"),
        (SWITCH_DEFAULT, "loc_10AB"),
    )


    label("loc_EDE")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F0F")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F1F")

    label("loc_F0F")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F1F")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F75")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F75")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F98")
    Sound(461, 0, 100, 0)

    label("loc_F98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FB8")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_FC8")

    label("loc_FB8")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_FC8")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_E07")

    label("loc_FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1054")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_1017")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_102F")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_102A")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_102F")

    label("loc_102A")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_102F")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_106E")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1064")
    OP_AF(0xFB)
    Jump("loc_106E")

    label("loc_1064")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_106E")

    Jump("loc_10B5")

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A6")

    label("loc_108C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_109C")
    OP_AF(0xFB)
    Jump("loc_10A6")

    label("loc_109C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A6")

    Jump("loc_10B5")

    label("loc_10AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B5")

    Jump("loc_E07")

    label("loc_10BA")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_D8F end

    def Function_5_10C8(): pass

    label("Function_5_10C8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1123")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1118")
    Sound(2502, 255, 100, 0)
    Jump("loc_111E")

    label("loc_1118")

    Sound(2503, 255, 100, 0)

    label("loc_111E")

    Jump("loc_1147")

    label("loc_1123")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1141")
    Sound(3347, 255, 100, 0)
    Jump("loc_1147")

    label("loc_1141")

    Sound(3348, 255, 100, 0)

    label("loc_1147")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_10C8 end

    def Function_6_115C(): pass

    label("Function_6_115C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_116D")
    Call(0, 9)
    Jump("loc_1181")

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_117E")
    Call(0, 8)
    Jump("loc_1181")

    label("loc_117E")

    Call(0, 7)

    label("loc_1181")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    Return()

    # Function_6_115C end

    def Function_7_1191(): pass

    label("Function_7_1191")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B6")

    AnonymousTalk(
        0x105,
        (
            "#10401F"Ouroboros" is protecting it, eh...?\x02\x03",
            "#10403FThe girl in armor guarding the door\x01",
            "is one the "Steel Maiden" subordinates.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00013FThose archaisms at her side are big...\x01",
            "They're of a type I've never seen.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1378")

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw them in the database.\x01",
            "They look like a model that was used by\x01",
            "the Society during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10401FThe "Vanguard", was it? It should be a\x01",
            "highly efficient model for hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_1378")


    AnonymousTalk(
        0x105,
        (
            "#10403FThose should be a highly efficient model for\x01",
            "hand-to-hand combat the Society used at the\x01",
            "time of the Liberl phenomenon.\x02\x03",
            "#10400FThe "Vanguard", I believe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141F")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DD")

    ChrTalk(
        0x101,
        (
            "#00003F#6P...At any rate, it would be\x01",
            "better to pull out for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PEven so, Wazy, it seems\x01",
            "you're very knowledgeable\x01",
            "about the "Society", huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1578")

    label("loc_14DD")


    ChrTalk(
        0x101,
        (
            "#00003F#6P...At any rate, it would be\x01",
            "better to pull out for now.\x02\x03",
            "#00005FEven so, Wazy, it seems\x01",
            "you're very knowledgeable\x01",
            "about the "Society", huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1578")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1689")

    ChrTalk(
        0x105,
        (
            "#10404F#12PHu hu...\x01",
            "Well, somewhat, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CThe "Knights" and the "Society" are\x01",
            "recorded to have confronted each other\x01",
            "many times in the shadows of history.\x02\x03",
            "Even among them, knowing their\x01",
            "opponents is the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1793")

    label("loc_1689")


    ChrTalk(
        0x105,
        (
            "#10404F#6PHu hu...\x01",
            "Well, somewhat, I guess?\x02\x03",
            "#10400FThe "Knights" and the "Society" are\x01",
            "recorded to have confronted each other\x01",
            "many times in the shadows of history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see...If the circumstances are like that,\x01",
            "knowing your opponents is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1793")


    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, since the "Knights" and the "Society"\x01",
            "circumstances are always changing,\x01",
            "they're frankly into a vicious circle.\x02\x03",
            "#10402FOops, I wonder if Abbass would get angry at\x01",
            "me for talking carelessly about such things?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18C4")

    ChrTalk(
        0x109,
        "#10106F#6PG-Geez, Wazy...\x02",
    )

    CloseMessageWindow()

    label("loc_18C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_194D")

    ChrTalk(
        0x106,
        (
            "#10709F#6PA-Ahaha...\x01",
            "Mr. Abbas seems to have it hard too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P...Let's walk away from here for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B1")

    label("loc_194D")


    ChrTalk(
        0x101,
        (
            "#00006F#6PMr. Abbas seems to have it hard too...\x02\x03",
            "#00000F...Let's walk away from here for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B1")

    Jump("loc_1C52")

    label("loc_19B6")


    AnonymousTalk(
        0x101,
        "#00003F#6P"Ouroboros" is protecting it, eh...?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00103F#6PI think that who's standing over there\x01",
            "is one of the subordinates who\x01",
            "were accompanying the "Steel Maiden".\x02\x03",
            "#00101FAlso, that white archaism...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208F#6PI saw it in the database.\x01",
            "It appears to be a model that was used by\x01",
            "the Society during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10101F#6PJudging by its armaments, it seems a highly\x01",
            "efficient model for hand-to-hand combat...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00303F#6P...I'm sure that gettin' close\x01",
            "to it nonchalantly is\x01",
            "gonna be a suicidal act.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00001F#6P...At any rate, it would be\x01",
            "better to pull out for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10700F#6PYes, let's walk away for the time being.\x02",
    )

    CloseMessageWindow()

    label("loc_1C52")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C6C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1C6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C85")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1C85")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_7_1191 end

    def Function_8_1C9C(): pass

    label("Function_8_1C9C")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D39")

    AnonymousTalk(
        0x105,
        (
            "#10401F"Ouroboros" is here too, eh...?\x02\x03",
            "#10403FThe girl in armor guarding the door\x01",
            "is one the "Steel Maiden" subordinates.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1D39")


    AnonymousTalk(
        0x106,
        (
            "#10701F"Ouroboros" is guarding here too...\x02\x03",
            "#10703FThe girl in armor guarding the door\x01",
            "is one the "Steel Maiden" subordinates.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBD")


    AnonymousTalk(
        0x104,
        (
            "#00301FThe archaisms at her side\x01",
            "are pretty big too...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00208FI saw them in the database.\x01",
            "They look like a model that was used by\x01",
            "the Society during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EED")

    AnonymousTalk(
        0x105,
        (
            "#10401FThe "Vanguard", was it? It should be a\x01",
            "highly efficient model for hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1EED")


    AnonymousTalk(
        0x109,
        (
            "#10101FJudging by their armaments, they look like\x01",
            "highly efficient models for hand-to-hand combat...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F57")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FF8")

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CAs you can imagine, dealing with them\x01",
            "carelessly is not a good plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's walk away for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_208D")

    label("loc_1FF8")


    ChrTalk(
        0x101,
        (
            "#00003F#6P...As expected, it seems it's better give up\x01",
            "the idea to deal with them in a careless way.\x02\x03",
            "#00000FLet's walk away from here for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20C0")

    ChrTalk(
        0x106,
        "#10701F#6PYes, let's do that.\x02",
    )

    CloseMessageWindow()

    label("loc_20C0")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20DA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_20DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20F3")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_20F3")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_8_1C9C end

    def Function_9_210A(): pass

    label("Function_9_210A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIt looks like the "Society"\x01",
            "is guarding further ahead.\x02\x03",
            "#00001F...It seems that, for now,\x01",
            "it would be better to pull out.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6370, -3700, 23670, 19)
    EventEnd(0x4)
    Return()

    # Function_9_210A end

    def Function_10_21A7(): pass

    label("Function_10_21A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21E9")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_21DE():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21DE)
    Sleep(50)

    label("loc_21E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222B")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2220():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2220)
    Sleep(50)

    label("loc_222B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_226D")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2262():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2262)
    Sleep(50)

    label("loc_226D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B6")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0xA, 500)

    def lambda_22AB():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22AB)
    Sleep(50)

    label("loc_22B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22FF")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0xA, 500)

    def lambda_22F4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_22F4)
    Sleep(50)

    label("loc_22FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2348")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0xA, 500)

    def lambda_233D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_233D)
    Sleep(50)

    label("loc_2348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2391")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0xA, 500)

    def lambda_2386():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2386)
    Sleep(50)

    label("loc_2391")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23DA")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0xA, 500)

    def lambda_23CF():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_23CF)
    Sleep(50)

    label("loc_23DA")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_248F")
    SetChrPos(0x0, 6840, -3700, 25000, 20)

    label("loc_248F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24AF")
    SetChrPos(0x1, 5580, -3700, 24600, 20)

    label("loc_24AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24CF")
    SetChrPos(0x2, 8390, -3700, 25230, 20)

    label("loc_24CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24EF")
    SetChrPos(0x3, 6770, -3700, 22930, 20)

    label("loc_24EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2519")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, 8320, -3700, 23330, 20)

    label("loc_2519")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2543")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, 5820, -3700, 23330, 20)

    label("loc_2543")

    Return()

    # Function_10_21A7 end

    def Function_11_2544(): pass

    label("Function_11_2544")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2564")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2564")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2579")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2579")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_258E")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_258E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25A3")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25B8")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25CD")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25E2")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25F7")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25F7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_11_2544 end

    def Function_12_2602(): pass

    label("Function_12_2602")

    Fade(500)
    OP_68(9400, -4400, 31020, 0)
    MoveCamera(20, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Return()

    # Function_12_2602 end

    def Function_13_2637(): pass

    label("Function_13_2637")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(32640, -8500, 94450, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14430, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2701")
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
    Jump("loc_2760")

    label("loc_2701")

    SetChrPos(0x101, 33980, -13200, 91570, 0)
    SetChrPos(0x102, 35370, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2760")

    OP_68(32640, -9700, 94450, 3000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2831")

    def lambda_2786():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2786)
    Sleep(50)

    def lambda_27A3():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27A3)
    Sleep(50)

    def lambda_27C0():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27C0)
    Sleep(50)

    def lambda_27DD():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27DD)
    Sleep(50)

    def lambda_27FA():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27FA)
    Sleep(50)

    def lambda_2817():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2817)
    Jump("loc_28BF")

    label("loc_2831")


    def lambda_2836():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2836)
    Sleep(50)

    def lambda_2853():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2853)
    Sleep(50)

    def lambda_2870():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2870)
    Sleep(50)

    def lambda_288D():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_288D)
    Sleep(50)

    def lambda_28AA():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28AA)

    label("loc_28BF")

    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#00000FWe've arrived at the "Tower of Stargaze".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, it's been some time since we've been here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F*phew*, looking at it \x01",
            "closely, it's very tall.\x02\x03",
            "#10304FIt looks worthy to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThe barricade too was removed. It seems\x01",
            "we can begin our investigation at once.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B13")

    ChrTalk(
        0x104,
        "#00304FWell, let's move in caref──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FLet's proceed paying attention to\x01",
            "not let our guard down too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FMrr...\x01",
            "Typical of you, peTiote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, it's like Tio says.\x02\x03",
            "#00000FAll right, then let's\x01",
            "enter immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8F")

    label("loc_2B13")


    ChrTalk(
        0x104,
        "#00304FWell, let's move in carefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, you're right.\x02\x03",
            "#00000FAll right, then let's\x01",
            "enter immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB8")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_2BC2")

    label("loc_2BB8")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2BC2")

    SetChrPos(0x0, 34460, -13200, 96070, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x2)
    SetScenarioFlags(0x153, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_2637 end

    def Function_14_2BE8(): pass

    label("Function_14_2BE8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C38")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_2C38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C50")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_2C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C68")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_2C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C80")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_2C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C98")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_2C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CB0")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_2CB0")

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

    def lambda_2E8F():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E8F)
    Sleep(50)

    def lambda_2EA7():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EA7)
    Sleep(50)

    def lambda_2EBF():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2EBF)
    Sleep(50)

    def lambda_2ED7():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2ED7)
    Sleep(50)

    def lambda_2EEF():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2EEF)
    Sleep(50)

    def lambda_2F07():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2F07)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3147")

    ChrTalk(
        0x101,
        (
            "#00013F#12PThey're big...\x01",
            "They're of a type I've never seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PI saw them in the database.\x01",
            "They look like a model that was used by\x01",
            "the Society during the Liberl phenomenon...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30D4")

    ChrTalk(
        0x105,
        (
            "#10401F#12PThe "Vanguard", was it? It should be a\x01",
            "highly efficient model for hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3142")

    label("loc_30D4")


    ChrTalk(
        0x109,
        (
            "#10101F#12PJudging by their armaments, they look like\x01",
            "highly efficient models for hand-to-hand combat...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3142")

    Jump("loc_3293")

    label("loc_3147")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A5")

    ChrTalk(
        0x105,
        (
            "#10401F#12PThey look like the "Vanguard"\x01",
            "archaisms the Society use.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F2")

    label("loc_31A5")


    ChrTalk(
        0x109,
        (
            "#10101F#12PLooking at them closely, their\x01",
            "dreadfulness is very obvious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F2")


    ChrTalk(
        0x101,
        (
            "#00013F#12PThey are a model for\x01",
            "hand-to-hand combat, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PIt appears that entering inside the "Tower"\x01",
            "is going to require us much effort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3293")

    Sleep(300)
    StopBGM(0x1388)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3895V#30A#30WVanguard F3 "Sleipnir"...\x02\x03",
            "#3896V#40A#30WA machine especially tuned for\x01",
            "being used by my "Stahlritter".\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3484")

    ChrTalk(
        0x106,
        "#10701F#6P#N#15AThe "Steel Maiden"...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_34B0")

    label("loc_3484")


    ChrTalk(
        0x109,
        "#10101F#6P#N#15AThe "Steel Maiden"...!\x02",
    )

    CloseMessageWindow()

    label("loc_34B0")

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
            "#3897V#40A#30WIt appears you broke through\x01",
            "Campanella's defenses without problem.\x02\x03",
            "#3898V#45A#30WIn this tower of karma, my\x01",
            "squad will be your opponents.\x07\x00\x02",
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

    def lambda_3626():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3626)

    def lambda_363B():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_363B)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_370A")
    Sound(540, 0, 50, 0)

    label("loc_370A")

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
            "#30WFirst, show me you will\x01",
            "break through their defences.\x02\x03",
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
        "#00307F#12P#NHah! ...Bring it on!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#12PWe'll crush them with all our might!\x02",
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

    def lambda_389B():
        OP_9B(0x1, 0xFE, 0xFFFB, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_389B)

    def lambda_38B0():
        OP_9B(0x1, 0xFE, 0x5, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38B0)
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

    # Function_14_2BE8 end

    def Function_15_38FC(): pass

    label("Function_15_38FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3916")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_15_38FC")

    label("loc_3916")

    Return()

    # Function_15_38FC end

    def Function_16_3917(): pass

    label("Function_16_3917")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_392F():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_392F)
    Sleep(100)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3917 end

    def Function_17_3953(): pass

    label("Function_17_3953")

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

    # Function_17_3953 end

    def Function_18_39A0(): pass

    label("Function_18_39A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39DF")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_39DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39F7")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_39F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A0F")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_3A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A27")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_3A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A3F")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_3A3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A57")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_3A57")

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

    def lambda_3C06():

        label("loc_3C06")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_3C06")

    QueueWorkItem2(0x8, 3, lambda_3C06)

    def lambda_3C24():

        label("loc_3C24")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_3C24")

    QueueWorkItem2(0x9, 3, lambda_3C24)
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

    def lambda_3CB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3CB6)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_3D10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3D10)
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
            "──It appears you\x01",
            "are "qualified".\x02\x03",
            "The "Stahlritter" soldiers guard\x01",
            "the tower's important positions.\x02\x03",
            "Challenge them with resolve\x01",
            "and determination.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F1D")
    Sound(540, 0, 50, 0)

    label("loc_3F1D")

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
            "#00008F#11PThe "Stahlritter"...\x01",
            "The girls wearing armors, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40D2")

    ChrTalk(
        0x105,
        (
            "#10406F#12PA fighting squad said to be the\x01",
            "strongest even among the "Society".\x02\x03",
            "#10401FIt seems it's better to consider each\x01",
            "of them able to pressure an Enforcer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_40D2")


    ChrTalk(
        0x106,
        (
            "#10703F#12P...I heard that name\x01",
            "in the underworld.\x02\x03",
            "#10701FEach of them is a\x01",
            "master "warrior".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4136")


    ChrTalk(
        0x104,
        (
            "#00306F#12P...Indeed, they looked\x01",
            "quite dangerous girls.\x02",
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

    def lambda_41F7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41F7)
    Sleep(50)

    def lambda_4207():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4207)
    Sleep(50)

    def lambda_4217():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4217)
    Sleep(50)

    def lambda_4227():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4227)
    Sleep(50)

    def lambda_4237():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4237)
    Sleep(50)

    def lambda_4247():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_4247)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x103,
        "#00205F#6P...Miss Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PAre you worried about something?\x02",
    )

    CloseMessageWindow()
    OP_64(0x102)
    Sleep(500)
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00106F#11PAh, yes, but...\x01",
            "It's nothing so important.\x02\x03",
            "#00101FThe "Steel Maiden"...\x01",
            "I was wondering what kind of person is she,\x01",
            "since she's hiding her face under the helmet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PWell...you've got a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PCould she have some circumstances if\x01",
            "she is hiding her face on purpose...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4492")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4423")
    OP_FC(0xB)
    Jump("loc_4438")

    label("loc_4423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4438")
    OP_FC(0x6)

    label("loc_4438")


    ChrTalk(
        0x105,
        (
            "#10406F#13PUhhm, even the Gralsritter can't get\x01",
            "hold of her normal face and origins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4492")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_450E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BC")
    OP_FC(0xB)
    Jump("loc_44D1")

    label("loc_44BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44D1")
    OP_FC(0x6)

    label("loc_44D1")


    ChrTalk(
        0x106,
        (
            "#10708F#13P...Unlike me, she isn't\x01",
            "hiding her gender...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_450E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4538")
    OP_FC(0xB)
    Jump("loc_454D")

    label("loc_4538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_454D")
    OP_FC(0x6)

    label("loc_454D")


    ChrTalk(
        0x109,
        (
            "#10108F#13PIt doesn't even seem it's just simply\x01",
            "because she has a criminal record.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A6")


    ChrTalk(
        0x101,
        (
            "#00003F#5P...Right.\x02\x03",
            "#00008FMaybe we will find out that too\x01",
            "while confronting those girls.\x02\x03",
            "#00013F──I don't want to use her words, but let's\x01",
            "face them with resolve and determination!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PYes...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A7")
    OP_FC(0xB)
    Jump("loc_46BC")

    label("loc_46A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46BC")
    OP_FC(0x6)

    label("loc_46BC")


    ChrTalk(
        0x109,
        "#10107F#13PYes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_471D")

    label("loc_46D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46F0")
    OP_FC(0xB)
    Jump("loc_4705")

    label("loc_46F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4705")
    OP_FC(0x6)

    label("loc_4705")


    ChrTalk(
        0x106,
        "#10707F#13PYes...!\x02",
    )

    CloseMessageWindow()

    label("loc_471D")

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
            "Unless you finish exploring the "Tower of\x01",
            "Stargaze", you will not be able to freely\x01",
            "move to Crossbell areas for while.\x02\x03",
            "Since you will not be able to use the terminal\x01",
            "and other functions too, please be careful.\x07\x00\x02",
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

    # Function_18_39A0 end

    def Function_19_487A(): pass

    label("Function_19_487A")

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

    # Function_19_487A end

    def Function_20_48BE(): pass

    label("Function_20_48BE")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_20_48BE end

    def Function_21_48D7(): pass

    label("Function_21_48D7")

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

    # Function_21_48D7 end

    SaveToFile()

Try(main)
