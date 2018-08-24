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
        "Function_7_6300",         # 07, 7
        "Function_8_636A",         # 08, 8
        "Function_9_63D4",         # 09, 9
        "Function_10_643E",        # 0A, 10
        "Function_11_64A8",        # 0B, 11
        "Function_12_6512",        # 0C, 12
        "Function_13_657C",        # 0D, 13
        "Function_14_6598",        # 0E, 14
        "Function_15_65B7",        # 0F, 15
        "Function_16_65D6",        # 10, 16
        "Function_17_65F5",        # 11, 17
        "Function_18_6614",        # 12, 18
        "Function_19_6633",        # 13, 19
        "Function_20_6645",        # 14, 20
        "Function_21_6654",        # 15, 21
        "Function_22_6666",        # 16, 22
        "Function_23_6678",        # 17, 23
        "Function_24_6684",        # 18, 24
        "Function_25_66D2",        # 19, 25
        "Function_26_6720",        # 1A, 26
        "Function_27_6756",        # 1B, 27
        "Function_28_6793",        # 1C, 28
        "Function_29_67E5",        # 1D, 29
        "Function_30_6905",        # 1E, 30
        "Function_31_6A54",        # 1F, 31
        "Function_32_6AC9",        # 20, 32
        "Function_33_6AE5",        # 21, 33
        "Function_34_6AFA",        # 22, 34
        "Function_35_6B09",        # 23, 35
        "Function_36_6B74",        # 24, 36
        "Function_37_6B8A",        # 25, 37
        "Function_38_6BA0",        # 26, 38
        "Function_39_6BB6",        # 27, 39
        "Function_40_6BCC",        # 28, 40
        "Function_41_6BE2",        # 29, 41
        "Function_42_6BFF",        # 2A, 42
        "Function_43_6C1C",        # 2B, 43
        "Function_44_6C2B",        # 2C, 44
        "Function_45_6C3A",        # 2D, 45
        "Function_46_6C87",        # 2E, 46
        "Function_47_8C6F",        # 2F, 47
        "Function_48_8CBE",        # 30, 48
        "Function_49_8CE8",        # 31, 49
        "Function_50_8CEF",        # 32, 50
        "Function_51_8D0B",        # 33, 51
        "Function_52_8D89",        # 34, 52
        "Function_53_8DAB",        # 35, 53
        "Function_54_8DB9",        # 36, 54
        "Function_55_8DD3",        # 37, 55
        "Function_56_8DF0",        # 38, 56
        "Function_57_8E0F",        # 39, 57
        "Function_58_9D43",        # 3A, 58
        "Function_59_9D54",        # 3B, 59
        "Function_60_9D8F",        # 3C, 60
        "Function_61_9EB2",        # 3D, 61
        "Function_62_A04C",        # 3E, 62
        "Function_63_A0D1",        # 3F, 63
        "Function_64_A0E0",        # 40, 64
        "Function_65_A0F2",        # 41, 65
        "Function_66_A104",        # 42, 66
        "Function_67_A110",        # 43, 67
        "Function_68_A15E",        # 44, 68
        "Function_69_A1AC",        # 45, 69
        "Function_70_A1C9",        # 46, 70
        "Function_71_A20E",        # 47, 71
        "Function_72_E4F0",        # 48, 72
        "Function_73_E537",        # 49, 73
        "Function_74_E595",        # 4A, 74
        "Function_75_E5C0",        # 4B, 75
        "Function_76_E5EB",        # 4C, 76
        "Function_77_E60F",        # 4D, 77
        "Function_78_E663",        # 4E, 78
        "Function_79_E685",        # 4F, 79
        "Function_80_E6A7",        # 50, 80
        "Function_81_E6C9",        # 51, 81
        "Function_82_E745",        # 52, 82
        "Function_83_E7C1",        # 53, 83
        "Function_84_E808",        # 54, 84
        "Function_85_E827",        # 55, 85
        "Function_86_E846",        # 56, 86
        "Function_87_E865",        # 57, 87
        "Function_88_E884",        # 58, 88
        "Function_89_E8A3",        # 59, 89
        "Function_90_E91F",        # 5A, 90
        "Function_91_E964",        # 5B, 91
        "Function_92_E9EE",        # 5C, 92
        "Function_93_EA66",        # 5D, 93
        "Function_94_EA8A",        # 5E, 94
        "Function_95_EAAE",        # 5F, 95
        "Function_96_EAD2",        # 60, 96
        "Function_97_EAFC",        # 61, 97
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
        "#40W─So you've come.\x02",
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
            "#3789V#40W#30AUhuhu... Welcome.\x02\x03",
            "#3790V#40ATo the farthest reaches of the\x01",
            "world, the core of causality\x01",
            "itself.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FA1")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBA")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie... ...Tio...\x01",
            "Randy...\x02\x03",
            "#3637V#20ANoｱl and Wazy too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_F9C")

    label("loc_EBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2D")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie...\x01",
            "...Tio... Randy...\x02\x03",
            "#3638V#20ANoｱl and Rixia too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_F9C")

    label("loc_F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F9C")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie...\x01",
            "...Tio... Randy...\x02\x03",
            "#3639V#20ANoｱl and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_F9C")

    Jump("loc_10F8")

    label("loc_FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1098")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1024")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie...\x01",
            "...Tio... Randy...\x02\x03",
            "#3640V#20AWazy and Rixia too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Jump("loc_1093")

    label("loc_1024")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1093")

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie...\x01",
            "...Tio... Randy...\x02\x03",
            "#3641V#20AWazy and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_1093")

    Jump("loc_10F8")

    label("loc_1098")


    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3636V#50W#50ALloyd... Elie...\x01",
            "...Tio... Randy...\x02\x03",
            "#3642V#20ARixia and Dudley too...\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    label("loc_10F8")

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
        "#00007F#3330V#5P#N#30W#15AKeA!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 230, -1, -1)

    ChrTalk(
        0x103,
        (
            "#00214F#2694V#11P#N#30W#25AThank goodness... You're\x01",
            "safe...\x02",
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
            "#00108F#3407V#11P#N#30W#26AHonestly! You always\x01",
            "make us worry!\x02",
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
            "#3644V#50AKeA...#400W...#50W always\x01",
            "had something... that she\x01",
            "couldn't tell you all...\x02",
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
            "#12313F#3645V#5P#40A#50W...I'm sorry for...#400W...\x01",
            "#50W...remaining silent and deceiving you...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5P#NThere's no need to\x01",
            "apologize! You have no\x01",
            "obligation to us!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#11P#NTo us, the fact that\x01",
            "you're safe is enough!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#5P#NAnd it's only natural\x01",
            "for kids to keep secrets\x01",
            "from their parents!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00103F#11P#NYou seduced KeA with\x01",
            "something so ordinary?\x02",
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
            "#00107F#11PBell, Lawyer Ian! This\x01",
            "is your doing, isn't\x01",
            "it!?\x02",
        )
    )

    Sleep(200)

    def lambda_1526():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1526)
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
            "#10809F#5PUhuhu... How scary.\x02\x03",
            "#10800F#5PHowever, we hold KeA's\x01",
            "will in the highest\x01",
            "regard.\x02\x03",
            "#10811FIsn't that right, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#6P#N#30W......(*nods*)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00010F#11PGuh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_169A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1659")
    OP_FC(0xB)
    Jump("loc_165C")

    label("loc_1659")

    OP_FC(0xB)

    label("loc_165C")


    ChrTalk(
        0x109,
        (
            "#10101F#13PIt's not what you say,\x01",
            "it's how you say it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C4")
    OP_FC(0xB)
    Jump("loc_16C7")

    label("loc_16C4")

    OP_FC(0xB)

    label("loc_16C7")


    ChrTalk(
        0x106,
        "#10701F#13P...Hypocrite.\x02",
    )

    CloseMessageWindow()

    label("loc_16E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1753")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_170F")
    OP_FC(0xB)
    Jump("loc_1712")

    label("loc_170F")

    OP_FC(0xB)

    label("loc_1712")


    ChrTalk(
        0x105,
        (
            "#10406F#13POh man. You really have\x01",
            "no shame at all, do you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1753")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_177D")
    OP_FC(0xB)
    Jump("loc_1780")

    label("loc_177D")

    OP_FC(0xB)

    label("loc_1780")


    ChrTalk(
        0x10A,
        "#00601F#13P............\x02",
    )

    CloseMessageWindow()

    label("loc_179D")


    ChrTalk(
        0x104,
        (
            "#00301F#11P...Anyway, first come\x01",
            "back with us. Then we'll\x01",
            "talk at leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#11PRight. A family council.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12309F#6P#N#40WEhehe... *chuckle*...\x01",
            "...Thank you,\x01",
            "everyone...\x02\x03",
            "#12302FBut KeA... can't move\x01",
            "from this place...\x02\x03",
            "...So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PKeA... Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P...There's something\x01",
            "right? Related to your\x01",
            "power as a Sept-Terrion.\x02",
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
            "#10804F#6PUhuhu, KeA. Why don't\x01",
            "you tell them?\x02\x03",
            "#10811FThat you are doing all\x01",
            "of this for Lloyd and\x01",
            "the others.\x02",
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
            "#10800F#5PUnlike the former Sept-Terrion of Mirage, KeA,\x01",
            "the Sept-Terrion of Zero, possesses the powers\x01",
            "of Time and Space as well.\x02\x03",
            "#10804FWhen the power of Mirage, which interferes with\x01",
            "perception of cause and effect, unites with the\x01",
            "powers to tamper with space and time...\x02\x03",
            "#10811FKeA obtained the "power to create worlds".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#NT-The power to create\x01",
            "worlds...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CBE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C99")
    OP_FC(0xFFFA)
    Jump("loc_1C9C")

    label("loc_1C99")

    OP_FC(0xFFF4)

    label("loc_1C9C")


    ChrTalk(
        0x109,
        "#10111F#13PT-That's...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1D06")

    label("loc_1CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CE8")
    OP_FC(0xFFFA)
    Jump("loc_1CEB")

    label("loc_1CE8")

    OP_FC(0xFFF4)

    label("loc_1CEB")


    ChrTalk(
        0x106,
        "#10712F#13PThat's...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1D06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D30")
    OP_FC(0xFFFA)
    Jump("loc_1D33")

    label("loc_1D30")

    OP_FC(0xFFF4)

    label("loc_1D33")


    ChrTalk(
        0x105,
        (
            "#10401F#13PThere you go throwing\x01",
            "strange words at us\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1D77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DCB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DA1")
    OP_FC(0xFFFA)
    Jump("loc_1DA4")

    label("loc_1DA1")

    OP_FC(0xFFF4)

    label("loc_1DA4")


    ChrTalk(
        0x10A,
        "#00601F#13PWhat could that mean?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1DCB")

    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02203F#11PThis very ability could be said to\x01",
            "be the main goal of the "Azure-Zero\x01",
            "Project"...\x02\x03",
            "#02201F"To create worlds"─ In other words,\x01",
            "it's the power to manipulate\x01",
            "casuality, rearranging the world.\x02",
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
        (
            "#00101F#12P#NR-Rearrange the\x01",
            "world...?\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N#30W...The network of causality\x01",
            "that everything in the world\x01",
            "possesses...\x02\x03",
            "#00201FIs it the ability to\x01",
            "manipulate and alter its\x01",
            "past, present and future...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhuhu, that is Miss Tio for you. You\x01",
            "catch on quickly.\x02\x03",
            "#10800FCorrect, it is something akin to the\x01",
            "authority an orbal net admin with\x01",
            "the highest privileges can exert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02201F#11PChanging the reality that has produced\x01",
            "conflict, rearranging it into a more\x01",
            "peaceful one...\x02\x03",
            "#02203FFor instance, replacing the reality\x01",
            "where Crossbell is dependent on and made\x01",
            "fun of by the Empire and Republic...\x02\x03",
            "#02200FInto one where Crossbell reigns, as a\x01",
            ""suzerain state", on the major powers.\x01",
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
        "#00007F#6P#N...Wha...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2365")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2347")
    OP_FC(0xFFFA)
    Jump("loc_234A")

    label("loc_2347")

    OP_FC(0xFFF4)

    label("loc_234A")


    ChrTalk(
        0x109,
        "#10101F#13PU-Umm...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2365")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238F")
    OP_FC(0xFFFA)
    Jump("loc_2392")

    label("loc_238F")

    OP_FC(0xFFF4)

    label("loc_2392")


    ChrTalk(
        0x10A,
        "#00610F#13PT-That's crazy...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_23B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2404")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23DF")
    OP_FC(0xFFFA)
    Jump("loc_23E2")

    label("loc_23DF")

    OP_FC(0xFFF4)

    label("loc_23E2")


    ChrTalk(
        0x106,
        "#10706F#13P...Impossible...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2404")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2477")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_242E")
    OP_FC(0xFFFA)
    Jump("loc_2431")

    label("loc_242E")

    OP_FC(0xFFF4)

    label("loc_2431")


    ChrTalk(
        0x105,
        (
            "#10410F#13P...That should be\x01",
            "impossible even for the\x01",
            "Goddess...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2477")


    ChrTalk(
        0x104,
        (
            "#00307F#6P#NHey now, say what you\x01",
            "like, but isn't that a\x01",
            "little too nonsensical?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#N...As you might\x01",
            "imagine... it's too\x01",
            "sudden to believe.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5P*chuckle*... You've all\x01",
            "been saying some strange\x01",
            "things, haven't you?\x02\x03",
            "#10811F─Since you all have\x01",
            "already been saved by\x01",
            "her once before.\x02",
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
        "#00305F#6P#NHuh?\x02",
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
            "#00201F#12P#N...Don't tell me... What\x01",
            "we saw before...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00010F#6P#NWhen we infiltrated the\x01",
            "cult lodge some months\x01",
            "ago...!?\x02",
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
        "#00011F#6P#N#50W...Ah...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PHuhu. It seems you've\x01",
            ""remembered", Lloyd.\x02\x03",
            "#10804FReality alteration has been\x01",
            "already performed once, albeit\x01",
            "on an extremely small scale.\x02\x03",
            "#10811FThe reality of you all having\x01",
            "been killed by Joachim when he\x01",
            "went berserk was altered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N#30W...............\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#6P#N#30W...Are you... kiddin'\x01",
            "me...?\x02",
        )
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
            "#12306F#11P#30WThe first time... you guys\x01",
            "weren't so close with Estelle\x01",
            "and Joshua, or Renne either...\x02",
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
            "#12308F#11PThat being the case, you entered\x01",
            "with just the four of you... In the\x01",
            "end, that child's help never came...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 0, 0, 40)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0xA,
        (
            "#10800F#5PKeA, who "knew" that, allowed her\x01",
            "Sept-Terrion power to run wild and\x01",
            "interfere with causality in the past.\x02\x03",
            "#10804FThe result of that led to you solving\x01",
            "the Angel of Slaughter's problem...\x02\x03",
            "One thing led to another and the two\x01",
            "Liberl bracers showed up as your\x01",
            "helpers...\x02\x03",
            "#10811FAnd then─ In the scene where you were\x01",
            "killed originally, the Angel of\x01",
            "Slaughter came to save you.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F58")
    OP_FC(0xFFFA)
    Jump("loc_2F5B")

    label("loc_2F58")

    OP_FC(0xFFF4)

    label("loc_2F5B")


    ChrTalk(
        0x109,
        "#10110F#13PT-That's...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3012")

    label("loc_2F7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FA7")
    OP_FC(0xFFFA)
    Jump("loc_2FAA")

    label("loc_2FA7")

    OP_FC(0xFFF4)

    label("loc_2FAA")


    ChrTalk(
        0x106,
        "#10708F#13PThat's...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3012")

    label("loc_2FCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3012")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FF4")
    OP_FC(0xFFFA)
    Jump("loc_2FF7")

    label("loc_2FF4")

    OP_FC(0xFFF4)

    label("loc_2FF7")


    ChrTalk(
        0x10A,
        "#00610F#13PThat's...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3012")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3084")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_303C")
    OP_FC(0xFFFA)
    Jump("loc_303F")

    label("loc_303C")

    OP_FC(0xFFF4)

    label("loc_303F")


    ChrTalk(
        0x105,
        (
            "#10403F#13P...But... It doesn't\x01",
            "seem to be a total lie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_316D")

    label("loc_3084")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30AE")
    OP_FC(0xFFFA)
    Jump("loc_30B1")

    label("loc_30AE")

    OP_FC(0xFFF4)

    label("loc_30B1")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P...However... It doesn't\x01",
            "appear to be a total\x01",
            "lie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_316D")

    label("loc_30FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_316D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3126")
    OP_FC(0xFFFA)
    Jump("loc_3129")

    label("loc_3126")

    OP_FC(0xFFF4)

    label("loc_3129")


    ChrTalk(
        0x106,
        (
            "#10703F#13P...However... It doesn't\x01",
            "seem to be a total lie.\x02",
        )
    )

    OP_5A()
    OP_57(0x0)
    OP_5A()

    label("loc_316D")

    Sleep(300)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#5P#N#30W...............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10804F#5PUhuhu... As expected, you're shocked,\x01",
            "aren't you?\x02\x03",
            "#10800FHowever, as for the true meaning of\x01",
            "the "power to rearrange reality" that\x01",
            "the Sept-Terrion of Zero possesses─\x02\x03",
            "Avoiding your tragedy was only the\x01",
            "beginning.\x02",
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
            "#10804F#5PThis Azure Tree─\x02\x03",
            "It amplifies KeA's power. It is a divine\x01",
            "tree that can link with the world itself\x01",
            "through the septium veins...\x02\x03",
            "#10811F#5PTo say nothing of avoiding tragedies, it\x01",
            "should be possible to alter reality at\x01",
            "the level Mr. Grimwood mentioned earlier.\x02",
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
        (
            "#00201F#12P#NThat is this Huge Tree's\x01",
            "power...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N...Hey now... That's not\x01",
            "funny...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_349D")
    OP_FC(0xFFFA)
    Jump("loc_34A0")

    label("loc_349D")

    OP_FC(0xFFF4)

    label("loc_34A0")


    ChrTalk(
        0x105,
        (
            "#10408F#13P(...I see... The same as\x01",
            "the original Primal\x01",
            "Ground...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_34E9")


    ChrTalk(
        0xA,
        (
            "#10802F#5P#30WUhuhu... Wonderful, right?\x02\x03",
            "#10809FBecause we have such a\x01",
            "wonderful thing, we have\x01",
            "nothing to fear!\x02\x03",
            "We could bring happiness to\x01",
            "the entire world! No more\x01",
            "sorrows!\x02\x03",
            "Man would be free from all\x01",
            "anxieties and could pursue\x01",
            "only "the good"!\x02\x03",
            "#10811FWhat is no doubt alchemy's\x01",
            "greatest secret art─ The great\x01",
            "secret formula Ars Magna!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#6P#NBell... You...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#N...............\x02",
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
            "#00003F#6P#N─Lawyer Ian.\x02\x03",
            "#00013FAre you really fine with\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02201F#11P#30W...............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02211F#11P...In anything one does,\x01",
            "preparations are needed.\x02\x03",
            "Human history is one\x01",
            "that deals with all\x01",
            "sorts of risk...\x02\x03",
            "And KeA has the\x01",
            "wonderful power to\x01",
            "control it.\x02\x03",
            "That is an undeniable\x01",
            ""reality".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NEven if the result were to imprison\x01",
            "KeA in this place...?\x02\x03",
            "#00008FI heard that the previous Sept-Terrion\x01",
            "of Mirage grieved before long and\x01",
            "decided to erase its own existence.\x02\x03",
            "#00013FDo you really intend... to force such\x01",
            "a heavy responsibility on a single\x01",
            "little girl?\x02",
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
            "#12300F#5P#NLloyd, that's─\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10800F#5PUhuhu. That is why we're here, so that\x01",
            "doesn't happen.\x02\x03",
            "#10804FWe are not forcing the entire\x01",
            "responsibility for changing to world onto\x01",
            "KeA...\x02\x03",
            "Knowledgeable people like Mr. Grimwood\x01",
            "here are going to advise her on altering\x01",
            "the world into a "more correct direction".\x02\x03",
            "#10802FIsn't it a different story if we do it\x01",
            "like that?\x02",
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
            "#00107F#12P#NY-You will completely\x01",
            "deny a democratic\x01",
            "process...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P...Elie, you should be well aware of\x01",
            "the flaws of democracy.\x02\x03",
            "It is a system prone to fall into\x01",
            "mobocracy and where important\x01",
            "matters cannot be decided quickly...\x02\x03",
            "#02201FIsn't that a reality you can see not\x01",
            "just in Crossbell, but anywhere?\x02",
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
            "#02200F#11PAnd, it isn't the case that we\x01",
            "intend to present solely our own\x01",
            "views to KeA.\x02\x03",
            "#02203FI want to request the cooperation\x01",
            "of knowledgeable people such as\x01",
            "Chairman MacDowell as well.\x02\x03",
            "Dieter too could be useful again\x01",
            "from a management point of view.\x02\x03",
            "#02200FAlso─ I would like your\x01",
            "cooperation in our experiment as\x01",
            "well.\x02",
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
            "#02203F#11PTo open the path to a new era, the\x01",
            "views of young people are necessary.\x02\x03",
            "#02201FAnd if it is you all...\x02\x03",
            "If it is you all, who managed to reach\x01",
            "this place... I am sure, based on your\x01",
            "own experiences, you understand what\x01",
            "is needed for the next era.\x02\x03",
            "#02200FWhat do you say?─ What do you think of\x01",
            "this proposal?\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P#N#30W...T-That's...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#N#30WDamn... It's oddly\x01",
            "persuasive, but...\x02",
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
            "#00003FYou haven't answered my\x01",
            "question yet.\x02\x03",
            "#00001F#6P#NAre you─ Are you really\x01",
            "fine with that?\x02",
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
            "#00003F#6P#N#30WEverything has its own "dignity".\x02\x03",
            "Man, society, history too.\x02\x03",
            "#00008FEven if they're connected by mistakes\x01",
            "and results that produce tragedies...\x02\x03",
            "#00013FPretending that they never happened...\x01",
            "It's the same a violating the\x01",
            ""dignity" of the people concerned.\x02\x03",
            "#00006FFor instance, the dignity of people\x01",
            "who obtain strength after recovering\x01",
            "from a tragedy...\x02\x03",
            "#00002FYou understand that too, don't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W...............\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4375")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4312")
    OP_FC(0xFFFA)
    Jump("loc_4315")

    label("loc_4312")

    OP_FC(0xFFF4)

    label("loc_4315")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P#30WIndeed... Man isn't an\x01",
            "existence that only makes\x01",
            "correct decisions...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_447F")

    label("loc_4375")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_439F")
    OP_FC(0xFFFA)
    Jump("loc_43A2")

    label("loc_439F")

    OP_FC(0xFFF4)

    label("loc_43A2")


    ChrTalk(
        0x109,
        (
            "#10106F#13P#30WIndeed... Man is an\x01",
            "existence that, at\x01",
            "times, makes mistakes.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_447F")

    label("loc_43FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_447F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4424")
    OP_FC(0xFFFA)
    Jump("loc_4427")

    label("loc_4424")

    OP_FC(0xFFF4)

    label("loc_4427")


    ChrTalk(
        0x106,
        (
            "#10708F#13P#30W...Indeed... Man is an\x01",
            "existence that, at\x01",
            "times, makes mistakes...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_447F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4500")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44A9")
    OP_FC(0xFFFA)
    Jump("loc_44AC")

    label("loc_44A9")

    OP_FC(0xFFF4)

    label("loc_44AC")


    ChrTalk(
        0x105,
        (
            "#10401F#13P#30WHowever, if he forgets\x01",
            "those mistakes, man\x01",
            "cannot grow...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45FD")

    label("loc_4500")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_457F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_452A")
    OP_FC(0xFFFA)
    Jump("loc_452D")

    label("loc_452A")

    OP_FC(0xFFF4)

    label("loc_452D")


    ChrTalk(
        0x106,
        (
            "#10701F#13P#30WStill, if he forgets\x01",
            "those mistakes, man\x01",
            "cannot grow...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45FD")

    label("loc_457F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45A9")
    OP_FC(0xFFFA)
    Jump("loc_45AC")

    label("loc_45A9")

    OP_FC(0xFFF4)

    label("loc_45AC")


    ChrTalk(
        0x109,
        (
            "#10101F#13P#30WHowever, if he forgets\x01",
            "those mistakes, man\x01",
            "won't ever grow.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_45FD")


    ChrTalk(
        0x103,
        (
            "#00204F#12P#N#30W...The meaning of learning\x01",
            "together, cooperating,\x01",
            "moving forward...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00300F#6P#N#30WYeah, it would end up\x01",
            "cleanly castin' away all\x01",
            "of that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        "#02211F#11P#40W...............\x02",
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
            "#12305F#5P#N#30W...Lloyd...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00004F#11P─KeA. Come back with us.\x02\x03",
            "#00000FYou don't need to push\x01",
            "yourself for our sake any\x01",
            "more than you already have.\x02",
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
            "#00008F#11P...When we lost our\x01",
            "lives before...\x02\x03",
            "We made you feel...\x01",
            "heartbroken, in pain and\x01",
            "sad.\x02\x03",
            "#00006FSorry, KeA. It was our\x01",
            "fault for being\x01",
            "worthless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#5P#N#30WT-That's not true!\x02\x03",
            "#12313F...KeA did that of her\x01",
            "own free will!\x02\x03",
            "So, Lloyd, you don't\x01",
            "have to apologize─\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#11PThen, KeA.\x02\x03",
            "#00013FWhy have you been making\x01",
            "that sad face this whole\x01",
            "time?\x02",
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
            "by manipulating causality because\x01",
            "you were so sad over our deaths...\x02\x03",
            "#00013F─You realized it was "unfair".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#5P#N#40W...Ah...\x02\x03",
            "#12308F...............\x02",
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
            "#00306F#11PWell, I can't really say\x01",
            "I'd be glad if we were\x01",
            "dead, but...\x02\x03",
            "#00300FEven so, I can certainly\x01",
            "say that was an "illegal\x01",
            "move".\x02",
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
            "#00106F#11P...Lawyer Ian, Bell.\x02\x03",
            "About that... I think\x01",
            ""politics" is the same.\x02\x03",
            "#00108FSometimes, there are\x01",
            "times when things must be\x01",
            "done in an improper way.\x02\x03",
            "#00101FHowever, doing things\x01",
            "improperly is a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02201F#5P...Elie...\x02",
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
            "That's not politics anymore, that's\x01",
            "merely praying to a god.\x02\x03",
            "#00108FOvercoming difficult circumstances with\x01",
            "the proper procedures and dialogue,\x01",
            "thinking of them as everyone's problem...\x02\x03",
            "#00101FThat's what I think "true politics" is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI think it's very possible that, without\x01",
            "KeA's power, Crossbell will be faced with\x01",
            "serious dangers.\x02\x03",
            "#00008FUnrest across the whole continent,\x01",
            "economic crisis... And also, as soon as\x01",
            "the civil war in the Empire is over, it'll\x01",
            "probably bare its fangs at Crossbell.\x02",
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
            "#00013F#11P─And yet, I still can't think\x01",
            "that forcing all of this on KeA\x01",
            "is the right choice.\x02\x03",
            "#00004FIf we relied only on miracles\x01",
            "given to us, we would never\x01",
            "grow...\x02\x03",
            "#00000FThat's why, even if it's\x01",
            "painful... I think we now have\x01",
            "to proceed in "the proper way".\x02",
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
        "#02203F#5P#40W...............\x02",
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
        "#02211F#11P#40W...So this is it.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 28)
    WaitChrThread(0x8, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40WI... thought it wasn't a\x01",
            "personal grudge, but...\x02\x03",
            "Really... In some\x01",
            "respects, it's like I\x01",
            "was deceiving myself.\x02\x03",
            "#02200F...It seemed just like I\x01",
            "was being reprimanded by\x01",
            "Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#N...Lawyer Ian...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#02203F#11P#40W...I'm sorry. I had no\x01",
            "right to tell you.\x02\x03",
            "...............\x02",
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
            "#02203F#11P#30W...KeA. I'm sorry to\x01",
            "have misled you.\x02\x03",
            "#02201FYou should decide what\x01",
            "to do... using your own\x01",
            "judgement.\x02\x03",
            "#02202FYou should be able to do\x01",
            "that, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#5P#N#30W...Lawyer Ian....\x02",
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
            "#02203F#11P#30WAlso, Mariabell... I'm\x01",
            "sorry for not living up\x01",
            "to your expectations.\x02\x03",
            "#02201FIt seems my role ends\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#6PUhuhu... I don't mind.\x02\x03",
            "After all, it was I who\x01",
            "originally came to you for a\x01",
            "comprehensive project plan.\x02\x03",
            "#10811FThank you for all your hard\x01",
            "work up until now─ Mr.\x01",
            "Grimwood.\x02",
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

    def lambda_551C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_551C)
    BeginChrThread(0xC, 3, 0, 33)
    Sleep(250)

    def lambda_5536():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5536)
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

    def lambda_565F():

        label("loc_565F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_565F")

    QueueWorkItem2(0x101, 2, lambda_565F)

    def lambda_5671():

        label("loc_5671")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5671")

    QueueWorkItem2(0x102, 2, lambda_5671)

    def lambda_5683():

        label("loc_5683")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5683")

    QueueWorkItem2(0x103, 2, lambda_5683)

    def lambda_5695():

        label("loc_5695")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5695")

    QueueWorkItem2(0x104, 2, lambda_5695)

    def lambda_56A7():

        label("loc_56A7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56A7")

    QueueWorkItem2(0xF4, 2, lambda_56A7)

    def lambda_56B9():

        label("loc_56B9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56B9")

    QueueWorkItem2(0xF5, 2, lambda_56B9)
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
        "#00007F#12P#NWha!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#12P#N...Bell!?\x02",
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
            "#02213F#11P#60W...Haha... This too\x01",
            "is... karmic\x01",
            "retribution, eh?\x02\x03",
            "#70WGuy... Lloyd...\x01",
            "...I'm... sorry...\x02",
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
        "#00207F#5PLawyer Ian!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5893")

    ChrTalk(
        0x10A,
        "#00610F#5PWhat did you!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_58FA")

    label("loc_5893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58C7")

    ChrTalk(
        0x109,
        "#10110F#5PHow could you!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_58FA")

    label("loc_58C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58FA")

    ChrTalk(
        0x106,
        "#10707F#5P...How could you...\x02",
    )

    CloseMessageWindow()

    label("loc_58FA")

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

    def lambda_5967():
        TurnDirection(0x101, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5967)
    Sleep(0)

    def lambda_5977():
        TurnDirection(0x102, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5977)
    Sleep(0)

    def lambda_5987():
        TurnDirection(0x103, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5987)
    Sleep(0)

    def lambda_5997():
        TurnDirection(0x104, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5997)
    Sleep(0)

    def lambda_59A7():
        TurnDirection(0xF4, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_59A7)
    Sleep(0)

    def lambda_59B7():
        TurnDirection(0xF5, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_59B7)
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
            "#12313F#12PBell... Why!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#5PUhuhu, I merely disposed\x01",
            "of a useless tool.\x02\x03",
            "#10811FIn that sense, KeA. ─You\x01",
            "are no exception, you\x01",
            "know?\x02",
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
            "#12311F#3646V#5P#50W#18A...Uwaah!?\x02",
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
        "#00007F#5PKeA!?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PHey! The fuck are you\x01",
            "doin' to our kid!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#10804F#5PHuhu. If she continues to be hesitant,\x01",
            "I will have her turn into an adorable\x01",
            "doll with no will of its own...\x02\x03",
            "#10811FBy nature, she is a homunculus given\x01",
            "life by the Crois clan's secret\x01",
            "arts...\x02\x03",
            "Is how to handle her not mine to\x01",
            "freely decide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PS-Stop messing around!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#11PBell! There're some things\x01",
            "you can say, and some things\x01",
            "you can't, you know!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#5P...I'll have you take\x01",
            "that back!\x02",
        )
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
            "#3791V#40W#36AUhuhuhuhu... Very well.\x02\x03",
            "#3792V#25AI am Mariabell Crois.\x02\x03",
            "#3793V#50ADescendant of the clan that desired\x01",
            "a Sept-Terrion surpassing the\x01",
            "Goddess, and sacrified everything\x02\x03",
            "to get it...\x02\x03",
            "#3794V#71AWhich is really strong? The weight\x01",
            "of a firm conviction spanning 1000\x01",
            "years? Or your bonds which amount\x02\x03",
            "to not even a year...?\x02\x03",
            "#3795V#35AShall we try comparing them using\x01",
            "the full extent of our powers?\x02",
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
        "#00007F#6P#30W#15ABring it on!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#30W#20A#NBell! I won't go easy on\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_615E")
    OP_FC(0x6)
    Jump("loc_6161")

    label("loc_615E")

    OP_FC(0xC)

    label("loc_6161")


    ChrTalk(
        0x105,
        (
            "#10407F#13P#30W#25A#NI acknowledge you as a\x01",
            "supreme Magius! I'll\x01",
            "attack with my full power!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D2")

    label("loc_61C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_624D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61F1")
    OP_FC(0x6)
    Jump("loc_61F4")

    label("loc_61F1")

    OP_FC(0xC)

    label("loc_61F4")


    ChrTalk(
        0x106,
        (
            "#10707F#13P#30W#25A#NI sense dark powers!\x01",
            "I'll exorcise you with\x01",
            "all my might!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D2")

    label("loc_624D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6277")
    OP_FC(0x6)
    Jump("loc_627A")

    label("loc_6277")

    OP_FC(0xC)

    label("loc_627A")


    ChrTalk(
        0x109,
        (
            "#10107F#13P#30W#25A#NEstimated danger level:\x01",
            "S! I'll attack with all\x01",
            "my firepower!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D2")

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

    def Function_7_6300(): pass

    label("Function_7_6300")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_633F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_633F)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_7_6300 end

    def Function_8_636A(): pass

    label("Function_8_636A")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_63A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_63A9)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_8_636A end

    def Function_9_63D4(): pass

    label("Function_9_63D4")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6413():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6413)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_9_63D4 end

    def Function_10_643E(): pass

    label("Function_10_643E")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_647D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_647D)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_10_643E end

    def Function_11_64A8(): pass

    label("Function_11_64A8")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_64E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64E7)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_11_64A8 end

    def Function_12_6512(): pass

    label("Function_12_6512")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6551():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6551)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_12_6512 end

    def Function_13_657C(): pass

    label("Function_13_657C")

    OP_95(0xFE, 0, 1000, -12060, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_657C end

    def Function_14_6598(): pass

    label("Function_14_6598")

    Sleep(50)
    OP_95(0xFE, 1120, 1000, -13300, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_6598 end

    def Function_15_65B7(): pass

    label("Function_15_65B7")

    Sleep(100)
    OP_95(0xFE, 420, 1000, -14370, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_65B7 end

    def Function_16_65D6(): pass

    label("Function_16_65D6")

    Sleep(150)
    OP_95(0xFE, -1270, 1000, -13930, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_65D6 end

    def Function_17_65F5(): pass

    label("Function_17_65F5")

    Sleep(200)
    OP_95(0xFE, -2540, 1990, -13310, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_65F5 end

    def Function_18_6614(): pass

    label("Function_18_6614")

    Sleep(250)
    OP_95(0xFE, 2540, 1000, -13510, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_6614 end

    def Function_19_6633(): pass

    label("Function_19_6633")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_6633 end

    def Function_20_6645(): pass

    label("Function_20_6645")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_6645 end

    def Function_21_6654(): pass

    label("Function_21_6654")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_6654 end

    def Function_22_6666(): pass

    label("Function_22_6666")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_6666 end

    def Function_23_6678(): pass

    label("Function_23_6678")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_6678 end

    def Function_24_6684(): pass

    label("Function_24_6684")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66A4")
    Sound(540, 0, 50, 0)
    Jump("loc_66C9")

    label("loc_66A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C9")
    Sound(531, 0, 100, 0)

    label("loc_66C9")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_6684 end

    def Function_25_66D2(): pass

    label("Function_25_66D2")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66F2")
    Sound(540, 0, 50, 0)
    Jump("loc_6717")

    label("loc_66F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6717")
    Sound(531, 0, 100, 0)

    label("loc_6717")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_66D2 end

    def Function_26_6720(): pass

    label("Function_26_6720")

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

    # Function_26_6720 end

    def Function_27_6756(): pass

    label("Function_27_6756")

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

    # Function_27_6756 end

    def Function_28_6793(): pass

    label("Function_28_6793")

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

    # Function_28_6793 end

    def Function_29_67E5(): pass

    label("Function_29_67E5")

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

    # Function_29_67E5 end

    def Function_30_6905(): pass

    label("Function_30_6905")

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

    # Function_30_6905 end

    def Function_31_6A54(): pass

    label("Function_31_6A54")

    SetChrChipByIndex(0xFE, 0x21)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)

    label("loc_6A72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AC8")
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
    Jump("loc_6A72")

    label("loc_6AC8")

    Return()

    # Function_31_6A54 end

    def Function_32_6AC9(): pass

    label("Function_32_6AC9")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(600)
    Return()

    # Function_32_6AC9 end

    def Function_33_6AE5(): pass

    label("Function_33_6AE5")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_33_6AE5 end

    def Function_34_6AFA(): pass

    label("Function_34_6AFA")

    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_34_6AFA end

    def Function_35_6B09(): pass

    label("Function_35_6B09")

    SetChrPos(0x8, 9600, 700, -9900, 305)
    SetChrChipByIndex(0x8, 0x21)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrSubChip(0x8, 0x5)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 9730, 1100, -10330, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_35_6B09 end

    def Function_36_6B74(): pass

    label("Function_36_6B74")

    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(429)
    Return()

    # Function_36_6B74 end

    def Function_37_6B8A(): pass

    label("Function_37_6B8A")

    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_37_6B8A end

    def Function_38_6BA0(): pass

    label("Function_38_6BA0")

    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(500)
    Return()

    # Function_38_6BA0 end

    def Function_39_6BB6(): pass

    label("Function_39_6BB6")

    SetChrSubChip(0xFE, 0x12)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(667)
    Return()

    # Function_39_6BB6 end

    def Function_40_6BCC(): pass

    label("Function_40_6BCC")

    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x12)
    Sleep(667)
    Return()

    # Function_40_6BCC end

    def Function_41_6BE2(): pass

    label("Function_41_6BE2")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_41_6BE2 end

    def Function_42_6BFF(): pass

    label("Function_42_6BFF")

    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_42_6BFF end

    def Function_43_6C1C(): pass

    label("Function_43_6C1C")

    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    Return()

    # Function_43_6C1C end

    def Function_44_6C2B(): pass

    label("Function_44_6C2B")

    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    Return()

    # Function_44_6C2B end

    def Function_45_6C3A(): pass

    label("Function_45_6C3A")

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

    # Function_45_6C3A end

    def Function_46_6C87(): pass

    label("Function_46_6C87")

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
            "#12306F#5P#60W...*sigh*... *pant,\x01",
            "pant*...\x02",
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
            "#12314F#11P#N#45W...Yes... Ehehe...\x01",
            "Somehow...\x02",
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
        "#00306F#5P*sigh*, man oh man...\x02",
    )

    CloseMessageWindow()

    def lambda_71B7():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_71B7)
    WaitChrThread(0xA, 2)
    Sleep(500)
    PlayBGM("ed7572", 0)

    ChrTalk(
        0xA,
        (
            "#10803F#11P#30WGuh... I see.\x02\x03",
            "#10801FAs expected... It wasn't\x01",
            "for nothing that you beat\x01",
            "Arios and the others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PBell... End it here!\x02\x03",
            "#00101FThere's no more meaning\x01",
            "in fighting us!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11P#30WUhuhu, my cute Elie.\x02\x03",
            "I don't think this request is so\x01",
            "unexpected, coming from you, but...\x02\x03",
            "#10811FYou know already, right...? My\x01",
            "personality is such that, the cuter the\x01",
            "girl, the more I want to tease them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PW-What are you...\x02",
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
            "#10802F#5P#30W─By the way, KeA.\x02\x03",
            "I wonder if Lloyd and\x01",
            "the others know about\x01",
            ""that thing"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#N#30W...Ah...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10809F#5PUhuhu. Based on\x01",
            "reaction, I suppose you\x01",
            "haven't told them?\x02\x03",
            "#10811FThat's just perfect\x01",
            "then. Shall we tell them\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12313F#11P#N#30WN-No... Stop...\x02\x03",
            "#12311F...Bell... I'm begging\x01",
            "you!\x02",
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
        "#00013F#5P...What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PHey, young lady!\x02\x03",
            "Don't tease our Keddo,\x01",
            "got it!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#10804F#11PUhuhu. You all really do love\x01",
            "KeA, don't you?\x02\x03",
            "#10800FA homunculus without a genuine\x01",
            "soul, entrusted to the Cult by\x01",
            "the Crois clan....\x02\x03",
            "A fake doll for the sole purpose\x01",
            "of joining together the countless\x01",
            "souls sacrificed by the cult.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5PThat again!?\x02\x03",
            "#00010FZeit already told us\x01",
            "about that a long time\x01",
            "ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PKeA staying at our side\x01",
            "as KeA...\x02\x03",
            "#00201FThere's nothing more\x01",
            "important than that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10804F#11PUhuhu, KeA. You're really lucky, aren't\x01",
            "you?\x02\x03",
            "You've been able to gather the favor and\x01",
            "affection of Lloyd and the others... No, of\x01",
            "all the people you came in contact with.\x02\x03",
            "#10811F─Because of your powers.\x02",
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

    def lambda_7942():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7942)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_7962():
        OP_A6(0xFE, 0x0, 0x32, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7962)
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
            "#12306F#5P#N#50W...Ooh... Aaah....\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00005F#6P#N...Huh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#N...Bell... What did you\x01",
            "just...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10811F#11P#30WHeh... Did you not find it strange,\x01",
            "I wonder?\x02\x03",
            "Most likely, right after meeting\x01",
            "her, you could not help but love\x01",
            "her and want to protect her, right?\x02\x03",
            "Why do you think that was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P#N...............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#N...It can't be...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NHey now, what nonsense\x01",
            "are you...\x02",
        )
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
            "#10804F#11P#30W─It goes without saying for that Joachim,\x01",
            "but neither the mafia nor even monsters\x01",
            "ever tried to actively harm KeA.\x02\x03",
            "A little girl with whom everyone becomes\x01",
            "friends immediately, who ends up being\x01",
            "loved unconditionally...\x02\x03",
            "#10811FHas anyone ever thought to question that\x01",
            "abnormality?\x02",
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
            "#12307F#3647V#5P#N#50W#30A...No... That's not\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#10803F#11P#30W#15ANo─ That's exactly how\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#10801F#11P#40W#30AThough unconscious, you have the\x01",
            "power to catch hold of the hearts and\x01",
            "souls of the people who surround you.\x02\x03",
            "#10804F#40W#30AThe power to manipulate causality and\x01",
            "cognition to have everybody love you,\x01",
            "protect you.\x02\x03",
            "#10811F#40W#30AHehe... Imitation love for an\x01",
            "imitation of an existence, huh?\x02",
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
        "#00110F#5P#40W#20A...Ah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8435")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83FA")
    OP_FC(0x5)
    Jump("loc_83FD")

    label("loc_83FA")

    OP_FC(0xB)

    label("loc_83FD")


    ChrTalk(
        0x105,
        (
            "#10410F#13P#40W#20A...This spirit\x01",
            "pressure...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F1")

    label("loc_8435")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8499")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_845F")
    OP_FC(0x5)
    Jump("loc_8462")

    label("loc_845F")

    OP_FC(0xB)

    label("loc_8462")


    ChrTalk(
        0x106,
        (
            "#10707F#13P#40W#20AT-This spirit\x01",
            "pressure...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F1")

    label("loc_8499")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84C3")
    OP_FC(0x5)
    Jump("loc_84C6")

    label("loc_84C3")

    OP_FC(0xB)

    label("loc_84C6")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20A...T-This light...\x02",
    )

    CloseMessageWindow()

    label("loc_84F1")

    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8554")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_851E")
    OP_FC(0x5)
    Jump("loc_8521")

    label("loc_851E")

    OP_FC(0xB)

    label("loc_8521")


    ChrTalk(
        0x10A,
        "#00610F#13P#40W#20AAn azure... "god"...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_860F")

    label("loc_8554")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_857E")
    OP_FC(0x5)
    Jump("loc_8581")

    label("loc_857E")

    OP_FC(0xB)

    label("loc_8581")


    ChrTalk(
        0x109,
        "#10110F#13P#40W#20AAn azure... "god"...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_860F")

    label("loc_85B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_860F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85DE")
    OP_FC(0x5)
    Jump("loc_85E1")

    label("loc_85DE")

    OP_FC(0xB)

    label("loc_85E1")


    ChrTalk(
        0x106,
        "#10700F#13P#40W#20AAn azure... "god"...?\x02",
    )

    CloseMessageWindow()

    label("loc_860F")

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
            "#10804F#3796V#6P#N#40W#82AHehe. This is her original form, after\x01",
            "complete unification of the Sept-Terrion of\x01",
            "Zero and the Azure Tree...\x02\x03",
            "#3797V#80AThe god of the false world that manipulates\x01",
            "the causality of all space-time and truly\x01",
            "shatters the shackles imposed by the Goddess!\x02\x03",
            "#10811F#3798V#35AThe Azure Demiourgos!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00010F#3332V#6P#N#30W#25AI don't give a damn\x01",
            "about your speeches!\x02\x03",
            "#3333V#35AEverything will start\x01",
            "after... we've taken\x01",
            "back that child, KeA!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#2775V#6P#N#30W#32AYeah, it won't be too\x01",
            "late for serious\x01",
            "discussion after that!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#2695V#12P#N#30W#40A─Manifestation of a gigantic\x01",
            "spiritual body confirmed! KeA is\x01",
            "inside the core part in the center!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#3408V#12P#N#30W#32AWe must get KeA out of\x01",
            "there at any cost!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00015F#3334V#6P#N#30AEveryone─ This the final\x01",
            "battle!\x02\x03",
            "#00007F#3335V#50ALet's hit that azure existence\x01",
            "hard with everything we've\x01",
            "got, body and soul!!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B28")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_8B31")

    label("loc_8B28")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_8B31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B64")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B5E")
    Sound(2417, 255, 100, 4)
    Jump("loc_8B64")

    label("loc_8B5E")

    Sound(2417, 255, 100, 3)

    label("loc_8B64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B91")
    Sound(4115, 255, 100, 4)
    Jump("loc_8B97")

    label("loc_8B91")

    Sound(4115, 255, 100, 3)

    label("loc_8B97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BC4")
    Sound(3174, 255, 100, 4)
    Jump("loc_8BCA")

    label("loc_8BC4")

    Sound(3174, 255, 100, 3)

    label("loc_8BCA")

    SetChrName("Members")

    AnonymousTalk(
        0xFF,
        "#5S#15AYeah!\x02",
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

    # Function_46_6C87 end

    def Function_47_8C6F(): pass

    label("Function_47_8C6F")

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

    # Function_47_8C6F end

    def Function_48_8CBE(): pass

    label("Function_48_8CBE")

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

    # Function_48_8CBE end

    def Function_49_8CE8(): pass

    label("Function_49_8CE8")

    Sound(898, 0, 100, 0)
    Return()

    # Function_49_8CE8 end

    def Function_50_8CEF(): pass

    label("Function_50_8CEF")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(400)
    Return()

    # Function_50_8CEF end

    def Function_51_8D0B(): pass

    label("Function_51_8D0B")

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

    # Function_51_8D0B end

    def Function_52_8D89(): pass

    label("Function_52_8D89")

    OP_71(0x0, 0x821, 0x82A, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xF, 3, 0, 55)
    OP_71(0x0, 0x835, 0x85B, 0x0, 0x20)
    Return()

    # Function_52_8D89 end

    def Function_53_8DAB(): pass

    label("Function_53_8DAB")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7460", 0)
    Return()

    # Function_53_8DAB end

    def Function_54_8DB9(): pass

    label("Function_54_8DB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DD2")
    Sound(824, 0, 100, 0)
    Sleep(1300)
    Jump("Function_54_8DB9")

    label("loc_8DD2")

    Return()

    # Function_54_8DB9 end

    def Function_55_8DD3(): pass

    label("Function_55_8DD3")

    Sleep(200)

    label("loc_8DD6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DEF")
    Sound(824, 0, 50, 0)
    Sleep(3800)
    Jump("loc_8DD6")

    label("loc_8DEF")

    Return()

    # Function_55_8DD3 end

    def Function_56_8DF0(): pass

    label("Function_56_8DF0")

    Sound(929, 0, 50, 0)
    Sleep(500)
    Sound(940, 0, 100, 0)
    Sleep(200)
    Sound(936, 0, 100, 0)
    Sound(1029, 0, 100, 0)
    Return()

    # Function_56_8DF0 end

    def Function_57_8E0F(): pass

    label("Function_57_8E0F")

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

    def lambda_9250():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9250)
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
        "#00310F#6PGuh... What the heck!?\x02",
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
        (
            "#00007F#6P#4SIf you can hear me,\x01",
            "answer me!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10803F#6P#30WGuh, impossible...\x02\x03",
            "#10810F...At this rate... Is it going to be\x01",
            "like what happened with the Sept-\x01",
            "Terrion of Mirage back then...?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9583")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_955B")
    OP_FC(0x6)
    Jump("loc_955E")

    label("loc_955B")

    OP_FC(0xC)

    label("loc_955E")


    ChrTalk(
        0x109,
        "#10107F#13PY-You mean...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_962A")

    label("loc_9583")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95AD")
    OP_FC(0x6)
    Jump("loc_95B0")

    label("loc_95AD")

    OP_FC(0xC)

    label("loc_95B0")


    ChrTalk(
        0x106,
        "#10707F#13PY-You mean...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_962A")

    label("loc_95D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_962A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95FF")
    OP_FC(0x6)
    Jump("loc_9602")

    label("loc_95FF")

    OP_FC(0xC)

    label("loc_9602")


    ChrTalk(
        0x10A,
        "#00607F#13PDon't tell me that...!?\x02",
    )

    CloseMessageWindow()

    label("loc_962A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9654")
    OP_FC(0x6)
    Jump("loc_9657")

    label("loc_9654")

    OP_FC(0xC)

    label("loc_9657")


    ChrTalk(
        0x105,
        (
            "#10410F#13PWhen it unbound the causality\x01",
            "of its own existence and\x01",
            "erased itself!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9796")

    label("loc_96B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9727")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96DD")
    OP_FC(0x6)
    Jump("loc_96E0")

    label("loc_96DD")

    OP_FC(0xC)

    label("loc_96E0")


    ChrTalk(
        0x10A,
        (
            "#00610F#13PWhen it ended up erasing\x01",
            "itself by its own hand!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9796")

    label("loc_9727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9796")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9751")
    OP_FC(0x6)
    Jump("loc_9754")

    label("loc_9751")

    OP_FC(0xC)

    label("loc_9754")


    ChrTalk(
        0x106,
        (
            "#10701F#13PWhen it ended up erasing\x01",
            "itself by its own hand!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9796")


    ChrTalk(
        0x101,
        "#00013F#6P...............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 61)
    OP_68(0, 2800, -6500, 2000)
    MoveCamera(330, 5, 0, 2000)
    OP_6E(700, 2000)
    Sleep(500)

    def lambda_97EB():

        label("loc_97EB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_97EB")

    QueueWorkItem2(0xA, 2, lambda_97EB)
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
        "#00105F#6P#NLloyd!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00207F#6P#NLloyd!?\x02",
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
        "#00307F#6P#NWhat are you planning!?\x02",
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
            "Wait there for me!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x4, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        (
            "#00015F#5P#60W#25AThis child... I'll\x01",
            "definitely...\x02",
        )
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
        (
            "#00007F#5P#80W#28A...With my own hands,\x01",
            "I'll... KeA─\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(4000, 16777215, -1)

    def lambda_9B44():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9B44)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF0")

    ChrTalk(
        0x102,
        "#00107F#3409V#6P#4S#N#15A#30WLloooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D29")

    label("loc_9BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2F")

    ChrTalk(
        0x103,
        "#00207F#2696V#6P#4S#N#15A#30WLloyd─!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D29")

    label("loc_9C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C6F")

    ChrTalk(
        0x104,
        "#00307F#2776V#6P#4S#N#15A#30WLloooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D29")

    label("loc_9C6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CAE")

    ChrTalk(
        0x105,
        "#10407F#2925V#6P#4S#N#15A#30WLloyd─!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D29")

    label("loc_9CAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CEF")

    ChrTalk(
        0x109,
        "#10107F#3531V#6P#4S#N#15A#30WLlooooyd!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D29")

    label("loc_9CEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D29")

    ChrTalk(
        0x106,
        "#10707F#3264V#6P#4S#N#15A#30WLloyd─!\x02",
    )

    CloseMessageWindow()

    label("loc_9D29")

    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9013", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_57_8E0F end

    def Function_58_9D43(): pass

    label("Function_58_9D43")

    OP_74(0x1, 0xA)
    OP_71(0x1, 0x51, 0x64, 0x0, 0x20)
    Return()

    # Function_58_9D43 end

    def Function_59_9D54(): pass

    label("Function_59_9D54")

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

    # Function_59_9D54 end

    def Function_60_9D8F(): pass

    label("Function_60_9D8F")

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

    def lambda_9E11():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E11)

    def lambda_9E2B():
        OP_96(0xFE, 0x0, 0xFA0, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9E2B)
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

    # Function_60_9D8F end

    def Function_61_9EB2(): pass

    label("Function_61_9EB2")

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

    def lambda_9F7E():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9F7E)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)
    OP_9B(0x1, 0xFE, 0x0, 0x190, 0x3E8, 0x0)
    StopEffect(0x4, 0x2)
    Sound(833, 0, 60, 0)
    PlayEffect(0x3, 0x5, 0xFF, 0x1, 60, 4500, -2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)

    def lambda_9FF1():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9FF1)
    Sleep(250)
    SetChrSubChip(0xFE, 0x23)
    OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x3)

    label("loc_A01F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A04B")

    def lambda_A02F():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A02F)
    Sleep(400)
    Jump("loc_A01F")

    label("loc_A04B")

    Return()

    # Function_61_9EB2 end

    def Function_62_A04C(): pass

    label("Function_62_A04C")

    PlayEffect(0x3, 0xFF, 0xFF, 0x1, 60, 4100, -2210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0xB)

    def lambda_A08C():
        OP_A6(0xFE, 0x0, 0x32, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A08C)
    Sleep(250)
    SetChrSubChip(0xFE, 0x13)

    def lambda_A0AC():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0AC)
    Sound(920, 0, 100, 0)
    Sound(1005, 0, 100, 0)
    Sleep(700)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_62_A04C end

    def Function_63_A0D1(): pass

    label("Function_63_A0D1")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_63_A0D1 end

    def Function_64_A0E0(): pass

    label("Function_64_A0E0")

    Sleep(100)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_A0E0 end

    def Function_65_A0F2(): pass

    label("Function_65_A0F2")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_A0F2 end

    def Function_66_A104(): pass

    label("Function_66_A104")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_66_A104 end

    def Function_67_A110(): pass

    label("Function_67_A110")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A130")
    Sound(540, 0, 50, 0)
    Jump("loc_A155")

    label("loc_A130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A155")
    Sound(531, 0, 50, 0)

    label("loc_A155")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_A110 end

    def Function_68_A15E(): pass

    label("Function_68_A15E")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A17E")
    Sound(540, 0, 50, 0)
    Jump("loc_A1A3")

    label("loc_A17E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1A3")
    Sound(531, 0, 50, 0)

    label("loc_A1A3")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_68_A15E end

    def Function_69_A1AC(): pass

    label("Function_69_A1AC")

    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(571)
    Return()

    # Function_69_A1AC end

    def Function_70_A1C9(): pass

    label("Function_70_A1C9")

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

    # Function_70_A1C9 end

    def Function_71_A20E(): pass

    label("Function_71_A20E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A625")
    Jump("loc_A6CF")

    label("loc_A625")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A648")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x103)
    OP_FD(0x103, 0x10)
    Jump("loc_A6CF")

    label("loc_A648")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66B")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x104)
    OP_FD(0x104, 0x10)
    Jump("loc_A6CF")

    label("loc_A66B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68E")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x105)
    OP_FD(0x105, 0x10)
    Jump("loc_A6CF")

    label("loc_A68E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6B1")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x109)
    OP_FD(0x109, 0x10)
    Jump("loc_A6CF")

    label("loc_A6B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6CF")
    OP_FD(0x10, 0x102)
    OP_FD(0x102, 0x106)
    OP_FD(0x106, 0x10)

    label("loc_A6CF")

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

    def lambda_A7FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7FB)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 0, 0, 73)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B1")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20AAhhh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd... Keddo...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#11P#30W#20AYou've come... back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AC4B")

    label("loc_A8B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A940")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AWoah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00116F#6P#30W#20ALloyd... KeA!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#11P#30W#20AYou've come... back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AC4B")

    label("loc_A940")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9DA")

    ChrTalk(
        0x102,
        "#00116F#12P#30W#20AAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20ALloyd... KeA...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00315F#11P#30W#20AHaha... You've come...\x01",
            "back...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AC4B")

    label("loc_A9DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA03")
    OP_FC(0xC)
    Jump("loc_AA06")

    label("loc_AA03")

    OP_FC(0x6)

    label("loc_AA06")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...Lloyd!\x02",
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
        "#10411F#11P#30W#20AHehe... You're back, eh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AC4B")

    label("loc_AAB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB80")

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20AAhhh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20ALloyd!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB1E")
    OP_FC(0xC)
    Jump("loc_AB21")

    label("loc_AB1E")

    OP_FC(0x6)

    label("loc_AB21")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20AAnd KeA too!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10116F#11P#30W#20AYou've come... back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_AC4B")

    label("loc_AB80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4B")

    ChrTalk(
        0x104,
        "#00316F#12P#30W#20AWoah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABCA")
    OP_FC(0xC)
    Jump("loc_ABCD")

    label("loc_ABCA")

    OP_FC(0x6)

    label("loc_ABCD")


    ChrTalk(
        0x102,
        "#00116F#13P#30W#20ALloyd!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00216F#6P#30W#20A...And KeA too!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        "#10716F#11P#30W#20AYou've come... back...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AC4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACD4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC75")
    OP_FC(0xC)
    Jump("loc_AC78")

    label("loc_AC75")

    OP_FC(0x6)

    label("loc_AC78")


    ChrTalk(
        0x10A,
        (
            "#00604F#13P#30W#20AHonestly... That\x01",
            "recklessness would put\x01",
            "your brother to shame...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_ACD4")

    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#40WPhew...\x02\x03",
            "#30W#00000F─We're back, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#50W...Ooh... *sob*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD57")
    OP_FC(0x5)
    Jump("loc_ADED")

    label("loc_AD57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD80")
    OP_FC(0xC)
    Jump("loc_AD83")

    label("loc_AD80")

    OP_FC(0x6)

    label("loc_AD83")

    Jump("loc_ADED")

    label("loc_AD88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADB1")
    OP_FC(0xC)
    Jump("loc_ADB4")

    label("loc_ADB1")

    OP_FC(0x6)

    label("loc_ADB4")

    Jump("loc_ADED")

    label("loc_ADB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADE2")
    OP_FC(0xC)
    Jump("loc_ADE5")

    label("loc_ADE2")

    OP_FC(0x6)

    label("loc_ADE5")

    Jump("loc_ADED")

    label("loc_ADEA")

    OP_FC(0xB)

    label("loc_ADED")

    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00114F#13PLloyd... Thank goodness!\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7C")
    OP_FC(0xB)
    Jump("loc_AE7F")

    label("loc_AE7C")

    OP_FC(0x5)

    label("loc_AE7F")

    OP_6F(0x79)
    SetCameraDistance(10000, 30000)

    ChrTalk(
        0x103,
        (
            "#00214F#13PKeA... Are you all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PIt looks like she\x01",
            "returned to her original\x01",
            "form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, it's all right\x01",
            "now.\x02\x03",
            "#00000F...Come on, KeA. You\x01",
            "have something to tell\x01",
            "everyone, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#05817F#5P#40W*sigh*... Yeah...\x02",
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
            "#05821F#5P#40WI'm... sorry...\x02\x03",
            "...For having always made\x01",
            "you worry... For doing\x01",
            "things on my own...\x02\x03",
            "#05818FAnd also... Thank you for\x01",
            "coming for me...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0AB")
    OP_FC(0x5)
    Jump("loc_B141")

    label("loc_B0AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0D4")
    OP_FC(0xC)
    Jump("loc_B0D7")

    label("loc_B0D4")

    OP_FC(0x6)

    label("loc_B0D7")

    Jump("loc_B141")

    label("loc_B0DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B10D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B105")
    OP_FC(0xC)
    Jump("loc_B108")

    label("loc_B105")

    OP_FC(0x6)

    label("loc_B108")

    Jump("loc_B141")

    label("loc_B10D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B13E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B136")
    OP_FC(0xC)
    Jump("loc_B139")

    label("loc_B136")

    OP_FC(0x6)

    label("loc_B139")

    Jump("loc_B141")

    label("loc_B13E")

    OP_FC(0xB)

    label("loc_B141")


    ChrTalk(
        0x102,
        "#00116F#13PKeA...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B16F")
    OP_FC(0xB)
    Jump("loc_B172")

    label("loc_B16F")

    OP_FC(0x5)

    label("loc_B172")


    ChrTalk(
        0x103,
        "#00204F#13PNo need for thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PHaha... Ya best be\x01",
            "prepared for a spankin'\x01",
            "when we get home, 'k?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 76)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#05817F#5P#50W...Okay... *sob*...\x01",
            "Ooooh....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11POh, come on... There's\x01",
            "nothing to cry about\x01",
            "anymore, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B29A")
    OP_FC(0xC)
    Jump("loc_B29D")

    label("loc_B29A")

    OP_FC(0x6)

    label("loc_B29D")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph...\x02",
    )

    CloseMessageWindow()

    label("loc_B2B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B31B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2DC")
    OP_FC(0xB)
    Jump("loc_B2F9")

    label("loc_B2DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2F6")
    OP_FC(0xC)
    Jump("loc_B2F9")

    label("loc_B2F6")

    OP_FC(0x6)

    label("loc_B2F9")


    ChrTalk(
        0x105,
        "#10404F#13PHehe, oh brother.\x02",
    )

    CloseMessageWindow()

    label("loc_B31B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B387")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B342")
    OP_FC(0xB)
    Jump("loc_B35F")

    label("loc_B342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B35C")
    OP_FC(0xC)
    Jump("loc_B35F")

    label("loc_B35C")

    OP_FC(0x6)

    label("loc_B35F")


    ChrTalk(
        0x109,
        "#10106F#13P...*sob*... I'm glad...\x02",
    )

    CloseMessageWindow()

    label("loc_B387")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3F6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3AE")
    OP_FC(0xB)
    Jump("loc_B3CB")

    label("loc_B3AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3C8")
    OP_FC(0xC)
    Jump("loc_B3CB")

    label("loc_B3C8")

    OP_FC(0x6)

    label("loc_B3CB")


    ChrTalk(
        0x106,
        (
            "#10710F#13P(...These are...\x01",
            "bonds...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3F6")

    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#10803F#3799V#5P#N#40W#35A─Honestly. What a boring\x01",
            "ending.\x02",
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

    def lambda_B521():
        OP_93(0xFE, 0xAF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B521)
    Sleep(50)

    def lambda_B531():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B531)
    Sleep(50)

    def lambda_B541():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B541)
    Sleep(50)

    def lambda_B551():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B551)
    Sleep(50)

    def lambda_B561():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B561)
    Sleep(50)

    def lambda_B571():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B571)
    Sleep(50)

    def lambda_B581():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B581)
    Sleep(300)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)

    def lambda_B5A3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B5A3)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    def lambda_B5BA():
        OP_96(0xFE, 0xFFFFFE8E, 0x3B6, 0xFFFFCCFC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B5BA)

    ChrTalk(
        0x101,
        "#00001F#6P#N...Mariabell.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#NBell... Do you still\x01",
            "want to fight?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30WThere is nothing I can do.\x01",
            "The Sept-Terrion's power\x01",
            "has disappeared from KeA.\x02\x03",
            "Along with the firm\x01",
            "conviction of the Crois\x01",
            "clan spanning 1000 years.\x02\x03",
            "#10801FIt's really... a\x01",
            "disappointment...\x02",
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
            "#00206F#6P#NEven the cult\x01",
            "nightmare... Is it\x01",
            "really over?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10803F#5P#30WYes. However, more disasters lie\x01",
            "ahead for Crossbell.\x02\x03",
            "Erebonia, especially... Whichever\x01",
            "faction wins in the civil war, they\x01",
            "will very likely come to invade us.\x02\x03",
            "#10801FWhen that happens, Calvard will\x01",
            "dispatch its army to oppose them\x01",
            "for sure.\x02",
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
        "#00301F#12P#NIndeed...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8C5")
    OP_FC(0xFFF4)
    Jump("loc_B8C8")

    label("loc_B8C5")

    OP_FC(0xFFFA)

    label("loc_B8C8")


    ChrTalk(
        0x109,
        "#10108F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_B936")

    label("loc_B8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B936")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B915")
    OP_FC(0xFFF4)
    Jump("loc_B918")

    label("loc_B915")

    OP_FC(0xFFFA)

    label("loc_B918")


    ChrTalk(
        0x10A,
        "#00608F#13P............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B936")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WHowever, after losing the\x01",
            "Sept-Terrion, you have no\x01",
            "means to oppose them.\x02\x03",
            "#10800FYou understand that,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NEven so, we... We made this\x01",
            "decision with KeA.\x02\x03",
            "#00003FGetting over these barriers\x01",
            "together, to grasp the\x01",
            "light of tomorrow...\x02\x03",
            "#00000FThat's why─ We have no\x01",
            "regrets.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00202F#6P#NYes!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F#12P#N*giggle*. We're going to\x01",
            "be even busier than\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00304F#12P#NStill, we were only able to come\x01",
            "this far was because we went\x01",
            "through all sorts of hardships.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBB7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB6B")
    OP_FC(0xFFF4)
    Jump("loc_BB6E")

    label("loc_BB6B")

    OP_FC(0xFFFA)

    label("loc_BB6E")


    ChrTalk(
        0x109,
        (
            "#10100F#13PWe'll face them head-on,\x01",
            "and get through them\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BBB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBE1")
    OP_FC(0xFFF4)
    Jump("loc_BBE4")

    label("loc_BBE1")

    OP_FC(0xFFFA)

    label("loc_BBE4")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PThe value of the police\x01",
            "is going to questioned\x01",
            "more than ever as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BC3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC66")
    OP_FC(0xFFF4)
    Jump("loc_BC69")

    label("loc_BC66")

    OP_FC(0xFFFA)

    label("loc_BC69")


    ChrTalk(
        0x105,
        (
            "#10404F#13PHehe. I can't say anything careless\x01",
            "from my position, but...\x02\x03",
            "#10402FIt seems interference from the\x01",
            "Congregation for Divine Worship will\x01",
            "disappear, so the Church should be able\x01",
            "provide at least a little assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BD51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD7B")
    OP_FC(0xFFF4)
    Jump("loc_BD7E")

    label("loc_BD7B")

    OP_FC(0xFFFA)

    label("loc_BD7E")


    ChrTalk(
        0x106,
        (
            "#10704F#13PI will help too... To\x01",
            "the best of my ability.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_BDBD")


    ChrTalk(
        0xA,
        (
            "#10804F#5P#30WHehe... I can't handle\x01",
            "this any longer.\x02\x03",
            "#10802FWell, if that is the\x01",
            "case, do your best, all\x01",
            "right?\x02",
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
        "#00011F#6P#NMariabell!\x02",
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
            "#10804F#5P─Oh, about Mr. Grimwood. I\x01",
            "only put him in a temporary\x01",
            "state of apparent death.\x02\x03",
            "#10800FIf treated properly, he\x01",
            "will live.\x02",
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

    def lambda_C058():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C058)
    Sleep(50)

    def lambda_C068():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C068)
    Sleep(50)

    def lambda_C078():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C078)
    Sleep(50)

    def lambda_C088():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C088)
    Sleep(50)

    def lambda_C098():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C098)
    Sleep(50)

    def lambda_C0A8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_C0A8)
    Sleep(50)

    def lambda_C0B8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C0B8)
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

    def lambda_C139():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C139)
    Sleep(50)

    def lambda_C149():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C149)
    Sleep(50)

    def lambda_C159():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C159)
    Sleep(50)

    def lambda_C169():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C169)
    Sleep(50)

    def lambda_C179():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C179)
    Sleep(50)

    def lambda_C189():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_C189)
    Sleep(50)

    def lambda_C199():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C199)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0xA,
        (
            "#10804F#5PAnd because of the loss of the\x01",
            "Sept-Terrion's power, even this\x01",
            "Huge Tree will soon disappear.\x02\x03",
            "#10800FIt will be in a few hours...\x01",
            "See that you escape ASAP.\x02",
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
            "#10802F#5PHuhu. I had intended to leave\x01",
            "Crossbell, no matter how\x01",
            "things turned out.\x02\x03",
            "#10804FBecause I desired to serve the\x01",
            "Grandmaster of Ouroboros in\x01",
            "the stead of a missing Anguis.\x02",
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
        "#00007F#6P#NWha─\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NAnguis... The leaders of\x01",
            "Ouroboros?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12P#NBell... You...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10802F#5PUhuhu... Elie, don't make that\x01",
            "face.\x02\x03",
            "#10804FWith the continent having become\x01",
            "like this, there will be other\x01",
            "chances for us to meet again.\x02\x03",
            "#10800FUntil then, I will firmly watch,\x01",
            "from a distant land...\x02\x03",
            "Your vain struggle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N...Bell...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        "#05808F#6P#N...............\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10806F#5PAnd about my father...\x01",
            "Please spare him from\x01",
            "capital punishment.\x02\x03",
            "#10800FAfter all, he will be of\x01",
            "at least some use to you\x01",
            "in rebuilding Crossbell.\x02",
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
        (
            "#10809F#3800V#5P#40W#30AWell then, everyone─\x01",
            "Have a nice day.\x02",
        )
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
        "#00008F#5P#30W...............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C821")
    OP_FC(0x5)
    Jump("loc_C824")

    label("loc_C821")

    OP_FC(0xB)

    label("loc_C824")


    ChrTalk(
        0x102,
        (
            "#00106F#13P#30W...Bell... Selfish...\x01",
            "Until the very end...\x02",
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

    def lambda_C8C1():

        label("loc_C8C1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C8C1")

    QueueWorkItem2(0x9, 2, lambda_C8C1)
    Sleep(300)

    def lambda_C8D6():

        label("loc_C8D6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C8D6")

    QueueWorkItem2(0x102, 2, lambda_C8D6)
    Sleep(50)

    def lambda_C8EB():

        label("loc_C8EB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C8EB")

    QueueWorkItem2(0x103, 2, lambda_C8EB)
    Sleep(50)

    def lambda_C900():

        label("loc_C900")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C900")

    QueueWorkItem2(0x104, 2, lambda_C900)
    Sleep(50)

    def lambda_C915():

        label("loc_C915")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C915")

    QueueWorkItem2(0xF4, 2, lambda_C915)
    Sleep(50)

    def lambda_C92A():

        label("loc_C92A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C92A")

    QueueWorkItem2(0xF5, 2, lambda_C92A)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9BF")
    BeginChrThread(0x102, 0, 0, 84)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CB83")

    label("loc_C9BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9F7")
    BeginChrThread(0x102, 0, 0, 85)
    BeginChrThread(0x103, 0, 0, 84)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CB83")

    label("loc_C9F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA2F")
    BeginChrThread(0x102, 0, 0, 86)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 84)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CB83")

    label("loc_CA2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA79")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CA9D")

    label("loc_CA79")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CA9D")

    Jump("loc_CB83")

    label("loc_CAA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAEC")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CB10")

    label("loc_CAEC")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CB10")

    Jump("loc_CB83")

    label("loc_CB15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB83")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB5F")
    BeginChrThread(0x102, 0, 0, 87)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 84)
    BeginChrThread(0xF5, 0, 0, 88)
    BeginChrThread(0x9, 0, 0, 89)
    Jump("loc_CB83")

    label("loc_CB5F")

    BeginChrThread(0x102, 0, 0, 88)
    BeginChrThread(0x103, 0, 0, 85)
    BeginChrThread(0x104, 0, 0, 86)
    BeginChrThread(0xF4, 0, 0, 87)
    BeginChrThread(0xF5, 0, 0, 84)
    BeginChrThread(0x9, 0, 0, 89)

    label("loc_CB83")

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
            "#00004F#5P#30W...Yes. The wounds\x01",
            "really aren't fatal.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCBC")

    def lambda_CC5F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC5F)

    def lambda_CC6C():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CC6C)
    Sleep(50)

    def lambda_CC7C():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CC7C)
    Sleep(50)

    def lambda_CC8C():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CC8C)
    Sleep(50)

    def lambda_CC9C():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CC9C)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D048")

    label("loc_CCBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD2D")

    def lambda_CCD0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CCD0)

    def lambda_CCDD():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CCDD)
    Sleep(50)

    def lambda_CCED():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CCED)
    Sleep(50)

    def lambda_CCFD():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CCFD)
    Sleep(50)

    def lambda_CD0D():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CD0D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D048")

    label("loc_CD2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9E")

    def lambda_CD41():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CD41)

    def lambda_CD4E():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CD4E)
    Sleep(50)

    def lambda_CD5E():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CD5E)
    Sleep(50)

    def lambda_CD6E():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CD6E)
    Sleep(50)

    def lambda_CD7E():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CD7E)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D048")

    label("loc_CD9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE83")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE21")

    def lambda_CDC4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CDC4)

    def lambda_CDD1():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CDD1)
    Sleep(50)

    def lambda_CDE1():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CDE1)
    Sleep(50)

    def lambda_CDF1():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CDF1)
    Sleep(50)

    def lambda_CE01():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CE01)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CE7E")

    label("loc_CE21")


    def lambda_CE26():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CE26)

    def lambda_CE33():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CE33)
    Sleep(50)

    def lambda_CE43():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CE43)
    Sleep(50)

    def lambda_CE53():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CE53)
    Sleep(50)

    def lambda_CE63():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CE63)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_CE7E")

    Jump("loc_D048")

    label("loc_CE83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF06")

    def lambda_CEA9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CEA9)

    def lambda_CEB6():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CEB6)
    Sleep(50)

    def lambda_CEC6():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CEC6)
    Sleep(50)

    def lambda_CED6():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CED6)
    Sleep(50)

    def lambda_CEE6():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CEE6)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_CF63")

    label("loc_CF06")


    def lambda_CF0B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CF0B)

    def lambda_CF18():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF18)
    Sleep(50)

    def lambda_CF28():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CF28)
    Sleep(50)

    def lambda_CF38():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CF38)
    Sleep(50)

    def lambda_CF48():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_CF48)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_CF63")

    Jump("loc_D048")

    label("loc_CF68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D048")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFEB")

    def lambda_CF8E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_CF8E)

    def lambda_CF9B():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF9B)
    Sleep(50)

    def lambda_CFAB():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CFAB)
    Sleep(50)

    def lambda_CFBB():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CFBB)
    Sleep(50)

    def lambda_CFCB():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_CFCB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Jump("loc_D048")

    label("loc_CFEB")


    def lambda_CFF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_CFF0)

    def lambda_CFFD():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CFFD)
    Sleep(50)

    def lambda_D00D():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D00D)
    Sleep(50)

    def lambda_D01D():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D01D)
    Sleep(50)

    def lambda_D02D():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_D02D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)

    label("loc_D048")


    ChrTalk(
        0x101,
        (
            "#00000F#11PEveryone, let's split up\x01",
            "and carry Lawyer Ian to the\x01",
            "Merkabah.\x02\x03",
            "Also, we need to look after\x01",
            "Arios and the others and\x01",
            "carry them there as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D16F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D111")
    OP_FC(0xC)
    Jump("loc_D114")

    label("loc_D111")

    OP_FC(0x6)

    label("loc_D114")


    ChrTalk(
        0x10A,
        (
            "#00604F#13PBecause the Huge Tree\x01",
            "will collapse in a few\x01",
            "hours, we need to hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2A8")

    label("loc_D16F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D20E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D196")
    OP_FC(0x5)
    Jump("loc_D1B3")

    label("loc_D196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1B0")
    OP_FC(0xC)
    Jump("loc_D1B3")

    label("loc_D1B0")

    OP_FC(0x6)

    label("loc_D1B3")


    ChrTalk(
        0x106,
        (
            "#10700F#13PBecause the Huge Tree\x01",
            "will collapse in a few\x01",
            "hours, we need to hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2A8")

    label("loc_D20E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2A8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D235")
    OP_FC(0x5)
    Jump("loc_D252")

    label("loc_D235")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D24F")
    OP_FC(0xC)
    Jump("loc_D252")

    label("loc_D24F")

    OP_FC(0x6)

    label("loc_D252")


    ChrTalk(
        0x109,
        (
            "#10100F#13PBecause the Huge Tree\x01",
            "will collapse in a few\x01",
            "hours, we need to hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D33D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2CF")
    OP_FC(0x5)
    Jump("loc_D2EC")

    label("loc_D2CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2E9")
    OP_FC(0xC)
    Jump("loc_D2EC")

    label("loc_D2E9")

    OP_FC(0x6)

    label("loc_D2EC")


    ChrTalk(
        0x105,
        (
            "#10404F#13PLet's contact Abbas and\x01",
            "the others and have them\x01",
            "assist us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D461")

    label("loc_D33D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D364")
    OP_FC(0x5)
    Jump("loc_D381")

    label("loc_D364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D37E")
    OP_FC(0xC)
    Jump("loc_D381")

    label("loc_D37E")

    OP_FC(0x6)

    label("loc_D381")


    ChrTalk(
        0x109,
        (
            "#10104F#13PIt seems best to contact\x01",
            "the Merkabah and have\x01",
            "them assist us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D461")

    label("loc_D3D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D461")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3FC")
    OP_FC(0x5)
    Jump("loc_D419")

    label("loc_D3FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D416")
    OP_FC(0xC)
    Jump("loc_D419")

    label("loc_D416")

    OP_FC(0x6)

    label("loc_D419")


    ChrTalk(
        0x106,
        (
            "#10704F#13PWe should contact the\x01",
            "Merkabah and have them\x01",
            "assist us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D461")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D47B")
    OP_FC(0x5)
    Jump("loc_D47E")

    label("loc_D47B")

    OP_FC(0x6)

    label("loc_D47E")


    ChrTalk(
        0x103,
        (
            "#00206F#13PNevertheless...\x02\x03",
            "#00202FMariabell was Mariabell\x01",
            "until the very end, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4EE")
    OP_FC(0x5)
    Jump("loc_D4F1")

    label("loc_D4EE")

    OP_FC(0xC)

    label("loc_D4F1")


    ChrTalk(
        0x104,
        (
            "#00306F#13PYeah. Even though she did\x01",
            "what she did, somehow I\x01",
            "can't really hate her...\x02\x03",
            "#00302FCould that be another of\x01",
            "her natural virtues?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D599")
    OP_FC(0x6)
    Jump("loc_D646")

    label("loc_D599")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B0")
    OP_FC(0xC)
    Jump("loc_D646")

    label("loc_D5B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5D9")
    OP_FC(0xC)
    Jump("loc_D5DC")

    label("loc_D5D9")

    OP_FC(0x6)

    label("loc_D5DC")

    Jump("loc_D646")

    label("loc_D5E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D612")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D60A")
    OP_FC(0xC)
    Jump("loc_D60D")

    label("loc_D60A")

    OP_FC(0x6)

    label("loc_D60D")

    Jump("loc_D646")

    label("loc_D612")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D643")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D63B")
    OP_FC(0xC)
    Jump("loc_D63E")

    label("loc_D63B")

    OP_FC(0x6)

    label("loc_D63E")

    Jump("loc_D646")

    label("loc_D643")

    OP_FC(0x5)

    label("loc_D646")


    ChrTalk(
        0x102,
        (
            "#00106F#13PI think that maybe Bell... is being\x01",
            "completely honest to herself.\x02\x03",
            "#00103FOnce she sets her mind on doing\x01",
            "something, she tries to accomplish it by\x01",
            "any means, without a single hesitation...\x02\x03",
            "#00108FWithout even caring if she's alone...\x02\x03",
            "#00101FHowever... Not everyone is as strong as\x01",
            "Bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah, that's exactly why\x01",
            "man... needs family and\x01",
            "friends...\x02\x03",
            "#00008FTo get over barriers, in\x01",
            "order to grasp the light\x01",
            "of an unknown tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D82E")
    OP_FC(0x5)
    Jump("loc_D831")

    label("loc_D82E")

    OP_FC(0xC)

    label("loc_D831")


    ChrTalk(
        0x104,
        (
            "#00304F#13PWell, the time when we'll\x01",
            "be able to see that light\x01",
            "is still far off, but...\x02\x03",
            "#00300FEven so, I've got the\x01",
            "feelin' we'll get by,\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8E4")
    OP_FC(0x5)
    Jump("loc_D8E7")

    label("loc_D8E4")

    OP_FC(0x6)

    label("loc_D8E7")


    ChrTalk(
        0x103,
        "#00214F#13PRight!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB1B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D925")
    OP_FC(0x5)
    Jump("loc_D942")

    label("loc_D925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D93F")
    OP_FC(0xC)
    Jump("loc_D942")

    label("loc_D93F")

    OP_FC(0x6)

    label("loc_D942")


    ChrTalk(
        0x109,
        (
            "#10102F#13PWere able to do this\x01",
            "much with just the\x01",
            "people standing here!\x02\x03",
            "#10109FIf the people of\x01",
            "Crossbell unite, they\x01",
            "can do anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA4E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9F7")
    OP_FC(0x5)
    Jump("loc_DA14")

    label("loc_D9F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA11")
    OP_FC(0xC)
    Jump("loc_DA14")

    label("loc_DA11")

    OP_FC(0x6)

    label("loc_DA14")


    ChrTalk(
        0x105,
        (
            "#10404F#13PHehe. You might be right\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB16")

    label("loc_DA4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAC9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA75")
    OP_FC(0x5)
    Jump("loc_DA92")

    label("loc_DA75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA8F")
    OP_FC(0xC)
    Jump("loc_DA92")

    label("loc_DA8F")

    OP_FC(0x6)

    label("loc_DA92")


    ChrTalk(
        0x106,
        (
            "#10709F#13PHaha... Indeed, that may\x01",
            "be true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB16")

    label("loc_DAC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAF3")
    OP_FC(0xC)
    Jump("loc_DAF6")

    label("loc_DAF3")

    OP_FC(0x6)

    label("loc_DAF6")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph... Indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_DB16")

    Jump("loc_DDF6")

    label("loc_DB1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCE0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB42")
    OP_FC(0x5)
    Jump("loc_DB5F")

    label("loc_DB42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB5C")
    OP_FC(0xC)
    Jump("loc_DB5F")

    label("loc_DB5C")

    OP_FC(0x6)

    label("loc_DB5F")


    ChrTalk(
        0x105,
        (
            "#10404F#13PWell, with just the people we\x01",
            "have here we were able to do\x01",
            "this much.\x02\x03",
            "#10402FIf all the forces in Crossbell\x01",
            "join together, won't they be\x01",
            "able to make it, somehow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC8E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC3A")
    OP_FC(0x5)
    Jump("loc_DC57")

    label("loc_DC3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC54")
    OP_FC(0xC)
    Jump("loc_DC57")

    label("loc_DC54")

    OP_FC(0x6)

    label("loc_DC57")


    ChrTalk(
        0x106,
        (
            "#10709F#13PHaha... Indeed, that may\x01",
            "be true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCDB")

    label("loc_DC8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCDB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCB8")
    OP_FC(0xC)
    Jump("loc_DCBB")

    label("loc_DCB8")

    OP_FC(0x6)

    label("loc_DCBB")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph... Indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_DCDB")

    Jump("loc_DDF6")

    label("loc_DCE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF7")
    OP_FC(0x5)
    Jump("loc_DD14")

    label("loc_DCF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD11")
    OP_FC(0xC)
    Jump("loc_DD14")

    label("loc_DD11")

    OP_FC(0x6)

    label("loc_DD14")


    ChrTalk(
        0x106,
        (
            "#10704F#13P...With just the people here\x01",
            "we were able to do this\x01",
            "much.\x02\x03",
            "#10702FIf we join together with the\x01",
            "forces in Crossbell, I feel\x01",
            "like we can do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDD3")
    OP_FC(0xC)
    Jump("loc_DDD6")

    label("loc_DDD3")

    OP_FC(0x6)

    label("loc_DDD6")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph... Indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_DDF6")

    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 90)
    WaitChrThread(0x9, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#05821F#3655V#5P#40W#40AKeA too... KeA will do\x01",
            "her best too!\x02\x03",
            "#05819F#3656V#40ATo protect this precious\x01",
            "place... with everyone!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA8")
    OP_FC(0x6)
    Jump("loc_DF55")

    label("loc_DEA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEBF")
    OP_FC(0xC)
    Jump("loc_DF55")

    label("loc_DEBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEF0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEE8")
    OP_FC(0xC)
    Jump("loc_DEEB")

    label("loc_DEE8")

    OP_FC(0x6)

    label("loc_DEEB")

    Jump("loc_DF55")

    label("loc_DEF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF19")
    OP_FC(0xC)
    Jump("loc_DF1C")

    label("loc_DF19")

    OP_FC(0x6)

    label("loc_DF1C")

    Jump("loc_DF55")

    label("loc_DF21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF4A")
    OP_FC(0xC)
    Jump("loc_DF4D")

    label("loc_DF4A")

    OP_FC(0x6)

    label("loc_DF4D")

    Jump("loc_DF55")

    label("loc_DF52")

    OP_FC(0x5)

    label("loc_DF55")


    ChrTalk(
        0x102,
        "#00102F#3410V#13P#30W#25AKeA...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF94")
    OP_FC(0x5)
    Jump("loc_DF97")

    label("loc_DF94")

    OP_FC(0x6)

    label("loc_DF97")


    ChrTalk(
        0x103,
        (
            "#00204F#2697V#13P#30W#25AWith you, we will have\x01",
            "the strength of a\x01",
            "thousand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E002")
    OP_FC(0x5)
    Jump("loc_E005")

    label("loc_E002")

    OP_FC(0xC)

    label("loc_E005")


    ChrTalk(
        0x104,
        "#00309F#2777V#13P#30W#25AHaha, that's the spirit!\x02",
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
        (
            "#00009F#3337V#11P#30AYeah, let's do our best\x01",
            "together.\x02",
        )
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
            "#00004F#3338V#11P#30W#30A─Special Support Section,\x01",
            "withdraw.\x02\x03",
            "#3339V#11P#30W#45ALet's recover Arios and the\x01",
            "others and withdraw from the\x01",
            "Huge Tree in the Merkabah.\x02",
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
        (
            "#00000F#3340V#11P#30W#35ALet's return, to our\x01",
            "Crossbell!\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3FC")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "EXTRA Mode has been\x01",
            "unlocked.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "You can access EXTRA\x01",
            "Mode from the Title\x01",
            "Screen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_E3FC")

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

    # Function_71_A20E end

    def Function_72_E4F0(): pass

    label("Function_72_E4F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)), "loc_E536")
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
    Jump("Function_72_E4F0")

    label("loc_E536")

    Return()

    # Function_72_E4F0 end

    def Function_73_E537(): pass

    label("Function_73_E537")

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

    # Function_73_E537 end

    def Function_74_E595(): pass

    label("Function_74_E595")

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

    # Function_74_E595 end

    def Function_75_E5C0(): pass

    label("Function_75_E5C0")

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

    # Function_75_E5C0 end

    def Function_76_E5EB(): pass

    label("Function_76_E5EB")

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

    # Function_76_E5EB end

    def Function_77_E60F(): pass

    label("Function_77_E60F")

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

    # Function_77_E60F end

    def Function_78_E663(): pass

    label("Function_78_E663")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E675")
    Sleep(50)

    label("loc_E675")

    OP_9B(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
    Return()

    # Function_78_E663 end

    def Function_79_E685(): pass

    label("Function_79_E685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E697")
    Sleep(100)

    label("loc_E697")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_79_E685 end

    def Function_80_E6A7(): pass

    label("Function_80_E6A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6B9")
    Sleep(150)

    label("loc_E6B9")

    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    Return()

    # Function_80_E6A7 end

    def Function_81_E6C9(): pass

    label("Function_81_E6C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6ED")
    Sleep(200)

    label("loc_E6ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E711")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E711")
    Sleep(200)

    label("loc_E711")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E735")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E735")
    Sleep(200)

    label("loc_E735")

    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_81_E6C9 end

    def Function_82_E745(): pass

    label("Function_82_E745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E769")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E769")
    Sleep(250)

    label("loc_E769")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E78D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E78D")
    Sleep(250)

    label("loc_E78D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7B1")
    Sleep(250)

    label("loc_E7B1")

    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0xFA0, 0x0)
    Return()

    # Function_82_E745 end

    def Function_83_E7C1(): pass

    label("Function_83_E7C1")

    TurnDirection(0xFE, 0x8, 500)
    Sleep(450)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x1964, 0x7D0, 0x0)
    Return()

    # Function_83_E7C1 end

    def Function_84_E808(): pass

    label("Function_84_E808")

    Sleep(200)
    OP_96(0xFE, 0x1C5C, 0x3B6, 0xFFFFDD14, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_84_E808 end

    def Function_85_E827(): pass

    label("Function_85_E827")

    Sleep(1100)
    OP_96(0xFE, 0x16A8, 0x406, 0xFFFFDC60, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_85_E827 end

    def Function_86_E846(): pass

    label("Function_86_E846")

    Sleep(50)
    OP_96(0xFE, 0x1F04, 0x3B6, 0xFFFFD1D4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_86_E846 end

    def Function_87_E865(): pass

    label("Function_87_E865")

    Sleep(350)
    OP_96(0xFE, 0x19C8, 0x3B6, 0xFFFFD210, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_87_E865 end

    def Function_88_E884(): pass

    label("Function_88_E884")

    Sleep(1450)
    OP_96(0xFE, 0x1608, 0x3B6, 0xFFFFD670, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_88_E884 end

    def Function_89_E8A3(): pass

    label("Function_89_E8A3")

    Sleep(750)
    OP_9B(0x1, 0xFE, 0x0, 0x4E2, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1C52, 0x1388, 0x1)
    Sound(811, 0, 70, 0)
    Sound(898, 0, 50, 0)

    def lambda_E8D5():
        OP_A6(0xFE, 0x64, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E8D5)
    Sleep(50)

    def lambda_E8F1():
        OP_A6(0xFE, 0x32, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E8F1)
    Sleep(450)
    OP_9B(0x1, 0xFE, 0x109, 0x96, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_89_E8A3 end

    def Function_90_E91F(): pass

    label("Function_90_E91F")

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

    # Function_90_E91F end

    def Function_91_E964(): pass

    label("Function_91_E964")

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

    # Function_91_E964 end

    def Function_92_E9EE(): pass

    label("Function_92_E9EE")

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

    # Function_92_E9EE end

    def Function_93_EA66(): pass

    label("Function_93_EA66")

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

    # Function_93_EA66 end

    def Function_94_EA8A(): pass

    label("Function_94_EA8A")

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

    # Function_94_EA8A end

    def Function_95_EAAE(): pass

    label("Function_95_EAAE")

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

    # Function_95_EAAE end

    def Function_96_EAD2(): pass

    label("Function_96_EAD2")

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

    # Function_96_EAD2 end

    def Function_97_EAFC(): pass

    label("Function_97_EAFC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_EB1E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EB1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_EB36")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EB36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_EB4E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EB4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB71")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EB71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB94")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EB94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBB7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EBB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EBD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EBF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EC11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC3A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EC3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC63")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC87")

    label("loc_EC63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC87")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC87")

    Return()

    # Function_97_EAFC end

    SaveToFile()

Try(main)
