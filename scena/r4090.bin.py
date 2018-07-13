from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r4090.bin",                # FileName
        "r4090",                    # MapName
        "r4090",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 166, 0, 0, 0, 1],
    )

    BuildStringList((
        "r4090",                  # 0
        "CGF Member",             # 1
        "CGF Member",             # 2
        "CGF Member",             # 3
        "CGF Member",             # 4
        "CGF Member",             # 5
        "CGF Member",             # 6
        "Demon Wald",             # 7
        "2nd Lt. Mireille",       # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "State Guard Soldier",    # 11
        "State Guard Soldier",    # 12
        "State Guard Soldier",    # 13
        "State Guard Soldier",    # 14
        "State Guard Soldier",    # 15
        "State Guard Commander",  # 16
        "Zeit",                   # 17
        "倒木",                   # 18
        "倒木",                   # 19
        "倒木",                   # 20
        "汎用ダミー",             # 21
        "SE制御",                 # 22
        "br4020",                 # 23
        "br4020",                 # 24
    ))

    ATBonus("ATBonus_32C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_450", 0x11C2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_40C", 0x00E2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1464, 0)                                       # 0

    ScpFunction((
        "Function_0_5B8",          # 00, 0
        "Function_1_5F3",          # 01, 1
        "Function_2_62C",          # 02, 2
        "Function_3_1EA0",         # 03, 3
        "Function_4_1EC8",         # 04, 4
        "Function_5_1EF0",         # 05, 5
        "Function_6_1F18",         # 06, 6
        "Function_7_1F40",         # 07, 7
        "Function_8_1F68",         # 08, 8
        "Function_9_1F90",         # 09, 9
        "Function_10_1FA1",        # 0A, 10
        "Function_11_1FC1",        # 0B, 11
        "Function_12_1FE5",        # 0C, 12
        "Function_13_2005",        # 0D, 13
        "Function_14_204B",        # 0E, 14
        "Function_15_3E6C",        # 0F, 15
        "Function_16_3E96",        # 10, 16
        "Function_17_3EC0",        # 11, 17
        "Function_18_3F76",        # 12, 18
        "Function_19_4038",        # 13, 19
        "Function_20_40E4",        # 14, 20
        "Function_21_418A",        # 15, 21
        "Function_22_422A",        # 16, 22
        "Function_23_42D6",        # 17, 23
        "Function_24_438C",        # 18, 24
        "Function_25_44BF",        # 19, 25
        "Function_26_44DF",        # 1A, 26
        "Function_27_44FF",        # 1B, 27
        "Function_28_451F",        # 1C, 28
        "Function_29_453F",        # 1D, 29
        "Function_30_455F",        # 1E, 30
        "Function_31_457F",        # 1F, 31
        "Function_32_45A9",        # 20, 32
        "Function_33_45CD",        # 21, 33
        "Function_34_45F1",        # 22, 34
        "Function_35_4615",        # 23, 35
        "Function_36_4639",        # 24, 36
        "Function_37_465D",        # 25, 37
        "Function_38_468C",        # 26, 38
        "Function_39_46B5",        # 27, 39
        "Function_40_46DE",        # 28, 40
        "Function_41_4707",        # 29, 41
        "Function_42_4730",        # 2A, 42
        "Function_43_4759",        # 2B, 43
        "Function_44_4782",        # 2C, 44
        "Function_45_47A5",        # 2D, 45
        "Function_46_6559",        # 2E, 46
        "Function_47_659B",        # 2F, 47
        "Function_48_65DD",        # 30, 48
        "Function_49_661F",        # 31, 49
        "Function_50_6661",        # 32, 50
        "Function_51_66A3",        # 33, 51
        "Function_52_66F9",        # 34, 52
        "Function_53_673B",        # 35, 53
        "Function_54_677D",        # 36, 54
        "Function_55_678B",        # 37, 55
        "Function_56_67A1",        # 38, 56
        "Function_57_67D7",        # 39, 57
        "Function_58_682C",        # 3A, 58
        "Function_59_692C",        # 3B, 59
        "Function_60_6A3A",        # 3C, 60
        "Function_61_6A59",        # 3D, 61
        "Function_62_6A9E",        # 3E, 62
        "Function_63_6ADC",        # 3F, 63
        "Function_64_6B01",        # 40, 64
        "Function_65_6B4C",        # 41, 65
        "Function_66_6C1F",        # 42, 66
        "Function_67_6CB5",        # 43, 67
        "Function_68_6CD4",        # 44, 68
        "Function_69_6DBE",        # 45, 69
        "Function_70_6E71",        # 46, 70
        "Function_71_6F24",        # 47, 71
        "Function_72_6F41",        # 48, 72
    ))


    def Function_0_5B8(): pass

    label("Function_0_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 2)

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5E0")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_5F2")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5F2")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 45)

    label("loc_5F2")

    Return()

    # Function_0_5B8 end

    def Function_1_5F3(): pass

    label("Function_1_5F3")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF3C4169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_616")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_62B")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_62B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_62B")

    Return()

    # Function_1_5F3 end

    def Function_2_62C(): pass

    label("Function_2_62C")

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
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadEffect(0x0, "event/ev10008.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    LoadEffect(0x2, "event/ev14006.eff")
    SoundLoad(2914)
    SoundLoad(3571)
    SoundLoad(3572)
    SoundLoad(3573)
    SoundLoad(3574)
    SoundLoad(3576)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_7C2")
    SetChrPos(0x101, -2000, 0, 1550, 270)
    SetChrPos(0x102, -1600, 0, 2550, 270)
    SetChrPos(0x103, -200, 0, 1750, 270)
    SetChrPos(0x104, -350, 0, 3100, 270)
    SetChrPos(0x109, -400, 0, 750, 270)
    SetChrPos(0x105, 850, 0, 2350, 270)
    Jump("loc_828")

    label("loc_7C2")

    SetChrPos(0x101, 11000, 0, 1550, 270)
    SetChrPos(0x102, 11400, 0, 2550, 270)
    SetChrPos(0x103, 12800, 0, 1750, 270)
    SetChrPos(0x104, 12650, 0, 3100, 270)
    SetChrPos(0x109, 12600, 0, 750, 270)
    SetChrPos(0x105, 13850, 0, 2350, 270)

    label("loc_828")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_855")
    FadeToBright(0, 0)
    Jump("loc_F90")

    label("loc_855")

    FadeToBright(1000, 0)
    OP_68(-2000, 15700, 2000, 0)
    MoveCamera(345, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28000, 0)
    OP_68(-2000, 700, 2000, 15000)
    MoveCamera(315, 25, 0, 15000)
    SetCameraDistance(56000, 15000)
    Sleep(7000)

    def lambda_8B9():
        OP_9B(0x0, 0x101, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B9)
    Sleep(50)

    def lambda_8D1():
        OP_9B(0x0, 0x102, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8D1)
    Sleep(50)

    def lambda_8E9():
        OP_9B(0x0, 0x103, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E9)
    Sleep(50)

    def lambda_901():
        OP_9B(0x0, 0x104, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_901)
    Sleep(50)

    def lambda_919():
        OP_9B(0x0, 0x109, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_919)
    Sleep(50)

    def lambda_931():
        OP_9B(0x0, 0x105, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_931)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-1000, 700, 2000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x105,
        "#10308F#12P...We came out into the open.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PI too came only around\x01",
            "here for training...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#5POh...?\x01",
            "Was it a dead end here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PNo, there should be another\x01",
            "animal trail further ahead too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PIt appears fallen trees\x01",
            "have blocked the road...\x02\x03",
            "#00301FDid they fall about a month ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PB-But then, where has\x01",
            "that monster gone...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12P...I sense some kind\x01",
            "of presence...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3574, 255, 100, 0)
    Sound(833, 0, 40, 0)
    StopBGM(0xFA0)
    Fade(1500)
    SetCameraDistance(19000, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#00011F#5P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PIs it a laughing voice...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 15, -1, -1)
    SetChrName("Ominous Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3571V#40W#50AEh eh... Every one of you have\x01",
            "come here unconcerned, eh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrName("Ominous Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3572V#40W#30ASimple guys, as always...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    OP_68(-1000, 1000, 2000, 0)
    MoveCamera(225, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(35000, 0)
    OP_68(-1000, 1000, 2000, 10000)
    MoveCamera(270, 15, 0, 10000)
    SetCameraDistance(16650, 10000)
    OP_0D()

    ChrTalk(
        0x101,
        "#00013F#5PT-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#5PDon't tell me that... It's the culprit \x01",
            "who manipulated the monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PN-No... Moreover...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PThis voice... It's like I have \x01",
            "already heard it somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10310F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PHey now, there's no way that──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1000, 1000, 2000, 500)
    MoveCamera(270, 15, 0, 500)
    SetCameraDistance(15650, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x105,
        "#10307F#2914V#6P#4S#10AHere he comes──back away!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00010F#5P!!#8A\x02",
    )

    CloseMessageWindow()

    label("loc_F90")

    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xE, -22000, 17000, 15000, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x393, 0x3A2, 0x1, 0x8)
    Sound(3552, 255, 100, 0)
    Sound(200, 0, 50, 0)
    Sound(251, 0, 100, 0)
    OP_68(-22000, 22000, 15000, 0)
    MoveCamera(315, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10000, 0)
    OP_68(-3000, 1300, 2000, 2300)
    MoveCamera(315, 20, 0, 2300)
    SetCameraDistance(18500, 2300)
    Sound(834, 0, 100, 0)

    def lambda_106F():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFFE70, 0x1388, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_106F)
    Sleep(1500)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sound(3544, 255, 100, 0)
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(248, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xE, 0x5, 0, 1000, 3000, 0, 0, 0, 1500, 2500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x5, 0, 2500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x12C, 0x1388, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x109, 3, 0, 7)
    BeginChrThread(0x105, 3, 0, 8)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_82(0x96, 0x5A, 0x1388, 0x3E8)
    SetChrPos(0xE, -6000, 0, 0, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0xE, 3, 0, 9)
    SetChrFlags(0xE, 0x1)
    OP_68(-6000, 2300, 300, 0)
    MoveCamera(200, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(7800, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xA)
    OP_68(-1350, 1300, 300, 3000)
    MoveCamera(115, 18, 0, 3000)
    SetCameraDistance(12800, 3000)
    Sleep(500)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#5PWha──!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PAn o-ogre...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 150, -1, -1)
    SetChrName("Ogre")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3573V#50W#12A...Heh heh heh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0x3E8, 0x3E8)
    SetChrName("Ogre")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3574V#40W#4S#18A...GWAH HA HA HA HA HA HAH...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Sound(889, 0, 40, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    EndChrThread(0xE, 0x3)
    OP_74(0x0, 0x5)
    OP_68(-5000, 2100, 2000, 0)
    MoveCamera(180, 51, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13650, 0)
    OP_68(-5000, 4000, 2000, 5000)
    MoveCamera(270, -10, 0, 5000)
    SetCameraDistance(7350, 5000)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_71(0x0, 0x3DE, 0x3F2, 0x1, 0x8)
    OP_79(0x0)
    CancelBlur(0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107F............!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FT-This is...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10110FA-Absurd, it's the same as when \x01",
            "someone demonizes with Gnosis...!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x104,
        "#00311FYou...could you be...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00007FWald──\x01",
            "Is that you!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Ogre")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#23A#3S#3576V#50WEh eh eh...#1500W...\x01",
            "#40W#5SHA HA HA HA HA HA HA HA HA HA HAH!\x07\x00\x02",
        )
    )

    Sleep(1200)
    Fade(300)
    Sound(196, 0, 70, 0)
    Sound(200, 0, 60, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1200)
    OP_68(-5000, 3500, 2000, 1000)
    MoveCamera(270, 40, 0, 1000)
    SetCameraDistance(16000, 1000)
    BeginChrThread(0xE, 3, 0, 10)
    WaitChrThread(0xE, 3)
    OP_82(0x1F4, 0x0, 0xBB8, 0x4B0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 11)
    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WBannings and Orlando...\x01",
            "It's been quite a long time.\x02\x03",
            "#30WEh eh...  \x01",
            "And Wazy...you too, huh.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10306F#12P#NYeah...that's right.\x02\x03",
            "#10308FI knew about your bad\x01",
            "taste in fashion, but...\x02\x03",
            "#10310FSay what you like, as you can imagine\x01",
            "isn't that going too far, hm...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#30WEh eh...zip it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#4P#NW-Wait a moment!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10107F#4P#NT-Then it was you who\x01",
            "made the train derail...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh... Why're you confirming\x01",
            "on purpose something obvious...?\x02\x03",
            "#30WAs if those puny monsters could've\x01",
            "done something like that, eh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-5000, 4200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(7000, 0)
    Sound(892, 0, 100, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xE, 0x5, 0, 500, 0, 0, 0, 0, 2000, 2500, 2000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-500, 2300, 2000, 1000)
    MoveCamera(270, 14, 0, 1000)
    SetCameraDistance(23000, 1000)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 12)
    Sleep(500)
    CancelBlur(500)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(-1, 110, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4SOnly I, Wald Wales, who have obtained\x01",
            "a new "power", could've done iiit!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 10000)
    OP_0D()

    ChrTalk(
        0x103,
        "#00210F#11P......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PHow dreadful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PThat's not funny, you know...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WWell then, you've come all the way\x01",
            "here on purpose to chase me down...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WShould we start at once...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WTo make you understand thoroughly...\x01",
            "How much "superior" I am...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#11PKh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#11P...It seems you're serious.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 3200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    OP_68(-5000, 4500, 2000, 2000)
    SetCameraDistance(8250, 2000)
    MoveCamera(270, 15, 0, 2000)
    StopBGM(0xFA0)
    EndChrThread(0xE, 0x3)
    Sound(889, 0, 70, 0)
    BeginChrThread(0xE, 3, 0, 13)
    Sleep(500)
    StopSound(889, 1000, 70)
    CancelBlur(500)
    Sleep(1500)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh, it's now pointless to get\x01",
            "serious for the likes of you...\x02\x03",
            "#30WI'll pat you as gently as possible,\x01",
            "to an extent so you won't die...\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(6730, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S──To savor this genuine\x01",
            ""power" I've obtaaained!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-5000, 5800, 2000, 0)
    MoveCamera(270, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_68(-5000, 1500, 2000, 500)
    SetCameraDistance(23000, 500)
    EndChrThread(0xE, 0x3)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1E82")
    Battle("BattleInfo_450", 0x30200011, 0x0, 0x100, 0x13, 0xFF)
    Jump("loc_1E92")

    label("loc_1E82")

    Battle("BattleInfo_40C", 0x30200011, 0x0, 0x100, 0x13, 0xFF)

    label("loc_1E92")

    FadeToDark(0, 0, -1)
    Call(0, 14)
    Return()

    # Function_2_62C end

    def Function_3_1EA0(): pass

    label("Function_3_1EA0")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_3_1EA0 end

    def Function_4_1EC8(): pass

    label("Function_4_1EC8")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_1EC8 end

    def Function_5_1EF0(): pass

    label("Function_5_1EF0")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_1EF0 end

    def Function_6_1F18(): pass

    label("Function_6_1F18")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_6_1F18 end

    def Function_7_1F40(): pass

    label("Function_7_1F40")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1F40 end

    def Function_8_1F68(): pass

    label("Function_8_1F68")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1F68 end

    def Function_9_1F90(): pass

    label("Function_9_1F90")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_9_1F90 end

    def Function_10_1FA1(): pass

    label("Function_10_1FA1")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Return()

    # Function_10_1FA1 end

    def Function_11_1FC1(): pass

    label("Function_11_1FC1")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x78, 0x82, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_11_1FC1 end

    def Function_12_1FE5(): pass

    label("Function_12_1FE5")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3F2, 0x3FC, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x1, 0x20)
    Return()

    # Function_12_1FE5 end

    def Function_13_2005(): pass

    label("Function_13_2005")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x335, 0x339, 0x1, 0x8)
    OP_79(0x0)

    label("loc_2018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_204A")
    OP_74(0x0, 0x1)
    OP_71(0x0, 0x339, 0x33B, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x33B, 0x339, 0x1, 0x8)
    OP_79(0x0)
    Jump("loc_2018")

    label("loc_204A")

    Return()

    # Function_13_2005 end

    def Function_14_204B(): pass

    label("Function_14_204B")

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
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadChrToIndex("chr/ch32650.itc", 0x30)
    LoadChrToIndex("chr/ch32651.itc", 0x31)
    LoadChrToIndex("chr/ch32657.itc", 0x32)
    LoadChrToIndex("chr/ch32653.itc", 0x33)
    LoadChrToIndex("chr/ch31250.itc", 0x34)
    LoadChrToIndex("chr/ch31251.itc", 0x35)
    LoadChrToIndex("chr/ch31252.itc", 0x36)
    LoadChrToIndex("chr/ch31253.itc", 0x37)
    LoadChrToIndex("apl/ch51444.itc", 0x38)
    SoundLoad(3575)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/cr326000.eff")
    LoadEffect(0x3, "event\\ev15010.eff")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x5A, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFFFFCFB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E1")
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_2254")

    label("loc_21E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2224")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_2254")

    label("loc_2224")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_2254")

    SetChrPos(0x101, 1000, 0, 1550, 270)
    SetChrPos(0x102, 1400, 0, 2550, 270)
    SetChrPos(0x103, 2800, 0, 1750, 270)
    SetChrPos(0x104, 2650, 0, 3100, 270)
    SetChrPos(0x109, 2600, 0, 750, 270)
    SetChrPos(0x105, 3850, 0, 2350, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x30)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x34)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x34)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x34)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x34)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xF, 12000, 0, 2000, 270)
    SetChrPos(0x8, 13700, 0, 3000, 270)
    SetChrPos(0x9, 14700, 0, 2500, 270)
    SetChrPos(0xA, 15300, 0, 3500, 270)
    SetChrPos(0xB, 13200, 0, 1000, 270)
    SetChrPos(0xC, 15000, 0, 1500, 270)
    SetChrPos(0xD, 15300, 0, 500, 270)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2464")
    FadeToBright(0, 0)
    Jump("loc_3426")

    label("loc_2464")

    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C6")
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W...Hey now...\x01",
            "Are you looking down on me?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WNo matter what you do,\x01",
            "that's not enough at all...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2545():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2545)

    def lambda_255E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_255E)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x101, 2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#00006F#4P#NKh...*pant pant*...\x02",
    )

    CloseMessageWindow()

    def lambda_25BD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_25BD)

    def lambda_25D6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_25D6)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        "#00108F#12P#NI-Is it not having effect at all...?\x02",
    )

    CloseMessageWindow()

    def lambda_2647():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2647)

    def lambda_2660():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2660)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x103,
        "#00206F#12P#NThat's unbelievable...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2937")

    label("loc_26C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2841")
    OP_2C(0xA8, 0x1)
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh... \x01",
            "Well, that's to be expected.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WOh, man...\x01",
            "Have I become a little too strong?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#4P#NKh...\x02",
    )

    CloseMessageWindow()

    def lambda_2777():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2777)

    def lambda_2790():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2790)

    def lambda_27A9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_27A9)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#10108F#4P#NA-After all we did to him,\x01",
            "it's almost not having effect...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2937")

    label("loc_2841")

    OP_2C(0xA8, 0x2)
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh...\x01",
            "You're weaker than I thought, eh?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WI wanted to have some fun, but\x01",
            "you'll all end up getting eaten...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00013F#4P#NKh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#12P#NTch...\x01",
            "This is all six people can do!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2937")


    ChrTalk(
        0x105,
        "#10303F#12P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 15000)
    Sleep(500)
    SetMessageWindowPos(10, 120, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh...what's wrong, Wazy...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WTry saying something affected with that\x01",
            "tidy mug of yours like always, won't you...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WIf you don't do that, it won't \x01",
            "be fun, don't you think...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10306F──Wald.\x02\x03",
            "#10301FWhere the heck did\x01",
            "you get "Gnosis"?\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PN-Now that you mention it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PThose manufactured by Doctor Joachim \x01",
            "should all have been disposed, with the\x01",
            "exception of the investigation samples...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PDamn you...\x01",
            "Where the hell did you get it!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh...I wonder.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WAlso, don't misunderstand.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WThis "power" is not\x01",
            "due to the drug at all...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WThe drug is just a trigger──\x01",
            "This is a pure "power"\x01",
            "born from my own self.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WIt's different from the sham "power"\x01",
            "that Joachim had obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00201F#11P...Indeed...\x01",
            "Unlike at that time with Doctor Joachim,\x01",
            "it seems he is not going berserk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PTrigger aside, it means\x01",
            "you've mastered it, eh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-530, 2600, 2300, 0)
    MoveCamera(271, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    Sleep(300)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrPos(0x1C, 8000, 0, 1750, 270)

    NpcTalk(
        0x1C,
        "Man's Voice",
        "#2S#5PW-What the...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x1C, 8000, 0, 2250, 270)

    NpcTalk(
        0x1C,
        "Man's Voice",
        "#2S#11PA m-monster...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x1C, 0x80)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(12000, 1000, 2000, 0)
    OP_68(4500, 1000, 2000, 2500)
    MoveCamera(45, 24, 0, 0)
    MoveCamera(35, 21, 0, 2500)
    OP_6E(510, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 2500)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)
    OP_93(0x105, 0x5A, 0x0)
    SetMapObjFlags(0x0, 0x4)
    BeginChrThread(0xF, 3, 0, 15)
    Sleep(10)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xC, 3, 0, 16)
    BeginChrThread(0xD, 3, 0, 16)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        "#00305F#6PMireille...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6P2nd Lt. Mireille...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PThank goodness...!\x01",
            "The repair works are over, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07905F#11PY-Yes, and so we came \x01",
            "running in haste, but...\x02\x03",
            "#07907FW-What's that monster...!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3158():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3158)
    Sleep(50)

    def lambda_3168():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3168)
    Sleep(50)

    def lambda_3178():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3178)
    Sleep(50)

    def lambda_3188():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3188)
    Sleep(50)

    def lambda_3198():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3198)
    Sleep(50)

    def lambda_31A8():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_31A8)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(55, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_0D()
    SetMessageWindowPos(10, 120, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WEh eh...I guess today it ends here.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WSpecial Support Section...and Wazy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WNext time, make me have\x01",
            "at least some fun, eh...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WAt least like during that chase\x01",
            "battle we had in Downtown, huh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00013F#11PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PBastard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10307F#11PWald...!\x02",
    )

    CloseMessageWindow()
    OP_68(6000, 1000, 2000, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#07901F#11PA-As if we'd let you go!\x02\x03",
            "#07907FAll personnel, battle stations!\x01",
            "I permit you the missile pods use too!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("CGF Members")

    AnonymousTalk(
        0xFF,
        "#4SYES MA'AM!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3426")

    Fade(500)
    OP_68(7150, 1500, 2000, 0)
    MoveCamera(270, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13800, 0)
    OP_68(-1750, 1500, 2000, 3000)
    MoveCamera(310, 9, 0, 3000)
    SetCameraDistance(19800, 3000)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xF, 6000, 0, 2000, 270)
    SetChrPos(0x8, 7700, 0, 3000, 270)
    SetChrPos(0x9, 8700, 0, 2500, 270)
    SetChrPos(0xA, 9300, 0, 3500, 270)
    SetChrPos(0xB, 7200, 0, 1000, 270)
    SetChrPos(0xC, 9000, 0, 1500, 270)
    SetChrPos(0xD, 9300, 0, 500, 270)
    BeginChrThread(0xF, 3, 0, 17)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x9, 3, 0, 19)
    BeginChrThread(0xA, 3, 0, 20)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xC, 3, 0, 22)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 26)
    BeginChrThread(0x103, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    BeginChrThread(0x109, 3, 0, 29)
    BeginChrThread(0x105, 3, 0, 30)
    OP_6F(0x79)
    BeginChrThread(0x101, 0, 0, 24)
    MoveCamera(295, 9, 0, 9000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_0D()
    Fade(500)
    OP_68(-5000, 3300, 2000, 0)
    MoveCamera(270, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    MoveCamera(270, 30, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40A#3575VBwah ha...\x01",
            "#4SYou're weeeak!!\x07\x00\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 4250, 2000, 1200)
    MoveCamera(270, 15, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(9000, 1200)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0x7)
    OP_71(0x0, 0x335, 0x33E, 0x1, 0x8)
    OP_79(0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x33E, 0x348, 0x1, 0x8)
    Sound(3543, 255, 100, 0)
    Sound(833, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0x2328, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x3, 0xFF, 0xE, 0x5, 0, 2000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(-5000, 800, 2000, 1000)
    MoveCamera(270, 16, 0, 1000)
    SetCameraDistance(33000, 1000)
    Sleep(700)
    CancelBlur(500)
    BeginChrThread(0xF, 3, 0, 37)
    BeginChrThread(0x8, 3, 0, 38)
    BeginChrThread(0x9, 3, 0, 39)
    BeginChrThread(0xA, 3, 0, 40)
    BeginChrThread(0xB, 3, 0, 41)
    BeginChrThread(0xC, 3, 0, 42)
    BeginChrThread(0xD, 3, 0, 43)
    BeginChrThread(0x101, 3, 0, 31)
    BeginChrThread(0x102, 3, 0, 32)
    BeginChrThread(0x103, 3, 0, 33)
    BeginChrThread(0x104, 3, 0, 34)
    BeginChrThread(0x109, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)

    ChrTalk(
        0xF,
        "#07911FEeeek!?\x05\x02",
    )


    ChrTalk(
        0xD,
        "Uwaaah!?\x05\x02",
    )

    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xF, 3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-5000, 2800, 2000, 0)
    MoveCamera(120, 42, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27000, 0)
    BeginChrThread(0xE, 3, 0, 44)
    OP_D5(0xE, 0x0, 0x5F370, 0x0, 0x0)
    OP_D5(0xE, 0x0, 0x4BAF0, 0x0, 0x2BC)
    WaitChrThread(0xE, 3)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_68(-5000, 3800, 2000, 2000)
    MoveCamera(340, -15, 0, 2000)
    SetCameraDistance(12000, 2000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x105, 0x118, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x119, 0x122, 0x1, 0x20)
    Sleep(500)
    OP_68(-5000, 10000, 2000, 500)
    MoveCamera(340, -40, 0, 500)
    SetCameraDistance(20000, 500)
    OP_82(0xC8, 0x1F4, 0xFA0, 0x1F4)
    Sound(833, 0, 80, 0)
    Sound(251, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(1000)

    def lambda_394E():
        OP_9C(0xFE, 0xFFFEEE90, 0x0, 0x7530, 0x88B8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_394E)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x1)
    OP_74(0x0, 0x2D)
    OP_71(0x0, 0x123, 0x12C, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x140, 0x1, 0x20)
    OP_0D()
    Sleep(2500)
    Fade(500)
    EndChrThread(0xE, 0x1)
    OP_F0(0x0, 0x1)
    OP_F0(0x1, 0x3E8)
    OP_68(-26540, 13300, 18780, 0)
    MoveCamera(85, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(48960, 0)
    OP_68(-26540, 8300, 18780, 4000)
    MoveCamera(112, 23, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(73320, 4000)
    SetChrPos(0xE, -18600, 15800, 15800, 0)

    def lambda_3A48():
        OP_9D(0xFE, 0xFFFF9688, 0x23F0, 0x79AE, 0x1388, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A48)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x141, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_3AE6():
        OP_9D(0xFE, 0xFFFF444E, 0x3458, 0x57E4, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3AE6)
    OP_74(0x0, 0x23)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x4CE78, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_3B84():
        OP_9C(0xFE, 0xFFFEE2D8, 0x0, 0x9C40, 0x36B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3B84)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(550)
    BlurSwitch(0x96, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_82(0x5DC, 0x5DC, 0x1388, 0x3E8)
    Sleep(1000)
    CancelBlur(3000)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    OP_0D()
    StopBGM(0x2710)
    Fade(1000)
    OP_68(-14380, 14500, -2230, 0)
    MoveCamera(350, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(60750, 0)
    OP_68(-14380, 14500, -2230, 10000)
    MoveCamera(308, 0, 0, 10000)
    SetCameraDistance(60750, 10000)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "searched the vast dense woodland\x01",
            "cooperating with Mireille's troops, but...\x02\x03",
            "In the end, they couldn't\x01",
            "find the demonized Wald.\x02\x03",
            "Then, after aborting the search for\x01",
            "the moment due to night approaching...\x02\x03",
            "Lloyd and the others returned to the SSS towards midnight\x01",
            "and fell asleep like logs without even the energy to eat\x01",
            "the hot pot that KeA had prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x22, 2)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_204B end

    def Function_15_3E6C(): pass

    label("Function_15_3E6C")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E79():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E79)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_3E6C end

    def Function_16_3E96(): pass

    label("Function_16_3E96")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3EA3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EA3)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_3E96 end

    def Function_17_3EC0(): pass

    label("Function_17_3EC0")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3ECD():
        OP_95(0xFE, 1950, 0, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ECD)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3F02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F75")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3F02")

    label("loc_3F75")

    Return()

    # Function_17_3EC0 end

    def Function_18_3F76(): pass

    label("Function_18_3F76")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F83():
        OP_95(0xFE, -2100, 0, 9400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F83)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3FC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4037")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3FC4")

    label("loc_4037")

    Return()

    # Function_18_3F76 end

    def Function_19_4038(): pass

    label("Function_19_4038")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4045():
        OP_95(0xFE, 1700, 0, 7650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4045)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_407E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40E3")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(987, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_407E")

    label("loc_40E3")

    Return()

    # Function_19_4038 end

    def Function_20_40E4(): pass

    label("Function_20_40E4")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_40F1():
        OP_95(0xFE, 1100, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40F1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_4124")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4189")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(567, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_4124")

    label("loc_4189")

    Return()

    # Function_20_40E4 end

    def Function_21_418A(): pass

    label("Function_21_418A")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4197():
        OP_95(0xFE, -550, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4197)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_41CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4229")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_41CA")

    label("loc_4229")

    Return()

    # Function_21_418A end

    def Function_22_422A(): pass

    label("Function_22_422A")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4237():
        OP_95(0xFE, 1950, 0, -1300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4237)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_4270")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42D5")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(530, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_4270")

    label("loc_42D5")

    Return()

    # Function_22_422A end

    def Function_23_42D6(): pass

    label("Function_23_42D6")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_42E3():
        OP_95(0xFE, 2300, 0, -3900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42E3)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_4318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_438B")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_4318")

    label("loc_438B")

    Return()

    # Function_23_42D6 end

    def Function_24_438C(): pass

    label("Function_24_438C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44BE")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -6050, 0, 6310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -4270, 0, -2050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1110, 0, 2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2860, 0, 530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 0, -1780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_24_438C")

    label("loc_44BE")

    Return()

    # Function_24_438C end

    def Function_25_44BF(): pass

    label("Function_25_44BF")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_44BF end

    def Function_26_44DF(): pass

    label("Function_26_44DF")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_44DF end

    def Function_27_44FF(): pass

    label("Function_27_44FF")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_44FF end

    def Function_28_451F(): pass

    label("Function_28_451F")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_451F end

    def Function_29_453F(): pass

    label("Function_29_453F")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_453F end

    def Function_30_455F(): pass

    label("Function_30_455F")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_455F end

    def Function_31_457F(): pass

    label("Function_31_457F")

    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_457F end

    def Function_32_45A9(): pass

    label("Function_32_45A9")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_45A9 end

    def Function_33_45CD(): pass

    label("Function_33_45CD")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_45CD end

    def Function_34_45F1(): pass

    label("Function_34_45F1")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_45F1 end

    def Function_35_4615(): pass

    label("Function_35_4615")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4615 end

    def Function_36_4639(): pass

    label("Function_36_4639")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_4639 end

    def Function_37_465D(): pass

    label("Function_37_465D")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    OP_9D(0xFE, 0x154A, 0x0, 0x18EC, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_37_465D end

    def Function_38_468C(): pass

    label("Function_38_468C")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x50, 0x0, 0x2CD8, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_38_468C end

    def Function_39_46B5(): pass

    label("Function_39_46B5")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1068, 0x0, 0x2314, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_39_46B5 end

    def Function_40_46DE(): pass

    label("Function_40_46DE")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2CBA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_40_46DE end

    def Function_41_4707(): pass

    label("Function_41_4707")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x672, 0x0, 0xFFFFE502, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_41_4707 end

    def Function_42_4730(): pass

    label("Function_42_4730")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x154A, 0x0, 0xFFFFF7EA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_42_4730 end

    def Function_43_4759(): pass

    label("Function_43_4759")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1324, 0x0, 0xFFFFEA98, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_43_4759 end

    def Function_44_4782(): pass

    label("Function_44_4782")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x173, 0x17A, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x17A, 0x173, 0x1, 0x8)
    OP_79(0x0)
    Return()

    # Function_44_4782 end

    def Function_45_47A5(): pass

    label("Function_45_47A5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "eff\\cutin00.eff")
    LoadEffect(0x1, "eff\\\\step00.eff")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00056.itc", 0x20)
    LoadChrToIndex("chr/ch41450.itc", 0x21)
    LoadChrToIndex("chr/ch41451.itc", 0x22)
    LoadChrToIndex("chr/ch41452.itc", 0x23)
    LoadChrToIndex("chr/ch41453.itc", 0x24)
    LoadChrToIndex("apl/ch51613.itc", 0x25)
    SoundLoad(825)
    SoundLoad(2949)
    SoundLoad(2950)
    SoundLoad(2951)
    SoundLoad(2952)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, -36800, 0, 26550, 135)
    OP_D5(0x18, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -5000, 0, 2000, 180)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -6000, 0, -5000, 0)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -7000, 0, -3500, 0)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -8500, 0, -2500, 45)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4500, 0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, -3000, 0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2000, 0, -4500, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -500, 0, -2500, 315)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5000, 0, -2500, 0)
    SetMapObjFrame(0xFF, "touboku00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku02", 0x0, 0x1)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x2, 0x19)
    OP_49()
    SetChrPos(0x19, -28500, 0, 21580, 0)
    OP_D5(0x19, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0x3, 0x1A)
    OP_49()
    SetChrPos(0x1A, -27250, 0, 18000, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x4, 0x1B)
    OP_49()
    SetChrPos(0x1B, -24500, 0, 18250, 0)
    OP_D5(0x1B, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4AD6")
    FadeToBright(0, 0)
    Jump("loc_526C")

    label("loc_4AD6")

    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(-5000, 1000, -300, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    ChrTalk(
        0x101,
        "#00006F#50W#5P*pant pant pant*...ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P...Hmph.\x01",
            "Quite admirable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12PTo think that a mere detective\x01",
            "could've made so much fun of\x01",
            "us newborn State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6PIsn't he a former colleague\x01",
            "of 2nd Lt. Seeker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#6P"As expected", I should say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11PAll right, let's disarm him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11POrders are to capture him without\x01",
            "hurting him too much.\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7356", 0)
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    ChrTalk(
        0x101,
        "#00015F#60W#5P...I...refuse...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 10000)

    def lambda_4CFF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CFF)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 67)
    OP_0D()
    WaitChrThread(0x101, 2)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 54)
    BeginChrThread(0x10, 3, 0, 54)
    BeginChrThread(0x11, 3, 0, 54)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 54)
    BeginChrThread(0x13, 3, 0, 54)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 54)
    BeginChrThread(0x15, 3, 0, 54)
    BeginChrThread(0x16, 3, 0, 54)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)

    ChrTalk(
        0x10,
        "#12PYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12PYou can still move!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    ChrTalk(
        0x17,
        (
            "#11P...I don't get it.\x01",
            "Why going that far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PIt appears you can't stomach the\x01",
            "formation of a new Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PEven if you struggled alone, the\x01",
            "situation would never change.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5000, 1000, 2000, 8000)
    MoveCamera(0, 27, 0, 8000)
    SetCameraDistance(19500, 8000)

    ChrTalk(
        0x101,
        (
            "#00010F#5P#40WEven so...\x02\x03",
            "...Even so, \x01",
            "if no one raises,\x01",
            "nothing will ever change...!\x02\x03",
            "#00015FTo not get only swept away...\x01",
            "...To ascertain the truth\x01",
            "with my own eyes too...\x02\x03",
            "#00007FTo get back the persons...\x01",
            "...Who're precious to me too...!\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 60, 0)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 1000, 2000, 500)
    MoveCamera(0, 27, 0, 500)
    SetCameraDistance(17500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    Sleep(1200)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#4S#5PI...\x01",
            "I'll never give up!\x02\x03",
            "#4SNo matter how many times...!\x01",
            "I'll stand up even if\x01",
            "you smash my legs...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5000, 1000, -1400, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20250, 0)
    OP_0D()

    ChrTalk(
        0x10,
        "#6PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12PThis guy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5P...How regrettable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PCharge all at the same time.\x01",
            "Make him surrender.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#6PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12PAim at the legs.\x02",
    )

    CloseMessageWindow()

    label("loc_526C")

    Fade(500)
    OP_68(-5000, 1000, -300, 0)
    MoveCamera(135, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x1, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x2)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x2)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    OP_68(-5000, 1000, 2000, 2500)
    MoveCamera(0, 21, 0, 10000)
    OP_6E(550, 10000)
    SetCameraDistance(17000, 7500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2500)
    BeginChrThread(0x17, 3, 0, 46)
    BeginChrThread(0x10, 3, 0, 47)
    BeginChrThread(0x11, 3, 0, 48)
    BeginChrThread(0x12, 3, 0, 49)
    BeginChrThread(0x13, 3, 0, 50)
    BeginChrThread(0x14, 3, 0, 51)
    BeginChrThread(0x15, 3, 0, 52)
    BeginChrThread(0x16, 3, 0, 53)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#00013F#5P#40W(...Until the end...\x01",
            "I won't give up until the end...)\x02\x03",
            "#00003F(KeA...\x01",
            "...Elie...Tio...)\x02\x03",
            "(Randy...Wazy...\x01",
            "...Chief Sergei too...)\x02\x03",
            "#00010F(I beg you, please...\x01",
            "...Give me strength...!)\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    OP_6F(0x79)
    Sleep(200)
    Sound(912, 0, 100, 0)
    Fade(500)
    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(22500, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2949V#40W#4S──Goodness.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2950V#40W#4SIt seems you forgot\x01",
            "to beg someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB86)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PW-What was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PIt resounded in my head──\x02",
    )

    CloseMessageWindow()
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x7D0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x10, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x10)

    ChrTalk(
        0x10,
        "#12PEek...!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x15, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x15)

    ChrTalk(
        0x15,
        "#5PW-What the...!?\x02",
    )

    CloseMessageWindow()
    Sound(914, 0, 100, 0)
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    Sleep(500)
    Sleep(200)

    def lambda_57FC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57FC)
    BeginChrThread(0x17, 3, 0, 55)
    BeginChrThread(0x10, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 55)
    BeginChrThread(0x12, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 55)
    BeginChrThread(0x14, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 55)
    BeginChrThread(0x16, 3, 0, 55)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x101, 2)
    Fade(1000)
    SetChrPos(0x17, -5500, 0, -2150, 315)
    SetChrPos(0x12, -4750, 0, 4450, 300)
    OP_68(-36800, 4000, 26550, 0)
    MoveCamera(3, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(43000, 0)
    OP_68(-16120, 4000, 9190, 8500)
    MoveCamera(288, 3, 0, 8500)
    OP_6E(550, 8500)
    SetCameraDistance(23000, 8500)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x18, 3, 0, 65)
    WaitChrThread(0x18, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)
    OP_68(-9220, 3300, 3410, 2000)
    MoveCamera(284, 8, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(28200, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x10,
        "#5P#40W#2S......Huh......!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#40W#2S......Wha......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-9550, 3300, 4600, 0)
    MoveCamera(102, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22200, 0)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2951V#40W#4SBegone──\x01",
            "O soldiers who defend a false holy land.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 155, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2952V#40W#4SI will take care of this man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB88)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x17, 3, 0, 56)
    BeginChrThread(0x10, 3, 0, 57)

    ChrTalk(
        0x10,
        "#11PE-Eeeek...!\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x11, 3, 0, 57)
    BeginChrThread(0x12, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 57)
    BeginChrThread(0x14, 3, 0, 57)

    ChrTalk(
        0x15,
        "#11PUwaaah...!\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 57)
    BeginChrThread(0x16, 3, 0, 57)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_68(-9550, 1700, 4600, 1500)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    OP_9B(0x0, 0x17, 0x9, 0x1770, 0x1388, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    OP_A1(0x17, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x17,
        "#11P#4SD-Don't screw with us...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#4SThe newborn Crossbell State Guard\x01",
            "yielding to a mere Cryptid──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-15640, 9800, 8050, 0)
    MoveCamera(315, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-10700, 1000, 4500, 1500)
    MoveCamera(279, 26, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(18500, 1500)
    SetChrPos(0x18, -15350, 0, 8550, 225)
    SetChrPos(0x17, -10700, 0, 4500, 315)
    SetChrFlags(0x12, 0x8)
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x14, 0xE1, 0x0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0xB5, 0xDC, 0x0, 0x8)
    Sleep(300)
    CancelBlur(0)
    Sleep(850)
    StopSound(913, 700, 100)
    Sound(915, 0, 100, 0)
    SetChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 58)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_79(0x1)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    Sound(912, 0, 50, 0)

    ChrTalk(
        0x11,
        "#5P#50W......eh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11P#50W......uwah......\x02",
    )

    CloseMessageWindow()
    StopSound(912, 500, 40)
    Fade(500)
    OP_68(-8350, 5600, 2950, 0)
    MoveCamera(106, 31, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26750, 0)
    OP_68(-8350, 2100, 2950, 1500)
    MoveCamera(92, 36, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_5E67():

        label("loc_5E67")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E67")

    QueueWorkItem2(0x101, 2, lambda_5E67)

    def lambda_5E79():

        label("loc_5E79")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E79")

    QueueWorkItem2(0x10, 2, lambda_5E79)

    def lambda_5E8B():

        label("loc_5E8B")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E8B")

    QueueWorkItem2(0x11, 2, lambda_5E8B)

    def lambda_5E9D():

        label("loc_5E9D")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E9D")

    QueueWorkItem2(0x12, 2, lambda_5E9D)

    def lambda_5EAF():

        label("loc_5EAF")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5EAF")

    QueueWorkItem2(0x13, 2, lambda_5EAF)

    def lambda_5EC1():

        label("loc_5EC1")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5EC1")

    QueueWorkItem2(0x14, 2, lambda_5EC1)

    def lambda_5ED3():

        label("loc_5ED3")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5ED3")

    QueueWorkItem2(0x15, 2, lambda_5ED3)

    def lambda_5EE5():

        label("loc_5EE5")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5EE5")

    QueueWorkItem2(0x16, 2, lambda_5EE5)
    ClearChrFlags(0x12, 0x8)
    OP_64(0x17)
    SetChrFlags(0x17, 0x8)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0xB5, 0xB7, 0x1F4, 0x8)
    Sleep(500)
    ClearChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 59)
    OP_79(0x1)
    OP_74(0x1, 0x3)
    OP_71(0x1, 0xB7, 0xB5, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x12C, 0x20)
    WaitChrThread(0x17, 3)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x10, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x16, 0x2)
    Sleep(500)

    ChrTalk(
        0x17,
        "#60W#12P............\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W──Well then.\x01",
            "Should I repeat myself?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x17, 0x3)
    OP_A6(0x17, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(300)

    ChrTalk(
        0x17,
        "#60W#12P#60W...There's no need to...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-7900, 1000, 2580, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrSubChip(0x17, 0x1)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x1)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x17, 0x87, 0x1F4)
    Sleep(500)
    SetCameraDistance(25000, 750)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x17,
        "#5S#5PWithdraaaw!!!\x05\x02",
    )

    Sleep(1000)
    CancelBlur(500)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-4700, 2550, -400, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_68(-4700, 1550, -400, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x18, 0, 0, 63)
    Sound(871, 0, 60, 0)
    Sound(825, 2, 40, 0)
    BeginChrThread(0x17, 3, 0, 61)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 62)

    ChrTalk(
        0x11,
        "#5PUwaaaaaaaaaah!!\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x12, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 62)
    Sound(916, 0, 100, 0)

    ChrTalk(
        0x14,
        "#11PM-My Goddeeeeeeess!!\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 62)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x18, 0x0)
    OP_82(0x0, 0x46, 0xBB8, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(825, 1000, 40)
    OP_68(-5000, 1200, 2000, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_64(0x101)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_68(-7330, 3200, 1550, 2000)
    MoveCamera(348, 19, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(20760, 2000)
    BeginChrThread(0x18, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 72)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)
    OP_93(0x18, 0x87, 0x0)
    OP_9B(0x0, 0x18, 0x0, 0x1B58, 0xBB8, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x1D, 0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(20, 120, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30WHm, I think I've\x01",
            "really shocked them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30WIt's been a long time since I went\x01",
            "back to this form, so I don't know\x01",
            "how to restrain myself a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W...There're many things\x01",
            "I'd like to say, but...\x02\x03",
            "At any rate, let\x01",
            "me just say this.\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x1A4, 0x1AE, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x0, 0x20)
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30WHm, what is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-7330, 3200, 1550, 1200)
    MoveCamera(332, -2, 0, 1200)
    OP_6E(550, 1200)
    SetCameraDistance(20760, 1200)
    TurnDirection(0x101, 0x18, 500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x101,
        (
            "#00007F#12P#4S#N──Zeit! Don't you think your\x01",
            "timing is really too good!?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x339)
    SetScenarioFlags(0x22, 0)
    NewScene("e4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_47A5 end

    def Function_46_6559(): pass

    label("Function_46_6559")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFEC78, 0x0, 0xFFFFF254, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_46_6559 end

    def Function_47_659B(): pass

    label("Function_47_659B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -9000, 0, -3000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_47_659B end

    def Function_48_65DD(): pass

    label("Function_48_65DD")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10500, 0, 1000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_48_65DD end

    def Function_49_661F(): pass

    label("Function_49_661F")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10700, 0, 4500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_49_661F end

    def Function_50_6661(): pass

    label("Function_50_6661")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -1000, 0, -2000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_50_6661 end

    def Function_51_66A3(): pass

    label("Function_51_66A3")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 6000, 0x1)
    OP_95(0xFE, -6000, 0, 7500, 6000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_51_66A3 end

    def Function_52_66F9(): pass

    label("Function_52_66F9")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 1000, 0, 2000, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_66F9 end

    def Function_53_673B(): pass

    label("Function_53_673B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_673B end

    def Function_54_677D(): pass

    label("Function_54_677D")

    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_54_677D end

    def Function_55_678B(): pass

    label("Function_55_678B")

    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x18, 500)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_55_678B end

    def Function_56_67A1(): pass

    label("Function_56_67A1")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_67B8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67B8)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_56_67A1 end

    def Function_57_67D7(): pass

    label("Function_57_67D7")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_67EE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67EE)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_57_67D7 end

    def Function_58_682C(): pass

    label("Function_58_682C")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -10700, 500, 4500, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x7)
    ClearChrFlags(0xFE, 0x100)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    OP_D3(0x17, 0x1, "Null_kuti(41)")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x0, 0x0)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xFFFF8AD0, 0x64)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xEA60, 0x190)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x61A8, 0x190)
    OP_63(0xFE, 0x0, 300, 0x28, 0x2B, 0x64, 0x0)

    label("loc_6905")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_692B")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    Jump("loc_6905")

    label("loc_692B")

    Return()

    # Function_58_682C end

    def Function_59_692C(): pass

    label("Function_59_692C")

    Sound(915, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x5, 0x96)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x64, 0x0, 0x1388, 0x12C)
    OP_D3(0x17, 0xFF, "")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x100)
    ClearChrFlags(0xFE, 0x800)
    OP_D5(0xFE, 0x4E20, 0x0, 0x0, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFE124, 0x0, 0xA14, 0x1F4, 0x9C4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0xFE, 0x13B, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -7900, 150, 2580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_6A13():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A13)
    Sound(811, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x2)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_692C end

    def Function_60_6A3A(): pass

    label("Function_60_6A3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A58")
    OP_A1(0xFE, 0x9C4, 0x8, 0x10, 0x11, 0x12, 0x11, 0x10, 0x13, 0x14, 0x13)
    Jump("Function_60_6A3A")

    label("loc_6A58")

    Return()

    # Function_60_6A3A end

    def Function_61_6A59(): pass

    label("Function_61_6A59")

    SetChrFlags(0xFE, 0x2)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    BeginChrThread(0xFE, 1, 0, 60)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    OP_64(0xFE)
    Return()

    # Function_61_6A59 end

    def Function_62_6A9E(): pass

    label("Function_62_6A9E")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_62_6A9E end

    def Function_63_6ADC(): pass

    label("Function_63_6ADC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B00")
    OP_82(0x3C, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_63_6ADC")

    label("loc_6B00")

    Return()

    # Function_63_6ADC end

    def Function_64_6B01(): pass

    label("Function_64_6B01")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B4B")
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 200, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_64_6B01")

    label("loc_6B4B")

    Return()

    # Function_64_6B01 end

    def Function_65_6B4C(): pass

    label("Function_65_6B4C")

    BeginChrThread(0xFE, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 71)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)

    def lambda_6B6D():
        OP_9B(0x0, 0xFE, 0x163, 0x61A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B6D)
    Sleep(1800)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x19, 3, 0, 68)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1A, 3, 0, 69)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1B, 3, 0, 70)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x1D, 0x1)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -15430, 500, 8570, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    Return()

    # Function_65_6B4C end

    def Function_66_6C1F(): pass

    label("Function_66_6C1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CB4")
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, -2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, 2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_66_6C1F")

    label("loc_6CB4")

    Return()

    # Function_66_6C1F end

    def Function_67_6CB5(): pass

    label("Function_67_6CB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CD3")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_67_6CB5")

    label("loc_6CD3")

    Return()

    # Function_67_6CB5 end

    def Function_68_6CD4(): pass

    label("Function_68_6CD4")

    Sound(917, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -30500, 1500, 20080, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6D4D():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D4D)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x2, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_6CD4 end

    def Function_69_6DBE(): pass

    label("Function_69_6DBE")

    Sound(917, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6E00():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E00)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_6DBE end

    def Function_70_6E71(): pass

    label("Function_70_6E71")

    Sound(917, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6EB3():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EB3)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_6E71 end

    def Function_71_6F24(): pass

    label("Function_71_6F24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F40")
    Sleep(100)
    Sound(914, 0, 100, 0)
    Sleep(800)
    Jump("Function_71_6F24")

    label("loc_6F40")

    Return()

    # Function_71_6F24 end

    def Function_72_6F41(): pass

    label("Function_72_6F41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F5D")
    Sleep(250)
    Sound(914, 0, 100, 0)
    Sleep(650)
    Jump("Function_72_6F41")

    label("loc_6F5D")

    Return()

    # Function_72_6F41 end

    SaveToFile()

Try(main)
