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
        "Function_4_757",          # 04, 4
        "Function_5_795",          # 05, 5
        "Function_6_7A2",          # 06, 6
        "Function_7_1C9D",         # 07, 7
        "Function_8_1CBF",         # 08, 8
        "Function_9_1CE1",         # 09, 9
        "Function_10_1D03",        # 0A, 10
        "Function_11_1D25",        # 0B, 11
        "Function_12_1D3C",        # 0C, 12
        "Function_13_1D56",        # 0D, 13
        "Function_14_1D70",        # 0E, 14
        "Function_15_1D8A",        # 0F, 15
        "Function_16_1DB3",        # 10, 16
        "Function_17_1DDC",        # 11, 17
        "Function_18_1E3C",        # 12, 18
        "Function_19_332B",        # 13, 19
        "Function_20_3360",        # 14, 20
        "Function_21_33E9",        # 15, 21
        "Function_22_3FDD",        # 16, 22
        "Function_23_4013",        # 17, 23
        "Function_24_407D",        # 18, 24
        "Function_25_40A0",        # 19, 25
        "Function_26_5244",        # 1A, 26
        "Function_27_52B6",        # 1B, 27
        "Function_28_535F",        # 1C, 28
        "Function_29_5397",        # 1D, 29
        "Function_30_53CF",        # 1E, 30
        "Function_31_5407",        # 1F, 31
        "Function_32_543F",        # 20, 32
        "Function_33_5477",        # 21, 33
        "Function_34_54AF",        # 22, 34
        "Function_35_5C0F",        # 23, 35
        "Function_36_5C79",        # 24, 36
        "Function_37_6203",        # 25, 37
        "Function_38_625A",        # 26, 38
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
            "   Rosenberg Studio\x01",
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

    def Function_4_757(): pass

    label("Function_4_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_769")
    Call(0, 21)
    Return()

    label("loc_769")

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

    # Function_4_757 end

    def Function_5_795(): pass

    label("Function_5_795")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_795 end

    def Function_6_7A2(): pass

    label("Function_6_7A2")

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
            "Leave. I don't intend to let you\x01",
            "in.\x02\x03",
            "Even if you are the Thirteen\x01",
            "Workshops supervisor, you've no\x01",
            "right to enter.\x02",
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
            "...Huhu, very well then.\x02\x03",
            "That's No. XV's property. I don't\x01",
            "intend to take it away.\x02\x03",
            "However, Meister? Can you hand me\x01",
            "the data?\x02\x03",
            "That is "His" will, after all.\x02",
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
            "#03903F#5P...Hmph. You don't need\x01",
            "to tell me that.\x02",
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
            "#3701V#30WUhuhu, we don't get along very\x01",
            "well, do we.\x02\x03",
            "#3702VKnowing the professor hates you\x01",
            "too, you came to visit anyway.\x02",
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
            "#04709F#11PHaha. What are you saying?\x02\x03",
            "#04702FThe Meister and I are old\x01",
            "friends.\x02\x03",
            "Especially in regard to doll\x01",
            "making, we're tied by a solid\x01",
            "teacher-student bond, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHmph, stop the nonsense.\x02\x03",
            "#03900FAfter all, from the\x01",
            "society's point of view, my\x01",
            "skills are old-fashioned.\x02\x03",
            "With your Integration\x01",
            "Theory, you've no need to\x01",
            "rely on me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PHuhu, how modest.\x02\x03",
            "No one in this world can\x01",
            "surpass you when it comes\x01",
            "to doll making, Meister.\x02\x03",
            "#04705FAh, but could I have that\x01",
            "circuit you added to\x01",
            "Pater-Mater?\x02\x03",
            "#04703FIf not, our Angel of\x01",
            "Slaughter's potential\x01",
            "will go to waste...\x02",
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
        "#5PUmm, excuse us.\x02",
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

    def lambda_10AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10AA)
    Sleep(50)

    def lambda_10BA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10BA)
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
            "#04805F#5PHuh? It looks like we\x01",
            "have guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5P...Campanella. Your\x01",
            "business is done.\x02\x03",
            "#03900FTake that unpleasant man\x01",
            "with you and leave.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11C1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11C1)
    Sleep(50)

    def lambda_11D1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11D1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#04804F#12PUhuhu. Understood.\x02\x03",
            "#04802FCome now, professor. We\x01",
            "must be going.\x02\x03",
            "You want to finish things\x01",
            "today and go back to the\x01",
            "laboratory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PHoho, but of course.\x02\x03",
            "#04702FThen, Meister... I'll\x01",
            "excuse myself.\x02\x03",
            "Please check those\x01",
            "little guys as soon as\x01",
            "they're completed, hmm?\x02",
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
            "#03901F#5P#4SShut up! Get out of\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#04809F#12P#3703V#30WUhuhu. See you.\x02",
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
        "#03900F#5P...What foolishness.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F5")

    ChrTalk(
        0x101,
        "#00006F#12PE-Excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PThank you for back\x01",
            "then... It has been a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PThe Special Support\x01",
            "Section, eh? It's been a\x01",
            "while.\x02\x03",
            "#03900FRenne has left for\x01",
            "Liberl. What do you want\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170B")

    label("loc_15F5")


    ChrTalk(
        0x101,
        (
            "#00006F#12PE-Excuse us.\x02\x03",
            "#00000F...Nice to meet you. We're\x01",
            "the Crossbell Police's\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PRosenberg Studio owner\x01",
            "Meister Jｶrg, I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHmph, so you've heard\x01",
            "from Renne.\x02\x03",
            "#03900FRenne has left for\x01",
            "Liberl. What do you\x01",
            "want?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170B")


    ChrTalk(
        0x101,
        (
            "#00012F#12PWell, we were in the\x01",
            "area so we just wanted\x01",
            "to pay you a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PUmm... Sorry for coming\x01",
            "when you had guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03901F#5PHmph, they were\x01",
            "uninvited guests. Pay it\x01",
            "no mind.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(250)

    ChrTalk(
        0xB,
        (
            "#03903F#11PHowever, I don't have\x01",
            "anything in particular\x01",
            "to tell you right now.\x02\x03",
            "If you have other\x01",
            "business, you can come\x01",
            "visit again.\x02\x03",
            "#03900FI'll at least hear what\x01",
            "you have to say out of\x01",
            "deference for Renne.\x02",
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
        (
            "#10105F#12PT-The gate closed on its\x01",
            "own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PHmm. It's old, but maybe\x01",
            "it's got some kind of\x01",
            "mechanism?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AD4")

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah... After all, it's a\x01",
            "place where incredible\x01",
            "mechanized dolls are made.\x02\x03",
            "#00008FAlso... His guests earlier\x01",
            "worry me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B5A")

    label("loc_1AD4")


    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, like we heard from\x01",
            "Renne, it doesn't seem to\x01",
            "be a mere doll studio.\x02\x03",
            "#00008FAlso... His guests\x01",
            "earlier worry me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5A")

    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00103F#11PYes, but he called them\x01",
            "uninvited guests...\x02\x03",
            "#00108FHow to put it... They\x01",
            "were very suspicious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10106F#6PHmm...\x02\x03",
            "#10100FWell, they didn't look\x01",
            "dangerous, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12P(...Haha. They didn't\x01",
            "look dangerous, eh?)\x02",
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

    # Function_6_7A2 end

    def Function_7_1C9D(): pass

    label("Function_7_1C9D")

    OP_9B(0x0, 0xFE, 0x4, 0x36B0, 0x7D0, 0x0)

    def lambda_1CB1():

        label("loc_1CB1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1CB1")

    QueueWorkItem2(0xFE, 2, lambda_1CB1)
    Return()

    # Function_7_1C9D end

    def Function_8_1CBF(): pass

    label("Function_8_1CBF")

    OP_9B(0x0, 0xFE, 0x5, 0x3BC4, 0x7D0, 0x0)

    def lambda_1CD3():

        label("loc_1CD3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1CD3")

    QueueWorkItem2(0xFE, 2, lambda_1CD3)
    Return()

    # Function_8_1CBF end

    def Function_9_1CE1(): pass

    label("Function_9_1CE1")

    OP_9B(0x0, 0xFE, 0x6, 0x38A4, 0x7D0, 0x0)

    def lambda_1CF5():

        label("loc_1CF5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1CF5")

    QueueWorkItem2(0xFE, 2, lambda_1CF5)
    Return()

    # Function_9_1CE1 end

    def Function_10_1D03(): pass

    label("Function_10_1D03")

    OP_9B(0x0, 0xFE, 0x6, 0x3C8C, 0x7D0, 0x0)

    def lambda_1D17():

        label("loc_1D17")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1D17")

    QueueWorkItem2(0xFE, 2, lambda_1D17)
    Return()

    # Function_10_1D03 end

    def Function_11_1D25(): pass

    label("Function_11_1D25")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_11_1D25 end

    def Function_12_1D3C(): pass

    label("Function_12_1D3C")

    Sleep(50)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xE10, 0x7D0, 0x0)
    Return()

    # Function_12_1D3C end

    def Function_13_1D56(): pass

    label("Function_13_1D56")

    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_13_1D56 end

    def Function_14_1D70(): pass

    label("Function_14_1D70")

    Sleep(150)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_14_1D70 end

    def Function_15_1D8A(): pass

    label("Function_15_1D8A")

    Sleep(50)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_15_1D8A end

    def Function_16_1DB3(): pass

    label("Function_16_1DB3")

    Sleep(250)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_16_1DB3 end

    def Function_17_1DDC(): pass

    label("Function_17_1DDC")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)

    def lambda_1E11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_17_1DDC end

    def Function_18_1E3C(): pass

    label("Function_18_1E3C")

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

    def lambda_1FB1():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FB1)
    Sleep(10)

    def lambda_1FC9():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FC9)
    Sleep(10)

    def lambda_1FE1():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FE1)
    Sleep(10)

    def lambda_1FF9():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FF9)
    Sleep(10)

    def lambda_2011():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2011)
    Sleep(10)

    def lambda_2029():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2029)
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
        "#00205F#12PA transport truck?\x02",
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
            "#12PIt seems we'll make it\x01",
            "in time for the public\x01",
            "performance in two days!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHonestly... When it comes to\x01",
            "your troupe, your requests are\x01",
            "too demanding every single time.\x02\x03",
            "Not only the automatas' tuning,\x01",
            "but also the ordering of a new\x01",
            "stage setting...\x02\x03",
            "#03901FI'm busy, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAhaha... We're terribly\x01",
            "sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAnyhow, the requests from\x01",
            "Miss Ilya and the troupe\x01",
            "chief are taxing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAnd in the end, they even\x01",
            "made an additional order\x01",
            "for that kind of device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03900F#5PHmph, well, whatever.\x02\x03",
            "#03903F...Making use of my studio's\x01",
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
            "#12PWe've been inviting you for a long\x01",
            "time, and we'd really like you to see\x01",
            "an Arc-en-Ciel performance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAlso, you always provide us\x01",
            "with outstanding automatas\x01",
            "and stage settings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PI'm getting a suitable\x01",
            "amount of mira.\x02\x03",
            "#03900F...I'm busy. I'll accept\x01",
            "just your thoughts.\x02",
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

    def lambda_25A0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25A0)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    WaitChrThread(0xC, 1)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#12P...*sigh*. I knew he\x01",
            "wouldn't accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PI'd like him to see how\x01",
            "his stage settings are\x01",
            "used at least once, but...\x02",
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

    def lambda_2687():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2687)
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

    def lambda_2728():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2728)
    Sleep(50)

    def lambda_2740():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2740)
    Sleep(50)

    def lambda_2758():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2758)
    Sleep(50)

    def lambda_2770():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2770)
    Sleep(50)

    def lambda_2788():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2788)
    Sleep(50)

    def lambda_27A0():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_27A0)
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
            "#5POh... Aren't you the\x01",
            "Special Support Section?\x02",
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
            "#00100F#12PYou're the Arc-en-Ciel\x01",
            "engineer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, my name is Heintz.\x01",
            "I'm in charge of the\x01",
            "stage settings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PFancy meeting you here.\x01",
            "Do you need something\x01",
            "from the meister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PY-Yes, we'd like to\x01",
            "consult with him about\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12PDid you come to get\x01",
            "equipment for the stage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, we him asked to tune\x01",
            "our automatas and to make a\x01",
            "new stage setting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt was an unreasonable schedule for\x01",
            "the renewal performance, but he got\x01",
            "through all of it for us somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMaaan, all the troupe\x01",
            "members are really\x01",
            "indebted to the meister.\x02",
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
            "#00309F#12PBy the way, opening day of the\x01",
            "Arc-en-Ciel renewal performance\x01",
            "is the day after tomorrow, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes. Starting from Miss Ilya,\x01",
            "all our members are fired up\x01",
            "like never before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI feel tense too even\x01",
            "just being in charge of\x01",
            "the stage setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHehe, it seems it'll be\x01",
            "an amazing play for\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POops, I can't stay here.\x01",
            "I've got to get back and\x01",
            "get started setting up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P─See you everyone!\x01",
            "Please come visit our\x01",
            "theatre!\x02",
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

    def lambda_2CD4():
        OP_9B(0x1, 0xFE, 0xE6, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CD4)
    BeginChrThread(0xC, 1, 0, 20)
    OP_68(2900, 1000, 18300, 5000)
    SetCameraDistance(21500, 5000)

    def lambda_2D09():

        label("loc_2D09")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D09")

    QueueWorkItem2(0x101, 2, lambda_2D09)

    def lambda_2D1B():

        label("loc_2D1B")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D1B")

    QueueWorkItem2(0x102, 2, lambda_2D1B)

    def lambda_2D2D():

        label("loc_2D2D")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D2D")

    QueueWorkItem2(0x103, 2, lambda_2D2D)

    def lambda_2D3F():

        label("loc_2D3F")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D3F")

    QueueWorkItem2(0x104, 2, lambda_2D3F)

    def lambda_2D51():

        label("loc_2D51")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D51")

    QueueWorkItem2(0x109, 2, lambda_2D51)

    def lambda_2D63():

        label("loc_2D63")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2D63")

    QueueWorkItem2(0x105, 2, lambda_2D63)
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

    def lambda_2DAA():

        label("loc_2DAA")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2DAA")

    QueueWorkItem2(0x101, 2, lambda_2DAA)

    def lambda_2DBC():

        label("loc_2DBC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2DBC")

    QueueWorkItem2(0x102, 2, lambda_2DBC)

    def lambda_2DCE():

        label("loc_2DCE")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2DCE")

    QueueWorkItem2(0x103, 2, lambda_2DCE)

    def lambda_2DE0():

        label("loc_2DE0")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2DE0")

    QueueWorkItem2(0x104, 2, lambda_2DE0)

    def lambda_2DF2():

        label("loc_2DF2")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2DF2")

    QueueWorkItem2(0x109, 2, lambda_2DF2)

    def lambda_2E04():

        label("loc_2E04")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2E04")

    QueueWorkItem2(0x105, 2, lambda_2E04)
    OP_68(2900, 1000, 10300, 5000)
    SetCameraDistance(22500, 5000)
    Sound(465, 0, 100, 0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2E42():
        OP_9B(0x1, 0xFE, 0xA, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E42)
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

    def lambda_2F21():
        TurnDirection(0x101, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F21)
    Sleep(0)

    def lambda_2F31():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F31)
    Sleep(0)

    def lambda_2F41():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2F41)
    Sleep(0)

    def lambda_2F51():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2F51)
    Sleep(0)

    def lambda_2F61():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F61)
    Sleep(0)

    def lambda_2F71():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2F71)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_306E")

    ChrTalk(
        0x104,
        (
            "#00306F#12PI heard he was producin' the stage\x01",
            "settings, but...\x02\x03",
            "#00301FSomethin' like that almost makes you\x01",
            "think he's not connected to some\x01",
            "suspicious society or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PRight...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DF")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_30ED")

    ChrTalk(
        0x104,
        (
            "#00306F#12P...Hey now, what does\x01",
            "that mean?\x02\x03",
            "#00301FThat that old man makes\x01",
            "the Arc-en-Ciel stage\x01",
            "settings?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3166")

    label("loc_30ED")


    ChrTalk(
        0x104,
        (
            "#00306F#12P...Hey now, what does\x01",
            "that mean?\x02\x03",
            "#00301FYou're tellin' me the\x01",
            "Arc-en-Ciel stage\x01",
            "settings are made here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3166")


    ChrTalk(
        0x103,
        (
            "#00203F#6PIt appears so.\x02\x03",
            "#00201FWith the wire-action they\x01",
            "use, I thought it was rather\x01",
            "advanced technology, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31DF")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Well at least he's not\x01",
            "away.\x02\x03",
            "#00013FWill he tell us about the\x01",
            "actions of Ouroboros? Anyway,\x01",
            "all we can do is ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PHehe... Nothing\x01",
            "ventured, nothing\x01",
            "gained, I guess?\x02",
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

    # Function_18_1E3C end

    def Function_19_332B(): pass

    label("Function_19_332B")

    OP_93(0xB, 0x0, 0x1F4)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_334C():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_334C)
    Sleep(1500)
    Return()

    # Function_19_332B end

    def Function_20_3360(): pass

    label("Function_20_3360")

    OP_95(0xC, 2900, 0, 24300, 2000, 0x0)
    OP_95(0xC, 2900, 0, 18500, 2000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Sound(464, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)

    def lambda_33AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_33AC)
    OP_95(0xC, 3900, 500, 18500, 2000, 0x0)
    WaitChrThread(0xC, 3)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x2)
    Return()

    # Function_20_3360 end

    def Function_21_33E9(): pass

    label("Function_21_33E9")

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
            "※Once you visit the Doll Studio, you\x01",
            "will not be able to visit areas outside\x01",
            "Crossbell City for the rest of the day.\x07\x00\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Visit the Doll Studio Now]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_35AA"),
        (0, "loc_3FB0"),
        (SWITCH_DEFAULT, "loc_3FDC"),
    )


    label("loc_35AA")

    OP_68(2000, 1000, 26000, 1500)
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd used the door's\x01",
            "iron knocker.\x07\x00\x02",
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
        "#00003F#4S#11P─Excuse us!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#00001F#11PCrossbell Police,\x01",
            "Special Support Section!\x02\x03",
            "Meister Rosenberg! Are\x01",
            "you inside!?\x02",
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
            "...I can hear you even\x01",
            "if you don't shout like\x01",
            "that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3872")
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
            "It appears you're here because you\x01",
            "want to ask me something.\x02\x03",
            "I can't spare much time, but... I\x01",
            "don't mind hearing what you have to\x01",
            "say if it's only for a short while.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_39EC")

    label("loc_3872")

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
            "The Special Support\x01",
            "Section, huh.\x02\x03",
            "It appears you've come to\x01",
            "visit because you want to\x01",
            "ask me something.\x02\x03",
            "I don't mind hearing what\x01",
            "you have to say if it's\x01",
            "only for a short while.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_39EC")

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

    def lambda_3A7A():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A7A)
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
        "#10109F#12P#NS-So cute!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00112F#12P#NA Rosenberg Doll!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00205F#6P#N...It looks like it's an\x01",
            "automaton...\x02",
        )
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
            "Come inside. That little\x01",
            "one will guide you.\x02\x03",
            "See that you don't\x01",
            "wander anywhere\x01",
            "unnecessary, hm?\x07\x00\x02",
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
            "#00012F#12PI-It looks like it\x01",
            "really doesn't speak?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PBut, well, I can't\x01",
            "really think it's a\x01",
            "machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12P...So, are you taking us\x01",
            "to your master?\x02",
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
            "#00106F#12PR-Right. We shouldn't\x01",
            "make him wait, either...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#12P(Ouroboros... As\x01",
            "expected, they're an\x01",
            "impenetrable enemy.)\x02",
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
    Jump("loc_3FDC")

    label("loc_3FB0")

    SetChrPos(0x0, 1600, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_3FDC")

    label("loc_3FDC")

    Return()

    # Function_21_33E9 end

    def Function_22_3FDD(): pass

    label("Function_22_3FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FFA")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 35)
    Jump("loc_4012")

    label("loc_3FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4012")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 23)

    label("loc_4012")

    Return()

    # Function_22_3FDD end

    def Function_23_4013(): pass

    label("Function_23_4013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407C")
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

    label("loc_407C")

    Return()

    # Function_23_4013 end

    def Function_24_407D(): pass

    label("Function_24_407D")

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

    # Function_24_407D end

    def Function_25_40A0(): pass

    label("Function_25_40A0")

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

    def lambda_436D():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_436D)
    Sleep(50)

    def lambda_437D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_437D)
    Sleep(50)

    def lambda_438D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_438D)
    Sleep(50)

    def lambda_439D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_439D)
    Sleep(50)

    def lambda_43AD():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43AD)
    Sleep(50)

    def lambda_43BD():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_43BD)
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
            "#00106F#5P...Somehow... It was like I\x01",
            "was having a dream.\x02\x03",
            "#00108FThe "Phantasmal Blaze Plan"...\x01",
            "And the two Anguis who are\x01",
            "going to come to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PHonestly speaking, it's\x01",
            "so crazy that it seems\x01",
            "impossible...\x02\x03",
            "#10101FHow much of that is\x01",
            "real, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P...Based on what I heard about the\x01",
            "Liberl Phenomenon, it's certain they\x01",
            "aren't a bunch of guys who joke around.\x02\x03",
            "#00008FHowever, unlike in Liberl, I don't feel\x01",
            "like they're trying to devise something\x01",
            "on a grand scale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, the story goes\x01",
            "that even a giant air\x01",
            "battleship appeared...\x02\x03",
            "#10302FIt also seems they used\x01",
            "that giant automata\x01",
            "called Pater-Mater.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4680():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4680)
    Sleep(50)

    def lambda_4690():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4690)
    Sleep(50)

    def lambda_46A0():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_46A0)
    Sleep(50)

    def lambda_46B0():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46B0)
    Sleep(50)

    def lambda_46C0():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46C0)
    Sleep(50)

    def lambda_46D0():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_46D0)
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
            "Although it's Section\x01",
            "One classified intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#11PDo you hear even rumors\x01",
            "like that when you're\x01",
            "working as a host?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#6PHehe, well, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#11P...............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#12PYou two, is there\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_484C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_484C)

    def lambda_4859():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4859)

    def lambda_4866():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4866)

    def lambda_4873():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4873)
    Sleep(50)

    def lambda_4883():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4883)
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
            "#00306F#5PYeah... just a little\x01",
            "somethin'.\x02\x03",
            "#00301FBut it looks like\x01",
            "PeTiote is thinkin'\x01",
            "about somethin' else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P...Yes.\x02\x03",
            "#00201FIt's true of the doll that\x01",
            "guided us just now as\x01",
            "well...\x02\x03",
            "Ouroboros appears to be an\x01",
            "organization that plays\x01",
            "around an awful lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PPlays around a lot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PYes. Even though they have technological\x01",
            "strength exceeding the Epstein Foundation\x01",
            "and ZCF, it's like they're wasting it...\x02\x03",
            "#00201FIf they're advanced enough to make a\x01",
            "humanoid weapon like that Pater-Mater, it\x01",
            "seems they could easily make 50 airships.\x02",
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
            "#00108F#6PThey could have an\x01",
            "abundant source of\x01",
            "funds, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#5P...But for an army or crime syndicate,\x01",
            "efficiency of their organizational\x01",
            "structure is fundamentally important.\x02\x03",
            "#10108FPlaying around... Not doing the utmost\x01",
            "to act cool-headedly towards the\x01",
            "objective...\x02\x03",
            "#10101FI can't feel any of that\x01",
            "reasonableness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PI feel the same.\x02\x03",
            "#00301FRegardless of havin' amazin' tech and\x01",
            "employin' those monster-like guys...\x02\x03",
            "Red Constellation-class jaegers or\x01",
            "crime syndicates like Heiyue might be\x01",
            "more realistic threats.\x02\x03",
            "#00303FTo say nothing of direct confrontation\x01",
            "with major powers like the Empire and\x01",
            "Republic. I can't even imagine it.\x02",
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
            "#10304F#5PStill, in the current\x01",
            "situation created by all those\x01",
            "opposing forces...\x02\x03",
            "#10300FThe problem is what Ouroboros\x01",
            "is trying to achieve by coming\x01",
            "to Crossbell specifically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYou're right... Even their\x01",
            "support of the terrorists seems\x01",
            "to have been a mere whim.\x02\x03",
            "#00101FIt seems they aren't actively\x01",
            "involved in realistic power\x01",
            "struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIn that case... Could\x01",
            "they be acting for an\x01",
            ""unrealistic" purpose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PIf so, then it looks\x01",
            "like there's not much we\x01",
            "can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PB-But it seems certain\x01",
            "they're planning\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P─Anyhow, let's return to the\x01",
            "Support Section for now.\x02\x03",
            "#00001FI want to talk to chief and contact\x01",
            "the CGF and Guild too.\x02\x03",
            "No matter what Ouroboros is\x01",
            "planning, there should be something\x01",
            "we can do to be ready for it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_511E():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_511E)
    Sleep(50)

    def lambda_512E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_512E)
    Sleep(50)

    def lambda_513E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_513E)
    Sleep(50)

    def lambda_514E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_514E)
    Sleep(50)

    def lambda_515E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_515E)
    Sleep(50)

    def lambda_516E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_516E)
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
            "Crossbell City for now.\x02",
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

    # Function_25_40A0 end

    def Function_26_5244(): pass

    label("Function_26_5244")

    Sound(957, 2, 40, 0)

    def lambda_524F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_524F)
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

    # Function_26_5244 end

    def Function_27_52B6(): pass

    label("Function_27_52B6")

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

    def lambda_531F():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_531F)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_52B6 end

    def Function_28_535F(): pass

    label("Function_28_535F")


    def lambda_5364():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5364)
    OP_95(0xFE, 2000, 0, 20000, 2000, 0x0)

    def lambda_5389():

        label("loc_5389")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5389")

    QueueWorkItem2(0xFE, 2, lambda_5389)
    Return()

    # Function_28_535F end

    def Function_29_5397(): pass

    label("Function_29_5397")


    def lambda_539C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_539C)
    OP_95(0xFE, 1000, 0, 20750, 2000, 0x0)

    def lambda_53C1():

        label("loc_53C1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53C1")

    QueueWorkItem2(0xFE, 2, lambda_53C1)
    Return()

    # Function_29_5397 end

    def Function_30_53CF(): pass

    label("Function_30_53CF")


    def lambda_53D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_53D4)
    OP_95(0xFE, 3000, 0, 21500, 2000, 0x0)

    def lambda_53F9():

        label("loc_53F9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53F9")

    QueueWorkItem2(0xFE, 2, lambda_53F9)
    Return()

    # Function_30_53CF end

    def Function_31_5407(): pass

    label("Function_31_5407")


    def lambda_540C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_540C)
    OP_95(0xFE, 2000, 0, 22000, 2000, 0x0)

    def lambda_5431():

        label("loc_5431")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5431")

    QueueWorkItem2(0xFE, 2, lambda_5431)
    Return()

    # Function_31_5407 end

    def Function_32_543F(): pass

    label("Function_32_543F")


    def lambda_5444():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5444)
    OP_95(0xFE, 1500, 0, 23000, 2000, 0x0)

    def lambda_5469():

        label("loc_5469")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5469")

    QueueWorkItem2(0xFE, 2, lambda_5469)
    Return()

    # Function_32_543F end

    def Function_33_5477(): pass

    label("Function_33_5477")


    def lambda_547C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_547C)
    OP_95(0xFE, 0, 0, 22000, 2000, 0x0)

    def lambda_54A1():

        label("loc_54A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_54A1")

    QueueWorkItem2(0xFE, 2, lambda_54A1)
    Return()

    # Function_33_5477 end

    def Function_34_54AF(): pass

    label("Function_34_54AF")

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

    def lambda_5528():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5528)
    Sleep(100)

    def lambda_5540():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5540)
    Sleep(100)

    def lambda_5558():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5558)
    Sleep(100)

    def lambda_5570():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5570)
    Sleep(100)

    def lambda_5588():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5588)
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
            "#00006F#11PWell then... I hope he's\x01",
            "still home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PConsidering the\x01",
            "situation, I don't think\x01",
            "he's gone anywhere...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, I haven't.\x07\x00\x02",
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
        "#00011F#12PWha...\x02",
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
            "I thought you might show\x01",
            "up around now.\x07\x00\x02",
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

    def lambda_5858():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5858)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    ChrTalk(
        0x106,
        "#10712F#6P#N...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10400F#6P#NIt's a guide doll, you\x01",
            "know.\x02",
        )
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
            "I shouldn't need to remind you, but\x01",
            "if you stray away from that little\x01",
            "one, I can't guarantee your safety.\x07\x00\x02",
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
        "#10710F#12P...Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CHmph... Quite the\x01",
            "cautious one, as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI-In any case, this'll\x01",
            "save us time.\x02\x03",
            "#00000FLet's make the best of\x01",
            "this chance.\x02",
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

    # Function_34_54AF end

    def Function_35_5C0F(): pass

    label("Function_35_5C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C78")
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

    label("loc_5C78")

    Return()

    # Function_35_5C0F end

    def Function_36_5C79(): pass

    label("Function_36_5C79")

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

    def lambda_5E04():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5E04)
    Sleep(50)

    def lambda_5E14():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5E14)
    Sleep(50)

    def lambda_5E24():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5E24)
    Sleep(50)

    def lambda_5E34():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5E34)
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
            "#00204F#6PI thought we lucked out since\x01",
            "he actually listened to us,\x01",
            "but...\x02\x03",
            "#00202FIt was outside my expectations\x01",
            "that he would have even\x01",
            "provided assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PYeah. It seems they all\x01",
            "have their different\x01",
            "circumstances in Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PWell, that's exactly why\x01",
            "it's an organization you\x01",
            "can't grasp the truth of.\x02\x03",
            "#10400FHowever, regarding that old\x01",
            "man, it doesn't seem like a\x01",
            "bad idea to trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11P...You're right. He has\x01",
            "his own reasons too, it\x01",
            "seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CIf it's Jｶrg, he'll\x01",
            "bring us beneficial\x01",
            "information in time.\x02\x03",
            "#01200FWell, let's wait for him\x01",
            "to contact us without\x01",
            "expecting too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PYeah, let's.\x02\x03",
            "#00000F─Well then, it's time to\x01",
            "head for the mining\x01",
            "town.\x02\x03",
            "I'd like to look into\x01",
            "the actions of the\x01",
            "resistance as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702F#11PUnderstood.\x02",
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

    # Function_36_5C79 end

    def Function_37_6203(): pass

    label("Function_37_6203")

    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_621A():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_621A)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_6203 end

    def Function_38_625A(): pass

    label("Function_38_625A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe can't make the Meister\x01",
            "wait too long for us. Let's\x01",
            "enter the studio now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 830, 0, -1070, 0)
    EventEnd(0x4)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_38_625A end

    SaveToFile()

Try(main)
