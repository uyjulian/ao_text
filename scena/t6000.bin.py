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
        "Function_4_FB1",          # 04, 4
        "Function_5_1045",         # 05, 5
        "Function_6_2174",         # 06, 6
        "Function_7_2427",         # 07, 7
        "Function_8_24A8",         # 08, 8
        "Function_9_254B",         # 09, 9
        "Function_10_2888",        # 0A, 10
        "Function_11_294F",        # 0B, 11
        "Function_12_2D10",        # 0C, 12
        "Function_13_3157",        # 0D, 13
        "Function_14_3D39",        # 0E, 14
        "Function_15_3E47",        # 0F, 15
        "Function_16_3F0E",        # 10, 16
        "Function_17_4BE0",        # 11, 17
        "Function_18_4C10",        # 12, 18
        "Function_19_4C40",        # 13, 19
        "Function_20_4C5C",        # 14, 20
        "Function_21_4C76",        # 15, 21
        "Function_22_4CAF",        # 16, 22
        "Function_23_4CD4",        # 17, 23
        "Function_24_4CFD",        # 18, 24
        "Function_25_4D19",        # 19, 25
        "Function_26_4D3B",        # 1A, 26
        "Function_27_52A0",        # 1B, 27
        "Function_28_5313",        # 1C, 28
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

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C74")
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_A20")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A00"),
        (SWITCH_DEFAULT, "loc_A11"),
    )


    label("loc_A00")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_A1B")

    label("loc_A11")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1B")

    Jump("loc_C5D")

    label("loc_A20")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A52")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_A52")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A86"),
        (1, "loc_B8A"),
        (2, "loc_C1B"),
        (SWITCH_DEFAULT, "loc_C53"),
    )


    label("loc_A86")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB7")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_AC7")

    label("loc_AB7")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_AC7")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    Sound(461, 0, 100, 0)

    label("loc_B40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B60")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_B70")

    label("loc_B60")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_B70")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_9AB")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_BFC")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_BBF")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_BD7")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BD2")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_BD7")

    label("loc_BD2")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_BD7")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C16")

    label("loc_BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C0C")
    OP_AF(0xFB)
    Jump("loc_C16")

    label("loc_C0C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C16")

    Jump("loc_C5D")

    label("loc_C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4E")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C44")
    OP_AF(0xFB)
    Jump("loc_C4E")

    label("loc_C44")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4E")

    Jump("loc_C5D")

    label("loc_C53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C5D")

    Jump("loc_9AB")

    label("loc_C62")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Jump("loc_FB0")

    label("loc_C74")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA6")
    SetScenarioFlags(0x31, 2)

    label("loc_CA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CE6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDB")
    Sound(2499, 255, 100, 0)
    Jump("loc_CE1")

    label("loc_CDB")

    Sound(3537, 255, 100, 0)

    label("loc_CE1")

    Jump("loc_CEC")

    label("loc_CE6")

    Sound(3344, 255, 100, 0)

    label("loc_CEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D61")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D41"),
        (SWITCH_DEFAULT, "loc_D52"),
    )


    label("loc_D41")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D5C")

    label("loc_D52")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D5C")

    Jump("loc_F9E")

    label("loc_D61")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D93")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_D93")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DC7"),
        (1, "loc_ECB"),
        (2, "loc_F5C"),
        (SWITCH_DEFAULT, "loc_F94"),
    )


    label("loc_DC7")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_DF8")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_E08")

    label("loc_DF8")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_E08")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E5E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E81")
    Sound(461, 0, 100, 0)

    label("loc_E81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_EA1")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_EB1")

    label("loc_EA1")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_EB1")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_CEC")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F3D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F00")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F18")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F13")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F18")

    label("loc_F13")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F18")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F57")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F4D")
    OP_AF(0xFB)
    Jump("loc_F57")

    label("loc_F4D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F57")

    Jump("loc_F9E")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F75")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8F")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F85")
    OP_AF(0xFB)
    Jump("loc_F8F")

    label("loc_F85")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F8F")

    Jump("loc_F9E")

    label("loc_F94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9E")

    Jump("loc_CEC")

    label("loc_FA3")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)

    label("loc_FB0")

    Return()

    # Function_3_922 end

    def Function_4_FB1(): pass

    label("Function_4_FB1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_100C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1001")
    Sound(2502, 255, 100, 0)
    Jump("loc_1007")

    label("loc_1001")

    Sound(2503, 255, 100, 0)

    label("loc_1007")

    Jump("loc_1030")

    label("loc_100C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_102A")
    Sound(3347, 255, 100, 0)
    Jump("loc_1030")

    label("loc_102A")

    Sound(3348, 255, 100, 0)

    label("loc_1030")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_FB1 end

    def Function_5_1045(): pass

    label("Function_5_1045")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E2")

    ChrTalk(
        0xFE,
        (
            "Even prison security has\x01",
            "returned to our jurisdiction\x01",
            "from the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You might say the\x01",
            "situation was a little\x01",
            "too severe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe Empire and Republic\x01",
            "kept invading, so...\x01",
            "Indeed, you could say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThey probably reinforced\x01",
            "security following my\x01",
            "detention.\x02\x03",
            "#00003FIt appears Dieter tried to\x01",
            "guard against the Support\x01",
            "Section being reunited...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A8")

    label("loc_11E2")


    ChrTalk(
        0xFE,
        (
            "Even prison security has\x01",
            "returned to our jurisdiction\x01",
            "from the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By assigning personnel to the\x01",
            "appropriate positions, it'll be possible\x01",
            "to guard effectively like we did before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A8")

    Jump("loc_2170")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EA")

    ChrTalk(
        0x9,
        (
            "After hearing news of the\x01",
            "attack, the prison inmates\x01",
            "can't conceal their unrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, we checked on the safety of the\x01",
            "inmates' families, but, as expected,\x01",
            "there were some who didn't make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...It's painful to have to\x01",
            "say that, even if it is a\x01",
            "criminal you're saying it to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1474")

    label("loc_13EA")


    ChrTalk(
        0x9,
        (
            "A great number of them\x01",
            "have family in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Although they're criminals,\x01",
            "having to tell them that makes\x01",
            "your heart ache.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1474")

    Jump("loc_2170")

    label("loc_1479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(
        0x9,
        (
            "This derailment... I\x01",
            "wonder if it was done by\x01",
            "someone's hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If true, it's a serious\x01",
            "crime. After all, they hurt\x01",
            "so many innocent civilians...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2170")

    label("loc_1521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_16F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")

    ChrTalk(
        0x9,
        (
            "I've been hearing\x01",
            "screams from deep inside\x01",
            "for some time now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the inmates of\x01",
            "the prison are making\x01",
            "noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It could be scoundrels who are trying\x01",
            "to take advantage of the situation.\x01",
            "We need to pay close attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F1")

    label("loc_162A")


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
            "It could be scoundrels who are trying\x01",
            "to take advantage of the situation.\x01",
            "We need to pay close attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F1")

    Jump("loc_2170")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1835")

    ChrTalk(
        0x9,
        (
            "Due to being so close to them, there's\x01",
            "many jailers who get worn down by the\x01",
            "pressure looking after criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly speaking, aside from holidays,\x01",
            "I have no time to relax myself...\x01",
            "Still, someone's got to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A strong force of will\x01",
            "is needed. ...To work\x01",
            "here, I mean.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18E9")

    label("loc_1835")


    ChrTalk(
        0x9,
        (
            "Due to being so close to them, there's\x01",
            "many jailers who get worn down by the\x01",
            "pressure looking after criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A strong force of will\x01",
            "is needed. ...To work\x01",
            "here, I mean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E9")

    Jump("loc_2170")

    label("loc_18EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E7")

    ChrTalk(
        0x9,
        (
            "If we become independent, the system\x01",
            "will probably be revised to manage\x01",
            "Crossbell much more strictly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even the problematic\x01",
            "foreign criminals would\x01",
            "decrease in number...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...IF we become\x01",
            "independent, that is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A7D")

    label("loc_19E7")


    ChrTalk(
        0x9,
        (
            "If we become independent, the system\x01",
            "will probably be revised to manage\x01",
            "Crossbell much more strictly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...IF we become\x01",
            "independent, that is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7D")

    Jump("loc_2170")

    label("loc_1A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C07")

    ChrTalk(
        0x9,
        (
            "If a foreigner commits a crime,\x01",
            "he can't be detained for a long\x01",
            "period of time due to state law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's become one of the main reasons\x01",
            "so many criminals from the Empire and\x01",
            "Republic come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the legal reform by the new mayor underway,\x01",
            "things have improved a little, but... It's still\x01",
            "got a long way to go to be considered complete.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D09")

    label("loc_1C07")


    ChrTalk(
        0x9,
        (
            "If a foreigner commits a crime in\x01",
            "Crossbell, he can't be detained for\x01",
            "a long period due to state law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the legal reform by the new mayor underway,\x01",
            "things have improved a little, but... It's still\x01",
            "got a long way to go to be considered complete.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D09")

    Jump("loc_2170")

    label("loc_1D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E37")

    ChrTalk(
        0x9,
        (
            "We rethought prison\x01",
            "security after the cult\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although we were attacked by the\x01",
            "manipulated CGF, it was a loss of face to\x01",
            "have to forgive the prisoners' jailbreak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We intend to work out far\x01",
            "more strict security measures\x01",
            "so it doesn't happen again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ECB")

    label("loc_1E37")


    ChrTalk(
        0x9,
        (
            "We rethought prison\x01",
            "security after the cult\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To prevent future jailbreaks,\x01",
            "we intend to work out far\x01",
            "stricter security measures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECB")

    Jump("loc_2170")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2025")

    ChrTalk(
        0x9,
        (
            "The people in this prison are\x01",
            "suspected of violating state\x01",
            "law, regardless of importance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately, we've had custody of some congressmen\x01",
            "and mafia involved in the cult incident and\x01",
            "even the former mayor's secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyhow, as soon as their\x01",
            "trials are complete, they'll\x01",
            "be judged based on state law.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20FE")

    label("loc_2025")


    ChrTalk(
        0x9,
        (
            "Recently, we've had custody of some\x01",
            "congressmen and mafia involved in the cult\x01",
            "incident and that former mayor's secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyhow, as soon as their\x01",
            "trials are complete, they'll\x01",
            "be judged based on state law.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FE")

    Jump("loc_2170")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2170")

    ChrTalk(
        0x9,
        (
            "...This place is a\x01",
            "prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you don't have any\x01",
            "business, could you keep\x01",
            "away from here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2170")

    TalkEnd(0xFE)
    Return()

    # Function_5_1045 end

    def Function_6_2174(): pass

    label("Function_6_2174")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BD")

    ChrTalk(
        0x8,
        (
            "#01005F...Hmm? What's wrong?\x01",
            "Aren't you getting in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well... Being able to\x01",
            "ride in this is like,\x01",
            "awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FTo think, our own personal\x01",
            "car... Considering all that's\x01",
            "happened, we're hesitating.\x02\x03",
            "#00104FWe were indeed envious of the\x01",
            "men and women of Section One\x01",
            "and wanted one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FHehe. I can't say I\x01",
            "don't understand how you\x01",
            "feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FC'mon everyone! Let's\x01",
            "hurry and board!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha. This one's excited,\x01",
            "so maybe we shouldn't\x01",
            "tease her so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FT-That's also true.\x02\x03",
            "#00000FAlright then. Let's\x01",
            "board.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2423")

    label("loc_23BD")


    ChrTalk(
        0x8,
        (
            "#01002FC'mon, board at once.\x02\x03",
            "#01004FWith this baby, we'll be\x01",
            "back in Crossbell City\x01",
            "in a flash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2423")

    TalkEnd(0xFE)
    Return()

    # Function_6_2174 end

    def Function_7_2427(): pass

    label("Function_7_2427")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24A4")

    ChrTalk(
        0xFE,
        (
            "At present, nothing out\x01",
            "of the ordinary on\x01",
            "police academy grounds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll continue to be on\x01",
            "the lookout!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A4")

    TalkEnd(0xFE)
    Return()

    # Function_7_2427 end

    def Function_8_24A8(): pass

    label("Function_8_24A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2547")

    ChrTalk(
        0xFE,
        (
            "After the CGF withdrew they were\x01",
            "short-handed here, so we came rushing\x01",
            "here with Section Chief Joe Ridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please leave this place\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2547")

    TalkEnd(0xFE)
    Return()

    # Function_8_24A8 end

    def Function_9_254B(): pass

    label("Function_9_254B")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_257D")
    SetScenarioFlags(0x31, 2)

    label("loc_257D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_25BD")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25B2")
    Sound(2499, 255, 100, 0)
    Jump("loc_25B8")

    label("loc_25B2")

    Sound(3537, 255, 100, 0)

    label("loc_25B8")

    Jump("loc_25C3")

    label("loc_25BD")

    Sound(3344, 255, 100, 0)

    label("loc_25C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2638")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2618"),
        (SWITCH_DEFAULT, "loc_2629"),
    )


    label("loc_2618")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2633")

    label("loc_2629")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2633")

    Jump("loc_2875")

    label("loc_2638")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_266A")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_266A")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_269E"),
        (1, "loc_27A2"),
        (2, "loc_2833"),
        (SWITCH_DEFAULT, "loc_286B"),
    )


    label("loc_269E")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_26CF")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_26DF")

    label("loc_26CF")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_26DF")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2735")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2735")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2758")
    Sound(461, 0, 100, 0)

    label("loc_2758")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2778")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2788")

    label("loc_2778")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2788")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_25C3")

    label("loc_27A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2814")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_27D7")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_27EF")

    label("loc_27D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_27EA")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_27EF")

    label("loc_27EA")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_27EF")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_282E")

    label("loc_2814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2824")
    OP_AF(0xFB)
    Jump("loc_282E")

    label("loc_2824")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_282E")

    Jump("loc_2875")

    label("loc_2833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2866")

    label("loc_284C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_285C")
    OP_AF(0xFB)
    Jump("loc_2866")

    label("loc_285C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2866")

    Jump("loc_2875")

    label("loc_286B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2875")

    Jump("loc_25C3")

    label("loc_287A")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_254B end

    def Function_10_2888(): pass

    label("Function_10_2888")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
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
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294A")
    OP_E2(0x2)
    MiniGame(0x6, 0x15, 0x8B10, 0xFFFFD8F0, 0xFFFFC1BC, 0x10E, 0x7D00, 0xFFFFD8F0, 0xFFFFC180)

    label("loc_294A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_2888 end

    def Function_11_294F(): pass

    label("Function_11_294F")

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

    def lambda_29DB():
        OP_95(0xFE, 12000, -10000, -21650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29DB)

    def lambda_29F5():
        OP_95(0xFE, 11000, -10000, -23350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29F5)

    def lambda_2A0F():
        OP_95(0xFE, 13000, -10000, -22650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A0F)

    def lambda_2A29():
        OP_95(0xFE, 12000, -10000, -24350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A29)
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
            "#00002F#5PFinally... The police\x01",
            "academy building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PPhew, so we're finally\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PBeing located in a\x01",
            "forest like this, it's\x01",
            "rather quiet.\x02\x03",
            "#00100FI wonder where chief is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PFor now, let's use the main\x01",
            "entrance and speak with the\x01",
            "academy receptionist.\x02\x03",
            "#10100FShall we head inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, let's.\x02",
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

    # Function_11_294F end

    def Function_12_2D10(): pass

    label("Function_12_2D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FB")
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
        (
            "#00105F#11PMy, what's that\x01",
            "building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PAh... It's the prison.\x02\x03",
            "#00001FIt was built right next\x01",
            "to the police academy.\x02",
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
            "#00101F#5PThen, was Ernest brought\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah, Dudley and the\x01",
            "others just imprisoned\x01",
            "him.\x02\x03",
            "#00000FYou can see him if you\x01",
            "submit a meeting\x01",
            "request, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00106F#5P...Hmm, I'll pass on that.\x02\x03",
            "#00108FThat must have been a terrible\x01",
            "experience for him. I think he\x01",
            "needs time for introspection...\x02\x03",
            "#00102FI'd like to visit him with\x01",
            "grandfather later, if there's a\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PI see... That might be\x01",
            "for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12P(Looks like a lot\x01",
            "happened between them.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6P(Yeah... I don't know\x01",
            "the details either.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -11250, -10000, 7200, 180)
    SetScenarioFlags(0x127, 4)
    EventEnd(0x5)
    Jump("loc_3156")

    label("loc_30FB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe prison is ahead.\x01",
            "Let's stay away from\x01",
            "there for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -12250, -10000, 8310, 180)
    EventEnd(0x4)

    label("loc_3156")

    Return()

    # Function_12_2D10 end

    def Function_13_3157(): pass

    label("Function_13_3157")

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
            "#00105F#6PThe orbal car that was\x01",
            "issued to the Special\x01",
            "Support Section...?\x02",
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
        "#10302F#5PWow, not a bad design.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PT-This is...\x02\x03",
            "It doesn't look like a\x01",
            "Reinford or Verne Co.\x01",
            "model...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01009F#11PHehe, right answer.\x02\x03",
            "#01004FThis is the XD-78.\x02\x03",
            "#01002FIt's Zeiss Central\x01",
            "Factory's latest model.\x02",
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
        "#10107F#6PWh-Whaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PSince when was ZCF\x01",
            "developing orbal cars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#5PIs it that shocking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PYes. Liberl has a lot of\x01",
            "rugged terrain, so cars\x01",
            "are not widespread there.\x02\x03",
            "#00100FInstead, ZCF is known as\x01",
            "the world-leading airship\x01",
            "manufacturer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PT-To think ZCF developed\x01",
            "an orbal car!\x02\x03",
            "#10109FWhat are the specs!?\x01",
            "What's it's top speed!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#11PWhoa there, calm down.\x02\x03",
            "#01004FLooks like it's equipped\x01",
            "with a mini version of\x01",
            "their new airship engine.\x02\x03",
            "#01002FAnd it looks it can do\x01",
            "1500 selge per hour,\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PT-That's amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PThat's even faster than\x01",
            "a train...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PBut, we're pretty lucky\x01",
            "to have gotten a vehicle\x01",
            "like this.\x02\x03",
            "It's so new that it\x01",
            "hasn't been put on the\x01",
            "market yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PYeah. Normally, you guys\x01",
            "wouldn't be issued a car\x01",
            "like this.\x02\x03",
            "#01002FDieter, the new mayor,\x01",
            "got it for you.\x02",
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
        "#00011F#6PMayor Dieter!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PW-Well, it makes some\x01",
            "sense because "uncle" has\x01",
            "contacts at ZCF, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#6PThe president of the\x01",
            "incredible IBC is really\x01",
            "something else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PThat he got one this\x01",
            "nice for us makes me\x01",
            "cautious, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PHehe, well I'm sure you'll\x01",
            "be working plenty hard to\x01",
            "repay him.\x02\x03",
            "#01000FIf it's too much of a\x01",
            "burden, you could always\x01",
            "refuse acceptance, you know?\x02\x03",
            "In that case, we'll give you\x01",
            "a standard-issue Verne Co.\x01",
            "model instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo... We'll put this one\x01",
            "to good use.\x02\x03",
            "#00000FDoes it run?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01000F#11PMaintenance and test\x01",
            "runs are complete.\x02\x03",
            "Here, the keys.\x02",
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
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x35C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002F#6P...Haha... I'm moved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PThat's right... I remember\x01",
            "how envious we were of the\x01",
            "Section One detectives' cars.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHaha, so are we taking\x01",
            "her for a spin?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah. Let's return to\x01",
            "Crossbell City in the\x01",
            "car.\x02\x03",
            "Noｱl, will you handle\x01",
            "the driving?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    ChrTalk(
        0x109,
        "#10109F#5PYes. Leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PHmph, then I guess I'll\x01",
            "hitch a ride too.\x02",
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

    # Function_13_3157 end

    def Function_14_3D39(): pass

    label("Function_14_3D39")

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

    # Function_14_3D39 end

    def Function_15_3E47(): pass

    label("Function_15_3E47")


    def lambda_3E4C():
        OP_95(0xFE, 16500, -10000, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E4C)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    WaitChrThread(0xFE, 1)

    def lambda_3E8F():
        OP_9E(0xFE, 0x4074, 0xFFFFCF2C, 0xFFFEA070, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E8F)
    Sleep(2600)
    StopSound(468, 1000, 80)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(300)
    Sound(492, 0, 100, 0)
    Sleep(700)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_3ED2():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ED2)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 80, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3E47 end

    def Function_16_3F0E(): pass

    label("Function_16_3F0E")

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

    def lambda_41E7():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41E7)
    Sleep(100)

    def lambda_41FF():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_41FF)
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

    def lambda_42FF():
        OP_9B(0x0, 0xFE, 0x5, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42FF)
    Sleep(100)

    def lambda_4317():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4317)
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
            "#11103F#11P─This is as far as we\x01",
            "go.\x02\x03",
            "#11100FYou'll go by yourself\x01",
            "from here on.\x02",
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
            "#11104F#11PEven with these\x01",
            "circumstances, I'm still a\x01",
            "Revache boss.\x02\x03",
            "#11101FMy underlings of course, but\x01",
            "even that president... I\x01",
            "can't run away and leave 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PW-Wait!\x02\x03",
            "In that case, why did\x01",
            "you take me this far?\x02\x03",
            "#00007FAlso, even if it's you,\x01",
            "you won't succeed alone,\x01",
            "right!?\x02\x03",
            "Then, I'll─\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10B,
        (
            "#11107F#5S#11PDon't get the wrong\x01",
            "idea, kid!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10B,
        (
            "#11103F#11PTo discover the truth...\x01",
            "That's what you said.\x02\x03",
            "To free your arrested\x01",
            "comrades and get back\x01",
            "that brat, also.\x02\x03",
            "#11100F...Do you have the time\x01",
            "to dawdle in a place\x01",
            "like this?\x02",
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
            "#00003F#5P─Thanks, Garcｵa.\x02\x03",
            "#00008FGiven my position, I\x01",
            "can't exactly welcome\x01",
            "your jailbreak, but...\x02\x03",
            "#00001FPlease stay safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#11104F#11PHah! A needless worry.\x02",
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

    def lambda_47FD():
        OP_9B(0x0, 0xFE, 0x5, 0x2AF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47FD)
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
            "...That bastard's\x01",
            "younger brother, eh?\x02\x03",
            "#11100FHe's got quite the nice\x01",
            "expression, doesn't he.\x02",
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
        (
            "#11102F#11PHeh, this high ground is\x01",
            "enough...\x02",
        )
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
            "#11107F#11P#4SHave a taste of this\x01",
            "Killing Bear's iron\x01",
            "fists!\x02",
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

    # Function_16_3F0E end

    def Function_17_4BE0(): pass

    label("Function_17_4BE0")

    SetChrPos(0xFE, 2550, -10000, -1700, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_17_4BE0 end

    def Function_18_4C10(): pass

    label("Function_18_4C10")

    SetChrPos(0xFE, 700, -10000, -1250, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_18_4C10 end

    def Function_19_4C40(): pass

    label("Function_19_4C40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C5B")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_4C40")

    label("loc_4C5B")

    Return()

    # Function_19_4C40 end

    def Function_20_4C5C(): pass

    label("Function_20_4C5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C75")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_20_4C5C")

    label("loc_4C75")

    Return()

    # Function_20_4C5C end

    def Function_21_4C76(): pass

    label("Function_21_4C76")

    OP_82(0x64, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_4C8A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CAE")
    OP_82(0x0, 0x1E, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("loc_4C8A")

    label("loc_4CAE")

    Return()

    # Function_21_4C76 end

    def Function_22_4CAF(): pass

    label("Function_22_4CAF")


    def lambda_4CB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CB4)
    OP_9B(0x0, 0xFE, 0x0, 0x7530, 0xFA0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_4CAF end

    def Function_23_4CD4(): pass

    label("Function_23_4CD4")

    OP_95(0xFE, -16000, -10050, 15000, 5000, 0x1)
    OP_95(0xFE, 11500, -10000, -15650, 5000, 0x0)
    Return()

    # Function_23_4CD4 end

    def Function_24_4CFD(): pass

    label("Function_24_4CFD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D18")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_24_4CFD")

    label("loc_4D18")

    Return()

    # Function_24_4CFD end

    def Function_25_4D19(): pass

    label("Function_25_4D19")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Sleep(1400)
    Sound(909, 0, 20, 0)
    Sleep(850)
    Sound(910, 0, 20, 0)
    Return()

    # Function_25_4D19 end

    def Function_26_4D3B(): pass

    label("Function_26_4D3B")

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
            "#6P#00306FMan, he's doin' better\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FRight. At that rate,\x01",
            "he'll be in full health\x01",
            "soon enough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EDE")

    ChrTalk(
        0x105,
        (
            "#6P#10400FEven so, it was unexpected,\x01",
            "being encouraged by someone\x01",
            "like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA0")

    label("loc_4EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F41")

    ChrTalk(
        0x106,
        (
            "#6P#10703FStill, how unexpected to\x01",
            "be encouraged by a\x01",
            "person like him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA0")

    label("loc_4F41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FA0")

    ChrTalk(
        0x109,
        (
            "#6P#10100FEven so, it was unexpected,\x01",
            "being encouraged by former\x01",
            "mafia...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA0")


    ChrTalk(
        0x101,
        (
            "#00000FYeah... He's probably\x01",
            "changed through his own\x01",
            "experiences as well.\x02",
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
            "#12P#00211FNo, I was just thinking that\x01",
            "you were saying it like it\x01",
            "doesn't concern you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FI think, probably due to\x01",
            "your influence...\x02",
        )
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
            "#6P#00306FOh man. See, that's why\x01",
            "you're a natural gigolo.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51EF")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F...Even what he said, that\x01",
            "you resemble your older\x01",
            "brother, seems true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5270")

    label("loc_51EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5233")

    ChrTalk(
        0x109,
        (
            "#6P#10102FHaha, Lloyd is Lloyd\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5270")

    label("loc_5233")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5270")

    ChrTalk(
        0x106,
        (
            "#6P#10702FAhaha... Lloyd never\x01",
            "changes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5270")

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

    # Function_26_4D3B end

    def Function_27_52A0(): pass

    label("Function_27_52A0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, the woodland path\x01",
            "is this way. The orbal car\x01",
            "is in front of the garage.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11900, -10000, -15540, 0)
    EventEnd(0x4)
    Return()

    # Function_27_52A0 end

    def Function_28_5313(): pass

    label("Function_28_5313")

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

    # Function_28_5313 end

    SaveToFile()

Try(main)
