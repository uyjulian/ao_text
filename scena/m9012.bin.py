from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Lawyer Ian",             # 1
        "KeA",                    # 2
        "Mariabell",              # 3
        "Demiurgos",              # 4
        "マリアベルフェード",     # 5
        "イアンターゲット",       # 6
        "キーアダミー",           # 7
        "SE制御",                 # 8
        "APL表示用",              # 9
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
        "Function_7_64B2",         # 07, 7
        "Function_8_651C",         # 08, 8
        "Function_9_6586",         # 09, 9
        "Function_10_65F0",        # 0A, 10
        "Function_11_665A",        # 0B, 11
        "Function_12_66C4",        # 0C, 12
        "Function_13_672E",        # 0D, 13
        "Function_14_674A",        # 0E, 14
        "Function_15_6769",        # 0F, 15
        "Function_16_6788",        # 10, 16
        "Function_17_67A7",        # 11, 17
        "Function_18_67C6",        # 12, 18
        "Function_19_67E5",        # 13, 19
        "Function_20_67F7",        # 14, 20
        "Function_21_6806",        # 15, 21
        "Function_22_6818",        # 16, 22
        "Function_23_682A",        # 17, 23
        "Function_24_6836",        # 18, 24
        "Function_25_6884",        # 19, 25
        "Function_26_68D2",        # 1A, 26
        "Function_27_6908",        # 1B, 27
        "Function_28_6945",        # 1C, 28
        "Function_29_6997",        # 1D, 29
        "Function_30_6AB7",        # 1E, 30
        "Function_31_6C06",        # 1F, 31
        "Function_32_6C7B",        # 20, 32
        "Function_33_6C97",        # 21, 33
        "Function_34_6CAC",        # 22, 34
        "Function_35_6CBB",        # 23, 35
        "Function_36_6D26",        # 24, 36
        "Function_37_6D3C",        # 25, 37
        "Function_38_6D52",        # 26, 38
        "Function_39_6D68",        # 27, 39
        "Function_40_6D7E",        # 28, 40
        "Function_41_6D94",        # 29, 41
        "Function_42_6DB1",        # 2A, 42
        "Function_43_6DCE",        # 2B, 43
        "Function_44_6DDD",        # 2C, 44
        "Function_45_6DEC",        # 2D, 45
        "Function_46_6E39",        # 2E, 46
        "Function_47_8E74",        # 2F, 47
        "Function_48_8EC3",        # 30, 48
        "Function_49_8EED",        # 31, 49
        "Function_50_8EF4",        # 32, 50
        "Function_51_8F10",        # 33, 51
        "Function_52_8F8E",        # 34, 52
        "Function_53_8FB0",        # 35, 53
        "Function_54_8FBE",        # 36, 54
        "Function_55_8FD8",        # 37, 55
        "Function_56_8FF5",        # 38, 56
        "Function_57_9014",        # 39, 57
        "Function_58_9F6B",        # 3A, 58
        "Function_59_9F7C",        # 3B, 59
        "Function_60_9FB7",        # 3C, 60
        "Function_61_A0DA",        # 3D, 61
        "Function_62_A274",        # 3E, 62
        "Function_63_A2F9",        # 3F, 63
        "Function_64_A308",        # 40, 64
        "Function_65_A31A",        # 41, 65
        "Function_66_A32C",        # 42, 66
        "Function_67_A338",        # 43, 67
        "Function_68_A386",        # 44, 68
        "Function_69_A3D4",        # 45, 69
        "Function_70_A3F1",        # 46, 70
        "Function_71_A436",        # 47, 71
        "Function_72_E810",        # 48, 72
        "Function_73_E857",        # 49, 73
        "Function_74_E8B5",        # 4A, 74
        "Function_75_E8E0",        # 4B, 75
        "Function_76_E90B",        # 4C, 76
        "Function_77_E92F",        # 4D, 77
        "Function_78_E983",        # 4E, 78
        "Function_79_E9A5",        # 4F, 79
        "Function_80_E9C7",        # 50, 80
        "Function_81_E9E9",        # 51, 81
        "Function_82_EA65",        # 52, 82
        "Function_83_EAE1",        # 53, 83
        "Function_84_EB28",        # 54, 84
        "Function_85_EB47",        # 55, 85
        "Function_86_EB66",        # 56, 86
        "Function_87_EB85",        # 57, 87
        "Function_88_EBA4",        # 58, 88
        "Function_89_EBC3",        # 59, 89
        "Function_90_EC3F",        # 5A, 90
        "Function_91_EC84",        # 5B, 91
        "Function_92_ED0E",        # 5C, 92
        "Function_93_ED86",        # 5D, 93
        "Function_94_EDAA",        # 5E, 94
        "Function_95_EDCE",        # 5F, 95
        "Function_96_EDF2",        # 60, 96
        "Function_97_EE1C",        # 61, 97
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
        "#40W──So you've come.\x02",
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
            "#3789V#40W#30AUhuhu...welcome.\x02\x03",
            "#3790V#40ATo the core of the principle of\x01",
            "causality of everything, at the\x01",
            "farthest reaches of the world.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED4")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3637V#20ANoｱl and Wazy too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_ED4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F45")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3638V#20ANoｱl and Rixia too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_F45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB2")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3639V#20ANoｱl and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_FB2")

    Jump("loc_1108")

    label("loc_FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1038")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3640V#20AWazy and Rixia too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_1038")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A5")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3641V#20AWazy and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_10A5")

    Jump("loc_1108")

    label("loc_10AA")


    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd...Elie...\x01",
            "...Tio...Randy...\x02\x03",
            "#3642V#20ARixia and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_1108")

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
        "#00007F#3330V#5P#N#30W#15AKeA...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 230, -1, -1)

    ChrTalk(
        0x103,
        (
            "#00214F#2694V#11P#N#30W#25AThank goodness...\x01",
            "You are safe...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(200, 230, -1, -1)

    ChrTalk(
        0x104,
        "#00307F#2774V#5P#N#30W#20AKeddo, are you ok!?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(120, 230, -1, -1)

    ChrTalk(
        0x102,
        (
            "#00108F#3407V#11P#N#30W#26AHonestly...!\x01",
            "You always make us worry...!\x02",
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
            "#12303F#3643V#5P#50W#20A...Sorry...\x02\x03",
            "#3644V#50AKeA...#800W...#50Walways had something...\x01",
            "That couldn't tell to Lloyd and you all...\x02",
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
            "#12313F#3645V#5P#40A#50W.......I'm sorry for...#800W...\x01",
            "#50W...Staying silent and deceiving you......\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5P#N......Don't apologise...!\x01",
            "You don't need to feel beholden!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#11P#NTo us is just enough\x01",
            "that you are safe...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#5P#NAlso, it's natural that kids keep\x01",
            "stuff secret from their parents \x01",
            "to a greater or lesser extent!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00103F#11P#NUsing even such a natural thing\x01",
            "you instigated KeA──\x02",
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
            "#00107F#11PBell, Lawyer Ian!\x01",
            "This is your doing, right!?\x02",
        )
    )

    Sleep(200)

    def lambda_1572():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1572)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x8,
        "#02203F#5PYes, precisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhuhu...how scary.\x02\x03",
            "#10800F#5PHowever, we are respecting\x01",
            "Miss KeA's will at the most.\x01\x02\x03",
            "#10811FIsn't that so── Miss KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#6P#N#30W............(*nod*)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00010F#11PKh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16B3")
    OP_FC(0xB)
    Jump("loc_16B6")

    label("loc_16B3")

    OP_FC(0xB)

    label("loc_16B6")


    ChrTalk(
        0x109,
        "#10101F#13PSmooth words make smooth ways...\x02",
    )

    CloseMessageWindow()

    label("loc_16E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1735")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1711")
    OP_FC(0xB)
    Jump("loc_1714")

    label("loc_1711")

    OP_FC(0xB)

    label("loc_1714")


    ChrTalk(
        0x106,
        "#10701F#13P......Hypocrite.\x02",
    )

    CloseMessageWindow()

    label("loc_1735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1799")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_175F")
    OP_FC(0xB)
    Jump("loc_1762")

    label("loc_175F")

    OP_FC(0xB)

    label("loc_1762")


    ChrTalk(
        0x105,
        (
            "#10406F#13POh boy.\x01",
            "You have quite the thick hide.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1799")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17C3")
    OP_FC(0xB)
    Jump("loc_17C6")

    label("loc_17C3")

    OP_FC(0xB)

    label("loc_17C6")


    ChrTalk(
        0x10A,
        "#00601F#13P............ \x02",
    )

    CloseMessageWindow()

    label("loc_17E4")


    ChrTalk(
        0x104,
        (
            "#00301F#11P...In any case, first come back\x01",
            "and then we'll talk at leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PRight.\x01",
            "A family council.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12309F#6P#N#40WEhehe...*chuckle*...\x01",
            "...Thank you, everyone...\x02\x03",
            "#12302FBut KeA...\x01",
            "Can't move from here...\x02\x03",
            "...So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PKeA...why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P...There's something right?\x01",
            "Related to the power as a "Sept-Terrion".\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#6P#6P#30W...That's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#6PUhuhu, Miss KeA.\x01",
            "Why don't you tell them?\x02\x03",
            "#10811FThat you are doing all this for\x01",
            "Mr. Lloyd and the others?\x02",
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
        "#00205F#11P#30WWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11P#30W...What the...\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#6P#N#40W............\x02",
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
            "#10800F#5PUnlike the once "Sept-Terrion of Mirage",\x01",
            "Miss KeA, who is the "Sept-Terrion of Zero", \x01",
            "possesses the powers of "time" and "space".\x02\x03",
            "#10804FWhen the power of "mirage", interfering with\x01",
            "the cause and effect cognizance, united with\x01",
            "the powers to tamper with space-time...\x02\x03",
            "#10811FMiss KeA obtained the\x01",
            ""power to spin the world".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6P#NT-The power to spin the world...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CEB")
    OP_FC(0xFFFA)
    Jump("loc_1CEE")

    label("loc_1CEB")

    OP_FC(0xFFF4)

    label("loc_1CEE")


    ChrTalk(
        0x109,
        "#10111F#13PT-That's...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D58")

    label("loc_1D10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D3A")
    OP_FC(0xFFFA)
    Jump("loc_1D3D")

    label("loc_1D3A")

    OP_FC(0xFFF4)

    label("loc_1D3D")


    ChrTalk(
        0x106,
        "#10712F#13PThat's...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1D58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DC3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D82")
    OP_FC(0xFFFA)
    Jump("loc_1D85")

    label("loc_1D82")

    OP_FC(0xFFF4)

    label("loc_1D85")


    ChrTalk(
        0x105,
        (
            "#10401F#13PYou threw at us uncommon\x01",
            "words once again...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1DC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DED")
    OP_FC(0xFFFA)
    Jump("loc_1DF0")

    label("loc_1DED")

    OP_FC(0xFFF4)

    label("loc_1DF0")


    ChrTalk(
        0x10A,
        "#00601F#13PWhat do you mean...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1E16")

    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02203F#11PThat very ability can be said to be at the base\x01",
            "as the goal of the "Azure-Zero Project"...\x02\x03",
            "#02201F"To spin the world"──\x01",
            "In other words, it's the power to manage the\x01",
            "principle of casuality, to rearrange the world.\x02",
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
        "#00305F#6P#N#4SHUUH...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#12P#NR-Rearrange the world...?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N#30W...The "system" network that every\x01",
            "phenomenon in the world possess...\x02\x03",
            "#00201FIs it the ability to manage and alter that\x01",
            "regarding past, present and future...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhuhu, that is Miss Tio for you.\x01",
            "You understand quickly.\x02\x03",
            "#10800FCorrect, it is something close to the\x01",
            "authority the manager of the orbal net\x01",
            "with the highest privileges can exert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02201F#11PChanging the reality that has produced a conflict\x01",
            "rearranging it to a more peaceful one...\x02\x03",
            "#02203FFor instance, replacing the reality\x01",
            "where Crossbell is dependent and made\x01",
            "fun of from the Empire and Republic...\x02\x03",
            "#02200FTo one where Crossbell reigns, as a\x01",
            ""suzerain state", on the two major powers.\x01",
            "That, in theory, is possible.\x02",
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
        "#00007F#6P#N......Wha......\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C5")
    OP_FC(0xFFFA)
    Jump("loc_23C8")

    label("loc_23C5")

    OP_FC(0xFFF4)

    label("loc_23C8")


    ChrTalk(
        0x109,
        "#10101F#13PE-Ehhm...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_23E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2430")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_240E")
    OP_FC(0xFFFA)
    Jump("loc_2411")

    label("loc_240E")

    OP_FC(0xFFF4)

    label("loc_2411")


    ChrTalk(
        0x10A,
        "#00610F#13PN-Nonsense...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2430")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_247F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_245A")
    OP_FC(0xFFFA)
    Jump("loc_245D")

    label("loc_245A")

    OP_FC(0xFFF4)

    label("loc_245D")


    ChrTalk(
        0x106,
        "#10706F#13P...Impossible...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_247F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A9")
    OP_FC(0xFFFA)
    Jump("loc_24AC")

    label("loc_24A9")

    OP_FC(0xFFF4)

    label("loc_24AC")


    ChrTalk(
        0x105,
        (
            "#10410F#13P...That should be an impossible\x01",
            "deed even for the Goddess...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_24FA")


    ChrTalk(
        0x104,
        (
            "#00307F#6P#NHey now, say what you like, but\x01",
            "isn't that too much of a gag...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#N...As you can imagine...\x01",
            "That's suddenly unbelievable.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5P*chuckle chuckle*...\x01",
            "You say strange things.\x02\x03",
            "#10811F──Since even you have\x01",
            "been saved by that once.\x02",
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
        "#00305F#6P#NHuh...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00105F#12P#NS-Saved...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N...Don't tell me that...\x01",
            "...What we saw before...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00010F#6P#NWhen we infiltrated the Cult\x01",
            "lodge some months ago...!?\x02",
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
        "#00011F#6P#N#50W......Ah......\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PUh uh, it looks like \x01",
            "Mr. Lloyd has "remembered".\x02\x03",
            "#10804FReality alteration has been already performed\x01",
            "once, although on a very small scale.\x02\x03",
            "#10811FThe reality alteration of the fact that you all had \x01",
            "been killed by Joachim when he went berserk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N#30W............\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#6P#N#30W.......Are you...kiddin' me...?\x02",
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
            "#12306F#11P#30WThe first time... You guys\x01",
            "weren't so close with Estelle,\x01",
            "Joshua and Renne too...\x02",
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
            "#12308F#11PBeing that the case, you entered only in four...\x01",
            "...In the end, that child's help never came...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 0, 0, 40)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0xA,
        (
            "#10800F#5PMiss KeA who "knew" that, let the power\x01",
            "as a "Sept-Terrion" run wild and interfered\x01",
            "with the principle of causality of the past.\x02\x03",
            "#10804FThat result brought to the cause-effect of you\x01",
            "solving the "Angel of Slaughter"'s problem...\x02\x03",
            "One thing led to another and the two Liberl\x01",
            "Bracers showed up as your helpers...\x02\x03",
            "#10811FAnd then── In the scene where you\x01",
            "originally should have been killed, the\x01",
            "Angel of Slaughter came to save you.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_301E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FF9")
    OP_FC(0xFFFA)
    Jump("loc_2FFC")

    label("loc_2FF9")

    OP_FC(0xFFF4)

    label("loc_2FFC")


    ChrTalk(
        0x109,
        "#10110F#13PN-No way...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_30C3")

    label("loc_301E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3074")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3048")
    OP_FC(0xFFFA)
    Jump("loc_304B")

    label("loc_3048")

    OP_FC(0xFFF4)

    label("loc_304B")


    ChrTalk(
        0x106,
        "#10708F#13P...Such a thing...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_30C3")

    label("loc_3074")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30C3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_309E")
    OP_FC(0xFFFA)
    Jump("loc_30A1")

    label("loc_309E")

    OP_FC(0xFFF4)

    label("loc_30A1")


    ChrTalk(
        0x10A,
        "#00610F#13P...Impossible...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_30C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3134")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30ED")
    OP_FC(0xFFFA)
    Jump("loc_30F0")

    label("loc_30ED")

    OP_FC(0xFFF4)

    label("loc_30F0")


    ChrTalk(
        0x105,
        (
            "#10403F#13P...But...\x01",
            "It doesn't seem they're all lies.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_321B")

    label("loc_3134")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_315E")
    OP_FC(0xFFFA)
    Jump("loc_3161")

    label("loc_315E")

    OP_FC(0xFFF4)

    label("loc_3161")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...However...\x01",
            "It doesn't appear they're all lies.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_321B")

    label("loc_31AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_321B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D5")
    OP_FC(0xFFFA)
    Jump("loc_31D8")

    label("loc_31D5")

    OP_FC(0xFFF4)

    label("loc_31D8")


    ChrTalk(
        0x106,
        (
            "#10703F#13P...However...\x01",
            "It doesn't seem they're all lies.\x02",
        )
    )

    OP_5A()
    OP_57(0x0)
    OP_5A()

    label("loc_321B")

    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#30W............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10804F#5PUhuhu...as expected, it\x01",
            "looks like it was a shock, eh?\x02\x03",
            "#10800FHowever, the true meaning of the "power to rearrange\x01",
            "reality" the "Sept-Terrion of Zero" possesses──\x02\x03",
            "Avoiding your tragedy was nothing\x01",
            "more than just the beginning.\x02",
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
            "#10804F#5PThis "Tree of Azure"──\x02\x03",
            "Amplifies Miss KeA's power.\x01",
            "With a divine tree that can link with the\x01",
            "world itself through the Septium veins...\x02\x03",
            "#10811F#5PLet alone avoiding tragedies, it\x01",
            "could be possible to alter reality at the\x01",
            "level Mr. Grimwood was saying just before.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00013F#6P#N...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#12P#NThat is this "huge tree" power...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N...Hey now...\x01",
            "That's not funny...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_355B")
    OP_FC(0xFFFA)
    Jump("loc_355E")

    label("loc_355B")

    OP_FC(0xFFF4)

    label("loc_355E")


    ChrTalk(
        0x105,
        (
            "#10408F#13P(...I see...\x01",
            "The same as the original "Primal Ground"...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_35A9")


    ChrTalk(
        0xA,
        (
            "#10802F#5P#30WUhuhu...wonderful, right?\x02\x03",
            "#10809FIf we have such a wonderful thing,\x01",
            "we wouldn't have to fear anything...!\x02\x03",
            "We could give happiness to the entire world!\x01",
            "No more sorrows!\x02\x03",
            "Man would be free from all anxieties\x01",
            "and could pursue only "the good"!\x02\x03",
            "#10811FNo doubt that would be alchemy's most\x01",
            "secretive skill── What is called "Ars\x01",
            "Magna", the great secret formula!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#6P#NBell...you...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#N............\x02",
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
            "#00003F#6P#N──Lawyer Ian.\x02\x03",
            "#00013FAre you really fine with that?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02201F#11P#30W............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02211F#11P...In anything one does, preparations are needed.\x02\x03",
            "Human history is also one that\x01",
            "deals with all kinds of risk...\x02\x03",
            "And KeA has the wonderful\x01",
            "power to control that.\x02\x03",
            "That's an undeniable "reality".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NEven if the result was to\x01",
            "imprison KeA in such a place...?\x02\x03",
            "#00008FI heard that the previous "Sept-Terrion \x01",
            "of Mirage" before long was grieving and\x01",
            "came to the conclusion to erase itself.\x02\x03",
            "#00013FDo you really intend...\x01",
            "To force such a heavy responsibility\x01",
            "on a single little girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12300F#5P#NLloyd, that's──\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PUhuhu, that is why we are here,\x01",
            "so it does not turn that way.\x02\x03",
            "#10804FIt is not to force the entire responsibility\x01",
            "of world alterations on Miss KeA...\x02\x03",
            "Knowledgeable persons like Mr. Grimwood\x01",
            "are going to advise her for changing the\x01",
            "world into a "more right direction".\x02\x03",
            "#10802FIsn't it a different story doing it like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#NY-You will completely deny\x01",
            "a democratic process...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P...Elie, you too should know well\x01",
            "democracy's harmful effects.\x02\x03",
            "A system prone to fall to mobocracy\x01",
            "and that can't even have its way in\x01",
            "deciding important things quickly...\x02\x03",
            "#02201FIsn't it a reality you can see not\x01",
            "only in Crossbell, but anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N#30W...Well...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02200F#11PAlso, I don't intend to suggest\x01",
            "to KeA only my own opinions.\x02\x03",
            "#02203FI want to request the cooperation of knowledgeable \x01",
            "persons like Chairman MacDowell too.\x02\x03",
            "Dieter too would be useful\x01",
            "again from a management\x01",
            "point of view.\x02\x03",
            "#02200FAlso── I want your collaboration\x01",
            "to our experiments too.\x02",
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
            "#02203F#11PTo open up the path to a new era,\x01",
            "we need your youths' views too.\x02\x03",
            "#02201FAlso, you all who...\x02\x03",
            "You all who managed to reach this place...\x01",
            "I'm sure you personally understand\x01",
            "what's needed for the future era.\x02\x03",
            "#02200FWhat do you think── about this proposal?\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P#N#30W...T-That would be...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N#30WDamn... It's got an odd\x01",
            "persuasive power, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#6P#N#30W............\x02",
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
            "#00006F#6P#N...Lawyer Ian.\x02\x03",
            "#00003FYou haven't replied\x01",
            "to my question yet.\x02\x03",
            "#00001F#6P#NAre you──\x01",
            "Are you really fine with that?\x02",
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
            "#00003F#6P#N#30WEvery thing has got its own "dignity".\x02\x03",
            "Man, society, history too.\x02\x03",
            "#00008FEven if they're connected by mistakes\x01",
            "and results that produce tragedies...\x02\x03",
            "#00013FPretending that those never happened,\x01",
            "it's violating the "dignity" of the\x01",
            "people concerned with those.\x02\x03",
            "#00006FFor instance, like the dignity of the people who\x01",
            "obtain strength after recovering from a tragedy...\x02\x03",
            "#00002FActually...\x01",
            "You understand that too, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W............\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x102,
        "#00102F#12P#N#30WLloyd...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4449")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43E5")
    OP_FC(0xFFFA)
    Jump("loc_43E8")

    label("loc_43E5")

    OP_FC(0xFFF4)

    label("loc_43E8")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#30WIndeed...\x01",
            "Man isn't an existence that\x01",
            "can only take right decisions...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_4553")

    label("loc_4449")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4473")
    OP_FC(0xFFFA)
    Jump("loc_4476")

    label("loc_4473")

    OP_FC(0xFFF4)

    label("loc_4476")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#30WIndeed...\x01",
            "Man is an existence that at\x01",
            "times commits mistakes.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_4553")

    label("loc_44CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4553")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44F8")
    OP_FC(0xFFFA)
    Jump("loc_44FB")

    label("loc_44F8")

    OP_FC(0xFFF4)

    label("loc_44FB")


    ChrTalk(
        0x106,
        (
            "#10708F#13P#30W...Indeed...\x01",
            "Man is an existence that at\x01",
            "times commits mistakes...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4553")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45EA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_457D")
    OP_FC(0xFFFA)
    Jump("loc_4580")

    label("loc_457D")

    OP_FC(0xFFF4)

    label("loc_4580")


    ChrTalk(
        0x105,
        (
            "#10401F#13P#30WHowever, by pretending those\x01",
            "mistakes never happened,\x01",
            "man can't even grow up...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_470F")

    label("loc_45EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_467F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4614")
    OP_FC(0xFFFA)
    Jump("loc_4617")

    label("loc_4614")

    OP_FC(0xFFF4)

    label("loc_4617")


    ChrTalk(
        0x106,
        (
            "#10701F#13P#30WStill, by pretending those\x01",
            "mistakes never happened,\x01",
            "man can't even grow up...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_470F")

    label("loc_467F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_470F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A9")
    OP_FC(0xFFFA)
    Jump("loc_46AC")

    label("loc_46A9")

    OP_FC(0xFFF4)

    label("loc_46AC")


    ChrTalk(
        0x109,
        (
            "#10101F#13P#30WHowever, by pretending those\x01",
            "mistakes never happened,\x01",
            "man won't ever grow up.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_470F")


    ChrTalk(
        0x103,
        (
            "#00204F#12P#N#30W...The meaning of learning together,\x01",
            "cooperating, progressing forward...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00300F#6P#N#30WYeah, it would mean endin' up\x01",
            "cleanly castin' away all that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W............\x02",
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
            "#12305F#5P#N#30W......Lloyd......\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00004F#11P──KeA.\x01",
            "Come back with us.\x02\x03",
            "#00000FYou don't need to overdo yourself\x01",
            "for us anymore than this.\x02",
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
            "#12313F#5P#N...............\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#11P...When we lost\x01",
            "our lives before...\x02\x03",
            "We made you feel...\x01",
            "Heart-broken, in pain and sad.\x02\x03",
            "#00006FSorry, KeA.\x01",
            "It was our fault for being worthless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#5P#N#30WT-That's not true...!\x02\x03",
            "#12313F...KeA did that\x01",
            "on her own will...!\x02\x03",
            "So, Lloyd, you don't have to apologize──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#11PThen, KeA.\x02\x03",
            "#00013FWhy have you always\x01",
            "been looking depressed?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#5P#N...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYou noticed it too, right, KeA?\x02\x03",
            "#00008FThat you ended up changing reality\x01",
            "by managing the principle of causality\x01",
            "because you were so sad for our deaths...\x02\x03",
            "#00013F──You realized that was "unfair".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N#40W......oh......\x02\x03",
            "#12308F............\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#11P...KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, can't really say I'd be\x01",
            "glad with us bein' dead, but...\x02\x03",
            "#00300FEven so, I can say that was\x01",
            "surely an "illegal move".\x02",
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
            "#00106F#11P...Mr. Grimwood, Bell.\x02\x03",
            "About that...\x01",
            "I think that "politics" is the same.\x02\x03",
            "#00108FSometimes, there're times when doing\x01",
            "things not the proper way is needed too.\x02\x03",
            "#00101FHowever, since it's not a\x01",
            "proper way, it's wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02201F#5P......Elie......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10801F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PRelying on the personal transcendental\x01",
            "powers of KeA...\x02\x03",
            "That's not politics anymore,\x01",
            "that's a mere praying to a god.\x02\x03",
            "#00108FOvercoming difficult circumstances with the\x01",
            "proper procedures and a dialogue system,\x01",
            "solving them as everyone's problem...\x02\x03",
            "#00101FThat's what I think "true politics" is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI think it's very possible that\x01",
            "without KeA's power, Crossbell\x01",
            "will be confronted with serious dangers.\x02\x03",
            "#00008FUnrest in the whole continent, economic crisis...\x01",
            "Also, as soon as the civil war in the Empire is\x01",
            "over, it'll probably bare its teeth to Crossbell.\x02",
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
            "#00013F#11P──And yet, I can't really think\x01",
            "that forcing everything on KeA\x01",
            "would be the right choice.\x02\x03",
            "#00004FIf we relied only on given miracles,\x01",
            "we would never grow up...\x02\x03",
            "#00000FThat's why, even if it's painful...\x01",
            "I think that now we have to\x01",
            "proceed in "the proper way".\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W...Lloyd...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x8,
        "#02203F#5P#40W............\x02",
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
        "#02211F#11P#40W......So this is it.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 28)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40WI...thought it wasn't\x01",
            "a personal grudge, but...\x02\x03",
            "Really... In some respects,\x01",
            "it's like I was deceiving myself.\x02\x03",
            "#02200F...It seemed just like I was\x01",
            "been admonished by Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#N...Mr. Grimwood...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40W...I'm sorry.\x01",
            "I didn't have the right to tell you.\x02\x03",
            "............\x02",
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
            "#02203F#11P#30W......KeA. I'm sorry to have\x01",
            "misleaded you in many things.\x02\x03",
            "#02201FYou should decide what to do...\x01",
            "Using your own judgement.\x02\x03",
            "#02202FYou should be able to do that, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W...Mister....\x02",
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
            "#02203F#11P#30WAlso, Mariabell... I'm sorry for not\x01",
            "having lived up to your expectations.\x02\x03",
            "#02201FIt seems that my role ends here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#6PUhuhu...I do not mind.\x02\x03",
            "After all, I was the one who originally\x01",
            "begged you for a comprehensive\x01",
            "planning of the project.\x02\x03",
            "#10811FThank you for all your hard work\x01",
            "up to now── Mr. Grimwood.\x02",
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

    def lambda_5686():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5686)
    BeginChrThread(0xC, 3, 0, 33)
    Sleep(250)

    def lambda_56A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_56A0)
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

    def lambda_57C9():

        label("loc_57C9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_57C9")

    QueueWorkItem2(0x101, 2, lambda_57C9)

    def lambda_57DB():

        label("loc_57DB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_57DB")

    QueueWorkItem2(0x102, 2, lambda_57DB)

    def lambda_57ED():

        label("loc_57ED")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_57ED")

    QueueWorkItem2(0x103, 2, lambda_57ED)

    def lambda_57FF():

        label("loc_57FF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_57FF")

    QueueWorkItem2(0x104, 2, lambda_57FF)

    def lambda_5811():

        label("loc_5811")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5811")

    QueueWorkItem2(0xF4, 2, lambda_5811)

    def lambda_5823():

        label("loc_5823")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5823")

    QueueWorkItem2(0xF5, 2, lambda_5823)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x8,
        "#02212F#11P#10A...ghh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12313F#N!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#12P#NWha...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#12P#N...Bell...!?\x02",
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
            "#02213F#11P#60W...Ha ha...\x01",
            "...This too is...karma retribution, eh...?\x02\x03",
            "#70WGuy... Lloyd...\x01",
            "......I'm...sorry...\x02",
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
        "#00207F#5PLawyer Ian...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A0F")

    ChrTalk(
        0x10A,
        "#00610F#5PWhat did you...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A78")

    label("loc_5A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A45")

    ChrTalk(
        0x109,
        "#10110F#5PHow could you...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A78")

    label("loc_5A45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A78")

    ChrTalk(
        0x106,
        "#10707F#5P...How could you...\x02",
    )

    CloseMessageWindow()

    label("loc_5A78")

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

    def lambda_5AE5():
        TurnDirection(0x101, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5AE5)
    Sleep(0)

    def lambda_5AF5():
        TurnDirection(0x102, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5AF5)
    Sleep(0)

    def lambda_5B05():
        TurnDirection(0x103, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5B05)
    Sleep(0)

    def lambda_5B15():
        TurnDirection(0x104, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B15)
    Sleep(0)

    def lambda_5B25():
        TurnDirection(0xF4, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5B25)
    Sleep(0)

    def lambda_5B35():
        TurnDirection(0xF5, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5B35)
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
            "#12313F#12PBell...why!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#5PUhuhu, I only disposed\x01",
            "of a useless tool.\x02\x03",
            "#10811FIn that sense, Miss KeA.\x01",
            "──You too are not an exception, you know?\x02",
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
            "#12311F#3646V#5P#50W#18A...Uwaah...!?\x02",
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
        "#00007F#5PKeA...!?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PHey...!\x01",
            "The fuck are you doin' to our kid!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#10804F#5PUh uh, if she will be more hesitant\x01",
            "than this, I will have her turn into\x01",
            "an adorable doll which has no will...\x02\x03",
            "#10811FBy nature, she is a homunculus who was\x01",
            "given life to by the Crois clan secret arts...\x02\x03",
            "Is it not my own way\x01",
            "how to deal with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PS-Stop screwing around...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#11PBell...!\x01",
            "There're some things you can say, \x01",
            "and some things you can't!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00207F#5P...I'll have you retract that...!\x02",
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
            "#3791V#40W#36AUhuhuhuhu...very well.\x02\x03",
            "#3792V#25AI am Mariabell Crois.\x02\x03",
            "#3793V#50ADescendant of the clan\x01",
            "that sacrificed everything...\x02\x03",
            "To seek a "Sept-Terrion"\x01",
            "to surpass the Goddess.\x02\x03",
            "#3794V#71AWhich is really strong?\x01",
            "The weight of a 1000 years\x01",
            "deep-rooted delusion?\x02\x03",
            "Or your bonds that do not\x01",
            "even amount to 1 year...?\x02\x03",
            "#3795V#35AShould we try to compare\x01",
            "those using the full\x01",
            "extent of our powers?\x02",
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
        "#00007F#6P#30W#15A...That's what I want!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#30W#20A#NBell...!\x01",
            "I won't go easy on you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6361")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62F7")
    OP_FC(0x6)
    Jump("loc_62FA")

    label("loc_62F7")

    OP_FC(0xC)

    label("loc_62FA")


    ChrTalk(
        0x105,
        (
            "#10407F#13P#30W#25A#NRecognized as a supreme Magius...!\x01",
            "I'll suppress you with all my power!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6484")

    label("loc_6361")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_638B")
    OP_FC(0x6)
    Jump("loc_638E")

    label("loc_638B")

    OP_FC(0xC)

    label("loc_638E")


    ChrTalk(
        0x106,
        (
            "#10707F#13P#30W#25A#NAware of my black supernatural powers...!\x01",
            "I'll exorcise you with all my might!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6484")

    label("loc_63FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6484")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6426")
    OP_FC(0x6)
    Jump("loc_6429")

    label("loc_6426")

    OP_FC(0xC)

    label("loc_6429")


    ChrTalk(
        0x109,
        (
            "#10107F#13P#30W#25A#NEstimated danger level: S...!\x01",
            "I'll attack with all my firepower!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6484")

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

    def Function_7_64B2(): pass

    label("Function_7_64B2")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_64F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64F1)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_7_64B2 end

    def Function_8_651C(): pass

    label("Function_8_651C")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_655B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_655B)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_8_651C end

    def Function_9_6586(): pass

    label("Function_9_6586")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_65C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65C5)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_9_6586 end

    def Function_10_65F0(): pass

    label("Function_10_65F0")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_662F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_662F)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_10_65F0 end

    def Function_11_665A(): pass

    label("Function_11_665A")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6699():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6699)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_11_665A end

    def Function_12_66C4(): pass

    label("Function_12_66C4")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6703():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6703)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_12_66C4 end

    def Function_13_672E(): pass

    label("Function_13_672E")

    OP_95(0xFE, 0, 1000, -12060, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_672E end

    def Function_14_674A(): pass

    label("Function_14_674A")

    Sleep(50)
    OP_95(0xFE, 1120, 1000, -13300, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_674A end

    def Function_15_6769(): pass

    label("Function_15_6769")

    Sleep(100)
    OP_95(0xFE, 420, 1000, -14370, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_6769 end

    def Function_16_6788(): pass

    label("Function_16_6788")

    Sleep(150)
    OP_95(0xFE, -1270, 1000, -13930, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_6788 end

    def Function_17_67A7(): pass

    label("Function_17_67A7")

    Sleep(200)
    OP_95(0xFE, -2540, 1990, -13310, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_67A7 end

    def Function_18_67C6(): pass

    label("Function_18_67C6")

    Sleep(250)
    OP_95(0xFE, 2540, 1000, -13510, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_67C6 end

    def Function_19_67E5(): pass

    label("Function_19_67E5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_67E5 end

    def Function_20_67F7(): pass

    label("Function_20_67F7")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_67F7 end

    def Function_21_6806(): pass

    label("Function_21_6806")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_6806 end

    def Function_22_6818(): pass

    label("Function_22_6818")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_6818 end

    def Function_23_682A(): pass

    label("Function_23_682A")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_682A end

    def Function_24_6836(): pass

    label("Function_24_6836")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6856")
    Sound(540, 0, 50, 0)
    Jump("loc_687B")

    label("loc_6856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_687B")
    Sound(531, 0, 100, 0)

    label("loc_687B")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_6836 end

    def Function_25_6884(): pass

    label("Function_25_6884")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68A4")
    Sound(540, 0, 50, 0)
    Jump("loc_68C9")

    label("loc_68A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68C9")
    Sound(531, 0, 100, 0)

    label("loc_68C9")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_6884 end

    def Function_26_68D2(): pass

    label("Function_26_68D2")

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

    # Function_26_68D2 end

    def Function_27_6908(): pass

    label("Function_27_6908")

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

    # Function_27_6908 end

    def Function_28_6945(): pass

    label("Function_28_6945")

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

    # Function_28_6945 end

    def Function_29_6997(): pass

    label("Function_29_6997")

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

    # Function_29_6997 end

    def Function_30_6AB7(): pass

    label("Function_30_6AB7")

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

    # Function_30_6AB7 end

    def Function_31_6C06(): pass

    label("Function_31_6C06")

    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)

    label("loc_6C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7A")
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
    Jump("loc_6C24")

    label("loc_6C7A")

    Return()

    # Function_31_6C06 end

    def Function_32_6C7B(): pass

    label("Function_32_6C7B")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(600)
    Return()

    # Function_32_6C7B end

    def Function_33_6C97(): pass

    label("Function_33_6C97")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_33_6C97 end

    def Function_34_6CAC(): pass

    label("Function_34_6CAC")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_34_6CAC end

    def Function_35_6CBB(): pass

    label("Function_35_6CBB")

    SetChrPos(0x8, 9600, 700, -9900, 305)
    SetChrChipByIndex(0x8, 0x21)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x5)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_35_6CBB end

    def Function_36_6D26(): pass

    label("Function_36_6D26")

    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(429)
    Return()

    # Function_36_6D26 end

    def Function_37_6D3C(): pass

    label("Function_37_6D3C")

    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_37_6D3C end

    def Function_38_6D52(): pass

    label("Function_38_6D52")

    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(500)
    Return()

    # Function_38_6D52 end

    def Function_39_6D68(): pass

    label("Function_39_6D68")

    SetChrSubChip(0xFE, 0x12)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(667)
    Return()

    # Function_39_6D68 end

    def Function_40_6D7E(): pass

    label("Function_40_6D7E")

    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(667)
    Return()

    # Function_40_6D7E end

    def Function_41_6D94(): pass

    label("Function_41_6D94")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_41_6D94 end

    def Function_42_6DB1(): pass

    label("Function_42_6DB1")

    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_42_6DB1 end

    def Function_43_6DCE(): pass

    label("Function_43_6DCE")

    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    Return()

    # Function_43_6DCE end

    def Function_44_6DDD(): pass

    label("Function_44_6DDD")

    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    Return()

    # Function_44_6DDD end

    def Function_45_6DEC(): pass

    label("Function_45_6DEC")

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

    # Function_45_6DEC end

    def Function_46_6E39(): pass

    label("Function_46_6E39")

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
            "#12306F#5P#60W...*huuuh*...*pant pant*...\x02",
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
        "#00007F#5P#4SKeA, are you all right!?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#N#45W...Yes...\x01",
            "Eheheh...somehow...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00214F#5PThank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5P*sigh*, boy oh boy...\x02",
    )

    CloseMessageWindow()

    def lambda_7368():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7368)
    WaitChrThread(0xA, 2)
    Sleep(500)
    PlayBGM("ed7572", 0)

    ChrTalk(
        0xA,
        (
            "#10803F#11P#30WKh...I see.\x02\x03",
            "#10801FAs expected... You did not beat\x01",
            "Mr. Arios and the others for nothing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBell...stop it here!\x02\x03",
            "#00101FThere's no more meaning\x01",
            "in fighting us!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11P#30WUhuhu, my cute Elie.\x02\x03",
            "I do not think this is an\x01",
            "unexpected request from you, but...\x02\x03",
            "#10811FYou know, right...?\x01",
            "That it is my personality\x01",
            "to tease cute girls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PW-What're you...\x02",
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
            "#10802F#5P#30W──By the way, Miss KeA.\x02\x03",
            "I wonder if Mr. Lloyd and the\x01",
            "others know about "that thing"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#N#30W......Ah......\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhuhu, looking at your reaction\x01",
            "it appears you have not told them?\x02\x03",
            "#10811FThat is just perfect.\x01",
            "Let us tell them too now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#11P#N#30WN-No...stop...\x02\x03",
            "#12311F...Bell...I beg you...!\x02",
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
        "#00013F#5P...What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PHey, young lady!\x02\x03",
            "Don't tease out\x01",
            "Keddo, got it!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#11PUhuhu, you all really\x01",
            "love Miss KeA, right?\x02\x03",
            "#10800FA homunculus without a genuine soul\x01",
            "entrusted to the "Cult" by the Crois clan....\x02\x03",
            "An imitation doll just to tie together the\x01",
            "countless souls the Cult sacrificed.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5PWhat's with that again!?\x02\x03",
            "#00010FWe know about that after having\x01",
            "heard it from Zeit a long time ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PKeA staying at our\x01",
            "side as KeA...\x02\x03",
            "#00201FThere is anything more\x01",
            "important than that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11PUhuhu, Miss KeA.\x01",
            "You are really lucky, eh?\x02\x03",
            "You have been able to gather the favor and\x01",
            "affection of Mr. Lloyd and the others...\x01",
            "No, of all the people you came in touch with.\x02\x03",
            "#10811F──Because of your powers.\x02",
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

    def lambda_7AE5():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7AE5)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_7B05():
        OP_A6(0xFE, 0x0, 0x32, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7B05)
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
            "#12306F#5P#N#50W......Uuuh......Aaah....\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00005F#6P#N......Huh......\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#N......Bell......\x01",
            "What did you just...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10811F#11P#30WEh eh... Did you not find\x01",
            "it strange, I wonder?\x02\x03",
            "Since after just having met her,\x01",
            "you probably could not help but\x01",
            "love her and wanting to protect her?\x02\x03",
            "Why do you think it is like that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#N......No...way...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#6P#NHey now, what nonsense are you...\x02",
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
            "#10804F#11P#30W──It goes without saying for that Joachim,\x01",
            "but neither the mafia nor even the monsters\x01",
            "tried to initiatively harm Miss KeA.\x02\x03",
            "A little girl with whom everyone gets\x01",
            "along well immediately, who ends up\x01",
            "being loved unconditionally...\x02\x03",
            "#10811FHas anyone ever thought to\x01",
            "question that abnormality?\x02",
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
            "#12307F#3647V#5P#N#50W#30A...No...it's not like that...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0xA,
        "#10803F#11P#30W#15ANo── it IS like that.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#10801F#11P#40W#30AAlthough unconsciously, you have the\x01",
            "power to catch hold of the hearts and\x01",
            "souls of the people who surround you.\x02\x03",
            "#10804F#40W#30AThe power to manage the principle\x01",
            "of causality and cognizance to have\x01",
            "everybody love you, protect you.\x02\x03",
            "#10811F#40W#30AEh eh... An imitation of love for\x01",
            "an imitation of existence, eh?\x02",
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
            "#12311F#3648V#11P#N#4S#20A#80WNOOOOOOOHH!!\x07\x00\x02",
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
        "#00110F#5P#40W#20A......Ah......\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_860F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85DA")
    OP_FC(0x5)
    Jump("loc_85DD")

    label("loc_85DA")

    OP_FC(0xB)

    label("loc_85DD")


    ChrTalk(
        0x105,
        "#10410F#13P#40W#20A...This spiritual...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C5")

    label("loc_860F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_866D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8639")
    OP_FC(0x5)
    Jump("loc_863C")

    label("loc_8639")

    OP_FC(0xB)

    label("loc_863C")


    ChrTalk(
        0x106,
        "#10707F#13P#40W#20AT-This spiritual...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C5")

    label("loc_866D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8697")
    OP_FC(0x5)
    Jump("loc_869A")

    label("loc_8697")

    OP_FC(0xB)

    label("loc_869A")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20A...T-This light...\x02",
    )

    CloseMessageWindow()

    label("loc_86C5")

    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8727")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86F2")
    OP_FC(0x5)
    Jump("loc_86F5")

    label("loc_86F2")

    OP_FC(0xB)

    label("loc_86F5")


    ChrTalk(
        0x10A,
        "#00610F#13P#40W#20AAn azure..."god"...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_87E0")

    label("loc_8727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8786")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8751")
    OP_FC(0x5)
    Jump("loc_8754")

    label("loc_8751")

    OP_FC(0xB)

    label("loc_8754")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20AAn azure..."god"...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_87E0")

    label("loc_8786")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B0")
    OP_FC(0x5)
    Jump("loc_87B3")

    label("loc_87B0")

    OP_FC(0xB)

    label("loc_87B3")


    ChrTalk(
        0x106,
        "#10700F#13P#40W#20AAn azure..."god"...?\x02",
    )

    CloseMessageWindow()

    label("loc_87E0")

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
        "#00007F#3331V#6P#N#4S#25AKeAAAAAAH!!\x02",
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
            "#10804F#3796V#6P#N#40W#82AEh eh, this is the form of the beginning\x01",
            "after the total unification of the "Sept-\x01",
            "Terrion of Zero" with the "Tree of Azure"...\x02\x03",
            "#3797V#80AThe God of the false world who manipulates\x01",
            "the space-time principle of causality of\x01",
            "everything and truly shatters the\x01",
            "shackles imposed by the Goddess...!\x02\x03",
            "#10811F#3798V#35AThe "Azure Demiourgos"! \x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00010F#3332V#6P#N#30W#25AI don't give a damn of your tedious talk!\x02\x03",
            "#3333V#35AEverything will start after...\x01",
            "We have taken back that child, KeA!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#2775V#6P#N#30W#32AYeah, it's not late for \x01",
            "complex talks after that!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#2695V#12P#N#30W#40A──Confirmed the manifestation of a\x01",
            "gigantic spiritual body! KeA is\x01",
            "inside the core part in its center!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#3408V#12P#N#30W#32AWe must recover KeA from\x01",
            "there at any cost!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00015F#3334V#6P#N#30AEveryone──\x01",
            "This the final battle...!\x02\x03",
            "#00007F#3335V#50ALet's strike hard that azure existence with\x01",
            "everything we've got, body and soul!!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D35")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D2C")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_8D35")

    label("loc_8D2C")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_8D35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D62")
    Sound(2417, 255, 100, 4)
    Jump("loc_8D68")

    label("loc_8D62")

    Sound(2417, 255, 100, 3)

    label("loc_8D68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D95")
    Sound(4115, 255, 100, 4)
    Jump("loc_8D9B")

    label("loc_8D95")

    Sound(4115, 255, 100, 3)

    label("loc_8D9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DC8")
    Sound(3174, 255, 100, 4)
    Jump("loc_8DCE")

    label("loc_8DC8")

    Sound(3174, 255, 100, 3)

    label("loc_8DCE")

    SetChrName("Members")

    AnonymousTalk(
        0xFF,
        "#5S#15AYEAH!!\x02",
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

    # Function_46_6E39 end

    def Function_47_8E74(): pass

    label("Function_47_8E74")

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

    # Function_47_8E74 end

    def Function_48_8EC3(): pass

    label("Function_48_8EC3")

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

    # Function_48_8EC3 end

    def Function_49_8EED(): pass

    label("Function_49_8EED")

    Sound(898, 0, 100, 0)
    Return()

    # Function_49_8EED end

    def Function_50_8EF4(): pass

    label("Function_50_8EF4")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(400)
    Return()

    # Function_50_8EF4 end

    def Function_51_8F10(): pass

    label("Function_51_8F10")

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

    # Function_51_8F10 end

    def Function_52_8F8E(): pass

    label("Function_52_8F8E")

    OP_71(0x0, 0x821, 0x82A, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xF, 3, 0, 55)
    OP_71(0x0, 0x835, 0x85B, 0x0, 0x20)
    Return()

    # Function_52_8F8E end

    def Function_53_8FB0(): pass

    label("Function_53_8FB0")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7460", 0)
    Return()

    # Function_53_8FB0 end

    def Function_54_8FBE(): pass

    label("Function_54_8FBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FD7")
    Sound(824, 0, 100, 0)
    Sleep(1300)
    Jump("Function_54_8FBE")

    label("loc_8FD7")

    Return()

    # Function_54_8FBE end

    def Function_55_8FD8(): pass

    label("Function_55_8FD8")

    Sleep(200)

    label("loc_8FDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FF4")
    Sound(824, 0, 50, 0)
    Sleep(3800)
    Jump("loc_8FDB")

    label("loc_8FF4")

    Return()

    # Function_55_8FD8 end

    def Function_56_8FF5(): pass

    label("Function_56_8FF5")

    Sound(929, 0, 50, 0)
    Sleep(500)
    Sound(940, 0, 100, 0)
    Sleep(200)
    Sound(936, 0, 100, 0)
    Sound(1029, 0, 100, 0)
    Return()

    # Function_56_8FF5 end

    def Function_57_9014(): pass

    label("Function_57_9014")

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

    def lambda_9455():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9455)
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
        "#00310F#6PKh...what the heck!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PKeA...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PThis is sadness...\x01",
            "...And despair...!?\x02",
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
        "#00007F#6P#4SKeA, hang in there!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#00007F#6P#4SIf you can hear me, answer me!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10803F#6P#30WKh, impossible...\x02\x03",
            "#10810F...At this rate...it is going to be like with\x01",
            "the Sept-Terrion of Mirage back then...?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9775")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_974D")
    OP_FC(0x6)
    Jump("loc_9750")

    label("loc_974D")

    OP_FC(0xC)

    label("loc_9750")


    ChrTalk(
        0x109,
        "#10107F#13PY-You mean...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_981C")

    label("loc_9775")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_979F")
    OP_FC(0x6)
    Jump("loc_97A2")

    label("loc_979F")

    OP_FC(0xC)

    label("loc_97A2")


    ChrTalk(
        0x106,
        "#10707F#13PY-You mean...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_981C")

    label("loc_97C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_981C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97F1")
    OP_FC(0x6)
    Jump("loc_97F4")

    label("loc_97F1")

    OP_FC(0xC)

    label("loc_97F4")


    ChrTalk(
        0x10A,
        "#00607F#13PDon't tell me that...!?\x02",
    )

    CloseMessageWindow()

    label("loc_981C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9846")
    OP_FC(0x6)
    Jump("loc_9849")

    label("loc_9846")

    OP_FC(0xC)

    label("loc_9849")


    ChrTalk(
        0x105,
        (
            "#10410F#13PWhen it untied the principle of causality\x01",
            "of its own existence and erased itself...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99A0")

    label("loc_98B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_992B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98DE")
    OP_FC(0x6)
    Jump("loc_98E1")

    label("loc_98DE")

    OP_FC(0xC)

    label("loc_98E1")


    ChrTalk(
        0x10A,
        (
            "#00610F#13PWhen it ended up erasing itself\x01",
            "with its own hands!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99A0")

    label("loc_992B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9955")
    OP_FC(0x6)
    Jump("loc_9958")

    label("loc_9955")

    OP_FC(0xC)

    label("loc_9958")


    ChrTalk(
        0x106,
        (
            "#10701F#13PWhen it ended up erasing itself\x01",
            "with its own hands...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99A0")


    ChrTalk(
        0x101,
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 61)
    OP_68(0, 2800, -6500, 2000)
    MoveCamera(330, 5, 0, 2000)
    OP_6E(700, 2000)
    Sleep(500)

    def lambda_99F2():

        label("loc_99F2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_99F2")

    QueueWorkItem2(0xA, 2, lambda_99F2)
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
        "#00105F#6P#NLloyd...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00207F#6P#NMr. Lloyd...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0xA, 0x2)

    ChrTalk(
        0xA,
        "#10805F#6PW-What are you...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6P#NWhat do you want to do!?\x02",
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
            "#00010F#5P#50W#25A...It's all right...\x01",
            "Wait there for me...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#00015F#5P#60W#25AThis child...I'll absolutely...\x02",
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
        "#00007F#5P#80W#28A...With my own hands, I'll... KeA──\x02",
    )

    CloseMessageWindow()
    FadeToDark(4000, 16777215, -1)

    def lambda_9D5A():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9D5A)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E06")

    ChrTalk(
        0x102,
        "#00107F#3409V#6P#4S#N#15A#30WLloooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F51")

    label("loc_9E06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E4B")

    ChrTalk(
        0x103,
        "#00207F#2696V#6P#4S#N#15A#30WMr. Lloyd──!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F51")

    label("loc_9E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E8B")

    ChrTalk(
        0x104,
        "#00307F#2776V#6P#4S#N#15A#30WLloooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F51")

    label("loc_9E8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ECC")

    ChrTalk(
        0x105,
        "#10407F#2925V#6P#4S#N#15A#30WLloyd──!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F51")

    label("loc_9ECC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F11")

    ChrTalk(
        0x109,
        "#10107F#3531V#6P#4S#N#15A#30WMr. Llooooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F51")

    label("loc_9F11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F51")

    ChrTalk(
        0x106,
        "#10707F#3264V#6P#4S#N#15A#30WMr. Lloyd──!\x02",
    )

    CloseMessageWindow()

    label("loc_9F51")

    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9013", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_57_9014 end

    def Function_58_9F6B(): pass

    label("Function_58_9F6B")

    OP_74(0x1, 0xA)
    OP_71(0x1, 0x51, 0x64, 0x0, 0x20)
    Return()

    # Function_58_9F6B end

    def Function_59_9F7C(): pass

    label("Function_59_9F7C")

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

    # Function_59_9F7C end

    def Function_60_9FB7(): pass

    label("Function_60_9FB7")

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

    def lambda_A039():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A039)

    def lambda_A053():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A053)
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

    # Function_60_9FB7 end

    def Function_61_A0DA(): pass

    label("Function_61_A0DA")

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

    def lambda_A1A6():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A1A6)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)
    OP_9B(0x1, 0xFE, 0x0, 0x190, 0x3E8, 0x0)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)

    def lambda_A219():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A219)
    Sleep(250)
    SetChrSubChip(0xFE, 0x23)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x3)

    label("loc_A247")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A273")

    def lambda_A257():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A257)
    Sleep(400)
    Jump("loc_A247")

    label("loc_A273")

    Return()

    # Function_61_A0DA end

    def Function_62_A274(): pass

    label("Function_62_A274")

    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4100, -2210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_A2B4():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A2B4)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)

    def lambda_A2D4():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2D4)
    Sound(920, 0, 100, 0)
    Sound(1005, 0, 100, 0)
    Sleep(700)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_62_A274 end

    def Function_63_A2F9(): pass

    label("Function_63_A2F9")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_63_A2F9 end

    def Function_64_A308(): pass

    label("Function_64_A308")

    Sleep(100)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_A308 end

    def Function_65_A31A(): pass

    label("Function_65_A31A")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_A31A end

    def Function_66_A32C(): pass

    label("Function_66_A32C")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_66_A32C end

    def Function_67_A338(): pass

    label("Function_67_A338")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A358")
    Sound(540, 0, 50, 0)
    Jump("loc_A37D")

    label("loc_A358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A37D")
    Sound(531, 0, 50, 0)

    label("loc_A37D")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_A338 end

    def Function_68_A386(): pass

    label("Function_68_A386")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3A6")
    Sound(540, 0, 50, 0)
    Jump("loc_A3CB")

    label("loc_A3A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3CB")
    Sound(531, 0, 50, 0)

    label("loc_A3CB")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_68_A386 end

    def Function_69_A3D4(): pass

    label("Function_69_A3D4")

    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_69_A3D4 end

    def Function_70_A3F1(): pass

    label("Function_70_A3F1")

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

    # Function_70_A3F1 end

    def Function_71_A436(): pass

    label("Function_71_A436")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84D")
    Jump("loc_A8F7")

    label("loc_A84D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A870")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x103)
    OP_FD(0x103, 0x10)
    Jump("loc_A8F7")

    label("loc_A870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A893")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x104)
    OP_FD(0x104, 0x10)
    Jump("loc_A8F7")

    label("loc_A893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B6")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x105)
    OP_FD(0x105, 0x10)
    Jump("loc_A8F7")

    label("loc_A8B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8D9")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x109)
    OP_FD(0x109, 0x10)
    Jump("loc_A8F7")

    label("loc_A8D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8F7")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x106)
    OP_FD(0x106, 0x10)

    label("loc_A8F7")

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

    def lambda_AA23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 0, 0, 73)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AADC")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...aah......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd...Keddo...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#11P#30W#20AYou've come...back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AE99")

    label("loc_AADC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB70")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AOoh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#6P#30W#20ALloyd...KeA...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#11P#30W#20AYou have...come back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AE99")

    label("loc_AB70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC0D")

    ChrTalk(
        0x102,
        "#00116F#12P#30W#20AAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20AMr. Lloyd...KeA...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00315F#11P#30W#20AHa ha...\x01",
            "You've come...back...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AE99")

    label("loc_AC0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC36")
    OP_FC(0xC)
    Jump("loc_AC39")

    label("loc_AC36")

    OP_FC(0x6)

    label("loc_AC39")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...Mr. Lloyd...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AAnd Keddo too...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10411F#11P#30W#20AHu hu...you're back, eh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AE99")

    label("loc_ACEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADC7")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...aah......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD63")
    OP_FC(0xC)
    Jump("loc_AD66")

    label("loc_AD63")

    OP_FC(0x6)

    label("loc_AD66")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AAnd KeA too...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10116F#11P#30W#20AYou've come...back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AE99")

    label("loc_ADC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE99")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AOoh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE13")
    OP_FC(0xC)
    Jump("loc_AE16")

    label("loc_AE13")

    OP_FC(0x6)

    label("loc_AE16")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20ALloyd...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...And KeA too...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10716F#11P#30W#20AYou've come...back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AE99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEC3")
    OP_FC(0xC)
    Jump("loc_AEC6")

    label("loc_AEC3")

    OP_FC(0x6)

    label("loc_AEC6")


    ChrTalk(
        0x10A,
        (
            "#00604F#13P#30W#20AHonestly... That recklessness\x01",
            "would put your brother to shame...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AF22")

    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#40W*phew*......\x02\x03",
            "#30W#00000F──We're back, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#50W...Uuh...*sob*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFAB")
    OP_FC(0x5)
    Jump("loc_B041")

    label("loc_AFAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFDC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFD4")
    OP_FC(0xC)
    Jump("loc_AFD7")

    label("loc_AFD4")

    OP_FC(0x6)

    label("loc_AFD7")

    Jump("loc_B041")

    label("loc_AFDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B005")
    OP_FC(0xC)
    Jump("loc_B008")

    label("loc_B005")

    OP_FC(0x6)

    label("loc_B008")

    Jump("loc_B041")

    label("loc_B00D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B03E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B036")
    OP_FC(0xC)
    Jump("loc_B039")

    label("loc_B036")

    OP_FC(0x6)

    label("loc_B039")

    Jump("loc_B041")

    label("loc_B03E")

    OP_FC(0xB)

    label("loc_B041")

    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00114F#13PLloyd...thank goodness!\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0CF")
    OP_FC(0xB)
    Jump("loc_B0D2")

    label("loc_B0CF")

    OP_FC(0x5)

    label("loc_B0D2")

    OP_6F(0x79)
    SetCameraDistance(10000, 30000)

    ChrTalk(
        0x103,
        (
            "#00214F#13PKeA...\x01",
            "Are you all right...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PIt looks like she's returned\x01",
            "to her original form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, it's all right now.\x02\x03",
            "#00000F...Come on, KeA.\x01",
            "You have something to tell everyone, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#40W*sigh*...yes...\x02",
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
            "#05821F#5P#40WI'm...sorry...\x02\x03",
            "...For having always made you worry...\x01",
            "For doing things on my own...\x02\x03",
            "#05818FAnd also...\x01",
            "...Thank you for coming for me...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B303")
    OP_FC(0x5)
    Jump("loc_B399")

    label("loc_B303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B334")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B32C")
    OP_FC(0xC)
    Jump("loc_B32F")

    label("loc_B32C")

    OP_FC(0x6)

    label("loc_B32F")

    Jump("loc_B399")

    label("loc_B334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B365")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B35D")
    OP_FC(0xC)
    Jump("loc_B360")

    label("loc_B35D")

    OP_FC(0x6)

    label("loc_B360")

    Jump("loc_B399")

    label("loc_B365")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B396")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B38E")
    OP_FC(0xC)
    Jump("loc_B391")

    label("loc_B38E")

    OP_FC(0x6)

    label("loc_B391")

    Jump("loc_B399")

    label("loc_B396")

    OP_FC(0xB)

    label("loc_B399")


    ChrTalk(
        0x102,
        "#00116F#13PKeA...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3C7")
    OP_FC(0xB)
    Jump("loc_B3CA")

    label("loc_B3C7")

    OP_FC(0x5)

    label("loc_B3CA")


    ChrTalk(
        0x103,
        "#00204F#13PNo need for thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PHa ha...well, be prepared for a\x01",
            "spankin' when we get home, 'k?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 76)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#05817F#5P#50W...Yes...\x01",
            "*sob*...uuuuh....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11POh, come on...\x01",
            "There's nothing to cry for anymore, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B507")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4EC")
    OP_FC(0xC)
    Jump("loc_B4EF")

    label("loc_B4EC")

    OP_FC(0x6)

    label("loc_B4EF")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph...\x02",
    )

    CloseMessageWindow()

    label("loc_B507")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B56A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B52E")
    OP_FC(0xB)
    Jump("loc_B54B")

    label("loc_B52E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B548")
    OP_FC(0xC)
    Jump("loc_B54B")

    label("loc_B548")

    OP_FC(0x6)

    label("loc_B54B")


    ChrTalk(
        0x105,
        "#10404F#13PHu hu, oh boy.\x02",
    )

    CloseMessageWindow()

    label("loc_B56A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5D5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B591")
    OP_FC(0xB)
    Jump("loc_B5AE")

    label("loc_B591")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5AB")
    OP_FC(0xC)
    Jump("loc_B5AE")

    label("loc_B5AB")

    OP_FC(0x6)

    label("loc_B5AE")


    ChrTalk(
        0x109,
        "#10106F#13P...*sob*...I'm glad...\x02",
    )

    CloseMessageWindow()

    label("loc_B5D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B643")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5FC")
    OP_FC(0xB)
    Jump("loc_B619")

    label("loc_B5FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B616")
    OP_FC(0xC)
    Jump("loc_B619")

    label("loc_B616")

    OP_FC(0x6)

    label("loc_B619")


    ChrTalk(
        0x106,
        "#10710F#13P(...These are...bonds...)\x02",
    )

    CloseMessageWindow()

    label("loc_B643")

    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#10803F#3799V#5P#N#40W#35A──Honestly.\x01",
            "What a boring ending.\x02",
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

    def lambda_B770():
        OP_93(0xFE, 0xAF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B770)
    Sleep(50)

    def lambda_B780():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B780)
    Sleep(50)

    def lambda_B790():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B790)
    Sleep(50)

    def lambda_B7A0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B7A0)
    Sleep(50)

    def lambda_B7B0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B7B0)
    Sleep(50)

    def lambda_B7C0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B7C0)
    Sleep(50)

    def lambda_B7D0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B7D0)
    Sleep(300)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)

    def lambda_B7F2():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B7F2)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    def lambda_B809():
        OP_96(0xFE, 0xFFFFFE8E, 0x3B6, 0xFFFFCCFC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B809)

    ChrTalk(
        0x101,
        "#00001F#6P#N...Miss Mariabell.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#NBell...\x01",
            "...Do you still want to fight?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30WThere is nothing I can do. The "Sept-Terrion"\x01",
            "powers have disappeared from Miss KeA .\x02\x03",
            "Along with the 1000 years deep-rooted\x01",
            "delusion of the Crois clan.\x02\x03",
            "#10801FIt is really a...\x01",
            "Disappointment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05816F#6P#N#30W...Bell...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00206F#6P#NEven the Cult nightmare...\x01",
            "Is it really over?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30WYes. However, in the future\x01",
            "even more disasters will\x01",
            "await for Crossbell.\x02\x03",
            "Erebonia, especially...\x01",
            "Whatever faction wins in the civil war,\x01",
            "will very likely come to invade us.\x02\x03",
            "#10801FWhen that happens, Calvard for sure\x01",
            "will dispatch the army to oppose them too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N...Yes...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00301F#12P#NI know...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB59")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB33")
    OP_FC(0xFFF4)
    Jump("loc_BB36")

    label("loc_BB33")

    OP_FC(0xFFFA)

    label("loc_BB36")


    ChrTalk(
        0x109,
        "#10108F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_BBA4")

    label("loc_BB59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBA4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB83")
    OP_FC(0xFFF4)
    Jump("loc_BB86")

    label("loc_BB83")

    OP_FC(0xFFFA)

    label("loc_BB86")


    ChrTalk(
        0x10A,
        "#00608F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BBA4")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WHowever, after losing the "Sept-Terrion",\x01",
            "you have no means to hold them back.\x02\x03",
            "#10800FYou understand that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NEven so, we...\x01",
            "We made this decision with KeA.\x02\x03",
            "#00003FGetting over these barriers together,\x01",
            "in order to grasp the light of tomorrow...\x02\x03",
            "#00000FThat's why── we have no regrets.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00202F#6P#N...Yes...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F#12P#N*giggle*, we're going to get\x01",
            "busy even more than we had.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00304F#12P#NStill, even havin' been able to come this far was\x01",
            "because we went through all sorta hardships.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE42")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDF4")
    OP_FC(0xFFF4)
    Jump("loc_BDF7")

    label("loc_BDF4")

    OP_FC(0xFFFA)

    label("loc_BDF7")


    ChrTalk(
        0x109,
        (
            "#10100F#13PWe'll overcome those together,\x01",
            "facing forward in earnest!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BE42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE6C")
    OP_FC(0xFFF4)
    Jump("loc_BE6F")

    label("loc_BE6C")

    OP_FC(0xFFFA)

    label("loc_BE6F")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PPolice worth too is going to be\x01",
            "questioned more than ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BEBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFC3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEE5")
    OP_FC(0xFFF4)
    Jump("loc_BEE8")

    label("loc_BEE5")

    OP_FC(0xFFFA)

    label("loc_BEE8")


    ChrTalk(
        0x105,
        (
            "#10404F#13PHu hu, I can't say anything\x01",
            "careless from my position, but...\x02\x03",
            "#10402FIt seems interference from the Congregation for\x01",
            "Divine Worship will disappear, and even the\x01",
            "Church should be able to help a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BFC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C02F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFED")
    OP_FC(0xFFF4)
    Jump("loc_BFF0")

    label("loc_BFED")

    OP_FC(0xFFFA)

    label("loc_BFF0")


    ChrTalk(
        0x106,
        (
            "#10704F#13PI will help too...\x01",
            "To the best of my ability.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_C02F")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WHu hu... \x01",
            "I cannot handle this any longer.\x02\x03",
            "#10802FWell, if that is the case,\x01",
            "do your best, all right?\x02",
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
        "#00105F#12P#NBell...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#6P#NMiss Mariabell...!\x02",
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
            "#10804F#5P──Oh, about Mr. Grimwood. I only put him\x01",
            "in a temporary state of apparent death.\x02\x03",
            "#10800FIf treated properly, he will live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(1590, 2400, -10140, 1500)
    MoveCamera(35, 15, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14390, 1500)

    def lambda_C2D7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C2D7)
    Sleep(50)

    def lambda_C2E7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C2E7)
    Sleep(50)

    def lambda_C2F7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C2F7)
    Sleep(50)

    def lambda_C307():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C307)
    Sleep(50)

    def lambda_C317():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C317)
    Sleep(50)

    def lambda_C327():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_C327)
    Sleep(50)

    def lambda_C337():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C337)
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

    def lambda_C3B8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C3B8)
    Sleep(50)

    def lambda_C3C8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3C8)
    Sleep(50)

    def lambda_C3D8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C3D8)
    Sleep(50)

    def lambda_C3E8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C3E8)
    Sleep(50)

    def lambda_C3F8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C3F8)
    Sleep(50)

    def lambda_C408():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_C408)
    Sleep(50)

    def lambda_C418():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C418)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0xA,
        (
            "#10804F#5PAlso, by losing the Sept-Terrion power,\x01",
            "even the "huge tree" will soon disappear.\x02\x03",
            "#10800FIt will be in a few hours...\x01",
            "See that you flee quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P#NYou...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#6P#N...Why...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10802F#5PHu hu, no matter the circumstances,\x01",
            "I had intended to leave Crossbell.\x02\x03",
            "#10804FBecause I desired to serve the\x01",
            "Grandmaster of "Ouroboros" in\x01",
            "stead of a missing Anguis.\x02",
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
        "#00007F#6P#NWha──\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NAnguis...\x01",
            "The "Society" highest executives...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12P#NBell...you...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10802F#5PUhuhu...\x01",
            "Elie, do not do that face.\x02\x03",
            "#10804FWith the continent having become like this,\x01",
            "there will be other chances to meet again.\x02\x03",
            "#10800FUntil then, I will firmly watch,\x01",
            "from a distant land...\x02\x03",
            "Your vain struggle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N......Bell......\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        "#05808F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10806F#5PAlso, about my father, please\x01",
            "spare him the capital punishment.\x02\x03",
            "#10800FAfter all, he will be a little useful\x01",
            "to you to rebuild Crossbell.\x02",
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
        "#10809F#3800V#5P#40W#30AThen, everyone── have a nice day.\x02",
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
        "#00008F#5P#30W............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA88")
    OP_FC(0x5)
    Jump("loc_CA8B")

    label("loc_CA88")

    OP_FC(0xB)

    label("loc_CA8B")


    ChrTalk(
        0x102,
        (
            "#00106F#13P#30W......Bell......\x01",
            "Selfish...until the very end...\x02",
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

    def lambda_CB2D():

        label("loc_CB2D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB2D")

    QueueWorkItem2(0x9, 2, lambda_CB2D)
    Sleep(300)

    def lambda_CB42():

        label("loc_CB42")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB42")

    QueueWorkItem2(0x102, 2, lambda_CB42)
    Sleep(50)

    def lambda_CB57():

        label("loc_CB57")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB57")

    QueueWorkItem2(0x103, 2, lambda_CB57)
    Sleep(50)

    def lambda_CB6C():

        label("loc_CB6C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB6C")

    QueueWorkItem2(0x104, 2, lambda_CB6C)
    Sleep(50)

    def lambda_CB81():

        label("loc_CB81")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB81")

    QueueWorkItem2(0xF4, 2, lambda_CB81)
    Sleep(50)

    def lambda_CB96():

        label("loc_CB96")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_CB96")

    QueueWorkItem2(0xF5, 2, lambda_CB96)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC2B")
    BeginChrThread(0x102, 0, 0, 84)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CDEF")

    label("loc_CC2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC63")
    BeginChrThread(0x102, 0, 0, 85)
    BeginChrThread(0x103, 0, 0, 84)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CDEF")

    label("loc_CC63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC9B")
    BeginChrThread(0x102, 0, 0, 86)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 84)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CDEF")

    label("loc_CC9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD0E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCE5")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CD09")

    label("loc_CCE5")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CD09")

    Jump("loc_CDEF")

    label("loc_CD0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD81")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD58")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CD7C")

    label("loc_CD58")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CD7C")

    Jump("loc_CDEF")

    label("loc_CD81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDEF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDCB")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CDEF")

    label("loc_CDCB")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CDEF")

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
            "#00004F#5P#30W...Yes.\x01",
            "The wounds are really not fatal.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF29")

    def lambda_CECC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CECC)

    def lambda_CED9():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CED9)
    Sleep(50)

    def lambda_CEE9():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CEE9)
    Sleep(50)

    def lambda_CEF9():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CEF9)
    Sleep(50)

    def lambda_CF09():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CF09)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D2B5")

    label("loc_CF29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF9A")

    def lambda_CF3D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF3D)

    def lambda_CF4A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF4A)
    Sleep(50)

    def lambda_CF5A():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CF5A)
    Sleep(50)

    def lambda_CF6A():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CF6A)
    Sleep(50)

    def lambda_CF7A():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CF7A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D2B5")

    label("loc_CF9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D00B")

    def lambda_CFAE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CFAE)

    def lambda_CFBB():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CFBB)
    Sleep(50)

    def lambda_CFCB():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CFCB)
    Sleep(50)

    def lambda_CFDB():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CFDB)
    Sleep(50)

    def lambda_CFEB():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CFEB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D2B5")

    label("loc_D00B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D08E")

    def lambda_D031():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_D031)

    def lambda_D03E():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D03E)
    Sleep(50)

    def lambda_D04E():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D04E)
    Sleep(50)

    def lambda_D05E():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D05E)
    Sleep(50)

    def lambda_D06E():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_D06E)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D0EB")

    label("loc_D08E")


    def lambda_D093():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_D093)

    def lambda_D0A0():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D0A0)
    Sleep(50)

    def lambda_D0B0():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D0B0)
    Sleep(50)

    def lambda_D0C0():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D0C0)
    Sleep(50)

    def lambda_D0D0():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_D0D0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_D0EB")

    Jump("loc_D2B5")

    label("loc_D0F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D173")

    def lambda_D116():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_D116)

    def lambda_D123():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D123)
    Sleep(50)

    def lambda_D133():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D133)
    Sleep(50)

    def lambda_D143():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D143)
    Sleep(50)

    def lambda_D153():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_D153)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D1D0")

    label("loc_D173")


    def lambda_D178():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_D178)

    def lambda_D185():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D185)
    Sleep(50)

    def lambda_D195():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D195)
    Sleep(50)

    def lambda_D1A5():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D1A5)
    Sleep(50)

    def lambda_D1B5():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_D1B5)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_D1D0")

    Jump("loc_D2B5")

    label("loc_D1D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D258")

    def lambda_D1FB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_D1FB)

    def lambda_D208():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D208)
    Sleep(50)

    def lambda_D218():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D218)
    Sleep(50)

    def lambda_D228():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D228)
    Sleep(50)

    def lambda_D238():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_D238)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D2B5")

    label("loc_D258")


    def lambda_D25D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_D25D)

    def lambda_D26A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D26A)
    Sleep(50)

    def lambda_D27A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D27A)
    Sleep(50)

    def lambda_D28A():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D28A)
    Sleep(50)

    def lambda_D29A():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_D29A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_D2B5")


    ChrTalk(
        0x101,
        (
            "#00000F#11PEveryone, let's divide the work among us\x01",
            "and carry Lawyer Ian to the Merkabah.\x02\x03",
            "Also, we need to nurse Mr. Arios\x01",
            "and the others and carry them too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D383")
    OP_FC(0xC)
    Jump("loc_D386")

    label("loc_D383")

    OP_FC(0x6)

    label("loc_D386")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PBecause it seems that the "huge tree"\x01",
            "is going to collapse in a few hours,\x01",
            "we need to hurry up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D56C")

    label("loc_D3FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D4B6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D422")
    OP_FC(0x5)
    Jump("loc_D43F")

    label("loc_D422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D43C")
    OP_FC(0xC)
    Jump("loc_D43F")

    label("loc_D43C")

    OP_FC(0x6)

    label("loc_D43F")


    ChrTalk(
        0x106,
        (
            "#10700F#13PBecause it appears that the "huge tree"\x01",
            "is going to collapse in a few hours,\x01",
            "we need to hurry up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D56C")

    label("loc_D4B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D56C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4DD")
    OP_FC(0x5)
    Jump("loc_D4FA")

    label("loc_D4DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D4F7")
    OP_FC(0xC)
    Jump("loc_D4FA")

    label("loc_D4F7")

    OP_FC(0x6)

    label("loc_D4FA")


    ChrTalk(
        0x109,
        (
            "#10100F#13PBecause it seems that the "huge tree"\x01",
            "is going to collapse in a few hours,\x01",
            "we need to make haste.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D56C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5FF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D593")
    OP_FC(0x5)
    Jump("loc_D5B0")

    label("loc_D593")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5AD")
    OP_FC(0xC)
    Jump("loc_D5B0")

    label("loc_D5AD")

    OP_FC(0x6)

    label("loc_D5B0")


    ChrTalk(
        0x105,
        (
            "#10404F#13PLet's contact Abbas and the others\x01",
            "and split up the work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D740")

    label("loc_D5FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6A1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D626")
    OP_FC(0x5)
    Jump("loc_D643")

    label("loc_D626")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D640")
    OP_FC(0xC)
    Jump("loc_D643")

    label("loc_D640")

    OP_FC(0x6)

    label("loc_D643")


    ChrTalk(
        0x109,
        (
            "#10104F#13PIt seems it would be better to contact\x01",
            "the Merkabah and divide the work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D740")

    label("loc_D6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D740")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C8")
    OP_FC(0x5)
    Jump("loc_D6E5")

    label("loc_D6C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6E2")
    OP_FC(0xC)
    Jump("loc_D6E5")

    label("loc_D6E2")

    OP_FC(0x6)

    label("loc_D6E5")


    ChrTalk(
        0x106,
        (
            "#10704F#13PIt appears it would be better to contact\x01",
            "the Merkabah and divide the work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D740")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D75A")
    OP_FC(0x5)
    Jump("loc_D75D")

    label("loc_D75A")

    OP_FC(0x6)

    label("loc_D75D")


    ChrTalk(
        0x103,
        (
            "#00206F#13PNevertheless...\x02\x03",
            "#00202FMiss Mariabell has been Miss\x01",
            "Mariabell until the very end, eh.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7DB")
    OP_FC(0x5)
    Jump("loc_D7DE")

    label("loc_D7DB")

    OP_FC(0xC)

    label("loc_D7DE")


    ChrTalk(
        0x104,
        (
            "#00306F#13PYeah. Although she did such things,\x01",
            "somehow I can't really hate her...\x02\x03",
            "#00302FCould that too be one of her natural virtues?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D882")
    OP_FC(0x6)
    Jump("loc_D92F")

    label("loc_D882")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D899")
    OP_FC(0xC)
    Jump("loc_D92F")

    label("loc_D899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8C2")
    OP_FC(0xC)
    Jump("loc_D8C5")

    label("loc_D8C2")

    OP_FC(0x6)

    label("loc_D8C5")

    Jump("loc_D92F")

    label("loc_D8CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8F3")
    OP_FC(0xC)
    Jump("loc_D8F6")

    label("loc_D8F3")

    OP_FC(0x6)

    label("loc_D8F6")

    Jump("loc_D92F")

    label("loc_D8FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D92C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D924")
    OP_FC(0xC)
    Jump("loc_D927")

    label("loc_D924")

    OP_FC(0x6)

    label("loc_D927")

    Jump("loc_D92F")

    label("loc_D92C")

    OP_FC(0x5)

    label("loc_D92F")


    ChrTalk(
        0x102,
        (
            "#00106F#13PI think that maybe Bell...\x01",
            "Is being completely honest to herself.\x02\x03",
            "#00103FOnce she thinks she wants to do something,\x01",
            "she tries to accomplish that with all means,\x01",
            "without a single hesitation...\x02\x03",
            "#00108FWithout caring at all even if she's alone...\x02\x03",
            "#00101FHowever...everyone is\x01",
            "not as strong as Bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah, that's exactly why man...\x01",
            "Need family and comrades...\x02\x03",
            "#00008FTo get over barriers, in order to grasp \x01",
            "the light of a still unknown tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB27")
    OP_FC(0x5)
    Jump("loc_DB2A")

    label("loc_DB27")

    OP_FC(0xC)

    label("loc_DB2A")


    ChrTalk(
        0x104,
        (
            "#00304F#13PWell, it seems the time when we'll be able \x01",
            "to see the light is still further away, but...\x02\x03",
            "#00300FEven so, I've got the feelin'\x01",
            "we'll get by, somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBEB")
    OP_FC(0x5)
    Jump("loc_DBEE")

    label("loc_DBEB")

    OP_FC(0x6)

    label("loc_DBEE")


    ChrTalk(
        0x103,
        "#00214F#13P...Yes...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE2A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC30")
    OP_FC(0x5)
    Jump("loc_DC4D")

    label("loc_DC30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC4A")
    OP_FC(0xC)
    Jump("loc_DC4D")

    label("loc_DC4A")

    OP_FC(0x6)

    label("loc_DC4D")


    ChrTalk(
        0x109,
        (
            "#10102F#13PJust with the people we have here\x01",
            "we were able to do this much!\x02\x03",
            "#10109FIf all the people in Crossbell unites,\x01",
            "we'll be able to do anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD61")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD11")
    OP_FC(0x5)
    Jump("loc_DD2E")

    label("loc_DD11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD2B")
    OP_FC(0xC)
    Jump("loc_DD2E")

    label("loc_DD2B")

    OP_FC(0x6)

    label("loc_DD2E")


    ChrTalk(
        0x105,
        "#10404F#13PHu hu, it could be indeed so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE25")

    label("loc_DD61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDD9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD88")
    OP_FC(0x5)
    Jump("loc_DDA5")

    label("loc_DD88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDA2")
    OP_FC(0xC)
    Jump("loc_DDA5")

    label("loc_DDA2")

    OP_FC(0x6)

    label("loc_DDA5")


    ChrTalk(
        0x106,
        "#10709F#13PUh uh...it could be really so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE25")

    label("loc_DDD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE25")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE03")
    OP_FC(0xC)
    Jump("loc_DE06")

    label("loc_DE03")

    OP_FC(0x6)

    label("loc_DE06")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph...indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_DE25")

    Jump("loc_E0F3")

    label("loc_DE2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFE1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE51")
    OP_FC(0x5)
    Jump("loc_DE6E")

    label("loc_DE51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE6B")
    OP_FC(0xC)
    Jump("loc_DE6E")

    label("loc_DE6B")

    OP_FC(0x6)

    label("loc_DE6E")


    ChrTalk(
        0x105,
        (
            "#10404F#13PWell, just with the people we have\x01",
            "here we were able to do this much.\x02\x03",
            "#10402FIf we join forces throughout Crossbell,\x01",
            "won't we be able to do it, somehow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF90")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3F")
    OP_FC(0x5)
    Jump("loc_DF5C")

    label("loc_DF3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF59")
    OP_FC(0xC)
    Jump("loc_DF5C")

    label("loc_DF59")

    OP_FC(0x6)

    label("loc_DF5C")


    ChrTalk(
        0x106,
        "#10709F#13PUh uh...it could be really so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFDC")

    label("loc_DF90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFDC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFBA")
    OP_FC(0xC)
    Jump("loc_DFBD")

    label("loc_DFBA")

    OP_FC(0x6)

    label("loc_DFBD")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph...indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_DFDC")

    Jump("loc_E0F3")

    label("loc_DFE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF8")
    OP_FC(0x5)
    Jump("loc_E015")

    label("loc_DFF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E012")
    OP_FC(0xC)
    Jump("loc_E015")

    label("loc_E012")

    OP_FC(0x6)

    label("loc_E015")


    ChrTalk(
        0x106,
        (
            "#10704F#13P...Just with the people who're here\x01",
            "we were able to do this much.\x02\x03",
            "#10702FIf we join forces throughout Crossbell,\x01",
            "I feel like we can do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0D1")
    OP_FC(0xC)
    Jump("loc_E0D4")

    label("loc_E0D1")

    OP_FC(0x6)

    label("loc_E0D4")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph...indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_E0F3")

    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 90)
    WaitChrThread(0x9, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#05821F#3655V#5P#40W#40AKeA too...\x01",
            "...KeA too will do her best...!\x02\x03",
            "#05819F#3656V#40ATo protect this precious place...\x01",
            "...Together with everyone!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1B7")
    OP_FC(0x6)
    Jump("loc_E264")

    label("loc_E1B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1CE")
    OP_FC(0xC)
    Jump("loc_E264")

    label("loc_E1CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1F7")
    OP_FC(0xC)
    Jump("loc_E1FA")

    label("loc_E1F7")

    OP_FC(0x6)

    label("loc_E1FA")

    Jump("loc_E264")

    label("loc_E1FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E230")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E228")
    OP_FC(0xC)
    Jump("loc_E22B")

    label("loc_E228")

    OP_FC(0x6)

    label("loc_E22B")

    Jump("loc_E264")

    label("loc_E230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E261")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E259")
    OP_FC(0xC)
    Jump("loc_E25C")

    label("loc_E259")

    OP_FC(0x6)

    label("loc_E25C")

    Jump("loc_E264")

    label("loc_E261")

    OP_FC(0x5)

    label("loc_E264")


    ChrTalk(
        0x102,
        "#00102F#3410V#13P#30W#25AKeA...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2A3")
    OP_FC(0x5)
    Jump("loc_E2A6")

    label("loc_E2A3")

    OP_FC(0x6)

    label("loc_E2A6")


    ChrTalk(
        0x103,
        "#00204F#2697V#13P#30W#25AWith you, we will have the strength of a thousand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E311")
    OP_FC(0x5)
    Jump("loc_E314")

    label("loc_E311")

    OP_FC(0xC)

    label("loc_E314")


    ChrTalk(
        0x104,
        "#00309F#2777V#13P#30W#25AHa ha, that's the spirit!\x02",
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
        "#00009F#3337V#11P#30AYeah, let's do our best together.\x02",
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
            "#00004F#3338V#11P#30W#30A──Special Support Section, withdraw.\x02\x03",
            "#3339V#11P#30W#45ALet's recover Mr. Arios and the others and break\x01",
            "away from the "huge tree" with the Merkabah.\x02",
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
        "#00000F#3340V#11P#30W#35ALet's go back, to our Crossbell...!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E71C")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "EXTRA Mode has been unlocked.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "You can access EXTRA Mode\x01",
            "from the Title Screen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_E71C")

    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　      - About the Clear Data Save -\x01",
            "Having a Clear Data and loading it from the Title Screen,\x01",
            "you can begin a new game cycle inheriting various things.",
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

    # Function_71_A436 end

    def Function_72_E810(): pass

    label("Function_72_E810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)), "loc_E856")
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
    Jump("Function_72_E810")

    label("loc_E856")

    Return()

    # Function_72_E810 end

    def Function_73_E857(): pass

    label("Function_73_E857")

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

    # Function_73_E857 end

    def Function_74_E8B5(): pass

    label("Function_74_E8B5")

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

    # Function_74_E8B5 end

    def Function_75_E8E0(): pass

    label("Function_75_E8E0")

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

    # Function_75_E8E0 end

    def Function_76_E90B(): pass

    label("Function_76_E90B")

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

    # Function_76_E90B end

    def Function_77_E92F(): pass

    label("Function_77_E92F")

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

    # Function_77_E92F end

    def Function_78_E983(): pass

    label("Function_78_E983")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E995")
    Sleep(50)

    label("loc_E995")

    OP_9B(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
    Return()

    # Function_78_E983 end

    def Function_79_E9A5(): pass

    label("Function_79_E9A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B7")
    Sleep(100)

    label("loc_E9B7")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_79_E9A5 end

    def Function_80_E9C7(): pass

    label("Function_80_E9C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9D9")
    Sleep(150)

    label("loc_E9D9")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_80_E9C7 end

    def Function_81_E9E9(): pass

    label("Function_81_E9E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA0D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA0D")
    Sleep(200)

    label("loc_EA0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA31")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA31")
    Sleep(200)

    label("loc_EA31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA55")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA55")
    Sleep(200)

    label("loc_EA55")

    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_81_E9E9 end

    def Function_82_EA65(): pass

    label("Function_82_EA65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA89")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA89")
    Sleep(250)

    label("loc_EA89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAAD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAAD")
    Sleep(250)

    label("loc_EAAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAD1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAD1")
    Sleep(250)

    label("loc_EAD1")

    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_82_EA65 end

    def Function_83_EAE1(): pass

    label("Function_83_EAE1")

    TurnDirection(0xFE, 0x8, 500)
    Sleep(450)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x1964, 0x7D0, 0x0)
    Return()

    # Function_83_EAE1 end

    def Function_84_EB28(): pass

    label("Function_84_EB28")

    Sleep(200)
    OP_96(0xFE, 0x1C5C, 0x3B6, 0xFFFFDD14, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_84_EB28 end

    def Function_85_EB47(): pass

    label("Function_85_EB47")

    Sleep(1100)
    OP_96(0xFE, 0x16A8, 0x406, 0xFFFFDC60, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_85_EB47 end

    def Function_86_EB66(): pass

    label("Function_86_EB66")

    Sleep(50)
    OP_96(0xFE, 0x1F04, 0x3B6, 0xFFFFD1D4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_86_EB66 end

    def Function_87_EB85(): pass

    label("Function_87_EB85")

    Sleep(350)
    OP_96(0xFE, 0x19C8, 0x3B6, 0xFFFFD210, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_87_EB85 end

    def Function_88_EBA4(): pass

    label("Function_88_EBA4")

    Sleep(1450)
    OP_96(0xFE, 0x1608, 0x3B6, 0xFFFFD670, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_88_EBA4 end

    def Function_89_EBC3(): pass

    label("Function_89_EBC3")

    Sleep(750)
    OP_9B(0x1, 0xFE, 0x0, 0x4E2, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1C52, 0x1388, 0x1)
    Sound(811, 0, 70, 0)
    Sound(898, 0, 50, 0)

    def lambda_EBF5():
        OP_A6(0xFE, 0x64, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EBF5)
    Sleep(50)

    def lambda_EC11():
        OP_A6(0xFE, 0x32, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EC11)
    Sleep(450)
    OP_9B(0x1, 0xFE, 0x109, 0x96, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_89_EBC3 end

    def Function_90_EC3F(): pass

    label("Function_90_EC3F")

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

    # Function_90_EC3F end

    def Function_91_EC84(): pass

    label("Function_91_EC84")

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

    # Function_91_EC84 end

    def Function_92_ED0E(): pass

    label("Function_92_ED0E")

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

    # Function_92_ED0E end

    def Function_93_ED86(): pass

    label("Function_93_ED86")

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

    # Function_93_ED86 end

    def Function_94_EDAA(): pass

    label("Function_94_EDAA")

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

    # Function_94_EDAA end

    def Function_95_EDCE(): pass

    label("Function_95_EDCE")

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

    # Function_95_EDCE end

    def Function_96_EDF2(): pass

    label("Function_96_EDF2")

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

    # Function_96_EDF2 end

    def Function_97_EE1C(): pass

    label("Function_97_EE1C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_EE3E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EE3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_EE56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EE56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_EE6E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EE6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE91")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EE91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEB4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EEB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EED7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEF5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EEF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF13")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EF13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF31")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EF31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EF5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF83")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFA7")

    label("loc_EF83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFA7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EFA7")

    Return()

    # Function_97_EE1C end

    SaveToFile()

Try(main)
