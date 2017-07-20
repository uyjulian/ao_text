from ScenarioHelper import *

def main():
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
        "Sergey Manager",           # 1
        "Nursery Melvin",           # 2
        "Policeman",                   # 3
        "policewoman",                   # 4
        "Military dog for events",       # 5
        "Military dog for events",       # 6
        "Military dog for events",       # 7
        "Defense Forces soldier",             # 8
        "Defense Forces soldier",             # 9
        "Defense Forces soldier",             # 10
        "Defense Forces soldier",             # 11
        "Defense Forces soldier",             # 12
        "Defense Forces soldier",             # 13
        "car",                     # 14
        "SE control",                 # 15
        "Knox Forest Road",         # 16
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

    PlaceName(90.0, 0.0, -80.0, 0x0000, 0x0000, "Knox Forest Road")

    ChipFrameInfo(1292, 0)                                       # 0

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_922",          # 03, 3
        "Function_4_FBD",          # 04, 4
        "Function_5_1051",         # 05, 5
        "Function_6_1EE5",         # 06, 6
        "Function_7_2173",         # 07, 7
        "Function_8_21D0",         # 08, 8
        "Function_9_225A",         # 09, 9
        "Function_10_259D",        # 0A, 10
        "Function_11_2671",        # 0B, 11
        "Function_12_2A19",        # 0C, 12
        "Function_13_2E1D",        # 0D, 13
        "Function_14_39A2",        # 0E, 14
        "Function_15_3AB0",        # 0F, 15
        "Function_16_3B77",        # 10, 16
        "Function_17_4814",        # 11, 17
        "Function_18_4844",        # 12, 18
        "Function_19_4874",        # 13, 19
        "Function_20_4890",        # 14, 20
        "Function_21_48AA",        # 15, 21
        "Function_22_48E3",        # 16, 22
        "Function_23_4908",        # 17, 23
        "Function_24_4931",        # 18, 24
        "Function_25_494D",        # 19, 25
        "Function_26_496F",        # 1A, 26
        "Function_27_4EC2",        # 1B, 27
        "Function_28_4F1D",        # 1C, 28
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

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C7A")
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_A24")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A04"),
        (SWITCH_DEFAULT, "loc_A15"),
    )


    label("loc_A04")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_A1F")

    label("loc_A15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1F")

    Jump("loc_C63")

    label("loc_A24")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A58")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_A58")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A8C"),
        (1, "loc_B90"),
        (2, "loc_C21"),
        (SWITCH_DEFAULT, "loc_C59"),
    )


    label("loc_A8C")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABD")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_ACD")

    label("loc_ABD")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_ACD")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B23")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46")
    Sound(461, 0, 100, 0)

    label("loc_B46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B66")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_B76")

    label("loc_B66")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_B76")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_9AB")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_C02")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_BC5")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_BDD")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BD8")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_BDD")

    label("loc_BD8")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_BDD")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C1C")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C12")
    OP_AF(0xFB)
    Jump("loc_C1C")

    label("loc_C12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1C")

    Jump("loc_C63")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C54")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C4A")
    OP_AF(0xFB)
    Jump("loc_C54")

    label("loc_C4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C54")

    Jump("loc_C63")

    label("loc_C59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C63")

    Jump("loc_9AB")

    label("loc_C68")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Jump("loc_FBC")

    label("loc_C7A")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAC")
    SetScenarioFlags(0x31, 2)

    label("loc_CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE1")
    Sound(2499, 255, 100, 0)
    Jump("loc_CE7")

    label("loc_CE1")

    Sound(3537, 255, 100, 0)

    label("loc_CE7")

    Jump("loc_CF2")

    label("loc_CEC")

    Sound(3344, 255, 100, 0)

    label("loc_CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D6B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D4B"),
        (SWITCH_DEFAULT, "loc_D5C"),
    )


    label("loc_D4B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D66")

    label("loc_D5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D66")

    Jump("loc_FAA")

    label("loc_D6B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D9F")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_D9F")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DD3"),
        (1, "loc_ED7"),
        (2, "loc_F68"),
        (SWITCH_DEFAULT, "loc_FA0"),
    )


    label("loc_DD3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_E04")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_E14")

    label("loc_E04")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_E14")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8D")
    Sound(461, 0, 100, 0)

    label("loc_E8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_EAD")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_EBD")

    label("loc_EAD")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_EBD")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_CF2")

    label("loc_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F49")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F0C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F24")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F1F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F24")

    label("loc_F1F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F24")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F63")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F59")
    OP_AF(0xFB)
    Jump("loc_F63")

    label("loc_F59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F63")

    Jump("loc_FAA")

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F81")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F9B")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F91")
    OP_AF(0xFB)
    Jump("loc_F9B")

    label("loc_F91")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9B")

    Jump("loc_FAA")

    label("loc_FA0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAA")

    Jump("loc_CF2")

    label("loc_FAF")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)

    label("loc_FBC")

    Return()

    # Function_3_922 end

    def Function_4_FBD(): pass

    label("Function_4_FBD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1018")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100D")
    Sound(2502, 255, 100, 0)
    Jump("loc_1013")

    label("loc_100D")

    Sound(2503, 255, 100, 0)

    label("loc_1013")

    Jump("loc_103C")

    label("loc_1018")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1036")
    Sound(3347, 255, 100, 0)
    Jump("loc_103C")

    label("loc_1036")

    Sound(3348, 255, 100, 0)

    label("loc_103C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_FBD end

    def Function_5_1051(): pass

    label("Function_5_1051")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D3")

    ChrTalk(
        0xFE,
        (
            "Security of detention centers also from the Defense Army\x01",
            "We decided to return to our jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bit too strict\x01",
            "Because it was a good condition to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FEmpire and Republic\x01",
            "Although the invasion was continuing ……\x01",
            "Surely it may be so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FPerhaps because I was detained\x01",
            "I guess it was strengthening the guard.\x02\x03",
            "#00003FMr. Dieter,\x01",
            "We will unite our support department\x01",
            "It seems she was alarmed … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1272")

    label("loc_11D3")


    ChrTalk(
        0xFE,
        (
            "Security of detention centers also from the Defense Army\x01",
            "We decided to return to our jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Appropriate personnel in the right place\x01",
            "By being allocated, as before\x01",
            "Efficient security will be possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")

    Jump("loc_1EE1")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")

    ChrTalk(
        0x9,
        (
            "Listening to the report of the attack incident,\x01",
            "Detainment detainees also\x01",
            "It seems I can not hide upset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once, confirmation of the safety of inmates' families\x01",
            "Even though I take it here,\x01",
            "Some people were not alright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… To tell it,\x01",
            "My heart is painful as opponent is a criminal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F5")

    label("loc_1373")


    ChrTalk(
        0x9,
        (
            "Among them are crossbells\x01",
            "Many things that leave their families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… When that safety can not be told,\x01",
            "My heart hurts that he is a criminal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F5")

    Jump("loc_1EE1")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1496")

    ChrTalk(
        0x9,
        (
            "The derailment accident this time\x01",
            "Thing by someone's hand\x01",
            "Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If so, it is too much a felony.\x01",
            "Only for innocent people\x01",
            "Because it caused the damage ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_160E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(
        0x9,
        (
            "From the bottom of the previous land\x01",
            "A cry as you hear ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Inmates in detention centers also\x01",
            "It looks awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take this machine, think that\x01",
            "There may also be unreasonable persons.\x01",
            "I have to pay close attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1609")

    label("loc_156F")


    ChrTalk(
        0x9,
        (
            "Inmates in detention centers, too,\x01",
            "To this abnormal situation\x01",
            "It looks awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take this machine, think that\x01",
            "There may also be unreasonable persons.\x01",
            "I have to pay close attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1609")

    Jump("loc_1EE1")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_17A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")

    ChrTalk(
        0x9,
        (
            "The criminal at the nearest place\x01",
            "To the heavy pressure we have to look at,\x01",
            "There are also many jail guards that will collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To be honest, I also do not have a holiday\x01",
            "There is no time to relax … …\x01",
            "Still someone has to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It requires strong mental power.\x01",
            "…… It's over here to work here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179F")

    label("loc_170E")


    ChrTalk(
        0x9,
        (
            "The criminal at the nearest place\x01",
            "To the heavy pressure we have to look at,\x01",
            "There are also many jail guards that will collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It requires strong mental power.\x01",
            "…… It's over here to work here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179F")

    Jump("loc_1EE1")

    label("loc_17A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1884")

    ChrTalk(
        0x9,
        (
            "If you become independent, crimes in Crossbell will also\x01",
            "To be more strongly regulated\x01",
            "The system will be reviewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Foreign criminals who were tasks, too,\x01",
            "It surely can reduce the number ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… If it is realized, it is a story of.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1902")

    label("loc_1884")


    ChrTalk(
        0x9,
        (
            "If you become independent, crimes in Crossbell will also\x01",
            "To be more strongly regulated\x01",
            "The system will be reviewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… If it is realized, it is a story of.\x02",
    )

    CloseMessageWindow()

    label("loc_1902")

    Jump("loc_1EE1")

    label("loc_1907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A32")

    ChrTalk(
        0x9,
        (
            "When a foreigner commits a crime,\x01",
            "Long period of autonomous state law\x01",
            "It can not be detained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's Cross Bell\x01",
            "Many criminals of the Empire and the Republic type enter\x01",
            "It is a factor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Law amendment by the new mayor is proceeding\x01",
            "A little improvement has been made … …\x01",
            "I guess it is still complete.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AF2")

    label("loc_1A32")


    ChrTalk(
        0x9,
        (
            "If a foreigner commits a crime at the crossbell,\x01",
            "Long period of autonomous state law\x01",
            "It can not be detained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Law amendment by the new mayor is proceeding\x01",
            "A little improvement has been made … …\x01",
            "I guess it is still complete.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF2")

    Jump("loc_1EE1")

    label("loc_1AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C00")

    ChrTalk(
        0x9,
        (
            "Security of detention centers after the cult incident\x01",
            "A considerable review was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it was attacked by a manipulated guard,\x01",
            "Prisoners are allowed to jailbreak etc.\x01",
            "It was a certain moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In future there will be no such thing,\x01",
            "We will also work for more strict security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C8E")

    label("loc_1C00")


    ChrTalk(
        0x9,
        (
            "Security of detention centers after the cult incident\x01",
            "A considerable review was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future to avoid any jailbreak and so on,\x01",
            "We will also work for more strict security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8E")

    Jump("loc_1EE1")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCA")

    ChrTalk(
        0x9,
        (
            "It is detained in this detention center,\x01",
            "Regardless of weight, within autonomous province\x01",
            "They are those who are suspected of crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Recently, I was involved in a cult incident\x01",
            "Some members of parliament and mafia,\x01",
            "And former mayor's secretary such as example was detained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As soon as the trial is ready,\x01",
            "They were based on autonomous state law\x01",
            "I will get judgment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E86")

    label("loc_1DCA")


    ChrTalk(
        0x9,
        (
            "Recently, I was involved in a cult incident\x01",
            "Some members of parliament and mafia,\x01",
            "Former mayor's secretary etc of the example were detained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As soon as the trial is ready,\x01",
            "They were based on autonomous state law\x01",
            "I will get judgment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E86")

    Jump("loc_1EE1")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EE1")

    ChrTalk(
        0x9,
        "…… This is a jail.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is no use,\x01",
            "Shall we not get too close?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE1")

    TalkEnd(0xFE)
    Return()

    # Function_5_1051 end

    def Function_6_1EE5(): pass

    label("Function_6_1EE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210E")

    ChrTalk(
        0x8,
        (
            "#01005F…, what's wrong?\x01",
            "Are not you going to ride?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo~……\x01",
            "When getting into it\x01",
            "Is it kind of afraid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's our private car … …\x01",
            "Considering the situation so far,\x01",
            "You surely gotta shrink.\x02\x03",
            "#00104FReally, people in one department\x01",
            "I miss memorizing the envy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FMy feeling is\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FSasa, everyone!\x01",
            "Let's get in early!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, this one is\x01",
            "It seems to be stingy,\x01",
            "Is not it bad if you scold me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat 's right.\x02\x03",
            "#00000FAll right, then\x01",
            "I suppose I tried getting in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_216F")

    label("loc_210E")


    ChrTalk(
        0x8,
        (
            "#01002FCome on, get on.\x02\x03",
            "#01004FIf this is the case, please cross the city of Crossbell\x01",
            "It will be in a flash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1EE5 end

    def Function_7_2173(): pass

    label("Function_7_2173")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21CC")

    ChrTalk(
        0xFE,
        (
            "Current situation, around the police school\x01",
            "There is no abnormality!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Continue to keep alert!\x02",
    )

    CloseMessageWindow()

    label("loc_21CC")

    TalkEnd(0xFE)
    Return()

    # Function_7_2173 end

    def Function_8_21D0(): pass

    label("Function_8_21D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2256")

    ChrTalk(
        0xFE,
        (
            "With Jorridge manager,\x01",
            "The guard withdrew and it was thin\x01",
            "I ran into this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please leave it to us here.\x02",
    )

    CloseMessageWindow()

    label("loc_2256")

    TalkEnd(0xFE)
    Return()

    # Function_8_21D0 end

    def Function_9_225A(): pass

    label("Function_9_225A")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228C")
    SetScenarioFlags(0x31, 2)

    label("loc_228C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_22CC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22C1")
    Sound(2499, 255, 100, 0)
    Jump("loc_22C7")

    label("loc_22C1")

    Sound(3537, 255, 100, 0)

    label("loc_22C7")

    Jump("loc_22D2")

    label("loc_22CC")

    Sound(3344, 255, 100, 0)

    label("loc_22D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_234B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_232B"),
        (SWITCH_DEFAULT, "loc_233C"),
    )


    label("loc_232B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2346")

    label("loc_233C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2346")

    Jump("loc_258A")

    label("loc_234B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_237F")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_237F")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23B3"),
        (1, "loc_24B7"),
        (2, "loc_2548"),
        (SWITCH_DEFAULT, "loc_2580"),
    )


    label("loc_23B3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_23E4")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_23F4")

    label("loc_23E4")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_23F4")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_244A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246D")
    Sound(461, 0, 100, 0)

    label("loc_246D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_248D")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_249D")

    label("loc_248D")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_249D")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_22D2")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2529")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_24EC")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2504")

    label("loc_24EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_24FF")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2504")

    label("loc_24FF")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2504")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2543")

    label("loc_2529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2539")
    OP_AF(0xFB)
    Jump("loc_2543")

    label("loc_2539")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2543")

    Jump("loc_258A")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2561")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257B")

    label("loc_2561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2571")
    OP_AF(0xFB)
    Jump("loc_257B")

    label("loc_2571")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257B")

    Jump("loc_258A")

    label("loc_2580")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_258A")

    Jump("loc_22D2")

    label("loc_258F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_225A end

    def Function_10_259D(): pass

    label("Function_10_259D")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266C")
    OP_E2(0x2)
    MiniGame(0x6, 0x15, 0x8B10, 0xFFFFD8F0, 0xFFFFC1BC, 0x10E, 0x7D00, 0xFFFFD8F0, 0xFFFFC180)

    label("loc_266C")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_259D end

    def Function_11_2671(): pass

    label("Function_11_2671")

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

    def lambda_26FD():
        OP_95(0xFE, 12000, -10000, -21650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26FD)

    def lambda_2717():
        OP_95(0xFE, 11000, -10000, -23350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2717)

    def lambda_2731():
        OP_95(0xFE, 13000, -10000, -22650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2731)

    def lambda_274B():
        OP_95(0xFE, 12000, -10000, -24350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_274B)
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
            "#00002F#5PWell ……\x01",
            "This is the building of the police school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F#12PWell, finally arrived?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PAs expected it is only in the forest\x01",
            "quiet#4RMyria#You are in a place.\x02\x03",
            "#00100FWhere is the section chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PTentatively, the front entrance\x01",
            "It will be a receptionist for the police school.\x02\x03",
            "#10100FLet's go inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5POh, let's do that.\x02",
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

    # Function_11_2671 end

    def Function_12_2A19(): pass

    label("Function_12_2A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCE")
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
        "#00105F#11POh, what's that there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11POh … it's a jail.\x02\x03",
            "#00001FOn the premises next to the police school\x01",
            "It is located in the same building.\x02",
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
            "#00101F#5PWell then Ernest is\x01",
            "To those who … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11POh, Mr. Dudley\x01",
            "It should have just been imprisoned.\x02\x03",
            "#00000FIf you apply for an appointment\x01",
            "I might be able to meet … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PAh……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00106F#5P…… No, I will stop.\x02\x03",
            "#00108FIt seems like I got into terrible eyes,\x01",
            "Now I have time to look back on my own\x01",
            "I think that it is necessary … ….\x02\x03",
            "#00102FWatching opportunity\x01",
            "I will visit with my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PReally……\x01",
            "That might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12P(There seems to be various things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6P(Yup……\x01",
            "I do not know the details though. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -11250, -10000, 7200, 180)
    SetScenarioFlags(0x127, 4)
    EventEnd(0x5)
    Jump("loc_2E1C")

    label("loc_2DCE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe future is a jail.\x01",
            "Let's keep away from now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -12250, -10000, 8310, 180)
    EventEnd(0x4)

    label("loc_2E1C")

    Return()

    # Function_12_2A19 end

    def Function_13_2E1D(): pass

    label("Function_13_2E1D")

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
        "#00005F#6PHere, this …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PPaid to the Special Affairs Support Division\x01",
            "Drifting car …\x02",
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
        "#10302F#5PWell, it's not bad design.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PHere, this …\x02\x03",
            "Both Vernes and Line faults\x01",
            "It is an invisible design line ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01009F#11PIt is a correct answer.\x02\x03",
            "#01004FThis model number is XD - 78.\x02\x03",
            "#01002FMade by Liberto\x01",
            "Z C F#8RZeiss Central Studio#It is a new type of.\x02",
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
        "#10107F#6PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PZCF drives a driven vehicle\x01",
            "Did you develop it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#5PIs it such a surprise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PYeah, Libert is\x01",
            "Because the country is steep\x01",
            "Drive vehicles are not widespread.\x02\x03",
            "#00100FInstead, ZCF\x01",
            "As the world's best airship manufacturer\x01",
            "It is known ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PThat ZCF is\x01",
            "You developed a powertrain!\x02\x03",
            "#10109FThe spec is! Is it?\x01",
            "What is the maximum speed? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#11PHow, calm down.\x02\x03",
            "#01004FAll-new engine for airship\x01",
            "It seems that a small version is loaded.\x02\x03",
            "#01002FWith maximum speed\x01",
            "1500 Serge seems to be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PThat is amazing …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIs it faster than the railroad … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PBut I often use such a car\x01",
            "Were you able to arrange it?\x02\x03",
            "It has not been officially released yet\x01",
            "It looks like a new model, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11POh, if you are true to you\x01",
            "It is a substitute that can not be paid.\x02\x03",
            "#01002FIt was the reason why I bent him\x01",
            "He is the new Mayor of Dieter.\x02",
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
        "#00011F#6PMayor Dieter! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PWell, indeed if it is your uncle\x01",
            "Because I have a relationship with ZCF\x01",
            "I am convinced ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#6P~ As expected\x01",
            "It is IBC president of the world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHuh, if you are ready so far\x01",
            "On the other hand I will be wary of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PWell, well well,\x01",
            "It will work and return it.\x02\x03",
            "#01000FIf the load is heavy\x01",
            "You can also decline it?\x02\x03",
            "In that case, it is adopted by the police\x01",
            "I will turn the general-purpose car of Verne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHouse……\x01",
            "Thankfully I will use it.\x02\x03",
            "#00000FCan you move it already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F#11PMaintenance and trial operation have already been completed.\x02\x03",
            "Here, Koitsu is the key.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '支援科车辆钥匙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('支援科车辆钥匙', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#6P……my mother……\x01",
            "Something a little emotional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PWell … … I'm going to tell you\x01",
            "I miss memorizing the envy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuh, then then,\x01",
            "Do you want to run a single?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#12POh, that's no problem\x01",
            "I will return to Cros Bell City.\x02\x03",
            "Noel, can you drive?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    ChrTalk(
        0x109,
        "#10109F#5PWell, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PHye, Son, then I\x01",
            "Would you like me to take advantage of it?\x02",
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

    # Function_13_2E1D end

    def Function_14_39A2(): pass

    label("Function_14_39A2")

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

    # Function_14_39A2 end

    def Function_15_3AB0(): pass

    label("Function_15_3AB0")


    def lambda_3AB5():
        OP_95(0xFE, 16500, -10000, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    WaitChrThread(0xFE, 1)

    def lambda_3AF8():
        OP_9E(0xFE, 0x4074, 0xFFFFCF2C, 0xFFFEA070, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AF8)
    Sleep(2600)
    StopSound(468, 1000, 80)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(300)
    Sound(492, 0, 100, 0)
    Sleep(700)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_3B3B():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B3B)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 80, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3AB0 end

    def Function_16_3B77(): pass

    label("Function_16_3B77")

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

    def lambda_3E50():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E50)
    Sleep(100)

    def lambda_3E68():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3E68)
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

    def lambda_3F68():
        OP_9B(0x0, 0xFE, 0x5, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F68)
    Sleep(100)

    def lambda_3F80():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3F80)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10B, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00005F#11PGarcia?\x02",
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
            "#11103F#11PThis is as far as we go together\x02\x03",
            "#11100FFrom here onwards,\x01",
            "You go alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11POnce again,\x01",
            "It is \"Wakasho\" of Rubache.\x02\x03",
            "#11101FOf course, that chairman\x01",
            "I can not let go and run away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PW-wait a minute\x02\x03",
            "Then why\x01",
            "You accompany me so far …\x02\x03",
            "#00007FAnd no matter how much it is\x01",
            "There is nothing I can do about it alone! Is it?\x02\x03",
            "In that case I'll come too\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10B,
        "#11107F#5S#11PBACK OFF BRAT!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10B,
        (
            "#11103F#11PDetermine the truth …\x01",
            "You should have said so.\x02\x03",
            "Release the captured companions\x01",
            "You regain that brat.\x02\x03",
            "#11100F…… In a place like this\x01",
            "Are you having time to gozozu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11P…\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5PThank you Garcia\x02\x03",
            "#00008FOn your stand, your escape\x01",
            "I can not welcome you ….\x02\x03",
            "#00001FBut please make it out ok\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#11104F#11PHappy\x01",
            "I'm worried about uselessness.\x02",
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

    def lambda_444A():
        OP_9B(0x0, 0xFE, 0x5, 0x2AF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_444A)
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
            "#11104F#11PLloyd · Bannings …\x01",
            "…… That brother of that bastard?\x02\x03",
            "#11100FIt is quite good\x01",
            "I guess it is getting on.\x02",
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
        "#2SThere he is!\x05\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(90, 50, -1, -1)

    AnonymousTalk(
        0x13,
        "#2SDon't let him get away\x05\x02",
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
        "#11102F#11PHaha, oh bring it on\x02",
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
            "#11107F#11P#4SIron fist of this \"Killing Bear\"\x01",
            "Have you taste it fully!\x02",
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

    # Function_16_3B77 end

    def Function_17_4814(): pass

    label("Function_17_4814")

    SetChrPos(0xFE, 2550, -10000, -1700, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_17_4814 end

    def Function_18_4844(): pass

    label("Function_18_4844")

    SetChrPos(0xFE, 700, -10000, -1250, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_18_4844 end

    def Function_19_4874(): pass

    label("Function_19_4874")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_488F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_4874")

    label("loc_488F")

    Return()

    # Function_19_4874 end

    def Function_20_4890(): pass

    label("Function_20_4890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48A9")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_20_4890")

    label("loc_48A9")

    Return()

    # Function_20_4890 end

    def Function_21_48AA(): pass

    label("Function_21_48AA")

    OP_82(0x64, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_48BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48E2")
    OP_82(0x0, 0x1E, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("loc_48BE")

    label("loc_48E2")

    Return()

    # Function_21_48AA end

    def Function_22_48E3(): pass

    label("Function_22_48E3")


    def lambda_48E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48E8)
    OP_9B(0x0, 0xFE, 0x0, 0x7530, 0xFA0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_48E3 end

    def Function_23_4908(): pass

    label("Function_23_4908")

    OP_95(0xFE, -16000, -10050, 15000, 5000, 0x1)
    OP_95(0xFE, 11500, -10000, -15650, 5000, 0x0)
    Return()

    # Function_23_4908 end

    def Function_24_4931(): pass

    label("Function_24_4931")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_494C")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_24_4931")

    label("loc_494C")

    Return()

    # Function_24_4931 end

    def Function_25_494D(): pass

    label("Function_25_494D")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Sleep(1400)
    Sound(909, 0, 20, 0)
    Sleep(850)
    Sound(910, 0, 20, 0)
    Return()

    # Function_25_494D end

    def Function_26_496F(): pass

    label("Function_26_496F")

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
            "#6P#00306FWell, than I thought\x01",
            "You looked fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FWell, if that's what you want\x01",
            "You will be able to recover in the near future.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B14")

    ChrTalk(
        0x105,
        (
            "#6P#10400FEven so, it was surprising.\x01",
            "A man like him got us\x01",
            "I will not encourage him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE9")

    label("loc_4B14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B7B")

    ChrTalk(
        0x106,
        (
            "#6P#10703FBut it was surprising.\x01",
            "People like him give us\x01",
            "To encourage me ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE9")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BE9")

    ChrTalk(
        0x109,
        (
            "#6P#10100FEven so, it was surprising.\x01",
            "The former Mafia tells us\x01",
            "To encourage me ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE9")


    ChrTalk(
        0x101,
        (
            "#00000FOh …… Through various incidents,\x01",
            "He may have changed, too.\x02",
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
        "#00005FWhat is it, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FNo, why are they someone else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FPerhaps, I think it's your influence … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00005F……What……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWell, because this is it\x01",
            "What is natural gigolo.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DF9")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F…… He was saying\x01",
            "The word that resembles guy,\x01",
            "It seems that you are not mistaken.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E92")

    label("loc_4DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E49")

    ChrTalk(
        0x109,
        (
            "#6P#10102FHuhu, Mr. Lloyd also\x01",
            "It really is as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E92")

    label("loc_4E49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E92")

    ChrTalk(
        0x106,
        (
            "#6P#10702FHaha ……\x01",
            "Mr. Lloyd is as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E92")

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

    # Function_26_496F end

    def Function_27_4EC2(): pass

    label("Function_27_4EC2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, this direction is for the forest road.\x01",
            "The guided car is in front of the garage.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11900, -10000, -15540, 0)
    EventEnd(0x4)
    Return()

    # Function_27_4EC2 end

    def Function_28_4F1D(): pass

    label("Function_28_4F1D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Western · Crossbell Police School\x01",
            "North / Knox forest area entrance\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_4F1D end

    SaveToFile()

Try(main)
