from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9012.bin",                # FileName
        "m9012",                    # MapName
        "m9012",                    # Location
        0x00C4,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 196, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9012",                  # 0
        "Ian lawyer",           # 1
        "Keya",                 # 2
        "Marybele",             # 3
        "Demiurgos",           # 4
        "Marybeleフェード",     # 5
        "Ian target",       # 6
        "Keyaダミー",           # 7
        "SE control",                 # 8
        "For APL display",              # 9
        "bm9070",                 # 10
        "bm9099",                 # 11
        "bm9099",                 # 12
    ))

    ATBonus("ATBonus_1C0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_1D0", 100, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_200", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_264", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_268", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_26C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_270", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_280", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_288", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_28C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_2C0", 0x0052, 255, 6, 45, 3, 1, 30, 0, "bm9070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03700.dat", "ms80500.dat", "ms80500.dat", "ms80500.dat", "ms80500.dat", 0, "ms80500.dat", 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7458", "ed7453", "ATBonus_1C0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x009A, 255, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            (0, 0, 0, 0, 0, "ms89000.dat", "ms86400.dat", 0, "MonsterBattlePostion_280", "MonsterBattlePostion_280", "ed7459", "ed7453", "ATBonus_1D0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_348", 0x009A, 255, 6, 45, 3, 1, 30, 0, "bm9099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89100.dat", 0, 0, 0, 0, 0, "ms86500.dat", 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_2A0", "ed7459", "ed7453", "ATBonus_1D0"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       3750,    4294961447, 0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_55E",          # 01, 1
        "Function_2_5AC",          # 02, 2
        "Function_3_60D",          # 03, 3
        "Function_4_66E",          # 04, 4
        "Function_5_689",          # 05, 5
        "Function_6_695",          # 06, 6
        "Function_7_61FD",         # 07, 7
        "Function_8_6267",         # 08, 8
        "Function_9_62D1",         # 09, 9
        "Function_10_633B",        # 0A, 10
        "Function_11_63A5",        # 0B, 11
        "Function_12_640F",        # 0C, 12
        "Function_13_6479",        # 0D, 13
        "Function_14_6495",        # 0E, 14
        "Function_15_64B4",        # 0F, 15
        "Function_16_64D3",        # 10, 16
        "Function_17_64F2",        # 11, 17
        "Function_18_6511",        # 12, 18
        "Function_19_6530",        # 13, 19
        "Function_20_6542",        # 14, 20
        "Function_21_6551",        # 15, 21
        "Function_22_6563",        # 16, 22
        "Function_23_6575",        # 17, 23
        "Function_24_6581",        # 18, 24
        "Function_25_65CF",        # 19, 25
        "Function_26_661D",        # 1A, 26
        "Function_27_6653",        # 1B, 27
        "Function_28_6690",        # 1C, 28
        "Function_29_66E2",        # 1D, 29
        "Function_30_6802",        # 1E, 30
        "Function_31_6951",        # 1F, 31
        "Function_32_69C6",        # 20, 32
        "Function_33_69E2",        # 21, 33
        "Function_34_69F7",        # 22, 34
        "Function_35_6A06",        # 23, 35
        "Function_36_6A71",        # 24, 36
        "Function_37_6A87",        # 25, 37
        "Function_38_6A9D",        # 26, 38
        "Function_39_6AB3",        # 27, 39
        "Function_40_6AC9",        # 28, 40
        "Function_41_6ADF",        # 29, 41
        "Function_42_6AFC",        # 2A, 42
        "Function_43_6B19",        # 2B, 43
        "Function_44_6B28",        # 2C, 44
        "Function_45_6B37",        # 2D, 45
        "Function_46_6B84",        # 2E, 46
        "Function_47_8A6A",        # 2F, 47
        "Function_48_8AB9",        # 30, 48
        "Function_49_8AE3",        # 31, 49
        "Function_50_8AEA",        # 32, 50
        "Function_51_8B06",        # 33, 51
        "Function_52_8B84",        # 34, 52
        "Function_53_8BA6",        # 35, 53
        "Function_54_8BB4",        # 36, 54
        "Function_55_8BCE",        # 37, 55
        "Function_56_8BEB",        # 38, 56
        "Function_57_8C0A",        # 39, 57
        "Function_58_9B33",        # 3A, 58
        "Function_59_9B44",        # 3B, 59
        "Function_60_9B7F",        # 3C, 60
        "Function_61_9CA2",        # 3D, 61
        "Function_62_9E3C",        # 3E, 62
        "Function_63_9EC1",        # 3F, 63
        "Function_64_9ED0",        # 40, 64
        "Function_65_9EE2",        # 41, 65
        "Function_66_9EF4",        # 42, 66
        "Function_67_9F00",        # 43, 67
        "Function_68_9F4E",        # 44, 68
        "Function_69_9F9C",        # 45, 69
        "Function_70_9FB9",        # 46, 70
        "Function_71_9FFE",        # 47, 71
        "Function_72_E07D",        # 48, 72
        "Function_73_E0C4",        # 49, 73
        "Function_74_E122",        # 4A, 74
        "Function_75_E14D",        # 4B, 75
        "Function_76_E178",        # 4C, 76
        "Function_77_E19C",        # 4D, 77
        "Function_78_E1F0",        # 4E, 78
        "Function_79_E212",        # 4F, 79
        "Function_80_E234",        # 50, 80
        "Function_81_E256",        # 51, 81
        "Function_82_E2D2",        # 52, 82
        "Function_83_E34E",        # 53, 83
        "Function_84_E395",        # 54, 84
        "Function_85_E3B4",        # 55, 85
        "Function_86_E3D3",        # 56, 86
        "Function_87_E3F2",        # 57, 87
        "Function_88_E411",        # 58, 88
        "Function_89_E430",        # 59, 89
        "Function_90_E4AC",        # 5A, 90
        "Function_91_E4F1",        # 5B, 91
        "Function_92_E57B",        # 5C, 92
        "Function_93_E5F3",        # 5D, 93
        "Function_94_E617",        # 5E, 94
        "Function_95_E63B",        # 5F, 95
        "Function_96_E65F",        # 60, 96
        "Function_97_E689",        # 61, 97
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 6)), scpexpr(EXPR_END)), "loc_520")
    Event(0, 6)

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_537")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 46)
    Jump("loc_55D")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_54E")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 57)
    Jump("loc_55D")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_55D")
    ClearScenarioFlags(0x22, 2)
    Event(0, 71)

    label("loc_55D")

    Return()

    # Function_0_514 end

    def Function_1_55E(): pass

    label("Function_1_55E")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_57C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_591")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_591")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1CB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5A5")
    OP_24(0x70)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_5AB")

    label("loc_5A5")

    Sound(112, 1, 50, 0)

    label("loc_5AB")

    Return()

    # Function_1_55E end

    def Function_2_5AC(): pass

    label("Function_2_5AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C4")
    LoadChrToIndex("chr/ch03150.itc", 0x26)

    label("loc_5C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC")
    LoadChrToIndex("chr/ch03250.itc", 0x26)

    label("loc_5DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F4")
    LoadChrToIndex("chr/ch02950.itc", 0x26)

    label("loc_5F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60C")
    LoadChrToIndex("chr/ch00950.itc", 0x26)

    label("loc_60C")

    Return()

    # Function_2_5AC end

    def Function_3_60D(): pass

    label("Function_3_60D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_625")
    LoadChrToIndex("chr/ch03150.itc", 0x27)

    label("loc_625")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63D")
    LoadChrToIndex("chr/ch03250.itc", 0x27)

    label("loc_63D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_655")
    LoadChrToIndex("chr/ch02950.itc", 0x27)

    label("loc_655")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66D")
    LoadChrToIndex("chr/ch00950.itc", 0x27)

    label("loc_66D")

    Return()

    # Function_3_60D end

    def Function_4_66E(): pass

    label("Function_4_66E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_688")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_4_66E")

    label("loc_688")

    Return()

    # Function_4_66E end

    def Function_5_689(): pass

    label("Function_5_689")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_5_689 end

    def Function_6_695(): pass

    label("Function_6_695")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch05900.itc", 0x20)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadChrToIndex("chr/ch03752.itc", 0x29)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "battle/cr037000.eff")
    LoadEffect(0x1, "battle/cr037001.eff")
    LoadEffect(0x2, "battle/cr034001.eff")
    LoadEffect(0x3, "event\\ev202_00.eff")
    LoadEffect(0x4, "event/ev17006.eff")
    LoadEffect(0x5, "event/ev17007.eff")
    LoadEffect(0x6, "event\\ev500_00.eff")
    LoadEffect(0x7, "event/ev17075.eff")
    LoadEffect(0x8, "battle/cr037101.eff")
    SoundLoad(3407)
    SoundLoad(3330)
    SoundLoad(2774)
    SoundLoad(2694)
    SoundLoad(3789)
    SoundLoad(3790)
    SoundLoad(3791)
    SoundLoad(3792)
    SoundLoad(3793)
    SoundLoad(3794)
    SoundLoad(3795)
    SoundLoad(3636)
    SoundLoad(3637)
    SoundLoad(3638)
    SoundLoad(3639)
    SoundLoad(3640)
    SoundLoad(3641)
    SoundLoad(3643)
    SoundLoad(3644)
    SoundLoad(3645)
    SoundLoad(961)
    SoundLoad(474)
    SetChrPos(0x101, 0, 0, -54500, 0)
    SetChrPos(0x102, 0, 0, -54500, 19)
    SetChrPos(0x104, 0, 0, -54500, 342)
    SetChrPos(0x103, 0, 0, -54500, 6)
    SetChrPos(0xF4, 0, 0, -54500, 332)
    SetChrPos(0xF5, 0, 0, -54500, 32)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    Call(0, 43)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 0, 8000, -750, 180)
    PlayEffect(0x6, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -340, 2990, -5180, 180)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1190, 2990, -4720, 180)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -2029, 3000, -4860, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-900, 1400, -28370, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(70580, 0)
    OP_68(4380, 1400, -16990, 10000)
    MoveCamera(328, 11, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(51750, 10000)
    FadeToBright(1000, 0)
    PlaceName2(340, 40, "c_plac68", 0x0, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, -1100, 2500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43160, 0)
    OP_68(0, -1100, -52500, 5500)
    MoveCamera(0, 33, 0, 5500)
    OP_6E(700, 5500)
    SetCameraDistance(24050, 5500)
    OP_0D()
    OP_6F(0x79)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 7)
    Sleep(600)
    OP_6F(0x79)
    OP_68(0, 1200, -32450, 4500)
    MoveCamera(0, 5, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(32409, 4500)
    Sound(920, 0, 50, 0)
    BeginChrThread(0x102, 0, 0, 8)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0x104, 0, 0, 9)
    Sleep(600)
    Sound(920, 0, 50, 0)
    BeginChrThread(0x103, 0, 0, 10)
    Sleep(600)
    Sound(920, 0, 100, 0)
    BeginChrThread(0xF4, 0, 0, 11)
    Sleep(600)
    Sound(920, 0, 50, 0)
    BeginChrThread(0xF5, 0, 0, 12)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 13)
    BeginChrThread(0x102, 0, 0, 14)
    BeginChrThread(0x103, 0, 0, 15)
    BeginChrThread(0x104, 0, 0, 16)
    BeginChrThread(0xF4, 0, 0, 17)
    BeginChrThread(0xF5, 0, 0, 18)
    Sleep(200)
    OP_68(0, 3400, -9700, 6800)
    OP_6E(700, 6800)
    SetCameraDistance(18350, 6800)
    Sleep(1000)
    MoveCamera(43, 8, 0, 5800)
    Sleep(3900)
    Sleep(350)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        "#40WDid you come?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xA,
        (
            "#3789V#40W#30AUhufu … Welcome.\x02\x03",
            "#3790V#40ATake it to the end of the world\x01",
            "To the center of all causality.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_68(90, 5900, -740, 0)
    MoveCamera(25, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(33110, 0)
    SetCameraDistance(31110, 3000)
    Fade(500)
    OP_0D()
    OP_6F(0x79)
    OP_68(90, 8600, -740, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    SetCameraDistance(12000, 10000)
    OP_0D()
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAC")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3637V#20ANoel to Wadi … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_FAB")

    label("loc_EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2E")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3638V#20ANoel to Lisha … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_FAB")

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FAB")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3639V#20ANoel to Dudley … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_FAB")

    Jump("loc_112F")

    label("loc_FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10C0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1040")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3640V#20AWaji until Risha … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_10BB")

    label("loc_1040")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10BB")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3641V#20AWadi to Dudley … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_10BB")

    Jump("loc_112F")

    label("loc_10C0")


    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd …… Ellie … ….\x01",
            "…… Tio …… Randy ……\x02\x03",
            "#3642V#20ATo Leecha until Dudley … …\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_112F")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    MoveCamera(0, 9, 0, 32000)
    SetMessageWindowPos(-1, 230, -1, -1)

    ChrTalk(
        0x101,
        "#00007F#3330V#5P#N#30W#15AKeya……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 230, -1, -1)

    ChrTalk(
        0x103,
        (
            "#00214F#2694V#11P#N#30W#25AWas good……\x01",
            "Was it OK?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(200, 230, -1, -1)

    ChrTalk(
        0x104,
        "#00307F#2774V#5P#N#30W#20AKei Bou, are you okay! Is it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(120, 230, -1, -1)

    ChrTalk(
        0x102,
        (
            "#00108F#3407V#11P#N#30W#26AAlready……!\x01",
            "Not to worry … ….!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Call(0, 44)
    BeginChrThread(0x9, 0, 0, 36)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#3643V#5P#50W#20A………sorry…………\x02\x03",
            "#3644V#50AKeya…#800W…#50Wロイドたちに……\x01",
            "I had something I could not speak for a long time ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x9, 0, 0, 37)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#3645V#5P#40A#50W……… Keep silent ……#800W…\x01",
            "#50W… … Sorry to cheat … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5P#N… … Do not apologize … …!\x01",
            "I do not need to feel it as negative!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#11P#NJust because you are safe\x01",
            "It is enough for us …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#5P#NBesides kids,\x01",
            "More or less secretly to parents\x01",
            "It is commonplace to do it!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00103F#11P#NUtilizing such common things\x01",
            "Keyaちゃんを唆#2Rそそのか#した──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2900, -9000, 0)
    MoveCamera(114, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14700, 0)
    Call(0, 43)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        (
            "#00107F#11PBell, Ian Professor!\x01",
            "It is your work! Is it?\x02",
        )
    )

    Sleep(200)

    def lambda_1585():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1585)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x8,
        "#02203F#5POh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhufu … It is scary.\x02\x03",
            "#10800F#5PHowever, we\x01",
            "最大限にKeyaさんの意志を\x01",
            "I respect it.\x02\x03",
            "#10811Fそうですわよね──Keyaさん？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#6P#N#30W…………………… (Kokun)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00010F#11PDamn\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_170E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E4")
    OP_FC(0xB)
    Jump("loc_16E7")

    label("loc_16E4")

    OP_FC(0xB)

    label("loc_16E7")


    ChrTalk(
        0x109,
        "#10101F#13PThe thing is said … …\x02",
    )

    CloseMessageWindow()

    label("loc_170E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_175E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1738")
    OP_FC(0xB)
    Jump("loc_173B")

    label("loc_1738")

    OP_FC(0xB)

    label("loc_173B")


    ChrTalk(
        0x106,
        "#10701F#13P…… Vacant.\x02",
    )

    CloseMessageWindow()

    label("loc_175E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1788")
    OP_FC(0xB)
    Jump("loc_178B")

    label("loc_1788")

    OP_FC(0xB)

    label("loc_178B")


    ChrTalk(
        0x105,
        (
            "#10406F#13PWhew.\x01",
            "It is the thickness of the skin of a large surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1815")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17E9")
    OP_FC(0xB)
    Jump("loc_17EC")

    label("loc_17E9")

    OP_FC(0xB)

    label("loc_17EC")


    ChrTalk(
        0x10A,
        "#00601F#13P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1815")


    ChrTalk(
        0x104,
        (
            "#00301F#11P…… Anyway, first go back\x01",
            "From a place to talk carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PI agree.\x01",
            "It is a family conference.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12309F#6P#N#40WEh … … gus …\x01",
            "……Thanks guys……\x02\x03",
            "#12302FでもKeya……\x01",
            "I can not move here … …\x02\x03",
            "………… So ………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PKeyaちゃん……どうして？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P…… There is something?\x01",
            "Relating to the power as \"treasure\".\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#6P#6P#30W……………that is………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#6Pうふふ、Keyaさん。\x01",
            "Why do not you talk about it?\x02\x03",
            "#10811FWhat you are doing is\x01",
            "All for Lloyd's#24R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#Because.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#11P#30WHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11P#30W……what……\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#6P#N#40W…………………………………….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12870, 0)
    SetCameraDistance(11870, 10000)
    Call(0, 44)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#10800F#5PUnlike the former \"treasure of the phantom\"\x01",
            "《零の至宝》であるKeyaさんには\x01",
            "\"Time\" and \"sky\" power are provided.\x02\x03",
            "#10804FThe power of \"vision\" to interfere with causality and recognition\x01",
            "When the forces that interfere with space-time are combined ……\x02\x03",
            "#10811F\"Spinning the world#2RTo tie up#Power\x01",
            "Keyaさんは手に入れたのですわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6P#NLet's spin the world#2RTo tie up#Power ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D45")
    OP_FC(0xFFFA)
    Jump("loc_1D48")

    label("loc_1D45")

    OP_FC(0xFFF4)

    label("loc_1D48")


    ChrTalk(
        0x109,
        "#10111F#13PWell, that is ….\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1DB8")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D99")
    OP_FC(0xFFFA)
    Jump("loc_1D9C")

    label("loc_1D99")

    OP_FC(0xFFF4)

    label("loc_1D9C")


    ChrTalk(
        0x106,
        "#10712F#13Pthat is……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE2")
    OP_FC(0xFFFA)
    Jump("loc_1DE5")

    label("loc_1DE2")

    OP_FC(0xFFF4)

    label("loc_1DE5")


    ChrTalk(
        0x105,
        (
            "#10401F#13PAlso, words that are not ordinary\x01",
            "It came out …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1E24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E4E")
    OP_FC(0xFFFA)
    Jump("loc_1E51")

    label("loc_1E4E")

    OP_FC(0xFFF4)

    label("loc_1E51")


    ChrTalk(
        0x10A,
        "#00601F#13PWhat do you mean …?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1E75")

    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02203F#11PThat is the \"Plan for Aiki zero\"\x01",
            "The ability to say as a fundamental purpose ……\x02\x03",
            "#02201F\"Spinning the world\" -\x01",
            "Ie manipulating causality#22R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#,\x01",
            "Rearrange the world#16R噵 噵 噵 噵 噵 噵 噵 噵#That's power.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00305F#6P#N#4SHare ……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#12P#NLet's change the world … ….?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N#30W…… All of the events of the world have\x01",
            "Causality#4Rsystem#\"Network ……\x02\x03",
            "#00201FIn past, present and future\x01",
            "Ability to operate / change …?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhufu, as expected Tio\x01",
            "Swallowing is fast.\x02\x03",
            "#10800FYes, in the power net\x01",
            "To the authority that the top-level administrator can swing\x01",
            "There are something close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02201F#11PModify the reality itself that creates conflict,\x01",
            "We will switch to a more peaceful reality … …\x02\x03",
            "#02203FFor example, in the Empire and the Republic Crossbell\x01",
            "Reclaim reality subordinate · merciless … …\x02\x03",
            "#02200FCrossbell is at the top of the two countries\x01",
            "To the reality that reigns as a \"religious country\"\x01",
            "It is possible in principle to change.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#6P#Nな い …………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23B2")
    OP_FC(0xFFFA)
    Jump("loc_23B5")

    label("loc_23B2")

    OP_FC(0xFFF4)

    label("loc_23B5")


    ChrTalk(
        0x109,
        "#10101F#13PLet me see……?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_23D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2424")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2401")
    OP_FC(0xFFFA)
    Jump("loc_2404")

    label("loc_2401")

    OP_FC(0xFFF4)

    label("loc_2404")


    ChrTalk(
        0x10A,
        "#00610F#13PStupid …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2424")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2477")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244E")
    OP_FC(0xFFFA)
    Jump("loc_2451")

    label("loc_244E")

    OP_FC(0xFFF4)

    label("loc_2451")


    ChrTalk(
        0x106,
        "#10706F#13P……No way……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A1")
    OP_FC(0xFFFA)
    Jump("loc_24A4")

    label("loc_24A1")

    OP_FC(0xFFF4)

    label("loc_24A4")


    ChrTalk(
        0x105,
        (
            "#10410F#13P…… even the goddess\x01",
            "It is impossible practice … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_24E1")


    ChrTalk(
        0x104,
        (
            "#00307F#6P#NOoy and everything\x01",
            "Yota story is over past … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#N……As might be expected……\x01",
            "I can not believe in anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PCouscous……\x01",
            "You mean a funny thing?\x02\x03",
            "#10811F── You once again#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#,\x01",
            "It is helped#22R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#Although\x02",
        )
    )

    CloseMessageWindow()
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
        0x104,
        "#00305F#6P#NWhat……?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00105F#12P#NTo be saved, ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N…… No way … …\x01",
            "……… I saw that before ………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00010F#6P#NA few months ago, to the cult's lodge\x01",
            "When infiltrating ……! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis293.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis295.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis333.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis334.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    CreatePortrait(0, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis346.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    VolumeBGM(0x3C, 0x3E8)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x1, 0x47E, 0x47E, 0x5DC, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    Sound(3044, 255, 100, 0)
    Sleep(1500)
    BeginChrThread(0xF, 1, 0, 45)
    Sleep(2000)
    CreatePortrait(1, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis297.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x41A, 0x41A, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    FadeToBright(0, 16777215)
    Sleep(1500)
    StopSound(474, 2000, 90)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    VolumeBGM(0x64, 0x3E8)

    ChrTalk(
        0x101,
        "#00011F#6P#N#50W……………. Ah ………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PHuh, apparently Ms. Lloyd\x01",
            "It seems like \"I remembered\".\x02\x03",
            "#10804FIt's already very small once\x01",
            "Reality alterations are being made.\x02\x03",
            "#10811FYou are going to runaway Joachim#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "I got killed.#16R噵 噵 噵 噵 噵 噵 噵 噵#There is a reality alteration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N#30W……………………………………\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#6P#N#30W………… Seriously ……? …?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 8700, 0, 0)
    MoveCamera(354, 2, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13000, 4500)
    OP_0D()
    Sleep(300)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 38)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#11P#30WFirst time#8R噵 噵 噵 噵#…… Lloyd's are\x01",
            "With esters and lentils\x01",
            "I did not get along so much …\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x9, 0, 0, 39)
    Sleep(300)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#11PBecause of that it got aboard with just four people ……\x01",
            "…… Until that child's help comes in after all …\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 0, 0, 40)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0xA,
        (
            "#10800F#5Pそれを“識#2Rし#った”Keyaさんは\x01",
            "Make the power as \"treasure\" runaway\x01",
            "I interfered with the causal law in the past.\x02\x03",
            "#10804FAs a result, if you are an \"annihilated angel\"\x01",
            "The cause of solving the problem is led … …\x02\x03",
            "Around the tour, two Ravelite hookers\x01",
            "It appears in your assistant … …\x02\x03",
            "#10811FAnd - in the scene where you were originally killed\x01",
            "\"An exterminating angel\" came to help.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11870, 0)
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
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3007")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FD9")
    OP_FC(0xFFFA)
    Jump("loc_2FDC")

    label("loc_2FD9")

    OP_FC(0xFFF4)

    label("loc_2FDC")


    ChrTalk(
        0x109,
        "#10110F#13PWell, that's like that ….\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_30AE")

    label("loc_3007")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_305D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3031")
    OP_FC(0xFFFA)
    Jump("loc_3034")

    label("loc_3031")

    OP_FC(0xFFF4)

    label("loc_3034")


    ChrTalk(
        0x106,
        "#10708F#13P…… Such a thing ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_30AE")

    label("loc_305D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3087")
    OP_FC(0xFFFA)
    Jump("loc_308A")

    label("loc_3087")

    OP_FC(0xFFF4)

    label("loc_308A")


    ChrTalk(
        0x10A,
        "#00610F#13P…… Such a thing ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_30AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_311D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30D8")
    OP_FC(0xFFFA)
    Jump("loc_30DB")

    label("loc_30D8")

    OP_FC(0xFFF4)

    label("loc_30DB")


    ChrTalk(
        0x105,
        (
            "#10403F#13P… but ….\x01",
            "It looks like there is no lie indeed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_31FA")

    label("loc_311D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_318C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3147")
    OP_FC(0xFFFA)
    Jump("loc_314A")

    label("loc_3147")

    OP_FC(0xFFF4)

    label("loc_314A")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P… but ….\x01",
            "Even if it is a lie, it does not seem to be.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_31FA")

    label("loc_318C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31B6")
    OP_FC(0xFFFA)
    Jump("loc_31B9")

    label("loc_31B6")

    OP_FC(0xFFF4)

    label("loc_31B9")


    ChrTalk(
        0x106,
        (
            "#10703F#13P……but……\x01",
            "Even if it is a lie, it does not seem to be.\x02",
        )
    )

    OP_5A()
    OP_57(0x0)
    OP_5A()

    label("loc_31FA")

    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10804F#5PUhufu … indeed\x01",
            "It sounds like it was shocking, is not it?\x02\x03",
            "#10800FBut, with the \"treasure of zero\"\x01",
            "The essence of \"the power to rearrange the reality\" -\x02\x03",
            "To avoid your tragedy,\x01",
            "It is only the beginning.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1230, 7300, -3350, 0)
    MoveCamera(20, 3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43820, 0)
    MoveCamera(340, 4, 0, 45000)
    Call(0, 43)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#10804F#5PThis \"Big Tree\" ──\x02\x03",
            "Keyaさんの力を増幅し、\x01",
            "Through the Seven Okinawa, the world itself#8R噵 噵 噵 噵#When\x01",
            "If there is a shrine that can be linked ……\x02\x03",
            "#10811F#5PFar from being able to avoid tragedy,\x01",
            "At the level that the teacher mentioned earlier\x01",
            "It is possible to modify the reality.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00013F#6P#N……!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#12P#NThat is the power of this \"big tree\" …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N… … oooo …\x01",
            "You're getting fucked …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_353D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34EF")
    OP_FC(0xFFFA)
    Jump("loc_34F2")

    label("loc_34EF")

    OP_FC(0xFFF4)

    label("loc_34F2")


    ChrTalk(
        0x105,
        (
            "#10408F#13P(……Really……\x01",
            "It is the same as the original \"place of beginning\" … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_353D")


    ChrTalk(
        0xA,
        (
            "#10802F#5P#30WUhufu … … Is not it nice?\x02\x03",
            "#10809FSuch a lovely one#10R噵 噵 噵 噵 噵#If there is a\x01",
            "I am not scared of anything anymore …!\x02\x03",
            "Happiness is given to everything in the world,\x01",
            "I will not feel sorry!\x02\x03",
            "People are freed from every anxiety,\x01",
            "Only \"good things\" can be pursued!\x02\x03",
            "#10811FJust in the mystery of alchemy ─\x01",
            "Great mystery#12RAl-Magna#That is what!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#6P#NBell … …. you ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12870, 0)
    Call(0, 44)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#6P#N── Professor Ian.\x02\x03",
            "#00013FIs that really OK?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02201F#11P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02211F#11P…… I need preparation for everything.\x02\x03",
            "Human history, to every risk\x01",
            "It is also the history of how to deal with … …\x02\x03",
            "そしてKeya君はそれを制御できる\x01",
            "Have a great power.\x02\x03",
            "That is a fact that can not be denied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#Nその結果、Keyaをそんな場所に\x01",
            "Even if it is possible to push it in …?\x02\x03",
            "#00008FThe former \"treasure of the phantom\" is\x01",
            "Eventually he suffered a heart and extinguished himself\x01",
            "I heard that it came to the end.\x02\x03",
            "#00013FYou really are … …\x01",
            "Such heavy responsibility to one girl\x01",
            "Are you planning to press it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12300F#5P#NLloyd, that is ──\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PUhufu, as if not to be\x01",
            "We have ours.\x02\x03",
            "#10804FKeyaさんに世界改変の責任を\x01",
            "Rather than pressing everything ……\x02\x03",
            "An expert like a teacher\x01",
            "Change the world to \"more correct direction\"\x01",
            "I will advise the signposts …\x02\x03",
            "#10802FIf so, is the story different?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#N…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#NOnly, democratic process\x01",
            "I mean denying it all …?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P… … The evils of democracy\x01",
            "Ellie surely knows well.\x02\x03",
            "In any case, it fell into politics,\x01",
            "You can also decide important things quickly\x01",
            "A system that will become unwilling ……\x02\x03",
            "#02201FNot limited to crossbells,\x01",
            "Is not it a reality seen anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N#30W……that is……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02200F#11PBesides, with only myself, I got my own knowledge\x01",
            "Keya君に提示するつもりはない。\x02\x03",
            "#02203FEven experts like McDowell\x01",
            "I would like to request cooperation either.\x02\x03",
            "Dieter also,\x01",
            "From the viewpoint of management\x01",
            "It will be useful again.\x02\x03",
            "#02200FAnd ── you guys too,\x01",
            "We want us to cooperate with our attempt.\x02",
        )
    )

    CloseMessageWindow()
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

    ChrTalk(
        0x8,
        (
            "#02203F#11PIn order to open up a new era\x01",
            "You also need the opinions of the youngster.\x02\x03",
            "#02201FAnd if you guys ……\x02\x03",
            "If you guys arrived here,\x01",
            "What is necessary in the future times\x01",
            "You must know yourself.\x02\x03",
            "#02200FWhat are you thinking about this proposal?\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P#N#30W… … … that, such a thing …………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N#30WFucking …\x01",
            "It is strangely convincing, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#6P#N#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x1388)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#N…… Ian sensei.\x02\x03",
            "#00003FAfter all, in the previous question\x01",
            "I have not been answered yet?\x02\x03",
            "#00001F#6P#NThe teacher\x01",
            "Is that really OK?#24R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7543", 0)
    SetCameraDistance(11870, 10000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6P#N#30WEverything has \"dignity\".\x02\x03",
            "People, society, history as well.\x02\x03",
            "#00008FWrong or create a tragedy\x01",
            "Even if it leads to the result ……\x02\x03",
            "#00013FI decided not to have it#24R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#The\x01",
            "It is to commit the \"dignity\" of those involved.\x02\x03",
            "#00006FFor example, by recovering from a tragedy\x01",
            "As some people get the strength ……\x02\x03",
            "#00002FActually……\x01",
            "You also know the teacher, do not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x102,
        "#00102F#12P#N#30WLloyd …\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4339")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42E5")
    OP_FC(0xFFFA)
    Jump("loc_42E8")

    label("loc_42E5")

    OP_FC(0xFFF4)

    label("loc_42E8")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#30Wsurely……\x01",
            "People can only act correctly\x01",
            "It is not a possible existence … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_442E")

    label("loc_4339")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4363")
    OP_FC(0xFFFA)
    Jump("loc_4366")

    label("loc_4363")

    OP_FC(0xFFF4)

    label("loc_4366")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#30Wsurely……\x01",
            "People sometimes make mistakes\x01",
            "It is a existence that is committed.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_442E")

    label("loc_43B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_442E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43DF")
    OP_FC(0xFFFA)
    Jump("loc_43E2")

    label("loc_43DF")

    OP_FC(0xFFF4)

    label("loc_43E2")


    ChrTalk(
        0x106,
        (
            "#10708F#13P#30W……surely……\x01",
            "People sometimes make mistakes\x01",
            "Presence to commit ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_442E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4458")
    OP_FC(0xFFFA)
    Jump("loc_445B")

    label("loc_4458")

    OP_FC(0xFFF4)

    label("loc_445B")


    ChrTalk(
        0x105,
        (
            "#10401F#13P#30WBut that mistake\x01",
            "If it is decided not to be,\x01",
            "I can not grow up ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45D5")

    label("loc_44BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4548")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44E6")
    OP_FC(0xFFFA)
    Jump("loc_44E9")

    label("loc_44E6")

    OP_FC(0xFFF4)

    label("loc_44E9")


    ChrTalk(
        0x106,
        (
            "#10701F#13P#30WBut that mistake\x01",
            "If it is decided not to be\x01",
            "I can not grow up ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45D5")

    label("loc_4548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4572")
    OP_FC(0xFFFA)
    Jump("loc_4575")

    label("loc_4572")

    OP_FC(0xFFF4)

    label("loc_4575")


    ChrTalk(
        0x109,
        (
            "#10101F#13P#30WBut, that mistake\x01",
            "If you decide not to have it\x01",
            "I can not grow forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_45D5")


    ChrTalk(
        0x103,
        (
            "#00204F#12P#N#30W…… Learn both together,\x01",
            "Meaning of going ahead … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00300F#6P#N#30WCertainly, that's with a bagasari\x01",
            "It will be truncated.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5500, -6020, 0)
    MoveCamera(151, 30, 0, 0)
    MoveCamera(139, 30, 0, 20000)
    OP_6E(700, 0)
    SetCameraDistance(17340, 0)
    Call(0, 43)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_93(0x102, 0x0, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#5P#N#30W………… Lloyd ………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00004F#11P──Keya。\x01",
            "Let's go home with us.\x02\x03",
            "#00000FNo more, for us\x01",
            "There is no need to push yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N……… Well …………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… before us\x01",
            "Even when it is said that he lost his life ……\x02\x03",
            "It's hot and painful ……\x01",
            "I was sorrowful.\x02\x03",
            "#00006Fゴメンな、Keya。\x01",
            "Because we are unfriendly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#5P#N#30WThat's not true …!\x02\x03",
            "#12313F……あれはKeyaが\x01",
            "That's what I did arbitrarily …!\x02\x03",
            "So Lloyd is apologizing - ─\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#11PだったらKeya。\x02\x03",
            "#00013FWhy,\x01",
            "Do not you have a floating face?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#5P#N……!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#11PKeyaも気付いているんだろう？\x02\x03",
            "#00008FToo much sorrow for our death,\x01",
            "Manipulating causality\x01",
            "What has changed the reality … ….\x02\x03",
            "#00013FThat's it\x01",
            "That it was \"Zuru\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N#40W……………. Ah ………………\x02\x03",
            "#12308F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#11P……Keya………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, it is good that the dead ending was good\x01",
            "I can not say it …\x02\x03",
            "#00300FStill it is \"bad technique\"\x01",
            "I may be saying anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3500, -9100, 0)
    MoveCamera(125, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12860, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00106F#11P…… Ian sensei, bell.\x02\x03",
            "About that … …\x01",
            "I think that \"politics\" is also the same.\x02\x03",
            "#00108FSometimes it is not a royal road, a way offense\x01",
            "There are times when it is necessary.\x02\x03",
            "#00101FBut what assumes an evil way\x01",
            "It is still wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02201F#5P……… Eli … ……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10801F#5P…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PKeyaちゃんという個人の\x01",
            "To rely on transcendental force …\x02\x03",
            "It is no longer politics,\x01",
            "I can think only as a god-trust.\x02\x03",
            "#00108FDifficult situation, appropriate procedure and\x01",
            "Through the process of dialogue,\x01",
            "I will settle as a problem of everyone …\x02\x03",
            "#00101FI think that is \"true politics\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P多分、Keyaの力が無ければ\x01",
            "Crossbell is in a serious crisis\x01",
            "I think that the possibility of confronting it is high.\x02\x03",
            "#00008FTurmoil across the continent, economic crisis ……\x01",
            "And as the empire ceased civil war,\x01",
            "I will strip my fangs on the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(170, 3500, -8850, 800)
    OP_9B(0x1, 0x101, 0x0, 0xC8, 0x1F4, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00013F#11P── Even so,\x01",
            "Keyaに全てを押し付けるのが\x01",
            "I do not think it's a right choice.\x02\x03",
            "#00004FIf you rely on a miracle just to be given\x01",
            "We can not grow ourselves … …\x02\x03",
            "#00000FSo even if it is painful … …\x01",
            "I think that we should go through \"muscle\" now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W…………… Lloyd ………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x8,
        "#02203F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x13)
    OP_68(0, 3600, -9110, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11870, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(700)

    ChrTalk(
        0x8,
        "#02211F#11P#40W… … … until here?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 28)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40WOn your own … … as a grudge\x01",
            "I thought that it was not … …\x02\x03",
            "also……\x01",
            "It seems there was a cheating somewhere.\x02\x03",
            "#02200F… … as if you were a guy\x01",
            "Remark#2RSato#I felt as though it was being done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#N……teacher……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40W… … That's not done.\x01",
            "I was not obliged to tell you.\x02\x03",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1050, 4800, -5300, 0)
    MoveCamera(41, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17330, 0)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02203F#11P#30W……Keya君。\x01",
            "I made it awfully confusing.\x02\x03",
            "#02201FYou, at your own discretion ……\x01",
            "You should decide what to do.\x02\x03",
            "#02202FYou ought to be able to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W… … Sensei ………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02203F#11P#30WそしてMarybele君……\x01",
            "I can not live up to expectations.\x02\x03",
            "#02201FApparently my turn appears to be here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#6PUhufu … I do not mind.\x02\x03",
            "Originally to the teacher,\x01",
            "Planning comprehensive planning\x01",
            "Because it was only asking.\x02\x03",
            "#10811FI appreciate your hard work until now - the teacher.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    MoveCamera(63, 16, 0, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(13000, 1500)
    SetChrPos(0xA, -2000, 3000, -4850, 90)
    SetChrPos(0x8, 0, 3000, -5850, 270)
    OP_0D()
    OP_93(0xC, 0x5A, 0x0)
    Sleep(300)

    def lambda_548E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_548E)
    BeginChrThread(0xC, 3, 0, 33)
    Sleep(250)

    def lambda_54A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_54A8)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(150)
    BeginChrThread(0xA, 0, 0, 29)
    Sleep(350)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x7D0)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 30)
    OP_68(5000, 3200, -8150, 1000)
    MoveCamera(100, 12, 0, 1000)
    SetCameraDistance(22300, 1000)
    WaitChrThread(0xA, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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
    Sleep(500)

    def lambda_55D1():

        label("loc_55D1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_55D1")

    QueueWorkItem2(0x101, 2, lambda_55D1)

    def lambda_55E3():

        label("loc_55E3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_55E3")

    QueueWorkItem2(0x102, 2, lambda_55E3)

    def lambda_55F5():

        label("loc_55F5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_55F5")

    QueueWorkItem2(0x103, 2, lambda_55F5)

    def lambda_5607():

        label("loc_5607")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5607")

    QueueWorkItem2(0x104, 2, lambda_5607)

    def lambda_5619():

        label("loc_5619")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5619")

    QueueWorkItem2(0xF4, 2, lambda_5619)

    def lambda_562B():

        label("loc_562B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_562B")

    QueueWorkItem2(0xF5, 2, lambda_562B)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x8,
        "#02212F#11P#10A… …. ugh …\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12313F#NIt is! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#12P#NBecome Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#12P#N… …. Bell …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7585", 0)
    Fade(500)
    OP_68(4920, 3700, -12390, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7630, 0)
    SetChrPos(0xA, -90, 3000, -5290, 180)
    SetChrPos(0x8, 9400, 700, -9900, 270)
    BeginChrThread(0x8, 0, 0, 31)
    SetCameraDistance(5610, 5000)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#02213F#11P#60W……my mother……\x01",
            "… …. This is also … … causal response … ….\x02\x03",
            "#70WGuy … … Lloyd … …\x01",
            "…………………………………\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 32)
    WaitChrThread(0x8, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00207F#5PMr. Ian … …!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_582C")

    ChrTalk(
        0x10A,
        "#00610F#5PWhat a thing …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5893")

    label("loc_582C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5861")

    ChrTalk(
        0x109,
        "#10110F#5PWhat a thing …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5893")

    label("loc_5861")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5893")

    ChrTalk(
        0x106,
        "#10707F#5P…… what a thing ……\x02",
    )

    CloseMessageWindow()

    label("loc_5893")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-460, 3700, -1780, 0)
    MoveCamera(353, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16600, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x1000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x80)

    def lambda_5900():
        TurnDirection(0x101, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5900)
    Sleep(0)

    def lambda_5910():
        TurnDirection(0x102, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5910)
    Sleep(0)

    def lambda_5920():
        TurnDirection(0x103, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5920)
    Sleep(0)

    def lambda_5930():
        TurnDirection(0x104, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5930)
    Sleep(0)

    def lambda_5940():
        TurnDirection(0xF4, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5940)
    Sleep(0)

    def lambda_5950():
        TurnDirection(0xF5, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5950)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#12PBell … why! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#5PUfufu, unusable tool#4R噵 噵#To\x01",
            "It was only to dispose of it.\x02\x03",
            "#10811Fその意味では、Keyaさん。\x01",
            "── You are not an exception, are you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 33)
    WaitChrThread(0xA, 3)
    Sound(686, 0, 80, 0)
    PlayEffect(0x8, 0x6, 0xA, 0x1, 250, 2200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Fade(500)
    OP_68(0, 8600, -740, 0)
    MoveCamera(354, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15100, 0)
    SetCameraDistance(16650, 4000)
    Call(0, 44)
    SetChrPos(0x9, 300, 8400, -3000, 180)
    OP_0D()
    PlayEffect(0x7, 0xFF, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(283, 0, 100, 0)
    Sound(961, 2, 70, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3646V#5P#50W#18A… … Wow …! Is it?\x02",
        )
    )

    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0x320)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    StopEffect(0x6, 0x2)
    BeginChrThread(0x9, 0, 0, 42)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x101,
        "#00007F#5PKeya……！？\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PHey……!\x01",
            "What are you doing to my child! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#10804F#5PIf you get lost anymore\x01",
            "Like a lovely doll without a will\x01",
            "Just to get it ……\x02\x03",
            "#10811FOriginally, by the secret art of the Clois family\x01",
            "An artificial human given life#8RHomunculus#… ….\x02\x03",
            "How to treat\x01",
            "Is not my selfishness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PDo not be silly …!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#11PBell …!\x01",
            "There are good things to say and bad things! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00207F#5P…… I will withdraw … …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0xBB8)
    StopSound(961, 3000, 60)
    Fade(500)
    OP_68(200, 2700, -9200, 0)
    MoveCamera(359, 4, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(15330, 0)
    SetCameraDistance(12330, 42000)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0xF4, 0, 0, 24)
    BeginChrThread(0xF5, 0, 0, 25)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10802.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xA,
        (
            "#3791V#40W#36AHehehe … … would be nice.\x02\x03",
            "#3792V#25AわたくしはMarybele・クロイス。\x02\x03",
            "#3793V#50ASeeking \"treasure\" that exceeds the goddess,\x01",
            "Descendants of the family who has sacrificed everything.\x02\x03",
            "#3794V#71AThe weight of that millennium 's imbalance,\x01",
            "The bond that does not satisfy your year\x01",
            "Which is really strong ……\x02\x03",
            "#3795V#35ATogether with each other dead\x01",
            "Shall I compare it?\x02",
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
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#6P#30W#15A…… I hope!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#30W#20A#NBell …!\x01",
            "I will not hold back!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6079")
    OP_FC(0x6)
    Jump("loc_607C")

    label("loc_6079")

    OP_FC(0xC)

    label("loc_607C")


    ChrTalk(
        0x105,
        (
            "#10407F#13P#30W#25A#NThe highest ranked magician#6RMagis#Certified …!\x01",
            "We will control by all means!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61CF")

    label("loc_60D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6158")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6100")
    OP_FC(0x6)
    Jump("loc_6103")

    label("loc_6100")

    OP_FC(0xC)

    label("loc_6103")


    ChrTalk(
        0x106,
        (
            "#10707F#13P#30W#25A#NJetty black power#4RBulb#Sense …!\x01",
            "I will surrender with full power!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61CF")

    label("loc_6158")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6182")
    OP_FC(0x6)
    Jump("loc_6185")

    label("loc_6182")

    OP_FC(0xC)

    label("loc_6185")


    ChrTalk(
        0x109,
        (
            "#10107F#13P#30W#25A#NEstimated risk level S … …!\x01",
            "I will intercept with full firepower!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61CF")

    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    OP_24(0x1DA)
    OP_24(0x3C1)
    Battle("BattleInfo_2C0", 0x30200011, 0x0, 0x100, 0x41, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 46)
    Return()

    # Function_6_695 end

    def Function_7_61FD(): pass

    label("Function_7_61FD")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_623C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_623C)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_7_61FD end

    def Function_8_6267(): pass

    label("Function_8_6267")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_62A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_62A6)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_8_6267 end

    def Function_9_62D1(): pass

    label("Function_9_62D1")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6310():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6310)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_9_62D1 end

    def Function_10_633B(): pass

    label("Function_10_633B")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_637A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_637A)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_10_633B end

    def Function_11_63A5(): pass

    label("Function_11_63A5")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_63E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_63E4)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_11_63A5 end

    def Function_12_640F(): pass

    label("Function_12_640F")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_644E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_644E)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_12_640F end

    def Function_13_6479(): pass

    label("Function_13_6479")

    OP_95(0xFE, 0, 1000, -12060, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_6479 end

    def Function_14_6495(): pass

    label("Function_14_6495")

    Sleep(50)
    OP_95(0xFE, 1120, 1000, -13300, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_6495 end

    def Function_15_64B4(): pass

    label("Function_15_64B4")

    Sleep(100)
    OP_95(0xFE, 420, 1000, -14370, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_64B4 end

    def Function_16_64D3(): pass

    label("Function_16_64D3")

    Sleep(150)
    OP_95(0xFE, -1270, 1000, -13930, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_64D3 end

    def Function_17_64F2(): pass

    label("Function_17_64F2")

    Sleep(200)
    OP_95(0xFE, -2540, 1990, -13310, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_64F2 end

    def Function_18_6511(): pass

    label("Function_18_6511")

    Sleep(250)
    OP_95(0xFE, 2540, 1000, -13510, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_6511 end

    def Function_19_6530(): pass

    label("Function_19_6530")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_6530 end

    def Function_20_6542(): pass

    label("Function_20_6542")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_6542 end

    def Function_21_6551(): pass

    label("Function_21_6551")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_6551 end

    def Function_22_6563(): pass

    label("Function_22_6563")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_6563 end

    def Function_23_6575(): pass

    label("Function_23_6575")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_6575 end

    def Function_24_6581(): pass

    label("Function_24_6581")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65A1")
    Sound(540, 0, 50, 0)
    Jump("loc_65C6")

    label("loc_65A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65C6")
    Sound(531, 0, 100, 0)

    label("loc_65C6")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_6581 end

    def Function_25_65CF(): pass

    label("Function_25_65CF")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65EF")
    Sound(540, 0, 50, 0)
    Jump("loc_6614")

    label("loc_65EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6614")
    Sound(531, 0, 100, 0)

    label("loc_6614")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_65CF end

    def Function_26_661D(): pass

    label("Function_26_661D")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x10)
    Sleep(150)
    SetChrSubChip(0xFE, 0x11)
    Sound(318, 0, 60, 0)
    Sleep(350)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    Return()

    # Function_26_661D end

    def Function_27_6653(): pass

    label("Function_27_6653")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x11)
    Sound(318, 0, 60, 0)
    Sleep(350)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    Return()

    # Function_27_6653 end

    def Function_28_6690(): pass

    label("Function_28_6690")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    SetChrSubChip(0xFE, 0x12)
    Sleep(150)
    Sound(318, 0, 60, 0)
    SetChrSubChip(0xFE, 0x11)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xFE, 0x10)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_6690 end

    def Function_29_66E2(): pass

    label("Function_29_66E2")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x2, 0, 50, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(887, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(600)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Sound(246, 0, 100, 0)
    Sound(255, 0, 100, 0)
    Sound(874, 0, 90, 0)
    OP_82(0x64, 0x64, 0x7D0, 0x12C)
    Sleep(50)
    Sound(251, 0, 100, 0)
    PlayEffect(0x2, 0x0, 0x8, 0x1, 0, 500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    Return()

    # Function_29_66E2 end

    def Function_30_6802(): pass

    label("Function_30_6802")

    StopEffect(0x2, 0x0)
    PlayEffect(0x5, 0x2, 0x8, 0x5, 0, 750, 0, 20536, 0, 0, 670, 670, 670, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x2968, 0xBB8, 0xFFFFD634, 0x2EE, 0xBB8)
    StopEffect(0x1, 0x0)
    PlayEffect(0x5, 0x2, 0x8, 0x5, -400, 500, 400, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x32, 0x7D0, 0x12C)
    StopEffect(0x0, 0x2)
    Sound(886, 0, 100, 0)
    Sound(815, 0, 100, 0)
    Sound(833, 0, 60, 0)
    OP_9D(0xFE, 0x2774, 0x6A4, 0xFFFFD7C4, 0x96, 0x2BC)
    StopEffect(0x0, 0x2)
    OP_9D(0xFE, 0x2580, 0x2BC, 0xFFFFD954, 0x32, 0x2BC)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sound(811, 0, 100, 0)
    Sleep(20)
    Sound(862, 0, 40, 0)
    Return()

    # Function_30_6802 end

    def Function_31_6951(): pass

    label("Function_31_6951")

    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)

    label("loc_696F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69C5")
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(1600)
    Jump("loc_696F")

    label("loc_69C5")

    Return()

    # Function_31_6951 end

    def Function_32_69C6(): pass

    label("Function_32_69C6")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(600)
    Return()

    # Function_32_69C6 end

    def Function_33_69E2(): pass

    label("Function_33_69E2")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_33_69E2 end

    def Function_34_69F7(): pass

    label("Function_34_69F7")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_34_69F7 end

    def Function_35_6A06(): pass

    label("Function_35_6A06")

    SetChrPos(0x8, 9600, 700, -9900, 305)
    SetChrChipByIndex(0x8, 0x21)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x5)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_35_6A06 end

    def Function_36_6A71(): pass

    label("Function_36_6A71")

    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(429)
    Return()

    # Function_36_6A71 end

    def Function_37_6A87(): pass

    label("Function_37_6A87")

    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_37_6A87 end

    def Function_38_6A9D(): pass

    label("Function_38_6A9D")

    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(500)
    Return()

    # Function_38_6A9D end

    def Function_39_6AB3(): pass

    label("Function_39_6AB3")

    SetChrSubChip(0xFE, 0x12)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(667)
    Return()

    # Function_39_6AB3 end

    def Function_40_6AC9(): pass

    label("Function_40_6AC9")

    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(667)
    Return()

    # Function_40_6AC9 end

    def Function_41_6ADF(): pass

    label("Function_41_6ADF")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_41_6ADF end

    def Function_42_6AFC(): pass

    label("Function_42_6AFC")

    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_42_6AFC end

    def Function_43_6B19(): pass

    label("Function_43_6B19")

    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    Return()

    # Function_43_6B19 end

    def Function_44_6B28(): pass

    label("Function_44_6B28")

    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    Return()

    # Function_44_6B28 end

    def Function_45_6B37(): pass

    label("Function_45_6B37")

    Sound(474, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DA, 0xA)
    Sleep(100)
    OP_25(0x1DA, 0x14)
    Sleep(100)
    OP_25(0x1DA, 0x1E)
    Sleep(100)
    OP_25(0x1DA, 0x28)
    Sleep(100)
    OP_25(0x1DA, 0x32)
    Sleep(100)
    OP_25(0x1DA, 0x3C)
    Sleep(100)
    OP_25(0x1DA, 0x46)
    Sleep(100)
    OP_25(0x1DA, 0x50)
    Sleep(100)
    OP_25(0x1DA, 0x5A)
    Sleep(100)
    OP_25(0x1DA, 0x64)
    Return()

    # Function_45_6B37 end

    def Function_46_6B84(): pass

    label("Function_46_6B84")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadChrToIndex("chr/ch03751.itc", 0x29)
    LoadChrToIndex("chr/ch03753.itc", 0x2B)
    LoadChrToIndex("apl/ch51748.itc", 0x2C)
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev17077.eff")
    LoadEffect(0x2, "battle/cr036301.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    LoadEffect(0x6, "event/ev17076.eff")
    LoadEffect(0x7, "event/ev17075.eff")
    SoundLoad(3408)
    SoundLoad(3331)
    SoundLoad(3332)
    SoundLoad(3333)
    SoundLoad(3334)
    SoundLoad(3335)
    SoundLoad(2775)
    SoundLoad(2695)
    SoundLoad(3796)
    SoundLoad(3797)
    SoundLoad(3798)
    SoundLoad(3646)
    SoundLoad(3647)
    SoundLoad(3648)
    SoundLoad(961)
    SoundLoad(979)
    SoundLoad(1029)
    SoundLoad(960)
    SetChrPos(0x101, 0, 950, -11860, 0)
    SetChrPos(0x102, 1120, 950, -13300, 0)
    SetChrPos(0x103, 420, 950, -14370, 0)
    SetChrPos(0x104, -1270, 950, -13930, 0)
    SetChrPos(0xF4, -2540, 950, -13310, 0)
    SetChrPos(0xF5, 2540, 950, -13510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x27)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x6)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrPos(0x9, 0, 8000, -750, 180)
    SetChrPos(0x9, 100, 8400, -3000, 180)
    PlayEffect(0x0, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x7, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3000, -5850, 180)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0xB)
    ClearChrFlags(0xB, 0x80)
    OP_68(0, 3500, -6800, 0)
    MoveCamera(340, 1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    Sound(961, 2, 50, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 3500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 3900, -5840, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15300, 0)
    SetCameraDistance(14300, 3000)
    OP_6F(0x79)
    Sound(934, 0, 40, 0)
    Sound(283, 0, 30, 0)
    Fade(500)
    OP_68(0, 8300, 1820, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18900, 0)
    SetCameraDistance(17000, 4000)
    OP_0D()
    StopSound(961, 3000, 40)
    StopEffect(0x7, 0x2)
    PlayEffect(0x6, 0xFF, 0x9, 0x1, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x9, 3, 0, 48)
    WaitChrThread(0x9, 3)
    Sleep(300)
    Sleep(1700)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#60W…… Fuu … … ha ha … ….\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5500, -6020, 0)
    MoveCamera(221, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17340, 0)
    SetChrPos(0x9, 0, 8000, -750, 180)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#5P#4SKeya、大丈夫か！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#N#45W…… um … …\x01",
            "Err …… somehow ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00214F#5PWas good……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PWell, I'm glad … …\x02",
    )

    CloseMessageWindow()

    def lambda_70AE():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_70AE)
    WaitChrThread(0xA, 2)
    Sleep(500)
    PlayBGM("ed7572", 0)

    ChrTalk(
        0xA,
        (
            "#10803F#11P#30WCut … … I see.\x02\x03",
            "#10801FAs expected, Arios\x01",
            "There seems to be only a dismissal ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBell … … so far!\x02\x03",
            "#00101FNo more,\x01",
            "There is no meaning for us to fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11P#30WUhufu, my pretty Ellie.\x02\x03",
            "With your request,\x01",
            "I do not think so, but …\x02\x03",
            "#10811FYou probably know … ….?\x01",
            "I am as pretty as a cute one\x01",
            "It is a personality that makes me want to get caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PWhat?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1060, 5500, -5020, 0)
    MoveCamera(223, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10930, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10802F#5P#30W──ところでKeyaさん。\x02\x03",
            "Mr. Lloyd is \"that thing\"\x01",
            "I wonder if she knows … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#N#30W………….. Ah ………………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhufu, in its appearance\x01",
            "Does not it seem to tell?\x02\x03",
            "#10811FIt's just fine, even here they\x01",
            "Shall I tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#11P#N#30WOr … no … stop … …\x02\x03",
            "#12311F…… Belle … … please …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#5P…… What do you mean …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PShe is a lady!\x02\x03",
            "Sorry for my key stomach\x01",
            "Is not it an Ezimen!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#11PUhufu, you really are\x01",
            "Keyaさんを愛しているのですね？\x02\x03",
            "#10800FThe Clois family entrusted to the \"cult\"\x01",
            "An artificial man who does not have a real soul#8RHomunculus#… ….\x02\x03",
            "A number of souls sacrificed by the cult\x01",
            "Just the joined dummy dolls.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5PNow, what about it! Is it?\x02\x03",
            "#00010FSuch a long time ago,\x01",
            "I heard from Zeit know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PKeyaがKeyaとして\x01",
            "What is at our side ……\x02\x03",
            "#00201FMore than that\x01",
            "There should not be important things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11Pうふふ、Keyaさん。\x01",
            "You are a really happy person, do not you?\x02\x03",
            "Lloyd's … …\x01",
            "No, of all the people involved\x01",
            "I was able to gather goodwill and love.\x02\x03",
            "#10811F── Depending on your power#16R噵 噵 噵 噵 噵 噵 噵 噵#.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x9, 0xA)
    OP_68(0, 9400, 5350, 0)
    MoveCamera(357, -11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(19000, 4000)
    OP_0D()
    SetChrSubChip(0x9, 0x16)
    Sleep(125)
    SetChrSubChip(0x9, 0x17)
    Sleep(300)

    def lambda_782A():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_782A)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_784A():
        OP_A6(0xFE, 0x0, 0x32, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_784A)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 4700, 5350, 0)
    MoveCamera(0, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    SetCameraDistance(30500, 3500)
    OP_0D()
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

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#50W……… ぅ ぅ ぅ ……… ぁ ぁ …………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00005F#6P#N……Huh………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#N…… Bell ……\x01",
            "Now, what …?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10811F#11P#30WKuku … you are\x01",
            "Did not she wonder?\x02\x03",
            "Perhaps, since I first met him\x01",
            "Keyaさんが愛しくて、守りたくて\x01",
            "There was no choice.\x02\x03",
            "Why do you think that … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#N…… No way … … …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#6P#NHey, what are you stupid ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis298.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis299.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis300.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10804F#11P#30W── That Joachim, of course,\x01",
            "マフィアや魔獣ですらKeyaさんを\x01",
            "I did not actively harm it.\x02\x03",
            "Become friends immediately with anyone,\x01",
            "A girl who is unconditionally loved … …\x02\x03",
            "#10811FThat abnormality#4R噵 噵#Sakura, as no one\x01",
            "Were not you wondering?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(0, 4200, 5350, 20000)
    MoveCamera(0, 12, 0, 20000)
    OP_6E(700, 20000)
    SetCameraDistance(26810, 20000)
    SetChrSubChip(0x9, 0x16)
    Sleep(125)
    SetChrSubChip(0x9, 0xA)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#3647V#5P#N#50W#30A……… Different …… Different ………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0xA,
        "#10803F#11P#30W#15ANo ─ ─ no.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#10801F#11P#40W#30AUnconsciously to you\x01",
            "There is the ability to grasp the heart and soul of the surrounding human being.\x02\x03",
            "#10804F#40W#30AAs everyone loves you and protects you,\x01",
            "The power to manipulate causality and recognition.\x02\x03",
            "#10811F#40W#30AKuku …… to the existence of confusion\x01",
            "Is not it a love of confusion?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0xF, 1, 0, 53)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 50)
    WaitChrThread(0x9, 3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2000)
    OP_68(0, 6900, 5350, 2000)
    MoveCamera(0, 12, 0, 2000)
    SetCameraDistance(20000, 2000)
    FadeToDark(3000, 16777215, -1)
    OP_82(0x0, 0xC8, 0xBB8, 0x3E8)
    BeginChrThread(0xF, 2, 0, 56)
    PlayEffect(0x2, 0xFF, 0x9, 0x1, 0, 750, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3648V#11P#N#4S#20A#80WNo, ah ah ah ─ ─ ─ ─ ─ ─!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sound(934, 0, 100, 0)
    Sleep(1500)
    Sound(689, 0, 100, 0)
    Sound(694, 0, 80, 0)
    Sound(979, 2, 70, 0)
    Sleep(2000)
    FadeToBright(3000, 16777215)
    OP_68(0, 4400, 5350, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26910, 0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xB, 0, 10000, 0, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    Fade(1500)
    OP_68(1790, 5450, -470, 0)
    MoveCamera(298, 62, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(47700, 0)
    OP_68(0, 7000, 5350, 9000)
    MoveCamera(0, 19, 0, 9000)
    OP_6E(700, 9000)
    SetCameraDistance(31170, 9000)
    BeginChrThread(0xF, 3, 0, 54)
    OP_71(0x0, 0x7D1, 0x7F8, 0x0, 0x20)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    OP_0D()
    Sleep(1500)
    OP_6F(0x79)
    CancelBlur(0)
    Sound(1030, 0, 100, 0)
    Fade(500)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    EndChrThread(0xF, 0x3)
    BeginChrThread(0xB, 3, 0, 51)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(0, 11600, 0, 1000)
    MoveCamera(0, 22, 0, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(21500, 1000)
    OP_0D()
    OP_6F(0x79)
    Sleep(2000)
    Sound(1031, 0, 100, 0)
    Sleep(700)
    OP_68(-1150, 11100, -650, 0)
    MoveCamera(10, 4, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27140, 0)
    CancelBlur(1500)
    Fade(500)
    BeginChrThread(0xB, 3, 0, 52)
    OP_68(570, 11200, -130, 0)
    MoveCamera(7, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19270, 0)
    OP_68(570, 10900, -130, 100000)
    MoveCamera(4, -13, 0, 10000)
    SetCameraDistance(23130, 10000)
    Sleep(3000)

    ChrTalk(
        0x102,
        "#00110F#5P#40W#20A………….. Ah ………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8281")
    OP_FC(0x5)
    Jump("loc_8284")

    label("loc_8281")

    OP_FC(0xB)

    label("loc_8284")


    ChrTalk(
        0x105,
        "#10410F#13P#40W#20A…… This shrine ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_836F")

    label("loc_82B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8311")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82DE")
    OP_FC(0x5)
    Jump("loc_82E1")

    label("loc_82DE")

    OP_FC(0xB)

    label("loc_82E1")


    ChrTalk(
        0x106,
        "#10707F#13P#40W#20AHere, this shinki …\x02",
    )

    CloseMessageWindow()
    Jump("loc_836F")

    label("loc_8311")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_836F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_833B")
    OP_FC(0x5)
    Jump("loc_833E")

    label("loc_833B")

    OP_FC(0xB)

    label("loc_833E")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20A…… Here, this light ………\x02",
    )

    CloseMessageWindow()

    label("loc_836F")

    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_839C")
    OP_FC(0x5)
    Jump("loc_839F")

    label("loc_839C")

    OP_FC(0xB)

    label("loc_839F")


    ChrTalk(
        0x10A,
        "#00610F#13P#40W#20AAoi … … \"God\" … …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_848A")

    label("loc_83D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8430")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83FB")
    OP_FC(0x5)
    Jump("loc_83FE")

    label("loc_83FB")

    OP_FC(0xB)

    label("loc_83FE")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20AAoi … … \"God\" … …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_848A")

    label("loc_8430")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_848A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_845A")
    OP_FC(0x5)
    Jump("loc_845D")

    label("loc_845A")

    OP_FC(0xB)

    label("loc_845D")


    ChrTalk(
        0x106,
        "#10700F#13P#40W#20AAoi … … \"God\" … …?\x02",
    )

    CloseMessageWindow()

    label("loc_848A")

    Sleep(300)
    CancelBlur(500)
    Fade(1000)
    OP_68(-180, 7400, -1300, 0)
    MoveCamera(359, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(38490, 0)
    OP_68(-180, 7400, -1300, 20000)
    MoveCamera(359, -3, 0, 20000)
    OP_6E(700, 20000)
    SetCameraDistance(28230, 20000)
    OP_0D()
    Sleep(500)
    StopBGM(0x7D0)
    StopSound(979, 4000, 60)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x101,
        "#00007F#3331V#6P#N#4S#25AKeyaぁぁ───ッ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7459", 0)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 47)
    WaitChrThread(0xA, 0)
    Sleep(500)
    OP_68(-370, 12190, -1650, 60000)
    MoveCamera(359, -3, 0, 60000)
    OP_6E(700, 60000)
    SetCameraDistance(14000, 60000)

    ChrTalk(
        0xA,
        (
            "#10804F#3796V#6P#N#40W#82AKuku, this is \"the treasure of zero\"\x01",
            "\"A big tree\" is completely integrated\x01",
            "In the end, the form of the beginning …\x02\x03",
            "#3797V#80AIt manipulates all time-space causality,\x01",
            "Defeat the \"shackles\" imposed by the goddess\x01",
            "True to false ground God … …!\x02\x03",
            "#10811F#3798V#35A《碧の虚 神#5RDemiurgos#》ですわ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00010F#3332V#6P#N#30W#25AI was aware that such a trust!\x02\x03",
            "#3333V#35A全てはKeyaを……\x01",
            "You have regained that girl!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#2775V#6P#N#30W#32AOh, what a difficult story is\x01",
            "Even then it will not be late!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#2695V#12P#N#30W#40A── Confirm the manifestation of the giant creature!\x01",
            "中枢のコア部分にKeyaがいます！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#3408V#12P#N#30W#32AAnyhow from there\x01",
            "Keyaちゃんを解放しないと！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00015F#3334V#6P#N#30AEveryone\x01",
            "This is the last battle …!\x02\x03",
            "#00007F#3335V#50AWhole body, all of us\x01",
            "I will hit that blue sky!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8922")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8919")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_8922")

    label("loc_8919")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_8922")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8955")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_894F")
    Sound(2417, 255, 100, 4)
    Jump("loc_8955")

    label("loc_894F")

    Sound(2417, 255, 100, 3)

    label("loc_8955")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8988")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8982")
    Sound(4115, 255, 100, 4)
    Jump("loc_8988")

    label("loc_8982")

    Sound(4115, 255, 100, 3)

    label("loc_8988")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B5")
    Sound(3174, 255, 100, 4)
    Jump("loc_89BB")

    label("loc_89B5")

    Sound(3174, 255, 100, 3)

    label("loc_89BB")

    SetChrName("Members")

    AnonymousTalk(
        0xFF,
        "#5S#15AHuh! It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0xF, 0x3)
    SetScenarioFlags(0x0, 0)
    Sound(960, 0, 100, 0)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFF, 0x0)
    SetMapFlags(0x2000000)
    OP_C9(0x0, 0x8)
    Battle("BattleInfo_304", 0x30200012, 0x0, 0x100, 0x1E, 0xFF)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    OP_C9(0x0, 0x8)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_348", 0x30200012, 0x0, 0x100, 0x1F, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1770)
    WaitBGM()
    ClearMapFlags(0x2000000)
    Call(0, 57)
    Return()

    # Function_46_6B84 end

    def Function_47_8A6A(): pass

    label("Function_47_8A6A")

    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)
    Sound(809, 0, 40, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x3E8, 0x15E, 0x3E8)
    Sound(326, 0, 20, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_47_8A6A end

    def Function_48_8AB9(): pass

    label("Function_48_8AB9")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(429)
    Return()

    # Function_48_8AB9 end

    def Function_49_8AE3(): pass

    label("Function_49_8AE3")

    Sound(898, 0, 100, 0)
    Return()

    # Function_49_8AE3 end

    def Function_50_8AEA(): pass

    label("Function_50_8AEA")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(400)
    Return()

    # Function_50_8AEA end

    def Function_51_8B06(): pass

    label("Function_51_8B06")

    Sound(340, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sound(889, 0, 60, 0)
    OP_87(0x1, 0x1, 0x0, "891body:Layer2(4)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_74(0x0, 0xA)
    Sound(694, 0, 100, 0)
    OP_71(0x0, 0x803, 0x80C, 0x0, 0x0)
    OP_79(0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_71(0x0, 0x80D, 0x820, 0x0, 0x20)
    Return()

    # Function_51_8B06 end

    def Function_52_8B84(): pass

    label("Function_52_8B84")

    OP_71(0x0, 0x821, 0x82A, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xF, 3, 0, 55)
    OP_71(0x0, 0x835, 0x85B, 0x0, 0x20)
    Return()

    # Function_52_8B84 end

    def Function_53_8BA6(): pass

    label("Function_53_8BA6")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7460", 0)
    Return()

    # Function_53_8BA6 end

    def Function_54_8BB4(): pass

    label("Function_54_8BB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BCD")
    Sound(824, 0, 100, 0)
    Sleep(1300)
    Jump("Function_54_8BB4")

    label("loc_8BCD")

    Return()

    # Function_54_8BB4 end

    def Function_55_8BCE(): pass

    label("Function_55_8BCE")

    Sleep(200)

    label("loc_8BD1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BEA")
    Sound(824, 0, 50, 0)
    Sleep(3800)
    Jump("loc_8BD1")

    label("loc_8BEA")

    Return()

    # Function_55_8BCE end

    def Function_56_8BEB(): pass

    label("Function_56_8BEB")

    Sound(929, 0, 50, 0)
    Sleep(500)
    Sound(940, 0, 100, 0)
    Sleep(200)
    Sound(936, 0, 100, 0)
    Sound(1029, 0, 100, 0)
    Return()

    # Function_56_8BEB end

    def Function_57_8C0A(): pass

    label("Function_57_8C0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 97)
    LoadChrToIndex("apl/ch51747.itc", 0x1E)
    LoadChrToIndex("chr/ch00001.itc", 0x1F)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Call(0, 2)
    Call(0, 3)
    LoadChrToIndex("chr/ch03750.itc", 0x28)
    LoadEffect(0x0, "battle/bs891090.eff")
    LoadEffect(0x1, "battle/bs891062.eff")
    LoadEffect(0x2, "event/ev17070.eff")
    LoadEffect(0x3, "event/ev17071.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    LoadEffect(0x5, "event\\ev500_00.eff")
    SoundLoad(3409)
    SoundLoad(2925)
    SoundLoad(3531)
    SoundLoad(2776)
    SoundLoad(2696)
    SoundLoad(3264)
    SoundLoad(825)
    SoundLoad(961)
    SoundLoad(832)
    SoundLoad(676)
    SetChrPos(0x101, 0, 950, -11860, 0)
    SetChrPos(0x102, 1120, 950, -13300, 0)
    SetChrPos(0x103, 420, 950, -14370, 0)
    SetChrPos(0x104, -1270, 950, -13930, 0)
    SetChrPos(0xF4, -2540, 950, -13310, 0)
    SetChrPos(0xF5, 2540, 950, -13510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x27)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x17)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrPos(0x9, 0, 14600, -1150, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x5, 0xFF, 0x9, 0x41, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 14600, -1150, 180)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -3500, 3000, -4150, 45)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xB)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 3, 0, 58)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0xB, 0, 10000, 0, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    OP_68(0, 11400, -1880, 0)
    MoveCamera(0, -15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    Sound(825, 2, 100, 0)
    Sleep(300)
    Sound(843, 0, 100, 0)
    Sound(934, 0, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x1, 0, 4000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    FadeToBright(1000, 0)
    SetCameraDistance(27000, 4000)
    OP_0D()
    Sleep(2000)
    BeginChrThread(0xB, 3, 0, 59)
    BeginChrThread(0x9, 0, 0, 60)
    Sleep(2000)
    StopSound(825, 2000, 100)
    CancelBlur(500)
    Fade(500)
    OP_68(30, 14600, -310, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13330, 0)
    Sleep(3500)
    Sound(231, 0, 70, 0)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_68(30, 4600, -310, 5500)
    Sleep(5900)
    OP_68(0, 3400, 250, 5000)
    MoveCamera(0, 14, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(17750, 5000)
    Sleep(500)
    StopSound(832, 2000, 100)

    def lambda_904B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_904B)
    OP_75(0x1, 0x1, 0x5DC)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 2300, -7800, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    SetCameraDistance(14700, 30000)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 63)
    BeginChrThread(0x102, 0, 0, 64)
    BeginChrThread(0x103, 0, 0, 65)
    BeginChrThread(0x104, 0, 0, 66)
    BeginChrThread(0xF4, 0, 0, 67)
    BeginChrThread(0xF5, 0, 0, 68)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00310F#6PCut … What! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PKeyaちゃん……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PThis is sorrow … …\x01",
            "… … and despair … …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x4B0, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#6P#4SKeya、しっかりしろ！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#00007F#6P#4SPlease reply if you can hear it!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10803F#6P#30WCut, that kind of … …\x02\x03",
            "#10810F…… No way … just like this …\x01",
            "Like the treasure of the former vision … …?\x02",
        )
    )

    CloseMessageWindow()
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_935C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_932F")
    OP_FC(0x6)
    Jump("loc_9332")

    label("loc_932F")

    OP_FC(0xC)

    label("loc_9332")


    ChrTalk(
        0x109,
        "#10107F#13PWell, that is …! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9405")

    label("loc_935C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9386")
    OP_FC(0x6)
    Jump("loc_9389")

    label("loc_9386")

    OP_FC(0xC)

    label("loc_9389")


    ChrTalk(
        0x106,
        "#10707F#13PWell, that is …! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9405")

    label("loc_93B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9405")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93DD")
    OP_FC(0x6)
    Jump("loc_93E0")

    label("loc_93DD")

    OP_FC(0xC)

    label("loc_93E0")


    ChrTalk(
        0x10A,
        "#00607F#13PNo way it is …! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_9405")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9477")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_942F")
    OP_FC(0x6)
    Jump("loc_9432")

    label("loc_942F")

    OP_FC(0xC)

    label("loc_9432")


    ChrTalk(
        0x105,
        (
            "#10410F#13PSolving the cause of our existence\x01",
            "It is said to have disappeared …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9548")

    label("loc_9477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94A1")
    OP_FC(0x6)
    Jump("loc_94A4")

    label("loc_94A1")

    OP_FC(0xC)

    label("loc_94A4")


    ChrTalk(
        0x10A,
        (
            "#00610F#13PWith my own hands\x01",
            "It is said to have disappeared! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9548")

    label("loc_94E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9548")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_950D")
    OP_FC(0x6)
    Jump("loc_9510")

    label("loc_950D")

    OP_FC(0xC)

    label("loc_9510")


    ChrTalk(
        0x106,
        (
            "#10701F#13PWith my own hands\x01",
            "It disappeared … ….! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9548")


    ChrTalk(
        0x101,
        "#00013F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 61)
    OP_68(0, 2800, -6500, 2000)
    MoveCamera(330, 5, 0, 2000)
    OP_6E(700, 2000)
    Sleep(500)

    def lambda_95AA():

        label("loc_95AA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_95AA")

    QueueWorkItem2(0xA, 2, lambda_95AA)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x102,
        "#00105F#6P#NLloyd …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00207F#6P#NMr. Lloyd …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0xA, 0x2)

    ChrTalk(
        0xA,
        "#10805F#6PWhat is it …?! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6P#NI'm going to do! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 4100, -3910, 0)
    MoveCamera(330, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12810, 0)
    OP_0D()
    OP_68(0, 4300, -2110, 10000)
    MoveCamera(324, 8, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(12810, 10000)
    StopEffect(0x5, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        (
            "#00010F#5P#50W#25A……Should be fine……\x01",
            "Please wait there … …!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#00015F#5P#60W#25AI … … surely this girl … ….\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x5, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#00007F#5P#80W#28A……Keyaをこの手で────\x02",
    )

    CloseMessageWindow()
    FadeToDark(4000, 16777215, -1)

    def lambda_990A():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_990A)
    OP_68(0, 4300, -160, 4000)
    MoveCamera(324, 8, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(12810, 4000)
    BeginChrThread(0x101, 0, 0, 62)
    Sleep(1000)
    Sound(829, 0, 70, 0)
    StopSound(979, 2500, 70)
    StopSound(112, 2500, 50)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99BB")

    ChrTalk(
        0x102,
        "#00107F#3409V#6P#4S#N#15A#30WLloyd ─ ─!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B19")

    label("loc_99BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A02")

    ChrTalk(
        0x103,
        "#00207F#2696V#6P#4S#N#15A#30WMr. Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B19")

    label("loc_9A02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4B")

    ChrTalk(
        0x104,
        "#00307F#2776V#6P#4S#N#15A#30WLloyd ─ Oh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B19")

    label("loc_9A4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A8E")

    ChrTalk(
        0x105,
        "#10407F#2925V#6P#4S#N#15A#30WLloyd ─ ─!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B19")

    label("loc_9A8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD7")

    ChrTalk(
        0x109,
        "#10107F#3531V#6P#4S#N#15A#30WMr. Lloyd ─ ─!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B19")

    label("loc_9AD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B19")

    ChrTalk(
        0x106,
        "#10707F#3264V#6P#4S#N#15A#30WMr. Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_9B19")

    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9013", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_57_8C0A end

    def Function_58_9B33(): pass

    label("Function_58_9B33")

    OP_74(0x1, 0xA)
    OP_71(0x1, 0x51, 0x64, 0x0, 0x20)
    Return()

    # Function_58_9B33 end

    def Function_59_9B44(): pass

    label("Function_59_9B44")

    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(661, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x30C, 0x35C, 0x0, 0x0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sound(676, 0, 80, 0)
    OP_79(0x1)
    OP_71(0x1, 0x367, 0x38E, 0x0, 0x20)
    Return()

    # Function_59_9B44 end

    def Function_60_9B7F(): pass

    label("Function_60_9B7F")

    Sound(692, 0, 60, 0)
    Sound(930, 0, 100, 0)
    Sleep(1000)
    Sound(682, 0, 100, 0)
    Sound(832, 2, 100, 0)
    OP_87(0x1, 0x1, 0x1, "891core:Layer1(52)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(2500)
    Sleep(600)
    OP_75(0x1, 0x1, 0x2BC)
    Sound(223, 0, 100, 0)
    Sound(920, 0, 100, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(800)

    def lambda_9C01():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C01)

    def lambda_9C1B():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9C1B)
    Sleep(2200)
    BeginChrThread(0xF, 1, 0, 70)
    Sleep(300)
    PlayEffect(0x2, 0x2, 0xE, 0x1, 0, 750, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sleep(500)
    Sound(898, 0, 50, 0)
    BeginChrThread(0xFE, 0, 0, 69)
    WaitChrThread(0xFE, 0)
    WaitChrThread(0xFE, 1)
    OP_9B(0x1, 0xE, 0x0, 0x3E8, 0x1F4, 0x1)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_60_9B7F end

    def Function_61_9CA2(): pass

    label("Function_61_9CA2")

    Sound(1010, 2, 70, 0)
    OP_95(0xFE, 0, 0, -4750, 5000, 0x1)
    Sound(833, 0, 60, 0)
    StopSound(1010, 500, 60)
    StopSound(961, 1000, 40)
    Sound(979, 2, 80, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_9D6E():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9D6E)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)
    OP_9B(0x1, 0xFE, 0x0, 0x190, 0x3E8, 0x0)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)

    def lambda_9DE1():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9DE1)
    Sleep(250)
    SetChrSubChip(0xFE, 0x23)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x3)

    label("loc_9E0F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E3B")

    def lambda_9E1F():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9E1F)
    Sleep(400)
    Jump("loc_9E0F")

    label("loc_9E3B")

    Return()

    # Function_61_9CA2 end

    def Function_62_9E3C(): pass

    label("Function_62_9E3C")

    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4100, -2210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_9E7C():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9E7C)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)

    def lambda_9E9C():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E9C)
    Sound(920, 0, 100, 0)
    Sound(1005, 0, 100, 0)
    Sleep(700)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_62_9E3C end

    def Function_63_9EC1(): pass

    label("Function_63_9EC1")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_63_9EC1 end

    def Function_64_9ED0(): pass

    label("Function_64_9ED0")

    Sleep(100)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_9ED0 end

    def Function_65_9EE2(): pass

    label("Function_65_9EE2")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_9EE2 end

    def Function_66_9EF4(): pass

    label("Function_66_9EF4")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_66_9EF4 end

    def Function_67_9F00(): pass

    label("Function_67_9F00")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F20")
    Sound(540, 0, 50, 0)
    Jump("loc_9F45")

    label("loc_9F20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F45")
    Sound(531, 0, 50, 0)

    label("loc_9F45")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_9F00 end

    def Function_68_9F4E(): pass

    label("Function_68_9F4E")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F6E")
    Sound(540, 0, 50, 0)
    Jump("loc_9F93")

    label("loc_9F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F93")
    Sound(531, 0, 50, 0)

    label("loc_9F93")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_68_9F4E end

    def Function_69_9F9C(): pass

    label("Function_69_9F9C")

    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_69_9F9C end

    def Function_70_9FB9(): pass

    label("Function_70_9FB9")

    Sound(961, 2, 0, 0)
    Sleep(150)
    OP_25(0x3C1, 0x5)
    Sleep(150)
    OP_25(0x3C1, 0xA)
    Sleep(150)
    OP_25(0x3C1, 0xF)
    Sleep(150)
    OP_25(0x3C1, 0x14)
    Sleep(150)
    OP_25(0x3C1, 0x19)
    Sleep(150)
    OP_25(0x3C1, 0x1E)
    Sleep(150)
    OP_25(0x3C1, 0x23)
    Sleep(150)
    OP_25(0x3C1, 0x28)
    StopSound(112, 1000, 50)
    Return()

    # Function_70_9FB9 end

    def Function_71_9FFE(): pass

    label("Function_71_9FFE")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 97)
    CreatePortrait(0, 112, 76, 368, 204, 70, 90, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis419.itp")
    CreatePortrait(1, 112, 116, 368, 244, 118, 88, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis420.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis418.itp")
    LoadChrToIndex("chr/ch05000.itc", 0x1E)
    LoadChrToIndex("chr/ch03750.itc", 0x1F)
    LoadChrToIndex("chr/ch03752.itc", 0x20)
    LoadChrToIndex("apl/ch51745.itc", 0x21)
    LoadChrToIndex("apl/ch51216.itc", 0x22)
    LoadChrToIndex("chr/ch03754.itc", 0x23)
    LoadChrToIndex("apl/ch51757.itc", 0x24)
    LoadChrToIndex("apl/ch51758.itc", 0x25)
    LoadChrToIndex("apl/ch51777.itc", 0x26)
    LoadChrToIndex("apl/ch51776.itc", 0x27)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event/ev17070.eff")
    LoadEffect(0x2, "event/evwarp.eff")
    LoadEffect(0x3, "battle/cr036301.eff")
    LoadEffect(0x4, "event/ev14001.eff")
    SoundLoad(961)
    SoundLoad(832)
    SoundLoad(3410)
    SoundLoad(3337)
    SoundLoad(3338)
    SoundLoad(3339)
    SoundLoad(3340)
    SoundLoad(2777)
    SoundLoad(2697)
    SoundLoad(3799)
    SoundLoad(3800)
    SoundLoad(3655)
    SoundLoad(3656)
    OP_68(0, 2300, -7000, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, 0, 1000, -12500, 180)
    SetChrPos(0x102, 2120, 950, -10650, 222)
    SetChrPos(0x103, -3740, 950, -12910, 91)
    SetChrPos(0x104, 3750, 950, -12870, 268)
    SetChrPos(0xF4, 2380, 950, -15570, 317)
    SetChrPos(0xF5, -2360, 950, -15600, 42)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 2000, -12500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 1000, -13100, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 2900, -4800, 135)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    Call(0, 35)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xB)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 0, 950, -12500, 180)
    SetMapObjFrame(0xFF, "egg_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi35", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi25_", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line11a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pnrm0b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "line01a_add", 0x0, 0x1)
    PlayEffect(0x1, 0x0, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A415")
    Jump("loc_A4BF")

    label("loc_A415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A438")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x103)
    OP_FD(0x103, 0x10)
    Jump("loc_A4BF")

    label("loc_A438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45B")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x104)
    OP_FD(0x104, 0x10)
    Jump("loc_A4BF")

    label("loc_A45B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A47E")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x105)
    OP_FD(0x105, 0x10)
    Jump("loc_A4BF")

    label("loc_A47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4A1")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x109)
    OP_FD(0x109, 0x10)
    Jump("loc_A4BF")

    label("loc_A4A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4BF")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x106)
    OP_FD(0x106, 0x10)

    label("loc_A4BF")

    BeginChrThread(0xF, 1, 0, 70)
    FadeToBright(1000, 16777215)
    OP_68(0, 2100, -13000, 0)
    MoveCamera(290, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(23000, 3500)
    OP_0D()
    Sleep(2500)
    Sound(919, 0, 60, 0)
    PlayEffect(0x3, 0xFF, 0x101, 0x1, 0, 750, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(500)
    OP_93(0xA, 0xB4, 0x0)
    OP_68(0, 2100, -13000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(13450, 4000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 0, 0, 72)
    OP_0D()
    StopEffect(0x0, 0x2)
    StopSound(961, 2000, 40)
    OP_68(0, 2100, -13000, 10000)
    MoveCamera(0, 20, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(11500, 10000)
    Sound(934, 0, 40, 0)
    Sound(935, 0, 80, 0)
    Sound(223, 0, 100, 0)

    def lambda_A5EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5EB)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 0, 0, 73)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6AE")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A……Ahh………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd … … Keibo ……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#11P#30W#20ACome back … …. I came …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AA9E")

    label("loc_A6AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A753")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AOh……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#6P#30W#20Aロイド……Keyaちゃん……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#11P#30W#20ACome back … …. I came …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AA9E")

    label("loc_A753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7FD")

    ChrTalk(
        0x102,
        "#00116F#12P#30W#20AAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20Aロイドさん……Keya……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00315F#11P#30W#20Amy mother……\x01",
            "Back … … I came back …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AA9E")

    label("loc_A7FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A826")
    OP_FC(0xC)
    Jump("loc_A829")

    label("loc_A826")

    OP_FC(0x6)

    label("loc_A829")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A…… Lloyd … …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AKiyoshi too ……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10411F#11P#30W#20AHuh … … have you returned …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AA9E")

    label("loc_A8DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9C3")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A……Ahh………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A957")
    OP_FC(0xC)
    Jump("loc_A95A")

    label("loc_A957")

    OP_FC(0x6)

    label("loc_A95A")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AKeyaちゃんも……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10116F#11P#30W#20ACome back … …. I came …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AA9E")

    label("loc_A9C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9E")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AOh……!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA12")
    OP_FC(0xC)
    Jump("loc_AA15")

    label("loc_AA12")

    OP_FC(0x6)

    label("loc_AA15")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20ALloyd …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A……Keyaも……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10716F#11P#30W#20ACome back … …. I came …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AA9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC8")
    OP_FC(0xC)
    Jump("loc_AACB")

    label("loc_AAC8")

    OP_FC(0x6)

    label("loc_AACB")


    ChrTalk(
        0x10A,
        (
            "#00604F#13P#30W#20AAbsolutely …\x01",
            "It is not frightening of my elder brother … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AB0C")

    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#40WFuu …\x02\x03",
            "#30W#00000F── Now, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#50W… … … ugh …… Gus …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB91")
    OP_FC(0x5)
    Jump("loc_AC27")

    label("loc_AB91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABBA")
    OP_FC(0xC)
    Jump("loc_ABBD")

    label("loc_ABBA")

    OP_FC(0x6)

    label("loc_ABBD")

    Jump("loc_AC27")

    label("loc_ABC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABEB")
    OP_FC(0xC)
    Jump("loc_ABEE")

    label("loc_ABEB")

    OP_FC(0x6)

    label("loc_ABEE")

    Jump("loc_AC27")

    label("loc_ABF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC1C")
    OP_FC(0xC)
    Jump("loc_AC1F")

    label("loc_AC1C")

    OP_FC(0x6)

    label("loc_AC1F")

    Jump("loc_AC27")

    label("loc_AC24")

    OP_FC(0xB)

    label("loc_AC27")

    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00114F#13PLloyd … It was good!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10500, 1000)
    BeginChrThread(0x102, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 79)
    BeginChrThread(0x104, 0, 0, 80)
    BeginChrThread(0xF4, 0, 0, 81)
    BeginChrThread(0xF5, 0, 0, 82)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACB2")
    OP_FC(0xB)
    Jump("loc_ACB5")

    label("loc_ACB2")

    OP_FC(0x5)

    label("loc_ACB5")

    OP_6F(0x79)
    SetCameraDistance(10000, 30000)

    ChrTalk(
        0x103,
        (
            "#00214F#13PKeyaも……\x01",
            "Are you okay……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PApparently in the form of the original\x01",
            "I guess he returned, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, it's okay now.\x02\x03",
            "#00000F……ほら、Keya。\x01",
            "There are things to tell everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#40WGuss … … … … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 50, 0)
    Sound(898, 0, 30, 0)
    OP_68(0, 2000, -13000, 500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(250)
    OP_0D()
    Sleep(700)
    BeginChrThread(0x9, 1, 0, 74)
    WaitChrThread(0x9, 1)
    BeginChrThread(0x9, 1, 0, 75)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#05821F#5P#40WSorry ….\x02\x03",
            "…… Always worrying ……\x01",
            "Just do something.\x02\x03",
            "#05818Fthen……\x01",
            "……Thanks for coming……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEC2")
    OP_FC(0x5)
    Jump("loc_AF58")

    label("loc_AEC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEEB")
    OP_FC(0xC)
    Jump("loc_AEEE")

    label("loc_AEEB")

    OP_FC(0x6)

    label("loc_AEEE")

    Jump("loc_AF58")

    label("loc_AEF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF1C")
    OP_FC(0xC)
    Jump("loc_AF1F")

    label("loc_AF1C")

    OP_FC(0x6)

    label("loc_AF1F")

    Jump("loc_AF58")

    label("loc_AF24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF4D")
    OP_FC(0xC)
    Jump("loc_AF50")

    label("loc_AF4D")

    OP_FC(0x6)

    label("loc_AF50")

    Jump("loc_AF58")

    label("loc_AF55")

    OP_FC(0xB)

    label("loc_AF58")


    ChrTalk(
        0x102,
        "#00116F#13PKeyaちゃん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF90")
    OP_FC(0xB)
    Jump("loc_AF93")

    label("loc_AF90")

    OP_FC(0x5)

    label("loc_AF93")


    ChrTalk(
        0x103,
        "#00204F#13PI do not need to thank you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PHaha … well, when I return home\x01",
            "Prepare your ass pencil pen about it?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 76)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#05817F#5P#50W……Yup……\x01",
            "Gusu …. Uuu … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11POh no ….\x01",
            "Will not you cry anymore?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0A5")
    OP_FC(0xC)
    Jump("loc_B0A8")

    label("loc_B0A5")

    OP_FC(0x6)

    label("loc_B0A8")


    ChrTalk(
        0x10A,
        "#00604F#13PHydrofluoric acid\x02",
    )

    CloseMessageWindow()

    label("loc_B0C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B126")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0E8")
    OP_FC(0xB)
    Jump("loc_B105")

    label("loc_B0E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B102")
    OP_FC(0xC)
    Jump("loc_B105")

    label("loc_B102")

    OP_FC(0x6)

    label("loc_B105")


    ChrTalk(
        0x105,
        "#10404F#13PHuh, good grief.\x02",
    )

    CloseMessageWindow()

    label("loc_B126")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B193")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14D")
    OP_FC(0xB)
    Jump("loc_B16A")

    label("loc_B14D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B167")
    OP_FC(0xC)
    Jump("loc_B16A")

    label("loc_B167")

    OP_FC(0x6)

    label("loc_B16A")


    ChrTalk(
        0x109,
        "#10106F#13P…… Gus … … it was good …\x02",
    )

    CloseMessageWindow()

    label("loc_B193")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B200")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1BA")
    OP_FC(0xB)
    Jump("loc_B1D7")

    label("loc_B1BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1D4")
    OP_FC(0xC)
    Jump("loc_B1D7")

    label("loc_B1D4")

    OP_FC(0x6)

    label("loc_B1D7")


    ChrTalk(
        0x106,
        "#10710F#13P(… … this is … … bonds ……)\x02",
    )

    CloseMessageWindow()

    label("loc_B200")

    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#10803F#3799V#5P#N#40W#35A─ ─ absolutely.\x01",
            "It is boring curtain.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
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
    SetChrSubChip(0x9, 0x1F)
    Sleep(125)
    SetChrSubChip(0x9, 0x1E)
    Sleep(875)
    OP_68(0, 3300, -10520, 1800)
    MoveCamera(0, -1, 0, 1800)
    OP_6E(700, 1800)
    SetCameraDistance(10550, 1800)
    Sleep(200)

    def lambda_B333():
        OP_93(0xFE, 0xAF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B333)
    Sleep(50)

    def lambda_B343():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B343)
    Sleep(50)

    def lambda_B353():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B353)
    Sleep(50)

    def lambda_B363():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B363)
    Sleep(50)

    def lambda_B373():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B373)
    Sleep(50)

    def lambda_B383():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B383)
    Sleep(50)

    def lambda_B393():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B393)
    Sleep(300)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)

    def lambda_B3B5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B3B5)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    def lambda_B3CC():
        OP_96(0xFE, 0xFFFFFE8E, 0x3B6, 0xFFFFCCFC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B3CC)

    ChrTalk(
        0x101,
        "#00001F#6P#N……Marybeleさん。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#NBell …\x01",
            "… … Are you planning on doing so yet?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30Wやるも何も、Keyaさんから\x01",
            "The power of \"treasure\" has been lost.\x02\x03",
            "Along with the millions of imperfections of the Clois family.\x02\x03",
            "#10801Ftruly……\x01",
            "The time to go is also a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05816F#6P#N#30W…… Bell ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00206F#6P#NNightmares of the cult … ….\x01",
            "Is it the end in the true sense?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30WYeah, but this far\x01",
            "A further disaster strikes the crossbell\x01",
            "It will be on standby.\x02\x03",
            "Elebornia in particular …\x01",
            "Whichever powers won the civil war\x01",
            "The possibility of invading should be high.\x02\x03",
            "#10801FIf so, Calvert also rival\x01",
            "There is no mistake to dispatch an army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N… …. Yeah ………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00301F#12P#NI wonder …\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B69B")
    OP_FC(0xFFF4)
    Jump("loc_B69E")

    label("loc_B69B")

    OP_FC(0xFFFA)

    label("loc_B69E")


    ChrTalk(
        0x109,
        "#10108F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_B724")

    label("loc_B6CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B724")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6F7")
    OP_FC(0xFFF4)
    Jump("loc_B6FA")

    label("loc_B6F7")

    OP_FC(0xFFFA)

    label("loc_B6FA")


    ChrTalk(
        0x10A,
        "#00608F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B724")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WHowever, as I lost \"treasure\"\x01",
            "There is no technique to stop you.\x02\x03",
            "#10800FYou know it, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NStill we are …\x01",
            "Keyaと共にこの選択を選んだ。\x02\x03",
            "#00003FTogether with the barrier of disaster\x01",
            "To grab the light of tomorrow …\x02\x03",
            "#00000FThat's why I do not regret it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00202F#6P#N……Yes……!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F#12P#NHehe, more than ever\x01",
            "You will be busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00304F#12P#NHowever, until we come here\x01",
            "I'm struggling hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B95C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B912")
    OP_FC(0xFFF4)
    Jump("loc_B915")

    label("loc_B912")

    OP_FC(0xFFFA)

    label("loc_B915")


    ChrTalk(
        0x109,
        (
            "#10100F#13PStraight, just in one place\x01",
            "Just getting over with everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B95C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B986")
    OP_FC(0xFFF4)
    Jump("loc_B989")

    label("loc_B986")

    OP_FC(0xFFFA)

    label("loc_B989")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PMore than ever the police\x01",
            "The price will be questioned.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B9CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA80")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9F6")
    OP_FC(0xFFF4)
    Jump("loc_B9F9")

    label("loc_B9F6")

    OP_FC(0xFFFA)

    label("loc_B9F9")


    ChrTalk(
        0x105,
        (
            "#10404F#13PHuff, stand on,\x01",
            "I can not say rare things ….\x02\x03",
            "#10402FLord's landing by liturgy is going to disappear\x01",
            "The church should be able to do a little with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BA80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAAA")
    OP_FC(0xFFF4)
    Jump("loc_BAAD")

    label("loc_BAAA")

    OP_FC(0xFFFA)

    label("loc_BAAD")


    ChrTalk(
        0x106,
        (
            "#10704F#13PMe too……\x01",
            "It will be power, not worse.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BAE2")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WGiggle\x01",
            "I can not keep company with you.\x02\x03",
            "#10802FWell, if that's the case\x01",
            "You ought to do your best at best.\x02",
        )
    )

    CloseMessageWindow()
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    Sleep(700)
    Sound(357, 0, 80, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0xA, 3, 0, 4)
    PlayEffect(0x0, 0x0, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#12P#NBell …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#6P#NMarybeleさん……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10804F#5P─ ─ Ah, I am Mr. Ian\x01",
            "I just made a state of death.\x02\x03",
            "#10800FYou will be saved if you do it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#NAh……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(1590, 2400, -10140, 1500)
    MoveCamera(35, 15, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14390, 1500)

    def lambda_BD6E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BD6E)
    Sleep(50)

    def lambda_BD7E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BD7E)
    Sleep(50)

    def lambda_BD8E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BD8E)
    Sleep(50)

    def lambda_BD9E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BD9E)
    Sleep(50)

    def lambda_BDAE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_BDAE)
    Sleep(50)

    def lambda_BDBE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BDBE)
    Sleep(50)

    def lambda_BDCE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BDCE)
    WaitChrThread(0xF5, 2)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(9510, 1700, -9870, 0)
    MoveCamera(46, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sleep(1700)
    Fade(500)
    OP_68(0, 3300, -10520, 0)
    MoveCamera(0, -1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10550, 0)
    OP_0D()

    def lambda_BE4F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE4F)
    Sleep(50)

    def lambda_BE5F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE5F)
    Sleep(50)

    def lambda_BE6F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BE6F)
    Sleep(50)

    def lambda_BE7F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BE7F)
    Sleep(50)

    def lambda_BE8F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_BE8F)
    Sleep(50)

    def lambda_BE9F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BE9F)
    Sleep(50)

    def lambda_BEAF():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BEAF)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0xA,
        (
            "#10804F#5PAlso, because the power of treasure has been lost\x01",
            "\"Taiki\" will soon disappear.\x02\x03",
            "#10800FWith a few hours …\x01",
            "At best, escape early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P#NYou …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#6P#N……why……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10802F#5PWhatever happens to the end of this time\x01",
            "Crossbell was going to leave.\x02\x03",
            "#10804FTo the Confederation of \"Eating Serpent\"\x01",
            "I will take the place of a lost apostle\x01",
            "Because it was wanted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#6P#NI\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NApostle……\x01",
            "Is it the highest executive of \"association\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12P#NBell …… you ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10802F#5PUfufu …\x01",
            "Eli, please do not face such a face.\x02\x03",
            "#10804FAs the continents have become like this,\x01",
            "There will be opportunities to see each other again.\x02\x03",
            "#10800FIn the meantime, from the distant land\x01",
            "Well, I will show you.\x02\x03",
            "Tell your evil posters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N……… Bell …………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        "#05808F#6P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10806F#5PAnd it's my father,\x01",
            "Please give me pardon.\x02\x03",
            "#10800FTo rebuild the crossbell\x01",
            "It will be a little useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3000, 5320, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21500, 2000)
    Sleep(1000)
    BeginChrThread(0xA, 0, 0, 77)
    WaitChrThread(0xA, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#10809F#3800V#5P#40W#30AWell then, everyone - good-bye.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1388)
    SetCameraDistance(20500, 3000)
    StopSound(832, 1000, 90)
    Sound(936, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    Sleep(1500)
    SetChrFlags(0xA, 0x80)
    OP_6F(0x79)
    WaitBGM()
    OP_68(0, 800, 5320, 4500)
    MoveCamera(0, 6, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(30180, 4500)
    Sleep(4000)
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
    Sleep(500)

    ChrTalk(
        0x101,
        "#00008F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4F1")
    OP_FC(0x5)
    Jump("loc_C4F4")

    label("loc_C4F1")

    OP_FC(0xB)

    label("loc_C4F4")


    ChrTalk(
        0x102,
        (
            "#00106F#13P#30W………… Bell …………\x01",
            "Until the end … … It is selfish … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7541", 0)
    Fade(500)
    OP_68(1910, 2500, -12300, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13910, 0)
    SetChrPos(0x101, 0, 950, -13000, 0)
    BeginChrThread(0x101, 0, 0, 83)
    Sleep(1200)

    def lambda_C599():

        label("loc_C599")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C599")

    QueueWorkItem2(0x9, 2, lambda_C599)
    Sleep(300)

    def lambda_C5AE():

        label("loc_C5AE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C5AE")

    QueueWorkItem2(0x102, 2, lambda_C5AE)
    Sleep(50)

    def lambda_C5C3():

        label("loc_C5C3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C5C3")

    QueueWorkItem2(0x103, 2, lambda_C5C3)
    Sleep(50)

    def lambda_C5D8():

        label("loc_C5D8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C5D8")

    QueueWorkItem2(0x104, 2, lambda_C5D8)
    Sleep(50)

    def lambda_C5ED():

        label("loc_C5ED")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C5ED")

    QueueWorkItem2(0xF4, 2, lambda_C5ED)
    Sleep(50)

    def lambda_C602():

        label("loc_C602")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C602")

    QueueWorkItem2(0xF5, 2, lambda_C602)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    EndChrThread(0x9, 0x2)
    Sound(802, 0, 50, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_63(0x101, 0x96, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C697")
    BeginChrThread(0x102, 0, 0, 84)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C85B")

    label("loc_C697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6CF")
    BeginChrThread(0x102, 0, 0, 85)
    BeginChrThread(0x103, 0, 0, 84)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C85B")

    label("loc_C6CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C707")
    BeginChrThread(0x102, 0, 0, 86)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 84)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C85B")

    label("loc_C707")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C77A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C751")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C775")

    label("loc_C751")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_C775")

    Jump("loc_C85B")

    label("loc_C77A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7C4")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C7E8")

    label("loc_C7C4")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_C7E8")

    Jump("loc_C85B")

    label("loc_C7ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C85B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C837")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_C85B")

    label("loc_C837")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_C85B")

    Sleep(300)
    OP_68(7610, 2000, -10530, 5500)
    MoveCamera(49, 30, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13000, 3500)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    SetCameraDistance(10000, 120000)

    ChrTalk(
        0x101,
        (
            "#00004F#5P#30W……Yup.\x01",
            "It is certainly not a fatal injury.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)
    SetChrChipByIndex(0x101, 0x26)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0x5)
    OP_93(0x9, 0xE1, 0x1F4)
    SetChrChipByIndex(0x9, 0x27)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C990")

    def lambda_C933():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C933)

    def lambda_C940():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C940)
    Sleep(50)

    def lambda_C950():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C950)
    Sleep(50)

    def lambda_C960():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_C960)
    Sleep(50)

    def lambda_C970():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C970)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CD1C")

    label("loc_C990")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA01")

    def lambda_C9A4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C9A4)

    def lambda_C9B1():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C9B1)
    Sleep(50)

    def lambda_C9C1():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C9C1)
    Sleep(50)

    def lambda_C9D1():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_C9D1)
    Sleep(50)

    def lambda_C9E1():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C9E1)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CD1C")

    label("loc_CA01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA72")

    def lambda_CA15():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA15)

    def lambda_CA22():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CA22)
    Sleep(50)

    def lambda_CA32():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CA32)
    Sleep(50)

    def lambda_CA42():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CA42)
    Sleep(50)

    def lambda_CA52():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CA52)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CD1C")

    label("loc_CA72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB57")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAF5")

    def lambda_CA98():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CA98)

    def lambda_CAA5():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CAA5)
    Sleep(50)

    def lambda_CAB5():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CAB5)
    Sleep(50)

    def lambda_CAC5():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CAC5)
    Sleep(50)

    def lambda_CAD5():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CAD5)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CB52")

    label("loc_CAF5")


    def lambda_CAFA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CAFA)

    def lambda_CB07():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CB07)
    Sleep(50)

    def lambda_CB17():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CB17)
    Sleep(50)

    def lambda_CB27():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CB27)
    Sleep(50)

    def lambda_CB37():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CB37)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_CB52")

    Jump("loc_CD1C")

    label("loc_CB57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBDA")

    def lambda_CB7D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CB7D)

    def lambda_CB8A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CB8A)
    Sleep(50)

    def lambda_CB9A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CB9A)
    Sleep(50)

    def lambda_CBAA():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CBAA)
    Sleep(50)

    def lambda_CBBA():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CBBA)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CC37")

    label("loc_CBDA")


    def lambda_CBDF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CBDF)

    def lambda_CBEC():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CBEC)
    Sleep(50)

    def lambda_CBFC():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CBFC)
    Sleep(50)

    def lambda_CC0C():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CC0C)
    Sleep(50)

    def lambda_CC1C():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CC1C)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_CC37")

    Jump("loc_CD1C")

    label("loc_CC3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCBF")

    def lambda_CC62():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CC62)

    def lambda_CC6F():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC6F)
    Sleep(50)

    def lambda_CC7F():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CC7F)
    Sleep(50)

    def lambda_CC8F():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CC8F)
    Sleep(50)

    def lambda_CC9F():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CC9F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CD1C")

    label("loc_CCBF")


    def lambda_CCC4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CCC4)

    def lambda_CCD1():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CCD1)
    Sleep(50)

    def lambda_CCE1():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CCE1)
    Sleep(50)

    def lambda_CCF1():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CCF1)
    Sleep(50)

    def lambda_CD01():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CD01)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_CD1C")


    ChrTalk(
        0x101,
        (
            "#00000F#11PEveryone, hand it out\x01",
            "Let's send Professor Ian to Mercapa.\x02\x03",
            "And Arios also\x01",
            "You will need to take care of them and carry them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE1C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDC1")
    OP_FC(0xC)
    Jump("loc_CDC4")

    label("loc_CDC1")

    OP_FC(0x6)

    label("loc_CDC4")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PIn a few hours\x01",
            "Because \"Taiki\" is going to collapse\x01",
            "It looks like you have to hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF55")

    label("loc_CE1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEBA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE43")
    OP_FC(0x5)
    Jump("loc_CE60")

    label("loc_CE43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE5D")
    OP_FC(0xC)
    Jump("loc_CE60")

    label("loc_CE5D")

    OP_FC(0x6)

    label("loc_CE60")


    ChrTalk(
        0x106,
        (
            "#10700F#13PIn a few hours\x01",
            "Because \"Taiki\" is going to collapse\x01",
            "It seems necessary to hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF55")

    label("loc_CEBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF55")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEE1")
    OP_FC(0x5)
    Jump("loc_CEFE")

    label("loc_CEE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEFB")
    OP_FC(0xC)
    Jump("loc_CEFE")

    label("loc_CEFB")

    OP_FC(0x6)

    label("loc_CEFE")


    ChrTalk(
        0x109,
        (
            "#10100F#13PIn a few hours\x01",
            "Because \"Taiki\" is going to collapse\x01",
            "I heard you need to hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFE2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7C")
    OP_FC(0x5)
    Jump("loc_CF99")

    label("loc_CF7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF96")
    OP_FC(0xC)
    Jump("loc_CF99")

    label("loc_CF96")

    OP_FC(0x6)

    label("loc_CF99")


    ChrTalk(
        0x105,
        (
            "#10404F#13PContact Abbas and everyone\x01",
            "Shall I make a break?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0F9")

    label("loc_CFE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D06F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D009")
    OP_FC(0x5)
    Jump("loc_D026")

    label("loc_D009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D023")
    OP_FC(0xC)
    Jump("loc_D026")

    label("loc_D023")

    OP_FC(0x6)

    label("loc_D026")


    ChrTalk(
        0x109,
        (
            "#10104F#13PPlease contact Mercapa\x01",
            "It seems better to organize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0F9")

    label("loc_D06F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0F9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D096")
    OP_FC(0x5)
    Jump("loc_D0B3")

    label("loc_D096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0B0")
    OP_FC(0xC)
    Jump("loc_D0B3")

    label("loc_D0B0")

    OP_FC(0x6)

    label("loc_D0B3")


    ChrTalk(
        0x106,
        (
            "#10704F#13PPlease contact Mercapa\x01",
            "It seems better to organize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0F9")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D113")
    OP_FC(0x5)
    Jump("loc_D116")

    label("loc_D113")

    OP_FC(0x6)

    label("loc_D116")


    ChrTalk(
        0x103,
        (
            "#00206F#13PEven so ……\x02\x03",
            "#00202F最後までMarybeleさんは\x01",
            "Marybeleさんでしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D188")
    OP_FC(0x5)
    Jump("loc_D18B")

    label("loc_D188")

    OP_FC(0xC)

    label("loc_D18B")


    ChrTalk(
        0x104,
        (
            "#00306F#13POh, I did something for you guys\x01",
            "I do not hate somewhere … …\x02\x03",
            "#00302FIs that such a virtuous person?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D217")
    OP_FC(0x6)
    Jump("loc_D2C4")

    label("loc_D217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D22E")
    OP_FC(0xC)
    Jump("loc_D2C4")

    label("loc_D22E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D257")
    OP_FC(0xC)
    Jump("loc_D25A")

    label("loc_D257")

    OP_FC(0x6)

    label("loc_D25A")

    Jump("loc_D2C4")

    label("loc_D25F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D290")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D288")
    OP_FC(0xC)
    Jump("loc_D28B")

    label("loc_D288")

    OP_FC(0x6)

    label("loc_D28B")

    Jump("loc_D2C4")

    label("loc_D290")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2B9")
    OP_FC(0xC)
    Jump("loc_D2BC")

    label("loc_D2B9")

    OP_FC(0x6)

    label("loc_D2BC")

    Jump("loc_D2C4")

    label("loc_D2C1")

    OP_FC(0x5)

    label("loc_D2C4")


    ChrTalk(
        0x102,
        (
            "#00106F#13PBelle probably … ….\x01",
            "I think that I am honest with myself anywhere.\x02\x03",
            "#00103FWhat I wanted to do once\x01",
            "With no hesitation, in any way\x01",
            "I try to accomplish it …\x02\x03",
            "#00108FEven if you do not care at all … …\x02\x03",
            "#00101FBut … everyone else\x01",
            "It is not strong like a bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh, that's why the person ……\x01",
            "I think it is necessary for my family and friends.\x02\x03",
            "#00008FOvercome the walls, tomorrow's still unseen\x01",
            "In order to grasp the light …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D463")
    OP_FC(0x5)
    Jump("loc_D466")

    label("loc_D463")

    OP_FC(0xC)

    label("loc_D466")


    ChrTalk(
        0x104,
        (
            "#00304F#13PWell, the light is visible\x01",
            "It is likely to be ahead yet … …\x02\x03",
            "#00300FStill it is getting better\x01",
            "Do not feel like it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4FB")
    OP_FC(0x5)
    Jump("loc_D4FE")

    label("loc_D4FB")

    OP_FC(0x6)

    label("loc_D4FE")


    ChrTalk(
        0x103,
        "#00214F#13P……Yes……!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D722")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D544")
    OP_FC(0x5)
    Jump("loc_D561")

    label("loc_D544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D55E")
    OP_FC(0xC)
    Jump("loc_D561")

    label("loc_D55E")

    OP_FC(0x6)

    label("loc_D561")


    ChrTalk(
        0x109,
        (
            "#10102F#13PEven people alone here\x01",
            "I could do only this!\x02\x03",
            "#10109FPeople in the crossbell\x01",
            "Everything can be done if it comes to a single!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D659")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D60E")
    OP_FC(0x5)
    Jump("loc_D62B")

    label("loc_D60E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D628")
    OP_FC(0xC)
    Jump("loc_D62B")

    label("loc_D628")

    OP_FC(0x6)

    label("loc_D62B")


    ChrTalk(
        0x105,
        "#10404F#13PHuh, maybe it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D71D")

    label("loc_D659")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6CD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D680")
    OP_FC(0x5)
    Jump("loc_D69D")

    label("loc_D680")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D69A")
    OP_FC(0xC)
    Jump("loc_D69D")

    label("loc_D69A")

    OP_FC(0x6)

    label("loc_D69D")


    ChrTalk(
        0x106,
        "#10709F#13PHehe … … that is certainly the case.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D71D")

    label("loc_D6CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D71D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6F7")
    OP_FC(0xC)
    Jump("loc_D6FA")

    label("loc_D6F7")

    OP_FC(0x6)

    label("loc_D6FA")


    ChrTalk(
        0x10A,
        "#00604F#13PHut … … certainly.\x02",
    )

    CloseMessageWindow()

    label("loc_D71D")

    Jump("loc_D9B7")

    label("loc_D722")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8B5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D749")
    OP_FC(0x5)
    Jump("loc_D766")

    label("loc_D749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D763")
    OP_FC(0xC)
    Jump("loc_D766")

    label("loc_D763")

    OP_FC(0x6)

    label("loc_D766")


    ChrTalk(
        0x105,
        (
            "#10404F#13PWell, even people just here\x01",
            "I could do just that.\x02\x03",
            "#10402FAfter adjusting the forces in the crossbell\x01",
            "Does it manage?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D860")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D813")
    OP_FC(0x5)
    Jump("loc_D830")

    label("loc_D813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D82D")
    OP_FC(0xC)
    Jump("loc_D830")

    label("loc_D82D")

    OP_FC(0x6)

    label("loc_D830")


    ChrTalk(
        0x106,
        "#10709F#13PHehe … … that is certainly the case.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8B0")

    label("loc_D860")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D88A")
    OP_FC(0xC)
    Jump("loc_D88D")

    label("loc_D88A")

    OP_FC(0x6)

    label("loc_D88D")


    ChrTalk(
        0x10A,
        "#00604F#13PHut … … certainly.\x02",
    )

    CloseMessageWindow()

    label("loc_D8B0")

    Jump("loc_D9B7")

    label("loc_D8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8CC")
    OP_FC(0x5)
    Jump("loc_D8E9")

    label("loc_D8CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8E6")
    OP_FC(0xC)
    Jump("loc_D8E9")

    label("loc_D8E6")

    OP_FC(0x6)

    label("loc_D8E9")


    ChrTalk(
        0x106,
        (
            "#10704F#13P…… Even people alone here\x01",
            "I could do just that.\x02\x03",
            "#10702FAfter adjusting the forces in the crossbell\x01",
            "I feel like I can do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D991")
    OP_FC(0xC)
    Jump("loc_D994")

    label("loc_D991")

    OP_FC(0x6)

    label("loc_D994")


    ChrTalk(
        0x10A,
        "#00604F#13PHut … … certainly.\x02",
    )

    CloseMessageWindow()

    label("loc_D9B7")

    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 90)
    WaitChrThread(0x9, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#05821F#3655V#5P#40W#40AKeyaも……\x01",
            "……Keyaもがんばる……！\x02\x03",
            "#05819F#3656V#40ATogether with … …\x01",
            "…… to protect important places!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA6F")
    OP_FC(0x6)
    Jump("loc_DB1C")

    label("loc_DA6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA86")
    OP_FC(0xC)
    Jump("loc_DB1C")

    label("loc_DA86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAB7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAAF")
    OP_FC(0xC)
    Jump("loc_DAB2")

    label("loc_DAAF")

    OP_FC(0x6)

    label("loc_DAB2")

    Jump("loc_DB1C")

    label("loc_DAB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAE0")
    OP_FC(0xC)
    Jump("loc_DAE3")

    label("loc_DAE0")

    OP_FC(0x6)

    label("loc_DAE3")

    Jump("loc_DB1C")

    label("loc_DAE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB19")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB11")
    OP_FC(0xC)
    Jump("loc_DB14")

    label("loc_DB11")

    OP_FC(0x6)

    label("loc_DB14")

    Jump("loc_DB1C")

    label("loc_DB19")

    OP_FC(0x5)

    label("loc_DB1C")


    ChrTalk(
        0x102,
        "#00102F#3410V#13P#30W#25AKeyaちゃん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB65")
    OP_FC(0x5)
    Jump("loc_DB68")

    label("loc_DB65")

    OP_FC(0x6)

    label("loc_DB68")


    ChrTalk(
        0x103,
        "#00204F#2697V#13P#30W#25A…… It is a thousand force.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBB1")
    OP_FC(0x5)
    Jump("loc_DBB4")

    label("loc_DBB1")

    OP_FC(0xC)

    label("loc_DBB4")


    ChrTalk(
        0x104,
        "#00309F#2777V#13P#30W#25AHaha, that's the spirit.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 1, 0, 91)
    BeginChrThread(0x9, 1, 0, 92)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x101,
        "#00009F#3337V#11P#30AOh, let 's do our best together.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 93)
    BeginChrThread(0x9, 1, 0, 94)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x9, 1)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#00004F#3338V#11P#30W#30A─ ─ Special Affairs Support Division, withdrawal.\x02\x03",
            "#3339V#11P#30W#45AWhile collecting Arios' s\x01",
            "In Melkova to leave \"big tree\".\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(10000, 1000)
    BeginChrThread(0x101, 1, 0, 96)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00000F#3340V#11P#30W#35ALet's go back to our crossbell …!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(13820, 4300)
    Sleep(300)
    FadeToDark(4000, 16777215, -1)
    StopBGM(0x1F40)
    Sleep(4000)
    Sleep(1000)
    OP_C9(0x0, 0x10)
    FadeToBright(3000, 16777215)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_ed.pmf", 0x35, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(4000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    OP_E0(0x23, 0x0)
    OP_E0(0x1A, 0x0)
    OP_E0(0x1B, 0x0)
    OP_E0(0x80, 0x0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF87")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "EXTRA mode has been released.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "From the title screen\x01",
            "You can enter EXTRA mode.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_DF87")

    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Save about clear data ~\x01",
            "When you create clear data and load it from the title screen\x01",
            "You can start the second lap while taking over various data.",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveClearMenu()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x10)
    OP_B9(0x0)
    Return()

    # Function_71_9FFE end

    def Function_72_E07D(): pass

    label("Function_72_E07D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)), "loc_E0C3")
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x3)
    Sleep(167)
    SetChrSubChip(0xFE, 0x4)
    Sleep(167)
    SetChrSubChip(0xFE, 0x3)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    Jump("Function_72_E07D")

    label("loc_E0C3")

    Return()

    # Function_72_E07D end

    def Function_73_E0C4(): pass

    label("Function_73_E0C4")

    OP_96(0xFE, 0x0, 0x3B6, 0xFFFFCF2C, 0x12C, 0x1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(167)
    SetChrSubChip(0xFE, 0x8)
    Sleep(167)
    SetChrSubChip(0xFE, 0x9)
    Sleep(167)
    SetChrSubChip(0xFE, 0xA)
    Sleep(167)
    SetChrSubChip(0xFE, 0xB)
    Sleep(500)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(100)
    Sound(326, 0, 30, 0)
    Return()

    # Function_73_E0C4 end

    def Function_74_E122(): pass

    label("Function_74_E122")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(125)
    SetChrSubChip(0xFE, 0x19)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(750)
    Return()

    # Function_74_E122 end

    def Function_75_E14D(): pass

    label("Function_75_E14D")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(750)
    Return()

    # Function_75_E14D end

    def Function_76_E178(): pass

    label("Function_76_E178")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(125)
    SetChrSubChip(0xFE, 0x20)
    Sleep(375)
    Return()

    # Function_76_E178 end

    def Function_77_E19C(): pass

    label("Function_77_E19C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(571)
    Return()

    # Function_77_E19C end

    def Function_78_E1F0(): pass

    label("Function_78_E1F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E202")
    Sleep(50)

    label("loc_E202")

    OP_9B(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
    Return()

    # Function_78_E1F0 end

    def Function_79_E212(): pass

    label("Function_79_E212")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E224")
    Sleep(100)

    label("loc_E224")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_79_E212 end

    def Function_80_E234(): pass

    label("Function_80_E234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E246")
    Sleep(150)

    label("loc_E246")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_80_E234 end

    def Function_81_E256(): pass

    label("Function_81_E256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E27A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E27A")
    Sleep(200)

    label("loc_E27A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E29E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E29E")
    Sleep(200)

    label("loc_E29E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2C2")
    Sleep(200)

    label("loc_E2C2")

    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_81_E256 end

    def Function_82_E2D2(): pass

    label("Function_82_E2D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2F6")
    Sleep(250)

    label("loc_E2F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E31A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E31A")
    Sleep(250)

    label("loc_E31A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E33E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E33E")
    Sleep(250)

    label("loc_E33E")

    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_82_E2D2 end

    def Function_83_E34E(): pass

    label("Function_83_E34E")

    TurnDirection(0xFE, 0x8, 500)
    Sleep(450)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x1964, 0x7D0, 0x0)
    Return()

    # Function_83_E34E end

    def Function_84_E395(): pass

    label("Function_84_E395")

    Sleep(200)
    OP_96(0xFE, 0x1C5C, 0x3B6, 0xFFFFDD14, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_84_E395 end

    def Function_85_E3B4(): pass

    label("Function_85_E3B4")

    Sleep(1100)
    OP_96(0xFE, 0x16A8, 0x406, 0xFFFFDC60, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_85_E3B4 end

    def Function_86_E3D3(): pass

    label("Function_86_E3D3")

    Sleep(50)
    OP_96(0xFE, 0x1F04, 0x3B6, 0xFFFFD1D4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_86_E3D3 end

    def Function_87_E3F2(): pass

    label("Function_87_E3F2")

    Sleep(350)
    OP_96(0xFE, 0x19C8, 0x3B6, 0xFFFFD210, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_87_E3F2 end

    def Function_88_E411(): pass

    label("Function_88_E411")

    Sleep(1450)
    OP_96(0xFE, 0x1608, 0x3B6, 0xFFFFD670, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_88_E411 end

    def Function_89_E430(): pass

    label("Function_89_E430")

    Sleep(750)
    OP_9B(0x1, 0xFE, 0x0, 0x4E2, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1C52, 0x1388, 0x1)
    Sound(811, 0, 70, 0)
    Sound(898, 0, 50, 0)

    def lambda_E462():
        OP_A6(0xFE, 0x64, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E462)
    Sleep(50)

    def lambda_E47E():
        OP_A6(0xFE, 0x32, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E47E)
    Sleep(450)
    OP_9B(0x1, 0xFE, 0x109, 0x96, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_89_E430 end

    def Function_90_E4AC(): pass

    label("Function_90_E4AC")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(625)
    Sound(812, 0, 100, 0)
    Sound(802, 0, 30, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(125)
    SetChrSubChip(0xFE, 0x5)
    Sleep(375)
    Return()

    # Function_90_E4AC end

    def Function_91_E4F1(): pass

    label("Function_91_E4F1")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    SetChrSubChip(0xFE, 0x6)
    Sleep(120)
    SetChrSubChip(0xFE, 0x7)
    Sleep(120)
    SetChrSubChip(0xFE, 0x8)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(300)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    Return()

    # Function_91_E4F1 end

    def Function_92_E57B(): pass

    label("Function_92_E57B")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    SetChrSubChip(0xFE, 0x6)
    Sleep(120)
    SetChrSubChip(0xFE, 0x7)
    Sleep(120)
    SetChrSubChip(0xFE, 0x8)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(300)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xA)
    Sleep(120)
    Return()

    # Function_92_E57B end

    def Function_93_E5F3(): pass

    label("Function_93_E5F3")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(200)
    SetChrSubChip(0xFE, 0xD)
    Sleep(200)
    SetChrSubChip(0xFE, 0xE)
    Sleep(400)
    Return()

    # Function_93_E5F3 end

    def Function_94_E617(): pass

    label("Function_94_E617")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(200)
    SetChrSubChip(0xFE, 0xD)
    Sleep(200)
    SetChrSubChip(0xFE, 0xE)
    Sleep(400)
    Return()

    # Function_94_E617 end

    def Function_95_E63B(): pass

    label("Function_95_E63B")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0x10)
    Sleep(429)
    Return()

    # Function_95_E63B end

    def Function_96_E65F(): pass

    label("Function_96_E65F")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x10)
    Sleep(143)
    SetChrSubChip(0xFE, 0x11)
    Sleep(143)
    SetChrSubChip(0xFE, 0x12)
    Sleep(429)
    Return()

    # Function_96_E65F end

    def Function_97_E689(): pass

    label("Function_97_E689")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_E6AB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_E6C3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_E6DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6FE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E721")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E744")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E762")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E780")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E79E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E79E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E7C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7F0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E814")

    label("loc_E7F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E814")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E814")

    Return()

    # Function_97_E689 end

    SaveToFile()

Try(main)
