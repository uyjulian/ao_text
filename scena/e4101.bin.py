﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4101.bin",                # FileName
        "e4101",                    # MapName
        "e4101",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4101",                  # 0
        "Special Support Vehicle",# 1
        "Transport",              # 2
        "Arianrhod",              # 3
        "Duvalie the Swift",      # 4
        "Ennea the Chiron",       # 5
        "Aines the Stout",        # 6
        "Minneth",                # 7
        "猫型魔獣",               # 8
        "猫型魔獣",               # 9
        "猫型魔獣",               # 10
        "猫型魔獣",               # 11
        "猫型魔獣",               # 12
        "槍",                     # 13
        "共和国戦車",             # 14
        "共和国戦車",             # 15
        "共和国戦車",             # 16
        "共和国戦車",             # 17
        "共和国飛行艇",           # 18
        "共和国飛行艇",           # 19
        "共和国飛行艇",           # 20
        "共和国飛行艇",           # 21
        "SE制御",                 # 22
        "Dummy",                  # 23
        "Dummy",                  # 24
        "Dummy",                  # 25
        "Dummy",                  # 26
        "Dummy",                  # 27
        "br2000",                 # 28
    ))

    ATBonus("ATBonus_3B8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_478", 0x0042, 255, 6, 45, 3, 3, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82004.dat", "ms82004.dat", "ms82004.dat", "ms82004.dat", "ms82004.dat", 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7453", "ed7453", "ATBonus_3B8"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1364, 0)                                       # 0

    ScpFunction((
        "Function_0_554",          # 00, 0
        "Function_1_5A0",          # 01, 1
        "Function_2_5A1",          # 02, 2
        "Function_3_5B6",          # 03, 3
        "Function_4_108F",         # 04, 4
        "Function_5_10F1",         # 05, 5
        "Function_6_1145",         # 06, 6
        "Function_7_1199",         # 07, 7
        "Function_8_11A9",         # 08, 8
        "Function_9_11B9",         # 09, 9
        "Function_10_11C9",        # 0A, 10
        "Function_11_11D9",        # 0B, 11
        "Function_12_11E9",        # 0C, 12
        "Function_13_11F9",        # 0D, 13
        "Function_14_123F",        # 0E, 14
        "Function_15_137D",        # 0F, 15
        "Function_16_13C3",        # 10, 16
        "Function_17_161D",        # 11, 17
        "Function_18_166A",        # 12, 18
        "Function_19_16BF",        # 13, 19
        "Function_20_170B",        # 14, 20
        "Function_21_17C2",        # 15, 21
        "Function_22_19BD",        # 16, 22
        "Function_23_1A67",        # 17, 23
        "Function_24_3D90",        # 18, 24
        "Function_25_3DAA",        # 19, 25
        "Function_26_3DCD",        # 1A, 26
        "Function_27_3DE0",        # 1B, 27
        "Function_28_3DF9",        # 1C, 28
        "Function_29_3E79",        # 1D, 29
        "Function_30_3F07",        # 1E, 30
        "Function_31_3F42",        # 1F, 31
        "Function_32_3FA3",        # 20, 32
        "Function_33_3FF5",        # 21, 33
        "Function_34_4033",        # 22, 34
        "Function_35_4071",        # 23, 35
        "Function_36_409B",        # 24, 36
        "Function_37_40C5",        # 25, 37
    ))


    def Function_0_554(): pass

    label("Function_0_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_568")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_59F")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_57C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)
    Jump("loc_59F")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_590")
    ClearScenarioFlags(0x22, 2)
    Event(0, 16)
    Jump("loc_59F")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_59F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 23)

    label("loc_59F")

    Return()

    # Function_0_554 end

    def Function_1_5A0(): pass

    label("Function_1_5A0")

    Return()

    # Function_1_5A0 end

    def Function_2_5A1(): pass

    label("Function_2_5A1")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_2_5A1 end

    def Function_3_5B6(): pass

    label("Function_3_5B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x7, "event/ev15070.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    OP_F3(200000)
    Call(0, 2)
    SoundLoad(924)
    SoundLoad(497)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 0, 0, 0)
    OP_74(0x0, 0x1E)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x15)
    OP_93(0x15, 0x10E, 0x0)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 0, 0, 0, 0)
    OP_74(0x1, 0x1E)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x16)
    OP_93(0x16, 0x10E, 0x0)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 0, 0, 0, 0)
    OP_74(0x9, 0x1E)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_78(0x9, 0x17)
    OP_93(0x17, 0x10E, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 0, 0, 0, 0)
    OP_74(0xA, 0x1E)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0xA, 0x18)
    OP_93(0x18, 0x10E, 0x0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x18, 0x40)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 0, 0, 0, 0)
    OP_74(0x2, 0x1E)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x19)
    OP_93(0x19, 0x10E, 0x0)
    OP_71(0x2, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 0, 0, 0, 0)
    OP_74(0x3, 0x1E)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0x1A)
    OP_93(0x1A, 0x10E, 0x0)
    OP_71(0x3, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 0, 0, 0, 0)
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x1B)
    OP_93(0x1B, 0x10E, 0x0)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 0, 0, 0, 0)
    OP_74(0x8, 0x1E)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x1C)
    OP_93(0x1C, 0x10E, 0x0)
    OP_71(0x8, 0x3D, 0x78, 0x0, 0x20)
    OP_68(-170690, -2150, -14350, 0)
    MoveCamera(259, 176, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(90630, 0)
    OP_68(-174690, -2150, -14350, 5500)
    OP_11(0xD0, 0xD0, 0xFF, 0x32, 0x226, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac65", 0x0, 0)
    OP_6F(0x79)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0x15E, 0x0)
    BeginChrThread(0x1D, 1, 0, 13)
    Sound(497, 2, 50, 0)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x15, -9000, 0, -1600, 270)
    SetChrPos(0x16, 3600, 0, -3700, 270)
    SetChrPos(0x17, 40000, 0, -3200, 270)
    SetChrPos(0x18, 77100, 0, -3200, 270)
    OP_FF(0x9, 0x320, 0x320, 0x320)
    OP_FF(0xA, 0x2BC, 0x2BC, 0x2BC)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x19, -1000, 18000, -13000, 270)
    SetChrPos(0x1A, 45000, 15000, -6000, 270)
    SetChrPos(0x1B, 85000, 36500, 4059, 270)
    SetChrPos(0x1C, 64000, 35500, 6360, 270)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x9, 0x1F4, 0x1F4, 0x1F4)
    OP_FF(0xA, 0x1F4, 0x1F4, 0x1F4)
    Fade(500)
    OP_68(-89570, 2650, -10430, 0)
    MoveCamera(83, -7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6260, 0)
    PlayEffect(0x7, 0x0, 0x19, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x1, 0x19, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x2, 0x1A, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x3, 0x1A, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0x1B, 0x5, -3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x5, 0x1B, 0x5, 3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x6, 0x1C, 0x5, -3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x7, 0x1C, 0x5, 3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x15, 0, 0, 5)
    BeginChrThread(0x16, 0, 0, 6)
    BeginChrThread(0x17, 0, 0, 7)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 9)
    BeginChrThread(0x1A, 0, 0, 10)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 12)
    MoveCamera(83, -9, 0, 5500)
    OP_0D()
    Sleep(4500)
    OP_68(-89570, 1650, -10430, 18000)
    MoveCamera(290, 7, 0, 18000)
    SetCameraDistance(5500, 14000)
    Sleep(4000)
    BlurSwitch(0xBB8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(4000)
    CancelBlur(2000)
    Sleep(2000)
    EndChrThread(0x1D, 0x1)
    OP_25(0x39C, 0x28)
    OP_25(0x1F1, 0x64)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    OP_71(0x2, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x3, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x8, 0x3D, 0x78, 0x0, 0x20)
    SetChrPos(0x19, 4000, 12450, 3090, 0)
    SetChrPos(0x1A, 20000, 18600, 6160, 0)
    SetChrPos(0x1B, -21000, 8000, -12000, 0)
    SetChrPos(0x1C, 7000, 11000, -14000, 0)
    OP_93(0x19, 0x10B, 0x0)
    OP_93(0x1A, 0x10B, 0x0)
    OP_93(0x1B, 0x10B, 0x0)
    OP_93(0x1C, 0x10B, 0x0)
    SetChrPos(0x15, -39000, 0, -1600, 270)
    SetChrPos(0x16, -21600, 0, -4200, 270)
    SetChrPos(0x17, -4000, 0, -3200, 270)
    SetChrPos(0x18, 15100, 0, -2800, 270)
    OP_FF(0x0, 0x384, 0x384, 0x384)
    OP_FF(0x1, 0x384, 0x384, 0x384)
    OP_FF(0x9, 0x384, 0x384, 0x384)
    OP_FF(0xA, 0x384, 0x384, 0x384)
    OP_FF(0x2, 0x384, 0x384, 0x384)
    OP_FF(0x3, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x7, 0x1C2, 0x1C2, 0x1C2)
    OP_FF(0x8, 0x226, 0x226, 0x226)
    PlayEffect(0x7, 0xFF, 0x19, 0x5, -5760, 1000, 225, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x19, 0x5, 5760, 1000, 225, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1A, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1A, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1B, 0x5, -2880, 450, 112, 0, 0, 0, 450, 450, 450, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1B, 0x5, 2880, 450, 112, 0, 0, 0, 450, 450, 450, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1C, 0x5, -3520, 550, 138, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1C, 0x5, 3520, 550, 138, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0x1B, 0x5, 0, 0, 0, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0x1B, 0x5, 0, 0, 0, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_11(0xD0, 0xD0, 0xFF, 0x55, 0x1F3, 0x0)
    Fade(500)
    OP_68(-33540, 1650, -1540, 0)
    MoveCamera(278, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(71590, 0)
    OP_68(-83980, 1650, -6630, 12000)
    MoveCamera(274, 19, 0, 12000)
    OP_6E(600, 12000)
    SetCameraDistance(71590, 12000)
    BeginChrThread(0x15, 0, 0, 5)
    BeginChrThread(0x16, 0, 0, 6)
    BeginChrThread(0x17, 0, 0, 7)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 9)
    BeginChrThread(0x1A, 0, 0, 10)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 12)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_0D()
    CancelBlur(2000)
    Sleep(2000)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(8000)
    StopSound(924, 2000, 40)
    StopSound(497, 2000, 100)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5B6 end

    def Function_4_108F(): pass

    label("Function_4_108F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 37450, 0, -2200)
    OP_9F(0x1, -124100, 0, -3550)
    OP_9F(0x1, -155100, 0, -7150)
    OP_9F(0x1, -186100, 0, -13850)
    OP_9F(0x1, -222900, 0, -23800)
    OP_9F(0x1, -268250, 0, -29550)
    OP_9F(0x2, 0xFE, 3000, 0x6)
    Return()

    # Function_4_108F end

    def Function_5_10F1(): pass

    label("Function_5_10F1")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -124100, 0, -2450)
    OP_9F(0x1, -155100, 0, -6050)
    OP_9F(0x1, -186100, 0, -12750)
    OP_9F(0x1, -222900, 0, -22700)
    OP_9F(0x1, -268250, 0, -28150)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_5_10F1 end

    def Function_6_1145(): pass

    label("Function_6_1145")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -124100, 0, -6050)
    OP_9F(0x1, -155100, 0, -9650)
    OP_9F(0x1, -186100, 0, -16350)
    OP_9F(0x1, -222900, 0, -26300)
    OP_9F(0x1, -268250, 0, -32049)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_6_1145 end

    def Function_7_1199(): pass

    label("Function_7_1199")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_7_1199 end

    def Function_8_11A9(): pass

    label("Function_8_11A9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_8_11A9 end

    def Function_9_11B9(): pass

    label("Function_9_11B9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_9_11B9 end

    def Function_10_11C9(): pass

    label("Function_10_11C9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1AF4, 0x1)
    Return()

    # Function_10_11C9 end

    def Function_11_11D9(): pass

    label("Function_11_11D9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1A90, 0x1)
    Return()

    # Function_11_11D9 end

    def Function_12_11E9(): pass

    label("Function_12_11E9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1A2C, 0x1)
    Return()

    # Function_12_11E9 end

    def Function_13_11F9(): pass

    label("Function_13_11F9")

    Sound(924, 2, 10, 0)
    Sleep(500)
    OP_25(0x39C, 0x14)
    Sleep(500)
    OP_25(0x39C, 0x1E)
    Sleep(500)
    OP_25(0x39C, 0x28)
    Sleep(500)
    OP_25(0x39C, 0x32)
    Sleep(500)
    OP_25(0x39C, 0x3C)
    Sleep(500)
    OP_25(0x39C, 0x46)
    Sleep(1000)
    OP_25(0x39C, 0x50)
    Sleep(1000)
    OP_25(0x39C, 0x5A)
    Sleep(1000)
    OP_25(0x39C, 0x64)
    Return()

    # Function_13_11F9 end

    def Function_14_123F(): pass

    label("Function_14_123F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(952)
    SoundLoad(145)
    SetChrPos(0x0, -185300, 15250, -52700, 0)
    Call(0, 2)
    OP_68(-185300, 30750, -52700, 0)
    MoveCamera(45, -15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-185300, 16500, -52700, 5000)
    MoveCamera(45, 0, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16250, 5000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-185300, 15750, -52700, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_68(-185300, 16250, -52700, 3000)
    SetCameraDistance(25000, 7000)
    BeginChrThread(0x1D, 1, 0, 15)
    OP_71(0x6, 0x0, 0xD2, 0x0, 0x8)
    OP_79(0x6)
    Sound(952, 2, 100, 0)
    OP_71(0x6, 0xD2, 0x12C, 0x0, 0x20)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(952, 500, 100)
    OP_0D()
    OP_24(0x91)
    SetScenarioFlags(0x22, 0)
    NewScene("e4830", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_123F end

    def Function_15_137D(): pass

    label("Function_15_137D")

    Sound(140, 0, 100, 0)
    Sleep(500)
    Sound(145, 2, 100, 0)
    Sleep(1200)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Sleep(200)
    Sound(145, 2, 100, 0)
    Sleep(1900)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Sleep(200)
    Sound(145, 2, 100, 0)
    Sleep(2400)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Return()

    # Function_15_137D end

    def Function_16_13C3(): pass

    label("Function_16_13C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    OP_49()
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x8, 1, 0, 21)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    OP_49()
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x9, 1, 0, 22)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(-236580, 1250, -26430, 0)
    MoveCamera(34, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30020, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    OP_6B(0x1E)
    BeginChrThread(0x1E, 1, 0, 20)
    Sleep(500)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8)
    LoadEffect(0x0, "battle/cr003200.eff")
    LoadEffect(0x1, "event/ev12013.eff")
    OP_F3(990000)
    SoundLoad(469)
    Sound(469, 2, 100, 0)
    BeginChrThread(0x1D, 1, 0, 19)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x1F, -197980, 50, -12890, 90)
    SetChrPos(0x21, -187980, 50, -12890, 90)
    BeginChrThread(0x1F, 1, 0, 17)
    BeginChrThread(0x21, 1, 0, 18)
    Sleep(2000)
    Sleep(1900)
    SetChrPos(0x20, -160530, 50, -10830, 90)
    SetChrPos(0x22, -150530, 50, -10830, 90)
    BeginChrThread(0x20, 1, 0, 17)
    BeginChrThread(0x22, 1, 0, 18)
    Sleep(2000)
    Sleep(3100)
    SetChrPos(0x1F, -108310, 50, -780, 90)
    SetChrPos(0x21, -98310, 50, -780, 90)
    BeginChrThread(0x1F, 1, 0, 17)
    BeginChrThread(0x21, 1, 0, 18)
    Sleep(600)
    SetChrPos(0x20, -101150, 50, -3960, 90)
    SetChrPos(0x22, -91150, 50, -3960, 90)
    BeginChrThread(0x20, 1, 0, 17)
    BeginChrThread(0x22, 1, 0, 18)
    Sleep(1400)
    Sleep(600)
    Sleep(2500)
    StopSound(469, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 6)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_13C3 end

    def Function_17_161D(): pass

    label("Function_17_161D")

    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
    Sleep(2000)
    Return()

    # Function_17_161D end

    def Function_18_166A(): pass

    label("Function_18_166A")

    Sleep(500)
    Sleep(2000)
    OP_82(0x12C, 0x1F4, 0xBB8, 0x190)
    Sound(196, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_18_166A end

    def Function_19_16BF(): pass

    label("Function_19_16BF")

    Sleep(1200)
    Sound(457, 0, 100, 0)
    Sleep(2000)
    Sound(486, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(2500)
    Sound(458, 0, 100, 0)
    Sleep(1400)
    Sound(492, 0, 100, 0)
    Sleep(3100)
    Sound(494, 0, 100, 0)
    Sleep(2000)
    Sound(494, 0, 100, 0)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    Return()

    # Function_19_16BF end

    def Function_20_170B(): pass

    label("Function_20_170B")

    SetChrPos(0xFE, -235580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -233580, 0, -26430)
    OP_9F(0x1, -209600, 0, -21900)
    OP_9F(0x1, -195960, 0, -16980)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -169890, 0, -10880)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x1, -139150, 0, -4810)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110490, 0, -2720)
    OP_9F(0x1, -88320, 0, -2970)
    OP_9F(0x1, -38320, 0, -2510)
    OP_9F(0x1, 28510, 0, -2510)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    Return()

    # Function_20_170B end

    def Function_21_17C2(): pass

    label("Function_21_17C2")

    SetChrPos(0xFE, -248580, 0, -25430, 0)
    OP_9F(0x0, 0xFE)
    Sound(494, 0, 100, 0)
    OP_9F(0x1, -248580, 0, -25430)
    OP_9F(0x1, -211600, 0, -19900)
    OP_9F(0x2, 0xFE, 12500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -197960, 0, -14980)
    OP_9F(0x1, -192500, 0, -16980)
    OP_9F(0x1, -185500, 0, -15480)
    OP_9F(0x1, -180500, 0, -14000)
    OP_9F(0x1, -169890, 0, -12500)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -169890, 0, -12500)
    OP_9F(0x1, -156500, 0, -9600)
    OP_9F(0x1, -152500, 0, -6000)
    OP_9F(0x1, -145500, 0, -4500)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -145500, 0, -4500)
    OP_9F(0x1, -130150, 0, -2200)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -130150, 0, -2200)
    OP_9F(0x1, -105490, 0, -1200)
    OP_9F(0x1, -101490, 0, -4100)
    OP_9F(0x1, -97500, 0, -4200)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -97500, 0, -4200)
    OP_9F(0x1, -96500, 0, -4100)
    OP_9F(0x1, -95500, 0, -3400)
    OP_9F(0x1, -92500, 0, -1100)
    OP_9F(0x1, -89500, 0, -1100)
    OP_9F(0x1, -86500, 0, -1100)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -86500, 0, -1100)
    OP_9F(0x1, -79320, 0, -1710)
    OP_9F(0x1, -70320, 0, -1810)
    OP_9F(0x1, -40320, 0, -2110)
    OP_9F(0x1, 26510, 0, -3510)
    OP_9F(0x2, 0xFE, 9300, 0x6)
    Return()

    # Function_21_17C2 end

    def Function_22_19BD(): pass

    label("Function_22_19BD")

    SetChrPos(0xFE, -224580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -223580, 0, -26430)
    OP_9F(0x1, -206600, 0, -21900)
    OP_9F(0x1, -192960, 0, -16980)
    OP_9F(0x1, -166890, 0, -10880)
    OP_9F(0x1, -134150, 0, -4810)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -106490, 0, -2720)
    OP_9F(0x1, -85320, 0, -2970)
    OP_9F(0x1, -35320, 0, -2510)
    OP_9F(0x1, 31510, 0, -2510)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_22_19BD end

    def Function_23_1A67(): pass

    label("Function_23_1A67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    LoadChrToIndex("apl/ch51546.itc", 0x1F)
    LoadChrToIndex("monster/ch82051.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51544.itc", 0x27)
    LoadChrToIndex("monster/ch82050.itc", 0x28)
    SoundLoad(469)
    SoundLoad(868)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    OP_49()
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x9, 1, 0, 29)
    OP_68(-82750, 1250, -3000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32500, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    OP_6B(0x1E)
    BeginChrThread(0x1E, 1, 0, 28)
    Sleep(500)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x14, 0x27)
    SetChrSubChip(0x14, 0x0)
    LoadEffect(0x1, "event/ev15100.eff")
    LoadEffect(0x2, "event/ev15101.eff")
    LoadEffect(0x3, "event/ev10010.eff")
    LoadEffect(0x4, "event/ev15102.eff")
    Sound(469, 2, 100, 0)
    Sound(494, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3500)
    Sound(288, 0, 100, 0)
    BeginChrThread(0x1D, 2, 0, 25)
    OP_82(0x3E8, 0x7D0, 0xBB8, 0x320)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, -167950, 0, -11810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -167950, 0, -11810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x14, -167950, 0, -11810, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    Sleep(500)
    Sound(487, 0, 100, 0)

    NpcTalk(
        0x9,
        "Minneth",
        "#11AWhaaaaaat!?\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(500)
    Sound(200, 0, 80, 0)
    Sound(880, 0, 100, 0)
    OP_24(0x1D5)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x8)
    OP_82(0x12C, 0x4B0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -160750, 1850, 1110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(868, 2, 30, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -159400, 2150, 2080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    OP_6B(0xFF)
    OP_68(-171180, 1250, -4430, 3000)
    MoveCamera(14, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(29580, 3000)

    def lambda_1D85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1D85)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x8, 1, 0, 30)
    OP_6F(0x79)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x8, 1)
    StopSound(459, 500, 90)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x8)
    Sleep(500)

    NpcTalk(
        0x8,
        "Elie",
        "#00105FW-What's going on!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Tio",
        (
            "#00205FIt seems there was a big\x01",
            "impact...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    StopSound(868, 3000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-168010, 1250, -6300, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16780, 0)
    SetChrPos(0x101, -169400, 50, -6500, 90)
    SetChrPos(0x102, -169300, 50, -7900, 90)
    SetChrPos(0x104, -169300, 50, -5100, 90)
    SetChrPos(0x109, -171200, 50, -6500, 90)
    SetChrPos(0x103, -171000, 50, -7900, 90)
    SetChrPos(0x105, -171000, 50, -5100, 90)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -164500, 50, -6100, 270)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "W-What the heck...\x01",
            "happened!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI don't really know,\x01",
            "but...\x02\x03",
            "#00001F...It's time to pay the\x01",
            "piper. Will you\x01",
            "surrender peacefully?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Hehehe...\x01",
            "Hehehehehe!!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xE,
        (
            "#5SBwah ha ha ha ha ha\x01",
            "ha!!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Fine... At last, it\x01",
            "seems the Goddess has\x01",
            "abandoned me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "However... My nature is\x01",
            "to turn everything to\x01",
            "profit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If this is how it's gonna be,\x01",
            "I'll drag you all down to the\x01",
            "depths of hell with me!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    OP_68(-165130, 1250, -4310, 2000)
    MoveCamera(52, 30, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16780, 2000)
    OP_93(0xE, 0x2D, 0x1F4)

    def lambda_224F():

        label("loc_224F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_224F")

    QueueWorkItem2(0x101, 1, lambda_224F)

    def lambda_2261():

        label("loc_2261")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2261")

    QueueWorkItem2(0x102, 1, lambda_2261)

    def lambda_2273():

        label("loc_2273")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2273")

    QueueWorkItem2(0x103, 1, lambda_2273)

    def lambda_2285():

        label("loc_2285")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2285")

    QueueWorkItem2(0x104, 1, lambda_2285)

    def lambda_2297():

        label("loc_2297")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_2297")

    QueueWorkItem2(0x109, 1, lambda_2297)

    def lambda_22A9():

        label("loc_22A9")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_22A9")

    QueueWorkItem2(0x105, 1, lambda_22A9)
    OP_95(0xE, -163200, 50, -3580, 4000, 0x0)
    Sound(454, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    OP_93(0xE, 0x10E, 0x1F4)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    BeginChrThread(0xF, 1, 0, 31)
    Sleep(200)
    Sound(948, 0, 80, 0)
    WaitChrThread(0xF, 1)
    BeginChrThread(0xF, 1, 0, 32)
    BeginChrThread(0x1D, 1, 0, 24)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x10, 1, 0, 31)
    WaitChrThread(0x10, 1)
    BeginChrThread(0x10, 1, 0, 33)
    OP_68(-169280, 1250, -6210, 3000)
    MoveCamera(25, 30, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21690, 3000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    Sleep(200)
    BeginChrThread(0x11, 1, 0, 31)
    WaitChrThread(0x11, 1)
    BeginChrThread(0x11, 1, 0, 34)
    BeginChrThread(0x12, 1, 0, 31)
    WaitChrThread(0x12, 1)
    BeginChrThread(0x12, 1, 0, 35)
    BeginChrThread(0x13, 1, 0, 31)
    WaitChrThread(0x13, 1)
    BeginChrThread(0x13, 1, 0, 36)

    def lambda_247D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_247D)

    def lambda_248A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_248A)

    def lambda_2497():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2497)

    def lambda_24A4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24A4)

    def lambda_24B1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24B1)

    def lambda_24BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24BE)
    WaitChrThread(0x13, 1)
    OP_6F(0x79)
    EndChrThread(0x1D, 0x1)
    Sound(911, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2573")

    ChrTalk(
        0x109,
        "#10107F#11PT-Those are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310FRed Constellation's\x01",
            "cougars!?\x02\x03",
            "#00307FCareful! With those\x01",
            "numbers, we can't\x01",
            "underestimate them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2635")

    label("loc_2573")


    ChrTalk(
        0x109,
        "#10107F#11PT-Those are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310FRed Constellation's cougars...\x01",
            "Then you've got ties with\x01",
            "uncle and the others, huh?\x02\x03",
            "#00307FCareful! With those numbers,\x01",
            "we can't underestimate them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2635")


    ChrTalk(
        0xE,
        (
            "Bwah ha ha... You're\x01",
            "lunch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10307F...Here they come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FLet's attack!!\x02",
    )

    CloseMessageWindow()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_478", 0x30200011, 0x0, 0x100, 0x9, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x4, "event/ev15102.eff")
    LoadEffect(0x5, "event/evwarp.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -159400, 2150, 2080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    SetChrPos(0x8, -177440, 0, -7510, 0)
    OP_D5(0x8, 0x0, 0xFE74, 0x0, 0x0)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    SetChrPos(0x9, -160890, 0, 880, 0)
    OP_D5(0x9, 0x0, 0xD836, 0x0, 0x0)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    LoadChrToIndex("chr/ch03500.itc", 0x25)
    LoadChrToIndex("chr/ch43100.itc", 0x26)
    LoadChrToIndex("chr/ch43300.itc", 0x27)
    LoadChrToIndex("chr/ch43200.itc", 0x28)
    LoadChrToIndex("apl/ch51546.itc", 0x29)
    LoadChrToIndex("apl/ch51544.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00151.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00351.itc", 0x2E)
    LoadChrToIndex("chr/ch02951.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    SoundLoad(3893)
    SoundLoad(868)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    OP_68(-168010, 1250, -6300, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16780, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -169400, 50, -6500, 90)
    SetChrPos(0x102, -169300, 50, -7900, 135)
    SetChrPos(0x104, -169300, 50, -5100, 45)
    SetChrPos(0x109, -171200, 50, -6500, 225)
    SetChrPos(0x103, -171000, 50, -7900, 45)
    SetChrPos(0x105, -171000, 50, -5100, 270)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -164500, 50, -6100, 270)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, -167950, 0, -11810, 0)
    PlayBGM("ed7111", 0)
    BeginChrThread(0x1D, 2, 0, 25)
    Sound(868, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006FPhew. Did we do it!?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_29E7():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29E7)
    Sleep(50)

    def lambda_29F7():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29F7)
    Sleep(50)

    def lambda_2A07():
        TurnDirection(0x104, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A07)
    Sleep(50)

    def lambda_2A17():
        TurnDirection(0x103, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A17)
    Sleep(50)

    def lambda_2A27():
        TurnDirection(0x105, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A27)
    Sleep(50)

    def lambda_2A37():
        TurnDirection(0x109, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A37)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "I-Impossible...\x01",
            "Impossibleeeeee...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Those jaegers' monsters\x01",
            "were dispatched by the\x01",
            "likes of the state police!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Taking us lightly\x01",
            "isn't such a great idea,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BE4")

    ChrTalk(
        0x104,
        (
            "#00304FWell, just because they're jaeger\x01",
            "monsters, it doesn't mean an amateur\x01",
            "can use them at their full potential.\x02\x03",
            "#00301FGive it up and let us arrest you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCE")

    label("loc_2BE4")


    ChrTalk(
        0x104,
        (
            "#00304FIt seems you're a supplier for my\x01",
            "uncle and the others, but...\x02\x03",
            "#00300FWell, just because they're jaeger\x01",
            "monsters, it doesn't mean an amateur\x01",
            "can use them at their full potential.\x02\x03",
            "#00301FGive it up and let us arrest you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCE")


    ChrTalk(
        0xE,
        "U-Uuugh...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00203FLet's have him tell us everything\x01",
            "about his relationship with Red\x01",
            "Constellation.\x02\x03",
            "#00200FWe might get some information on\x01",
            "where they've gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, I don't think we can expect\x01",
            "much in that department.\x02\x03",
            "#00301FAfter all, he's nothing more than\x01",
            "their business partner... He\x01",
            "wouldn't have any valuable info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven so... I wonder what\x01",
            "could have stopped the\x01",
            "transport back there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FThat's right...\x02\x03",
            "I saw something like a\x01",
            "spear fly down...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -153500, 6050, 3990, 225)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -152000, 6050, 6500, 225)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -153500, 6050, 6500, 225)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -155000, 6050, 6500, 225)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F...Everyone, watch out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FHuh!?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xA,
        "???",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3893V#30WHehe. As expected, you\x01",
            "noticed me.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF35)
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    EndChrThread(0x1D, 0x2)
    BeginChrThread(0x1D, 2, 0, 26)
    OP_68(-151950, 6050, 4880, 5000)
    MoveCamera(19, 32, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(18780, 5000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_305A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_305A)
    Sleep(10)

    def lambda_306A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_306A)
    Sleep(30)

    def lambda_307A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_307A)
    Sleep(10)

    def lambda_308A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_308A)
    Sleep(10)

    def lambda_309A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_309A)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "It seems you had the skills to deal\x01",
            "with all those monsters.\x02\x03",
            "You have made steady progress since\x01",
            "we met at the Marshlands...\x02\x03",
            "Perhaps you did not even need my\x01",
            "help.\x02",
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
    Fade(500)
    OP_68(-153340, 3650, 1560, 0)
    MoveCamera(29, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26890, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0xB4, 0x0)

    def lambda_3219():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3219)

    def lambda_3226():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3226)

    def lambda_3233():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3233)

    def lambda_3240():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3240)

    def lambda_324D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_324D)

    def lambda_325A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_325A)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x30)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrPos(0x101, -159820, 0, -12540, 45)
    SetChrPos(0x102, -158320, 0, -12540, 45)
    SetChrPos(0x104, -161320, 0, -12540, 45)
    SetChrPos(0x109, -159820, 0, -14540, 45)
    SetChrPos(0x103, -158320, 0, -14540, 45)
    SetChrPos(0x105, -161320, 0, -14540, 45)
    OP_0D()

    def lambda_331C():
        OP_95(0xFE, -152130, 0, -270, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_331C)

    def lambda_3336():
        OP_95(0xFE, -150960, 0, -470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3336)

    def lambda_3350():
        OP_95(0xFE, -153660, 0, -470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3350)

    def lambda_336A():
        OP_95(0xFE, -152130, 0, -2970, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_336A)

    def lambda_3384():
        OP_95(0xFE, -150960, 0, -2670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3384)

    def lambda_339E():
        OP_95(0xFE, -153660, 0, -2670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_339E)
    WaitChrThread(0x101, 1)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)

    def lambda_33CA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33CA)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_33E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33E9)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)

    def lambda_3402():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3402)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)

    def lambda_341B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_341B)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)

    def lambda_3434():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3434)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)

    def lambda_344D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_344D)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x109,
        (
            "#10107FThe ones from the\x01",
            "Marshlands!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FThen, the spear that\x01",
            "came flying down\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FArianrhod, the Steel\x01",
            "Maiden... That's your\x01",
            "name, right?\x02\x03",
            "#00013F...What's your purpose?\x01",
            "Why are you helping us?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-148790, 3050, 8370, 30000)
    MoveCamera(51, 26, 0, 30000)
    OP_6E(600, 30000)
    SetCameraDistance(25170, 30000)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F...Because the act of that man\x01",
            "over there was against my\x01",
            "style.\x02\x03",
            "In war, there are times one\x01",
            "must commit crimes to preserve\x01",
            "one's own life.\x02\x03",
            "However, simple theft of\x01",
            "goodwill toward the wounded is\x01",
            "inexcusable.\x02\x03",
            "No style, no dignity, not even\x01",
            "resolve... I cannot let such\x01",
            "vulgar behavior go unpunished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FT-Then... It was to stop\x01",
            "Minneth's crime...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWow... Very well said,\x01",
            "for someone belonging to\x01",
            "a secret organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900FYou can perceive it as you\x01",
            "like.\x02\x03",
            "─Continue to train until\x01",
            "next we meet.\x02\x03",
            "If you do not want to fall\x01",
            "in an instant before the\x01",
            "flash of my spear, that is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(3894, 255, 100, 0)
    Sleep(1500)
    BeginChrThread(0x1D, 1, 0, 27)
    PlayEffect(0x5, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3829():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3829)
    Sleep(600)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3874():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3874)
    Sleep(50)
    PlayEffect(0x5, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_38BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38BF)
    Sleep(50)
    PlayEffect(0x5, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_390A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_390A)
    Sleep(1200)
    StopBGM(0x1388)
    OP_68(-151980, 550, -460, 3000)
    MoveCamera(38, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21150, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F...Looks like they're\x01",
            "gone.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    def lambda_39A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39A8)

    def lambda_39B5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39B5)

    def lambda_39C2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_39C2)

    def lambda_39CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_39CF)

    def lambda_39DC():
        OP_93(0xFE, 0x140, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_39DC)

    def lambda_39E9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_39E9)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FIt really does look like\x01",
            "they showed up just for\x01",
            "that...\x02\x03",
            "#00301FJeez... Seriously, who\x01",
            "are those guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FIn any event, it seems we'll\x01",
            "need to lookout for the\x01",
            "Ouroboros in the future, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PFor sure... They're a\x01",
            "mysterious group in many\x01",
            "ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Say, Lloyd. Shouldn't\x01",
            "we arrest Minneth?\x02\x03",
            "#00100FIt's no use just\x01",
            "standing here thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Yeah, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PShould we ask the CGF for\x01",
            "support just in case?\x02\x03",
            "They're on high alert, but\x01",
            "they should at least be able\x01",
            "to send out a transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, that's a good\x01",
            "idea. Please contact\x01",
            "them, Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(868, 1000, 15)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others took\x01",
            "Minneth to the police with\x01",
            "the prisoner transport...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They explained the details of\x01",
            "the case to Billy and Ricardo\x01",
            "who were waiting at the airport.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, they went\x01",
            "with Billy to St. Ursula\x01",
            "Hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1A67 end

    def Function_24_3D90(): pass

    label("Function_24_3D90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DA9")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_24_3D90")

    label("loc_3DA9")

    Return()

    # Function_24_3D90 end

    def Function_25_3DAA(): pass

    label("Function_25_3DAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DCC")
    Sound(203, 0, 15, 0)
    Sleep(800)
    Sound(203, 0, 10, 0)
    Sleep(1000)
    Jump("Function_25_3DAA")

    label("loc_3DCC")

    Return()

    # Function_25_3DAA end

    def Function_26_3DCD(): pass

    label("Function_26_3DCD")

    Sleep(800)
    Sound(203, 0, 5, 0)
    Sleep(800)
    Sound(203, 0, 5, 0)
    Return()

    # Function_26_3DCD end

    def Function_27_3DE0(): pass

    label("Function_27_3DE0")

    Sound(223, 0, 50, 0)
    Sleep(500)
    Sound(936, 0, 90, 0)
    Sleep(600)
    Sound(936, 0, 60, 0)
    Return()

    # Function_27_3DE0 end

    def Function_28_3DF9(): pass

    label("Function_28_3DF9")

    SetChrPos(0xFE, -222580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -222580, 0, -26430)
    OP_9F(0x1, -211600, 0, -21900)
    OP_9F(0x1, -197960, 0, -16980)
    OP_9F(0x1, -163890, 0, -10880)
    OP_9F(0x2, 0xFE, 10200, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -162890, 0, -9880)
    OP_9F(0x1, -160890, 0, 880)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_28_3DF9 end

    def Function_29_3E79(): pass

    label("Function_29_3E79")

    SetChrPos(0xFE, -228580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -228580, 0, -26430)
    OP_9F(0x1, -211600, 0, -21900)
    OP_9F(0x1, -197960, 0, -16980)
    OP_9F(0x1, -171890, 0, -10880)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -171890, 0, -10880)
    OP_9F(0x1, -169000, 0, -8200)
    OP_9F(0x1, -160890, 0, 880)
    OP_9F(0x2, 0xFE, 8000, 0x6)
    Return()

    # Function_29_3E79 end

    def Function_30_3F07(): pass

    label("Function_30_3F07")

    SetChrPos(0xFE, -188460, 50, -12620, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -188460, 50, -12620)
    OP_9F(0x1, -177440, 50, -7510)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_30_3F07 end

    def Function_31_3F42(): pass

    label("Function_31_3F42")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x8000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -163420, 550, -1890, 220)

    def lambda_3F6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F6D)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0xFFFD7C4A, 0x0, 0xFFFFF25E, 0x2BC, 0x7D0)
    Sound(30, 0, 100, 0)
    Sound(48, 0, 100, 0)
    Return()

    # Function_31_3F42 end

    def Function_32_3FA3(): pass

    label("Function_32_3FA3")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166160, 0, -9990, 4000, 0x0)
    OP_95(0xFE, -170080, 50, -10770, 4000, 0x0)
    OP_95(0xFE, -173280, 50, -9200, 4000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3FA3 end

    def Function_33_3FF5(): pass

    label("Function_33_3FF5")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166910, 50, -1870, 4000, 0x0)
    OP_95(0xFE, -169250, 50, -1610, 4000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3FF5 end

    def Function_34_4033(): pass

    label("Function_34_4033")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166160, 0, -9990, 4000, 0x0)
    OP_95(0xFE, -169960, 50, -10200, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_4033 end

    def Function_35_4071(): pass

    label("Function_35_4071")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166010, 50, -7030, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4071 end

    def Function_36_409B(): pass

    label("Function_36_409B")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166150, 50, -3370, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_409B end

    def Function_37_40C5(): pass

    label("Function_37_40C5")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40EC")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_40D0")

    label("loc_40EC")

    Return()

    # Function_37_40C5 end

    SaveToFile()

Try(main)
