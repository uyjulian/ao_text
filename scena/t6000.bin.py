from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t6000.bin",                # FileName
        "t6000",                    # MapName
        "t6000",                    # Location
        0x00A4,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 164, 0, 1, 0, 2],
    )

    BuildStringList((
        "t6000",                  # 0
        "Chief Sergei",           # 1
        "Jailkeeper Melvin",      # 2
        "Policeman",              # 3
        "Policewoman",            # 4
        "イベント用軍用犬",       # 5
        "イベント用軍用犬",       # 6
        "イベント用軍用犬",       # 7
        "State Guard Soldier",    # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "State Guard Soldier",    # 11
        "State Guard Soldier",    # 12
        "State Guard Soldier",    # 13
        "車",                     # 14
        "SE制御",                 # 15
        "Knox Woodland Road",     # 16
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch30600.itc",                   # 02
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

    DeclNpc(17000,   4294957296, 4294962296, 270,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294951296, 4294957296, 29500,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(17549,   4294957296, 4294952517, 225,  389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294960126, 4294957296, 140,     270,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  -13.0,                 11.0,                  -11.0,                 324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.0833333730697632,    -3.6666667461395264,   2.200000047683716,     1.0])
    DeclEvent(0x0040, 0, 13,  18.5,                  -8.0,                  -11.0,                 36.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5416667461395264,   0.6666666865348816,    2.200000047683716,     1.0])
    DeclEvent(0x0000, 0, 27,  12.0,                  -18.600000381469727,   -11.0,                 441.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.8571429252624512,   6.200000286102295,     2.200000047683716,     1.0])

    DeclActor(18500,   4294957296, 4294959296, 3200,    18500,   4294959296, 4294959296, 0x007C, 0,  3,  0x0000)
    DeclActor(4294956816, 4294957296, 3490,    1200,    4294956816, 4294959296, 3490,    0x007C, 0,  9,  0x0000)
    DeclActor(4294956296, 4294957296, 4750,    1200,    4294956296, 4294959296, 4750,    0x007C, 0,  9,  0x0000)
    DeclActor(32000,   4294957296, 4294951296, 1500,    32000,   4294959296, 4294951296, 0x007C, 0,  10, 0x0000)
    DeclActor(24920,   4294966986, 4294897906, 1500,    24920,   1510,    4294897906, 0x007C, 0,  28, 0x0000)

    PlaceName(90.0, 0.0, -80.0, 0x0000, 0x0000, "Knox Woodland Road")

    ChipFrameInfo(1292, 0)                                       # 0

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_922",          # 03, 3
        "Function_4_FA9",          # 04, 4
        "Function_5_103D",         # 05, 5
        "Function_6_22DE",         # 06, 6
        "Function_7_25D3",         # 07, 7
        "Function_8_265B",         # 08, 8
        "Function_9_2702",         # 09, 9
        "Function_10_2A3B",        # 0A, 10
        "Function_11_2B00",        # 0B, 11
        "Function_12_2EEB",        # 0C, 12
        "Function_13_3331",        # 0D, 13
        "Function_14_3FD2",        # 0E, 14
        "Function_15_40E0",        # 0F, 15
        "Function_16_41A7",        # 10, 16
        "Function_17_4EA8",        # 11, 17
        "Function_18_4ED8",        # 12, 18
        "Function_19_4F08",        # 13, 19
        "Function_20_4F24",        # 14, 20
        "Function_21_4F3E",        # 15, 21
        "Function_22_4F77",        # 16, 22
        "Function_23_4F9C",        # 17, 23
        "Function_24_4FC5",        # 18, 24
        "Function_25_4FE1",        # 19, 25
        "Function_26_5003",        # 1A, 26
        "Function_27_559D",        # 1B, 27
        "Function_28_5611",        # 1C, 28
    ))


    def Function_0_50C(): pass

    label("Function_0_50C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_544"),
        (1, "loc_550"),
        (2, "loc_55C"),
        (3, "loc_568"),
        (4, "loc_574"),
        (5, "loc_580"),
        (6, "loc_58C"),
        (SWITCH_DEFAULT, "loc_598"),
    )


    label("loc_544")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_550")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_55C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_568")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_574")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_580")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_58C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_598")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_5BB")

    Return()

    # Function_0_50C end

    def Function_1_5BC(): pass

    label("Function_1_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5EC")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC")
    ClearChrFlags(0x8, 0x80)

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_600")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_60F")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_60F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 26)

    label("loc_60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_63B")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63B")
    Event(0, 16)

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    SetChrPos(0x0, -10410, -10000, 2530, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 4)

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6B6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6")
    SetChrPos(0x0, -11000, -10000, 4750, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_6B6")

    Return()

    # Function_1_5BC end

    def Function_2_6B7(): pass

    label("Function_2_6B7")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70C")
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70C")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722")
    OP_66(0x0, 0x1)

    label("loc_722")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_744")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76A")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_779")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FD")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_814")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_814")

    label("loc_814")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_837")
    SetMapObjFrame(0xFF, "t6000:layer21", 0x0, 0x1)

    label("loc_837")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 32000, -10000, -16000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_897")
    OP_66(0x3, 0x1)

    label("loc_897")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_921")
    OP_65(0x1, 0x1)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x5, 0x15)
    SetChrPos(0x15, 18500, -10000, -8000, 270)
    OP_D5(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x2)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA0)

    label("loc_921")

    Return()

    # Function_2_6B7 end

    def Function_3_922(): pass

    label("Function_3_922")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C70")
    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    SetScenarioFlags(0x31, 2)

    label("loc_965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_9A5")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99A")
    Sound(2499, 255, 100, 0)
    Jump("loc_9A0")

    label("loc_99A")

    Sound(3537, 255, 100, 0)

    label("loc_9A0")

    Jump("loc_9AB")

    label("loc_9A5")

    Sound(3344, 255, 100, 0)

    label("loc_9AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_A1E")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9FE"),
        (SWITCH_DEFAULT, "loc_A0F"),
    )


    label("loc_9FE")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_A19")

    label("loc_A0F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A19")

    Jump("loc_C59")

    label("loc_A1E")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A50")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_A50")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A82"),
        (1, "loc_B86"),
        (2, "loc_C17"),
        (SWITCH_DEFAULT, "loc_C4F"),
    )


    label("loc_A82")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB3")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_AC3")

    label("loc_AB3")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_AC3")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B19")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B19")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C")
    Sound(461, 0, 100, 0)

    label("loc_B3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5C")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_B6C")

    label("loc_B5C")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_B6C")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_9AB")

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_BF8")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_BBB")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_BD3")

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BCE")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_BD3")

    label("loc_BCE")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_BD3")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C12")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C08")
    OP_AF(0xFB)
    Jump("loc_C12")

    label("loc_C08")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C12")

    Jump("loc_C59")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4A")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C40")
    OP_AF(0xFB)
    Jump("loc_C4A")

    label("loc_C40")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4A")

    Jump("loc_C59")

    label("loc_C4F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C59")

    Jump("loc_9AB")

    label("loc_C5E")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Jump("loc_FA8")

    label("loc_C70")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA2")
    SetScenarioFlags(0x31, 2)

    label("loc_CA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD7")
    Sound(2499, 255, 100, 0)
    Jump("loc_CDD")

    label("loc_CD7")

    Sound(3537, 255, 100, 0)

    label("loc_CDD")

    Jump("loc_CE8")

    label("loc_CE2")

    Sound(3344, 255, 100, 0)

    label("loc_CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D5B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D3B"),
        (SWITCH_DEFAULT, "loc_D4C"),
    )


    label("loc_D3B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D56")

    label("loc_D4C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D56")

    Jump("loc_F96")

    label("loc_D5B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D8D")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_D8D")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DBF"),
        (1, "loc_EC3"),
        (2, "loc_F54"),
        (SWITCH_DEFAULT, "loc_F8C"),
    )


    label("loc_DBF")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_DF0")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_E00")

    label("loc_DF0")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_E00")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E56")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E79")
    Sound(461, 0, 100, 0)

    label("loc_E79")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_E99")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_EA9")

    label("loc_E99")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_EA9")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_CE8")

    label("loc_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F35")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_EF8")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F10")

    label("loc_EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F0B")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F10")

    label("loc_F0B")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F10")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F4F")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F45")
    OP_AF(0xFB)
    Jump("loc_F4F")

    label("loc_F45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4F")

    Jump("loc_F96")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F87")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F7D")
    OP_AF(0xFB)
    Jump("loc_F87")

    label("loc_F7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F87")

    Jump("loc_F96")

    label("loc_F8C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F96")

    Jump("loc_CE8")

    label("loc_F9B")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)

    label("loc_FA8")

    Return()

    # Function_3_922 end

    def Function_4_FA9(): pass

    label("Function_4_FA9")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1004")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FF9")
    Sound(2502, 255, 100, 0)
    Jump("loc_FFF")

    label("loc_FF9")

    Sound(2503, 255, 100, 0)

    label("loc_FFF")

    Jump("loc_1028")

    label("loc_1004")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1022")
    Sound(3347, 255, 100, 0)
    Jump("loc_1028")

    label("loc_1022")

    Sound(3348, 255, 100, 0)

    label("loc_1028")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_FA9 end

    def Function_5_103D(): pass

    label("Function_5_103D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DD")

    ChrTalk(
        0xFE,
        (
            "Even the prison security returned to our\x01",
            "jurisdiction from the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can say it was a\x01",
            "little too severe situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe Empire and Republic\x01",
            "kept invading, so...\x01",
            "Indeed, it could be so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FMaybe they intensified the lookout\x01",
            "after I was held in custody.\x02\x03",
            "#00003FIt appears that Mr. Dieter\x01",
            "was vigilant about our Support\x01",
            "Section to get united...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B3")

    label("loc_11DD")


    ChrTalk(
        0xFE,
        (
            "Even the prison security returned to our\x01",
            "jurisdiction from the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By assigning the appropriate personnel to the\x01",
            "appropriate places, it's possible to guard\x01",
            "effectively like we were doing before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B3")

    Jump("loc_22DA")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1425")

    ChrTalk(
        0x9,
        (
            "Hearing the information about\x01",
            "the raid, it seems that the prison\x01",
            "inmates can't conceal their unrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, we took care of checking the safety of\x01",
            "the inmates' families, but, as expected, there\x01",
            "were also some people who were not unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Even if the other party is a criminal,\x01",
            "telling him that it makes his heart ache.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C1")

    label("loc_1425")


    ChrTalk(
        0x9,
        (
            "A great number among them\x01",
            "has left a family in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...When you can't tell them they're safe,\x01",
            "although they're criminals, your heart aches.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C1")

    Jump("loc_22DA")

    label("loc_14C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1574")

    ChrTalk(
        0x9,
        (
            "This derail incident...\x01",
            "I wonder if it's\x01",
            "someone's work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If that's the case, it's a serious crime.\x01",
            "After all, it's hurt so many\x01",
            "innocent commoners...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DA")

    label("loc_1574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1682")

    ChrTalk(
        0x9,
        (
            "Since some time it's like you can\x01",
            "hear screams from deep down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the inmates of the\x01",
            "prison are making noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There could be some scoundrels who\x01",
            "think to take advantage of this situation.\x01",
            "We need to pay close attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174D")

    label("loc_1682")


    ChrTalk(
        0x9,
        (
            "It seems the inmates of the\x01",
            "prison are making noise too\x01",
            "in this unusual situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There could be some scoundrels who\x01",
            "think to take advantage of this situation.\x01",
            "We need to pay close attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174D")

    Jump("loc_22DA")

    label("loc_1752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189A")

    ChrTalk(
        0x9,
        (
            "Due to being so close, there're many\x01",
            "jailers who get worn out by the pressure\x01",
            "of having to keep a look on criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Frankly speaking, aside from holidays,\x01",
            "I too have got no time to relax myself...\x01",
            "Still, someone must do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A strong force of will is needed.\x01",
            "...To work here, I mean.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1954")

    label("loc_189A")


    ChrTalk(
        0x9,
        (
            "Due to being so close, there're many\x01",
            "jailers who get worn out by the pressure\x01",
            "of having to keep a look on criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A strong force of will is needed.\x01",
            "...To work here, I mean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1954")

    Jump("loc_22DA")

    label("loc_1959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A61")

    ChrTalk(
        0x9,
        (
            "If we get independent, the system \x01",
            "will probably be revised to manage\x01",
            "Crossbell crime way more firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even the foreigner criminals who're an issue\x01",
            "would certainly decrease in numbers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...IF we get independent, that is.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AF5")

    label("loc_1A61")


    ChrTalk(
        0x9,
        (
            "If we get independent, the system \x01",
            "will probably be revised to manage\x01",
            "Crossbell crime way more firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...IF we get independent, that is.\x02",
    )

    CloseMessageWindow()

    label("loc_1AF5")

    Jump("loc_22DA")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9F")

    ChrTalk(
        0x9,
        (
            "In case a foreigner commits a crime,\x01",
            "due to the autonomous state law, he\x01",
            "can't be detained for a long period of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's become one of the main causes\x01",
            "so many criminals from Empire and\x01",
            "Republic origin get inside Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the legal reform by the new mayor being\x01",
            "underway, things have improved a little, but...\x01",
            "It's still got a long way to go to be considered complete.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DC8")

    label("loc_1C9F")


    ChrTalk(
        0x9,
        (
            "In case a foreigner commits a crime inside\x01",
            "Crossbell, due to the autonomous state law,\x01",
            "he can't be detained for a long period of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the legal reform by the new mayor being\x01",
            "underway, things have improved a little, but...\x01",
            "It's still got a long way to go to be considered complete.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC8")

    Jump("loc_22DA")

    label("loc_1DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F07")

    ChrTalk(
        0x9,
        (
            "The prison security was quite\x01",
            "rethought after the Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although attacked by the manipulated\x01",
            "CGF, ending up forgiving the prisoners'\x01",
            "jailbreak was an unbecoming event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So that such a thing won't happen next time,\x01",
            "we intend to work out a way more strict security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FB0")

    label("loc_1F07")


    ChrTalk(
        0x9,
        (
            "The prison security was quite\x01",
            "rethought after the Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So that a jailbreak won't happen next time,\x01",
            "we intend to work out a way more strict security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB0")

    Jump("loc_22DA")

    label("loc_1FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2158")

    ChrTalk(
        0x9,
        (
            "Those who're held in this prison are persons\x01",
            "suspected of crimes by the autonomous \x01",
            "state law, regardless of importance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Recently we have in custody a part of the\x01",
            "congressmen and mafia involved in the Cult\x01",
            "incident and even that former mayor secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, as soon as the trials \x01",
            "arrangements are complete, they'll receive\x01",
            "judgement based on the autonomous state law.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_225E")

    label("loc_2158")


    ChrTalk(
        0x9,
        (
            "Recently we have in custody a part of the diet\x01",
            "members and mafia involved in the Cult\x01",
            "incident and that former mayor secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, as soon as the trials \x01",
            "arrangements are complete, they'll receive\x01",
            "judgement based on the autonomous state law.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225E")

    Jump("loc_22DA")

    label("loc_2263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_22DA")

    ChrTalk(
        0x9,
        "...This place is a prison.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you don't have any business,\x01",
            "could you refrain to get close too much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DA")

    TalkEnd(0xFE)
    Return()

    # Function_5_103D end

    def Function_6_22DE(): pass

    label("Function_6_22DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2563")

    ChrTalk(
        0x8,
        (
            "#01005F...Hm? What's wrong?\x01",
            "Aren't you getting in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well...\x01",
            "Being able to ride in this\x01",
            "is somehow, like, awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's our personal car, but...\x01",
            "Considering all that's happened until now,\x01",
            "after all, we're hesitating.\x02\x03",
            "#00104FBut it's true that we desired one and\x01",
            "were envying the men of Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FEh eh, it's not that I don't\x01",
            "understand how you feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FCome on, everyone!\x01",
            "Let's get inside quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, she seems in high spirits,\x01",
            "so wouldn't it be bad to keep\x01",
            "her in suspense?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FT-That's also true.\x02\x03",
            "#00000FAlright, then, let's\x01",
            "try riding in it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25CF")

    label("loc_2563")


    ChrTalk(
        0x8,
        (
            "#01002FCome now, get in at once.\x02\x03",
            "#01004FWith this one, Crossbell City\x01",
            "will just be around the corner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CF")

    TalkEnd(0xFE)
    Return()

    # Function_6_22DE end

    def Function_7_25D3(): pass

    label("Function_7_25D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2657")

    ChrTalk(
        0xFE,
        (
            "At present, nothing out of the ordinary\x01",
            "in the Police Academy environs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will continue to be on the lookout!\x02",
    )

    CloseMessageWindow()

    label("loc_2657")

    TalkEnd(0xFE)
    Return()

    # Function_7_25D3 end

    def Function_8_265B(): pass

    label("Function_8_265B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26FE")

    ChrTalk(
        0xFE,
        (
            "After the CGF retreated and the place\x01",
            "became short-handed, we came running\x01",
            "here with Section Chief Joe Ridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please leave this place to us.\x02",
    )

    CloseMessageWindow()

    label("loc_26FE")

    TalkEnd(0xFE)
    Return()

    # Function_8_265B end

    def Function_9_2702(): pass

    label("Function_9_2702")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2734")
    SetScenarioFlags(0x31, 2)

    label("loc_2734")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_277A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2774")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2769")
    Sound(2499, 255, 100, 0)
    Jump("loc_276F")

    label("loc_2769")

    Sound(3537, 255, 100, 0)

    label("loc_276F")

    Jump("loc_277A")

    label("loc_2774")

    Sound(3344, 255, 100, 0)

    label("loc_277A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_27ED")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27CD"),
        (SWITCH_DEFAULT, "loc_27DE"),
    )


    label("loc_27CD")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_27E8")

    label("loc_27DE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27E8")

    Jump("loc_2A28")

    label("loc_27ED")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_281F")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_281F")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2851"),
        (1, "loc_2955"),
        (2, "loc_29E6"),
        (SWITCH_DEFAULT, "loc_2A1E"),
    )


    label("loc_2851")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2882")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2892")

    label("loc_2882")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2892")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28E8")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290B")
    Sound(461, 0, 100, 0)

    label("loc_290B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_292B")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_293B")

    label("loc_292B")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_293B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_277A")

    label("loc_2955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_29C7")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_298A")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_29A2")

    label("loc_298A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_299D")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_29A2")

    label("loc_299D")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_29A2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29E1")

    label("loc_29C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_29D7")
    OP_AF(0xFB)
    Jump("loc_29E1")

    label("loc_29D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29E1")

    Jump("loc_2A28")

    label("loc_29E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A19")

    label("loc_29FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2A0F")
    OP_AF(0xFB)
    Jump("loc_2A19")

    label("loc_2A0F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A19")

    Jump("loc_2A28")

    label("loc_2A1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A28")

    Jump("loc_277A")

    label("loc_2A2D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_2702 end

    def Function_10_2A3B(): pass

    label("Function_10_2A3B")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(33030, -9000, -16129, 1500)
    MoveCamera(54, 38, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(10340, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFB")
    OP_E2(0x2)
    MiniGame(0x6, 0x15, 0x8B10, 0xFFFFD8F0, 0xFFFFC1BC, 0x10E, 0x7D00, 0xFFFFD8F0, 0xFFFFC180)

    label("loc_2AFB")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_2A3B end

    def Function_11_2B00(): pass

    label("Function_11_2B00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13330, 750, -64160, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_90(0x101, 12000, 0, -63650, 0)
    OP_90(0x102, 11000, 0, -65349, 0)
    OP_90(0x109, 13000, 0, -64650, 0)
    OP_90(0x105, 12000, 0, -66350, 0)
    FadeToBright(1000, 0)

    def lambda_2B8C():
        OP_95(0xFE, 12000, -10000, -21650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B8C)

    def lambda_2BA6():
        OP_95(0xFE, 11000, -10000, -23350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BA6)

    def lambda_2BC0():
        OP_95(0xFE, 13000, -10000, -22650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2BC0)

    def lambda_2BDA():
        OP_95(0xFE, 12000, -10000, -24350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BDA)
    OP_68(-8680, 750, -39570, 9000)
    SetCameraDistance(33500, 9000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(28490, 750, -27110, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(26430, 0)
    OP_68(-30330, 750, 3140, 18000)
    Sleep(16000)
    OP_0D()
    Fade(1000)
    OP_68(13270, -4850, 4770, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(37650, 0)
    SetCameraDistance(73520, 9000)
    Sleep(4000)
    PlaceName2(340, 200, "c_plac37", 0x0, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(11860, -9000, -22290, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, 12000, -10000, -21650, 0)
    SetChrPos(0x102, 11000, -10000, -23350, 0)
    SetChrPos(0x109, 13000, -10000, -22650, 0)
    SetChrPos(0x105, 12000, -10000, -24350, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002F#5PWell then...\x01",
            "This is the Police Academy building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F#12P*sigh*, we've finally arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PAs might be expected from being inside\x01",
            "a forest, it is located in a quiet place.\x02\x03",
            "#00100FI wonder where's the Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PIn any case, the Police Academy\x01",
            "reception is at the front entrance.\x02\x03",
            "#10100FLet's try getting inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, let's do that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12000, -10000, -22000, 0)
    SetScenarioFlags(0x127, 3)
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0xA1, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_11_2B00 end

    def Function_12_2EEB(): pass

    label("Function_12_2EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D4")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-15200, -8350, 11350, 0)
    MoveCamera(24, 9, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x102, -12700, -10000, 11550, 0)
    SetChrPos(0x101, -11800, -10000, 10000, 0)
    SetChrPos(0x109, -13500, -10000, 8300, 0)
    SetChrPos(0x105, -12400, -10000, 7950, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#11POh, what's that building?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PAh...it's the prison.\x02\x03",
            "#00001FIt was established in the premises\x01",
            "near the Police Academy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00101F#5PThen, is Mr.\x01",
            "Ernest there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYes, Mr. Dudley and the others\x01",
            "should've just imprisoned him.\x02\x03",
            "#00000FIf you apply for a visit,\x01",
            "you can meet him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PAh... \x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00106F#5P...No, I won't.\x02\x03",
            "#00108FHe went through a terrible experience.\x01",
            "Now I think he needs the time to\x01",
            "reconsider himself...\x02\x03",
            "#00102FI'll find an opportunity in the future\x01",
            "and try visiting him with grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PI see...\x01",
            "That could be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12P(It seems many things happened.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6P(Yes...\x01",
            "I don't know the details, though.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -11250, -10000, 7200, 180)
    SetScenarioFlags(0x127, 4)
    EventEnd(0x5)
    Jump("loc_3330")

    label("loc_32D4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe prison is further ahead.\x01",
            "Let's not get close for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -12250, -10000, 8310, 180)
    EventEnd(0x4)

    label("loc_3330")

    Return()

    # Function_12_2EEB end

    def Function_13_3331(): pass

    label("Function_13_3331")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(16000, -8900, -6550, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14750, 0)
    SetChrPos(0x101, 14200, -10000, -7000, 90)
    SetChrPos(0x102, 13550, -10000, -5950, 90)
    SetChrPos(0x109, 14750, -10000, -5750, 90)
    SetChrPos(0x105, 14550, -10000, -4300, 135)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 17000, -10000, -5000, 225)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005F#6PT-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PThe orbal car that was supplied\x01",
            "to the Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(19250, -8950, -8000, 0)
    MoveCamera(145, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13650, 0)
    OP_68(17500, -8950, -8000, 7500)
    MoveCamera(56, 10, 0, 7500)
    SetCameraDistance(8000, 6500)
    OP_6F(0x10)
    SetCameraDistance(9500, 4500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(16000, -8900, -6550, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10302F#5PEeh, that's not a bad design.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PT-This is...\x02\x03",
            "A design line that doesn't look neither\x01",
            "like a Verne nor a Reinford...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01009F#11PEh eh, correct.\x02\x03",
            "#01004FThis it the XD-78 model.\x02\x03",
            "#01002FMade in Liberl──\x01",
            "It's the new model of the Zeiss Central Factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10107F#6PEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PWere the ZCF developing\x01",
            "orbal cars!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#5PIs that such a shocking thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PYes, since Liberl is also\x01",
            "a steep nation, orbal cars\x01",
            "are not spread.\x02\x03",
            "#00100FInstead, ZCF is known\x01",
            "as the world top class\x01",
            "airship manufacturer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PT-To think that ZCF had\x01",
            "developed an orbal car!!\x02\x03",
            "#10109FWhat're the specs!?\x01",
            "What's the max speed!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#11PThere, there, calm down.\x02\x03",
            "#01004FIt appears it boards a small size version \x01",
            "of a new engine for airship use.\x02\x03",
            "#01002FAs for its maximum speed,\x01",
            "it seems it's 1500 selge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PC-Crazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIts speed is more than the railroad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PHowever, how could you \x01",
            "obtain such a vehicle?\x02\x03",
            "It seems a new model not even\x01",
            "officially on the market yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PYeah, the truth is that this thing\x01",
            "shouldn't have been assigned to you.\x02\x03",
            "#01002FThe new mayor, Dieter,\x01",
            "granted it to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        "#00011F#6PMayor Dieter did!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PW-Well, it makes sense, since\x01",
            ""uncle" is also acquainted with \x01",
            "the ZCF, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#6P*haah*, as expected from the\x01",
            "talented IBC President!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHu hu, he readied this much for us, but\x01",
            "conversely we'll have to be cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PEh eh, well, about that, you'll\x01",
            "just repay him with your work.\x02\x03",
            "#01000FIf you think it's too much of a responsibility,\x01",
            "you could even refuse it, you know?\x02\x03",
            "In that case, we'll give you one of the generic\x01",
            "Verne Corporation car employed in the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo... We'll use it\x01",
            "with gratitude.\x02\x03",
            "#00000FCan it run yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F#11PMaintenance and test runs are done.\x02\x03",
            "Here, these are the keys.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x35C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x35C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#6P...Ha ha...\x01",
            "Somehow, this is a little moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PRight... We desired one and were\x01",
            "envying the men of Section One.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, so, are we going to\x01",
            "take it for a spin immediately?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah, since we have this occasion,\x01",
            "let's go back to Crossbell City.\x02\x03",
            "Noｱl, can we entrust you with the driving?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    ChrTalk(
        0x109,
        "#10109F#5PYes, please leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PHmph, then I guess I'll take\x01",
            "advantage of this ride too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17000, -10000, -5000, 270)
    SetChrPos(0x0, 14500, -10000, -8000, 90)
    SetScenarioFlags(0x127, 6)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x0, 0x1)
    OP_29(0xA1, 0x1, 0x9)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1D, (scpexpr(EXPR_PUSH_LONG, 0x21260000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_13_3331 end

    def Function_14_3FD2(): pass

    label("Function_14_3FD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(468)
    OP_68(17550, -9000, -8000, 0)
    MoveCamera(60, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(8650, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x8, 0x8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(12000, -9000, -12550, 6000)
    MoveCamera(48, 30, 0, 6000)
    OP_6E(650, 6000)
    SetCameraDistance(17350, 6000)
    Sleep(500)
    Sound(494, 0, 60, 0)
    Sound(468, 2, 80, 0)
    BeginChrThread(0x15, 3, 0, 15)
    OP_6F(0x79)
    Fade(500)
    OP_F0(0x0, 0x1)
    OP_68(13550, -9000, -13850, 0)
    MoveCamera(19, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16880, 0)
    OP_68(13550, -9000, -20850, 4000)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x15, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("r4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3FD2 end

    def Function_15_40E0(): pass

    label("Function_15_40E0")


    def lambda_40E5():
        OP_95(0xFE, 16500, -10000, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40E5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    WaitChrThread(0xFE, 1)

    def lambda_4128():
        OP_9E(0xFE, 0x4074, 0xFFFFCF2C, 0xFFFEA070, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4128)
    Sleep(2600)
    StopSound(468, 1000, 80)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(300)
    Sound(492, 0, 100, 0)
    Sleep(700)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_416B():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_416B)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 80, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_40E0 end

    def Function_16_41A7(): pass

    label("Function_16_41A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch04150.itc", 0x24)
    LoadChrToIndex("chr/ch04154.itc", 0x25)
    LoadChrToIndex("apl/ch51612.itc", 0x26)
    LoadEffect(0x0, "event\\ev306_00.eff")
    SoundLoad(825)
    SoundLoad(907)
    SetChrPos(0x101, -16000, -10050, 36750, 180)
    SetChrPos(0x10B, -16000, -10050, 38750, 180)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 11500, -9500, 10500, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12500, -9500, 10500, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 11500, -9500, 10500, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12500, -9500, 10500, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -16000, -10050, 30750, 180)
    SetChrFlags(0x13, 0x8)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -16000, -10050, 32750, 180)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 11500, -9500, 10500, 180)
    SetChrFlags(0xC, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 0, 0, 24)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 12500, -9500, 10500, 180)
    SetChrFlags(0xD, 0x20)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 24)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -16000, -10050, 35750, 180)
    SetChrFlags(0xE, 0x20)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 24)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x9, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x19)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x14)
    OP_68(-16000, -3950, 30750, 0)
    MoveCamera(30, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(35000, 0)
    FadeToBright(1000, 0)
    OP_68(-16000, -8750, 30750, 3000)
    MoveCamera(30, 20, 0, 3000)
    SetCameraDistance(25000, 3000)
    Sleep(1000)

    def lambda_4480():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4480)
    Sleep(100)

    def lambda_4498():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4498)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10B, 1)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(3400, -7600, -7700, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(8000, -8000, -11000, 5000)
    MoveCamera(36, 27, 0, 5000)
    SetCameraDistance(30000, 5000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x10B, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0x1388)
    Fade(1000)
    OP_68(12700, -4450, -51000, 0)
    MoveCamera(36, 36, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 13550, -7000, -43950, 180)
    SetChrPos(0x10B, 12300, -7300, -42650, 180)
    MoveCamera(36, 30, 0, 3500)
    SetCameraDistance(21500, 3500)

    def lambda_4598():
        OP_9B(0x0, 0xFE, 0x5, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4598)
    Sleep(100)

    def lambda_45B0():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_45B0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10B, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00005F#11PGarcｵa...?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    Fade(500)
    OP_68(12300, -3350, -53000, 0)
    MoveCamera(135, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 1000)
    SetChrPos(0x101, 12100, -3920, -54150, 0)
    SetChrPos(0x10B, 12500, -4650, -51750, 180)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(15000, 20000)
    OP_93(0x10B, 0x0, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x26)
    SetChrSubChip(0x10B, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10B,
        (
            "#11103F#11P──Our collusion ends here.\x02\x03",
            "#11100FFrom now on, you'll\x01",
            "go by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PEven though these're the circumstances,\x01",
            "I'm still Revache's leader of the young men.\x02\x03",
            "#11101FOf course my underlings, but even that President...\x01",
            "I can't run away and leave 'em alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PW-Wait!\x02\x03",
            "In that case, why did you\x01",
            "come with me so far...?\x02\x03",
            "#00007FAlso, no matter if it's you, you\x01",
            "won't succeed alone, right!?\x02\x03",
            "Then, I'll──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10B,
        "#11107F#5S#11PDon't get the wrong idea, kid!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10B,
        (
            "#11103F#11PTo ascertain the truth...\x01",
            "You said that..\x02\x03",
            "To free your arrested comrades\x01",
            "and get back that brat, also.\x02\x03",
            "#11100F...Do you have the time to\x01",
            "dawdle in such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──Thank you, Garcｵa.\x02\x03",
            "#00008FFrom my standpoint I can't\x01",
            "welcome your jailbreak, but...\x02\x03",
            "#00001FPlease stay safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PHah!\x01",
            "A needless worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(13200, -3350, -55250, 0)
    MoveCamera(30, 35, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    OP_68(12500, -3650, -51750, 4000)
    MoveCamera(30, 30, 0, 4000)
    SetCameraDistance(18500, 4000)
    SetChrSubChip(0x10B, 0x0)

    def lambda_4ABA():
        OP_9B(0x0, 0xFE, 0x5, 0x2AF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ABA)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x10B, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10B)

    ChrTalk(
        0x10B,
        (
            "#11104F#11PLloyd Bannings...\x01",
            "...That bastard's younger brother, eh?\x02\x03",
            "#11100FHe got quite the\x01",
            "nice expression, eh?\x02",
        )
    )

    CloseMessageWindow()
    Sound(907, 2, 70, 0)
    Sleep(800)
    Fade(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)
    OP_68(500, -4500, 6000, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(40000, 0)
    OP_68(500, -4500, -1000, 5000)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0xE, 0x8)
    BeginChrThread(0x13, 3, 0, 23)
    BeginChrThread(0x14, 3, 0, 23)
    BeginChrThread(0xE, 3, 0, 23)
    BeginChrThread(0xF, 3, 0, 22)
    BeginChrThread(0x10, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0xD, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0xC, 3, 0, 22)
    OP_0D()
    BeginChrThread(0x16, 1, 0, 25)
    SetMessageWindowPos(280, 120, -1, -1)

    AnonymousTalk(
        0xF,
        "#2SThere he is...!\x05\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(90, 50, -1, -1)

    AnonymousTalk(
        0x13,
        "#2SDon't let him get away!\x05\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Sleep(1000)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Fade(1000)
    OP_68(11910, -3250, -50960, 0)
    MoveCamera(135, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14200, 0)
    SetChrSubChip(0x10B, 0x1)
    SetCameraDistance(13700, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(150)
    Fade(250)
    Sound(908, 0, 100, 0)
    Sound(2854, 255, 100, 0)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x24)
    SetChrSubChip(0x10B, 0x0)
    BeginChrThread(0x10B, 0, 0, 19)
    OP_0D()

    ChrTalk(
        0x10B,
        "#11102F#11PEh eh, this advantage position is enough...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    PlayEffect(0x0, 0x1, 0x10B, 0x1, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(12000, 500)
    EndChrThread(0x10B, 0x0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    Sound(881, 0, 40, 0)
    Sound(833, 0, 60, 0)
    Sound(825, 2, 70, 0)
    BeginChrThread(0x10B, 0, 0, 20)
    BeginChrThread(0x10B, 3, 0, 21)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x10B,
        (
            "#11107F#11P#4SI'll make you savor the\x01",
            ""Killing Bear" iron fists aplenty!!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 1000, 70)
    StopSound(907, 1000, 60)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(11750, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x10B, 0x3)
    EndChrThread(0x10B, 0x0)
    RemoveParty(0xA, 0xFF)
    OP_24(0x38B)
    SetScenarioFlags(0x22, 1)
    NewScene("r4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_41A7 end

    def Function_17_4EA8(): pass

    label("Function_17_4EA8")

    SetChrPos(0xFE, 2550, -10000, -1700, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_17_4EA8 end

    def Function_18_4ED8(): pass

    label("Function_18_4ED8")

    SetChrPos(0xFE, 700, -10000, -1250, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_18_4ED8 end

    def Function_19_4F08(): pass

    label("Function_19_4F08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F23")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_4F08")

    label("loc_4F23")

    Return()

    # Function_19_4F08 end

    def Function_20_4F24(): pass

    label("Function_20_4F24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F3D")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_20_4F24")

    label("loc_4F3D")

    Return()

    # Function_20_4F24 end

    def Function_21_4F3E(): pass

    label("Function_21_4F3E")

    OP_82(0x64, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_4F52")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F76")
    OP_82(0x0, 0x1E, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("loc_4F52")

    label("loc_4F76")

    Return()

    # Function_21_4F3E end

    def Function_22_4F77(): pass

    label("Function_22_4F77")


    def lambda_4F7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F7C)
    OP_9B(0x0, 0xFE, 0x0, 0x7530, 0xFA0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_4F77 end

    def Function_23_4F9C(): pass

    label("Function_23_4F9C")

    OP_95(0xFE, -16000, -10050, 15000, 5000, 0x1)
    OP_95(0xFE, 11500, -10000, -15650, 5000, 0x0)
    Return()

    # Function_23_4F9C end

    def Function_24_4FC5(): pass

    label("Function_24_4FC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FE0")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_24_4FC5")

    label("loc_4FE0")

    Return()

    # Function_24_4FC5 end

    def Function_25_4FE1(): pass

    label("Function_25_4FE1")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Sleep(1400)
    Sound(909, 0, 20, 0)
    Sleep(850)
    Sound(910, 0, 20, 0)
    Return()

    # Function_25_4FE1 end

    def Function_26_5003(): pass

    label("Function_26_5003")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10760, -9000, 21160, 0)
    MoveCamera(44, 34, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15080, 0)
    SetChrPos(0x101, -9700, -10000, 20860, 270)
    SetChrPos(0x102, -10100, -10000, 21870, 225)
    SetChrPos(0x103, -10320, -10000, 19680, 315)
    SetChrPos(0x104, -12120, -10000, 20670, 90)
    SetChrPos(0xF4, -11320, -10000, 22270, 135)
    SetChrPos(0xF5, -11520, -10000, 19680, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh boy, he seemed to be doin'\x01",
            "fine more than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FRight. At that rate, he'll be\x01",
            "in full health soon enough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51BA")

    ChrTalk(
        0x105,
        (
            "#6P#10400FEven so, it was unexpected,\x01",
            "getting encouraged by\x01",
            "a person like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5284")

    label("loc_51BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_521D")

    ChrTalk(
        0x106,
        (
            "#6P#10703FStill, how unexpected\x01",
            "to be encouraged by\x01",
            "a person like him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5284")

    label("loc_521D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5284")

    ChrTalk(
        0x109,
        (
            "#6P#10100FEven so, it was unexpected,\x01",
            "getting encouraged by\x01",
            "a former mafia man...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5284")


    ChrTalk(
        0x101,
        (
            "#00000FYeah...maybe he went through many\x01",
            "events and he changed too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    ChrTalk(
        0x101,
        "#00005FW-What is it, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FNo, I was only thinking why you were saying \x01",
            "it like it were someone else's business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI think that maybe it was your influence...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00005F...Huh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh man, that's why you're\x01",
            "a natural gigolo, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54DB")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F...Even what he said, that\x01",
            "you resemble your older\x01",
            "brother, seems true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_556D")

    label("loc_54DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5527")

    ChrTalk(
        0x109,
        (
            "#6P#10102FUh uh, Mr. Lloyd\x01",
            "is the same as always.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_556D")

    label("loc_5527")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_556D")

    ChrTalk(
        0x106,
        (
            "#6P#10702FAhaha...\x01",
            "Mr. Lloyd is always the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_556D")

    OP_5A()
    SetScenarioFlags(0x1BC, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -9700, -10000, 20860, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_26_5003 end

    def Function_27_559D(): pass

    label("Function_27_559D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOh, this way it the woodland road area.\x01",
            "The orbal car is in front of the garage.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11900, -10000, -15540, 0)
    EventEnd(0x4)
    Return()

    # Function_27_559D end

    def Function_28_5611(): pass

    label("Function_28_5611")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West - Crossbell Police Academy\x01",
            "North - Knox Woodlands Entrance\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_5611 end

    SaveToFile()

Try(main)
