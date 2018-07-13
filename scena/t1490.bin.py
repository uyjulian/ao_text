from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Mariabell",              # 1
        "Secretary Arios",        # 2
        "KeA",                    # 3
        "State Guard Soldier",    # 4
        "State Guard Soldier",    # 5
        "State Guard Soldier",    # 6
        "State Guard Soldier",    # 7
        "State Guard Soldier",    # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "State Guard Soldier",    # 11
        "2nd Lt. Noｱl",          # 12
        "映像",                   # 13
        "映像",                   # 14
        "映像",                   # 15
        "映像",                   # 16
        "映像",                   # 17
        "SE制御",                 # 18
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
        "Function_6_2C68",         # 06, 6
        "Function_7_2CD4",         # 07, 7
        "Function_8_2D40",         # 08, 8
        "Function_9_2DA6",         # 09, 9
        "Function_10_2E12",        # 0A, 10
        "Function_11_2E34",        # 0B, 11
        "Function_12_2E56",        # 0C, 12
        "Function_13_2E78",        # 0D, 13
        "Function_14_2E9A",        # 0E, 14
        "Function_15_2EBC",        # 0F, 15
        "Function_16_2ECC",        # 10, 16
        "Function_17_2EDC",        # 11, 17
        "Function_18_2EEC",        # 12, 18
        "Function_19_2EFC",        # 13, 19
        "Function_20_2F0C",        # 14, 20
        "Function_21_2F27",        # 15, 21
        "Function_22_2F39",        # 16, 22
        "Function_23_39D4",        # 17, 23
        "Function_24_3A57",        # 18, 24
        "Function_25_3A77",        # 19, 25
        "Function_26_3AA1",        # 1A, 26
        "Function_27_3ACB",        # 1B, 27
        "Function_28_3AF5",        # 1C, 28
        "Function_29_3B35",        # 1D, 29
        "Function_30_3B51",        # 1E, 30
        "Function_31_4565",        # 1F, 31
        "Function_32_6447",        # 20, 32
        "Function_33_6492",        # 21, 33
        "Function_34_64B1",        # 22, 34
        "Function_35_64D0",        # 23, 35
        "Function_36_662F",        # 24, 36
        "Function_37_6682",        # 25, 37
        "Function_38_66D4",        # 26, 38
        "Function_39_6700",        # 27, 39
        "Function_40_672C",        # 28, 40
        "Function_41_682F",        # 29, 41
        "Function_42_6888",        # 2A, 42
        "Function_43_68DB",        # 2B, 43
        "Function_44_692E",        # 2C, 44
        "Function_45_6981",        # 2D, 45
        "Function_46_699B",        # 2E, 46
        "Function_47_69B5",        # 2F, 47
        "Function_48_69C8",        # 30, 48
        "Function_49_69F3",        # 31, 49
        "Function_50_7A31",        # 32, 50
        "Function_51_7A51",        # 33, 51
        "Function_52_7A91",        # 34, 52
        "Function_53_7ACB",        # 35, 53
        "Function_54_7B05",        # 36, 54
        "Function_55_7B45",        # 37, 55
        "Function_56_7B7F",        # 38, 56
        "Function_57_7BBF",        # 39, 57
        "Function_58_7BF9",        # 3A, 58
        "Function_59_7C39",        # 3B, 59
        "Function_60_7C75",        # 3C, 60
        "Function_61_7CB1",        # 3D, 61
        "Function_62_7CE7",        # 3E, 62
        "Function_63_7D23",        # 3F, 63
        "Function_64_7D33",        # 40, 64
        "Function_65_7D6E",        # 41, 65
        "Function_66_7DA9",        # 42, 66
        "Function_67_7DE4",        # 43, 67
        "Function_68_7E1F",        # 44, 68
        "Function_69_7E5A",        # 45, 69
        "Function_70_7E95",        # 46, 70
        "Function_71_7ED0",        # 47, 71
        "Function_72_7F0B",        # 48, 72
        "Function_73_7F3E",        # 49, 73
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

    def lambda_BC2():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC2)
    Sleep(50)

    def lambda_BDA():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BDA)
    Sleep(50)

    def lambda_BF2():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF2)
    Sleep(50)

    def lambda_C0A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00201F#11PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11P...Hey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PWhy...\x02",
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

    def lambda_CEB():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEB)
    Sleep(50)

    def lambda_D03():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D03)
    Sleep(50)

    def lambda_D1B():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D1B)
    Sleep(50)

    def lambda_D33():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D33)
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
            "#00007F#3321V#30W#20AKeA!\x01",
            "Mr. Arios...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107F#3398V#30W#15A...Bell...!\x02",
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
        "#3625V#40W...Lloyd...everyone...\x02",
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
        "#10503F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#10804F#3780V#5P#30WUh uh...\x01",
            "You have finally come.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC4)
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    ChrTalk(
        0x102,
        "#00106F#3399V#11P#40WBell... Why...\x02",
    )

    CloseMessageWindow()
    OP_24(0xD47)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x102,
        (
            "#00107F#3400V#11P#4S#30WWhy are\x01",
            "you there!?\x02",
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
            "#3781V#30WUh uh──\x01",
            "It is simple.\x02\x03",
            "#3782VAs a descendant of the Crois\x01",
            "clan that inherited the \x01",
            ""Great Sept-Terrion"...\x02\x03",
            "#3783VIt is only natural to\x01",
            "carry out my duty.\x02",
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
        "#00011F#11PThe "Great Sept-Terrion"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PIt can't be...\x01",
            "The same kind of the "Aureole"\x01",
            "that appeared in Liberl...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10809F#5PThis will save me time.\x02\x03",
            "#10804FThe "Sept-Terrions" the Goddess gave to\x01",
            "humanity a very long time ago...\x02\x03",
            "#10811FOne of them was inherited by my family.\x01\x02\x03",
            "That was over 1200 years ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11P......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PI don't get it at all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PUh uh, due to some unfortunate events,\x01",
            "this Goddess' Sept-Terrion was lost.\x02\x03",
            "#10803FAs a result, the Crois clan's founders\x01",
            "devised an extraordinary grand project to\x01",
            "retrieve this Sept-Terrion at all costs...\x02\x03",
            "#10800FThey decided to construct a giant\x01",
            ""ceremony" in the land of Crossbell.\x02",
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
        "#00108F#11PA giant "ceremony"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PThe inexplicable and giant system\x01",
            "that uses the orbal net...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10803F#5PYes, a "magical science" brought forth\x01",
            "by uniting the present orbal technology \x01",
            "with the Crois clan's alchemy...\x02\x03",
            "#10802FThereby, an absurdly giant \x01",
            ""ceremony" can finally be realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PA "ceremony" from "magical science"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#11PA-And also alchemy...\x02",
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
            "#00006F#11P...I see...\x01",
            "So that's how it is.\x02\x03",
            "#00008FThe group of alchemists who built\x01",
            "the "Tower of Stargaze" once and\x01",
            "sponsored the "Cult" technologies...\x02\x03",
            "#00007F──It was you, the Crois\x01",
            "clan, that did that, right!?\x02",
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
        "#00305F#11PWhat...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PB-But...\x01",
            "If you consider it, it makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PT-Then, even that\x01",
            ""cradle" where KeA\x01",
            "was sleeping into...\x02",
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
            "#10804F#5PUh uh, naturally it was something\x01",
            "the Crois clan offered to the "Cult".\x02\x03",
            "#10811F──We gave them an object to worship,\x01",
            "to make them pleasantly work for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05808F#5P............\x02",
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
            "#00013F#11PThen, the "D∴G Cult",\x01",
            "you really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11P...Manipulated it from the shadows in\x01",
            "order to reach the Crois clan goals...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PYes, it was nothing more than a puppet.\x02\x03",
            "#10811FEh eh...although they probably\x01",
            "weren't self-conscious about it.\x02",
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
            "#10809F#5PUh uh, I guess they roughly\x01",
            "believed in that setting?\x02\x03",
            "#10805F──Oh, incidentally,\x01",
            "Mr. Arios here is not\x01",
            "related to my family.\x02\x03",
            "#10804FThis time he is a reliable\x01",
            "collaborator who agrees\x01",
            "to our project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10503F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11PMr. Arios...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P...Are you crazy?\x01",
            "Believing in such a wild delusion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5PHmph...a wild delusion?\x02\x03",
            "#10502FIndeed, I too agree\x01",
            "on that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10801F#6PMy...!\x01",
            "How rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PHowever, they have that power...\x01",
            "If I want to change this situation...\x02\x03",
            "I'll get on with that fantasy\x01",
            "as much as they want.\x02\x03",
            "#10501F──Even if I had to go against\x01",
            "the will of the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PUnbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11P...Why would you...\x02",
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
            "#00006F#11P...Honestly speaking, I can't sort out\x01",
            "all of these absurd stories yet, however...\x02\x03",
            "#00003FHowever...I can only say this.\x02",
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
            "#00010F#11PI won't ever accept you involving\x01",
            "KeA in those delusions!!\x02",
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
            "#00007F#11P#4SKeA, come back!\x02\x03",
            "#3SI don't know what they suggested you,\x01",
            "but KeA is KeA!, am I not right?\x02\x03",
            "You've got no reason to sit there...\x01",
            "With such a painful-looking expression!\x02",
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
        "#05812F#5P#30W...Lloyd... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PUhuhu... Miss KeA.\x02\x03",
            "Mr. Lloyd is saying\x01",
            "all that, however...\x02\x03",
            "#10811FWhat do YOU want to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#05808F#5P#30W............\x02",
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
        "#00011F...KeA...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00105FW-What's wrong...?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 170, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00307F#4SKeddo, there's nothin'\x01",
            "to hesitate 'bout!\x02\x03",
            "Come jump into Lloyd's\x01",
            "arms like you always do!\x02\x03",
            "Isn't that what makes you\x01",
            "feel secure the most!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        "#05812F#5P#30WRandy...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00104F...He's right. Probably you have\x01",
            "your own circumstances, but...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FI think they aren't definitely\x01",
            "more important than that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#05808F#5P#30W...Elie... Tio...\x02\x03",
            "#05814F#40W............\x02",
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
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3719V#30WUhuhu... \x01",
            "Having fun, aren't you?\x07\x00\x02",
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
        "#00110F#11P"Ouroboros"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PAs we thought, you have\x01",
            "a connection with them...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#10804F#5PUh uh, we just have a relationship\x01",
            "of mutual cooperation...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10802F#11P──Everone. I believe your\x01",
            "preparations are finished?\x02",
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
            "Hoho, but of course.\x02\x03",
            "I think they're finished in a way you \x01",
            "will be satisfied of, you know?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(280, 135, -1, -1)
    SetChrName("Arianrhod")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The "bells" too are ready.\x02\x03",
            "What remains is only to turn the "key".\x07\x00\x02",
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
            "I would be fine waiting until\x01",
            "they understand it, but...\x02\x03",
            "It seems we're out of time, hm?\x07\x00\x02",
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
        "#10800F#11PMy my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10501F#5P...So they're coming.\x02",
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
        "#00011F#11PW-What're you saying...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PWhat's with being out of time!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PNaturally──it's the invasion...\x02\x03",
            "#10501FBy the Imperial and Republican armies.\x02",
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
        "#00007F#11P#4S!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#11PAh...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#10809F#5PUh uh, since we are here,\x01",
            "should we watch it live?\x02",
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

    def Function_6_2C68(): pass

    label("Function_6_2C68")


    def lambda_2C6D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C6D)

    def lambda_2C82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C82)
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_2C68 end

    def Function_7_2CD4(): pass

    label("Function_7_2CD4")


    def lambda_2CD9():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CD9)

    def lambda_2CEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CEE)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_2CD4 end

    def Function_8_2D40(): pass

    label("Function_8_2D40")


    def lambda_2D45():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D45)

    def lambda_2D5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D5A)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_2D40 end

    def Function_9_2DA6(): pass

    label("Function_9_2DA6")


    def lambda_2DAB():
        OP_9B(0x0, 0xFE, 0x0, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DAB)

    def lambda_2DC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC0)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_2DA6 end

    def Function_10_2E12(): pass

    label("Function_10_2E12")

    OP_71(0x0, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_10_2E12 end

    def Function_11_2E34(): pass

    label("Function_11_2E34")

    OP_71(0x1, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_11_2E34 end

    def Function_12_2E56(): pass

    label("Function_12_2E56")

    OP_71(0x2, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_12_2E56 end

    def Function_13_2E78(): pass

    label("Function_13_2E78")

    OP_71(0x3, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x3)
    OP_71(0x3, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_13_2E78 end

    def Function_14_2E9A(): pass

    label("Function_14_2E9A")

    OP_71(0x4, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_14_2E9A end

    def Function_15_2EBC(): pass

    label("Function_15_2EBC")

    OP_71(0x0, 0xF5, 0x12C, 0x0, 0x8)
    OP_79(0x0)
    Return()

    # Function_15_2EBC end

    def Function_16_2ECC(): pass

    label("Function_16_2ECC")

    OP_71(0x1, 0xFA, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    Return()

    # Function_16_2ECC end

    def Function_17_2EDC(): pass

    label("Function_17_2EDC")

    OP_71(0x2, 0xFF, 0x12C, 0x0, 0x8)
    OP_79(0x2)
    Return()

    # Function_17_2EDC end

    def Function_18_2EEC(): pass

    label("Function_18_2EEC")

    OP_71(0x3, 0x104, 0x12C, 0x0, 0x8)
    OP_79(0x3)
    Return()

    # Function_18_2EEC end

    def Function_19_2EFC(): pass

    label("Function_19_2EFC")

    OP_71(0x4, 0x10E, 0x12C, 0x0, 0x8)
    OP_79(0x4)
    Return()

    # Function_19_2EFC end

    def Function_20_2F0C(): pass

    label("Function_20_2F0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F26")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_20_2F0C")

    label("loc_2F26")

    Return()

    # Function_20_2F0C end

    def Function_21_2F27(): pass

    label("Function_21_2F27")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_21_2F27 end

    def Function_22_2F39(): pass

    label("Function_22_2F39")

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
        "#00110FN-No way...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x104,
        "#00311FThey did come...!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FThe CGF military power\x01",
            "won't keep them in check...\x02",
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
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──The girl is the "key"\x01",
            "that will overthrow them.\x07\x00\x02",
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
        "#00010F#11PPresident Dieter...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11P..."Uncle"...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lady and gentlemen from the "Society".\x01",
            "You have my thanks for cooperating to my project.\x02\x03",
            "Bell and Arios too.\x01",
            "It seems it's going according to plan?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#10804F#5PYes, up to here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5P...We can only entrust\x01",
            "the rest to her.\x02",
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
            "──It's as you've heard, KeA.\x02\x03",
            "You understand, right?\x02\x03",
            "That you're the only one who can\x01",
            "do something about this situation──\x02",
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
        "#05803F#5P#30W............(*nods*)\x02",
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
        "#10811F#5PUh uh, what a good girl.\x02",
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

    # Function_22_2F39 end

    def Function_23_39D4(): pass

    label("Function_23_39D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A56")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A04")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_3A4E")

    label("loc_3A04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A29")
    OP_82(0xA, 0x1E, 0xBB8, 0x1F4)
    Jump("loc_3A4E")

    label("loc_3A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4E")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_3A4E")

    label("loc_3A4E")

    Sleep(500)
    Jump("Function_23_39D4")

    label("loc_3A56")

    Return()

    # Function_23_39D4 end

    def Function_24_3A57(): pass

    label("Function_24_3A57")

    SetMapObjFrame(0xFF, "chair", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    Return()

    # Function_24_3A57 end

    def Function_25_3A77(): pass

    label("Function_25_3A77")

    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on_ani")
    Sleep(1133)
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    Return()

    # Function_25_3A77 end

    def Function_26_3AA1(): pass

    label("Function_26_3AA1")

    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    Return()

    # Function_26_3AA1 end

    def Function_27_3ACB(): pass

    label("Function_27_3ACB")

    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_27_3ACB end

    def Function_28_3AF5(): pass

    label("Function_28_3AF5")

    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_28_3AF5 end

    def Function_29_3B35(): pass

    label("Function_29_3B35")

    Sleep(500)
    Sound(162, 0, 100, 0)
    Sleep(400)
    Sound(162, 0, 100, 0)
    Sleep(300)
    Sound(162, 0, 100, 0)
    Return()

    # Function_29_3B35 end

    def Function_30_3B51(): pass

    label("Function_30_3B51")

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
        "#00007F#11P#4S──KeA, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PBell, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PI don't get it, but\x01",
            "we won't let you do it...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIn any case...\x01",
            "Let's stop them!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -8500, 1000)

    def lambda_3EE6():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EE6)
    Sleep(50)

    def lambda_3EFE():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EFE)
    Sleep(50)

    def lambda_3F16():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F16)
    Sleep(50)

    def lambda_3F2E():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F2E)
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

    def lambda_4034():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4034)
    Sleep(50)

    def lambda_404C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_404C)
    Sleep(50)

    def lambda_4064():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4064)
    Sleep(50)

    def lambda_407C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_407C)
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
        "#00011F#6P#N...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#4P#NThe "Divine Blade of Wind"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "#10503F#5P#40W............\x02",
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
            "#4055V#40W...If you want to pass,\x01",
            "you should attack me all together.\x02\x03",
            "#4056VMake me see if you have the\x01",
            "power to get over that "barrier"──\x02\x03",
            "#4057V#30WThat Guy, I and Mr.\x01",
            "Sergei couldn't...!\x02",
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
        "#00010F#3322V#6P#N#30W#15AKh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x104,
        "#00307F#2766V#6P#N#30W#20ADon't freak out, he's alone!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00107F#3401V#6P#N#30W#20AWe must win in some way...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00207F#2684V#12P#N#30W#25AAeon System, full activation!\x01",
            "I will destroy the target...!\x02",
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

    def lambda_44B1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44B1)

    def lambda_44C6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44C6)

    def lambda_44DB():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44DB)

    def lambda_44F0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44F0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_24(0x3A3)
    OP_24(0x340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4543")
    Battle("BattleInfo_3E0", 0x0, 0x0, 0x100, 0x3F, 0xFF)
    Jump("loc_4553")

    label("loc_4543")

    Battle("BattleInfo_39C", 0x0, 0x0, 0x100, 0x3F, 0xFF)

    label("loc_4553")

    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Return()

    # Function_30_3B51 end

    def Function_31_4565(): pass

    label("Function_31_4565")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48EB")
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
    Jump("loc_4B54")

    label("loc_48EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49BF")
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
    Jump("loc_4B54")

    label("loc_49BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A93")
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
    Jump("loc_4B54")

    label("loc_4A93")

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

    label("loc_4B54")

    PlayBGM("ed7572", 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50BA")
    OP_2C(0xAD, 0x5)

    ChrTalk(
        0x101,
        "#00002F#6P#NW-We did it...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x103,
        "Randy",
        (
            "#00302F#12P#NHah...\x01",
            "It's only that what you've got?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#10504F#5P...Hmph...\x01",
            "You surprised me.\x02\x03",
            "#10502FIf this is the case, then...\x01",
            "You could really surpass us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6P#N...What...\x02",
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
            "#00207F#12P#NI don't sense a presence\x01",
            "from Mr. Arios!\x02",
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

    def lambda_4E1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E1B)
    Sleep(50)

    def lambda_4E2B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E2B)
    Sleep(50)

    def lambda_4E3B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4E3B)
    Sleep(50)

    def lambda_4E4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E4B)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        "#00310F#5PA copy image...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5P#NDamn──\x02",
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
        "#15A#10503F#11P──Second Form, "Gale".\x02",
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
        "#12A#5P#10507F#5S#9AStrike...!\x02",
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
    Jump("loc_5364")

    label("loc_50BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5192")
    OP_2C(0xAD, 0x3)

    ChrTalk(
        0x101,
        (
            "#00010F#11P#30WKh...\x01",
            "...We came so far...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P#30WAs if we'd let \x01",
            "this end here...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5P...You've grown.\x02\x03",
            "#10502FMaybe one day...\x01",
            "You'll be able to surpass us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5364")

    label("loc_5192")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A1")
    OP_2C(0xAD, 0x1)

    ChrTalk(
        0x101,
        "#00006F#11P#30WKh...*pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P#30WThe difference in our fighting\x01",
            "abilities...is too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PIt's not a bad thing,\x01",
            "but you're too upright.\x02\x03",
            "#10501FIn that case, you'll repeat\x01",
            "our same mistakes, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5364")

    label("loc_52A1")


    ChrTalk(
        0x101,
        "#00006F#11P#40W...Ghh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P#40WW-We can't even\x01",
            "rival with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PYou lack focus.\x02\x03",
            "#10500FIn that state, you won't be able\x01",
            "to protect what's important to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5364")

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
        "#05807F#3626V#5P#4S#30W#13AEveryone...!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10804F#6P#NUh uh, he struck them with the back of the sword.\x02\x03",
            "#10811FThings won't go well if you\x01",
            "interrupt your concentration...\x02",
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
            "#05806F#3627V#5P#40W#15A...I got it...\x02\x03",
            "#25A#05801F#3628V#30WI won't...\x01",
            "Hesitate anymore...!\x02",
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
        "#00107F#3402V#30W#18AK-KeA...!?\x02",
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
        "#00007F#3323V#4S#16A#30WStooooop...!\x02",
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
        "#00106F#11PEeeeek...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#11PT-This light is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PThe heck's going on...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00210F#11PThe hi-density spirit particles data\x01",
            "of the seven elements are...!\x02",
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
        "#10500F#11P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005F......ah......\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00105FKeA....?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#10804F#3784V#40W......Uhuhu...\x01",
            "It was a success....\x02\x03",
            "#10811F#3785VIt is the revival of the lost\x01",
            ""Sept-Terrion of Mirage"...\x02\x03",
            "#10809F#3786V#30WNo, it is the birth of the "Sept-Terrion of Zero"\x01",
            "that surpasses even that!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xECA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FT-The "Sept-Terrion of Zero"...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 170, -1, -1)

    AnonymousTalk(
        0x104,
        "#00310FT-The hell is that...\x02",
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
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3629V#40WLIoyd... Everyone...\x07\x00\x02",
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
            "#00011F#3324V#40W............\x02\x03",
            "#00013F#3325V#40W......KeA......\x01",
            "Are you really...KeA...?\x02",
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
            "#12303F#40W#5PYes......\x07\x00\x02",
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
            "#12315F#40W#11P...Bell, let's go.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 170, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005F#30WHuh...\x02",
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
            "#10804F#11PUh uh, very well.\x02\x03",
            "#10800FMr. Arios,\x01",
            "I leave them to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10503F#11P...Understood.\x02",
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

    def lambda_60EA():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_60EA)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1000)

    def lambda_6110():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6110)
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
        "#00205F#2685V#11P#30W#12AKeA....!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#2767V#11P#30W#15AHey, where're you...!?\x02",
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
            "#12304F#3630V#5P#40W#5P#40AI'm sorry.\x01",
            "...And thank you for everything until now.\x07\x00\x02",
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
            "#12302F#3631V#40W#5P#30AI really love you──everyone.\x07\x00\x02",
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

    # Function_31_4565 end

    def Function_32_6447(): pass

    label("Function_32_6447")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6491")
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_32_6447")

    label("loc_6491")

    Return()

    # Function_32_6447 end

    def Function_33_6492(): pass

    label("Function_33_6492")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64B0")
    OP_A1(0xFE, 0x3E8, 0x8, 0x30, 0x31, 0x32, 0x31, 0x30, 0x33, 0x34, 0x33)
    Jump("Function_33_6492")

    label("loc_64B0")

    Return()

    # Function_33_6492 end

    def Function_34_64B1(): pass

    label("Function_34_64B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64CF")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_34_64B1")

    label("loc_64CF")

    Return()

    # Function_34_64B1 end

    def Function_35_64D0(): pass

    label("Function_35_64D0")

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2EE0, 0x1)
    StopEffect(0x2, 0x2)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    def lambda_653C():
        OP_9B(0x1, 0xFE, 0x0, 0x1964, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_653C)
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

    # Function_35_64D0 end

    def Function_36_662F(): pass

    label("Function_36_662F")

    Sound(2029, 255, 100, 1)

    ChrTalk(
        0x101,
        "#00010F#5P......Urgh......!\x05\x02",
    )


    def lambda_665B():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_665B)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_662F end

    def Function_37_6682(): pass

    label("Function_37_6682")

    Sound(2129, 255, 90, 2)

    ChrTalk(
        0x102,
        "#00106F#12P......Ah......!\x05\x02",
    )


    def lambda_66AD():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66AD)
    SetChrChipByIndex(0xFE, 0x37)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_6682 end

    def Function_38_66D4(): pass

    label("Function_38_66D4")


    def lambda_66D9():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66D9)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_66D4 end

    def Function_39_6700(): pass

    label("Function_39_6700")


    def lambda_6705():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6705)
    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_39_6700 end

    def Function_40_672C(): pass

    label("Function_40_672C")

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

    # Function_40_672C end

    def Function_41_682F(): pass

    label("Function_41_682F")


    def lambda_6834():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6834)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2031, 255, 100, 1)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFDCD8, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 100, 0)
    Return()

    # Function_41_682F end

    def Function_42_6888(): pass

    label("Function_42_6888")


    def lambda_688D():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_688D)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2128, 255, 90, 2)
    OP_9D(0xFE, 0xFFFFFC18, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_6888 end

    def Function_43_68DB(): pass

    label("Function_43_68DB")


    def lambda_68E0():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_68E0)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2224, 255, 100, 3)
    OP_9D(0xFE, 0x3E8, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_68DB end

    def Function_44_692E(): pass

    label("Function_44_692E")


    def lambda_6933():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6933)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2764, 255, 100, 4)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFD508, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_692E end

    def Function_45_6981(): pass

    label("Function_45_6981")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_699A")
    Sound(929, 0, 40, 0)
    Sleep(2200)
    Jump("Function_45_6981")

    label("loc_699A")

    Return()

    # Function_45_6981 end

    def Function_46_699B(): pass

    label("Function_46_699B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69B4")
    Sound(929, 0, 20, 0)
    Sleep(2200)
    Jump("Function_46_699B")

    label("loc_69B4")

    Return()

    # Function_46_699B end

    def Function_47_69B5(): pass

    label("Function_47_69B5")

    Sleep(6000)
    Sound(930, 0, 100, 0)
    Sleep(2000)
    Sound(928, 0, 100, 0)
    Return()

    # Function_47_69B5 end

    def Function_48_69C8(): pass

    label("Function_48_69C8")

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

    # Function_48_69C8 end

    def Function_49_69F3(): pass

    label("Function_49_69F3")

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
        "#00010F#11P#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12P#30W...Nonsense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#30W...Did we have...\x01",
            "A dream...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11P#30WUnfortunately...\x01",
            "...It seems to be reality...\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7571", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#10503F#4069V#5P#40W#N──Exactly.\x02\x03",
            "#10501F#4070VEven after a "miracle",\x01",
            "reality awaits.\x02",
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
        "Voice",
        "#1PThere they are...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Voice",
        (
            "#1PSecretary Arios!\x01",
            "Are you all right!?\x02",
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
        "#00013F#6P#NAah──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#NTch...!\x02",
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
        "Girl's Voice",
        "#3523V#30W#15A──Resistance is futile.\x02",
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
        "#00105F#5PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#5PThis voice...!\x02",
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
            "#3524V#30WThe State Guard has already total\x01",
            "control of the Michelam zone.\x02\x03",
            "#3525VPlease...\x01",
            "Surrender peacefully.\x02",
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
        "#00301F#6PNoｱl, you...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Lloyd",
        "#00013F#6P#N...Why...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10208F#5P#30W............\x02",
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
            "#10503F#5P──Well done, 2nd Lt. Seeker.\x02\x03",
            "#10500FI'll return to Orchis Tower.\x01",
            "I leave their arrest to you.\x02",
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
        "#10201F#11P...Roger...!\x02",
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
        "#00007F#11P──Please wait!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCFE)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W...One thing...\x01",
            "Please answer just one thing.\x02\x03",
            "#00008FIf you have been cooperating\x01",
            "with them for many years...\x02\x03",
            "#00013FThen, is it you who killed Guy\x01",
            "Bannings──my big brother?\x02",
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

    def lambda_77F8():

        label("loc_77F8")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_77F8")

    QueueWorkItem2(0x13, 2, lambda_77F8)
    Sleep(300)

    ChrTalk(
        0x13,
        "#10205F#11PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#5PR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PHey, no way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10500F#5P#40W............\x02",
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
        "#10503F#4058V#5P#40W#30AYes──it's as you say.\x02",
    )

    CloseMessageWindow()
    OP_24(0xFDA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(20000, 5000)
    BeginChrThread(0x9, 0, 0, 73)

    def lambda_7916():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7916)
    Sleep(300)

    def lambda_792E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_792E)
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

    # Function_49_69F3 end

    def Function_50_7A31(): pass

    label("Function_50_7A31")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_7A31 end

    def Function_51_7A51(): pass

    label("Function_51_7A51")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFFC568, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_51_7A51 end

    def Function_52_7A91(): pass

    label("Function_52_7A91")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFEA070, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_7A91 end

    def Function_53_7ACB(): pass

    label("Function_53_7ACB")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF15A0, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_7ACB end

    def Function_54_7B05(): pass

    label("Function_54_7B05")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF5038, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_54_7B05 end

    def Function_55_7B45(): pass

    label("Function_55_7B45")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x3A98, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_55_7B45 end

    def Function_56_7B7F(): pass

    label("Function_56_7B7F")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x15F90, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_56_7B7F end

    def Function_57_7BBF(): pass

    label("Function_57_7BBF")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xEA60, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_57_7BBF end

    def Function_58_7BF9(): pass

    label("Function_58_7BF9")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xAFC8, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_58_7BF9 end

    def Function_59_7C39(): pass

    label("Function_59_7C39")


    def lambda_7C3E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C3E)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_59_7C39 end

    def Function_60_7C75(): pass

    label("Function_60_7C75")


    def lambda_7C7A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C7A)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_60_7C75 end

    def Function_61_7CB1(): pass

    label("Function_61_7CB1")


    def lambda_7CB6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7CB6)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_61_7CB1 end

    def Function_62_7CE7(): pass

    label("Function_62_7CE7")


    def lambda_7CEC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7CEC)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_62_7CE7 end

    def Function_63_7D23(): pass

    label("Function_63_7D23")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_63_7D23 end

    def Function_64_7D33(): pass

    label("Function_64_7D33")

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

    # Function_64_7D33 end

    def Function_65_7D6E(): pass

    label("Function_65_7D6E")

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

    # Function_65_7D6E end

    def Function_66_7DA9(): pass

    label("Function_66_7DA9")

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

    # Function_66_7DA9 end

    def Function_67_7DE4(): pass

    label("Function_67_7DE4")

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

    # Function_67_7DE4 end

    def Function_68_7E1F(): pass

    label("Function_68_7E1F")


    def lambda_7E24():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E24)
    Sound(2029, 255, 70, 0)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_68_7E1F end

    def Function_69_7E5A(): pass

    label("Function_69_7E5A")


    def lambda_7E5F():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E5F)
    Sound(2127, 255, 70, 1)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_69_7E5A end

    def Function_70_7E95(): pass

    label("Function_70_7E95")


    def lambda_7E9A():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E9A)
    Sound(2223, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_70_7E95 end

    def Function_71_7ED0(): pass

    label("Function_71_7ED0")


    def lambda_7ED5():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7ED5)
    Sound(2317, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_71_7ED0 end

    def Function_72_7F0B(): pass

    label("Function_72_7F0B")

    ClearChrFlags(0x9, 0x4)
    OP_9B(0x0, 0xFE, 0x14, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x1964, 0xBB8, 0x0)
    Return()

    # Function_72_7F0B end

    def Function_73_7F3E(): pass

    label("Function_73_7F3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F5C")
    OP_A1(0xFE, 0x5DC, 0x8, 0x1, 0x2, 0x3, 0x2, 0x1, 0x4, 0x5, 0x4)
    Jump("Function_73_7F3E")

    label("loc_7F5C")

    Return()

    # Function_73_7F3E end

    SaveToFile()

Try(main)
