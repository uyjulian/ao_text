from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1490.bin",                # FileName
        "t1490",                    # MapName
        "t1490",                    # Location
        0x00BB,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1490",                  # 0
        "Marybele",             # 1
        "Secretary Arios",           # 2
        "Keya",                 # 3
        "Defense Forces soldier",             # 4
        "Defense Forces soldier",             # 5
        "Defense Forces soldier",             # 6
        "Defense Forces soldier",             # 7
        "Defense Forces soldier",             # 8
        "Defense Forces soldier",             # 9
        "Defense Forces soldier",             # 10
        "Defense Forces soldier",             # 11
        "Lieutenant Noel",             # 12
        "Image",                   # 13
        "Image",                   # 14
        "Image",                   # 15
        "Image",                   # 16
        "Image",                   # 17
        "SE control",                 # 18
        "bt1430",                 # 19
        "bt1430",                 # 20
    ))

    ATBonus("ATBonus_2BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_3E0", 0x1142, 3, 6, 45, 3, 3, 30, 0, "bt1430", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_37C", "ed7540", "ed7453", "ATBonus_2BC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_39C", 0x1162, 3, 6, 45, 3, 3, 30, 0, "bt1430", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_37C", "ed7540", "ed7453", "ATBonus_2BC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294957296, 5000,    8500,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294960796, 6349,    8300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(10000,   5000,    8500,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(6500,    6349,    8300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294967196, 10699,   9300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1356, 0)                                       # 0

    ScpFunction((
        "Function_0_54C",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_650",          # 02, 2
        "Function_3_70A",          # 03, 3
        "Function_4_7C4",          # 04, 4
        "Function_5_87E",          # 05, 5
        "Function_6_2B7E",         # 06, 6
        "Function_7_2BEA",         # 07, 7
        "Function_8_2C56",         # 08, 8
        "Function_9_2CBC",         # 09, 9
        "Function_10_2D28",        # 0A, 10
        "Function_11_2D4A",        # 0B, 11
        "Function_12_2D6C",        # 0C, 12
        "Function_13_2D8E",        # 0D, 13
        "Function_14_2DB0",        # 0E, 14
        "Function_15_2DD2",        # 0F, 15
        "Function_16_2DE2",        # 10, 16
        "Function_17_2DF2",        # 11, 17
        "Function_18_2E02",        # 12, 18
        "Function_19_2E12",        # 13, 19
        "Function_20_2E22",        # 14, 20
        "Function_21_2E3D",        # 15, 21
        "Function_22_2E4F",        # 16, 22
        "Function_23_38BB",        # 17, 23
        "Function_24_393E",        # 18, 24
        "Function_25_395E",        # 19, 25
        "Function_26_3988",        # 1A, 26
        "Function_27_39B2",        # 1B, 27
        "Function_28_39DC",        # 1C, 28
        "Function_29_3A1C",        # 1D, 29
        "Function_30_3A38",        # 1E, 30
        "Function_31_4448",        # 1F, 31
        "Function_32_62D1",        # 20, 32
        "Function_33_631C",        # 21, 33
        "Function_34_633B",        # 22, 34
        "Function_35_635A",        # 23, 35
        "Function_36_64B9",        # 24, 36
        "Function_37_650B",        # 25, 37
        "Function_38_6560",        # 26, 38
        "Function_39_658C",        # 27, 39
        "Function_40_65B8",        # 28, 40
        "Function_41_66BB",        # 29, 41
        "Function_42_6714",        # 2A, 42
        "Function_43_6767",        # 2B, 43
        "Function_44_67BA",        # 2C, 44
        "Function_45_680D",        # 2D, 45
        "Function_46_6827",        # 2E, 46
        "Function_47_6841",        # 2F, 47
        "Function_48_6854",        # 30, 48
        "Function_49_687F",        # 31, 49
        "Function_50_78D1",        # 32, 50
        "Function_51_78F1",        # 33, 51
        "Function_52_7931",        # 34, 52
        "Function_53_796B",        # 35, 53
        "Function_54_79A5",        # 36, 54
        "Function_55_79E5",        # 37, 55
        "Function_56_7A1F",        # 38, 56
        "Function_57_7A5F",        # 39, 57
        "Function_58_7A99",        # 3A, 58
        "Function_59_7AD9",        # 3B, 59
        "Function_60_7B15",        # 3C, 60
        "Function_61_7B51",        # 3D, 61
        "Function_62_7B87",        # 3E, 62
        "Function_63_7BC3",        # 3F, 63
        "Function_64_7BD3",        # 40, 64
        "Function_65_7C0E",        # 41, 65
        "Function_66_7C49",        # 42, 66
        "Function_67_7C84",        # 43, 67
        "Function_68_7CBF",        # 44, 68
        "Function_69_7CFA",        # 45, 69
        "Function_70_7D35",        # 46, 70
        "Function_71_7D70",        # 47, 71
        "Function_72_7DAB",        # 48, 72
        "Function_73_7DDE",        # 49, 73
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_581")
    SetScenarioFlags(0x0, 0)
    Event(0, 5)

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_595")
    ClearScenarioFlags(0x22, 0)
    Event(0, 22)
    Jump("loc_5CF")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5A9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 30)
    Jump("loc_5CF")

    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_5BD")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)
    Jump("loc_5CF")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_5CF")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 1)
    Event(0, 49)

    label("loc_5CF")

    Return()

    # Function_0_54C end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5FF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_617")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_617")
    SetScenarioFlags(0x0, 2)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_617")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_649")
    OP_24(0x39F)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_64F")

    label("loc_649")

    Sound(927, 1, 80, 0)

    label("loc_64F")

    Return()

    # Function_1_5D0 end

    def Function_2_650(): pass

    label("Function_2_650")

    SetMapObjFrame(0xFF, "floor03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x0, 0x1)
    Return()

    # Function_2_650 end

    def Function_3_70A(): pass

    label("Function_3_70A")

    SetMapObjFrame(0xFF, "floor03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x1, 0x1)
    Return()

    # Function_3_70A end

    def Function_4_7C4(): pass

    label("Function_4_7C4")

    SetMapObjFrame(0xFF, "floor03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x1, 0x1)
    Return()

    # Function_4_7C4 end

    def Function_5_87E(): pass

    label("Function_5_87E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("apl/ch51529.itc", 0x22)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05800.itp")
    LoadEffect(0x0, "event\\ev15050.eff")
    SoundLoad(3719)
    SoundLoad(3398)
    SoundLoad(3399)
    SoundLoad(3400)
    SoundLoad(3321)
    SoundLoad(3780)
    SoundLoad(3781)
    SoundLoad(3782)
    SoundLoad(3783)
    SoundLoad(3625)
    SetChrPos(0x101, 0, -2000, -41500, 0)
    SetChrPos(0x102, -1000, -2000, -41500, 0)
    SetChrPos(0x103, 1000, -2000, -41500, 0)
    SetChrPos(0x104, 0, -2000, -41500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 180)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x14)
    OP_78(0x1, 0x15)
    OP_78(0x2, 0x16)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "m_face2", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face3", 0x0, 0x1)
    Call(0, 3)
    OP_68(0, 1000, -36000, 0)
    MoveCamera(145, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    FadeToBright(1000, 0)
    OP_68(0, -300, -36000, 6000)
    SetCameraDistance(16500, 6000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 8)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 9)
    WaitChrThread(0x101, 3)
    StopBGM(0xFA0)
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4S!!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -300, -26000, 2000)
    MoveCamera(135, 16, 0, 2000)
    SetCameraDistance(15000, 2000)

    def lambda_BC4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC4)
    Sleep(50)

    def lambda_BDC():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BDC)
    Sleep(50)

    def lambda_BF4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF4)
    Sleep(50)

    def lambda_C0C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00201F#11PT-this is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11POi oi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PWhy…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(1000)
    Call(0, 2)
    OP_68(0, 4000, -19000, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40000, 0)
    OP_68(0, 4000, 5000, 12000)
    MoveCamera(0, 15, 0, 12000)
    SetCameraDistance(35000, 12000)
    Sleep(1000)

    def lambda_CF9():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF9)
    Sleep(50)

    def lambda_D11():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D11)
    Sleep(50)

    def lambda_D29():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D29)
    Sleep(50)

    def lambda_D41():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D41)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 1400, 5000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3300, 5000, 4000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00007F#3321V#30W#20AKa au!\x01",
            "Mr. Arios …!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107F#3398V#30W#15ABelle!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        "#3625V#40WLloyd… guys…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE29)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#10503F#5P#30W….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#10804F#3780V#5P#30WGiggle\x01",
            "I finally arrived.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC4)
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    ChrTalk(
        0x102,
        "#00106F#3399V#11P#40WBelle, why..\x02",
    )

    CloseMessageWindow()
    OP_24(0xD47)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x102,
        (
            "#00107F#3400V#11P#4S#30WHow come you\x01",
            "You are in such a place! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD48)
    Fade(500)
    Call(0, 2)
    OP_68(-510, 3300, 2670, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16740, 0)
    SetCameraDistance(15740, 1500)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#3781V#30WEhe, it's a simple matter\x02\x03",
            "#3782VI inherited \"great treasure\"\x01",
            "As descendants of the Clois family ……\x02\x03",
            "#3783VNaturally responsible\x01",
            "Just playing it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xEC7)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(300)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#11PThe Great Master…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PNo way it appeared in Libert\x01",
            "\"Shining ring#6RAuriol#\"And the same kind …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10809F#5PEhe, you already know!\x02\x03",
            "#10804FLong ago, goddess gave to man\x01",
            "\"The treasure of seven#8RSept-Terion#\"… ….\x02\x03",
            "#10811FOne of them,\x01",
            "Our family inherited.\x02\x03",
            "Well, that was 1200 years ago\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11P…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PI don't really get it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PHuff, due to unfortunate events\x01",
            "The treasure of the goddess was lost.\x02\x03",
            "#10803FAs a result, the founder of the Clois family\x01",
            "To regain treasure\x01",
            "I envisioned a tremendously far-reaching plan … …\x02\x03",
            "#10800FHuge in this crossbell land\x01",
            "I decided to build an \"expression\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PA large \"ceremony\"…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PNo way I used a power net\x01",
            "Mysterious and huge system … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10803F#5PYes, with modern dynamics technology\x01",
            "Fusion of Alchemy of the Cloyce family\x01",
            "The \"magical science\" created … …\x02\x03",
            "#10802FIt was finally realized\x01",
            "It is a stupid huge \"formula\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PA ceremony of magical science..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#11PAnd Alchemy..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……Really……\x01",
            "Was it such a thing?\x02\x03",
            "#00008FOnce the \"Tower of Hoshi\" was built,\x01",
            "He provided technology to the \"cult\"\x01",
            "A group of alchemists ……\x02\x03",
            "#00007F── That you ladies\x01",
            "It was about the Clois family! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00305F#11PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PBut,\x01",
            "Tsujiki goes well with that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PWell then\x01",
            "Ka'a was sleeping.\x01",
            "That \"cradle#4RCradle#\"Because … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 1000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#10804F#5POf course, Clois family\x01",
            "It was provided to the \"cult\".\x02\x03",
            "#10811F─ ─ We give them the object of faith,\x01",
            "To make it work comfortably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05808F#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00013F#11PWell then,\x01",
            "What is \"D∴G Church\" … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PTo reach the purpose of the Clois family\x01",
            "It was derived from the shadow …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PYes, puppet#4RPicture#That's why.\x02\x03",
            "#10811FKuku …… but most of them\x01",
            "I guess there was no consciousness.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x8,
        (
            "#10809F#5PHuff, the approximate background is\x01",
            "Could you please swallow it?\x02\x03",
            "#10805F─ ─ Oh, by the way\x01",
            "Mr. Arios here\x01",
            "It has nothing to do with my family.\x02\x03",
            "#10804FTo this time our plan\x01",
            "I agreed\x01",
            "It is a dependable collaborator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10503F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11PArios..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P…… Anta, sane?\x01",
            "To such a delusional story ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5PHa. Dellusional\x02\x03",
            "#10502FCertainly on that point\x01",
            "I agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10801F#6Poh dear……!\x01",
            "It is terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PBut they have that power,\x01",
            "If this situation can be changed …\x02\x03",
            "I do not care how much\x01",
            "I just attend to that illusion.\x02\x03",
            "#10501F─ ─ Even if the will of the goddess\x01",
            "Even if it goes against you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PNo way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PWhy in the world…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    OP_A1(0x101, 0x3E8, 0x2, 0x1, 0x2)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#11P…… To be honest, with just tremendous story\x01",
            "I have not organized it yet ….\x02\x03",
            "#00003FBut I can say this\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0x101, 0x514, 0x2, 0x3, 0x4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00010F#11PIt involves Ka'a in that delusion\x01",
            "Absolutely not allowed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -10400, 500)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_6F(0x79)
    Sleep(300)
    Fade(250)
    SetCameraDistance(16200, 300)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    OP_A1(0x101, 0x3E8, 0x2, 0x6, 0x7)
    OP_6F(0x79)
    OP_0D()
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#11P#4SKEA, WE'RE GOING BACK!\x02\x03",
            "#3SWhat do you suggest?#2RIs it?#I do not know if it was done\x01",
            "Ka'a would be Ka ah! Is it?\x02\x03",
            "Have such a hot face ……\x01",
            "There is nothing to sit on such a chair!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 1000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#05812F#5P#30WLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PEhe, KeA\x02\x03",
            "Like that, Lloyd is\x01",
            "I am telling you ….\x02\x03",
            "#10811Fwhat will you do#8R噵 噵 噵 噵#Are you going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05808F#5P#30W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(14000, 15000)
    OP_0D()
    Sleep(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    Sleep(800)
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x101,
        "#00011FKeA?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00105FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 170, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00307F#4SKeA! There's nothing to be confused about!\x02\x03",
            "Always like\x01",
            "Dive into the chest of Lloyd!\x02\x03",
            "That's the best, for you\x01",
            "I guess it can be safe! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        "#05812F#5P#30WRandy…\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00104F… That's right.\x01",
            "I guess there are circumstances … …\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FMore important than that\x01",
            "I definitely do not think so.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#05808F#5P#30WElie…Tio…\x02\x03",
            "#05814F#40W…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(921, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 3400, 7500, 0)
    MoveCamera(30, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Voice of a boy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3719V#30WUhufu …\x01",
            "Is not it excited?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE87)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-8000, 5500, 8400, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 11)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(8000, 5500, 8400, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x16, 3, 0, 12)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 5200, 7000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(32000, 4000)
    Sleep(500)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00110F#11P\"Eating snake#10RUroboros#\"……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PSo they are involved…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#10804F#5PCooperative relationship with each other\x01",
            "I'm just tying you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10802F#11P── Everyone.\x01",
            "Are you ready already?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(0, 5200, 7000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    SetMessageWindowPos(80, 120, -1, -1)
    SetChrName("Dr. Novartis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, of course\x02\x03",
            "To the satisfactory performance\x01",
            "I think it's finished?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(280, 135, -1, -1)
    SetChrName("Ariane Road")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The \"Bell\" is also prepared\x02\x03",
            "All we need is the Key there\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 150, -1, -1)
    SetChrName("Campanella")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Until they agree\x01",
            "I can wait ……\x02\x03",
            "But it's almost time\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-1500, 3000, 3800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#10800F#11POh now\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10501F#5PAre you coming?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#11PWhat are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PWhat is it time for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PIt's obvious.\x02\x03",
            "#10501FThe invasion of the Empire and the Republic\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4S!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#11PAh!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#10809F#5PBecause it's cheap\x01",
            "Shall I make it live?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(300)
    OP_68(0, 9400, 5500, 5000)
    MoveCamera(0, -15, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19000, 5000)
    OP_6F(0x79)
    BeginChrThread(0x18, 3, 0, 14)
    Sleep(2000)
    StopSound(927, 1000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t2100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_87E end

    def Function_6_2B7E(): pass

    label("Function_6_2B7E")


    def lambda_2B83():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B83)

    def lambda_2B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B98)
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_2B7E end

    def Function_7_2BEA(): pass

    label("Function_7_2BEA")


    def lambda_2BEF():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BEF)

    def lambda_2C04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C04)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_2BEA end

    def Function_8_2C56(): pass

    label("Function_8_2C56")


    def lambda_2C5B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C5B)

    def lambda_2C70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C70)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_2C56 end

    def Function_9_2CBC(): pass

    label("Function_9_2CBC")


    def lambda_2CC1():
        OP_9B(0x0, 0xFE, 0x0, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CC1)

    def lambda_2CD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CD6)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_2CBC end

    def Function_10_2D28(): pass

    label("Function_10_2D28")

    OP_71(0x0, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_10_2D28 end

    def Function_11_2D4A(): pass

    label("Function_11_2D4A")

    OP_71(0x1, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_11_2D4A end

    def Function_12_2D6C(): pass

    label("Function_12_2D6C")

    OP_71(0x2, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_12_2D6C end

    def Function_13_2D8E(): pass

    label("Function_13_2D8E")

    OP_71(0x3, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x3)
    OP_71(0x3, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_13_2D8E end

    def Function_14_2DB0(): pass

    label("Function_14_2DB0")

    OP_71(0x4, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_14_2DB0 end

    def Function_15_2DD2(): pass

    label("Function_15_2DD2")

    OP_71(0x0, 0xF5, 0x12C, 0x0, 0x8)
    OP_79(0x0)
    Return()

    # Function_15_2DD2 end

    def Function_16_2DE2(): pass

    label("Function_16_2DE2")

    OP_71(0x1, 0xFA, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    Return()

    # Function_16_2DE2 end

    def Function_17_2DF2(): pass

    label("Function_17_2DF2")

    OP_71(0x2, 0xFF, 0x12C, 0x0, 0x8)
    OP_79(0x2)
    Return()

    # Function_17_2DF2 end

    def Function_18_2E02(): pass

    label("Function_18_2E02")

    OP_71(0x3, 0x104, 0x12C, 0x0, 0x8)
    OP_79(0x3)
    Return()

    # Function_18_2E02 end

    def Function_19_2E12(): pass

    label("Function_19_2E12")

    OP_71(0x4, 0x10E, 0x12C, 0x0, 0x8)
    OP_79(0x4)
    Return()

    # Function_19_2E12 end

    def Function_20_2E22(): pass

    label("Function_20_2E22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3C")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_20_2E22")

    label("loc_2E3C")

    Return()

    # Function_20_2E22 end

    def Function_21_2E3D(): pass

    label("Function_21_2E3D")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_21_2E3D end

    def Function_22_2E4F(): pass

    label("Function_22_2E4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    SoundLoad(852)
    SoundLoad(825)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 180)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x14)
    OP_78(0x1, 0x15)
    OP_78(0x2, 0x16)
    OP_78(0x3, 0x17)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    SetMapObjFrame(0x4, "m_face1", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face3", 0x0, 0x1)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 9400, 5500, 0)
    MoveCamera(0, -15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 4000)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00110FN-no way!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x104,
        "#00311FThey came already\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FHowever, with the force of the guard\x01",
            "Let's stop it … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(921, 0, 80, 0)
    Sleep(500)
    Fade(500)
    OP_68(0, 3400, 7500, 0)
    MoveCamera(330, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── The key that can overturn it is\x01",
            "That is why.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(6500, 6350, 8300, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 13)
    WaitChrThread(0x17, 3)
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010F#11PPresident Dieter…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PSir…\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Men of \"association\".\x01",
            "We appreciate your cooperation in the plan.\x02\x03",
            "Arios also to the bell.\x01",
            "Apparently it seems to be on schedule?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#10804F#5PYes, so far\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5P…… Afterwards to her\x01",
            "There is no choice but to leave it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(1700, 3400, 9440, 0)
    MoveCamera(326, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 1500)
    SetCameraDistance(24500, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(230, 150, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's as you heard, KeA\x02\x03",
            "You understand, right?\x02\x03",
            "I can do something about this\x01",
            "There is only you#12R噵 噵 噵 噵 噵 噵#That being\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_63(0xA, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xA,
        "#05803F#5P#30W… (nod)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7585", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x249), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 5000)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(928, 0, 50, 0)
    Sound(852, 2, 100, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x1)
    BeginChrThread(0xA, 3, 0, 24)
    WaitChrThread(0xA, 3)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    Sound(825, 2, 50, 0)
    OP_0D()
    Fade(1000)
    OP_68(0, 3900, 10000, 0)
    OP_68(0, 7900, 10000, 3000)
    MoveCamera(0, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    BeginChrThread(0x19, 1, 0, 29)
    BeginChrThread(0x14, 3, 0, 15)
    BeginChrThread(0x15, 3, 0, 16)
    BeginChrThread(0x16, 3, 0, 17)
    BeginChrThread(0x17, 3, 0, 18)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(1300)
    Sound(147, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 25)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_25(0x339, 0x3C)
    OP_68(0, -2000, 7500, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(39000, 0)
    OP_68(0, 7000, 7500, 10000)
    Sleep(750)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)
    Sleep(2000)
    BeginChrThread(0xA, 3, 0, 27)
    WaitChrThread(0xA, 3)
    Sleep(4000)
    OP_0D()
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10500, 0)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(833, 0, 100, 0)
    OP_11(0x53, 0x59, 0x88, 0x2D, 0x78, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 3900, 7500, 1000)
    MoveCamera(0, 4, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(84250, 1000)
    Sleep(1000)
    CancelBlur(1000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(1000)
    OP_68(0, 4900, 4000, 0)
    OP_68(0, 3900, 4000, 2500)
    MoveCamera(325, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_11(0x53, 0x59, 0x88, 0xF, 0x78, 0x0)
    OP_6F(0x79)
    OP_0D()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10811F#5PAhah, good girl\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    Sound(357, 0, 100, 0)
    StopSound(852, 1000, 100)
    PlayEffect(0x0, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 20)
    Sleep(1300)
    StopSound(825, 2000, 70)
    StopSound(927, 2000, 70)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_24(0x354)
    OP_24(0x339)
    SetScenarioFlags(0x22, 0)
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_2E4F end

    def Function_23_38BB(): pass

    label("Function_23_38BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38EB")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_3935")

    label("loc_38EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3910")
    OP_82(0xA, 0x1E, 0xBB8, 0x1F4)
    Jump("loc_3935")

    label("loc_3910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3935")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_3935")

    label("loc_3935")

    Sleep(500)
    Jump("Function_23_38BB")

    label("loc_393D")

    Return()

    # Function_23_38BB end

    def Function_24_393E(): pass

    label("Function_24_393E")

    SetMapObjFrame(0xFF, "chair", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    Return()

    # Function_24_393E end

    def Function_25_395E(): pass

    label("Function_25_395E")

    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on_ani")
    Sleep(1133)
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    Return()

    # Function_25_395E end

    def Function_26_3988(): pass

    label("Function_26_3988")

    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    Return()

    # Function_26_3988 end

    def Function_27_39B2(): pass

    label("Function_27_39B2")

    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_27_39B2 end

    def Function_28_39DC(): pass

    label("Function_28_39DC")

    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_28_39DC end

    def Function_29_3A1C(): pass

    label("Function_29_3A1C")

    Sleep(500)
    Sound(162, 0, 100, 0)
    Sleep(400)
    Sound(162, 0, 100, 0)
    Sleep(300)
    Sound(162, 0, 100, 0)
    Return()

    # Function_29_3A1C end

    def Function_30_3A38(): pass

    label("Function_30_3A38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("apl/ch51530.itc", 0x22)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch03850.itc", 0x2B)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    SoundLoad(931)
    SoundLoad(832)
    SoundLoad(533)
    SoundLoad(932)
    SoundLoad(4055)
    SoundLoad(4056)
    SoundLoad(4057)
    SoundLoad(3401)
    SoundLoad(3322)
    SoundLoad(2766)
    SoundLoad(2684)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 90)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    Sound(832, 2, 70, 0)
    PlayEffect(0x0, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 20)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Call(0, 28)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    Sound(931, 2, 10, 0)
    Sound(832, 2, 40, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22500, 5500)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_25(0x340, 0x1E)
    Call(0, 3)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4SKeA, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PBele, please stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PI do not know what it is\x01",
            "Can I miss it …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PTentatively …\x01",
            "I will stop you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -8500, 1000)

    def lambda_3DE1():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DE1)
    Sleep(50)

    def lambda_3DF9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DF9)
    Sleep(50)

    def lambda_3E11():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E11)
    Sleep(50)

    def lambda_3E29():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E29)
    Sleep(450)
    StopBGM(0xFA0)
    StopSound(931, 2000, 10)
    Fade(250)
    OP_25(0x340, 0x46)
    Call(0, 2)
    OP_68(0, -800, -10500, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 2070, -250, 2000)
    MoveCamera(0, 7, 0, 2000)
    OP_6E(900, 2000)
    SetCameraDistance(9700, 2000)
    BlurSwitch(0x2BC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -250, 180)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)

    def lambda_3F2F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F2F)
    Sleep(50)

    def lambda_3F47():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F47)
    Sleep(50)

    def lambda_3F5F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F5F)
    Sleep(50)

    def lambda_3F77():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F77)
    Sleep(950)
    CancelBlur(1250)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#6P#N…!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#4P#NDivine Blade of Wind…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "#10503F#5P#40W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    Sound(932, 0, 100, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    SetCameraDistance(9200, 500)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetCameraDistance(8700, 8000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x9,
        (
            "#4055V#40W…… I want to pass\x01",
            "You should hit all of you.\x02\x03",
            "#4056VGuy and I, Sergei san\x01",
            "\"Wall\" not exceeded ──\x02\x03",
            "#4057V#30WThe ability to overcome it\x01",
            "I wonder if you are in … …!\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_24(0xFD9)
    OP_82(0x0, 0x15E, 0xBB8, 0x1F4)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x8)
    SetCameraDistance(8200, 250)
    Sound(533, 0, 60, 0)
    Sound(540, 0, 60, 0)
    Sound(531, 0, 60, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    CancelBlur(500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1270, -1750, 0)
    MoveCamera(0, 3, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11550, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#3322V#6P#N#30W#15A…!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x104,
        "#00307F#2766V#6P#N#30W#20ADon't back off!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00107F#3401V#6P#N#30W#20AWe have to face him!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00207F#2684V#12P#N#30W#25AAion system fully opened!\x01",
            "I will destroy the goal …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x27)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(100)
    OP_68(0, 2070, -250, 600)
    MoveCamera(0, 7, 0, 600)
    OP_6E(900, 600)
    SetCameraDistance(7700, 600)

    def lambda_4394():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4394)

    def lambda_43A9():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43A9)

    def lambda_43BE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43BE)

    def lambda_43D3():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43D3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_24(0x3A3)
    OP_24(0x340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4426")
    Battle("BattleInfo_3E0", 0x0, 0x0, 0x100, 0x3F, 0xFF)
    Jump("loc_4436")

    label("loc_4426")

    Battle("BattleInfo_39C", 0x0, 0x0, 0x100, 0x3F, 0xFF)

    label("loc_4436")

    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Return()

    # Function_30_3A38 end

    def Function_31_4448(): pass

    label("Function_31_4448")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch00056.itc", 0x2B)
    LoadChrToIndex("chr/ch00156.itc", 0x2C)
    LoadChrToIndex("chr/ch00256.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch03850.itc", 0x2F)
    LoadChrToIndex("chr/ch03853.itc", 0x32)
    LoadChrToIndex("apl/ch51531.itc", 0x33)
    LoadChrToIndex("chr/ch03856.itc", 0x34)
    LoadChrToIndex("chr/ch03852.itc", 0x35)
    LoadChrToIndex("chr/ch00053.itc", 0x36)
    LoadChrToIndex("chr/ch00153.itc", 0x37)
    LoadChrToIndex("chr/ch00253.itc", 0x38)
    LoadChrToIndex("chr/ch00353.itc", 0x39)
    LoadChrToIndex("apl/ch51545.itc", 0x3A)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    LoadEffect(0x2, "event\\ev400_00.eff")
    LoadEffect(0x3, "event\\ev15051.eff")
    LoadEffect(0x4, "event\\evwarp.eff")
    LoadEffect(0x5, "event\\ev609_00.eff")
    LoadEffect(0x6, "event\\ev609_01.eff")
    LoadEffect(0x7, "event\\ev001_00.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(852)
    SoundLoad(3402)
    SoundLoad(3323)
    SoundLoad(3324)
    SoundLoad(3325)
    SoundLoad(2767)
    SoundLoad(2685)
    SoundLoad(3784)
    SoundLoad(3785)
    SoundLoad(3786)
    SoundLoad(3626)
    SoundLoad(3627)
    SoundLoad(3628)
    SoundLoad(3629)
    SoundLoad(3630)
    SoundLoad(3631)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 90)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    Sound(832, 2, 50, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 20)
    PlayEffect(0x1, 0x1, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Call(0, 28)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47CE")
    SetChrChipByIndex(0x9, 0x32)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x101, 0x23)
    SetChrChipByIndex(0x102, 0x25)
    SetChrChipByIndex(0x103, 0x27)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, 0, 0, -3500, 0)
    OP_90(0x102, -1000, 0, -4500, 0)
    OP_90(0x103, 1000, 0, -4500, 0)
    OP_90(0x104, 0, 0, -5500, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -1000, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, 1200, -1000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 3000)
    Call(0, 2)
    Jump("loc_4A37")

    label("loc_47CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A2")
    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)
    Jump("loc_4A37")

    label("loc_48A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4976")
    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)
    Jump("loc_4A37")

    label("loc_4976")

    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)

    label("loc_4A37")

    PlayBGM("ed7572", 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FAB")
    OP_2C(0xAD, 0x5)

    ChrTalk(
        0x101,
        "#00002F#6P#NW-we did it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x103,
        "Randy",
        (
            "#00302F#12P#NHappy\x01",
            "What kind of monza it is!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#10504F#5P……\x01",
            "It will surprise you.\x02\x03",
            "#10502FIf this is really … …\x01",
            "It might be beyond us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6P#NHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00207F#12P#NFrom Mr. Arios\x01",
            "I do not feel a sign!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#6P#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetCameraDistance(15500, 0)
    Sound(341, 0, 100, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x2BC)
    OP_0D()
    Fade(500)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, -800, -5000, 0)
    OP_68(0, -800, -6500, 1000)
    MoveCamera(30, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12000, 0)
    Sleep(250)
    Sound(341, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, -2000, -9500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x226)
    OP_6F(0x79)
    OP_0D()
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
    Sleep(1000)

    def lambda_4CF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CF7)
    Sleep(50)

    def lambda_4D07():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D07)
    Sleep(50)

    def lambda_4D17():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D17)
    Sleep(50)

    def lambda_4D27():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4D27)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        "#00310F#5PEmpty cicada#4RObsusiness#… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5P#NCrap!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BlurSwitch(0xFA, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -1000, -9000, 1200)
    MoveCamera(150, 30, 0, 1200)
    OP_6E(750, 1200)
    SetCameraDistance(10000, 1200)
    Sleep(500)
    CancelBlur(1000)
    OP_6F(0x79)
    Fade(400)
    SetCameraDistance(9500, 0)
    SetChrChipByIndex(0x9, 0x35)
    OP_A1(0x9, 0x3E8, 0x2, 0x4, 0x3)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(3990, 255, 100, 0)

    ChrTalk(
        0x9,
        "#15A#10503F#11P── The second type \"gale#4RHayate#\".\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF96)
    ClearChrFlags(0x9, 0x4)
    OP_68(0, 0, -3400, 1000)
    MoveCamera(145, 36, 0, 1000)
    OP_6E(750, 1000)
    SetCameraDistance(11700, 1000)
    Sound(251, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 35)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Sleep(250)
    Fade(250)
    OP_68(0, 300, -3500, 0)
    OP_68(0, 1300, -1500, 1500)
    MoveCamera(40, 12, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12000, 0)
    OP_90(0x9, 0, 0, -1500, 0)
    Sleep(300)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sound(3992, 255, 100, 0)

    ChrTalk(
        0x9,
        "#12A#5P#10507F#5S#9ASlash#2RXan#…!\x02",
    )

    BeginChrThread(0x9, 3, 0, 40)
    WaitChrThread(0x9, 3)
    Sleep(800)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_90(0x9, 0, 3000, -2500, 180)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    SetChrFlags(0x9, 0x4)
    Jump("loc_5225")

    label("loc_4FAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5096")
    OP_2C(0xAD, 0x3)

    ChrTalk(
        0x101,
        (
            "#00010F#11P#30WDamn\x01",
            "…… Come here … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P#30Wlike this……\x01",
            "It's kudas ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5P…… It has grown up.\x02\x03",
            "#10502FIf … someday … …\x01",
            "It might be beyond us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5225")

    label("loc_5096")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5177")
    OP_2C(0xAD, 0x1)

    ChrTalk(
        0x101,
        "#00006F#11P#30WCut … … Ha ha … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P#30WCombat ability is … ….\x01",
            "…… It is too different … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PAlthough not bad,\x01",
            "It seems to be too straight.\x02\x03",
            "#10501FWell then, our\x01",
            "Will not you become a dance of Ni?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5225")

    label("loc_5177")


    ChrTalk(
        0x101,
        "#00006F#11P#40W… …. um ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P#40WHere, so far\x01",
            "I can not be a partner …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PI'm defeated.\x02\x03",
            "#10500FIn its work\x01",
            "Protect important things?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5225")

    Fade(1000)
    OP_25(0x340, 0x46)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 3800, 4000, 0)
    OP_68(0, 3800, 5500, 1200)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#05807F#3626V#5P#4S#30W#13AGuys!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10804F#6P#NEhe, well that was inevitable.\x02\x03",
            "#10811FIf you lose focus\x01",
            "I can not go wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Sound(825, 2, 50, 0)
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#05806F#3627V#5P#40W#15AGot it…\x02\x03",
            "#25A#05801F#3628V#30WAlready……\x01",
            "I will not get lost … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2C)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    OP_0D()
    Sleep(300)
    OP_A1(0xA, 0x3E8, 0x2, 0xE, 0x6)
    Sleep(200)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrPos(0xA, 0, 3350, 7150, 180)
    SetChrSubChip(0xA, 0x10)
    OP_0D()
    Sleep(300)
    OP_A1(0xA, 0x514, 0x2, 0x11, 0x12)
    Sleep(300)
    OP_A1(0xA, 0x514, 0x2, 0x13, 0x14)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7552", 0)
    Fade(500)
    SetCameraDistance(16500, 0)
    BeginChrThread(0xA, 3, 0, 32)
    Sound(928, 0, 80, 0)
    Sound(929, 0, 60, 0)
    Sound(852, 2, 100, 0)
    OP_0D()
    SetCameraDistance(15500, 10000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107F#3402V#30W#18AKeA!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x190, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 170, -1, -1)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x101,
        "#00007F#3323V#4S#16A#30WSTOP IT!!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopSound(832, 1400, 70)
    StopSound(825, 1400, 50)
    Sound(829, 0, 100, 0)
    FadeToDark(1500, 16777215, -1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(1)
    StopSound(927, 500, 80)
    StopSound(852, 500, 100)
    OP_C9(0x0, 0x10)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_24(0x340)
    OP_24(0x339)
    OP_24(0x354)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_05.pmf", 0x228, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    EndChrThread(0xA, 0x3)
    StopEffect(0x1, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x2D, 0x0)
    SoundLoad(933)
    SoundLoad(852)
    SoundLoad(825)
    SoundLoad(927)
    Sound(825, 2, 50, 0)
    Sound(927, 2, 80, 0)
    Sound(933, 2, 80, 0)
    FadeToBright(20000, 16777215)
    OP_11(0x53, 0x59, 0x88, 0x2D, 0x78, 0x3E8)
    OP_68(0, 3900, -4200, 0)
    OP_68(0, 3900, 7500, 10000)
    MoveCamera(0, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(75000, 0)
    BeginChrThread(0x19, 1, 0, 45)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    EndChrThread(0x19, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_11(0x53, 0x59, 0x88, 0xF, 0x78, 0x0)
    BeginChrThread(0x19, 1, 0, 46)
    FadeToDark(0, 16777215, 120)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, -800, -8500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00106F#11PAh … ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#11PAhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PT-this light is..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00210F#11PHave a tremendous density\x01",
            "Seven attributes of spiritual information ……!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -300, -7500, 2000)
    Sleep(500)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(1000)
    EndChrThread(0x19, 0x1)
    BeginChrThread(0x19, 1, 0, 45)
    Fade(1000)
    OP_68(0, 4200, 7500, 0)
    MoveCamera(0, 30, 0, 0)
    MoveCamera(0, 15, 0, 8000)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(15500, 8000)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x33)
    SetChrSubChip(0xA, 0x30)
    BeginChrThread(0xA, 3, 0, 33)
    SetChrPos(0xA, 0, 3750, 7150, 180)
    SetChrFlags(0xA, 0x8)
    BeginChrThread(0x19, 2, 0, 47)
    BeginChrThread(0x19, 3, 0, 48)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x19, 0x1)
    Sound(852, 2, 100, 0)
    StopSound(933, 1000, 80)
    StopSound(825, 1000, 50)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(14500, 0)
    ClearChrFlags(0xA, 0x8)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 0, 750, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x9,
        "#10500F#11PSeptian information overload!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005F…\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00105FAh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#10804F#3784V#40W… … Uhufu …………\x01",
            "I have succeeded …\x02\x03",
            "#10811F#3785VEhehe, what a success\x02\x03",
            "#10809F#3786V#30WNo, it surpasses even that\x01",
            "\"zero#2Rzero#The treasure of \"is the birth of!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xECA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FNo, this is the Rebirth of our Supreme Master of Zero!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 170, -1, -1)

    AnonymousTalk(
        0x104,
        "#00310FMaster of Zero…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    SetCameraDistance(14000, 1500)
    EndChrThread(0xA, 0x3)
    OP_A1(0xA, 0x3E8, 0x7, 0x34, 0x36, 0x37, 0x0, 0x1, 0x2, 0x3)
    OP_A1(0xA, 0x3E8, 0x3, 0x4, 0x5, 0x6)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 34)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetChrName("What in the hell is that")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3629V#40WLloyd… Guys…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2D)
    Sleep(150)
    SetMessageWindowPos(0, 140, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00011F#3324V#40W…Ah\x02\x03",
            "#00013F#3325V#40W… … … Keya ……………\x01",
            "Is it really … … Kaoru …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCFD)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x33)
    OP_A1(0xA, 0x3E8, 0x3, 0x6, 0x7, 0x8)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#40W#5PYes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x3E8, 0x2, 0x7, 0x6)
    Sleep(300)
    OP_A1(0xA, 0x3E8, 0x2, 0xA, 0xB)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12315F#40W#11PBelle, let's go\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 170, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005F#30WHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 34)
    OP_93(0x8, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10804F#11PEhe, understood.\x02\x03",
            "#10800FMr. Arios.\x01",
            "I'll leave it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10503F#11PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(20500, 5000)
    SetChrFlags(0xA, 0x20)

    def lambda_5F8F():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5F8F)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1000)

    def lambda_5FB5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5FB5)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xA, 0x20)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, -800, -8500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00205F#2685V#11P#30W#12AKeA!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#2767V#11P#30W#15AOi where are you going!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 5300, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x33)
    SetChrSubChip(0xA, 0x6)
    OP_6F(0x79)
    OP_0D()
    OP_A1(0xA, 0x3E8, 0x5, 0x6, 0xD, 0xE, 0xF, 0x10)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12304F#3630V#5P#40W#5P#40Asorry.\x01",
            "… … Thank you for everything.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(14500, 500)
    OP_A1(0xA, 0x3E8, 0x4, 0x10, 0x11, 0x12, 0x13)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#3631V#40W#5P#30AI love you all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2F)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(28000, 1500)
    MoveCamera(0, 15, 0, 1500)
    StopSound(852, 1000, 100)
    Sleep(700)
    Sound(936, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0xA, 0x8)
    Sleep(300)
    Sound(936, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0x8, 0x8)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(927, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x228), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x354)
    OP_24(0x339)
    OP_24(0x39F)
    SetScenarioFlags(0x22, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4448 end

    def Function_32_62D1(): pass

    label("Function_32_62D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_631B")
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_32_62D1")

    label("loc_631B")

    Return()

    # Function_32_62D1 end

    def Function_33_631C(): pass

    label("Function_33_631C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_633A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x30, 0x31, 0x32, 0x31, 0x30, 0x33, 0x34, 0x33)
    Jump("Function_33_631C")

    label("loc_633A")

    Return()

    # Function_33_631C end

    def Function_34_633B(): pass

    label("Function_34_633B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6359")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_34_633B")

    label("loc_6359")

    Return()

    # Function_34_633B end

    def Function_35_635A(): pass

    label("Function_35_635A")

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2EE0, 0x1)
    StopEffect(0x2, 0x2)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    def lambda_63C6():
        OP_9B(0x1, 0xFE, 0x0, 0x1964, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C6)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sound(569, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 300, -3500, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_82(0x15E, 0x15E, 0x1388, 0x2BC)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 37)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x101, 3, 0, 36)
    WaitChrThread(0xFE, 1)
    StopEffect(0x2, 0x2)
    CancelBlur(500)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Sleep(700)
    SetChrSubChip(0xFE, 0x2)
    Sleep(75)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_635A end

    def Function_36_64B9(): pass

    label("Function_36_64B9")

    Sound(2029, 255, 100, 1)

    ChrTalk(
        0x101,
        "#00010F#5P… …. Ugh … …!\x05\x02",
    )


    def lambda_64E4():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64E4)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_64B9 end

    def Function_37_650B(): pass

    label("Function_37_650B")

    Sound(2129, 255, 90, 2)

    ChrTalk(
        0x102,
        "#00106F#12P……… Oooh ……!\x05\x02",
    )


    def lambda_6539():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6539)
    SetChrChipByIndex(0xFE, 0x37)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_650B end

    def Function_38_6560(): pass

    label("Function_38_6560")


    def lambda_6565():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6565)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_6560 end

    def Function_39_658C(): pass

    label("Function_39_658C")


    def lambda_6591():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6591)
    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_39_658C end

    def Function_40_65B8(): pass

    label("Function_40_65B8")

    Fade(500)
    SetCameraDistance(10500, 500)
    Sound(533, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sound(532, 0, 100, 0)
    Sound(833, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(75)
    Sound(569, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 1300, -5500, 700)
    SetCameraDistance(12500, 700)
    SetChrSubChip(0xFE, 0x2)
    Sleep(75)
    SetChrSubChip(0xFE, 0x3)
    Sound(200, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x3E8)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x104, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 42)
    BeginChrThread(0x103, 3, 0, 43)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(500)
    CancelBlur(1500)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Fade(250)
    SetChrSubChip(0xFE, 0x4)
    OP_0D()
    Return()

    # Function_40_65B8 end

    def Function_41_66BB(): pass

    label("Function_41_66BB")


    def lambda_66C0():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66C0)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2031, 255, 100, 1)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFDCD8, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 100, 0)
    Return()

    # Function_41_66BB end

    def Function_42_6714(): pass

    label("Function_42_6714")


    def lambda_6719():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6719)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2128, 255, 90, 2)
    OP_9D(0xFE, 0xFFFFFC18, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_6714 end

    def Function_43_6767(): pass

    label("Function_43_6767")


    def lambda_676C():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_676C)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2224, 255, 100, 3)
    OP_9D(0xFE, 0x3E8, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_6767 end

    def Function_44_67BA(): pass

    label("Function_44_67BA")


    def lambda_67BF():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_67BF)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2764, 255, 100, 4)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFD508, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_67BA end

    def Function_45_680D(): pass

    label("Function_45_680D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6826")
    Sound(929, 0, 40, 0)
    Sleep(2200)
    Jump("Function_45_680D")

    label("loc_6826")

    Return()

    # Function_45_680D end

    def Function_46_6827(): pass

    label("Function_46_6827")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6840")
    Sound(929, 0, 20, 0)
    Sleep(2200)
    Jump("Function_46_6827")

    label("loc_6840")

    Return()

    # Function_46_6827 end

    def Function_47_6841(): pass

    label("Function_47_6841")

    Sleep(6000)
    Sound(930, 0, 100, 0)
    Sleep(2000)
    Sound(928, 0, 100, 0)
    Return()

    # Function_47_6841 end

    def Function_48_6854(): pass

    label("Function_48_6854")

    Sound(934, 0, 70, 0)
    Sleep(1500)
    Sound(934, 0, 80, 0)
    Sleep(1500)
    Sound(934, 0, 90, 0)
    Sleep(1500)
    Sound(934, 0, 100, 0)
    Sleep(1500)
    Sound(934, 0, 90, 0)
    Return()

    # Function_48_6854 end

    def Function_49_687F(): pass

    label("Function_49_687F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00056.itc", 0x26)
    LoadChrToIndex("chr/ch00156.itc", 0x27)
    LoadChrToIndex("chr/ch00256.itc", 0x28)
    LoadChrToIndex("chr/ch00356.itc", 0x29)
    LoadChrToIndex("chr/ch03800.itc", 0x2A)
    LoadChrToIndex("chr/ch03850.itc", 0x2B)
    LoadChrToIndex("chr/ch03900.itc", 0x2C)
    LoadChrToIndex("chr/ch41450.itc", 0x2D)
    LoadChrToIndex("chr/ch41451.itc", 0x2E)
    LoadChrToIndex("chr/ch41452.itc", 0x2F)
    LoadChrToIndex("apl/ch51533.itc", 0x30)
    LoadChrToIndex("apl/ch51534.itc", 0x31)
    SoundLoad(4069)
    SoundLoad(4070)
    SoundLoad(4058)
    SoundLoad(3326)
    SoundLoad(3523)
    SoundLoad(3524)
    SoundLoad(3525)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis411.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10200.itp")
    SetChrChipByIndex(0x101, 0x26)
    SetChrChipByIndex(0x102, 0x27)
    SetChrChipByIndex(0x103, 0x28)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2D)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x2D)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x2D)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x13, 0, -2000, -20000, 0)
    SetChrPos(0xB, 500, -2000, -28000, 0)
    SetChrPos(0xC, 1500, -2000, -28500, 0)
    SetChrPos(0xD, 2000, -2000, -30000, 0)
    SetChrPos(0xE, 500, -2000, -29500, 0)
    SetChrPos(0xF, -500, -2000, -28000, 0)
    SetChrPos(0x10, -1500, -2000, -28500, 0)
    SetChrPos(0x11, -2000, -2000, -30000, 0)
    SetChrPos(0x12, -500, -2000, -29500, 0)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    SetMapObjFrame(0x4, "m_face1", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face2", 0x0, 0x1)
    Call(0, 2)
    OP_68(0, 7000, 9500, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(40000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 7000, -9500, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    Call(0, 4)
    OP_68(-850, -300, -10800, 0)
    MoveCamera(32, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12770, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00010F#11P#40W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P#30WThere's no way..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#30W………we…………\x01",
            "Are you still watching a dream …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11P#30WUnfortunately……\x01",
            "…… I want to reality ……\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7571", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#10503F#4069V#5P#40W#NExactly\x02\x03",
            "#10501F#4070VAfter the \"miracle\"\x01",
            "The reality awaits.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFE6)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    Sound(937, 0, 50, 0)

    NpcTalk(
        0xB,
        "voice",
        "#1PThere they are!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "voice",
        (
            "#1PSecretary Arios!\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -300, -7000, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(0, -1000, -21000, 3000)
    MoveCamera(135, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16500, 3000)
    BeginChrThread(0xB, 3, 0, 50)
    Sleep(200)
    BeginChrThread(0xC, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x12, 3, 0, 50)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#6P#NAh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#NTch!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    Fade(500)
    OP_68(0, -1000, -14000, 0)
    MoveCamera(50, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(0, -1000, -11000, 5000)
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 61)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 62)
    BeginChrThread(0xB, 3, 0, 51)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 54)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 56)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 58)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0x13, 0x8)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x13,
        "Daughter's voice",
        "#3523V#30W#15ANo resisting!\x02",
    )

    CloseMessageWindow()
    OP_24(0xDC3)
    OP_C9(0x1, 0x80000000)
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#5PThat voice is…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 4)
    OP_68(0, -1000, -10000, 0)
    MoveCamera(180, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, -1000, -13000, 4000)
    BeginChrThread(0x13, 3, 0, 63)
    WaitChrThread(0x13, 3)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x13,
        (
            "#3524V#30WAlready the Michelam region\x01",
            "The Defense Force is controlling.\x02\x03",
            "#3525Vplease……\x01",
            "Please surrender as usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDC5)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x104,
        "#00301F#6PNoel, you…\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Lloyd",
        "#00013F#6P#NWhy…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10208F#5P#30W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -300, -7000, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#10503F#5PGood work Seeker\x02\x03",
            "#10500FI will return to the Orkis Tower.\x01",
            "I will leave them to their detention.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -1000, -14000, 2000)
    MoveCamera(150, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    Fade(250)
    SetCameraDistance(16000, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x30)
    SetChrSubChip(0x13, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x13,
        "#10201F#11PRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Call(0, 2)
    OP_68(0, -1000, -10000, 0)
    MoveCamera(0, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(16000, 1000)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 65)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 66)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 67)
    CancelBlur(1500)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x10, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    Call(0, 4)
    OP_68(0, -300, -7000, 0)
    OP_68(0, -1200, -10000, 6000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 3, 0, 72)
    Sleep(3000)
    OP_0D()
    Fade(500)
    OP_68(-2560, -200, -12050, 0)
    OP_68(-2560, -200, -15050, 3000)
    MoveCamera(353, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sound(3326, 255, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11PWait!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCFE)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W……Only one thing……\x01",
            "Please just answer me one.\x02\x03",
            "#00008FIf you have been working for several years\x01",
            "If you were cooperating with them … …\x02\x03",
            "#00013FGuy Bannings ----\x01",
            "Are you the one who killed the older brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00205F#11P!?\x02",
    )

    CloseMessageWindow()

    def lambda_7689():

        label("loc_7689")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7689")

    QueueWorkItem2(0x13, 2, lambda_7689)
    Sleep(300)

    ChrTalk(
        0x13,
        "#10205F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#5PThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11POi, no way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10500F#5P#40W…\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 3000)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x9)
    Sleep(400)
    Fade(250)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        "#10503F#4058V#5P#40W#30AYes. That's correct.\x02",
    )

    CloseMessageWindow()
    OP_24(0xFDA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(20000, 5000)
    BeginChrThread(0x9, 0, 0, 73)

    def lambda_77B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_77B6)
    Sleep(300)

    def lambda_77CE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_77CE)
    Sleep(700)
    StopSound(927, 1000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_29(0xAD, 0x1, 0x6)
    OP_29(0xAD, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x21, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    ReplaceBGM(-1, -1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_49_687F end

    def Function_50_78D1(): pass

    label("Function_50_78D1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_78D1 end

    def Function_51_78F1(): pass

    label("Function_51_78F1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFFC568, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_51_78F1 end

    def Function_52_7931(): pass

    label("Function_52_7931")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFEA070, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_7931 end

    def Function_53_796B(): pass

    label("Function_53_796B")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF15A0, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_796B end

    def Function_54_79A5(): pass

    label("Function_54_79A5")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF5038, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_54_79A5 end

    def Function_55_79E5(): pass

    label("Function_55_79E5")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x3A98, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_55_79E5 end

    def Function_56_7A1F(): pass

    label("Function_56_7A1F")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x15F90, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_56_7A1F end

    def Function_57_7A5F(): pass

    label("Function_57_7A5F")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xEA60, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_57_7A5F end

    def Function_58_7A99(): pass

    label("Function_58_7A99")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xAFC8, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_58_7A99 end

    def Function_59_7AD9(): pass

    label("Function_59_7AD9")


    def lambda_7ADE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7ADE)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_59_7AD9 end

    def Function_60_7B15(): pass

    label("Function_60_7B15")


    def lambda_7B1A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B1A)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_60_7B15 end

    def Function_61_7B51(): pass

    label("Function_61_7B51")


    def lambda_7B56():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B56)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_61_7B51 end

    def Function_62_7B87(): pass

    label("Function_62_7B87")


    def lambda_7B8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B8C)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_62_7B87 end

    def Function_63_7BC3(): pass

    label("Function_63_7BC3")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_63_7BC3 end

    def Function_64_7BD3(): pass

    label("Function_64_7BD3")

    TurnDirection(0xFE, 0x104, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xA, 0x73A, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 71)
    WaitChrThread(0x104, 3)
    Return()

    # Function_64_7BD3 end

    def Function_65_7C0E(): pass

    label("Function_65_7C0E")

    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xA, 0xCB2, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 68)
    WaitChrThread(0x101, 3)
    Return()

    # Function_65_7C0E end

    def Function_66_7C49(): pass

    label("Function_66_7C49")

    TurnDirection(0xFE, 0x103, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x5, 0x109A, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 70)
    WaitChrThread(0x103, 3)
    Return()

    # Function_66_7C49 end

    def Function_67_7C84(): pass

    label("Function_67_7C84")

    TurnDirection(0xFE, 0x102, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xFFFB, 0x9C4, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 69)
    WaitChrThread(0x102, 3)
    Return()

    # Function_67_7C84 end

    def Function_68_7CBF(): pass

    label("Function_68_7CBF")


    def lambda_7CC4():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CC4)
    Sound(2029, 255, 70, 0)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_68_7CBF end

    def Function_69_7CFA(): pass

    label("Function_69_7CFA")


    def lambda_7CFF():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7CFF)
    Sound(2127, 255, 70, 1)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_69_7CFA end

    def Function_70_7D35(): pass

    label("Function_70_7D35")


    def lambda_7D3A():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7D3A)
    Sound(2223, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_70_7D35 end

    def Function_71_7D70(): pass

    label("Function_71_7D70")


    def lambda_7D75():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7D75)
    Sound(2317, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_71_7D70 end

    def Function_72_7DAB(): pass

    label("Function_72_7DAB")

    ClearChrFlags(0x9, 0x4)
    OP_9B(0x0, 0xFE, 0x14, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x1964, 0xBB8, 0x0)
    Return()

    # Function_72_7DAB end

    def Function_73_7DDE(): pass

    label("Function_73_7DDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DFC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x1, 0x2, 0x3, 0x2, 0x1, 0x4, 0x5, 0x4)
    Jump("Function_73_7DDE")

    label("loc_7DFC")

    Return()

    # Function_73_7DDE end

    SaveToFile()

Try(main)
