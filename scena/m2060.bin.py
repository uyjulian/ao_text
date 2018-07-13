﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2060.bin",                # FileName
        "m2060",                    # MapName
        "m2060",                    # Location
        0x0079,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 121, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2060",                  # 0
        "Campanella The Fool",    # 1
        "Bow Maiden Ennea",       # 2
        "SE制御",                 # 3
        "bm2060",                 # 4
    ))

    ATBonus("ATBonus_118", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1D8", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1BC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1C0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1C4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1C8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1CC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1D0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1F8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03600.dat", 0, 0, 0, 0, 0, "ms86300.dat", 0, "MonsterBattlePostion_1D8", "MonsterBattlePostion_1B8", "ed7458", "ed7453", "ATBonus_118"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(632, 0)                                        # 0

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_2C9",          # 01, 1
        "Function_2_496",          # 02, 2
        "Function_3_68F",          # 03, 3
        "Function_4_6B4",          # 04, 4
        "Function_5_6D9",          # 05, 5
        "Function_6_15E9",         # 06, 6
        "Function_7_1648",         # 07, 7
        "Function_8_1684",         # 08, 8
        "Function_9_2AF9",         # 09, 9
        "Function_10_2B20",        # 0A, 10
        "Function_11_2B51",        # 0B, 11
        "Function_12_3BF9",        # 0C, 12
        "Function_13_3CB4",        # 0D, 13
        "Function_14_3CDD",        # 0E, 14
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_2C8")

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_2B9")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 8)
    Jump("loc_2C8")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_2C8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 11)

    label("loc_2C8")

    Return()

    # Function_0_278 end

    def Function_1_2C9(): pass

    label("Function_1_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_328")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_END)), "loc_2FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_316")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_328")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_36B")
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    Jump("loc_406")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C8")
    LoadEffect(0x9, "map/mpbell02.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Jump("loc_406")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_END)), "loc_406")
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)

    label("loc_406")

    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x384, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_438")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x12C, 0x0)

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454")
    Sound(828, 1, 70, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470")
    Sound(828, 1, 100, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48C")
    Sound(828, 1, 70, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_48C")

    OP_24(0x33C)
    Sound(132, 1, 70, 0)

    label("loc_495")

    Return()

    # Function_1_2C9 end

    def Function_2_496(): pass

    label("Function_2_496")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("chr/ch43300.itc", 0x1F)
    LoadEffect(0x0, "battle/cr037100.eff")
    LoadEffect(0x1, "map/mpbell.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 15760, 7750, 100, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 15370, 7750, -1000, 45)
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_68(22000, 9700, 0, 0)
    MoveCamera(60, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46500, 0)
    FadeToBright(1000, 0)
    OP_68(22000, 10000, 0, 7000)
    MoveCamera(90, 5, 0, 7000)
    SetCameraDistance(17750, 7000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(28000, 10000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x19)
    Sleep(1)
    CancelBlur(4000)
    Sound(929, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 3)
    SetMapObjFrame(0x0, "root", 0x2, "move")
    SetMapObjFrame(0x0, "model02", 0x1, 0x1)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Sound(829, 0, 100, 0)
    Sleep(4000)
    StopSound(828, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0011", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_496 end

    def Function_3_68F(): pass

    label("Function_3_68F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_3_68F")

    label("loc_6B3")

    Return()

    # Function_3_68F end

    def Function_4_6B4(): pass

    label("Function_4_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D8")
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_4_6B4")

    label("loc_6D8")

    Return()

    # Function_4_6B4 end

    def Function_5_6D9(): pass

    label("Function_5_6D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x23)
    SoundLoad(961)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_724")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_724")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73C")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_754")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76C")
    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_76C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784")
    LoadChrToIndex("chr/ch03150.itc", 0x25)

    label("loc_784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79C")
    LoadChrToIndex("chr/ch03250.itc", 0x25)

    label("loc_79C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    LoadEffect(0x0, "battle\\cr036301.eff")
    SoundLoad(3724)
    SoundLoad(3725)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, -1290, 8000, -60, 90)
    OP_90(0x102, -1940, 8000, 680, 90)
    OP_90(0x103, -2200, 8000, -530, 90)
    OP_90(0x104, -2900, 8000, 140, 90)
    OP_90(0xF4, -3090, 8000, -950, 90)
    OP_90(0xF5, -3460, 8000, 1140, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16000, 7750, 0, 270)
    SetMapObjFlags(0x0, 0x1000)
    StopBGM(0xBB8)
    OP_68(0, 1960, 0, 0)
    OP_68(5880, 4940, 0, 2500)
    MoveCamera(57, 26, 0, 0)
    MoveCamera(57, 15, 0, 2500)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15000, 2500)
    FadeToBright(1000, 0)

    def lambda_917():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_917)
    Sleep(30)

    def lambda_92F():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_92F)
    Sleep(30)

    def lambda_947():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_947)
    Sleep(30)

    def lambda_95F():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_95F)
    Sleep(30)

    def lambda_977():
        OP_9B(0x0, 0xF4, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_977)
    Sleep(30)

    def lambda_98F():
        OP_9B(0x0, 0xF5, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_98F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
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
    OP_68(16750, 9700, 0, 2500)
    MoveCamera(63, 0, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(12800, 2500)
    OP_6F(0x79)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    OP_68(8050, 8400, -320, 2500)
    MoveCamera(90, 3, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(11030, 2500)
    Sleep(700)

    def lambda_AC4():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC4)
    Sleep(30)

    def lambda_ADC():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADC)
    Sleep(30)

    def lambda_AF4():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF4)
    Sleep(30)

    def lambda_B0C():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B0C)
    Sleep(30)

    def lambda_B24():
        OP_9B(0x0, 0xF4, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B24)
    Sleep(30)

    def lambda_B3C():
        OP_9B(0x0, 0xF5, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B3C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Uhuhu, well done.\x02\x03",
            "A "dungeon exploration"\x01",
            "and a "treasure hunt"...\x02\x03",
            "Every now and then, even such\x01",
            "simple ideas are not bad, right?\x02",
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

    ChrTalk(
        0x101,
        "#00006F#6PIt was really your doing, then...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00312F#6P#NYou made us go along with quite\x01",
            "a bothersome playin', you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04802F#11PUh uh, if there weren't some obstacles,\x01",
            "you too wouldn't enjoy it, right?\x02\x03",
            "#04809FI wish you to consider it a mischievous\x01",
            "service or something, distinctive of a fool㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P#NI am not happy at all...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5E")

    ChrTalk(
        0x109,
        (
            "#10106F#6P#NEven so, I...\x02\x03",
            "#10108FI can't really see you\x01",
            "as having the age to be in\x01",
            "something like the "Society"...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED1")

    label("loc_E5E")


    ChrTalk(
        0x106,
        (
            "#10703F#6P#NAt any rate, I...\x02\x03",
            "#10701FI can't imagine you have the age to\x01",
            "be in something like the "Society".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED1")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#6P#NI think in that regard\x01",
            "you're like Renne?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#11PUh uh, unlike her, my age does\x01",
            "not reflect my appearance.\x02\x03",
            "#04805F──Oh, right. I enjoyed the \x01",
            "Crossbell independence\x01",
            "declaration of invalidity.\x02\x03",
            "#04802FIt was really quite interesting, but I wonder\x01",
            "if it won't turn out into a pretty thorny path?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P...We're fully aware.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P#NIf it will be a thorny path...\x01",
            "It will be just a "time"\x01",
            "we have to overcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#11PUhuhu, oh well.\x02\x03",
            "#04802FWhatever happens to Crossbell\x01",
            "is outside from my mission.\x02\x03",
            "In that sense, I could\x01",
            "retreat at once, but...\x02\x03",
            "#04809FShould I open my final\x01",
            "best show, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(16000, 8500, 0, 1500)
    MoveCamera(60, 10, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(12000, 1500)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(500)
    Fade(500)
    StopSound(828, 1000, 60)
    BeginChrThread(0xA, 1, 0, 7)
    BeginChrThread(0x8, 3, 0, 6)
    OP_68(16000, 8500, 0, 0)
    MoveCamera(40, 40, 0, 0)
    MoveCamera(90, 15, 0, 8000)
    OP_6E(650, 0)
    SetCameraDistance(19550, 0)
    SetCameraDistance(12550, 8000)
    Sleep(1500)
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
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D5")
    Sound(540, 0, 50, 0)

    label("loc_12D5")

    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x24)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x25)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#3P#NW-What's...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#3P#NSorcery...no, a special\x01",
            "phase space deployment!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13C5")

    ChrTalk(
        0x105,
        (
            "#10410F#6P#NDoes he want to trap us\x01",
            "in a magic barrier...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EB")

    label("loc_13C5")


    ChrTalk(
        0x106,
        "#10707F#6P#NA magic barrier...!?\x02",
    )

    CloseMessageWindow()

    label("loc_13EB")

    OP_57(0x0)
    OP_5A()
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)

    ChrTalk(
        0x8,
        (
            "#04804F#11P#30W#30AUhuhu, because the footing here is bad,\x01",
            "I'm going to guide you to a little larger place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(16000, 8600, 0, 10000)
    MoveCamera(90, 10, 0, 10000)
    OP_6E(650, 10000)
    SetCameraDistance(10000, 10000)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        (
            "#3724V#40A#35WEnforcer No. 0,\x01",
            "Campanella "The Fool".\x02\x03",
            "#3725V#30A#30WCome now, give me a fair\x01",
            "chance── Kidding!♪\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)
    SetScenarioFlags(0x0, 0)
    StopSound(825, 500, 40)
    StopSound(961, 500, 60)
    Sleep(500)
    Sound(960, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    StopEffect(0x0, 0x2)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_1F8", 0x0, 0x0, 0x100, 0x3C, 0xFF)
    FadeToDark(0, 0, -1)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 8)
    Return()

    # Function_5_6D9 end

    def Function_6_15E9(): pass

    label("Function_6_15E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1647")
    OP_82(0x28, 0x41, 0x1388, 0xFA)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    StopEffect(0x0, 0x2)
    Jump("Function_6_15E9")

    label("loc_1647")

    Return()

    # Function_6_15E9 end

    def Function_7_1648(): pass

    label("Function_7_1648")

    Sound(961, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(100)
    OP_25(0x3C1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x3C1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x3C1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x3C1, 0x3C)
    Sleep(100)
    OP_25(0x3C1, 0x46)
    Return()

    # Function_7_1648 end

    def Function_8_1684(): pass

    label("Function_8_1684")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16CC")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_16CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E4")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_16E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16FC")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_16FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1714")
    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_1714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172C")
    LoadChrToIndex("chr/ch03150.itc", 0x25)

    label("loc_172C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1744")
    LoadChrToIndex("chr/ch03250.itc", 0x25)

    label("loc_1744")

    LoadChrToIndex("chr/ch03653.itc", 0x26)
    LoadChrToIndex("chr/ch00001.itc", 0x27)
    LoadChrToIndex("chr/ch00301.itc", 0x28)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1771")
    LoadChrToIndex("chr/ch02901.itc", 0x29)
    Jump("loc_1777")

    label("loc_1771")

    LoadChrToIndex("chr/ch03201.itc", 0x29)

    label("loc_1777")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    LoadEffect(0x0, "event\\ev10002.eff")
    LoadEffect(0x1, "battle\\cr036301.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(959)
    SoundLoad(825)
    SoundLoad(132)
    SoundLoad(3726)
    SoundLoad(3727)
    SoundLoad(3728)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 11710, 8000, -60, 90)
    OP_90(0x102, 11060, 8000, 680, 90)
    OP_90(0x103, 10800, 8000, -530, 90)
    OP_90(0x104, 10100, 8000, 340, 90)
    OP_90(0xF4, 9910, 8000, -780, 90)
    OP_90(0xF5, 9540, 8000, 1140, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x24)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x25)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16000, 7750, 0, 270)
    SetMapObjFlags(0x0, 0x1000)
    PlayBGM("ed7584", 0)
    OP_68(14000, 8400, 0, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(10750, 0)
    SetCameraDistance(13750, 2500)
    Sound(202, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 0, 2000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(750)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04806F#11P#30W*pant*, oh my...\x02\x03",
            "#04801FI really shouldn't do \x01",
            "things I'm not used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#6P#30W*pant pant*...had enough?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A3D")

    ChrTalk(
        0x105,
        (
            "#10401F#6P#N#30WI guess it's our\x01",
            "victory, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A72")

    label("loc_1A3D")


    ChrTalk(
        0x106,
        (
            "#10701F#6P#N#30WI think we win\x01",
            "this one, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A72")

    OP_57(0x0)
    OP_5A()
    OP_68(14250, 8400, 0, 1000)
    Sleep(250)

    def lambda_1A8E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A8E)
    Sleep(250)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    WaitChrThread(0x8, 2)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04804F#11P#30W...Uhuhu, no objections.\x02\x03",
            "#04802FWell, I can't really picture you winning\x01",
            "against the "Steel Maiden", though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6P#30WKh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#6P#N#30WHuh...\x01",
            "None of your business.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#11P#30WUh uh, with this, I will \x01",
            "withdraw from Crossbell.\x02\x03",
            "#04800FThe outcome of the man-made "Sept-Terrion"...\x02\x03",
            "#04802FActually, I would have wanted to observe a\x01",
            "little more, but I'm busy in the Empire region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P#N#30WThe "Phantasmal Blaze Plan"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D06")

    ChrTalk(
        0x109,
        (
            "#10110F#6P#NAre you going to make a\x01",
            "mess of Erebonia next...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4F")

    label("loc_1D06")


    ChrTalk(
        0x106,
        (
            "#10701F#6P#NDo you intend to make a mess\x01",
            "of the Empire region next?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4F")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#11PUhuhu, everything is as\x01",
            "per the "Grandmaster"'s will...\x02\x03",
            "#04800FHowever, getting the answers are always the\x01",
            "children of man who find themselves inside fate.\x02\x03",
            "And that's the same for you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#6P#N...Getting the answers?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(16000, 8500, 0, 1500)
    MoveCamera(90, 15, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(13000, 300)
    Sound(959, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetCameraDistance(12000, 15000)
    CancelBlur(1000)
    Sleep(500)
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
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        (
            "#3726V#40W#40AUhuhu...\x01",
            "Let's meet again, \x01",
            "if fate allows it.\x02\x03",
            "#3727V#40AWhat kind of answers\x01",
            "will you get in the end...?\x02\x03",
            "#3728V#25AI really want you tell me♪\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11250, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopSound(959, 1000, 70)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    StopBGM(0x1770)

    ChrTalk(
        0x103,
        "#00201F#12P#N#30WAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(15000, 7800, 0, 0)
    OP_68(13500, 7800, 0, 2500)
    MoveCamera(50, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16450, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21A7")
    Sound(540, 0, 50, 0)

    label("loc_21A7")

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

    ChrTalk(
        0x104,
        (
            "#00306F#5PTch... He kept sayin'\x01",
            "cryptic stuff until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PThe answers we will get...\x01",
            "I wonder what he meant.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22BD")

    ChrTalk(
        0x105,
        (
            "#10403F#5PHm...\x02\x03",
            "#10400FWell, should we stop the\x01",
            "bell ringing for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2312")

    label("loc_22BD")


    ChrTalk(
        0x106,
        (
            "#10708F#5P............\x02\x03",
            "#10701F...At any rate, should we\x01",
            "stop the bell ringing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2312")

    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00001F#11PRight...\x01",
            "Randy, help me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2375")

    ChrTalk(
        0x109,
        "#10101F#5PI'll help too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2395")

    label("loc_2375")


    ChrTalk(
        0x106,
        "#10703F#5PI will help too.\x02",
    )

    CloseMessageWindow()

    label("loc_2395")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x101, 21840, 7750, 2140, 180)
    SetChrPos(0x104, 21920, 7750, -1930, 0)
    SetChrPos(0x102, 17770, 7750, -2330, 45)
    SetChrPos(0x103, 19210, 7750, -3260, 45)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x104, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2470")
    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, 20010, 7750, 30, 90)
    BeginChrThread(0x109, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_245A")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_246B")

    label("loc_245A")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_246B")

    Jump("loc_24C8")

    label("loc_2470")

    SetChrChipByIndex(0x106, 0x29)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, 20010, 7750, 30, 90)
    BeginChrThread(0x106, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24B7")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_24C8")

    label("loc_24B7")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_24C8")

    StopEffect(0x7, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 2, 0, 4)
    BeginChrThread(0xA, 1, 0, 10)
    FadeToBright(1000, 0)
    OP_68(22000, 8500, 0, 0)
    OP_68(22000, 9500, 0, 6000)
    MoveCamera(110, 21, 0, 0)
    MoveCamera(75, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(15000, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(22000, 9500, 0, 0)
    MoveCamera(90, 27, 0, 0)
    MoveCamera(90, 6, 0, 5000)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_262C")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2638")

    label("loc_262C")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_2638")

    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x12C, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sleep(500)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    OP_68(22000, 12500, 0, 0)
    OP_68(22000, 9500, 0, 6000)
    MoveCamera(67, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x104, 0x13B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2711")
    OP_93(0x109, 0x2D, 0x0)
    Jump("loc_2718")

    label("loc_2711")

    OP_93(0x106, 0x2D, 0x0)

    label("loc_2718")

    OP_68(21400, 9150, 80, 0)
    OP_68(22400, 9150, 80, 3000)
    MoveCamera(89, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16320, 0)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105F#11PIt stopped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11P...The three higher elements are\x01",
            "at work as usual, however...\x02\x03",
            "#00202FIt appears we could cancel the\x01",
            "resonance with the other bells.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PSo, now if we stop the "Tower" bell, \x01",
            "everything's gonna be alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, at least the resonance with\x01",
            "the other bell should stop.\x02\x03",
            "#00000FIf what the Meister said is true,\x01",
            "even the barrier that surrounds\x01",
            "Crossbell should be released...\x02\x03",
            "#00007FLet's go── to the "Tower of Stargaze"!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2971")

    ChrTalk(
        0x109,
        "#10100F#11PRoger!\x02",
    )

    CloseMessageWindow()

    label("loc_2971")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2999")

    ChrTalk(
        0x106,
        "#10702F#11PYes...!\x02",
    )

    CloseMessageWindow()

    label("loc_2999")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29C5")

    ChrTalk(
        0x105,
        "#10402F#11POK, leader.\x02",
    )

    CloseMessageWindow()

    label("loc_29C5")

    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can go to the "Tower of Stargaze" by entering\x01",
            "the side road along St. Ursula Byroad.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearMapObjFlags(0x0, 0x1000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_37()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AA7")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2AAF")

    label("loc_2AA7")

    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_2AAF")

    OP_90(0x0, 17280, 7750, 240, 280)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 5)
    OP_29(0xB0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sound(132, 2, 70, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_1684 end

    def Function_9_2AF9(): pass

    label("Function_9_2AF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B1F")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_9_2AF9")

    label("loc_2B1F")

    Return()

    # Function_9_2AF9 end

    def Function_10_2B20(): pass

    label("Function_10_2B20")

    Sound(825, 2, 10, 0)
    Sleep(200)
    OP_25(0x339, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    Sleep(2000)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Return()

    # Function_10_2B20 end

    def Function_11_2B51(): pass

    label("Function_11_2B51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(132)
    SoundLoad(959)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("apl/ch51257.itc", 0x20)
    LoadEffect(0x0, "event\\ev10002.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    OP_68(21720, 6850, -210, 0)
    MoveCamera(91, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22260, 0)
    SetChrPos(0x101, 15890, 7750, 860, 90)
    SetChrPos(0x102, 15890, 7750, -720, 90)
    SetChrPos(0x103, 16140, 7750, 1880, 90)
    SetChrPos(0x104, 16140, 7750, -1890, 90)
    SetChrPos(0x109, 16140, 7750, 2860, 135)
    SetChrPos(0x105, 16149, 7750, -3080, 45)
    SetChrPos(0x18D, 16650, 7750, 90, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 14510, 8000, -30, 270)
    SetMapObjFlags(0x0, 0x1000)
    OP_68(21720, 9150, -210, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x18D,
        (
            "#12P#04400FThis is...\x01",
            "The "bell" that was in the report.\x02\x03",
            "#04403FIt's almost the same as the bell\x01",
            "located in Central Square...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt appears that with the bell ringing,\x01",
            "some kind of "force field" springs\x01",
            "fort and surrounds the whole ruins.\x02\x03",
            "#00206FI think that it's even the cause\x01",
            "of the spirits appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FPreviously we stopped the ringing\x01",
            "by stopping the bell by sheer strength.\x02\x03",
            "#00003FBy doing that, we could\x01",
            "clear the force field that\x01",
            "had appeared, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FThere's no way that such\x01",
            "a big bell would be\x01",
            "ringing by itself...\x02\x03",
            "#10106FSomeone could really have rung it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#12P#04403FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...In any case, let's\x01",
            "stop this bell first.\x02\x03",
            "#00003FEven in order to talk calmly,\x01",
            "it should be better to remove\x01",
            "the threat of demons for now.\x02\x03",
            "#00000F...Randy, Wazy.\x01",
            "Could you help me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, all right.\x01",
            "What a primitive method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FNo buts, and\x01",
            "let's stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#12P#04403FNo...\x01",
            "That wouldn't be safe.\x02\x03",
            "#04402FPlease back away a little.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30DD():

        label("loc_30DD")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_30DD")

    QueueWorkItem2(0x101, 1, lambda_30DD)
    Sleep(50)

    def lambda_30F2():

        label("loc_30F2")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_30F2")

    QueueWorkItem2(0x102, 1, lambda_30F2)
    Sleep(50)

    def lambda_3107():

        label("loc_3107")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_3107")

    QueueWorkItem2(0x103, 1, lambda_3107)
    Sleep(50)

    def lambda_311C():

        label("loc_311C")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_311C")

    QueueWorkItem2(0x104, 1, lambda_311C)
    Sleep(50)

    def lambda_3131():

        label("loc_3131")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_3131")

    QueueWorkItem2(0x109, 1, lambda_3131)
    Sleep(50)

    def lambda_3146():

        label("loc_3146")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_3146")

    QueueWorkItem2(0x105, 1, lambda_3146)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x18D, 0x0, 0x5DC, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    BeginChrThread(0x18D, 3, 0, 12)
    WaitChrThread(0x18D, 3)
    StopSound(828, 4000, 60)
    StopBGM(0xFA0)
    Sound(829, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(39080, 1000)
    FadeToDark(1000, 16777215, -1)
    Sleep(1000)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    Sleep(2000)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7304", 0)
    Sound(132, 2, 70, 0)
    SetChrChipByIndex(0x18D, 0xFF)
    SetChrSubChip(0x18D, 0x0)
    StopEffect(0x1, 0x0)
    FadeToBright(2000, 16777215)
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    OP_68(22400, 11650, 80, 0)
    MoveCamera(67, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(31880, 0)
    OP_68(22400, 9150, 80, 6000)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    Fade(500)
    OP_68(17930, 8450, 680, 0)
    MoveCamera(56, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16840, 0)
    OP_0D()

    ChrTalk(
        0x18D,
        "#6P#04404F...This should suffice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FMiss Ries, what did you...\x02",
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18D,
        (
            "#11P#04402FYes, it's a technique to seal evil\x01",
            "powers passed down in the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI see, in fact it appears\x01",
            "the three higher elements\x01",
            "have disappeared.\x02\x03",
            "#00200FIt seems all right to think that\x01",
            "for now, thanks to this, the\x01",
            "demons threat has vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FUh uh, in the end,\x01",
            "you took our spotlight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FNo... I could do it because\x01",
            "you all helped me.\x02\x03",
            "#04402FEveryone, thank\x01",
            "you very much.\x02\x03",
            "With this, I was able to\x01",
            "finish the investigation\x01",
            "about the "demons".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYou helped us too when\x01",
            "we were in a tough spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FWell, that's exactly it.\x02\x03",
            "#00309FIf it's for the sake of a cutie,\x01",
            "I'll go through fire and water.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18D, 0x104, 500)

    ChrTalk(
        0x18D,
        "#5P#04405FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FOuch, what a light reaction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FWell...Miss Ries,\x01",
            "please don't mind him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FA-Anyway.\x02\x03",
            "#00100FLet's accompany Miss Ries\x01",
            "back to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_370D")

    ChrTalk(
        0x109,
        (
            "#6P#10109FThat would be nice.\x01",
            "We parked the orbal car nearby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376D")

    label("loc_370D")


    ChrTalk(
        0x109,
        (
            "#6P#10100FThat would be nice. There's also a bus \x01",
            "stop if we go back to the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376D")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, that's right.\x01",
            "...What do you say, Miss Ries?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18D,
        (
            "#11P#04404FThen, I will accept your kind offer.\x02\x03",
            "#04402FI am also hungry, so I would\x01",
            "really like to have Sister Juju's\x01",
            "cookies or something immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHa ha...\x01",
            "Then, shall we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6840, 5050, -120, 7000)
    MoveCamera(52, 32, 0, 7000)
    OP_6E(650, 7000)
    SetCameraDistance(16840, 7000)

    def lambda_38B5():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B5)
    Sleep(50)

    def lambda_38D2():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38D2)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 14)
    Sleep(800)

    def lambda_3913():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_3913)
    OP_6F(0x79)
    WaitChrThread(0x18D, 1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x18D, 0x80)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_68(11990, 9000, -1150, 3000)
    MoveCamera(58, 12, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(12600, 3000)
    OP_6F(0x79)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Youth")

    AnonymousTalk(
        0xFF,
        (
            "A "Gralsritter" woman...\x01",
            "And also, the SSS...\x02\x03",
            "In yesterday's "Pom!",\x01",
            "they did quite well too.\x02\x03",
            "I wonder if they really\x01",
            "could become... Key persons\x01",
            "for the current "plan"?\x02\x03",
            "Uhuhu... Somehow I\x01",
            "have something to look\x01",
            "forward to once again.\x02",
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
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 80, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(12050, 300)
    Sound(959, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(1000)
    Sleep(500)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11250, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopSound(959, 1000, 70)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    SetCameraDistance(13250, 3000)
    Sleep(1000)
    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3BF)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x158, 0)
    SetScenarioFlags(0x22, 2)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2B51 end

    def Function_12_3BF9(): pass

    label("Function_12_3BF9")

    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0x20)
    SetChrSubChip(0x18D, 0x0)
    Sleep(1000)
    Sound(357, 0, 70, 0)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x1, 0x2)
    Sound(222, 0, 80, 0)
    PlayEffect(0x2, 0x2, 0x18D, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x3)
    Sleep(500)
    SetChrSubChip(0x18D, 0x4)
    Return()

    # Function_12_3BF9 end

    def Function_13_3CB4(): pass

    label("Function_13_3CB4")

    OP_95(0xFE, 15890, 7750, 860, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_3CB4 end

    def Function_14_3CDD(): pass

    label("Function_14_3CDD")

    OP_95(0xFE, 15890, 7750, -720, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_3CDD end

    SaveToFile()

Try(main)
