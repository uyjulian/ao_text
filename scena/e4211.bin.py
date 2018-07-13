from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4211.bin",                # FileName
        "e4211",                    # MapName
        "e4211",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x00',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4211",                  # 0
        "State Guard Soldier",    # 1
        "State Guard Soldier",    # 2
        "Estelle",                # 3
        "Joshua",                 # 4
        "Renne",                  # 5
        "アイオーン３",           # 6
        "Pater-Mater",            # 7
        "台詞表示用ダミーキャラ", # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "State Guard Soldier",    # 11
        "空",                     # 12
        "フェンス",               # 13
        "フェンス",               # 14
        "フェンス",               # 15
        "バリケード",             # 16
        "SE制御",                 # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(912, 0)                                        # 0

    ScpFunction((
        "Function_0_390",          # 00, 0
        "Function_1_3A8",          # 01, 1
        "Function_2_3CC",          # 02, 2
        "Function_3_3D2",          # 03, 3
        "Function_4_8FF",          # 04, 4
        "Function_5_91B",          # 05, 5
        "Function_6_937",          # 06, 6
        "Function_7_991",          # 07, 7
        "Function_8_AC8",          # 08, 8
        "Function_9_AEF",          # 09, 9
        "Function_10_B16",         # 0A, 10
        "Function_11_C48",         # 0B, 11
        "Function_12_CA5",         # 0C, 12
        "Function_13_F21",         # 0D, 13
        "Function_14_2758",        # 0E, 14
        "Function_15_2817",        # 0F, 15
        "Function_16_282B",        # 10, 16
        "Function_17_288A",        # 11, 17
        "Function_18_28BE",        # 12, 18
        "Function_19_295C",        # 13, 19
        "Function_20_2A60",        # 14, 20
        "Function_21_2ACF",        # 15, 21
        "Function_22_2B4E",        # 16, 22
        "Function_23_2B67",        # 17, 23
        "Function_24_2BBA",        # 18, 24
        "Function_25_2C1F",        # 19, 25
        "Function_26_2C84",        # 1A, 26
        "Function_27_2CE1",        # 1B, 27
        "Function_28_2D24",        # 1C, 28
        "Function_29_2D76",        # 1D, 29
        "Function_30_2D77",        # 1E, 30
        "Function_31_2E04",        # 1F, 31
        "Function_32_2E50",        # 20, 32
        "Function_33_2EF3",        # 21, 33
        "Function_34_2FE8",        # 22, 34
        "Function_35_31D2",        # 23, 35
        "Function_36_31D3",        # 24, 36
        "Function_37_31FE",        # 25, 37
        "Function_38_3232",        # 26, 38
        "Function_39_3278",        # 27, 39
        "Function_40_32D8",        # 28, 40
        "Function_41_3324",        # 29, 41
        "Function_42_336E",        # 2A, 42
        "Function_43_33B1",        # 2B, 43
        "Function_44_342F",        # 2C, 44
        "Function_45_34B5",        # 2D, 45
        "Function_46_34B6",        # 2E, 46
        "Function_47_3534",        # 2F, 47
        "Function_48_354E",        # 30, 48
        "Function_49_3560",        # 31, 49
        "Function_50_35F4",        # 32, 50
        "Function_51_3685",        # 33, 51
        "Function_52_369B",        # 34, 52
        "Function_53_36A7",        # 35, 53
        "Function_54_36B3",        # 36, 54
        "Function_55_3773",        # 37, 55
        "Function_56_3813",        # 38, 56
        "Function_57_3850",        # 39, 57
        "Function_58_390B",        # 3A, 58
        "Function_59_3A8F",        # 3B, 59
        "Function_60_3B3C",        # 3C, 60
        "Function_61_4047",        # 3D, 61
        "Function_62_430A",        # 3E, 62
        "Function_63_4355",        # 3F, 63
        "Function_64_43B7",        # 40, 64
        "Function_65_4426",        # 41, 65
        "Function_66_4495",        # 42, 66
        "Function_67_44BB",        # 43, 67
        "Function_68_4585",        # 44, 68
        "Function_69_45EB",        # 45, 69
        "Function_70_463E",        # 46, 70
        "Function_71_468D",        # 47, 71
    ))


    def Function_0_390(): pass

    label("Function_0_390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    SetMapObjFlags(0xA, 0x2000000)

    label("loc_3A7")

    Return()

    # Function_0_390 end

    def Function_1_3A8(): pass

    label("Function_1_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_3CB")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3CB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_3CB")

    Return()

    # Function_1_3A8 end

    def Function_2_3CC(): pass

    label("Function_2_3CC")

    OP_F3(100000)
    Return()

    # Function_2_3CC end

    def Function_3_3D2(): pass

    label("Function_3_3D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    SoundLoad(993)
    SoundLoad(825)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Call(0, 9)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    Jump("loc_41F")

    label("loc_41C")

    Call(0, 10)

    label("loc_41F")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13060, 0, -26480, 270)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -12880, 0, -28330, 270)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2150, 0, -15190, 188)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 5940, 0, 5200, 180)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 1140, 2500, 21380, 180)
    ClearChrFlags(0xF, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF, -16000, 4400, -20300, 0)
    OP_70(0x8, 0x1E)
    OP_70(0x9, 0x1E)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    OP_68(10300, 2600, 32500, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(37000, 0)
    FadeToBright(1000, 0)
    OP_68(-11500, 0, -28500, 9000)
    MoveCamera(130, 21, 0, 9000)
    OP_6E(510, 9000)
    SetCameraDistance(38220, 9000)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    OP_68(-13150, 2500, -27500, 0)
    MoveCamera(57, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    Fade(500)
    OP_68(-13150, 1200, -27500, 3000)
    MoveCamera(57, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5P...It looks like fighting has begun\x01",
            "at the north and east entrances...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        "#11PHey...isn't that bad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf Commander Sonya's unit\x01",
            "were to come to attack us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI-It's fine.\x01",
            "It seems we're only going to supervise\x01",
            "until the political problem is settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAt any rate, until things are concluded,\x01",
            "we just have to wait, and that's it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Young Girl's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#NTee-hee......\x01",
            "I wonder if such a fence-sitting\x01",
            "idea is going to be fine?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x18, 1, 0, 6)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 5)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x9,
        "#5PW-What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PThis sound...where is it...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F8")
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_0D()
    SetScenarioFlags(0x24, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_8FE")

    label("loc_8F8")

    Call(0, 7)
    Call(0, 13)

    label("loc_8FE")

    Return()

    # Function_3_3D2 end

    def Function_4_8FF(): pass

    label("Function_4_8FF")

    OP_93(0xFE, 0x140, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x82, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_8FF end

    def Function_5_91B(): pass

    label("Function_5_91B")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_5_91B end

    def Function_6_937(): pass

    label("Function_6_937")

    Sound(825, 2, 30, 0)
    Sound(993, 2, 30, 0)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x3E1, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    OP_25(0x3E1, 0x32)
    Sleep(200)
    OP_25(0x339, 0x3C)
    OP_25(0x3E1, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    OP_25(0x3E1, 0x46)
    Sleep(200)
    OP_25(0x339, 0x50)
    OP_25(0x3E1, 0x50)
    Sleep(200)
    OP_25(0x339, 0x5A)
    OP_25(0x3E1, 0x5A)
    Sleep(200)
    OP_25(0x339, 0x64)
    OP_25(0x3E1, 0x64)
    Return()

    # Function_6_937 end

    def Function_7_991(): pass

    label("Function_7_991")

    Call(0, 8)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Call(0, 12)
    SetChrPos(0xE, 0, 50000, 0, 0)
    OP_68(0, 48500, 0, 0)
    MoveCamera(180, -45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(57000, 0)
    Fade(500)
    OP_68(0, 55000, 0, 4000)
    MoveCamera(180, -22, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(9250, 4000)
    OP_0D()
    Sound(990, 0, 100, 0)
    Sleep(1000)
    Sound(994, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1000)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    Return()

    # Function_7_991 end

    def Function_8_AC8(): pass

    label("Function_8_AC8")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xC5, 0xEE, 0xFE, 0xC8, 0x514, 0x0)
    Return()

    # Function_8_AC8 end

    def Function_9_AEF(): pass

    label("Function_9_AEF")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x190)
    Return()

    # Function_9_AEF end

    def Function_10_B16(): pass

    label("Function_10_B16")

    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch09500.itc", 0x20)
    LoadChrToIndex("apl/ch50115.itc", 0x21)
    LoadChrToIndex("apl/ch50547.itc", 0x22)
    LoadChrToIndex("apl/ch50338.itc", 0x23)
    LoadChrToIndex("chr/ch00650.itc", 0x24)
    LoadChrToIndex("chr/ch00651.itc", 0x25)
    LoadChrToIndex("chr/ch00750.itc", 0x26)
    LoadChrToIndex("chr/ch00751.itc", 0x27)
    LoadChrToIndex("chr/ch09556.itc", 0x28)
    LoadChrToIndex("chr/ch00656.itc", 0x29)
    LoadChrToIndex("chr/ch00757.itc", 0x2A)
    LoadEffect(0x8, "event/ev15059.eff")
    LoadEffect(0x2, "event/ev10018.eff")
    LoadEffect(0x0, "event/ev600_00.eff")
    LoadEffect(0x1, "event/ev601_01.eff")
    LoadEffect(0x3, "event/ev14003.eff")
    LoadEffect(0x4, "battle/mgaria0.eff")
    LoadEffect(0x5, "event/ev17064.eff")
    LoadEffect(0x6, "event/ev17063.eff")
    LoadEffect(0x7, "event/eva01_01.eff")
    LoadEffect(0x9, "event/ev17038.eff")
    LoadEffect(0xA, "event/ev17039.eff")
    SoundLoad(979)
    Return()

    # Function_10_B16 end

    def Function_11_C48(): pass

    label("Function_11_C48")

    OP_8A(0x0)
    OP_8A(0x1)
    OP_8A(0x3)
    OP_8A(0x8)
    LoadEffect(0x0, "battle/cr006300.eff")
    LoadEffect(0x1, "battle/cr007100.eff")
    LoadEffect(0x3, "event/ev10017.eff")
    LoadEffect(0x8, "event/ev17107.eff")
    Return()

    # Function_11_C48 end

    def Function_12_CA5(): pass

    label("Function_12_CA5")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 100000, 0, 0)
    OP_78(0xA, 0x13)
    OP_93(0x13, 0x10E, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 0, 0, 0)
    OP_74(0x0, 0xF)
    OP_78(0x0, 0xE)
    OP_93(0xE, 0x0, 0x0)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_D3(0xC, 0x0, "Null_ren(52)")
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x0, 0xF1, 0x104, 0x1, 0x20)
    Return()

    # Function_12_CA5 end

    def Function_13_F21(): pass

    label("Function_13_F21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F41")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 10)

    label("loc_F41")

    SoundLoad(979)
    SoundLoad(996)
    SoundLoad(950)
    SoundLoad(579)
    SoundLoad(1038)
    Call(0, 9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03300.itp")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 100000, 0, 0)
    OP_78(0xA, 0x13)
    OP_93(0x13, 0x10E, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -3000, 5000, -27500, 0)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xD)
    OP_93(0xD, 0x10E, 0x0)
    SetChrFlags(0xD, 0x1)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x0, 0xF)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    Call(0, 12)
    SetChrPos(0xE, -22000, 5000, -27500, 0)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -22500, 0, -36500, 90)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -24370, 100, -31100, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13060, 0, -26480, 270)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -12880, 0, -28330, 270)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2150, 0, -15190, 180)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15000, 0, -20330, 0)
    OP_93(0x14, 0x10E, 0x0)
    OP_78(0x2, 0x14)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -15000, 0, -36330, 0)
    OP_93(0x15, 0x10E, 0x0)
    OP_78(0x3, 0x15)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -15000, 0, -43850, 0)
    OP_93(0x16, 0x10E, 0x0)
    OP_78(0x4, 0x16)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -15000, 0, -28750, 0)
    OP_93(0x17, 0x0, 0x0)
    OP_78(0x5, 0x17)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    OP_68(-23500, 5000, -27500, 0)
    MoveCamera(270, 50, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1232")
    Sound(994, 0, 100, 0)
    FadeToBright(1000, 0)
    Jump("loc_1237")

    label("loc_1232")

    Fade(500)

    label("loc_1237")

    OP_68(-23500, 2000, -27500, 1300)
    MoveCamera(270, 30, 0, 1300)
    OP_6E(800, 1300)
    SetCameraDistance(13500, 1300)
    BeginChrThread(0xE, 0, 0, 14)
    BeginChrThread(0xE, 1, 0, 15)
    OP_0D()
    Sleep(500)
    OP_68(-20750, 4100, -29150, 0)
    MoveCamera(312, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9900, 0)
    Fade(500)
    OP_0D()
    CancelBlur(0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#5P#4SWhaaaaat!?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0)

    ChrTalk(
        0x8,
        "#5P#4SA red "Aion"...!?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xC, 0, 0, 16)
    WaitChrThread(0xC, 0)
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "*chuckle*...good day to you.\x02\x03",
            "However, please don't\x01",
            "lump "Pater-Mater"\x01",
            "together with such dolls.\x02\x03",
            "He is way nicer, smarter\x01",
            "and useful, you know.\x02",
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
    Sound(903, 0, 100, 0)
    Sleep(1000)
    OP_68(-18470, 2800, -29000, 0)
    MoveCamera(34, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12380, 0)
    Fade(500)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PI-Impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PE-Enemies...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03304F#5PTee-hee, I don't care\x01",
            "about you soldiers.\x02\x03",
            "#03300FIf you don't want to get trampled on,\x01",
            "you should step away.\x02\x03",
            "#03302F──Look, it's here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PEh...\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E2")
    Call(0, 8)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetChrPos(0xD, 45000, 55000, -27500, 0)
    Sound(979, 2, 100, 0)
    OP_68(-12500, 12400, -27500, 0)
    MoveCamera(90, -26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    Fade(500)
    Sound(834, 0, 100, 0)
    SetCameraDistance(24000, 2000)
    BeginChrThread(0xD, 0, 0, 17)
    Sleep(1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sound(990, 0, 100, 0)
    WaitChrThread(0xD, 0)

    label("loc_15E2")

    Call(0, 9)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0xD, -5000, 10000, -27500, 0)
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    OP_68(-4000, 13200, -27500, 0)
    MoveCamera(90, 50, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_68(-4000, 2000, -27500, 1700)
    MoveCamera(90, 30, 0, 1700)
    OP_6E(800, 1700)
    SetCameraDistance(13500, 1700)
    BeginChrThread(0xD, 0, 0, 18)
    BeginChrThread(0xD, 1, 0, 19)
    OP_0D()
    OP_6F(0x79)
    Sleep(700)
    OP_68(-5500, 3900, -27500, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13350, 0)
    Fade(500)
    OP_0D()
    CancelBlur(0)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#11P#4SWhaah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#4SAn azure-colored "Aion"...!\x02",
    )

    CloseMessageWindow()
    OP_68(-15000, 3400, -27500, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16000, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 20)
    BeginChrThread(0x9, 0, 0, 21)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#03302F#5PTee-hee...so you came.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 26)
    Sleep(600)
    OP_68(-15550, -800, -27800, 800)
    MoveCamera(41, 20, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(16350, 800)
    WaitChrThread(0xC, 0)
    BeginChrThread(0xE, 1, 0, 29)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 27)
    BeginChrThread(0xB, 0, 0, 28)
    OP_0D()
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)

    def lambda_17EF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17EF)

    def lambda_17FC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17FC)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00807F#12PYou!\x01",
            "Just step away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00907F#6PIt's not a battle you can get into\x01",
            "with that kind of fighting power!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUuuh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PL-Let's retreat to the iron bridge!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 0, 0, 23)
    BeginChrThread(0x9, 0, 0, 24)
    BeginChrThread(0x10, 0, 0, 25)
    WaitChrThread(0xE, 1)
    Sleep(2000)

    def lambda_191A():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_191A)
    Sleep(50)

    def lambda_192A():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_192A)
    SetChrPos(0xE, -22500, 0, -27500, 0)
    OP_93(0xE, 0x5A, 0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    SetChrPos(0xD, -3000, 0, -27500, 0)
    OP_93(0xD, 0x10E, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x33, 0x5A, 0x0, 0x0)
    OP_D3(0xC, 0xFF, "")
    SetChrChipByIndex(0xC, 0x22)
    SetChrPos(0xC, -20200, 0, -33250, 71)
    TurnDirection(0xC, 0xD, 0)
    SetChrPos(0xA, -18500, 0, -33500, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0xA, 0xD, 0)
    SetChrPos(0xB, -19250, 0, -32000, 45)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0xB, 0xD, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_FF(0xB, 0x3E8, 0x3E8, 0xFA)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_68(-19800, 500, -33100, 0)
    MoveCamera(251, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10810, 0)
    Fade(500)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#00808F#6PRenne...don't do anything crazy.\x02\x03",
            "#00801FWe'll back you up with everything we've got.\x02",
        )
    )

    Call(0, 11)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00903F#12PPater-Mater has been strengthened, but\x01",
            "even so, they have the edge over there.\x02\x03",
            "#00901FWe can only find a chance to win \x01",
            "while keeping to trifle with them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03303F#5PYes, I know.\x02\x03",
            "#03308F──I won't let them do what \x01",
            "they want on the land where\x01",
            "those persons live anymore...\x02\x03",
            "#03307FLet's go!\x01",
            "Estelle, Joshua!\x01",
            ""Pater-Mater"!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-20750, 3300, -28470, 0)
    MoveCamera(224, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10730, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    BeginChrThread(0xE, 3, 0, 71)
    Sound(903, 0, 100, 0)
    WaitChrThread(0xE, 3)
    Sleep(1000)
    OP_68(-4250, 4100, -27500, 0)
    MoveCamera(144, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    BeginChrThread(0xD, 0, 0, 30)
    BeginChrThread(0xE, 0, 0, 36)
    BeginChrThread(0xC, 0, 0, 40)
    BeginChrThread(0xA, 0, 0, 41)
    BeginChrThread(0xB, 0, 0, 42)
    Sleep(500)
    Sound(979, 2, 50, 0)
    Sleep(400)
    OP_68(-4250, 4000, -27501, 800)
    MoveCamera(144, 25, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(20030, 800)
    OP_0D()
    Sound(655, 0, 50, 0)
    OP_87(0x6, 0xFF, 0x1, "Null_eyes(76)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    OP_68(-23770, 4200, -28350, 2600)
    MoveCamera(115, 22, 0, 2600)
    OP_6E(800, 2600)
    SetCameraDistance(20590, 2600)
    Sleep(1000)
    Sleep(1500)
    OP_68(-24750, 3800, -24090, 1000)
    MoveCamera(131, 20, 0, 1000)
    OP_6E(800, 1000)
    SetCameraDistance(20590, 1000)
    BlurSwitch(0x1392, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(450)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -34980, 7900, -27270, 99, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    WaitChrThread(0xE, 0)
    BeginChrThread(0xE, 0, 0, 37)
    OP_68(-27050, 3800, -26330, 800)
    MoveCamera(112, 20, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(16480, 800)
    Sleep(700)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-25000, 3100, -26000, 800)
    MoveCamera(114, 22, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(15500, 800)
    OP_6F(0x79)
    WaitChrThread(0xE, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -24660, 5400, -27620, 82, 90, 0, 700, 1500, 700, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    Sound(902, 0, 100, 0)

    label("loc_1ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE1")
    Sleep(50)
    Jump("loc_1ECA")

    label("loc_1EE1")

    OP_68(-18500, 3700, -29000, 2000)
    MoveCamera(112, 25, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(27350, 2000)
    Sleep(500)
    CancelBlur(500)
    Sleep(500)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    SetChrPos(0xE, -26000, 0, -26000, 35)
    SetChrPos(0xD, -8500, 0, -33240, 300)
    OP_68(-9800, 4100, -32450, 0)
    MoveCamera(121, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14760, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0xD, 0, 0, 43)
    Sleep(400)
    OP_68(-9800, 5700, -32450, 3000)
    MoveCamera(121, 23, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(12200, 4000)
    Sleep(1000)
    Sleep(700)
    SetCameraDistance(12200, 1200)
    OP_87(0x9, 0x6, 0x1, "Null_hand_l(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    OP_87(0x9, 0x7, 0x1, "Null_hand_r(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Sound(1039, 0, 100, 0)
    Sleep(2200)
    OP_6F(0x79)
    Fade(500)
    OP_68(-9800, 5200, -32450, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_0D()
    Sound(1038, 2, 100, 0)
    Sound(1014, 0, 100, 0)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    OP_87(0xA, 0x4, 0x1, "Null_hand_l(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x3E8, 0x0)
    OP_87(0xA, 0x5, 0x1, "Null_hand_r(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x3E8, 0x0)
    MoveCamera(64, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    Sleep(500)
    WaitChrThread(0xD, 0)
    OP_6F(0x79)
    StopSound(579, 500, 70)
    StopSound(1038, 1000, 90)
    SetMapObjFlags(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2180")
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    Call(0, 8)
    SetChrPos(0x13, 0, 0, 0, 0)
    Jump("loc_2180")

    label("loc_2180")

    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    Fade(500)
    OP_68(-23610, 800, -36580, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10350, 0)
    BeginChrThread(0xE, 0, 0, 44)
    BeginChrThread(0xC, 0, 0, 46)
    BeginChrThread(0xA, 0, 0, 49)
    BeginChrThread(0xB, 0, 0, 50)

    label("loc_21D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E8")
    Sleep(50)
    Jump("loc_21D1")

    label("loc_21E8")

    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222F")
    OP_68(-26050, 2300, -30050, 700)
    MoveCamera(323, 1, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(16180, 700)
    Jump("loc_225D")

    label("loc_222F")

    OP_68(-24870, 2900, -26210, 700)
    MoveCamera(329, 29, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(13680, 700)

    label("loc_225D")

    Sleep(400)
    BlurSwitch(0x0, 0x88FFFFFF, 0x0, 0x1, 0xA)
    Sound(1038, 2, 100, 0)
    Sound(1014, 0, 100, 0)
    PlayEffect(0xA, 0x4, 0xFF, 0x0, -2750, 5000, -38400, 297, 2, 0, 1500, 1500, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x5, 0xFF, 0x0, -1070, 5000, -34550, 289, 5, 0, 1500, 1500, 950, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    CancelBlur(1000)
    Sleep(800)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopSound(1038, 1000, 90)
    Sleep(1000)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233F")
    ClearMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    Call(0, 9)
    Jump("loc_233F")

    label("loc_233F")

    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xC, -24000, 0, -37000, 349)
    SetChrPos(0xA, -20020, 0, -37390, 78)
    SetChrPos(0xB, -20020, 0, -35630, 80)
    OP_68(-21400, 400, -36720, 0)
    MoveCamera(260, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    Fade(500)
    BeginChrThread(0xE, 0, 0, 45)
    BeginChrThread(0xC, 0, 0, 51)
    BeginChrThread(0xA, 0, 0, 54)
    BeginChrThread(0xB, 0, 0, 55)
    PlayEffect(0x3, 0x7, 0xA, 0x5, 0, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    CancelBlur(1000)
    OP_68(-8750, 1400, -34450, 1300)
    MoveCamera(260, 20, 0, 1300)
    OP_6E(800, 1300)
    SetCameraDistance(6750, 1300)
    OP_6F(0x79)
    Sleep(600)
    StopEffect(0x7, 0x2)
    Sleep(350)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xA, -11800, 0, -37820, 45)
    SetChrFlags(0xA, 0x4)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrPos(0xB, -5790, 800, -28380, 225)
    SetChrFlags(0xB, 0x4)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    OP_68(-7830, 1400, -33700, 0)
    MoveCamera(103, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16840, 0)
    Fade(500)
    BeginChrThread(0xD, 0, 0, 56)
    BeginChrThread(0xA, 0, 0, 59)
    BeginChrThread(0xB, 0, 0, 61)
    MoveCamera(116, 30, 0, 3200)
    Sleep(3200)
    SetCameraDistance(9350, 700)
    Sleep(700)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-7830, 1400, -33700, 2500)
    MoveCamera(135, 64, 0, 2500)
    SetCameraDistance(22000, 2500)
    Sleep(2500)
    CancelBlur(500)
    OP_68(-7830, 1300, -33700, 800)
    MoveCamera(135, 39, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(12500, 800)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xD, 0)
    OP_6F(0x79)
    Sleep(300)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_68(-7830, 2000, -33700, 0)
    MoveCamera(93, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20000, 0)
    Fade(500)
    SetCameraDistance(22000, 2000)
    BeginChrThread(0xD, 0, 0, 63)
    BeginChrThread(0xA, 0, 0, 64)
    BeginChrThread(0xB, 0, 0, 65)
    Sleep(2000)
    OP_0D()
    OP_68(-7830, 2000, -33700, 2500)
    MoveCamera(78, 47, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(22000, 2500)
    Sleep(800)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -20080, 7700, -27960, 122, 90, 0, 250, 2250, 250, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xA, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_68(-19550, 100, -29800, 0)
    MoveCamera(239, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12310, 0)
    SetChrPos(0xC, -23500, 0, -34750, 0)
    TurnDirection(0xC, 0xD, 0)
    OP_68(-14570, 3600, -30280, 5000)
    MoveCamera(177, 40, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(32910, 5000)
    BeginChrThread(0xD, 0, 0, 66)
    BeginChrThread(0xE, 0, 0, 67)
    BeginChrThread(0xC, 0, 0, 68)
    BeginChrThread(0xA, 0, 0, 69)
    BeginChrThread(0xB, 0, 0, 70)
    Sleep(2000)
    BlurSwitch(0x7D0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(2000)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    StopSound(979, 1000, 40)
    StopSound(833, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 4)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_F21 end

    def Function_14_2758(): pass

    label("Function_14_2758")

    SetChrPos(0xFE, -23000, 5000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -22500, 0, -27500)
    OP_9F(0x2, 0xFE, 8000, 0x0)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sleep(300)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    Return()

    # Function_14_2758 end

    def Function_15_2817(): pass

    label("Function_15_2817")

    Sleep(1150)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    Return()

    # Function_15_2817 end

    def Function_16_282B(): pass

    label("Function_16_282B")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(800)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_16_282B end

    def Function_17_288A(): pass

    label("Function_17_288A")

    SetChrPos(0xFE, 45000, 55000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -2000, 10000, -27500)
    OP_9F(0x2, 0xFE, 42000, 0x0)
    Return()

    # Function_17_288A end

    def Function_18_28BE(): pass

    label("Function_18_28BE")

    SetChrPos(0xFE, -3000, 10000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -3000, 0, -27500)
    OP_9F(0x2, 0xFE, 10000, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x33, 0x5A, 0x0, 0x0)
    StopSound(979, 1000, 100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0x1770, 0x6A4)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Return()

    # Function_18_28BE end

    def Function_19_295C(): pass

    label("Function_19_295C")

    Sleep(1100)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x3E8)
    Sound(880, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sleep(50)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x320)
    Sleep(50)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x258)
    Sleep(50)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Sound(200, 0, 100, 0)
    PlayEffect(0x8, 0x1, 0xFF, 0x0, -4030, 30, -27550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x0, 0xFF, 0x0, -5030, 200, -27550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_FF(0xB, 0x3E8, 0x3E8, 0x190)
    Sleep(50)
    Sound(833, 0, 100, 0)
    OP_FF(0xB, 0x3E8, 0x3E8, 0xFA)
    Sleep(600)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_79(0x1)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x172, 0x19A, 0x0, 0x20)
    Return()

    # Function_19_295C end

    def Function_20_2A60(): pass

    label("Function_20_2A60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2ACE")
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(700)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_20_2A60")

    label("loc_2ACE")

    Return()

    # Function_20_2A60 end

    def Function_21_2ACF(): pass

    label("Function_21_2ACF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B4D")
    Sleep(100)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(400)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Jump("Function_21_2ACF")

    label("loc_2B4D")

    Return()

    # Function_21_2ACF end

    def Function_22_2B4E(): pass

    label("Function_22_2B4E")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    Return()

    # Function_22_2B4E end

    def Function_23_2B67(): pass

    label("Function_23_2B67")

    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xFA0, 0x1388, 0x1)

    def lambda_2B95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B95)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_2B67 end

    def Function_24_2BBA(): pass

    label("Function_24_2BBA")

    Sleep(200)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x128E, 0x1388, 0x1)

    def lambda_2BFA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BFA)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_2BBA end

    def Function_25_2C1F(): pass

    label("Function_25_2C1F")

    Sleep(400)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xBB8, 0x1388, 0x1)

    def lambda_2C5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C5F)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_2C1F end

    def Function_26_2C84(): pass

    label("Function_26_2C84")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0xFF, "")
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x5A, 0x0)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB118, 0x0, 0xFFFF7E1E, 0x3E8, 0x7D0)
    Sound(326, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_26_2C84 end

    def Function_27_2CE1(): pass

    label("Function_27_2CE1")


    def lambda_2CE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CE6)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -18500, 0, -33500, 6000, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_2CE1 end

    def Function_28_2D24(): pass

    label("Function_28_2D24")


    def lambda_2D29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D29)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB4CE, 0x0, 0xFFFF8300, 0x3E8, 0x5DC)
    Sound(326, 0, 40, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_28_2D24 end

    def Function_29_2D76(): pass

    label("Function_29_2D76")

    Return()

    # Function_29_2D76 end

    def Function_30_2D77(): pass

    label("Function_30_2D77")

    OP_70(0x1, 0x1AE)
    Sleep(500)
    SetChrPos(0xFE, -3000, 0, -27500, 0)
    OP_74(0x1, 0x1E)
    BeginChrThread(0xFE, 1, 0, 32)
    BeginChrThread(0x18, 1, 0, 31)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    Sound(1019, 0, 100, 0)
    OP_71(0x1, 0x24E, 0x276, 0x1, 0x0)
    OP_79(0x1)
    Sound(288, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_71(0x1, 0x276, 0x28A, 0x1, 0x0)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_71(0x1, 0x28A, 0x2B2, 0x1, 0x0)
    Return()

    # Function_30_2D77 end

    def Function_31_2E04(): pass

    label("Function_31_2E04")

    Sleep(500)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Return()

    # Function_31_2E04 end

    def Function_32_2E50(): pass

    label("Function_32_2E50")

    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -3500, 0, -27500)
    OP_9F(0x1, -4500, 0, -27500)
    OP_9F(0x1, -5500, 0, -27500)
    OP_9F(0x2, 0xFE, 2000, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F40, 0x32C8, 0x1)
    BeginChrThread(0xFE, 3, 0, 33)
    OP_9B(0x1, 0xFE, 0x0, 0x1F40, 0x32C8, 0x1)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_32_2E50 end

    def Function_33_2EF3(): pass

    label("Function_33_2EF3")

    Sound(114, 0, 100, 0)

    def lambda_2EFE():
        OP_96(0xFE, 0xFFFFBD98, 0x15E, 0xFFFF8FB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2EFE)

    def lambda_2F18():
        OP_D5(0xFE, 0x0, 0x2710, 0x14C08, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2F18)
    Sleep(100)

    def lambda_2F34():
        OP_96(0xFE, 0xFFFFC568, 0x32, 0xFFFF75FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F34)

    def lambda_2F4E():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0x2710, 0x2BC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2F4E)
    Sleep(50)
    Sound(1018, 0, 100, 0)

    def lambda_2F70():
        OP_96(0xFE, 0xFFFFC568, 0x64, 0xFFFFAE3E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F70)

    def lambda_2F8A():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0xFFFFD8F0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2F8A)
    Sleep(50)

    def lambda_2FA6():
        OP_D5(0xFE, 0x80E8, 0x445C0, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2FA6)
    Sleep(150)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x14, 2)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    OP_FF(0x5, 0x3B6, 0x15E, 0x2EE)
    Return()

    # Function_33_2EF3 end

    def Function_34_2FE8(): pass

    label("Function_34_2FE8")

    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_300B():
        TurnDirection(0xFE, 0xE, 20)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_300B)
    BeginChrThread(0xFE, 3, 0, 35)
    Sound(996, 2, 50, 0)
    OP_9D(0xFE, 0xFFFFCB44, 0x0, 0xFFFF86E8, 0x3E8, 0x258)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x1388, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0xFA0, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0xBB8, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x7D0, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(996, 1000, 40)
    Return()

    # Function_34_2FE8 end

    def Function_35_31D2(): pass

    label("Function_35_31D2")

    Return()

    # Function_35_31D2 end

    def Function_36_31D3(): pass

    label("Function_36_31D3")

    Sleep(2400)
    BeginChrThread(0xFE, 1, 0, 38)
    Sleep(200)
    OP_96(0xFE, 0xFFFF9A70, 0x0, 0xFFFFB5C8, 0x1B58, 0x1)
    Sleep(500)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    Return()

    # Function_36_31D3 end

    def Function_37_31FE(): pass

    label("Function_37_31FE")

    OP_9D(0xFE, 0xFFFF8AD0, 0x0, 0xFFFF9E58, 0x2EE, 0x3E8)
    Sound(902, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 39)
    Sleep(200)
    EndChrThread(0xD, 0x0)
    BeginChrThread(0xD, 0, 0, 34)
    Return()

    # Function_37_31FE end

    def Function_38_3232(): pass

    label("Function_38_3232")

    OP_D5(0xFE, 0x0, 0x20F58, 0x0, 0x190)
    OP_74(0x0, 0xC)
    OP_71(0x0, 0xDD, 0xF0, 0x1, 0x0)
    OP_79(0x0)
    OP_D5(0xFE, 0x0, 0x27100, 0x0, 0xC8)
    OP_71(0x0, 0x2EE, 0x302, 0x1, 0x0)
    Return()

    # Function_38_3232 end

    def Function_39_3278(): pass

    label("Function_39_3278")


    def lambda_327D():
        OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_327D)
    Sound(905, 0, 100, 0)
    Sound(576, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x302, 0x306, 0x1, 0x0)
    OP_79(0x0)

    label("loc_32B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C7")
    Sleep(50)
    Jump("loc_32B0")

    label("loc_32C7")

    OP_71(0x0, 0x306, 0x316, 0x1, 0x0)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_39_3278 end

    def Function_40_32D8(): pass

    label("Function_40_32D8")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFA240, 0x64, 0xFFFF6F78, 0x3E8, 0x5DC)
    Sound(326, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_3316():

        label("loc_3316")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3316")

    QueueWorkItem2(0xFE, 2, lambda_3316)
    Return()

    # Function_40_32D8 end

    def Function_41_3324(): pass

    label("Function_41_3324")

    Sleep(3000)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFAC04, 0x0, 0xFFFF7072, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_3360():

        label("loc_3360")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3360")

    QueueWorkItem2(0xFE, 2, lambda_3360)
    Return()

    # Function_41_3324 end

    def Function_42_336E(): pass

    label("Function_42_336E")

    Sleep(3000)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFA628, 0x0, 0xFFFF7842, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_33A3():

        label("loc_33A3")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_33A3")

    QueueWorkItem2(0xFE, 2, lambda_33A3)
    Return()

    # Function_42_336E end

    def Function_43_33B1(): pass

    label("Function_43_33B1")

    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x33, 0x1, 0x0)
    OP_79(0x1)
    PlayEffect(0x2, 0xFF, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(978, 0, 70, 0)
    Sound(579, 2, 80, 0)
    OP_71(0x1, 0xC9, 0xDC, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_71(0x1, 0xDD, 0x104, 0x1, 0x20)
    Return()

    # Function_43_33B1 end

    def Function_44_342F(): pass

    label("Function_44_342F")


    def lambda_3434():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3434)

    label("loc_343C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3453")
    Sleep(50)
    Jump("loc_343C")

    label("loc_3453")

    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(950, 2, 80, 0)
    PlayEffect(0x5, 0xFF, 0xE, 0x5, 0, 3500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(700)
    Sound(202, 0, 100, 0)
    StopSound(950, 1000, 80)
    Sleep(700)
    Return()

    # Function_44_342F end

    def Function_45_34B5(): pass

    label("Function_45_34B5")

    Return()

    # Function_45_34B5 end

    def Function_46_34B6(): pass

    label("Function_46_34B6")

    Sleep(150)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    TurnDirection(0xFE, 0xE, 300)
    Sleep(100)
    Sound(357, 0, 70, 0)
    PlayEffect(0x4, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 47)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xFE, 0x3)
    StopEffect(0x0, 0x2)
    EndChrThread(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 48)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_46_34B6 end

    def Function_47_3534(): pass

    label("Function_47_3534")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_354D")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_47_3534")

    label("loc_354D")

    Return()

    # Function_47_3534 end

    def Function_48_354E(): pass

    label("Function_48_354E")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_48_354E end

    def Function_49_3560(): pass

    label("Function_49_3560")

    Sleep(300)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF6D20, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    label("loc_3594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35AB")
    Sleep(50)
    Jump("loc_3594")

    label("loc_35AB")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    OP_9B(0x0, 0xFE, 0x4, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB87A, 0x1F4, 0xFFFF6F5A, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCB94, 0x0, 0xFFFF736A, 0xC8, 0x3E8)
    Return()

    # Function_49_3560 end

    def Function_50_35F4(): pass

    label("Function_50_35F4")

    Sleep(400)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF7428, 0xFA0, 0x0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    label("loc_3628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363F")
    Sleep(50)
    Jump("loc_3628")

    label("loc_363F")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x164, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB88E, 0x1F4, 0xFFFF7608, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCBC6, 0x0, 0xFFFF796E, 0xC8, 0x3E8)
    Return()

    # Function_50_35F4 end

    def Function_51_3685(): pass

    label("Function_51_3685")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_51_3685 end

    def Function_52_369B(): pass

    label("Function_52_369B")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_52_369B end

    def Function_53_36A7(): pass

    label("Function_53_36A7")

    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_53_36A7 end

    def Function_54_36B3(): pass

    label("Function_54_36B3")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    Sound(809, 0, 50, 0)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFB87A, 0x1F4, 0xFFFF6F5A, 0x258, 0x3E8)
    Sound(326, 0, 50, 0)
    Sound(809, 0, 80, 0)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFCB94, 0x0, 0xFFFF736A, 0xC8, 0x3E8)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sound(326, 0, 80, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x1, 0x7D0, 0x1388, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_93(0xFE, 0x86, 0x0)
    Sound(844, 0, 70, 0)
    Sound(250, 0, 50, 0)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFE624, 0x4B0, 0xFFFF6BAE, 0x4E2, 0x3E8)
    Return()

    # Function_54_36B3 end

    def Function_55_3773(): pass

    label("Function_55_3773")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFB88E, 0x1F4, 0xFFFF7608, 0x258, 0x3E8)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFCBC6, 0x0, 0xFFFF796E, 0xC8, 0x3E8)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0x7D0, 0x1388, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_93(0xFE, 0x21, 0x0)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFE3A4, 0x4B0, 0xFFFF895E, 0x4E2, 0x3E8)
    Return()

    # Function_55_3773 end

    def Function_56_3813(): pass

    label("Function_56_3813")

    Sound(579, 2, 100, 0)
    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    StopSound(579, 1000, 90)
    OP_71(0x1, 0x105, 0x118, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    Return()

    # Function_56_3813 end

    def Function_57_3850(): pass

    label("Function_57_3850")

    Sleep(250)
    Sound(534, 0, 100, 0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_57_3850 end

    def Function_58_390B(): pass

    label("Function_58_390B")

    Sleep(900)
    Sound(307, 0, 100, 0)
    Sound(329, 0, 100, 0)
    Sound(264, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -300, 8000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -180, 7200, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -90, 6400, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -30, 5600, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 0, 4800, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 0, 4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    Return()

    # Function_58_390B end

    def Function_59_3A8F(): pass

    label("Function_59_3A8F")

    OP_95(0xFE, -5740, 100, -36860, 7000, 0x1)
    OP_95(0xFE, -5100, 0, -30220, 7000, 0x1)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0xFFFFEB56, 0x2BC, 0xFFFF91A6, 0x2EE, 0x5DC)
    Sound(326, 0, 60, 0)
    BeginChrThread(0xFE, 3, 0, 57)

    def lambda_3AE5():
        OP_93(0xFE, 0xF0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AE5)
    Sound(844, 0, 40, 0)
    OP_9D(0xFE, 0xFFFFD198, 0x0, 0xFFFF8A44, 0x3E8, 0x5DC)
    Sound(326, 0, 60, 0)
    BeginChrThread(0xFE, 1, 0, 60)
    OP_95(0xFE, -7950, 100, -33580, 5000, 0x1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_59_3A8F end

    def Function_60_3B3C(): pass

    label("Function_60_3B3C")

    Sound(562, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(120)
    SetChrSubChip(0xFE, 0x3)
    Sleep(120)
    SetChrSubChip(0xFE, 0x4)
    Sleep(120)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    Sound(321, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1017, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(90)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(60)
    SetChrSubChip(0xFE, 0x4)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(60)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1300, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1300, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1300, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(60)
    SetChrSubChip(0xFE, 0x4)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1300, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(60)
    Sound(501, 0, 100, 0)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(300)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    Return()

    # Function_60_3B3C end

    def Function_61_4047(): pass

    label("Function_61_4047")

    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD332, 0x32, 0xFFFF7DBA, 0x5DC, 0x7D0)
    Sound(326, 0, 70, 0)

    def lambda_406F():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_406F)
    OP_96(0xFE, 0xFFFFD292, 0x0, 0xFFFF7A90, 0x1B58, 0x1)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD6F2, 0x7D0, 0xFFFF7AEA, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -250, 850, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 250, 650, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4130():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4130)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD206, 0x0, 0xFFFF6E60, 0xFA, 0x9C4)
    Sound(326, 0, 70, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFDA8, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x7D0, 0x1)
    Sleep(1300)
    BeginChrThread(0xFE, 1, 0, 62)
    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_41D5():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41D5)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFDD46, 0x11F8, 0xFFFF89F4, 0x122A, 0x1194)
    Sound(326, 0, 50, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_424B():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_424B)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD45E, 0x19C8, 0xFFFF7838, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_42C1():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42C1)
    BeginChrThread(0xFE, 3, 0, 58)
    Sound(251, 0, 50, 0)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFDB48, 0x0, 0xFFFF8058, 0xABE, 0x9C4)
    Sound(326, 0, 70, 0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_61_4047 end

    def Function_62_430A(): pass

    label("Function_62_430A")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    Sound(540, 0, 40, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x3)
    Sleep(80)
    SetChrSubChip(0xFE, 0x4)
    Sleep(80)
    SetChrSubChip(0xFE, 0x5)
    Sleep(80)
    Sound(255, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(80)
    Return()

    # Function_62_430A end

    def Function_63_4355(): pass

    label("Function_63_4355")

    OP_93(0xFE, 0x14A, 0x3C)
    OP_93(0xFE, 0x10E, 0x3C)

    def lambda_4368():
        OP_93(0xFE, 0x12C, 0x3C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4368)
    Sound(1019, 0, 100, 0)
    OP_71(0x1, 0x118, 0x140, 0x1, 0x0)
    OP_79(0x1)
    Sound(288, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_71(0x1, 0x141, 0x154, 0x1, 0x0)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x155, 0x168, 0x1, 0x0)
    Return()

    # Function_63_4355 end

    def Function_64_43B7(): pass

    label("Function_64_43B7")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0xFE, 0xFFFFCF54, 0x0, 0xFFFF8A8A, 0x1F4, 0x4B0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFB780, 0x0, 0xFFFF9E1C, 0x1F4, 0x4B0)
    Sound(326, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_43B7 end

    def Function_65_4426(): pass

    label("Function_65_4426")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFCC5C, 0x0, 0xFFFF8580, 0x1F4, 0x4B0)
    Sound(326, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB230, 0x0, 0xFFFF8EA4, 0x5DC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_4426 end

    def Function_66_4495(): pass

    label("Function_66_4495")

    TurnDirection(0xFE, 0xE, 500)
    Sleep(1500)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x3E8, 0x1)
    Return()

    # Function_66_4495 end

    def Function_67_44BB(): pass

    label("Function_67_44BB")

    TurnDirection(0xFE, 0xD, 500)
    OP_74(0x0, 0x1E)

    def lambda_44CB():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44CB)

    label("loc_44DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4584")
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(902, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(902, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)
    Jump("loc_44DB")

    label("loc_4584")

    Return()

    # Function_67_44BB end

    def Function_68_4585(): pass

    label("Function_68_4585")

    TurnDirection(0xFE, 0xD, 500)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(357, 0, 80, 0)
    PlayEffect(0x4, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 47)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_68_4585 end

    def Function_69_45EB(): pass

    label("Function_69_45EB")

    TurnDirection(0xFE, 0xD, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -19550, 100, -29800, 5000, 0x1)

    def lambda_4613():
        TurnDirection(0xFE, 0xD, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4613)
    OP_96(0xFE, 0xFFFFA9AC, 0x64, 0xFFFF7B30, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_45EB end

    def Function_70_463E(): pass

    label("Function_70_463E")

    TurnDirection(0xFE, 0xD, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 30, 0)
    OP_9D(0xFE, 0xFFFFAE98, 0x64, 0xFFFF80D0, 0x1F4, 0x5DC)
    OP_96(0xFE, 0xFFFFACFE, 0x64, 0xFFFF78E2, 0xFA0, 0x0)
    Sound(540, 0, 30, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_463E end

    def Function_71_468D(): pass

    label("Function_71_468D")

    Sound(655, 0, 50, 0)
    OP_87(0x6, 0xFF, 0x0, "Null_eyes(74)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Return()

    # Function_71_468D end

    SaveToFile()

Try(main)
