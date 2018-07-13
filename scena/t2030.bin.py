from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2030.bin",                # FileName
        "t2030",                    # MapName
        "t2030",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 0, 0, 1],
    )

    BuildStringList((
        "t2030",                  # 0
        "2nd Lt. Noｱl",          # 1
        "Commander Sonya",        # 2
        "Doll",                   # 3
        "Dummy",                  # 4
        "bt2030",                 # 5
    ))

    ATBonus("ATBonus_20C", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2FC", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_31C", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bt2030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2FC", "MonsterBattlePostion_2DC", "ed7452", "ed7452", "ATBonus_20C"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   -18.0,                 -4.0,                  -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.0,                   0.800000011920929,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 8,   -37.630001068115234,   -14.710000038146973,   -3.2200000286102295,   900.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.05000000074505806,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.543334007263184,    0.7355000376701355,    0.6439999938011169,    1.0])

    DeclActor(21160,   4294966716, 4294962676, 1200,    23230,   500,     4294962066, 0x007C, 0,  7,  0x0000)
    DeclActor(16000,   0,       4294937796, 1200,    16000,   1500,    4294937796, 0x007C, 0,  2,  0x0000)

    ChipFrameInfo(904, 0)                                        # 0

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_3AC",          # 01, 1
        "Function_2_452",          # 02, 2
        "Function_3_514",          # 03, 3
        "Function_4_B6F",          # 04, 4
        "Function_5_2046",         # 05, 5
        "Function_6_26A5",         # 06, 6
        "Function_7_26C4",         # 07, 7
        "Function_8_306A",         # 08, 8
        "Function_9_316C",         # 09, 9
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_39C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_3AB")

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3AB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)

    label("loc_3AB")

    Return()

    # Function_0_388 end

    def Function_1_3AC(): pass

    label("Function_1_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DA")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3DA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DA")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_3F2")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_434")

    OP_65(0x1, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_451")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_451")

    Return()

    # Function_1_3AC end

    def Function_2_452(): pass

    label("Function_2_452")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The "Popular Cocktails - Beginners' Guide" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_510")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Pinky Rose"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_510")

    TalkEnd(0xFF)
    Return()

    # Function_2_452 end

    def Function_3_514(): pass

    label("Function_3_514")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 29000, -2220, -10000, 270)
    SetChrPos(0x106, 30500, -2220, -10680, 270)
    SetChrPos(0x103, 29960, -2220, -9450, 270)
    SetChrPos(0x104, 31060, -2220, -9070, 270)
    SetChrPos(0x107, 32970, -2220, -9240, 270)
    SetChrPos(0x105, 31580, -2220, -10100, 270)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    CreatePortrait(0, 16, 20, 528, 84, 0, 10, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis512.itp")
    OP_68(-3050, -700, -11150, 0)
    MoveCamera(318, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(34300, 0)
    FadeToBright(1000, 0)
    OP_68(10100, -700, -13000, 9000)
    MoveCamera(312, 10, 0, 9000)
    Sleep(2500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Fade(1000)
    OP_68(23250, -700, -10100, 0)
    MoveCamera(305, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15750, 2500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)

    def lambda_6CC():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CC)
    Sleep(50)

    def lambda_6E4():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6E4)
    Sleep(50)

    def lambda_6FC():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6FC)
    Sleep(50)

    def lambda_714():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_714)
    Sleep(50)

    def lambda_72C():
        OP_9B(0x0, 0x106, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_72C)
    Sleep(50)

    def lambda_744():
        OP_9B(0x0, 0x107, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_744)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_END)), "loc_8A5")

    ChrTalk(
        0x101,
        (
            "#00003F#11PThe freight platform...\x01",
            "It's been quite some time.\x02\x03",
            "#00001FLuckily, it seems there's\x01",
            "no one around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, that's 'cause it seems that the\x01",
            "transcontinental railroad service is suspended.\x02\x03",
            "#00300FI guess they don't have too\x01",
            "much staff to spare for this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_962")

    label("loc_8A5")


    ChrTalk(
        0x101,
        "#00005F#11PThis place is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PYep, it's Bellguard Gate\x01",
            "freight platform.\x02\x03",
            "#00300FBecause the transcontinental railroad service\x01",
            "is suspended, it seems they cut the staff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962")


    ChrTalk(
        0x103,
        (
            "#00204F#12PRight...\x01",
            "It is a chance to sneak in, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#12PIf Commander Sonya is here, she\x01",
            "should be in the Commander room at 3F?\x02\x03",
            "#10401FI hope we can reach her without\x01",
            "getting seen in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PIf push comes to shove, I'll do a\x01",
            "diversion and attract the attention.\x02\x03",
            "#10701FAt any rate, let's try going up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PUnderstood...\x01",
            "However, don't do anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#3C#12PHm...let's go upstairs.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 22000, -2220, -10000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 2)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_3_514 end

    def Function_4_B6F(): pass

    label("Function_4_B6F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch03950.itc", 0x1F)
    LoadChrToIndex("chr/ch03951.itc", 0x20)
    LoadChrToIndex("chr/ch03952.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00051.itc", 0x23)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10200.itp")
    SoundLoad(3526)
    SoundLoad(3527)
    SoundLoad(3528)
    SoundLoad(3529)
    SoundLoad(3530)
    SoundLoad(4116)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -17000, 0, -4000, 90)
    SetChrPos(0x106, -17810, 0, -3210, 90)
    SetChrPos(0x103, -18390, 0, -4720, 90)
    SetChrPos(0x104, -18930, 0, -3660, 90)
    SetChrPos(0x107, -19460, 0, -2370, 90)
    SetChrPos(0x105, -19650, 0, -4890, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -4800, 0, -3800, 270)
    SetChrFlags(0x8, 0x8)
    OP_32(0xFF, 0xF9, 0x0)
    OP_68(-13000, 1200, -4000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(16000, 2500)

    def lambda_CF5():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CF5)
    Sleep(30)

    def lambda_D0D():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D0D)
    Sleep(30)

    def lambda_D25():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D25)
    Sleep(30)

    def lambda_D3D():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D3D)
    Sleep(30)

    def lambda_D55():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_D55)
    Sleep(30)

    def lambda_D6D():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_D6D)
    Sleep(1500)
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Girl's Voice",
        "#3526V#1P#12A#30W──Please stop.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-12500, 1000, -4000, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-11500, 1000, -4000, 2500)
    SetCameraDistance(15200, 2500)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0x8, 0x8)
    OP_9B(0x0, 0x8, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005F#6PNoｱl...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PHow...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "...Even if now I'm part of the\x01",
            "State Guard, I understand your\x01",
            "moves to a certain degree.\x02\x03",
            "After having formed a partnership\x01",
            "with the Resistance in Mainz...\x02\x03",
            "I thought that the next place\x01",
            "you'd come would've been here.\x01",
            "So I was vaguely on lookout.\x02",
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
        0x105,
        "#10406F#6POh boy...you got us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PAs expected, I'd say...\x01",
            "Nice foresight, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10206F#11PI didn't want to\x01",
            "be right, but...\x02\x03",
            "#10201F──Have you come to talk\x01",
            "to Commander Sonya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah...precisely.\x02\x03",
            "#00001FWe heard from 2nd Lt. Mireille\x01",
            "that those who have doubts about\x01",
            "the State Guard are really many.\x02\x03",
            "I want to ask the Commander's opinion even\x01",
            "in order to find a way out of this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10208F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PMiss Noｱl...\x01",
            "Miss Fran is acting\x01",
            "with us now.\x02\x03",
            "#00201FShe is already completely fine...\x01",
            "And she wants to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6PI won't tell you to not stick\x01",
            "to your principles, but...\x02\x03",
            "#00300FWouldn't it be alright even if there was\x01",
            "at least some margin to discuss things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10203F#11PEven so...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_A1(0x8, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#10201F#11PEven so, I can't let\x01",
            "you go past here.\x02\x03",
            "As a State Guard soldier...\x02\x03",
            "I can't overlook Resistance\x01",
            "forces sneaking in the State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6PMiss Noｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6P...Oh boy.\x01",
            "You're really awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10206F#11PPlease withdraw, everyone.\x02\x03",
            "I could still...\x01",
            "Decide I didn't see you.\x02\x03",
            "#10208FEven if in time we won't\x01",
            "help but fighting each other...\x02\x03",
            "#10213F...At least for now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P──You're soft, Noｱl.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#10205F#11P...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-10390, 1000, -3670, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x320, 0x3E8, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00001F#6PIf you're a true State Guard soldier,\x01",
            "there's no use for such an argument.\x02\x03",
            "You should surround us without\x01",
            "excuses and neutralize us.\x02\x03",
            "#00006FAnd yet, you're trying to make us leave\x01",
            "with such sentimental words...\x02\x03",
            "#00013FDo you really intend to sacrifice yourself\x01",
            "for a just cause with such a soft readiness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10210F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6PMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6P#NHa ha...\x01",
            "How unusually severe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI'll tell you clearly──\x01",
            "Noｱl, you've become weak.\x02\x03",
            "You became unable to be frank\x01",
            "and singlemindedly honest.\x02\x03",
            "#00000FIf I were to face you now...\x01",
            "Even I, who isn't a soldier, could win.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetCameraDistance(14750, 500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#10211F#11P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6P#NM-Mr. Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6PHey now, what're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P──You're free to choose the weapon.\x01",
            "I'll face you alone.\x02\x03",
            "If you win, you can\x01",
            "arrest us all.\x02\x03",
            "#00013FOn the contrary──\x01",
            "If I win, you'll be mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#10205F#3527V#11P#10A#30W#4SEH.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1300)
    OP_64(0xFFFF)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Fade(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)

    def lambda_1B01():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B01)
    SetChrFlags(0x8, 0x20)
    OP_9B(0x1, 0x8, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
    ClearChrFlags(0x8, 0x20)
    WaitChrThread(0x8, 2)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x8,
        "#10214F#3528V#11P#20A#50WW-What a-are you sa...!?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI can't look at you...\x02\x03",
            "#00008FRemaining in a place\x01",
            "where you can't be yourself...\x02\x03",
            "#00013FAs your companion, I can't\x01",
            "ignore this any longer.\x02\x03",
            "#00007FLet's fight──\x01",
            "2nd Lt. Noｱl Seeker!\x02",
        )
    )

    CloseMessageWindow()
    Fade(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sound(2463, 255, 100, 0)

    ChrTalk(
        0x8,
        "#10210F#11P#6AKh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(809, 0, 70, 0)
    OP_68(-9600, 1000, -3670, 1000)
    OP_9C(0x8, 0x3E8, 0x0, 0x0, 0x12C, 0xFA0)
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_A1(0x8, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-12500, 1000, -4000, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x107, 0x190, 1900, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    ChrTalk(
        0x104,
        (
            "#00306F#6P(Hey hey hey...!\x01",
            "Heaven forbid!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P(...No way.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#6P(...Eeehm...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6P(Uhhm, hasn't he\x01",
            "gone berserk...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#3C#6P(Hu hu, indeed.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    Fade(500)
    PlayBGM("ed7452", 0)
    OP_68(-9630, 1000, -3450, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-9630, 1000, -3450, 13000)
    MoveCamera(49, 18, 0, 13000)
    OP_6E(600, 13000)
    SetCameraDistance(15000, 13000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#10210F#3529V#11P#30A#30W──Fine!\x01",
            "I won't lose!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#10207F#3530V#4S#11P#25AYou're on!\x01",
            "Detective Lloyd Bannings!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCA)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(4116, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00007F#4S#6P#20AYeah, bring it on!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(5000, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x1000)

    def lambda_1FBD():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FBD)

    def lambda_1FD2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FD2)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x8, 0x1)
    ClearChrFlags(0x101, 0x1000)
    SetChrBattleFlags(0x106, 0x8)
    SetChrBattleFlags(0x103, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    SetChrBattleFlags(0x107, 0x8)
    Battle("BattleInfo_31C", 0x0, 0x0, 0x0, 0x22, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x106, 0x8)
    ClearChrBattleFlags(0x103, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    ClearChrBattleFlags(0x107, 0x8)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 5)
    Return()

    # Function_4_B6F end

    def Function_5_2046(): pass

    label("Function_5_2046")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch12200.itc", 0x1F)
    LoadChrToIndex("chr/ch03953.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10600.itp")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -11000, 0, -4000, 90)
    SetChrPos(0x106, -13810, 0, -3210, 90)
    SetChrPos(0x103, -14390, 0, -4720, 90)
    SetChrPos(0x104, -14930, 0, -3660, 90)
    SetChrPos(0x107, -15460, 0, -2370, 90)
    SetChrPos(0x105, -15650, 0, -4890, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    BeginChrThread(0x101, 0, 0, 6)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -8000, 0, -4000, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 5000, 180)
    SetChrFlags(0x9, 0x8)
    OP_68(-9500, 1000, -4000, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00015F#40W#6P*pant*... *pant*...\x02\x03",
            "#00000F#30W...I...won.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21EF():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_21EF)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10206F#40W#11P......Kh......\x01",
            "......uuuh......\x02\x03",
            "#10208F...I'm sorry...\x01",
            "...Commander Sonya...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x8)

    NpcTalk(
        0x9,
        "Woman's Voice",
        "#12P──No need to apologize.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1000, 1500, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2500)
    OP_9B(0x0, 0x9, 0x0, 0xDAC, 0x7D0, 0x0)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005F#6P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#10213F#30W#6P#NC-Commander...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#NAck...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x107,
        "#01200F#3C#6P#NHm, we were noticed.\x02",
    )

    CloseMessageWindow()
    OP_68(-500, 1000, 1300, 3000)

    def lambda_242F():
        OP_9B(0x0, 0xFE, 0x8, 0x2260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_242F)
    Sleep(1500)
    Fade(500)
    OP_68(-9550, 1000, -3150, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(13500, 3000)
    EndChrThread(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    Sleep(800)
    Fade(150)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "You know that the sound of your \x01",
            "fight echoed up above too?\x02\x03",
            "Well, I had cleared put \x01",
            "the people though.\x02",
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
        "#00006F#6PI-I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6P#N...Long time no see,\x01",
            "Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#10602F#11PYes, really.\x02\x03",
            "#10606FI have an idea about the reason\x01",
            "why you came here, but...\x02\x03",
            "#10600FFor now, I think I'll hear\x01",
            "you out in my room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(13300, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t2020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2046 end

    def Function_6_26A5(): pass

    label("Function_6_26A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26C3")
    OP_A1(0xFE, 0x320, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_26A5")

    label("loc_26C3")

    Return()

    # Function_6_26A5 end

    def Function_7_26C4(): pass

    label("Function_7_26C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(21050, 720, -4390, 0)
    MoveCamera(323, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15640, 0)
    SetChrPos(0x101, 20740, 0, -3990, 90)
    SetChrPos(0x102, 20620, -890, -4950, 90)
    SetChrPos(0x103, 19290, 0, -3680, 90)
    SetChrPos(0x104, 20630, -1840, -5960, 90)
    SetChrPos(0x109, 19070, -750, -4810, 90)
    SetChrPos(0x105, 19080, -1810, -5930, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00005FI-It was in such a place...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10103FWhat was written on the card,\x01",
            ""The iron road that runs under the\x01",
            "feet of the western protectors"...\x02\x03",
            "#10100FIt was the underground freight line\x01",
            "platform of Bellguard Gate that\x01",
            "protects the national border west side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FAt any rate, it seems we\x01",
            "can't open the trunk here.\x02\x03",
            "#10302FWhy don't we move to the platform over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FYeah, let's move it there carefully.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-28050, 1300, -26470, 0)
    MoveCamera(303, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13840, 0)
    OP_78(0x1, 0xB)
    SetChrPos(0xB, -29850, 0, -26100, 0)
    OP_D5(0xB, 0x0, 0xFFFEA070, 0x0, 0x0)
    SetChrPos(0x101, -28270, 0, -26080, 270)
    SetChrPos(0x102, -28200, 0, -27310, 270)
    SetChrPos(0x103, -28200, 0, -24750, 270)
    SetChrPos(0x104, -27050, 0, -26080, 270)
    SetChrPos(0x109, -27050, 0, -27310, 270)
    SetChrPos(0x105, -27050, 0, -24750, 270)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x8)
    SetChrPos(0xA, -29850, 150, -26100, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1024, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x1)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On the reverse side of the trunk\x01",
            "there was a card attached.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The last cell is inside the city.\x01",
            "At the skyscraper that towers high, descend\x01",
            "to 21F from the 16F summit and search the\x01",
            "many windows peering into another world.\x07\x00\x02",
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
        0x102,
        (
            "#6P#00100FNo doubt, this is a\x01",
            "doll that Bell called\x01",
            ""Sharon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThis is the fourth one...\x01",
            "Only one left, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FThe problem is the final doll location\x01",
            "written on the card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FInside the city, "the skyscraper\x01",
            "that towers high"... It's a\x01",
            "reference to a quite high building.\x02\x03",
            "#10101FCould it be that Orchis Tower...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FUhhm, Orchis Tower is said \x01",
            "to be 40 floors above ground...\x02\x03",
            "#00100FBut it contradicts with the\x01",
            ""summit" being it the "16F"...\x01",
            "Maybe it's another place?\x02\x03",
            "#00106FIt also contradicts saying \x01",
            ""descend to 21F from the 16F summit"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FI believe that could be where\x01",
            "the mystery lies.\x02\x03",
            "#10304FAlso, the "many windows peering into\x01",
            "another world"... It seems we need to\x01",
            "think about what this is indicating too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FLike until now, we can think\x01",
            "about some examples.\x02\x03",
            "#00000FLet's search inside the city while\x01",
            "keeping the words' meaning in mind.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16IRosenberg Doll S\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x338, 1)
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0xA, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, -27660, 0, -26170, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x157, 4)
    OP_29(0x7A, 0x1, 0x5)
    OP_65(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_26C4 end

    def Function_8_306A(): pass

    label("Function_8_306A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DD")

    ChrTalk(
        0x101,
        (
            "#00000FIt's dangerous walking on the tracks more than this.\x01",
            "Let's quietly retrace our steps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3130")

    label("loc_30DD")


    ChrTalk(
        0x101,
        (
            "#00001F...Garrelia Fortress is this way.\x01",
            "Let's not proceed further than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3130")

    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3158")
    SetChrPos(0x0, -34000, -2220, -18820, 90)
    Jump("loc_3169")

    label("loc_3158")

    SetChrPos(0x0, -34000, -2220, -10970, 90)

    label("loc_3169")

    EventEnd(0x4)
    Return()

    # Function_8_306A end

    def Function_9_316C(): pass

    label("Function_9_316C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt's dangerous walking on the tracks more than this.\x01",
            "Let's quietly retrace our steps.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31F8")
    SetChrPos(0x0, 27940, -2220, -18600, 270)
    Jump("loc_3209")

    label("loc_31F8")

    SetChrPos(0x0, 28100, -2220, -10060, 270)

    label("loc_3209")

    EventEnd(0x4)
    Return()

    # Function_9_316C end

    SaveToFile()

Try(main)
