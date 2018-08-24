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
        "Function_6_2BDE",         # 06, 6
        "Function_7_2C4A",         # 07, 7
        "Function_8_2CB6",         # 08, 8
        "Function_9_2D1C",         # 09, 9
        "Function_10_2D88",        # 0A, 10
        "Function_11_2DAA",        # 0B, 11
        "Function_12_2DCC",        # 0C, 12
        "Function_13_2DEE",        # 0D, 13
        "Function_14_2E10",        # 0E, 14
        "Function_15_2E32",        # 0F, 15
        "Function_16_2E42",        # 10, 16
        "Function_17_2E52",        # 11, 17
        "Function_18_2E62",        # 12, 18
        "Function_19_2E72",        # 13, 19
        "Function_20_2E82",        # 14, 20
        "Function_21_2E9D",        # 15, 21
        "Function_22_2EAF",        # 16, 22
        "Function_23_3960",        # 17, 23
        "Function_24_39E3",        # 18, 24
        "Function_25_3A03",        # 19, 25
        "Function_26_3A2D",        # 1A, 26
        "Function_27_3A57",        # 1B, 27
        "Function_28_3A81",        # 1C, 28
        "Function_29_3AC1",        # 1D, 29
        "Function_30_3ADD",        # 1E, 30
        "Function_31_44DB",        # 1F, 31
        "Function_32_63B2",        # 20, 32
        "Function_33_63FD",        # 21, 33
        "Function_34_641C",        # 22, 34
        "Function_35_643B",        # 23, 35
        "Function_36_659A",        # 24, 36
        "Function_37_65ED",        # 25, 37
        "Function_38_663F",        # 26, 38
        "Function_39_666B",        # 27, 39
        "Function_40_6697",        # 28, 40
        "Function_41_679A",        # 29, 41
        "Function_42_67F3",        # 2A, 42
        "Function_43_6846",        # 2B, 43
        "Function_44_6899",        # 2C, 44
        "Function_45_68EC",        # 2D, 45
        "Function_46_6906",        # 2E, 46
        "Function_47_6920",        # 2F, 47
        "Function_48_6933",        # 30, 48
        "Function_49_695E",        # 31, 49
        "Function_50_798E",        # 32, 50
        "Function_51_79AE",        # 33, 51
        "Function_52_79EE",        # 34, 52
        "Function_53_7A28",        # 35, 53
        "Function_54_7A62",        # 36, 54
        "Function_55_7AA2",        # 37, 55
        "Function_56_7ADC",        # 38, 56
        "Function_57_7B1C",        # 39, 57
        "Function_58_7B56",        # 3A, 58
        "Function_59_7B96",        # 3B, 59
        "Function_60_7BD2",        # 3C, 60
        "Function_61_7C0E",        # 3D, 61
        "Function_62_7C44",        # 3E, 62
        "Function_63_7C80",        # 3F, 63
        "Function_64_7C90",        # 40, 64
        "Function_65_7CCB",        # 41, 65
        "Function_66_7D06",        # 42, 66
        "Function_67_7D41",        # 43, 67
        "Function_68_7D7C",        # 44, 68
        "Function_69_7DB7",        # 45, 69
        "Function_70_7DF2",        # 46, 70
        "Function_71_7E2D",        # 47, 71
        "Function_72_7E68",        # 48, 72
        "Function_73_7E9B",        # 49, 73
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
        "#00007F#3321V#30W#20AKeA! Arios!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 170, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107F#3398V#30W#15A...Bell!\x02",
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
        "#3625V#40W...Lloyd... Everyone...\x02",
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
            "#10804F#3780V#5P#30WHehe... You've finally\x01",
            "come.\x02",
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
            "#00107F#3400V#11P#4S#30WWhat are YOU doing\x01",
            "here!?\x02",
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
            "#3781V#30WHehe─ It's simple.\x02\x03",
            "#3782VAs a descendant of the Crois clan\x01",
            "that inherited the Great Sept-\x01",
            "Terrion...\x02\x03",
            "#3783VIt is only natural to carry out my\x01",
            "duty.\x02",
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
        (
            "#00011F#11PThe Great Sept-\x01",
            "Terrion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PIt can't be... The same\x01",
            "as the Aureole that\x01",
            "appeared in Liberl!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10809F#5PHehe. Then this will be\x01",
            "quick.\x02\x03",
            "#10804FThe Sept-Terrions the\x01",
            "Goddess gave to humanity\x01",
            "a long, long time ago...\x02\x03",
            "#10811FOne of them was\x01",
            "inherited by my family.\x02\x03",
            "That was over 1200 years\x01",
            "ago, though.\x02",
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
            "#10804F#5PHehe. Due to an unfortunate event, the\x01",
            "Goddess' Sept-Terrions were lost.\x02\x03",
            "#10803FAs a result, the Crois clan's founders\x01",
            "devised a grand project to recover\x01",
            "their Sept-Terrion at all costs...\x02\x03",
            "#10800FThey decided to construct a giant\x01",
            "Ceremony in the land of Crossbell.\x02",
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
        "#00108F#11PA giant Ceremony...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PDon't tell me... It's the\x01",
            "mysterious giantantic\x01",
            "system using the orbal net?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10803F#5PYes, a Magical Science brought forth\x01",
            "by uniting the current orbal tech\x01",
            "with the Crois clan's alchemy...\x02\x03",
            "#10802FBy using it, an absurdly gigantic\x01",
            "Ceremony can finally be realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11PA Ceremony from Magical\x01",
            "Science...\x02",
        )
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
            "#00006F#11P...I see... So that's how it is.\x02\x03",
            "#00008FThe group of alchemists who built\x01",
            "the Tower of Stargaze long ago and\x01",
            "taught the Cult its techniques...\x02\x03",
            "#00007F─It was you, the Crois clan, that\x01",
            "did those things, right!?\x02",
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
        "#00305F#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#11PB-But... If you think\x01",
            "about it, everything\x01",
            "does line up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PT-Then, even that Cradle\x01",
            "KeA was sleeping in...\x02",
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
            "#10804F#5PHehe. Naturally, the Crois\x01",
            "clan offered it to the Cult.\x02\x03",
            "#10811F─We gave them something to\x01",
            "believe in, so they would work\x01",
            "for us without reservation.\x02",
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
            "#00013F#11PI knew it. Regarding the\x01",
            "D∴G Cult, you really\x01",
            "did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11P...Manipulate it from the\x01",
            "shadows to further the\x01",
            "Crois clan's goals...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PYes, they were nothing\x01",
            "more than puppets.\x02\x03",
            "#10811FHehe... Although they\x01",
            "themselves probably\x01",
            "didn't realize it.\x02",
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
            "#10809F#5PHehe. Hook, line and\x01",
            "sinker, I suppose?\x02\x03",
            "#10805F─Oh, incidentally, Arios'\x01",
            "presence here is not\x01",
            "related to my family.\x02\x03",
            "#10804FThis time, he is a\x01",
            "reliable ally who agrees\x01",
            "with our plan.\x02",
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
        "#00013F#11PArios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P...Are you crazy?\x01",
            "Believin' a delusional\x01",
            "idea like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5PHmph... A delusional\x01",
            "idea, huh.\x02\x03",
            "#10502FIndeed, I too agree in\x01",
            "that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10801F#6PMy...! How rude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PHowever, if, having that\x01",
            "power, they can change\x01",
            "this situation...\x02\x03",
            "I'll go along with their\x01",
            "delusions as much as I\x01",
            "like.\x02\x03",
            "#10501F─Even if it is against\x01",
            "the Goddess' will.\x02",
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
            "#00006F#11P...Honestly, I can't\x01",
            "sort out all these\x01",
            "absurd stories yet...\x02\x03",
            "#00003FI can say only this.\x02",
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
            "#00010F#11PWe'll never accept you\x01",
            "involving KeA in those\x01",
            "delusions!!\x02",
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
            "#00007F#11P#4SKeA, come back to us!\x02\x03",
            "#3SI don't know what they\x01",
            "told you, but you are who\x01",
            "you are! Am I not right?\x02\x03",
            "You've got no reason to\x01",
            "sit there... with such a\x01",
            "painful look on your face!\x02",
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
        "#05812F#5P#30W...Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10804F#5PUhuhu... KeA.\x02\x03",
            "Lloyd says all that.\x01",
            "However...\x02\x03",
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
            "Isn't that what makes\x01",
            "you feel safest!?\x02",
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
            "#00104F...Right. There probably\x01",
            "some situation, but...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FI think there can't be\x01",
            "anything more important\x01",
            "than that.\x02",
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
            "#05814F#40W...............\x02",
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
            "#3719V#30WUhuhu... Having fun,\x01",
            "aren't you?\x07\x00\x02",
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
        "#00110F#11POuroboros!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PAs we thought, you have\x01",
            "a connection with\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#10804F#5PHehe. It's merely a\x01",
            "relationship of mutual\x01",
            "cooperation...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10802F#11P─Everyone. I believe\x01",
            "your preparations are\x01",
            "complete?\x02",
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
            "I think you'll be quite\x01",
            "satisified wtih our\x01",
            "results.\x07\x00\x02",
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
            "The Bells are ready as\x01",
            "well.\x02\x03",
            "All that remains is to\x01",
            "turn that Key.\x07\x00\x02",
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
            "I would be fine waiting\x01",
            "until they understand,\x01",
            "but...\x02\x03",
            "It seems we're out of\x01",
            "time, yes?\x07\x00\x02",
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
        "#10800F#11PMy, my.\x02",
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
        (
            "#00011F#11PW-What're you\x01",
            "saying...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11POut of time for what!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PIsn't it obvious?──\x02\x03",
            "#10501FIt's the invasion of the\x01",
            "Imperial and Republican\x01",
            "armies.\x02",
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
        "#00110F#11PAh...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#10809F#5PHehe. Since we're all\x01",
            "here, should we watch it\x01",
            "live?\x02",
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

    def Function_6_2BDE(): pass

    label("Function_6_2BDE")


    def lambda_2BE3():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BE3)

    def lambda_2BF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BF8)
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_2BDE end

    def Function_7_2C4A(): pass

    label("Function_7_2C4A")


    def lambda_2C4F():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C4F)

    def lambda_2C64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C64)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_2C4A end

    def Function_8_2CB6(): pass

    label("Function_8_2CB6")


    def lambda_2CBB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CBB)

    def lambda_2CD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CD0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_2CB6 end

    def Function_9_2D1C(): pass

    label("Function_9_2D1C")


    def lambda_2D21():
        OP_9B(0x0, 0xFE, 0x0, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D21)

    def lambda_2D36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D36)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_2D1C end

    def Function_10_2D88(): pass

    label("Function_10_2D88")

    OP_71(0x0, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_10_2D88 end

    def Function_11_2DAA(): pass

    label("Function_11_2DAA")

    OP_71(0x1, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_11_2DAA end

    def Function_12_2DCC(): pass

    label("Function_12_2DCC")

    OP_71(0x2, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_12_2DCC end

    def Function_13_2DEE(): pass

    label("Function_13_2DEE")

    OP_71(0x3, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x3)
    OP_71(0x3, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_13_2DEE end

    def Function_14_2E10(): pass

    label("Function_14_2E10")

    OP_71(0x4, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_14_2E10 end

    def Function_15_2E32(): pass

    label("Function_15_2E32")

    OP_71(0x0, 0xF5, 0x12C, 0x0, 0x8)
    OP_79(0x0)
    Return()

    # Function_15_2E32 end

    def Function_16_2E42(): pass

    label("Function_16_2E42")

    OP_71(0x1, 0xFA, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    Return()

    # Function_16_2E42 end

    def Function_17_2E52(): pass

    label("Function_17_2E52")

    OP_71(0x2, 0xFF, 0x12C, 0x0, 0x8)
    OP_79(0x2)
    Return()

    # Function_17_2E52 end

    def Function_18_2E62(): pass

    label("Function_18_2E62")

    OP_71(0x3, 0x104, 0x12C, 0x0, 0x8)
    OP_79(0x3)
    Return()

    # Function_18_2E62 end

    def Function_19_2E72(): pass

    label("Function_19_2E72")

    OP_71(0x4, 0x10E, 0x12C, 0x0, 0x8)
    OP_79(0x4)
    Return()

    # Function_19_2E72 end

    def Function_20_2E82(): pass

    label("Function_20_2E82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E9C")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_20_2E82")

    label("loc_2E9C")

    Return()

    # Function_20_2E82 end

    def Function_21_2E9D(): pass

    label("Function_21_2E9D")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_21_2E9D end

    def Function_22_2EAF(): pass

    label("Function_22_2EAF")

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
        "#00311FThey really did come!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 170, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FBut with the CGF's battle\x01",
            "strength, even if they\x01",
            "tried to stop them...\x02",
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
            "─The girl is the Key\x01",
            "that will overthrow\x01",
            "them.\x07\x00\x02",
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
            "Ladies and gentlemen of\x01",
            "Ouroboros. I thank you for\x01",
            "your cooperation with my plan.\x02\x03",
            "Bell and Arios too. It seems\x01",
            "everything is going according\x01",
            "to plan?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        "#10804F#5PYes. So far so good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5P...We can only leave the\x01",
            "rest to her.\x02",
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
            "─You heard them, Miss\x01",
            "KeA.\x02\x03",
            "You understand, don't\x01",
            "you?\x02\x03",
            "That you're the only one\x01",
            "who can do anything\x01",
            "about this situation─\x02",
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
        "#05803F#5P#30W............ (*nods*)\x02",
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
        "#10811F#5PHehe, what a good girl.\x02",
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

    # Function_22_2EAF end

    def Function_23_3960(): pass

    label("Function_23_3960")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39E2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3990")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_39DA")

    label("loc_3990")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B5")
    OP_82(0xA, 0x1E, 0xBB8, 0x1F4)
    Jump("loc_39DA")

    label("loc_39B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DA")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_39DA")

    label("loc_39DA")

    Sleep(500)
    Jump("Function_23_3960")

    label("loc_39E2")

    Return()

    # Function_23_3960 end

    def Function_24_39E3(): pass

    label("Function_24_39E3")

    SetMapObjFrame(0xFF, "chair", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    Return()

    # Function_24_39E3 end

    def Function_25_3A03(): pass

    label("Function_25_3A03")

    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on_ani")
    Sleep(1133)
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    Return()

    # Function_25_3A03 end

    def Function_26_3A2D(): pass

    label("Function_26_3A2D")

    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    Return()

    # Function_26_3A2D end

    def Function_27_3A57(): pass

    label("Function_27_3A57")

    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_27_3A57 end

    def Function_28_3A81(): pass

    label("Function_28_3A81")

    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_28_3A81 end

    def Function_29_3AC1(): pass

    label("Function_29_3AC1")

    Sleep(500)
    Sound(162, 0, 100, 0)
    Sleep(400)
    Sound(162, 0, 100, 0)
    Sleep(300)
    Sound(162, 0, 100, 0)
    Return()

    # Function_29_3AC1 end

    def Function_30_3ADD(): pass

    label("Function_30_3ADD")

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
        "#00007F#11P#4S─KeA, no!\x02",
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
            "#00310F#11PI don't get it, but we\x01",
            "won't let you do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PIn any case... Let's\x01",
            "stop them!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -8500, 1000)

    def lambda_3E6D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E6D)
    Sleep(50)

    def lambda_3E85():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E85)
    Sleep(50)

    def lambda_3E9D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E9D)
    Sleep(50)

    def lambda_3EB5():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EB5)
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

    def lambda_3FBB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FBB)
    Sleep(50)

    def lambda_3FD3():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FD3)
    Sleep(50)

    def lambda_3FEB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FEB)
    Sleep(50)

    def lambda_4003():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4003)
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
        (
            "#00311F#4P#NThe Divine Blade of\x01",
            "Wind...\x02",
        )
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
            "#4055V#40W...If you want to pass, come at me\x01",
            "all together.\x02\x03",
            "#4056VThe Barrier Guy, Sergei and I\x01",
            "couldn't overcome─\x02\x03",
            "#4057V#30WShow me if you have the power to\x01",
            "overcome it!\x02",
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
        "#00010F#3322V#6P#N#30W#15AGuh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00307F#2766V#6P#N#30W#20ADon't freak out, he's\x01",
            "alone!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00107F#3401V#6P#N#30W#20AIf we can grasp victory\x01",
            "somehow...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00207F#2684V#12P#N#30W#25AAeon System, full\x01",
            "activation! I'll destroy\x01",
            "the target!\x02",
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

    def lambda_4427():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4427)

    def lambda_443C():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_443C)

    def lambda_4451():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4451)

    def lambda_4466():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4466)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_24(0x3A3)
    OP_24(0x340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_44B9")
    Battle("BattleInfo_3E0", 0x0, 0x0, 0x100, 0x3F, 0xFF)
    Jump("loc_44C9")

    label("loc_44B9")

    Battle("BattleInfo_39C", 0x0, 0x0, 0x100, 0x3F, 0xFF)

    label("loc_44C9")

    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Return()

    # Function_30_3ADD end

    def Function_31_44DB(): pass

    label("Function_31_44DB")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4861")
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
    Jump("loc_4ACA")

    label("loc_4861")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4935")
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
    Jump("loc_4ACA")

    label("loc_4935")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A09")
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
    Jump("loc_4ACA")

    label("loc_4A09")

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

    label("loc_4ACA")

    PlayBGM("ed7572", 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5020")
    OP_2C(0xAD, 0x5)

    ChrTalk(
        0x101,
        "#00002F#6P#NW-We did it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x103,
        "Randy",
        (
            "#00302F#12P#NHah... It's that all\x01",
            "you've got?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#10504F#5P...Hmph... You surprised\x01",
            "me.\x02\x03",
            "#10502FIf this is how it is...\x01",
            "then you might really\x01",
            "surpass us.\x02",
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

    def lambda_4D88():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D88)
    Sleep(50)

    def lambda_4D98():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D98)
    Sleep(50)

    def lambda_4DA8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4DA8)
    Sleep(50)

    def lambda_4DB8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4DB8)
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
        "#15A#10503F#11P─Second Form, Gale.\x02",
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
    Jump("loc_52E8")

    label("loc_5020")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5101")
    OP_2C(0xAD, 0x3)

    ChrTalk(
        0x101,
        (
            "#00010F#11P#30WKh... ...We came so\x01",
            "far...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11P#30WAs if we'd let this end\x01",
            "here... like this...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10504F#5P...You've grown.\x02\x03",
            "#10502FYou all may be able to\x01",
            "surpass us, one day.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_52E8")

    label("loc_5101")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5218")
    OP_2C(0xAD, 0x1)

    ChrTalk(
        0x101,
        "#00006F#11P#30WGuh... *pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P#30WThe difference in our\x01",
            "fighting abilities... is\x01",
            "too great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PNot too bad, but you're\x01",
            "too straightforward.\x02\x03",
            "#10501FAt this rate, you'll\x01",
            "never be on the level we\x01",
            "were, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_52E8")

    label("loc_5218")


    ChrTalk(
        0x101,
        "#00006F#11P#40W...Ghh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P#40WT-To think we were this\x01",
            "poor of a match for\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10503F#5PYou lack focus.\x02\x03",
            "#10500FLike that, you won't be\x01",
            "able to protect what's\x01",
            "important to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_52E8")

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
            "#10804F#6P#NHehe, he struck them\x01",
            "with the back of his\x01",
            "blade.\x02\x03",
            "#10811FThings won't go well if\x01",
            "you interrupt your\x01",
            "concentration, you know?\x02",
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
            "#25A#05801F#3628V#30WI won't... Hesitate\x01",
            "anymore...!\x02",
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
            "#00210F#11PHigh-density elemental\x01",
            "spirit particle data\x01",
            "are...!\x02",
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
        "#00005F......Ah......\x02",
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
            "#10804F#3784V#40W......Uhuhu... It was a\x01",
            "success....\x02\x03",
            "#10811F#3785VIt's the revival of the\x01",
            "lost Sept-Terrion of\x01",
            "Mirage...\x02\x03",
            "#10809F#3786V#30WNo, it is the birth of\x01",
            "the Sept-Terrion of Zero\x01",
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
        (
            "#00201FT-The Sept-Terrion of\x01",
            "Zero...\x02",
        )
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
            "#00013F#3325V#40W......KeA...... Are you\x01",
            "really... KeA...?\x02",
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
            "#10804F#11PHehe, very well.\x02\x03",
            "#10800FArios, I leave them to\x01",
            "you.\x02",
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

    def lambda_605B():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_605B)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1000)

    def lambda_6081():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6081)
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
            "#12304F#3630V#5P#40W#5P#40AI'm sorry. ...And thank\x01",
            "you for everything.\x07\x00\x02",
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
            "#12302F#3631V#40W#5P#30AI really do love you──\x01",
            "everyone.\x07\x00\x02",
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

    # Function_31_44DB end

    def Function_32_63B2(): pass

    label("Function_32_63B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63FC")
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_32_63B2")

    label("loc_63FC")

    Return()

    # Function_32_63B2 end

    def Function_33_63FD(): pass

    label("Function_33_63FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_641B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x30, 0x31, 0x32, 0x31, 0x30, 0x33, 0x34, 0x33)
    Jump("Function_33_63FD")

    label("loc_641B")

    Return()

    # Function_33_63FD end

    def Function_34_641C(): pass

    label("Function_34_641C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_34_641C")

    label("loc_643A")

    Return()

    # Function_34_641C end

    def Function_35_643B(): pass

    label("Function_35_643B")

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2EE0, 0x1)
    StopEffect(0x2, 0x2)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    def lambda_64A7():
        OP_9B(0x1, 0xFE, 0x0, 0x1964, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64A7)
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

    # Function_35_643B end

    def Function_36_659A(): pass

    label("Function_36_659A")

    Sound(2029, 255, 100, 1)

    ChrTalk(
        0x101,
        "#00010F#5P......Urgh......!\x05\x02",
    )


    def lambda_65C6():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65C6)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_659A end

    def Function_37_65ED(): pass

    label("Function_37_65ED")

    Sound(2129, 255, 90, 2)

    ChrTalk(
        0x102,
        "#00106F#12P......Ah......!\x05\x02",
    )


    def lambda_6618():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6618)
    SetChrChipByIndex(0xFE, 0x37)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_65ED end

    def Function_38_663F(): pass

    label("Function_38_663F")


    def lambda_6644():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6644)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_663F end

    def Function_39_666B(): pass

    label("Function_39_666B")


    def lambda_6670():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6670)
    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_39_666B end

    def Function_40_6697(): pass

    label("Function_40_6697")

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

    # Function_40_6697 end

    def Function_41_679A(): pass

    label("Function_41_679A")


    def lambda_679F():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_679F)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2031, 255, 100, 1)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFDCD8, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 100, 0)
    Return()

    # Function_41_679A end

    def Function_42_67F3(): pass

    label("Function_42_67F3")


    def lambda_67F8():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_67F8)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2128, 255, 90, 2)
    OP_9D(0xFE, 0xFFFFFC18, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_67F3 end

    def Function_43_6846(): pass

    label("Function_43_6846")


    def lambda_684B():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_684B)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2224, 255, 100, 3)
    OP_9D(0xFE, 0x3E8, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_6846 end

    def Function_44_6899(): pass

    label("Function_44_6899")


    def lambda_689E():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_689E)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2764, 255, 100, 4)
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFD508, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_6899 end

    def Function_45_68EC(): pass

    label("Function_45_68EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6905")
    Sound(929, 0, 40, 0)
    Sleep(2200)
    Jump("Function_45_68EC")

    label("loc_6905")

    Return()

    # Function_45_68EC end

    def Function_46_6906(): pass

    label("Function_46_6906")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_691F")
    Sound(929, 0, 20, 0)
    Sleep(2200)
    Jump("Function_46_6906")

    label("loc_691F")

    Return()

    # Function_46_6906 end

    def Function_47_6920(): pass

    label("Function_47_6920")

    Sleep(6000)
    Sound(930, 0, 100, 0)
    Sleep(2000)
    Sound(928, 0, 100, 0)
    Return()

    # Function_47_6920 end

    def Function_48_6933(): pass

    label("Function_48_6933")

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

    # Function_48_6933 end

    def Function_49_695E(): pass

    label("Function_49_695E")

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
            "#00106F#6P#30W...Did we have... a\x01",
            "dream...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11P#30WUnfortunately... ...It\x01",
            "seems to be reality...\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7571", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#10503F#4069V#5P#40W#N─Exactly.\x02\x03",
            "#10501F#4070VEven after a Miracle,\x01",
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
            "#1PSecretary Arios! Are you\x01",
            "all right!?\x02",
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
        "#3523V#30W#15A─Resistance is futile.\x02",
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
        "#00105F#5PHuh...\x02",
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
            "#3525VPlease... Surrender peacefully.\x02",
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
            "#10503F#5P─Well done, 2nd Lt.\x01",
            "Seeker.\x02\x03",
            "#10500FI'll return to Orchis\x01",
            "Tower. I leave their\x01",
            "arrest to you.\x02",
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
        "#10201F#11P...Roger!\x02",
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
        "#00007F#11P─Please wait!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCFE)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W...One thing... Please\x01",
            "answer just one thing.\x02\x03",
            "#00008FIf you have been\x01",
            "cooperating with them\x01",
            "for many years...\x02\x03",
            "#00013FThen, was it you who\x01",
            "killed Guy Bannings─ my\x01",
            "big brother?\x02",
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

    def lambda_7755():

        label("loc_7755")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7755")

    QueueWorkItem2(0x13, 2, lambda_7755)
    Sleep(300)

    ChrTalk(
        0x13,
        "#10205F#11PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PWhoa, no way...\x02",
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
        "#10503F#4058V#5P#40W#30AYes─ It is as you say.\x02",
    )

    CloseMessageWindow()
    OP_24(0xFDA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(20000, 5000)
    BeginChrThread(0x9, 0, 0, 73)

    def lambda_7873():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7873)
    Sleep(300)

    def lambda_788B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_788B)
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

    # Function_49_695E end

    def Function_50_798E(): pass

    label("Function_50_798E")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_798E end

    def Function_51_79AE(): pass

    label("Function_51_79AE")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFFC568, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_51_79AE end

    def Function_52_79EE(): pass

    label("Function_52_79EE")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFEA070, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_79EE end

    def Function_53_7A28(): pass

    label("Function_53_7A28")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF15A0, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_7A28 end

    def Function_54_7A62(): pass

    label("Function_54_7A62")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF5038, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_54_7A62 end

    def Function_55_7AA2(): pass

    label("Function_55_7AA2")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x3A98, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_55_7AA2 end

    def Function_56_7ADC(): pass

    label("Function_56_7ADC")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x15F90, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_56_7ADC end

    def Function_57_7B1C(): pass

    label("Function_57_7B1C")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xEA60, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_57_7B1C end

    def Function_58_7B56(): pass

    label("Function_58_7B56")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xAFC8, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_58_7B56 end

    def Function_59_7B96(): pass

    label("Function_59_7B96")


    def lambda_7B9B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B9B)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_59_7B96 end

    def Function_60_7BD2(): pass

    label("Function_60_7BD2")


    def lambda_7BD7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7BD7)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_60_7BD2 end

    def Function_61_7C0E(): pass

    label("Function_61_7C0E")


    def lambda_7C13():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C13)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_61_7C0E end

    def Function_62_7C44(): pass

    label("Function_62_7C44")


    def lambda_7C49():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C49)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_62_7C44 end

    def Function_63_7C80(): pass

    label("Function_63_7C80")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_63_7C80 end

    def Function_64_7C90(): pass

    label("Function_64_7C90")

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

    # Function_64_7C90 end

    def Function_65_7CCB(): pass

    label("Function_65_7CCB")

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

    # Function_65_7CCB end

    def Function_66_7D06(): pass

    label("Function_66_7D06")

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

    # Function_66_7D06 end

    def Function_67_7D41(): pass

    label("Function_67_7D41")

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

    # Function_67_7D41 end

    def Function_68_7D7C(): pass

    label("Function_68_7D7C")


    def lambda_7D81():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D81)
    Sound(2029, 255, 70, 0)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_68_7D7C end

    def Function_69_7DB7(): pass

    label("Function_69_7DB7")


    def lambda_7DBC():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7DBC)
    Sound(2127, 255, 70, 1)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_69_7DB7 end

    def Function_70_7DF2(): pass

    label("Function_70_7DF2")


    def lambda_7DF7():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DF7)
    Sound(2223, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_70_7DF2 end

    def Function_71_7E2D(): pass

    label("Function_71_7E2D")


    def lambda_7E32():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7E32)
    Sound(2317, 255, 70, 2)
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_71_7E2D end

    def Function_72_7E68(): pass

    label("Function_72_7E68")

    ClearChrFlags(0x9, 0x4)
    OP_9B(0x0, 0xFE, 0x14, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x1964, 0xBB8, 0x0)
    Return()

    # Function_72_7E68 end

    def Function_73_7E9B(): pass

    label("Function_73_7E9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EB9")
    OP_A1(0xFE, 0x5DC, 0x8, 0x1, 0x2, 0x3, 0x2, 0x1, 0x4, 0x5, 0x4)
    Jump("Function_73_7E9B")

    label("loc_7EB9")

    Return()

    # Function_73_7E9B end

    SaveToFile()

Try(main)
