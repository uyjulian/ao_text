from ScenarioHelper import *

def main():
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
        "Guide doll",               # 1
        "A man in white robe",               # 2
        "boy",                   # 3
        "Jorgg Aged",             # 4
        "Heinz",               # 5
        "car",                     # 6
        "SE control",                 # 7
        "Mainz Mountain Road",           # 8
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
        "Function_4_762",          # 04, 4
        "Function_5_7A0",          # 05, 5
        "Function_6_7AD",          # 06, 6
        "Function_7_1BF8",         # 07, 7
        "Function_8_1C1A",         # 08, 8
        "Function_9_1C3C",         # 09, 9
        "Function_10_1C5E",        # 0A, 10
        "Function_11_1C80",        # 0B, 11
        "Function_12_1C97",        # 0C, 12
        "Function_13_1CB1",        # 0D, 13
        "Function_14_1CCB",        # 0E, 14
        "Function_15_1CE5",        # 0F, 15
        "Function_16_1D0E",        # 10, 16
        "Function_17_1D37",        # 11, 17
        "Function_18_1D97",        # 12, 18
        "Function_19_3194",        # 13, 19
        "Function_20_31C9",        # 14, 20
        "Function_21_3252",        # 15, 21
        "Function_22_3DC3",        # 16, 22
        "Function_23_3DF9",        # 17, 23
        "Function_24_3E63",        # 18, 24
        "Function_25_3E86",        # 19, 25
        "Function_26_4ECE",        # 1A, 26
        "Function_27_4F40",        # 1B, 27
        "Function_28_4FE9",        # 1C, 28
        "Function_29_5021",        # 1D, 29
        "Function_30_5059",        # 1E, 30
        "Function_31_5091",        # 1F, 31
        "Function_32_50C9",        # 20, 32
        "Function_33_5101",        # 21, 33
        "Function_34_5139",        # 22, 34
        "Function_35_583C",        # 23, 35
        "Function_36_58A6",        # 24, 36
        "Function_37_5D78",        # 25, 37
        "Function_38_5DCF",        # 26, 38
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
            "\"Rosenberg Studio\"\x01",
            "Do not enter other than stakeholders.\x02",
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

    def Function_4_762(): pass

    label("Function_4_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    Call(0, 21)
    Return()

    label("loc_774")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is tightly closed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_4_762 end

    def Function_5_7A0(): pass

    label("Function_5_7A0")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_7A0 end

    def Function_6_7AD(): pass

    label("Function_6_7AD")

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
            "─ ─ Terror.\x01",
            "I'm not going to put on any odds.\x02\x03",
            "How can you say \"thirteen studio\" supervisor,\x01",
            "There is no right to enter.\x02",
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
            "…… Huh, that's okay.\x02\x03",
            "It is No. Possession of..\x01",
            "I do not intend to pick it up.\x02\x03",
            "But, Meister?\x01",
            "Will you hand over the data one by one?\x02\x03",
            "It is \"that person\"\x01",
            "Because it is also your will.\x02",
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
            "#03903F#5P…… Hun.\x01",
            "There is no need to say to your nakedness.\x02",
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
            "#3701V#30WUhufu, they are really bad.\x02\x03",
            "#3702VDr. also knows that she is disliked\x01",
            "You should not bother to visit.\x02",
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
            "#04709F#11PHaha, what are you saying?\x02\x03",
            "#04702FMe and meister are old friends.\x02\x03",
            "Especially regarding doll making\x01",
            "With a solid teacher's bond\x01",
            "Because it is tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PHun, romance#4RInnocent#Stop it.\x02\x03",
            "#03900FTechniques such as something new\x01",
            "It is a stale thing if it makes it to an association.\x02\x03",
            "With the \"integration theory\" of okayashi\x01",
            "Do you need to rely on me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PHuh, please humbly.\x02\x03",
            "Adjusting this doll\x01",
            "Human being on the right of Meister\x01",
            "It does not exist in this world.\x02\x03",
            "#04705FOh, but I got it on \"Patel-Mattel\"\x01",
            "You can not just have that circuit?\x02\x03",
            "#04703FWell then, that's wrong.\x01",
            "Annihilation#4RAnxiomatosis#The potential of \"angel\"\x01",
            "It will be useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#03901F#5P…… This cross road is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5PEr, I'm sorry.\x02",
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

    def lambda_10AB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10AB)
    Sleep(50)

    def lambda_10BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10BB)
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
        "#04705F#5PWha …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04805F#5Pthat?\x01",
            "It looks like a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5P… …. Campanella.\x01",
            "You have finished the matter.\x02\x03",
            "#03900FTake that uncomfortable man\x01",
            "Let's get away at last.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11C2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11C2)
    Sleep(50)

    def lambda_11D2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11D2)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#04804F#12PUhufu, okay.\x02\x03",
            "#04802FDr. Hehara.\x01",
            "I have to go quickly.\x02\x03",
            "Complete for today\x01",
            "You go back to the laboratory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04704F#11PHuh, of course.\x02\x03",
            "#04702FWell then Meister,\x01",
            "I will be rude with this.\x02\x03",
            "As the children of the example are completed,\x01",
            "Please check it, are not you?\x02",
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
            "#03901F#5P#4S…… That's bad!\x01",
            "Lost quickly but nice!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#04809F#12P#3703V#30WUhufu, then again.\x02",
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
        "#03900F#5P…… what a fist#2RHow#It is out.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15D1")

    ChrTalk(
        0x101,
        "#00006F#12PWell, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PThank you for that passage …\x01",
            "I was out of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PIt is a long time since the Special Affairs Support Division.\x02\x03",
            "#03900FLen departed to Libert.\x01",
            "What are you doing here for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F2")

    label("loc_15D1")


    ChrTalk(
        0x101,
        (
            "#00006F#12PWell, sorry.\x02\x03",
            "#00000F……Nice to meet you.\x01",
            "Crossbell Police,\x01",
            "It is a person of the affairs support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PLord of Rosenberg workshop,\x01",
            "Are you Jorg Meister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PSomewhat from Hung, Len,\x01",
            "You seem to have heard the story.\x02\x03",
            "#03900FLen departed to Libert.\x01",
            "What is it for here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F2")


    ChrTalk(
        0x101,
        (
            "#00012F#12PNo, because I came nearby\x01",
            "I just came across a greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PThat……\x01",
            "I was sorry during the visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03901F#5PHun, it is a guest who is not invited.\x01",
            "I am concerned about that.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(250)

    ChrTalk(
        0xB,
        (
            "#03903F#11PBut now, especially speaking\x01",
            "It is not necessarily certain.\x02\x03",
            "When I have something to do\x01",
            "You should visit again.\x02\x03",
            "#03900FLet's dispense with Len and listen to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PAh……\x02",
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
        "#10105F#12POr, the gate closed without permission …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PWhoa, it's old fashioned\x01",
            "Is there something also a gimmick?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A3B")

    ChrTalk(
        0x101,
        (
            "#00006F#5PAh……\x01",
            "An outrageous fly\x01",
            "It's a place I am making.\x02\x03",
            "#00008Fin addition……\x01",
            "Also worry about visitors who came earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB0")

    label("loc_1A3B")


    ChrTalk(
        0x101,
        (
            "#00006F#5POh, as I told Ren,\x01",
            "It looks like it's not just a puppeteer.\x02\x03",
            "#00008Fin addition……\x01",
            "Also worry about visitors who came earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB0")

    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00103F#11PYes, invited guests\x01",
            "I was telling you ….\x02\x03",
            "#00108FWhat's that, that … ….\x01",
            "It was a dubious feeling.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10106F#6PI agree……\x02\x03",
            "#10100FWell, it looks dangerous\x01",
            "I did not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12P(… … Huff.\x01",
            "Does not it look dangerous? )\x02",
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

    # Function_6_7AD end

    def Function_7_1BF8(): pass

    label("Function_7_1BF8")

    OP_9B(0x0, 0xFE, 0x4, 0x36B0, 0x7D0, 0x0)

    def lambda_1C0C():

        label("loc_1C0C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C0C")

    QueueWorkItem2(0xFE, 2, lambda_1C0C)
    Return()

    # Function_7_1BF8 end

    def Function_8_1C1A(): pass

    label("Function_8_1C1A")

    OP_9B(0x0, 0xFE, 0x5, 0x3BC4, 0x7D0, 0x0)

    def lambda_1C2E():

        label("loc_1C2E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C2E")

    QueueWorkItem2(0xFE, 2, lambda_1C2E)
    Return()

    # Function_8_1C1A end

    def Function_9_1C3C(): pass

    label("Function_9_1C3C")

    OP_9B(0x0, 0xFE, 0x6, 0x38A4, 0x7D0, 0x0)

    def lambda_1C50():

        label("loc_1C50")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C50")

    QueueWorkItem2(0xFE, 2, lambda_1C50)
    Return()

    # Function_9_1C3C end

    def Function_10_1C5E(): pass

    label("Function_10_1C5E")

    OP_9B(0x0, 0xFE, 0x6, 0x3C8C, 0x7D0, 0x0)

    def lambda_1C72():

        label("loc_1C72")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C72")

    QueueWorkItem2(0xFE, 2, lambda_1C72)
    Return()

    # Function_10_1C5E end

    def Function_11_1C80(): pass

    label("Function_11_1C80")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_11_1C80 end

    def Function_12_1C97(): pass

    label("Function_12_1C97")

    Sleep(50)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xE10, 0x7D0, 0x0)
    Return()

    # Function_12_1C97 end

    def Function_13_1CB1(): pass

    label("Function_13_1CB1")

    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_13_1CB1 end

    def Function_14_1CCB(): pass

    label("Function_14_1CCB")

    Sleep(150)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_14_1CCB end

    def Function_15_1CE5(): pass

    label("Function_15_1CE5")

    Sleep(50)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_15_1CE5 end

    def Function_16_1D0E(): pass

    label("Function_16_1D0E")

    Sleep(250)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_16_1D0E end

    def Function_17_1D37(): pass

    label("Function_17_1D37")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)

    def lambda_1D6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D6C)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_17_1D37 end

    def Function_18_1D97(): pass

    label("Function_18_1D97")

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

    def lambda_1F0C():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F0C)
    Sleep(10)

    def lambda_1F24():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F24)
    Sleep(10)

    def lambda_1F3C():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1F3C)
    Sleep(10)

    def lambda_1F54():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F54)
    Sleep(10)

    def lambda_1F6C():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F6C)
    Sleep(10)

    def lambda_1F84():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F84)
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
        "#00005F#11PThat is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P運搬car……？\x02",
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
            "#12PMeister,\x01",
            "it was a great help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PSomehow tomorrow's performance\x01",
            "It is going to make it in time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PAbsolutely …\x01",
            "When your messenger group\x01",
            "Every time, the request is too high.\x02\x03",
            "Automatic doll#8RAuto meta#If it's adjusted\x01",
            "Until ordering of a new stage equipment …\x02\x03",
            "#03901FYou are not free from me, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PHaha ……\x01",
            "Really sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAnything with Mr. Ilya\x01",
            "The demand from the theater company manager is high … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PWell, until such a trick\x01",
            "We ordered additional order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03900F#5PHun, that's okay.\x02\x03",
            "#03903F…… Our workshop technology,\x01",
            "You better use it on your stage\x01",
            "Suitable for the will of the goddess#2RWonder#Let's make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PHaha … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P── That's right, Meister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAs you invited from last week,\x01",
            "By all means the performance of the alkane shell\x01",
            "I'd like to see it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAlways wonderful dolls and stage equipment\x01",
            "We are offering it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#03903F#5PI received the corresponding Mira.\x02\x03",
            "#03900F…… I am busy.\x01",
            "Let's just give favor.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)

    ChrTalk(
        0xC,
        "#12PAh……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_68(1400, 1000, 24300, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(20500, 1000)

    def lambda_247E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_247E)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    WaitChrThread(0xC, 1)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#12P…… Huh.\x01",
            "Can you respond to me after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PA great stage equipment,\x01",
            "How is it used?\x01",
            "I want you to see it once ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F……that………\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2565():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2565)
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

    def lambda_2606():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2606)
    Sleep(50)

    def lambda_261E():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_261E)
    Sleep(50)

    def lambda_2636():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2636)
    Sleep(50)

    def lambda_264E():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_264E)
    Sleep(50)

    def lambda_2666():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2666)
    Sleep(50)

    def lambda_267E():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_267E)
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
            "#5PGee\x01",
            "Is it certain of the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12POh, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12POf alkane shell\x01",
            "You are an engineer, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, I'm in charge of the stage equipment\x01",
            "Heinzです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI will meet you in a rare place.\x01",
            "Do you need help with Meister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PWell, yeah, a little consultation\x01",
            "There was something I wanted to ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12PThere is a device for the stage\x01",
            "To receive ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYes, with automatic doll adjustment\x01",
            "Production of a new stage device\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PTogether with the renewal performance\x01",
            "It was an inconvenient schedule\x01",
            "I managed to finish it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWell ~, all the theater members,\x01",
            "To Meister\x01",
            "I can not sleep with my legs facing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PSo that's the alkane shell\x01",
            "The first performance of the renewal stage\x01",
            "It is finally the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYeah, Iria started,\x01",
            "The more all members are ever\x01",
            "There was a fighting spirit ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAs a stage equipment manager\x01",
            "I feel tight towards myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHuh, on a great stage\x01",
            "I guess it will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POops, I can not do this.\x01",
            "I have to go home early and set … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P── Everyone, I am with this!\x01",
            "Please come to the theater again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#12PYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PPlease take care.\x02",
    )

    CloseMessageWindow()

    def lambda_2B3D():
        OP_9B(0x1, 0xFE, 0xE6, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B3D)
    BeginChrThread(0xC, 1, 0, 20)
    OP_68(2900, 1000, 18300, 5000)
    SetCameraDistance(21500, 5000)

    def lambda_2B72():

        label("loc_2B72")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B72")

    QueueWorkItem2(0x101, 2, lambda_2B72)

    def lambda_2B84():

        label("loc_2B84")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B84")

    QueueWorkItem2(0x102, 2, lambda_2B84)

    def lambda_2B96():

        label("loc_2B96")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B96")

    QueueWorkItem2(0x103, 2, lambda_2B96)

    def lambda_2BA8():

        label("loc_2BA8")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BA8")

    QueueWorkItem2(0x104, 2, lambda_2BA8)

    def lambda_2BBA():

        label("loc_2BBA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BBA")

    QueueWorkItem2(0x109, 2, lambda_2BBA)

    def lambda_2BCC():

        label("loc_2BCC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BCC")

    QueueWorkItem2(0x105, 2, lambda_2BCC)
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

    def lambda_2C13():

        label("loc_2C13")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C13")

    QueueWorkItem2(0x101, 2, lambda_2C13)

    def lambda_2C25():

        label("loc_2C25")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C25")

    QueueWorkItem2(0x102, 2, lambda_2C25)

    def lambda_2C37():

        label("loc_2C37")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C37")

    QueueWorkItem2(0x103, 2, lambda_2C37)

    def lambda_2C49():

        label("loc_2C49")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C49")

    QueueWorkItem2(0x104, 2, lambda_2C49)

    def lambda_2C5B():

        label("loc_2C5B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C5B")

    QueueWorkItem2(0x109, 2, lambda_2C5B)

    def lambda_2C6D():

        label("loc_2C6D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C6D")

    QueueWorkItem2(0x105, 2, lambda_2C6D)
    OP_68(2900, 1000, 10300, 5000)
    SetCameraDistance(22500, 5000)
    Sound(465, 0, 100, 0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2CAB():
        OP_9B(0x1, 0xFE, 0xA, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CAB)
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

    def lambda_2D8A():
        TurnDirection(0x101, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D8A)
    Sleep(0)

    def lambda_2D9A():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D9A)
    Sleep(0)

    def lambda_2DAA():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DAA)
    Sleep(0)

    def lambda_2DBA():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DBA)
    Sleep(0)

    def lambda_2DCA():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DCA)
    Sleep(0)

    def lambda_2DDA():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DDA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2ECF")

    ChrTalk(
        0x104,
        (
            "#00306F#12PBut the alkane shell\x01",
            "I'm working on a stage device\x01",
            "I was listening … …\x02\x03",
            "#00301FWhen we look at such places\x01",
            "It is related to a dubious association\x01",
            "Do not think like a workshop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PI see …\x02",
    )

    CloseMessageWindow()
    Jump("loc_3044")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_2F56")

    ChrTalk(
        0x104,
        (
            "#00306F#12P…… Hey, what do you mean?\x02\x03",
            "#00301FWhat is the stage equipment of the alkane shell?\x01",
            "Is that the mon who handed that old man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCD")

    label("loc_2F56")


    ChrTalk(
        0x104,
        (
            "#00306F#12P…… Hey, what do you mean?\x02\x03",
            "#00301FWhat is the stage equipment of the alkane shell?\x01",
            "Is this a mon made in this workshop?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCD")


    ChrTalk(
        0x103,
        (
            "#00203F#6Pseems that way.\x02\x03",
            "#00201FIt is called wire action,\x01",
            "A considerable advanced technology is used\x01",
            "I thought … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3044")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PTentatively\x01",
            "I was saved because I was out.\x02\x03",
            "#00013FOn the movement of \"association\"\x01",
            "Whether you can talk to me ……\x01",
            "Just listen and just ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PYes……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PGiggle\x01",
            "Is it a place to stay in the tiger's hole?\x02",
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

    # Function_18_1D97 end

    def Function_19_3194(): pass

    label("Function_19_3194")

    OP_93(0xB, 0x0, 0x1F4)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_31B5():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_31B5)
    Sleep(1500)
    Return()

    # Function_19_3194 end

    def Function_20_31C9(): pass

    label("Function_20_31C9")

    OP_95(0xC, 2900, 0, 24300, 2000, 0x0)
    OP_95(0xC, 2900, 0, 18500, 2000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Sound(464, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)

    def lambda_3215():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3215)
    OP_95(0xC, 3900, 500, 18500, 2000, 0x0)
    WaitChrThread(0xC, 3)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x2)
    Return()

    # Function_20_31C9 end

    def Function_21_3252(): pass

    label("Function_21_3252")

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
            "※ Once you visit the puppet factory\x01",
            "On this day, we will visit various places other than Crossbell City\x01",
            "I will not be able to visit.\x07\x00\x02",
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
            "【There are still other things to do】\x01",            # 0
            "[Visit this puppet studio as it is]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_33FD"),
        (0, "loc_3D96"),
        (SWITCH_DEFAULT, "loc_3DC2"),
    )


    label("loc_33FD")

    OP_68(2000, 1000, 26000, 1500)
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd sounded the iron knocker on the door.\x07\x00\x02",
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
        "#00003F#4S#11P── I'm sorry!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#00001F#11PCrossbell Police,\x01",
            "It is a person of the Special Affairs Support Division!\x02\x03",
            "Meister · Rosenberg!\x01",
            "Do you Come! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "… … so loud\x01",
            "I can hear it without raising it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3698")
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
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apparently I have something I want to ask\x01",
            "You seem to have visited.\x02\x03",
            "I do not have much time … …\x01",
            "For a while\x01",
            "I have not heard the story.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_37D2")

    label("loc_3698")

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
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Are you the Special Affairs Division?\x02\x03",
            "Apparently I have something I want to ask\x01",
            "You seem to have visited … …\x02\x03",
            "For a while\x01",
            "I have not heard the story.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_37D2")

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

    def lambda_3860():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3860)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#6PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12P#NOr, it's cute …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00112F#12P#NRosenberg doll ……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#6P#N…… It looks like an automatic doll … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I will let him guide you\x01",
            "Come in, come inside.\x02\x03",
            "Even more\x01",
            "I will not enter.\x07\x00\x02",
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
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PSurely\x01",
            "It seems I will not speak … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell,\x01",
            "I do not think it is a mechanical mechanism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12P…… Then you, to your master\x01",
            "Would you show me around?\x02",
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
        "#10112F#12PShall we go?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12PThat's right.\x01",
            "It is bad even if I let him wait ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#12P(\"Snake Snake\" … …\x01",
            "As expected, you are a bottomless opponent. )\x02",
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
    Jump("loc_3DC2")

    label("loc_3D96")

    SetChrPos(0x0, 1600, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_3DC2")

    label("loc_3DC2")

    Return()

    # Function_21_3252 end

    def Function_22_3DC3(): pass

    label("Function_22_3DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE0")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 35)
    Jump("loc_3DF8")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF8")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 23)

    label("loc_3DF8")

    Return()

    # Function_22_3DC3 end

    def Function_23_3DF9(): pass

    label("Function_23_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E62")
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

    label("loc_3E62")

    Return()

    # Function_23_3DF9 end

    def Function_24_3E63(): pass

    label("Function_24_3E63")

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

    # Function_24_3E63 end

    def Function_25_3E86(): pass

    label("Function_25_3E86")

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

    def lambda_4153():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4153)
    Sleep(50)

    def lambda_4163():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4163)
    Sleep(50)

    def lambda_4173():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4173)
    Sleep(50)

    def lambda_4183():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4183)
    Sleep(50)

    def lambda_4193():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4193)
    Sleep(50)

    def lambda_41A3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41A3)
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
            "#00106F#5P……what……\x01",
            "It sounds like I'm dreaming.\x02\x03",
            "#00108F\"Phantomhurgh#4RNuclear power plant#plan\"……\x01",
            "And they say they visit Crossbell\x01",
            "The existence of two \"apostles\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PTo be honest, crazy too\x01",
            "I do not have a sense of reality … ….\x02\x03",
            "#10101FHow far is true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P…… As long as you hear Libert's accident,\x01",
            "It will be certain that they are not fancy.\x02\x03",
            "#00008FHowever, unlike Libert\x01",
            "It seems like you are doing a large-scale trick\x01",
            "I did not feel it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, until a huge flying battleship\x01",
            "Because it is story about appearance.\x02\x03",
            "#10302FThat \"Patel = Mattel\" is said\x01",
            "He seemed to bring out a huge doll.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_440A():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_440A)
    Sleep(50)

    def lambda_441A():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_441A)
    Sleep(50)

    def lambda_442A():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_442A)
    Sleep(50)

    def lambda_443A():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_443A)
    Sleep(50)

    def lambda_444A():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_444A)
    Sleep(50)

    def lambda_445A():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_445A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00011F#11PDo not know well …\x01",
            "Even though it is confidential information in department 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#11PTo such a thing between hosts\x01",
            "Are rumors spreading?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#6PWell, that is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00005F#12PWhat happened, both of us?\x02",
    )

    CloseMessageWindow()

    def lambda_45BC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_45BC)

    def lambda_45C9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_45C9)

    def lambda_45D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D6)

    def lambda_45E3():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45E3)
    Sleep(50)

    def lambda_45F3():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45F3)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x103,
        "#00203F#11PHouse……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5POh … a little.\x02\x03",
            "#00301FThio is the person\x01",
            "Look at another thought again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P……I agree.\x02\x03",
            "#00201FI showed you earlier.\x01",
            "Even if it is made into a doll … ….\x02\x03",
            "Thank you for saying \"Society\"\x01",
            "play#4R噵 噵#I thought it was an organization with a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PThere are lots of fun … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PYes, Epstein Foundation and\x01",
            "While having technical expertise beyond ZCF\x01",
            "It seems like wasting it … …\x02\x03",
            "#00201FEven if you make that \"Patel = Mattel\"\x01",
            "If you make such humanoid weapons at practical level\x01",
            "It seems that 50 flying boats will be built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PIs that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PIs there a rich source of funds?\x01",
            "Or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#5P…… But certainly the military and criminal organization\x01",
            "It is basically an organizational format that emphasizes efficiency.\x02\x03",
            "#10108FAs much as possible do not have the part of play\x01",
            "It moves coldly for the purpose …\x02\x03",
            "#10101FSuch rationality is\x01",
            "I did not feel it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PIt is there that I thought.\x02\x03",
            "#00301FNo matter how great technical you have\x01",
            "Whether you are holding a celibate person … …\x02\x03",
            "Hunting corps of \"Red constellation\" class and\x01",
            "Syndicate like \"black moon\"\x01",
            "A realistic threat may be on top.\x02\x03",
            "#00303FEven the empire, with a great country that is a wonderful Republic\x01",
            "I can not think that we can do it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PThen, that kind of power\x01",
            "Currently making complicated conflict situation ……\x02\x03",
            "#10300FThose like \"Society\"\x01",
            "Come to the crossbell all the way\x01",
            "what#4R噵 噵#Whether it is aiming is a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PI see …\x01",
            "We also supported terrorists\x01",
            "It seems it was just a whim.\x02\x03",
            "#00101FMany, for a realistic power fight\x01",
            "I am actively involved\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIf so … …\x01",
            "For the purpose \"not realistic\"\x01",
            "Is it that it is moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThen, to us\x01",
            "It seems to be getting ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PBut, actually\x01",
            "I am planning to do something\x01",
            "I certainly wanted to … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P── Anyway, let's return to the support department once.\x02\x03",
            "#00001FI would like to talk to the section manager,\x01",
            "I also want to contact the guards and guilds.\x02\x03",
            "Whatever \"association\" intends to do\x01",
            "At minimum, you should be able to make it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DA6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DA6)
    Sleep(50)

    def lambda_4DB6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4DB6)
    Sleep(50)

    def lambda_4DC6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4DC6)
    Sleep(50)

    def lambda_4DD6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DD6)
    Sleep(50)

    def lambda_4DE6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4DE6)
    Sleep(50)

    def lambda_4DF6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4DF6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00101F#5PYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#5PWell then,\x01",
            "Returning to Cros Bell City.\x02",
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

    # Function_25_3E86 end

    def Function_26_4ECE(): pass

    label("Function_26_4ECE")

    Sound(957, 2, 40, 0)

    def lambda_4ED9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4ED9)
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

    # Function_26_4ECE end

    def Function_27_4F40(): pass

    label("Function_27_4F40")

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

    def lambda_4FA9():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4FA9)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_4F40 end

    def Function_28_4FE9(): pass

    label("Function_28_4FE9")


    def lambda_4FEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4FEE)
    OP_95(0xFE, 2000, 0, 20000, 2000, 0x0)

    def lambda_5013():

        label("loc_5013")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5013")

    QueueWorkItem2(0xFE, 2, lambda_5013)
    Return()

    # Function_28_4FE9 end

    def Function_29_5021(): pass

    label("Function_29_5021")


    def lambda_5026():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5026)
    OP_95(0xFE, 1000, 0, 20750, 2000, 0x0)

    def lambda_504B():

        label("loc_504B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_504B")

    QueueWorkItem2(0xFE, 2, lambda_504B)
    Return()

    # Function_29_5021 end

    def Function_30_5059(): pass

    label("Function_30_5059")


    def lambda_505E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_505E)
    OP_95(0xFE, 3000, 0, 21500, 2000, 0x0)

    def lambda_5083():

        label("loc_5083")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5083")

    QueueWorkItem2(0xFE, 2, lambda_5083)
    Return()

    # Function_30_5059 end

    def Function_31_5091(): pass

    label("Function_31_5091")


    def lambda_5096():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5096)
    OP_95(0xFE, 2000, 0, 22000, 2000, 0x0)

    def lambda_50BB():

        label("loc_50BB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50BB")

    QueueWorkItem2(0xFE, 2, lambda_50BB)
    Return()

    # Function_31_5091 end

    def Function_32_50C9(): pass

    label("Function_32_50C9")


    def lambda_50CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_50CE)
    OP_95(0xFE, 1500, 0, 23000, 2000, 0x0)

    def lambda_50F3():

        label("loc_50F3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50F3")

    QueueWorkItem2(0xFE, 2, lambda_50F3)
    Return()

    # Function_32_50C9 end

    def Function_33_5101(): pass

    label("Function_33_5101")


    def lambda_5106():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5106)
    OP_95(0xFE, 0, 0, 22000, 2000, 0x0)

    def lambda_512B():

        label("loc_512B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_512B")

    QueueWorkItem2(0xFE, 2, lambda_512B)
    Return()

    # Function_33_5101 end

    def Function_34_5139(): pass

    label("Function_34_5139")

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

    def lambda_51B2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51B2)
    Sleep(100)

    def lambda_51CA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51CA)
    Sleep(100)

    def lambda_51E2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_51E2)
    Sleep(100)

    def lambda_51FA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51FA)
    Sleep(100)

    def lambda_5212():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5212)
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
            "#00006F#11PWell ……\x01",
            "I hope not to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PThis is the situation, and in other places\x01",
            "I think that I have not gone out … ….\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I'm not going out.\x07\x00\x02",
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
        "#00011F#12PWow\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#12P… …. Voice tube?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Whether it is about to come\x01",
            "I thought that.\x07\x00\x02",
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

    def lambda_54DC():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54DC)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    ChrTalk(
        0x106,
        "#10712F#6P#N……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10400F#6P#NA doll of a guide rider.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Come in.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 0, -1, -1)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Needless to say,\x01",
            "If I can get stuck from that girl\x01",
            "Can you guarantee yourself?\x07\x00\x02",
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
        "#10710F#12PWell ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#12P#3CFu … as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PTomorrow\x01",
            "The story was early and it helped.\x02\x03",
            "#00000FLet me interfere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12Pis not it.\x02",
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

    # Function_34_5139 end

    def Function_35_583C(): pass

    label("Function_35_583C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A5")
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

    label("loc_58A5")

    Return()

    # Function_35_583C end

    def Function_36_58A6(): pass

    label("Function_36_58A6")

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

    def lambda_5A31():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5A31)
    Sleep(50)

    def lambda_5A41():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A41)
    Sleep(50)

    def lambda_5A51():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5A51)
    Sleep(50)

    def lambda_5A61():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5A61)
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
            "#00204F#6PAs long as you talk, I'm lucky\x01",
            "I thought that … ….\x02\x03",
            "#00202FThe one who did the cooperation is\x01",
            "It was unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POh, although saying \"association\"\x01",
            "There seems to be various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PWell, that's why it's real\x01",
            "It is an organization that I can not grasp.\x02\x03",
            "#10400FBut for that old man\x01",
            "Even if you trust it does not seem to be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704F#11P……I agree.\x01",
            "There seems to be a reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CIf it is Jorg,\x01",
            "It will provide valuable information.\x02\x03",
            "#01200FWell, without excessive expectation\x01",
            "You should wait for contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12POh, I will.\x02\x03",
            "#00000F── Well then.\x01",
            "I will be heading for mining town soon.\x02\x03",
            "Trends of resistance forces as well\x01",
            "I want to explore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702F#11POK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#5PWell then let's go.\x02",
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

    # Function_36_58A6 end

    def Function_37_5D78(): pass

    label("Function_37_5D78")

    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_5D8F():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5D8F)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_5D78 end

    def Function_38_5DCF(): pass

    label("Function_38_5DCF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FNot much meister\x01",
            "I can not let you wait.\x01",
            "Let's get inside the studio as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 830, 0, -1070, 0)
    EventEnd(0x4)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_38_5DCF end

    SaveToFile()

Try(main)
