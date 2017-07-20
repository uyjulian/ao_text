from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1090.bin",                # FileName
        "m1090",                    # MapName
        "m1090",                    # Location
        0x0072,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 114, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1090",                  # 0
        "Ariane Road",         # 1
        "The maid of the sword Jeanne",       # 2
        "Reims",                 # 3
        "Ariane Road",         # 4
        "Keya",                 # 5
        "SE control",                 # 6
        "bm1070",                 # 7
    ))

    ATBonus("ATBonus_1CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_270", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_278", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_27C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_280", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_284", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2AC", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bm1070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03500.dat", 0, 0, 0, 0, 0, "ms04200.dat", 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_26C", "ed7458", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   -14.5,                 5.5,                   -1.0,                  306.25,                [0.10101521760225296,  0.1414213925600052,    -0.0,                  0.0,                   -0.10101528465747833,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.0203046798706055,    1.2727930545806885,    0.19999998807907104,   1.0])

    ChipFrameInfo(812, 0)                                        # 0

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_356",          # 01, 1
        "Function_2_57A",          # 02, 2
        "Function_3_789",          # 03, 3
        "Function_4_7AE",          # 04, 4
        "Function_5_7D3",          # 05, 5
        "Function_6_1BF3",         # 06, 6
        "Function_7_1C12",         # 07, 7
        "Function_8_1D4C",         # 08, 8
        "Function_9_1DDE",         # 09, 9
        "Function_10_1E03",        # 0A, 10
        "Function_11_1E3C",        # 0B, 11
        "Function_12_1E56",        # 0C, 12
        "Function_13_4E36",        # 0D, 13
        "Function_14_4E5D",        # 0E, 14
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_343")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 2)
    Jump("loc_355")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_355")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)

    label("loc_355")

    Return()

    # Function_0_32C end

    def Function_1_356(): pass

    label("Function_1_356")

    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_404")
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C7")
    LoadEffect(0x9, "map/mpbell02.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x1, 0x1)

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_4DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F5")

    label("loc_4DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_50A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_50A")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53F")
    OP_24(0x84)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_561")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    OP_24(0x84)
    Sound(828, 1, 70, 0)
    Jump("loc_561")

    label("loc_55B")

    Sound(132, 1, 70, 0)

    label("loc_561")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_579")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_579")

    Return()

    # Function_1_356 end

    def Function_2_57A(): pass

    label("Function_2_57A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03500.itc", 0x1E)
    LoadChrToIndex("chr/ch43100.itc", 0x1F)
    LoadEffect(0x0, "battle/cr037100.eff")
    LoadEffect(0x1, "map/mpbell.eff")
    SoundLoad(828)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, -5740, 1190, 40, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -6360, 1090, -1240, 45)
    SetChrFlags(0x9, 0x4)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    Sound(828, 2, 100, 0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_68(-3620, 3240, 10, 0)
    MoveCamera(90, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(33000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 3450, 0, 7000)
    MoveCamera(60, 15, 0, 7000)
    SetCameraDistance(21000, 7000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(28000, 10000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x19)
    Sleep(1)
    CancelBlur(4000)
    Sound(929, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 3)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Sound(829, 0, 100, 0)
    Sleep(4000)
    StopSound(828, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r3080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_57A end

    def Function_3_789(): pass

    label("Function_3_789")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AD")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_3_789")

    label("loc_7AD")

    Return()

    # Function_3_789 end

    def Function_4_7AE(): pass

    label("Function_4_7AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D2")
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_4_7AE")

    label("loc_7D2")

    Return()

    # Function_4_7AE end

    def Function_5_7D3(): pass

    label("Function_5_7D3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_841")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85F")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_85F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_87D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B9")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D7")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_8D7")

    LoadChrToIndex("chr/ch03500.itc", 0x2A)
    LoadChrToIndex("chr/ch03550.itc", 0x2B)
    LoadChrToIndex("chr/ch03551.itc", 0x2C)
    LoadChrToIndex("chr/ch03552.itc", 0x2D)
    LoadChrToIndex("chr/ch03553.itc", 0x2E)
    LoadChrToIndex("chr/ch03554.itc", 0x2F)
    LoadChrToIndex("chr/ch03557.itc", 0x30)
    LoadChrToIndex("apl/ch51408.itc", 0x31)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(1, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis286.itp")
    LoadEffect(0x0, "event\\ev17090.eff")
    LoadEffect(0x1, "event\\ev14015.eff")
    SoundLoad(3899)
    SoundLoad(3900)
    SoundLoad(3901)
    SoundLoad(3902)
    SoundLoad(3903)
    SoundLoad(3904)
    SoundLoad(3905)
    SoundLoad(3632)
    SoundLoad(3633)
    SoundLoad(825)
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13110, 0, 5580, 90)
    SetChrPos(0x102, -13470, 0, 4350, 90)
    SetChrPos(0x103, -13880, 0, 6630, 90)
    SetChrPos(0x104, -13680, 0, 2960, 90)
    SetChrPos(0xF4, -15080, 0, 6140, 90)
    SetChrPos(0xF5, -14780, 0, 3600, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16250, 0, -8350, 45)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 17450, 0, -5600, 225)
    SetChrFlags(0xC, 0x8)
    OP_68(-5900, 5140, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_68(-5900, 2140, 0, 8000)
    OP_6F(0x79)
    OP_0D()
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 5000)
    OP_6E(550, 5000)
    SetCameraDistance(18150, 5000)

    def lambda_B17():
        OP_95(0xFE, -14680, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B17)
    Sleep(50)

    def lambda_B34():
        OP_95(0xFE, -15780, 0, -1400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B34)
    Sleep(50)

    def lambda_B51():
        OP_95(0xFE, -14470, 0, -650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B51)
    Sleep(50)

    def lambda_B6E():
        OP_95(0xFE, -14110, 0, 580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6E)
    Sleep(50)

    def lambda_B8B():
        OP_95(0xFE, -16079, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B8B)
    Sleep(50)

    def lambda_BA8():
        OP_95(0xFE, -14880, 0, 1630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA8)
    WaitChrThread(0x104, 1)

    def lambda_BC6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC6)
    WaitChrThread(0xF5, 1)

    def lambda_BD7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BD7)
    WaitChrThread(0x102, 1)

    def lambda_BE8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE8)
    WaitChrThread(0x101, 1)

    def lambda_BF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF9)
    WaitChrThread(0xF4, 1)

    def lambda_C0A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C0A)
    WaitChrThread(0x103, 1)

    def lambda_C1B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C1B)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 11)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#3899V#3C#40W#20AYou came?\x02\x03",
            "#3900V#35AApparently preparedness and determination\x01",
            "It looks like it got stuck.\x02",
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

    ChrTalk(
        0x102,
        "#00101F#6P#N\"steel#2RGlasses#The saint of \"… ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#6P#N\"Eating snake#10RUroboros#\"The apostle? …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6P#N── \"Clown#6RCampanella#\"To say\x01",
            "Your plan and doing\x01",
            "Have you already moved to the Imperial direction?\x02\x03",
            "#00001FNo more crossbells\x01",
            "Is it necessary to stay alive?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04900F#3C#30WNo, in reality there is not.\x02\x03",
            "Dr. Potential of \"Zero's treasure\"\x01",
            "I am interested but …\x02\x03",
            "Already from our plan\x01",
            "It is an existence that has come off.\x02\x03",
            "Afterwards with the people of the Clois family\x01",
            "It will be your problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F5C")

    ChrTalk(
        0x109,
        "#10107F#6P#NIf so, why …?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_F5C")


    ChrTalk(
        0x106,
        "#10701F#6P#NThen why…!?\x02",
    )

    CloseMessageWindow()

    label("loc_F82")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE3")

    ChrTalk(
        0x105,
        (
            "#10406F#6P#NHonestly, if it does not matter\x01",
            "I'd like to collect it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1027")

    label("loc_FE3")


    ChrTalk(
        0x104,
        (
            "#00306F#12P#N…… If it does not matter\x01",
            "To be honest, I would like to return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1027")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04900F#3CIt is a simple matter.\x02\x03",
            "From the Treasure of \"Treasure\"\x01",
            "It was because I was asked directly.\x02",
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
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00005F#6P#NHuh!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#6P#NFrom KeA?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x33C, 0xA)
    OP_CB(0x1, 0x1, 0x41A, 0x41A, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x1)
    Sleep(800)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#04924F#3901V#11P#3C#25A#40WI shall accept\x02\x03",
            "#04922F#3902V#40ATo the utmost of Miko 's will,\x01",
            "I am talking to the \"leader\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12304F#3632V#5P#13C#20A#40WThank you.\x02\x03",
            "#12302F#3633V#35AAlso to your master\x01",
            "Tell me a thank you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x1, 0x1, 0x47E, 0x47E, 0x5DC, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToBright(1500, 16777215)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x33C, 0x1E)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#04900F#3C#30W\"Soldier\" to \"demon\" ……\x01",
            "Both of us as a person\x01",
            "Those who exceeded#2RAfter all#I am.\x02\x03",
            "If you proceed further\x01",
            "You can not stay safe.\x02\x03",
            "I do not want to see a scratch figure ……\x01",
            "That was said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#30W#6P#NKeA…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00308F#30W#12P#NKeA… you said that…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#N#30WThank you, Iron Maiden\x02\x03",
            "#00000F#20WThanks to your hesitation\x01",
            "I feel completely disconnected.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    SetCameraDistance(17000, 500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1574")
    Sound(540, 0, 50, 0)

    label("loc_1574")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#04900F#3C… … process.\x01",
            "Does that happen by listening to the current story?\x02\x03",
            "Apparently the last push\x01",
            "You seem to have done it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6P#NOh ─ ─ Anything to you\x01",
            "Retire there#2RWhen#To have it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00104F#6P#NOvercome the \"wall\"\x01",
            "To hug that girl … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#00307F#12P#NIf I retire here\x01",
            "Male waste#2RSoda#Ru it's alright …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#6P#NSame for a girl!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1789")

    ChrTalk(
        0x105,
        (
            "#10402F#6P#NGhost, apparently\x01",
            "It seems that the fire has completely turned on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1789")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17D9")

    ChrTalk(
        0x106,
        (
            "#10706F#6P#NEveryone's feelings …\x01",
            "…… I understand it painfully.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(
        0x109,
        (
            "#10107F#6P#Nme too……\x01",
            "I will do my best to help you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1827")

    Sleep(500)

    ChrTalk(
        0x8,
        "#04900F#3C#30WHmm. Fine\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    OP_68(-5900, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    BeginChrThread(0x8, 3, 0, 7)
    WaitChrThread(0x8, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    StopSound(828, 500, 30)
    OP_68(-12700, 2420, 0, 16000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#3903V#3C#30W#40ASeven pillars of the serpent's apostles,\x01",
            "Ariane Road of \"Steel\" ……\x02\x03",
            "#3904V#48AFollowing the wishes of the \"Zero\"\x01",
            "I will not stand as a wall here.\x02\x03",
            "#3905V#30ANow, let us fight!\x07\x00\x02",
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
    Sleep(500)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 10)
    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Sound(2055, 255, 100, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A40")
    OP_FC(0x4)
    Sound(2478, 255, 100, 5)
    Jump("loc_1A49")

    label("loc_1A40")

    OP_FC(0x3)
    Sound(2478, 255, 100, 4)

    label("loc_1A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A76")
    Sound(2417, 255, 100, 5)
    Jump("loc_1A7C")

    label("loc_1A76")

    Sound(2417, 255, 100, 4)

    label("loc_1A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA9")
    Sound(3174, 255, 100, 5)
    Jump("loc_1AAF")

    label("loc_1AA9")

    Sound(3174, 255, 100, 4)

    label("loc_1AAF")

    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Lloyd's")

    AnonymousTalk(
        0xFF,
        "#5S#12ARight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 0)
    Sound(829, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5900, 1640, 0, 1000)

    def lambda_1B14():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B14)

    def lambda_1B29():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B29)

    def lambda_1B3E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B3E)

    def lambda_1B53():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B53)

    def lambda_1B68():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1B68)

    def lambda_1B7D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1B7D)
    Sleep(350)
    StopSound(825, 300, 100)
    StopSound(832, 300, 100)
    FadeToDark(0, -1, 0)
    FadeToDark(650, 16777215, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x0)
    Battle("BattleInfo_2AC", 0x0, 0x0, 0x100, 0x40, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 12)
    Return()

    # Function_5_7D3 end

    def Function_6_1BF3(): pass

    label("Function_6_1BF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C11")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_1BF3")

    label("loc_1C11")

    Return()

    # Function_6_1BF3 end

    def Function_7_1C12(): pass

    label("Function_7_1C12")

    Fade(500)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x31)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    OP_0D()
    SetCameraDistance(15000, 2000)
    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0xFE, 0x5, 0, 2200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1)
    CancelBlur(2500)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0xF)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -5900, 3300, -150, 0)

    def lambda_1CE7():
        OP_96(0xFE, 0xFFFFE8F4, 0x866, 0xFFFFFF6A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CE7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    Sound(288, 0, 70, 0)
    SetChrFlags(0xA, 0x80)
    OP_82(0x32, 0x0, 0x1388, 0x12C)
    OP_A1(0xFE, 0x4B0, 0x3, 0x5, 0x6, 0x7)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1C12 end

    def Function_8_1D4C(): pass

    label("Function_8_1D4C")

    Fade(500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x1F4, 0x1388, 0x1F4)
    Sound(825, 2, 100, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 100, 0)
    Sound(833, 0, 70, 0)
    SetCameraDistance(14500, 500)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0x0, 0xFE, 0x5, 0, 0, -750, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 2000)
    BeginChrThread(0x8, 0, 0, 6)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(1000)
    BeginChrThread(0xFE, 2, 0, 9)
    Return()

    # Function_8_1D4C end

    def Function_9_1DDE(): pass

    label("Function_9_1DDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E02")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_9_1DDE")

    label("loc_1E02")

    Return()

    # Function_9_1DDE end

    def Function_10_1E03(): pass

    label("Function_10_1E03")

    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_1E17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E3B")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("loc_1E17")

    label("loc_1E3B")

    Return()

    # Function_10_1E03 end

    def Function_11_1E3C(): pass

    label("Function_11_1E3C")

    OP_25(0x33C, 0x3C)
    Sleep(400)
    OP_25(0x33C, 0x32)
    Sleep(400)
    OP_25(0x33C, 0x28)
    Sleep(400)
    OP_25(0x33C, 0x1E)
    Return()

    # Function_11_1E3C end

    def Function_12_1E56(): pass

    label("Function_12_1E56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EB0")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_1EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ECE")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_1ECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EEC")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_1EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F0A")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_1F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F28")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_1F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F46")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_1F46")

    LoadChrToIndex("chr/ch04250.itc", 0x2B)
    LoadChrToIndex("chr/ch04253.itc", 0x2E)
    LoadChrToIndex("chr/ch04254.itc", 0x2F)
    LoadChrToIndex("chr/ch00001.itc", 0x30)
    LoadChrToIndex("chr/ch00301.itc", 0x31)
    LoadChrToIndex("chr/ch02901.itc", 0x32)
    LoadChrToIndex("chr/ch03201.itc", 0x33)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(132)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13700.itp")
    SoundLoad(3906)
    SoundLoad(3907)
    SoundLoad(3908)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14110, 0, 580, 90)
    SetChrPos(0x102, -14470, 0, -650, 90)
    SetChrPos(0x103, -14880, 0, 1630, 90)
    SetChrPos(0x104, -14680, 0, -2040, 90)
    SetChrPos(0xF4, -16079, 0, 1140, 90)
    SetChrPos(0xF5, -15780, 0, -1400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AB")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_20E3")

    label("loc_20AB")

    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x29)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    label("loc_20E3")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5900, 2140, 0, 0)
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16149, 0)
    SetCameraDistance(18150, 5000)
    BeginChrThread(0xD, 1, 0, 11)
    PlayBGM("ed7584", 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B65")
    OP_2C(0xB0, 0x5)
    OP_29(0xB0, 0x1, 0x7)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#13703F#40W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#40W#6P#NHa Ha……\x01",
            "How is it …?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#40W#12P#NHere, this is ours\x01",
            "I'm the best guy … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13704F#30WI am surprised. \x02\x03",
            "#13702FThose who kneel on me\x01",
            "What does it mean to appear again …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_22D8():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22D8)
    Sleep(250)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 40, 0)
    Sound(358, 0, 60, 0)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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
        0x101,
        "#00010F#6P#NUgh!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244E")

    ChrTalk(
        0x105,
        "#10410F#6P#N#40WShe can still stand!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2479")

    label("loc_244E")


    ChrTalk(
        0x106,
        "#10707F#6P#N#40WI can stand still …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2479")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24C6")

    ChrTalk(
        0x109,
        (
            "#10107F#6P#N#40WBut,\x01",
            "Here too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_24FA")

    label("loc_24C6")


    ChrTalk(
        0x106,
        (
            "#10707F#6P#N#40WBut …\x01",
            "Here too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_24FA")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#30W── Any more,\x01",
            "Contradiction#2RA cow#I'm not going to meet.\x02\x03",
            "If you are now\x01",
            "Also for \"demons\" and \"swordsmen\"\x01",
            "Will it arrive?\x02",
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
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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
        0x101,
        "#00005F#6P#NAh….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00305F#6P#NWithdraw#2RFacial#Will you be there …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13704F#11PIf I could show you the light\x01",
            "More than that is useless handout.\x02\x03",
            "#13702FAs a result of this result,\x01",
            "There is nothing but conviction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6P#NI see…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A39")

    ChrTalk(
        0x105,
        (
            "#10403F#6P#NIron Maiden, we thank you\x02\x03",
            "#10408FBut the Order#6RBokura#With you\x01",
            "There is no way to get along well … …\x02\x03",
            "#10401FYou understand that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13703F#11POf course, Blue Sage.\x02\x03",
            "If the upheaval in the empire resolves\x01",
            "\"Phantom flame plan\" is also completed ……\x02\x03",
            "#13700FThis time#4RThis time#Whatever happened to the end of\x01",
            "It will be close when you decide between males and females.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#6P#NYes, right\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BAC")

    ChrTalk(
        0x106,
        (
            "#10706F#6P#N\"Steel's Saint\" … …\x01",
            "Please teach me only one thing.\x02\x03",
            "#10701FDid you once meet my father?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13703F#11PYes, 10 years ago\x02\x03",
            "#13702FStrong enough to crush our face\x01",
            "Apparent#2RAppear#It is not something to be done.\x02\x03",
            "Already on that height\x01",
            "It may have arrived, but …\x02\x03",
            "#13704FWhether it goes another way or not\x01",
            "It will depend on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2BAC")

    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(-10990, 1920, -50, 800)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CBD")

    ChrTalk(
        0x102,
        (
            "#00103F#6P#NO-one more, please\x02\x03",
            "#00108FThat hair of you,\x01",
            "And it is called \"iron machine unit\".\x02\x03",
            "#00101FNo way,\x01",
            "What \"lion campaign\" … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2D5F")

    label("loc_2CBD")


    ChrTalk(
        0x102,
        (
            "#00106F#6P#N\"Steel's Saint\" … …\x01",
            "Please teach me only one thing.\x02\x03",
            "#00108FThat hair of you,\x01",
            "And it is called \"iron machine unit\".\x02\x03",
            "#00101FNo way,\x01",
            "What \"lion campaign\" … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2D5F")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#13704F#11P#30WEhe\x02\x03",
            "#13702F──On well noticed,\x01",
            "Let me answer.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00105F#6P#N#4S….!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00005F#5PElie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PWhat are you talking about?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30AWell then Farewell for now\x02\x03",
            "#3907V#30W#40AYou are before fate\x01",
            "To be able to give \"answer\" ……\x02\x03",
            "#13702F#3908V#30W#30AI shall pray for it from afar\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_2FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2FA3)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00008F#5P…… Eli.\x01",
            "What on earth were you talking about?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30D2():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_30D2)
    Sleep(30)

    def lambda_30E2():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_30E2)
    Sleep(30)

    def lambda_30F2():
        TurnDirection(0xF4, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_30F2)
    Sleep(30)

    def lambda_3102():
        TurnDirection(0xF5, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3102)
    Sleep(30)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x103,
        (
            "#00200FSomehow, it is terribly frustrating\x01",
            "It was interaction … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-16660, 2420, -660, 1500)
    MoveCamera(90, 17, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(14000, 1500)
    Sleep(500)
    OP_93(0x102, 0x110, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00106F#11PYeah…\x02\x03",
            "#00108FIt seems to be confusing\x01",
            "I do not want to say much, but …\x02\x03",
            "#00101FIf my opinion is right ─\x01",
            "She is a human being 250 years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00307FWhat!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3304")

    ChrTalk(
        0x109,
        "#10111FWell, that is …! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_3304")


    ChrTalk(
        0x106,
        "#10712FWhat do you …!?\x02",
    )

    CloseMessageWindow()

    label("loc_3323")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    SetCameraDistance(13000, 30000)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00103F#11P#30W250 years ago at Erebonia\x01",
            "A fierce successor fight over the throne\x01",
            "I had something happened.\x02\x03",
            "Conflict spreads throughout the empire,\x01",
            "Finally with the name \"lion battle\"\x01",
            "I was supposed to be called … ….\x02\x03",
            "#00108FAt that time, from a neutral standpoint\x01",
            "I got up to finish the war\x01",
            "There was a woman from a woman.\x02\x03",
            "#00101FLeanne Sandlot\x02\x03",
            "Lively beautiful golden hair,\x01",
            "Heading a group called \"Iron Fighter\"\x01",
            "People who ran through the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FAh….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310FThat's these guys, exactly!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35F2")

    ChrTalk(
        0x109,
        (
            "#10101FI am also in a book or something\x01",
            "I have read it … ….!\x02\x03",
            "#10103FA battle#2RHow old#Otome \"Lianne … ….\x01",
            "Or \"Spear Saint\" Lianne.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35ED")

    ChrTalk(
        0x105,
        (
            "#10403FEveryone knows in the empire\x01",
            "It is a historical celebrity …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35ED")

    Jump("loc_367C")

    label("loc_35F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_367C")

    ChrTalk(
        0x105,
        (
            "#10403FEveryone knows in the empire\x01",
            "It is a historical celebrity …\x02\x03",
            "#10408FMoreover, one of the street names,\x01",
            "\"Spear 's Saint\" was Rianne?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36BA")

    ChrTalk(
        0x106,
        (
            "#10701FSuch a person\x01",
            "Once in Elebonia …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36BA")


    ChrTalk(
        0x101,
        (
            "#00006F\"Iron Corps\" in the \"Iron Cavalry\" ……\x01",
            "\"Spirit of the Spear\" to \"Steal Saint\"?\x02\x03",
            "#00008FAppearance is nice, certainly too\x01",
            "The codes are too consistent ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P…… But 250 years ago,\x01",
            "Immediately after peace has returned with his own work,\x01",
            "She should have lost her life.\x02\x03",
            "#00108FI was scolded, I was sick,\x01",
            "There are various theories … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F…… If you think normally\x01",
            "I just mimicked that person\x01",
            "Maybe you should decide … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhen I see that terrible power\x01",
            "Do not think only by himself.\x02\x03",
            "#00301FYea, well, I do not know who I am.\x01",
            "It is a human being of \"association\".\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3919")
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#10708F(No way, \"silver#2RIn#\"As well\x01",
            "Someone took over the trace ……? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3919")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_396E")
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10401F(… this is also the president\x01",
            "I need to report it … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396E")


    ChrTalk(
        0x102,
        (
            "#00104F#11PEhe\x01",
            "After all I messed up.\x02\x03",
            "#00100F── Anyway she\x01",
            "I left the crossbell.\x02\x03",
            "Leave speculation,\x01",
            "Let's concentrate on our problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FYeah, that's right\x02",
    )

    CloseMessageWindow()
    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)

    def lambda_3A6D():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A6D)
    Sleep(30)

    def lambda_3A7D():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A7D)
    Sleep(30)

    def lambda_3A8D():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A8D)
    Sleep(30)

    def lambda_3A9D():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A9D)
    Sleep(30)

    def lambda_3AAD():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3AAD)
    Sleep(30)

    def lambda_3ABD():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3ABD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#NOk then let's stop the resonance\x02\x03",
            "#00000FIf you go well it will be\x01",
            "You should be able to break \"barrier\".\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x2C, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    Jump("loc_4A8B")

    label("loc_3B65")

    OP_29(0xB0, 0x1, 0x6)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_3B7C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B7C)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#40W#6P#NHeck … more and more …!\x02",
    )

    CloseMessageWindow()

    def lambda_3BE2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BE2)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x104, 2)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00310F#40W#12P#N…… In such a place ……\x01",
            "Can you stop at it!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)

    def lambda_3C6C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C6C)
    Sleep(50)

    def lambda_3C88():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C88)
    Sleep(50)

    def lambda_3CA4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3CA4)
    Sleep(50)

    def lambda_3CC0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_3CC0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF6")
    Sound(540, 0, 50, 0)

    label("loc_3CF6")

    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
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
            "Although I can not deny the feeling of insufficient power … …\x02\x03",
            "If you broke our face,\x01",
            "Also for \"demons\" and \"swordsmen\"\x01",
            "There is a possibility of reaching it.\x02",
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
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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
        0x101,
        "#00005F#6P#NAriane Road ……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#6P#NDid you mean ……\x01",
            "Withdraw#2RFacial#Will you be there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13704F#11PIf you could show a source of light\x01",
            "More than that is useless handout.\x02\x03",
            "#13702FAs a result of this result,\x01",
            "There is nothing but conviction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6P#NAh….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00305F#6P#NAre they serious?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42A7")

    ChrTalk(
        0x105,
        (
            "#10403F#6P#NIron Maiden, we thank you\x02\x03",
            "#10408FBut the Order#6RBokura#With you\x01",
            "There is no way to get along well … …\x02\x03",
            "#10401FYou understand that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13703F#11POf course, Blue Sage.\x02\x03",
            "If the upheaval in the empire resolves\x01",
            "\"Phantom flame plan\" is also completed ……\x02\x03",
            "#13700FThis time#4RThis time#Whatever happened to the end of\x01",
            "It will be close when you decide between males and females.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10406F#6P#NYes, right\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_42A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4403")

    ChrTalk(
        0x106,
        (
            "#10706F#6P#N\"Steel's Saint\" … …\x01",
            "Please teach me only one thing.\x02\x03",
            "#10701FDid you once meet my father?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13703F#11PYes, 10 years ago\x02\x03",
            "#13702FStrong enough to crush our face\x01",
            "Apparent#2RAppear#It is not something to be done.\x02\x03",
            "#13704FDo you aim for that height …?\x01",
            "Or is it going on another way\x01",
            "It will depend on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6P#N…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4403")

    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30AWell then Farewell for now\x02\x03",
            "#3907V#30W#40AYou are before fate\x01",
            "To be able to give \"answer\" ……\x02\x03",
            "#13702F#3908V#30W#30AI shall pray for it from afar\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_459E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_459E)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x14, 0x0, 0x7D0, 0x1F4)

    ChrTalk(
        0x101,
        "#00006F#40W#5PHa ha ha ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46F2")

    ChrTalk(
        0x109,
        "#10106F#30WI am tired, …\x02",
    )

    CloseMessageWindow()

    label("loc_46F2")


    ChrTalk(
        0x104,
        (
            "#00306F……Geez……\x01",
            "Mr. Tadashi, you, saint.\x02\x03",
            "#00301FMegacare is beautiful\x01",
            "I was a type older sister\x01",
            "I did not seduce him … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FRandy,\x01",
            "With that kind of problem ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut really …\x01",
            "Until you often crush that helmet face\x01",
            "I say that I could have dropped ……\x02\x03",
            "#00102FWe as it is\x01",
            "You seem to be growing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, that's right\x02\x03",
            "#00012FWell, listen to Ka'a's story\x01",
            "A#2RHala#It was possible to enclose\x01",
            "I also feel that it was big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAh……\x01",
            "Do not say such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F… … absolutely regain it\x01",
            "I do not feel like I can not hug you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4962")

    ChrTalk(
        0x105,
        (
            "#10402FWhew.\x01",
            "I really am stupid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4962")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49A4")

    ChrTalk(
        0x109,
        (
            "#10112FHaha ……\x01",
            "It seems they are Lloyd's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49E2")

    ChrTalk(
        0x106,
        (
            "#10709FHehu ……\x01",
            "But I feel I can understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E2")

    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#NOk then let's stop the resonance\x02\x03",
            "#00000FIf you go well it will be\x01",
            "You should be able to break \"barrier\".\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4A8B")

    OP_32(0xFF, 0xFF, 0x0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x101, 0, 1530, 2150, 180)
    SetChrPos(0x104, 0, 1530, -1900, 0)
    SetChrPos(0x102, -4480, 1300, -2860, 45)
    SetChrPos(0x103, -3630, 1320, -3800, 45)
    BeginChrThread(0x101, 3, 0, 13)
    BeginChrThread(0x104, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B5E")
    SetChrChipByIndex(0x109, 0x32)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, -2200, 1530, 0, 90)
    BeginChrThread(0x109, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B48")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_4B59")

    label("loc_4B48")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_4B59")

    Jump("loc_4BB6")

    label("loc_4B5E")

    SetChrChipByIndex(0x106, 0x33)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, -2200, 1530, 0, 90)
    BeginChrThread(0x106, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BA5")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_4BB6")

    label("loc_4BA5")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_4BB6")

    StopEffect(0x7, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 2, 0, 4)
    BeginChrThread(0xD, 1, 0, 14)
    FadeToBright(1000, 0)
    OP_68(0, 1850, 0, 0)
    OP_68(0, 2850, 0, 6000)
    MoveCamera(105, 21, 0, 0)
    MoveCamera(70, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(15000, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 2850, 0, 0)
    MoveCamera(90, 27, 0, 0)
    MoveCamera(90, 9, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    OP_6F(0x79)
    Sleep(50)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(36000, 1000)
    Sound(829, 0, 100, 0)
    StopSound(828, 2000, 60)
    StopSound(825, 2000, 60)
    FadeToDark(1000, 16777215, -1)
    Sleep(1000)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    EndChrThread(0x101, 0x2)
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D1A")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_4D26")

    label("loc_4D1A")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_4D26")

    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Sleep(500)
    OP_68(0, 3550, 0, 0)
    MoveCamera(50, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(20000, 5000)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1E56 end

    def Function_13_4E36(): pass

    label("Function_13_4E36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E5C")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_13_4E36")

    label("loc_4E5C")

    Return()

    # Function_13_4E36 end

    def Function_14_4E5D(): pass

    label("Function_14_4E5D")

    Sound(825, 2, 10, 0)
    Sleep(200)
    OP_25(0x339, 0x14)
    OP_25(0x33C, 0x28)
    Sleep(200)
    OP_25(0x339, 0x1E)
    OP_25(0x33C, 0x32)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x33C, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x32)
    OP_25(0x33C, 0x46)
    Sleep(2000)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Return()

    # Function_14_4E5D end

    SaveToFile()

Try(main)
