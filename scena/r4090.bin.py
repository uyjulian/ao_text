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
        "Function_3_1E6C",         # 03, 3
        "Function_4_1E94",         # 04, 4
        "Function_5_1EBC",         # 05, 5
        "Function_6_1EE4",         # 06, 6
        "Function_7_1F0C",         # 07, 7
        "Function_8_1F34",         # 08, 8
        "Function_9_1F5C",         # 09, 9
        "Function_10_1F6D",        # 0A, 10
        "Function_11_1F8D",        # 0B, 11
        "Function_12_1FB1",        # 0C, 12
        "Function_13_1FD1",        # 0D, 13
        "Function_14_2017",        # 0E, 14
        "Function_15_3DF1",        # 0F, 15
        "Function_16_3E1B",        # 10, 16
        "Function_17_3E45",        # 11, 17
        "Function_18_3EFB",        # 12, 18
        "Function_19_3FBD",        # 13, 19
        "Function_20_4069",        # 14, 20
        "Function_21_410F",        # 15, 21
        "Function_22_41AF",        # 16, 22
        "Function_23_425B",        # 17, 23
        "Function_24_4311",        # 18, 24
        "Function_25_4444",        # 19, 25
        "Function_26_4464",        # 1A, 26
        "Function_27_4484",        # 1B, 27
        "Function_28_44A4",        # 1C, 28
        "Function_29_44C4",        # 1D, 29
        "Function_30_44E4",        # 1E, 30
        "Function_31_4504",        # 1F, 31
        "Function_32_452E",        # 20, 32
        "Function_33_4552",        # 21, 33
        "Function_34_4576",        # 22, 34
        "Function_35_459A",        # 23, 35
        "Function_36_45BE",        # 24, 36
        "Function_37_45E2",        # 25, 37
        "Function_38_4611",        # 26, 38
        "Function_39_463A",        # 27, 39
        "Function_40_4663",        # 28, 40
        "Function_41_468C",        # 29, 41
        "Function_42_46B5",        # 2A, 42
        "Function_43_46DE",        # 2B, 43
        "Function_44_4707",        # 2C, 44
        "Function_45_472A",        # 2D, 45
        "Function_46_64AF",        # 2E, 46
        "Function_47_64F1",        # 2F, 47
        "Function_48_6533",        # 30, 48
        "Function_49_6575",        # 31, 49
        "Function_50_65B7",        # 32, 50
        "Function_51_65F9",        # 33, 51
        "Function_52_664F",        # 34, 52
        "Function_53_6691",        # 35, 53
        "Function_54_66D3",        # 36, 54
        "Function_55_66E1",        # 37, 55
        "Function_56_66F7",        # 38, 56
        "Function_57_672D",        # 39, 57
        "Function_58_6782",        # 3A, 58
        "Function_59_6882",        # 3B, 59
        "Function_60_6990",        # 3C, 60
        "Function_61_69AF",        # 3D, 61
        "Function_62_69F4",        # 3E, 62
        "Function_63_6A32",        # 3F, 63
        "Function_64_6A57",        # 40, 64
        "Function_65_6AA2",        # 41, 65
        "Function_66_6B75",        # 42, 66
        "Function_67_6C0B",        # 43, 67
        "Function_68_6C2A",        # 44, 68
        "Function_69_6D14",        # 45, 69
        "Function_70_6DC7",        # 46, 70
        "Function_71_6E7A",        # 47, 71
        "Function_72_6E97",        # 48, 72
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
    Jump("loc_F58")

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
        (
            "#10308F#12P...We came out into the\x01",
            "open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PI only came here for\x01",
            "training, but...\x02",
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
            "#00005F#5PHuh? Was there a dead\x01",
            "end here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PNo, another animal trail\x01",
            "continues ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PLooks like fallen trees\x01",
            "have blocked the path...\x02\x03",
            "#00301FI guess they fell about\x01",
            "a month ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PB-But then, where did\x01",
            "that monster go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PI sense some kind of\x01",
            "presence...\x02",
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
        "#00305F#11PIs this laughing!?\x02",
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
            "#3571V#40W#50AHehe... Each and every\x01",
            "one of you had the guts\x01",
            "to show up, eh?\x02",
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
            "#3572V#40W#30ANaive, as always...\x07\x00\x02",
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
            "#10107F#5PDon't tell me... It's\x01",
            "the culprit who\x01",
            "manipulated the monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PN-No... Not exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PThis voice... I feel\x01",
            "like I've heard it\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10310F#6P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#12PHey now, there's no way\x01",
            "that─\x02",
        )
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
        "#10307F#2914V#6P#4S#10AHere he comes─ Get back!\x02",
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

    label("loc_F58")

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

    def lambda_1037():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFFE70, 0x1388, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1037)
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
        "#00007F#5PWha!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PAn o-ogre!?\x02",
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
            "#3574V#40W#4S#18A...GWAH HA HA HA HA HA\x01",
            "HAH...\x07\x00\x02",
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
            "#10110FI don't believe it, it's\x01",
            "the same as when someone\x01",
            "demonizes with Gnosis!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x104,
        "#00311FYou... Could you be...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0x101,
        "#00007FWald─ Is that you!?\x02",
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
            "#23A#3S#3576V#50WHehehe...#800W...\x01",
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
            "It's been quite a long\x01",
            "time.\x02\x03",
            "#30WHehe... And Wazy...\x01",
            "You're here too, huh.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10306F#12P#NYeah... that's right.\x02\x03",
            "#10308FI knew about your bad\x01",
            "taste in fashion, but...\x02\x03",
            "#10310FSay what you like, isn't\x01",
            "that going a bit too\x01",
            "far?\x02",
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
            "#11P#30WHehe... Zip it.\x07\x00\x02",
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
            "#10107F#4P#NT-Then, it was you who\x01",
            "made the train derail!?\x02",
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
            "#30WHehe... Why go to the\x01",
            "trouble of confirming\x01",
            "something you already know?\x02\x03",
            "#30WAs if the likes of those\x01",
            "monsters could've done\x01",
            "anything like that...\x02",
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
            "#4SNone other than I, Wald Wales,\x01",
            "who has obtained a new\x01",
            ""power", could have done iiit!\x07\x00\x02",
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
        (
            "#00310F#11PThat's not funny, you\x01",
            "know...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WNow then, you've already\x01",
            "chased me all the way\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WShall we get started\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WI'll make you understand to\x01",
            "the very core of your being\x01",
            "just how superior I am!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#11PUgh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11P...It seems you're\x01",
            "serious.\x02",
        )
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
            "#30WHehe. It doesn't matter if\x01",
            "I'm serious against the\x01",
            "likes of you...\x02\x03",
            "#30WI'll at least pat you gently\x01",
            "enough so you don't die, so\x01",
            "be sure to enjoy it, okay?\x02",
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
            "#4S─This true "power" I've\x01",
            "obtaaained!!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1E4E")
    Battle("BattleInfo_450", 0x30200011, 0x0, 0x100, 0x13, 0xFF)
    Jump("loc_1E5E")

    label("loc_1E4E")

    Battle("BattleInfo_40C", 0x30200011, 0x0, 0x100, 0x13, 0xFF)

    label("loc_1E5E")

    FadeToDark(0, 0, -1)
    Call(0, 14)
    Return()

    # Function_2_62C end

    def Function_3_1E6C(): pass

    label("Function_3_1E6C")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_3_1E6C end

    def Function_4_1E94(): pass

    label("Function_4_1E94")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_1E94 end

    def Function_5_1EBC(): pass

    label("Function_5_1EBC")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_1EBC end

    def Function_6_1EE4(): pass

    label("Function_6_1EE4")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_6_1EE4 end

    def Function_7_1F0C(): pass

    label("Function_7_1F0C")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1F0C end

    def Function_8_1F34(): pass

    label("Function_8_1F34")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1F34 end

    def Function_9_1F5C(): pass

    label("Function_9_1F5C")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_9_1F5C end

    def Function_10_1F6D(): pass

    label("Function_10_1F6D")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Return()

    # Function_10_1F6D end

    def Function_11_1F8D(): pass

    label("Function_11_1F8D")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x78, 0x82, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_11_1F8D end

    def Function_12_1FB1(): pass

    label("Function_12_1FB1")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3F2, 0x3FC, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x1, 0x20)
    Return()

    # Function_12_1FB1 end

    def Function_13_1FD1(): pass

    label("Function_13_1FD1")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x335, 0x339, 0x1, 0x8)
    OP_79(0x0)

    label("loc_1FE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2016")
    OP_74(0x0, 0x1)
    OP_71(0x0, 0x339, 0x33B, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x33B, 0x339, 0x1, 0x8)
    OP_79(0x0)
    Jump("loc_1FE4")

    label("loc_2016")

    Return()

    # Function_13_1FD1 end

    def Function_14_2017(): pass

    label("Function_14_2017")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AD")
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
    Jump("loc_2220")

    label("loc_21AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F0")
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
    Jump("loc_2220")

    label("loc_21F0")

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

    label("loc_2220")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2430")
    FadeToBright(0, 0)
    Jump("loc_33B4")

    label("loc_2430")

    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268E")
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W...Hey now... How do you\x01",
            "guys like that?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WNo matter what you do,\x01",
            "isn't it just too\x01",
            "disappointing?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2514():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2514)

    def lambda_252D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_252D)
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
        "#00006F#4P#NTch... *pant pant*...\x02",
    )

    CloseMessageWindow()

    def lambda_258E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_258E)

    def lambda_25A7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_25A7)
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
        (
            "#00108F#12P#NI-It had no effect at\x01",
            "all?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_260E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_260E)

    def lambda_2627():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2627)
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
        "#00206F#12P#NThis is unbelievable...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_290C")

    label("loc_268E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FE")
    OP_2C(0xA8, 0x1)
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WHehe... Well that's just\x01",
            "how it is.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WOh, man... Have I become\x01",
            "a little too strong?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#4P#NGuh...\x02",
    )

    CloseMessageWindow()

    def lambda_273D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_273D)

    def lambda_2756():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2756)

    def lambda_276F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_276F)
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
            "#10108F#4P#NA-After all we did to\x01",
            "him, it had almost no\x01",
            "effect!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_290C")

    label("loc_27FE")

    OP_2C(0xA8, 0x2)
    SetMessageWindowPos(10, 80, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WHehe... I guess you're\x01",
            "weaker than I thought.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WI wanted to have a little more\x01",
            "fun, but it looks like you'll\x01",
            "all end up getting eaten...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00013F#4P#NUgh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#12P#NTch... Is this all six\x01",
            "people can do!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_290C")


    ChrTalk(
        0x105,
        "#10303F#12P#N...............\x02",
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
            "#30WHehe... What's wrong,\x01",
            "Wazy...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WWhy don't you try saying some\x01",
            "of your usual bullshit with\x01",
            "that pretty face of yours.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WIf you don't, it just\x01",
            "won't be any fun, don't\x01",
            "you think?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10306F─Wald.\x02\x03",
            "#10301FJust where the heck did\x01",
            "you get Gnosis?\x02",
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
        (
            "#00011F#11PN-Now that you mention\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PExcept for investigation samples,\x01",
            "all of it manufactured by Dr.\x01",
            "Joachim should've been destroyed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PDamn you... Where the\x01",
            "hell did you get it!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WHehe... I wonder.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WAnd don't misunderstand.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WThis "power" isn't just\x01",
            "from the drug...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WThe drug is just a trigger─\x01",
            "This is a pure "power" born\x01",
            "from my own self.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WIt's different from the\x01",
            "sham "power" that\x01",
            "Joachim obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00201F#11P...Indeed... Unlike\x01",
            "Doctor Joachim, it seems\x01",
            "he's not going berserk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PTrigger aside, it means\x01",
            "you've mastered it, eh?\x02",
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
        "#2S#5PW-What the!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x1C, 8000, 0, 2250, 270)

    NpcTalk(
        0x1C,
        "Man's Voice",
        "#2S#11PA m-monster!?\x02",
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
        "#00305F#6PMireille!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6P2nd Lt. Mireille!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PThank goodness! The\x01",
            "repair work is over,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07905F#11PY-Yes, and so we hurried\x01",
            "here, but...\x02\x03",
            "#07907FW-What's with that\x01",
            "monster...!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30DE():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30DE)
    Sleep(50)

    def lambda_30EE():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_30EE)
    Sleep(50)

    def lambda_30FE():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_30FE)
    Sleep(50)

    def lambda_310E():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_310E)
    Sleep(50)

    def lambda_311E():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_311E)
    Sleep(50)

    def lambda_312E():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_312E)
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
            "#30WHehe... I guess we'll\x01",
            "end here for today.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WSpecial Support\x01",
            "Section... and\x01",
            "especially you, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WLet me have a little\x01",
            "more fun next time we\x01",
            "meet, will you?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WLike that chase battle\x01",
            "we had downtown,\x01",
            "alright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00013F#11PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#11PBastard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10307F#11PWald!\x02",
    )

    CloseMessageWindow()
    OP_68(6000, 1000, 2000, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#07901F#11PA-As if we'd let you go!\x02\x03",
            "#07907FAll personnel, battle\x01",
            "stations! Use of missile\x01",
            "pods authorized!\x02",
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

    label("loc_33B4")

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
            "#40A#3575VBwah hah... \x01",
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

    def lambda_38DE():
        OP_9C(0xFE, 0xFFFEEE90, 0x0, 0x7530, 0x88B8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_38DE)
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

    def lambda_39D8():
        OP_9D(0xFE, 0xFFFF9688, 0x23F0, 0x79AE, 0x1388, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_39D8)
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

    def lambda_3A76():
        OP_9D(0xFE, 0xFFFF444E, 0x3458, 0x57E4, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A76)
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

    def lambda_3B14():
        OP_9C(0xFE, 0xFFFEE2D8, 0x0, 0x9C40, 0x36B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3B14)
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
            "Afterwards, Lloyd and the others cooperated with\x01",
            "Mireille's unit and searched the dense woodland,\x01",
            "but...\x02\x03",
            "In the end, they found no trace of the demonized\x01",
            "Wald.\x02\x03",
            "Then, after giving up the search as the night wore\x01",
            "on...\x02\x03",
            "Lloyd and the others returned to the Support Section\x01",
            "late that night and, without even the energy to eat\x01",
            "the hot pot KeA had prepared, they slept like logs.\x02",
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

    # Function_14_2017 end

    def Function_15_3DF1(): pass

    label("Function_15_3DF1")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3DFE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DFE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_3DF1 end

    def Function_16_3E1B(): pass

    label("Function_16_3E1B")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E28():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E28)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_3E1B end

    def Function_17_3E45(): pass

    label("Function_17_3E45")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E52():
        OP_95(0xFE, 1950, 0, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E52)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3E87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EFA")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3E87")

    label("loc_3EFA")

    Return()

    # Function_17_3E45 end

    def Function_18_3EFB(): pass

    label("Function_18_3EFB")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F08():
        OP_95(0xFE, -2100, 0, 9400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F08)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3F49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FBC")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3F49")

    label("loc_3FBC")

    Return()

    # Function_18_3EFB end

    def Function_19_3FBD(): pass

    label("Function_19_3FBD")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3FCA():
        OP_95(0xFE, 1700, 0, 7650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FCA)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_4003")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4068")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(987, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_4003")

    label("loc_4068")

    Return()

    # Function_19_3FBD end

    def Function_20_4069(): pass

    label("Function_20_4069")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4076():
        OP_95(0xFE, 1100, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4076)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_40A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410E")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(567, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_40A9")

    label("loc_410E")

    Return()

    # Function_20_4069 end

    def Function_21_410F(): pass

    label("Function_21_410F")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_411C():
        OP_95(0xFE, -550, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_411C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_414F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41AE")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_414F")

    label("loc_41AE")

    Return()

    # Function_21_410F end

    def Function_22_41AF(): pass

    label("Function_22_41AF")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_41BC():
        OP_95(0xFE, 1950, 0, -1300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41BC)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_41F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_425A")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(530, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_41F5")

    label("loc_425A")

    Return()

    # Function_22_41AF end

    def Function_23_425B(): pass

    label("Function_23_425B")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4268():
        OP_95(0xFE, 2300, 0, -3900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4268)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_429D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4310")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_429D")

    label("loc_4310")

    Return()

    # Function_23_425B end

    def Function_24_4311(): pass

    label("Function_24_4311")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4443")
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
    Jump("Function_24_4311")

    label("loc_4443")

    Return()

    # Function_24_4311 end

    def Function_25_4444(): pass

    label("Function_25_4444")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_4444 end

    def Function_26_4464(): pass

    label("Function_26_4464")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_4464 end

    def Function_27_4484(): pass

    label("Function_27_4484")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_4484 end

    def Function_28_44A4(): pass

    label("Function_28_44A4")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_44A4 end

    def Function_29_44C4(): pass

    label("Function_29_44C4")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_44C4 end

    def Function_30_44E4(): pass

    label("Function_30_44E4")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_44E4 end

    def Function_31_4504(): pass

    label("Function_31_4504")

    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_4504 end

    def Function_32_452E(): pass

    label("Function_32_452E")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_452E end

    def Function_33_4552(): pass

    label("Function_33_4552")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_4552 end

    def Function_34_4576(): pass

    label("Function_34_4576")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_4576 end

    def Function_35_459A(): pass

    label("Function_35_459A")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_459A end

    def Function_36_45BE(): pass

    label("Function_36_45BE")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_45BE end

    def Function_37_45E2(): pass

    label("Function_37_45E2")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    OP_9D(0xFE, 0x154A, 0x0, 0x18EC, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_37_45E2 end

    def Function_38_4611(): pass

    label("Function_38_4611")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x50, 0x0, 0x2CD8, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_38_4611 end

    def Function_39_463A(): pass

    label("Function_39_463A")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1068, 0x0, 0x2314, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_39_463A end

    def Function_40_4663(): pass

    label("Function_40_4663")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2CBA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_40_4663 end

    def Function_41_468C(): pass

    label("Function_41_468C")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x672, 0x0, 0xFFFFE502, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_41_468C end

    def Function_42_46B5(): pass

    label("Function_42_46B5")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x154A, 0x0, 0xFFFFF7EA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_42_46B5 end

    def Function_43_46DE(): pass

    label("Function_43_46DE")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1324, 0x0, 0xFFFFEA98, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_43_46DE end

    def Function_44_4707(): pass

    label("Function_44_4707")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x173, 0x17A, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x17A, 0x173, 0x1, 0x8)
    OP_79(0x0)
    Return()

    # Function_44_4707 end

    def Function_45_472A(): pass

    label("Function_45_472A")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A5B")
    FadeToBright(0, 0)
    Jump("loc_51E8")

    label("loc_4A5B")

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
        (
            "#00006F#50W#5P*pant pant pant*...\x01",
            "Ugh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P...Hmph. Quite\x01",
            "admirable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12PTo think the likes of a mere\x01",
            "detective could toy with the\x01",
            "newborn State Guard like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6PIsn't he a former\x01",
            "colleague of 2nd Lt.\x01",
            "Seeker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6P"As expected", I should\x01",
            "say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PAll right, let's disarm\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11POrders are to capture\x01",
            "him without hurting him\x01",
            "too much.\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7356", 0)
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    ChrTalk(
        0x101,
        "#00015F#60W#5P...I... refuse...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 10000)

    def lambda_4C8B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C8B)
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
        "#12PYou!\x02",
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
            "#11P...I don't get it. Why\x01",
            "is he going this far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PIt appears you can't\x01",
            "stomach the formation of\x01",
            "a new Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PEven if you struggled\x01",
            "alone, the situation\x01",
            "would never change.\x02",
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
            "...Even so, if no one\x01",
            "stands up, nothing will\x01",
            "ever change!\x02\x03",
            "#00015FI can't just go with the\x01",
            "flow... I have to see the\x01",
            "truth with my own eyes...\x02\x03",
            "#00007FAnd to take back... those\x01",
            "I care about!\x02",
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
            "#00007F#4S#5PI... I'll never give up!\x02\x03",
            "#4SNo matter how many times it\x01",
            "takes! I'll stand up even\x01",
            "if you break my legs...!\x02",
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
            "#5PCharge at him all at\x01",
            "once. Make him\x01",
            "surrender.\x02",
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
        "#12PAim for the legs.\x02",
    )

    CloseMessageWindow()

    label("loc_51E8")

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
            "I'll never give up until\x01",
            "the end...)\x02\x03",
            "#00003F(KeA... ...Elie...\x01",
            "Tio...)\x02\x03",
            "(Randy... Wazy...\x01",
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
            "#2949V#40W#4S─Goodness.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2950V#40W#4SIt seems there's someone\x01",
            "you forgot to beg.\x02",
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
        "#5PT-That just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PIt resonated in my head─\x02",
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

    def lambda_5786():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5786)
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
            "#2951V#40W#4SBegone─ O soldiers who\x01",
            "defend a false holy\x01",
            "land.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 155, -1, -1)
    SetChrName("Great White Wolf")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2952V#40W#4SI will take care of this\x01",
            "man.\x02",
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
        "#11P#4SD-Don't mess with us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#4SThe newborn Crossbell\x01",
            "State Guard yielding to\x01",
            "a mere Cryptid─\x02",
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
        "#5P#50W......Huh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11P#50W......Uwah......\x02",
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

    def lambda_5DEA():

        label("loc_5DEA")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5DEA")

    QueueWorkItem2(0x101, 2, lambda_5DEA)

    def lambda_5DFC():

        label("loc_5DFC")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5DFC")

    QueueWorkItem2(0x10, 2, lambda_5DFC)

    def lambda_5E0E():

        label("loc_5E0E")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E0E")

    QueueWorkItem2(0x11, 2, lambda_5E0E)

    def lambda_5E20():

        label("loc_5E20")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E20")

    QueueWorkItem2(0x12, 2, lambda_5E20)

    def lambda_5E32():

        label("loc_5E32")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E32")

    QueueWorkItem2(0x13, 2, lambda_5E32)

    def lambda_5E44():

        label("loc_5E44")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E44")

    QueueWorkItem2(0x14, 2, lambda_5E44)

    def lambda_5E56():

        label("loc_5E56")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E56")

    QueueWorkItem2(0x15, 2, lambda_5E56)

    def lambda_5E68():

        label("loc_5E68")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5E68")

    QueueWorkItem2(0x16, 2, lambda_5E68)
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
            "#30W─Well then. Shall I\x01",
            "repeat myself?\x02",
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
        "#60W#12P#60W...There's no need...\x02",
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
            "#30WHmm, I think I really\x01",
            "shocked them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30WIt's been a long time since\x01",
            "I've been in this form, so I'm\x01",
            "not so great at controlling it.\x02",
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
            "#00006F#5P#30W...There's so much I'd\x01",
            "like to say, but...\x02\x03",
            "For now, let me just say\x01",
            "this.\x02",
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
            "#30WYes, what is it?\x02",
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
            "#00007F#12P#4S#N─Zeit! Isn't your timing\x01",
            "just too good!?\x02",
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

    # Function_45_472A end

    def Function_46_64AF(): pass

    label("Function_46_64AF")

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

    # Function_46_64AF end

    def Function_47_64F1(): pass

    label("Function_47_64F1")

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

    # Function_47_64F1 end

    def Function_48_6533(): pass

    label("Function_48_6533")

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

    # Function_48_6533 end

    def Function_49_6575(): pass

    label("Function_49_6575")

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

    # Function_49_6575 end

    def Function_50_65B7(): pass

    label("Function_50_65B7")

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

    # Function_50_65B7 end

    def Function_51_65F9(): pass

    label("Function_51_65F9")

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

    # Function_51_65F9 end

    def Function_52_664F(): pass

    label("Function_52_664F")

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

    # Function_52_664F end

    def Function_53_6691(): pass

    label("Function_53_6691")

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

    # Function_53_6691 end

    def Function_54_66D3(): pass

    label("Function_54_66D3")

    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_54_66D3 end

    def Function_55_66E1(): pass

    label("Function_55_66E1")

    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x18, 500)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_55_66E1 end

    def Function_56_66F7(): pass

    label("Function_56_66F7")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_670E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_670E)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_56_66F7 end

    def Function_57_672D(): pass

    label("Function_57_672D")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6744():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6744)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_57_672D end

    def Function_58_6782(): pass

    label("Function_58_6782")

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

    label("loc_685B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6881")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    Jump("loc_685B")

    label("loc_6881")

    Return()

    # Function_58_6782 end

    def Function_59_6882(): pass

    label("Function_59_6882")

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

    def lambda_6969():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6969)
    Sound(811, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x2)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_6882 end

    def Function_60_6990(): pass

    label("Function_60_6990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69AE")
    OP_A1(0xFE, 0x9C4, 0x8, 0x10, 0x11, 0x12, 0x11, 0x10, 0x13, 0x14, 0x13)
    Jump("Function_60_6990")

    label("loc_69AE")

    Return()

    # Function_60_6990 end

    def Function_61_69AF(): pass

    label("Function_61_69AF")

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

    # Function_61_69AF end

    def Function_62_69F4(): pass

    label("Function_62_69F4")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_62_69F4 end

    def Function_63_6A32(): pass

    label("Function_63_6A32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A56")
    OP_82(0x3C, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_63_6A32")

    label("loc_6A56")

    Return()

    # Function_63_6A32 end

    def Function_64_6A57(): pass

    label("Function_64_6A57")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AA1")
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 200, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_64_6A57")

    label("loc_6AA1")

    Return()

    # Function_64_6A57 end

    def Function_65_6AA2(): pass

    label("Function_65_6AA2")

    BeginChrThread(0xFE, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 71)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)

    def lambda_6AC3():
        OP_9B(0x0, 0xFE, 0x163, 0x61A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AC3)
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

    # Function_65_6AA2 end

    def Function_66_6B75(): pass

    label("Function_66_6B75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C0A")
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, -2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, 2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_66_6B75")

    label("loc_6C0A")

    Return()

    # Function_66_6B75 end

    def Function_67_6C0B(): pass

    label("Function_67_6C0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C29")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_67_6C0B")

    label("loc_6C29")

    Return()

    # Function_67_6C0B end

    def Function_68_6C2A(): pass

    label("Function_68_6C2A")

    Sound(917, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -30500, 1500, 20080, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6CA3():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CA3)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x2, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_6C2A end

    def Function_69_6D14(): pass

    label("Function_69_6D14")

    Sound(917, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6D56():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D56)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_6D14 end

    def Function_70_6DC7(): pass

    label("Function_70_6DC7")

    Sound(917, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6E09():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E09)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_6DC7 end

    def Function_71_6E7A(): pass

    label("Function_71_6E7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E96")
    Sleep(100)
    Sound(914, 0, 100, 0)
    Sleep(800)
    Jump("Function_71_6E7A")

    label("loc_6E96")

    Return()

    # Function_71_6E7A end

    def Function_72_6E97(): pass

    label("Function_72_6E97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB3")
    Sleep(250)
    Sound(914, 0, 100, 0)
    Sleep(650)
    Jump("Function_72_6E97")

    label("loc_6EB3")

    Return()

    # Function_72_6E97 end

    SaveToFile()

Try(main)
