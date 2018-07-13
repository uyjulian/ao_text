from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3000.bin",                # FileName
        "t3000",                    # MapName
        "t3000",                    # Location
        0x005B,                     # MapIndex
        "ed7202",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 1, 0, 2],
    )

    BuildStringList((
        "t3000",                  # 0
        "Guide Doll",             # 1
        "Man in White Robe",      # 2
        "Boy",                    # 3
        "Meister Jｶrg",          # 4
        "Heintz",                 # 5
        "車",                     # 6
        "SE制御",                 # 7
        "Mainz Mountain Road",    # 8
    ))

    AddCharChip((
        "chr/ch47400.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  2.0,                   40.0,                  -0.5,                  900.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -0.1666666716337204,   -8.0,                  0.05000000074505806,   1.0])

    DeclActor(4294960206, 0,       24320,   1200,    4294960206, 2500,    24320,   0x007C, 0,  3,  0x0000)
    DeclActor(2070,    250,     26860,   1200,    2070,    1500,    26860,   0x007C, 0,  4,  0x0000)
    DeclActor(2000,    2500,    47300,   1200,    2000,    4000,    47300,   0x007C, 0,  5,  0x0000)

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "Mainz Mountain Road")

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_6F1",          # 03, 3
        "Function_4_759",          # 04, 4
        "Function_5_797",          # 05, 5
        "Function_6_7A4",          # 06, 6
        "Function_7_1D10",         # 07, 7
        "Function_8_1D32",         # 08, 8
        "Function_9_1D54",         # 09, 9
        "Function_10_1D76",        # 0A, 10
        "Function_11_1D98",        # 0B, 11
        "Function_12_1DAF",        # 0C, 12
        "Function_13_1DC9",        # 0D, 13
        "Function_14_1DE3",        # 0E, 14
        "Function_15_1DFD",        # 0F, 15
        "Function_16_1E26",        # 10, 16
        "Function_17_1E4F",        # 11, 17
        "Function_18_1EAF",        # 12, 18
        "Function_19_33BF",        # 13, 19
        "Function_20_33F4",        # 14, 20
        "Function_21_347D",        # 15, 21
        "Function_22_40C5",        # 16, 22
        "Function_23_40FB",        # 17, 23
        "Function_24_4165",        # 18, 24
        "Function_25_4188",        # 19, 25
        "Function_26_5394",        # 1A, 26
        "Function_27_5406",        # 1B, 27
        "Function_28_54AF",        # 1C, 28
        "Function_29_54E7",        # 1D, 29
        "Function_30_551F",        # 1E, 30
        "Function_31_5557",        # 1F, 31
        "Function_32_558F",        # 20, 32
        "Function_33_55C7",        # 21, 33
        "Function_34_55FF",        # 22, 34
        "Function_35_5D40",        # 23, 35
        "Function_36_5DAA",        # 24, 36
        "Function_37_6320",        # 25, 37
        "Function_38_6377",        # 26, 38
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_412")
    Jump("loc_46F")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 2500, 46450, 180)
    BeginChrThread(0x8, 0, 0, 0)
    Jump("loc_46F")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_44A")
    Jump("loc_46F")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_46F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 2500, 46450, 180)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_483")
    ClearScenarioFlags(0x22, 0)
    Event(0, 25)
    Jump("loc_492")

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_492")
    ClearScenarioFlags(0x22, 1)
    Event(0, 36)

    label("loc_492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_4E3")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_4E3")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E3")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_4E3")

    Return()

    # Function_1_404 end

    def Function_2_4E4(): pass

    label("Function_2_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4F6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_584")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_584")

    label("loc_584")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_597")
    Jump("loc_61C")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    Jump("loc_61C")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_61C")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_61C")
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_1B(0x0, 0x0, 0x26)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_END)), "loc_63D")
    Jump("loc_67E")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_659")
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_67E")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_END)), "loc_667")
    Jump("loc_67E")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_67E")
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    label("loc_67E")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_END)), "loc_692")
    Jump("loc_6CB")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_6AA")
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_6CB")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_END)), "loc_6B8")
    Jump("loc_6CB")

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_6CB")
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)

    label("loc_6CB")

    OP_65(0x2, 0x1)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_4E4 end

    def Function_3_6F1(): pass

    label("Function_3_6F1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   "Rosenberg Studio"\x01",
            "Authorized Personnel Only\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_6F1 end

    def Function_4_759(): pass

    label("Function_4_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76B")
    Call(0, 21)
    Return()

    label("loc_76B")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_4_759 end

    def Function_5_797(): pass

    label("Function_5_797")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_797 end

    def Function_6_7A4(): pass

    label("Function_6_7A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch06600.itc", 0x20)
    SoundLoad(3701)
    SoundLoad(3702)
    SoundLoad(3703)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    OP_68(2000, 600, 24500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 230, 0, 3850, 0)
    SetChrPos(0x102, 900, 0, 2310, 0)
    SetChrPos(0x109, -430, 0, 1790, 0)
    SetChrPos(0x105, 440, 0, 740, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrPos(0x9, 2600, 0, 22100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrPos(0xA, 1400, 0, 22100, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrPos(0xB, 2000, 0, 24300, 180)
    ClearChrFlags(0xB, 0x4)
    OP_70(0x0, 0xA)
    OP_68(2250, 6700, 42650, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(84820, 0)
    FadeToBright(1000, 0)
    OP_68(2250, 6700, 42650, 6000)
    MoveCamera(17, 11, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(93510, 6000)
    Sleep(1000)
    PlaceName2(100, 200, "c_plac16", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(2000, 3600, 23000, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    OP_68(2000, 1000, 23000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "──How insistent.\x01",
            "I don't intend to let you in.\x02\x03",
            "No matter if you're the "Thirteen\x01",
            "Workshops" supervisor, you have\x01",
            "no right to enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x9,
        (
            "...Hu hu, oh, fine then.\x02\x03",
            "That's No. XV's property.\x01",
            "I don't intend to take it away.\x02\x03",
            "However, Meister?\x01",
            "Can you hand me the data?\x02\x03",
            "That's what "that person"\x01",
            "wants too, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0xB,
        (
            "#03903F#5P...Hmph.\x01",
            "You don't need to tell me that.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xA,
        (
            "#3701V#30WUhuhu, you really don't get along.\x02\x03",
            "#3702VKnowing that he hates you, you came\x01",
            "to visit him on purpose, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE76)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#04709F#11PHa ha, what're you saying?\x02\x03",
            "#04702FThe Meister and I are old friends.\x02\x03",
            "Especially in regards to doll making,\x01",
            "we're tied by a solid teacher-student\x01",
            "bond, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHmph, stop the nonsense.\x02\x03",
            "#03900FAfter all, my skills are seen as\x01",
            "old fashioned by the Society.\x02\x03",
            "They have your "integration theory", so\x01",
            "what need do they have to rely on me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PUh uh, how modest.\x02\x03",
            "No one in this world\x01",
            "surpasses the Meister\x01",
            "in tuning the dolls.\x02\x03",
            "#04705FOh, but wouldn't you just give me the circuit\x01",
            "that was applied to the "Pater-Mater", hm?\x02\x03",
            "#04703FIf not, that would make all\x01",
            "of the "Angel of Slaughter"\x01",
            "potential go to waste...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#03901F#5P...Damn fiend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5PUhhm, excuse us.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(920, 300, 9760, 0)
    MoveCamera(33, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32049, 0)
    Fade(500)
    BeginChrThread(0x101, 0, 0, 7)
    BeginChrThread(0x102, 0, 0, 8)
    BeginChrThread(0x109, 0, 0, 9)
    BeginChrThread(0x105, 0, 0, 10)
    OP_68(2000, 1000, 23000, 8000)
    MoveCamera(42, 15, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(25150, 8000)

    def lambda_10F4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10F4)
    Sleep(50)

    def lambda_1104():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1104)
    Sleep(3000)
    OP_0D()
    OP_68(2000, 1000, 23000, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    Fade(500)
    OP_0D()
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x109, 0xFF)
    OP_4B(0x105, 0xFF)

    ChrTalk(
        0x9,
        "#04705F#5POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04805F#5PWhat?\x01",
            "Seems you have guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5P...Campanella.\x01",
            "Your business is over, right?\x02\x03",
            "#03900FTake that unpleasant man\x01",
            "with you and leave.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_120C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_120C)
    Sleep(50)

    def lambda_121C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_121C)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#04804F#12PUhuhu, all right.\x02\x03",
            "#04802FCome on now, Doctor.\x01",
            "Let's go to the next place at once.\x02\x03",
            "You want to finish things today and\x01",
            "go back to the laboratory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PHu hu, that goes without saying.\x02\x03",
            "#04702FThen, Meister...\x01",
            "I'll excuse myself now.\x02\x03",
            "Please check those little guys\x01",
            "as soon as they're completed, hm?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x109, 0xFF)
    OP_4C(0x105, 0xFF)
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        (
            "#03901F#5P#4S...How insistent you're!\x01",
            "Scram already!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#04809F#12P#3703V#30WUhuhu, see you again.\x02",
    )

    CloseMessageWindow()
    OP_24(0xE77)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(22250, 3000)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 16)
    BeginChrThread(0xA, 0, 0, 15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(2000)

    ChrTalk(
        0xB,
        "#03900F#5P...What nonsense.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
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
    BeginChrThread(0x101, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x109, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x105, 0, 0, 14)
    Sleep(300)
    SetCameraDistance(20150, 2000)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_165F")

    ChrTalk(
        0x101,
        "#00006F#12PE-Excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PThank you for back then...\x01",
            "It has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PThe SSS eh, it's been a while.\x02\x03",
            "#03900FRenne has left for Liberl.\x01",
            "What could you want now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177E")

    label("loc_165F")


    ChrTalk(
        0x101,
        (
            "#00006F#12PE-Excuse us..\x02\x03",
            "#00000F...Nice to meet you.\x01",
            "We're from the Police\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PAre you Meister Jｶrg, the\x01",
            "Rosenberg Studio owner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHmph, seems you've heard\x01",
            "something from Renne.\x02\x03",
            "#03900FRenne has left for Liberl.\x01",
            "What do you want?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177E")


    ChrTalk(
        0x101,
        (
            "#00012F#12PWell, since we were nearby\x01",
            "we just came to greet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PUhhm...\x01",
            "Excuse us, you were having guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03901F#5PHmph, unbidden guests.\x01",
            "Don't mind it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(250)

    ChrTalk(
        0xB,
        (
            "#03903F#11PHowever, now I don't have anything\x01",
            "in particular to tell you.\x02\x03",
            "If you have other business,\x01",
            "you can come visit again.\x02\x03",
            "#03900FI'll at least hear what you have to\x01",
            "say out of deference for Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PAh...\x02",
    )

    CloseMessageWindow()
    OP_68(2420, 1000, 24440, 2000)
    BeginChrThread(0xB, 0, 0, 17)
    Sleep(2000)
    Sound(113, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(800)
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

    ChrTalk(
        0x109,
        "#10105F#12PT-The gate closed on its own...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PUuhm, it's old but maybe it's\x01",
            "got some kind of mechanism?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(1870, 1000, 21870, 1300)
    MoveCamera(29, 14, 0, 1300)
    OP_6E(510, 1300)
    SetCameraDistance(19000, 1300)
    TurnDirection(0x101, 0x105, 500)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B2F")

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah...\x01",
            "After all, it's a place where incredible\x01",
            "mechanised dolls are made.\x02\x03",
            "#00008FAlso... Those guests\x01",
            "from before worry me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_1B2F")


    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, like we heard from Renne,\x01",
            "it doesn't seem to be a mere doll studio.\x02\x03",
            "#00008FAlso... Those guests\x01",
            "from before worry me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBB")

    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00103F#11PYes, he said they\x01",
            "were unbidden, but...\x02\x03",
            "#00108FHow can I explain, well...\x01",
            "I felt they were suspicious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10106F#6PYou're right...\x02\x03",
            "#10100FWell, they didn't look\x01",
            "dangerous, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12P(...Hu hu, they didn't look\x01",
            "dangerous, eh?)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 130, 0, 20860, 0)
    SetScenarioFlags(0x129, 4)
    OP_2C(0xA1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_6_7A4 end

    def Function_7_1D10(): pass

    label("Function_7_1D10")

    OP_9B(0x0, 0xFE, 0x4, 0x36B0, 0x7D0, 0x0)

    def lambda_1D24():

        label("loc_1D24")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D24")

    QueueWorkItem2(0xFE, 2, lambda_1D24)
    Return()

    # Function_7_1D10 end

    def Function_8_1D32(): pass

    label("Function_8_1D32")

    OP_9B(0x0, 0xFE, 0x5, 0x3BC4, 0x7D0, 0x0)

    def lambda_1D46():

        label("loc_1D46")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D46")

    QueueWorkItem2(0xFE, 2, lambda_1D46)
    Return()

    # Function_8_1D32 end

    def Function_9_1D54(): pass

    label("Function_9_1D54")

    OP_9B(0x0, 0xFE, 0x6, 0x38A4, 0x7D0, 0x0)

    def lambda_1D68():

        label("loc_1D68")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D68")

    QueueWorkItem2(0xFE, 2, lambda_1D68)
    Return()

    # Function_9_1D54 end

    def Function_10_1D76(): pass

    label("Function_10_1D76")

    OP_9B(0x0, 0xFE, 0x6, 0x3C8C, 0x7D0, 0x0)

    def lambda_1D8A():

        label("loc_1D8A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D8A")

    QueueWorkItem2(0xFE, 2, lambda_1D8A)
    Return()

    # Function_10_1D76 end

    def Function_11_1D98(): pass

    label("Function_11_1D98")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_11_1D98 end

    def Function_12_1DAF(): pass

    label("Function_12_1DAF")

    Sleep(50)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xE10, 0x7D0, 0x0)
    Return()

    # Function_12_1DAF end

    def Function_13_1DC9(): pass

    label("Function_13_1DC9")

    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_13_1DC9 end

    def Function_14_1DE3(): pass

    label("Function_14_1DE3")

    Sleep(150)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_14_1DE3 end

    def Function_15_1DFD(): pass

    label("Function_15_1DFD")

    Sleep(50)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_15_1DFD end

    def Function_16_1E26(): pass

    label("Function_16_1E26")

    Sleep(250)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_16_1E26 end

    def Function_17_1E4F(): pass

    label("Function_17_1E4F")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)

    def lambda_1E84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E84)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_17_1E4F end

    def Function_18_1EAF(): pass

    label("Function_18_1EAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x2, 0xD)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0x102, 750, 0, -6250, 0)
    SetChrPos(0x103, -750, 0, -7250, 0)
    SetChrPos(0x104, 0, 0, -7750, 0)
    SetChrPos(0x109, 250, 0, -8750, 0)
    SetChrPos(0x105, 1500, 0, -7250, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xB, 1600, 0, 24300, 180)
    SetChrPos(0xC, 1600, 0, 21300, 0)
    SetChrPos(0xD, 5000, 0, 19000, 180)
    OP_D5(0xD, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(0, 1000, -7000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(0, 1000, -4000, 3000)
    SetCameraDistance(20500, 3000)
    FadeToBright(1000, 0)

    def lambda_2024():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2024)
    Sleep(10)

    def lambda_203C():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_203C)
    Sleep(10)

    def lambda_2054():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2054)
    Sleep(10)

    def lambda_206C():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_206C)
    Sleep(10)

    def lambda_2084():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2084)
    Sleep(10)

    def lambda_209C():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_209C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PA transport truck...?\x02",
    )

    CloseMessageWindow()
    OP_68(1400, 1000, 22800, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(20500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#12PMeister, you've really\x01",
            "been a great help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PIt seems that we'll make it in time somehow\x01",
            "for the public performance in two days!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHonestly...\x01",
            "When it comes down to your troupe, every\x01",
            "single time your requests are too demanding.\x02\x03",
            "Not only the automatas' tuning, but\x01",
            "also the ordering of a new stage setting...\x02\x03",
            "#03901FEven I am busy, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAhaha...\x01",
            "I'm terribly sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAnyhow, the requests from Miss Ilya\x01",
            "and the Troupe Chief are taxing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAnd in the end, they even made an\x01",
            "additional order for that kind of device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03900F#5PHmph, well, whatever.\x02\x03",
            "#03903F...Making use of my studio's \x01",
            "technology for your plays would\x01",
            "probably suit the Goddess's will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PY-Yes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P──By the way, Meister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PWe have been inviting you for a long time,\x01",
            "we absolutely want you to see an\x01",
            "Arc-en-ciel public performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAlso, you always provide us with outstanding\x01",
            "automatas and stage settings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PI'm getting a suitable amount of mira.\x02\x03",
            "#03900F...I'm busy. \x01",
            "I'll just accept the thought.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)

    ChrTalk(
        0xC,
        "#12PAh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_68(1400, 1000, 24300, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(20500, 1000)

    def lambda_262E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_262E)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    WaitChrThread(0xC, 1)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#12P...*sigh*.\x01",
            "Couldn't you accept?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PI'd like you to see once how\x01",
            "the stage settings you work\x01",
            "so hard on are used...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Excuse us...\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2715():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2715)
    SetChrPos(0x101, 1400, 0, 15000, 0)
    SetChrPos(0x102, 2150, 0, 14750, 0)
    SetChrPos(0x103, 650, 0, 13750, 0)
    SetChrPos(0x104, 1400, 0, 13250, 0)
    SetChrPos(0x109, 1650, 0, 12250, 0)
    SetChrPos(0x105, 2900, 0, 13750, 0)
    OP_68(1400, 1000, 22500, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_27B6():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27B6)
    Sleep(50)

    def lambda_27CE():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_27CE)
    Sleep(50)

    def lambda_27E6():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_27E6)
    Sleep(50)

    def lambda_27FE():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_27FE)
    Sleep(50)

    def lambda_2816():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2816)
    Sleep(50)

    def lambda_282E():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_282E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0xC, 2)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#5POh...\x01",
            "Aren't you the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PAh, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PYou're the Arc-en-ciel\x01",
            "engineer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, my name is Heintz.\x01",
            "I'm in charge of the stage settings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PFancy meeting you here.\x01",
            "Do you need something from the Meister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PY-Yes, we would like to consult\x01",
            "with him about something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12PDid you come to get \x01",
            "equipment for the stage...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, we asked for automatas\x01",
            "tuning and the making of a\x01",
            "new stage setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt was an unreasonable schedule connected\x01",
            "to the renewal public performance, but\x01",
            "somehow he did us the favor to finish all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMaaan, all the troupe\x01",
            "members are really\x01",
            "indebted to the Meister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PBy the way, the Arc-en-ciel\x01",
            "renewal play first public\x01",
            "performance is in two days, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes. Starting from Miss Ilya,\x01",
            "all members are fired up as\x01",
            "they never have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI feel tense too being in\x01",
            "charge of the stage settings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHu hu, it seems it'll be\x01",
            "an amazing play for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POops, I can't stay here.\x01",
            "I must go back fast and set things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P──Everyone, see you!\x01",
            "Please come again to the theatre!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PYes, goodbye.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PPlease be careful.\x02",
    )

    CloseMessageWindow()

    def lambda_2D51():
        OP_9B(0x1, 0xFE, 0xE6, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D51)
    BeginChrThread(0xC, 1, 0, 20)
    OP_68(2900, 1000, 18300, 5000)
    SetCameraDistance(21500, 5000)

    def lambda_2D86():

        label("loc_2D86")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D86")

    QueueWorkItem2(0x101, 2, lambda_2D86)

    def lambda_2D98():

        label("loc_2D98")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D98")

    QueueWorkItem2(0x102, 2, lambda_2D98)

    def lambda_2DAA():

        label("loc_2DAA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2DAA")

    QueueWorkItem2(0x103, 2, lambda_2DAA)

    def lambda_2DBC():

        label("loc_2DBC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2DBC")

    QueueWorkItem2(0x104, 2, lambda_2DBC)

    def lambda_2DCE():

        label("loc_2DCE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2DCE")

    QueueWorkItem2(0x109, 2, lambda_2DCE)

    def lambda_2DE0():

        label("loc_2DE0")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2DE0")

    QueueWorkItem2(0x105, 2, lambda_2DE0)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xC, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    Sound(470, 0, 50, 0)
    OP_71(0x2, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x2)

    def lambda_2E27():

        label("loc_2E27")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E27")

    QueueWorkItem2(0x101, 2, lambda_2E27)

    def lambda_2E39():

        label("loc_2E39")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E39")

    QueueWorkItem2(0x102, 2, lambda_2E39)

    def lambda_2E4B():

        label("loc_2E4B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E4B")

    QueueWorkItem2(0x103, 2, lambda_2E4B)

    def lambda_2E5D():

        label("loc_2E5D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E5D")

    QueueWorkItem2(0x104, 2, lambda_2E5D)

    def lambda_2E6F():

        label("loc_2E6F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E6F")

    QueueWorkItem2(0x109, 2, lambda_2E6F)

    def lambda_2E81():

        label("loc_2E81")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E81")

    QueueWorkItem2(0x105, 2, lambda_2E81)
    OP_68(2900, 1000, 10300, 5000)
    SetCameraDistance(22500, 5000)
    Sound(465, 0, 100, 0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2EBF():
        OP_9B(0x1, 0xFE, 0xA, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2EBF)
    OP_D5(0xD, 0x0, 0x2E630, 0x0, 0x7D0)
    WaitChrThread(0xD, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x101, 1400, 0, 21000, 180)
    SetChrPos(0x102, 2450, 0, 20750, 0)
    SetChrPos(0x103, 650, 0, 19750, 0)
    SetChrPos(0x104, 1400, 0, 19250, 0)
    SetChrPos(0x109, 1650, 0, 18250, 0)
    SetChrPos(0x105, 2900, 0, 19750, 0)
    OP_68(1680, 1000, 20360, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18950, 0)

    def lambda_2F9E():
        TurnDirection(0x101, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F9E)
    Sleep(0)

    def lambda_2FAE():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2FAE)
    Sleep(0)

    def lambda_2FBE():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2FBE)
    Sleep(0)

    def lambda_2FCE():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2FCE)
    Sleep(0)

    def lambda_2FDE():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FDE)
    Sleep(0)

    def lambda_2FEE():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FEE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30EE")

    ChrTalk(
        0x104,
        (
            "#00306F#12PStill, I had heard he\x01",
            "was producin' the\x01",
            "stage settings, but...\x02\x03",
            "#00301FConsiderin' that, it doesn't\x01",
            "make you think about a studio\x01",
            "related to the suspicious Society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PRight...\x02",
    )

    CloseMessageWindow()
    Jump("loc_325B")

    label("loc_30EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_316D")

    ChrTalk(
        0x104,
        (
            "#00306F#12P...Hey now, what does that mean?\x02\x03",
            "#00301FThat that old man makes the\x01",
            "Arc-en-ciel stage settings?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E3")

    label("loc_316D")


    ChrTalk(
        0x104,
        (
            "#00306F#12P...Hey now, what does that mean?\x02\x03",
            "#00301FThat the Arc-en-ciel stage\x01",
            "settings are made in this studio?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E3")


    ChrTalk(
        0x103,
        (
            "#00203F#6PIt appears so.\x02\x03",
            "#00201FI had thought that the wire\x01",
            "action too was using quite\x01",
            "the advanced technology...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325B")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...For now, it helps us\x01",
            "that he's not away.\x02\x03",
            "#00013FWe can only ask him to see if...\x01",
            "He'll talk to us about the\x01",
            ""Society" movements or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PHu hu...\x01",
            "Nothing ventured, nothing gained, I guess?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetMapObjFlags(0x2, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, 1400, 0, 21000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x162, 2)
    EventEnd(0x5)
    Return()

    # Function_18_1EAF end

    def Function_19_33BF(): pass

    label("Function_19_33BF")

    OP_93(0xB, 0x0, 0x1F4)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_33E0():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_33E0)
    Sleep(1500)
    Return()

    # Function_19_33BF end

    def Function_20_33F4(): pass

    label("Function_20_33F4")

    OP_95(0xC, 2900, 0, 24300, 2000, 0x0)
    OP_95(0xC, 2900, 0, 18500, 2000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Sound(464, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)

    def lambda_3440():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3440)
    OP_95(0xC, 3900, 500, 18500, 2000, 0x0)
    WaitChrThread(0xC, 3)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x2)
    Return()

    # Function_20_33F4 end

    def Function_21_347D(): pass

    label("Function_21_347D")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 2000, 0, 25000, 0)
    SetChrPos(0x102, 2750, 0, 24750, 0)
    SetChrPos(0x103, 1250, 0, 23750, 0)
    SetChrPos(0x104, 2000, 0, 23250, 0)
    SetChrPos(0x109, 2250, 0, 22250, 0)
    SetChrPos(0x105, 3500, 0, 23750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(2000, 1000, 25000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21200, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Once you visit the doll studio, you\x01",
            "will not be able to visit other areas\x01",
            "outside Crossbell City for today.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Still Have Unfinished Business]\x01",      # 0
            "[Visit the Doll Studio Now]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_363D"),
        (0, "loc_4098"),
        (SWITCH_DEFAULT, "loc_40C4"),
    )


    label("loc_363D")

    OP_68(2000, 1000, 26000, 1500)
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd beat the iron made knocker attached to the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(956, 0, 100, 0)
    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00003F#4S#11P──Excuse us!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#00001F#11PWe're the Crossbell Police,\x01",
            "Special Support Section!\x02\x03",
            "Meister Rosenberg!\x01",
            "Are you inside!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I can hear you even if\x01",
            "you don't shout like that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3936")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears you've come to visit because\x01",
            "you want to ask me something.\x02\x03",
            "I can't spare too much time, but...\x01",
            "I don't mind hearing what you have to \x01",
            "say if it's for a short amount of time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AB8")

    label("loc_3936")

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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You're the Special Support Section?\x01",
            "It appears you've come to visit because\x01",
            "you want to ask me something...\x02\x03",
            "I don't mind hearing what you have to \x01",
            "say if it's for a short amount of time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3AB8")

    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    Fade(500)
    OP_90(0x8, 2000, 0, 38000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_68(1840, 600, 28950, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21340, 0)
    SetCameraDistance(18430, 3500)
    ClearChrFlags(0x8, 0x4)

    def lambda_3B46():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3B46)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12P#NS-So cute...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00112F#12P#NA Rosenberg Doll...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#6P#N...It looks like it is an automata...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Come inside, that little\x01",
            "one will guide you.\x02\x03",
            "See that you don't wander\x01",
            "in unnecessary places, hm?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(2000, 600, 28000, 3000)
    MoveCamera(25, 16, 0, 3000)
    SetCameraDistance(19000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PI-It really seems it\x01",
            "doesn't speak...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PAnyway, you know, I can't really\x01",
            "think it's a mechanical device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12P...So, can you take us\x01",
            "to your master's place?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    OP_68(1850, 1200, 29270, 8000)
    MoveCamera(35, 13, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(24000, 8000)
    ClearChrFlags(0x8, 0x4)
    OP_93(0x8, 0x0, 0x1F4)
    BeginChrThread(0xE, 1, 0, 24)
    OP_96(0x8, 0x7D0, 0x9C4, 0xB572, 0x7D0, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    StopSound(957, 500, 20)
    SetChrFlags(0x8, 0x4)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10112F#12PL-Let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12PR-Right.\x01",
            "Making him wait would be bad too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#12P("Ouroboros"... As expected,\x01",
            "they're an impenetrable enemy.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x0, 1420, 0, 24960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x162, 3)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0xA7, 0x1, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    OP_1B(0x0, 0x0, 0x26)
    OP_24(0x3BD)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_40C4")

    label("loc_4098")

    SetChrPos(0x0, 1600, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_40C4")

    label("loc_40C4")

    Return()

    # Function_21_347D end

    def Function_22_40C5(): pass

    label("Function_22_40C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40E2")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 35)
    Jump("loc_40FA")

    label("loc_40E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40FA")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 23)

    label("loc_40FA")

    Return()

    # Function_22_40C5 end

    def Function_23_40FB(): pass

    label("Function_23_40FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4164")
    SetScenarioFlags(0x168, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sound(957, 2, 40, 0)
    OP_93(0x8, 0x0, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_9B(0x1, 0x8, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(957, 1000, 30)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_10(0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_4164")

    Return()

    # Function_23_40FB end

    def Function_24_4165(): pass

    label("Function_24_4165")

    Sound(957, 2, 40, 0)
    Sleep(1000)
    OP_25(0x3BD, 0x23)
    Sleep(1000)
    OP_25(0x3BD, 0x1E)
    Sleep(1000)
    OP_25(0x3BD, 0x19)
    Sleep(1000)
    OP_25(0x3BD, 0x14)
    Return()

    # Function_24_4165 end

    def Function_25_4188(): pass

    label("Function_25_4188")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 2000, 2500, 48000, 180)
    SetChrPos(0x102, 1250, 2500, 48000, 180)
    SetChrPos(0x103, 2750, 2500, 48000, 180)
    SetChrPos(0x104, 2000, 2500, 48000, 180)
    SetChrPos(0x109, 1500, 2500, 48000, 180)
    SetChrPos(0x105, 250, 2500, 48000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 2000, 2500, 48000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(2000, 3100, 47000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_68(2000, 600, 23000, 15000)
    MoveCamera(45, 25, 0, 15000)
    OP_6E(510, 15000)
    SetCameraDistance(20000, 15000)
    BeginChrThread(0x8, 1, 0, 26)
    Sleep(2000)
    BeginChrThread(0x101, 1, 0, 28)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 29)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 30)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 31)
    Sleep(300)
    BeginChrThread(0x105, 1, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 32)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    BeginChrThread(0x8, 1, 0, 27)
    Sleep(5000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(2250, 600, 22100, 2000)
    MoveCamera(46, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20000, 2000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x109, 0x2)

    def lambda_4455():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4455)
    Sleep(50)

    def lambda_4465():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4465)
    Sleep(50)

    def lambda_4475():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4475)
    Sleep(50)

    def lambda_4485():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4485)
    Sleep(50)

    def lambda_4495():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4495)
    Sleep(50)

    def lambda_44A5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_44A5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00106F#5P...Somehow...\x01",
            "It was like I was having a dream.\x02\x03",
            "#00108FThe "Phantasmal Blaze Plan"...\x01",
            "And the two "Anguis" who're\x01",
            "going to come to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PHonestly speaking, it's too crazy\x01",
            "that seems impossible...\x02\x03",
            "#10101FHow much of that is real, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P...Based on what I heard about the\x01",
            "Liberl Phenomenon, it's certain they\x01",
            "aren't a bunch of guys who joke around.\x02\x03",
            "#00008FHowever, unlike the time with Liberl,\x01",
            "I didn't feel they're trying to devise\x01",
            "something on a large-scale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, the story goes that even a\x01",
            "giant air battleship appeared...\x02\x03",
            "#10302FIt also seems they used that giant\x01",
            "automata called "Pater-Mater".\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4770():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4770)
    Sleep(50)

    def lambda_4780():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4780)
    Sleep(50)

    def lambda_4790():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4790)
    Sleep(50)

    def lambda_47A0():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_47A0)
    Sleep(50)

    def lambda_47B0():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_47B0)
    Sleep(50)

    def lambda_47C0():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_47C0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00011F#11PYou sure know a lot...\x01",
            "Although it's Section One classified intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#11PDo even such rumors spread\x01",
            "when you're working as a host?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#6PHu hu, well, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#11P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00005F#12PYou two, is there something wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_4930():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4930)

    def lambda_493D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_493D)

    def lambda_494A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_494A)

    def lambda_4957():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4957)
    Sleep(50)

    def lambda_4967():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4967)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x103,
        "#00203F#11PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PYeah...something.\x02\x03",
            "#00301FBut it seems peTiote is deeply \x01",
            "thinkin' about something too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P...Yes.\x02\x03",
            "#00201FIt could be so considering the automata\x01",
            "that just guided us, but...\x02\x03",
            "The "Society" appears to be an\x01",
            "organization that plays a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PPlays a lot...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PYes. \x01",
            "Though they have the technological strength to\x01",
            "exceed the ZCF, it is like they are wasting it...\x02\x03",
            "#00201FConsidering that "Pater-Mater", if they can make \x01",
            "such a humanoid weapon with a practical use level,\x01",
            "they could build 50 airships instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PThey could have an abundant\x01",
            "source of fund, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#5P...However, it's true that for an army or a\x01",
            "criminal organization, the organizational form\x01",
            "efficiency is basically seriously important.\x02\x03",
            "#10108FPlaying around... Not doing the utmost to\x01",
            "act cool-headedly towards the objective...\x02\x03",
            "#10101FI can't feel any of that\x01",
            "reasonableness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PI thought the same too.\x02\x03",
            "#00301FRegardless of havin' indeed amazin' technology\x01",
            "and employin' guys who're like monsters...\x02\x03",
            "As a realistic menace, jaegers of the\x01",
            ""Red Constellation" class or a syndicate\x01",
            "like the "Heiyue" could be worse.\x02\x03",
            "#00303FTo say nothing of seriously pickin' a quarrel\x01",
            "with countries like the Empire and Republic.\x01",
            "I can't even picture it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PStill, at present such a force created\x01",
            "an intricate antagonism situation...\x02\x03",
            "#10300FGuys like those from the "Society"\x01",
            "are coming purpose to Crossbell.\x01",
            "The problem is, what're they aiming to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYou're right...\x01",
            "Even their backing up the terrorists\x01",
            "seems to have been a mere whim.\x02\x03",
            "#00101FIt seems they aren't \x01",
            "proactively involved with \x01",
            "realistic power struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIf that is the case...\x01",
            "Could it be they are acting\x01",
            "for an "unrealistic" purpose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThen, as you can imagine we\x01",
            "couldn't do anything 'bout it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PB-But it seems it's\x01",
            "certain  that they're \x01",
            "scheming something...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──At any rate, let's return to \x01",
            "the Support Section for now.\x02\x03",
            "#00001FI want to talk to the Chief and\x01",
            "contact the CGF and Guild too.\x02\x03",
            "No matter what the "Society" intends to do,\x01",
            "we should be able to prepare a minimum.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5273():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5273)
    Sleep(50)

    def lambda_5283():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5283)
    Sleep(50)

    def lambda_5293():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5293)
    Sleep(50)

    def lambda_52A3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_52A3)
    Sleep(50)

    def lambda_52B3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_52B3)
    Sleep(50)

    def lambda_52C3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_52C3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00101F#5PYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#5PThen, let's return to\x01",
            "Crossbell for now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x0, 860, 0, 20820, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 4)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_29(0xA7, 0x1, 0x2)
    OP_29(0xA7, 0x4, 0x10)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_24(0x3BD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_4188 end

    def Function_26_5394(): pass

    label("Function_26_5394")

    Sound(957, 2, 40, 0)

    def lambda_539F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_539F)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, 2000, 0, 24000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 100, 30)
    Sleep(500)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, 3750, 0, 24000, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0x8, 0x40)
    StopSound(957, 500, 30)
    Return()

    # Function_26_5394 end

    def Function_27_5406(): pass

    label("Function_27_5406")

    Sound(957, 2, 40, 0)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, 2000, 0, 25000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 100, 30)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_546F():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_546F)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_5406 end

    def Function_28_54AF(): pass

    label("Function_28_54AF")


    def lambda_54B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_54B4)
    OP_95(0xFE, 2000, 0, 20000, 2000, 0x0)

    def lambda_54D9():

        label("loc_54D9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54D9")

    QueueWorkItem2(0xFE, 2, lambda_54D9)
    Return()

    # Function_28_54AF end

    def Function_29_54E7(): pass

    label("Function_29_54E7")


    def lambda_54EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_54EC)
    OP_95(0xFE, 1000, 0, 20750, 2000, 0x0)

    def lambda_5511():

        label("loc_5511")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5511")

    QueueWorkItem2(0xFE, 2, lambda_5511)
    Return()

    # Function_29_54E7 end

    def Function_30_551F(): pass

    label("Function_30_551F")


    def lambda_5524():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5524)
    OP_95(0xFE, 3000, 0, 21500, 2000, 0x0)

    def lambda_5549():

        label("loc_5549")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5549")

    QueueWorkItem2(0xFE, 2, lambda_5549)
    Return()

    # Function_30_551F end

    def Function_31_5557(): pass

    label("Function_31_5557")


    def lambda_555C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_555C)
    OP_95(0xFE, 2000, 0, 22000, 2000, 0x0)

    def lambda_5581():

        label("loc_5581")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5581")

    QueueWorkItem2(0xFE, 2, lambda_5581)
    Return()

    # Function_31_5557 end

    def Function_32_558F(): pass

    label("Function_32_558F")


    def lambda_5594():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5594)
    OP_95(0xFE, 1500, 0, 23000, 2000, 0x0)

    def lambda_55B9():

        label("loc_55B9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_55B9")

    QueueWorkItem2(0xFE, 2, lambda_55B9)
    Return()

    # Function_32_558F end

    def Function_33_55C7(): pass

    label("Function_33_55C7")


    def lambda_55CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_55CC)
    OP_95(0xFE, 0, 0, 22000, 2000, 0x0)

    def lambda_55F1():

        label("loc_55F1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_55F1")

    QueueWorkItem2(0xFE, 2, lambda_55F1)
    Return()

    # Function_33_55C7 end

    def Function_34_55FF(): pass

    label("Function_34_55FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    SetChrPos(0x101, 2000, 0, 16000, 0)
    SetChrPos(0x103, 2750, 0, 14750, 0)
    SetChrPos(0x106, 1250, 0, 13750, 0)
    SetChrPos(0x105, 2000, 0, 13250, 0)
    SetChrPos(0x107, 3500, 0, 13750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_5678():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5678)
    Sleep(100)

    def lambda_5690():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5690)
    Sleep(100)

    def lambda_56A8():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_56A8)
    Sleep(100)

    def lambda_56C0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56C0)
    Sleep(100)

    def lambda_56D8():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_56D8)
    OP_68(2000, 2900, 39350, 0)
    MoveCamera(25, 5, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32549, 0)
    MoveCamera(45, 20, 0, 6000)
    OP_68(2420, 1000, 25710, 6000)
    SetCameraDistance(21210, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell then...\x01",
            "I hope he's not out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PConsidering the situation, I don't\x01",
            "think he went anywhere...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hm, I haven't.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PWoah....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#12P...A voice pipe?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I thought it would be time\x01",
            "for you to show up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    Fade(500)
    OP_90(0x8, 2000, 0, 38000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_68(1990, 600, 29050, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21340, 0)
    SetCameraDistance(18430, 3500)
    ClearChrFlags(0x8, 0x4)

    def lambda_59AC():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_59AC)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    ChrTalk(
        0x106,
        "#10712F#6P#N......!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10400F#6P#NIt's a guide doll, you know.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Come inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 0, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I shouldn't remind you, but if\x01",
            "you get away from that little one,\x01",
            "I won't guarantee for your safety.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(2000, 600, 28000, 0)
    MoveCamera(25, 16, 0, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    OP_68(1850, 1200, 29270, 8000)
    MoveCamera(35, 13, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(24000, 8000)
    BeginChrThread(0xE, 1, 0, 24)
    ClearChrFlags(0x8, 0x4)
    OP_93(0x8, 0x0, 0x1F4)
    OP_96(0x8, 0x7D0, 0x9C4, 0xB572, 0x7D0, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 300, 20)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10710F#12P...Uuhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#12P#3CHmph...same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI-In any case, this\x01",
            "will save us time.\x02\x03",
            "#00000FLet's impose on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PRight.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x0, 1250, 0, 24610, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x2)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    SetScenarioFlags(0x1A2, 1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_24(0x3BD)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_34_55FF end

    def Function_35_5D40(): pass

    label("Function_35_5D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DA9")
    SetScenarioFlags(0x1AB, 7)
    ModifyEventFlags(0, 0, 0x80)
    Sound(957, 2, 40, 0)
    OP_93(0x8, 0x0, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_9B(0x1, 0x8, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(957, 1000, 30)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_10(0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_5DA9")

    Return()

    # Function_35_5D40 end

    def Function_36_5DAA(): pass

    label("Function_36_5DAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(2000, 600, 24500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2000, 0, 20000, 0)
    SetChrPos(0x103, 1000, 0, 20750, 0)
    SetChrPos(0x106, 3000, 0, 21500, 0)
    SetChrPos(0x105, 2000, 0, 22300, 0)
    SetChrPos(0x107, -500, 0, 20500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    SetChrPos(0x8, 2000, 0, 25000, 180)
    OP_68(2000, 600, 23000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 37)
    Sleep(5000)
    OP_68(2000, 800, 21000, 2000)
    MoveCamera(46, 20, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(18500, 2000)
    SetChrFlags(0x107, 0x20)

    def lambda_5F35():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5F35)
    Sleep(50)

    def lambda_5F45():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5F45)
    Sleep(50)

    def lambda_5F55():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5F55)
    Sleep(50)

    def lambda_5F65():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5F65)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00204F#6PI thought we had been lucky\x01",
            "since he listened to us, but...\x02\x03",
            "#00202FIt was outside my expectations\x01",
            "that he would have even helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PYeah. It seems they all have their\x01",
            "different circumstances in the "Society".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PWell, that's exactly why it's an organization\x01",
            "you can't grasp the truth of.\x02\x03",
            "#10400FHowever, regarding that old man,\x01",
            "it doesn't seem a problem to trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11P...You're right.\x01",
            "It seems he has his reasons too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CIf it's Jｶrg, in time he'll bring\x01",
            "us beneficial information.\x02\x03",
            "#01200FWell, let's wait for him to contact us\x01",
            "without excessive expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PYeah, we'll do like that.\x02\x03",
            "#00000F──Well then, it's time to head\x01",
            "towards the mining town.\x02\x03",
            "I'd like to look into the\x01",
            "Resistance moves too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702F#11PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#5PThen, shall we go?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x0, 480, 0, 19570, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 2)
    OP_29(0xAF, 0x1, 0x9)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_24(0x3BD)
    EventEnd(0x5)
    Return()

    # Function_36_5DAA end

    def Function_37_6320(): pass

    label("Function_37_6320")

    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_6337():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6337)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_6320 end

    def Function_38_6377(): pass

    label("Function_38_6377")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe can't make the Meister\x01",
            "wait too much for us.\x01",
            "Let's enter the studio now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 830, 0, -1070, 0)
    EventEnd(0x4)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_38_6377 end

    SaveToFile()

Try(main)
