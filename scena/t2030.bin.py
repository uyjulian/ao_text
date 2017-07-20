from ScenarioHelper import *

def main():
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
        "Lieutenant Noel",             # 1
        "Sonya Command",           # 2
        "doll",                   # 3
        "dummy",                 # 4
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
        "Function_3_50B",          # 03, 3
        "Function_4_A91",          # 04, 4
        "Function_5_1F35",         # 05, 5
        "Function_6_2590",         # 06, 6
        "Function_7_25AF",         # 07, 7
        "Function_8_2E62",         # 08, 8
        "Function_9_2F33",         # 09, 9
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
            "\"Popular Cocktail Beginners' Guide\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_507")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Pinky Rose\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_507")

    TalkEnd(0xFF)
    Return()

    # Function_2_452 end

    def Function_3_50B(): pass

    label("Function_3_50B")

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

    def lambda_6C3():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C3)
    Sleep(50)

    def lambda_6DB():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6DB)
    Sleep(50)

    def lambda_6F3():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6F3)
    Sleep(50)

    def lambda_70B():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_70B)
    Sleep(50)

    def lambda_723():
        OP_9B(0x0, 0x106, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_723)
    Sleep(50)

    def lambda_73B():
        OP_9B(0x0, 0x107, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_73B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_END)), "loc_84C")

    ChrTalk(
        0x101,
        (
            "#00003F#11PCargo home ……\x01",
            "It's been a while since a long time ago.\x02\x03",
            "#00001FFortunately, the sign of the person\x01",
            "It seems there is nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, the transcontinental railroad\x01",
            "It seems that you are in luck.\x02\x03",
            "#00300FToo much here\x01",
            "You do not take on labor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_84C")


    ChrTalk(
        0x101,
        "#00005F#11PHere is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12POh, on the Belgard gate\x01",
            "It is a cargo home.\x02\x03",
            "#00300FThe transcontinental railroad is out of service\x01",
            "I do not think he is getting a lot of work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")


    ChrTalk(
        0x103,
        (
            "#00204F#12PI agree……\x01",
            "Whether it is a chance to infiltrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#12PIf there is a Sonja command\x01",
            "Is it the commander's office on the third floor?\x02\x03",
            "#10401FSomehow without noticing it\x01",
            "I hope to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PWhen it comes to emergency, I\x01",
            "It attracts eyes by moving positively.\x02\x03",
            "#10701FAnyway let's head up\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PI understood……\x01",
            "But do not be unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#3C#12PHmm. Let's get going\x02",
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

    # Function_3_50B end

    def Function_4_A91(): pass

    label("Function_4_A91")

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

    def lambda_C17():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C17)
    Sleep(30)

    def lambda_C2F():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C2F)
    Sleep(30)

    def lambda_C47():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C47)
    Sleep(30)

    def lambda_C5F():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C5F)
    Sleep(30)

    def lambda_C77():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_C77)
    Sleep(30)

    def lambda_C8F():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_C8F)
    Sleep(1500)
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Daughter's voice",
        "#3526V#1P#12A#30WStop right there\x02",
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
        "#00005F#6PNoel!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PWhy…\x02",
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
            "…… About your trends\x01",
            "Even the defense forces\x01",
            "I have grasped to a certain extent.\x02\x03",
            "Resistance to Mainz direction\x01",
            "After completing cooperation system … …\x02\x03",
            "If it comes next\x01",
            "I wonder if this person is\x01",
            "It was vaguely wary.\x02",
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
        "#10406F#6PWell that sucks\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PAs expected ……\x01",
            "Good read, Noel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10206F#11PI want you to win\x01",
            "I did not have it … ….\x02\x03",
            "#10201F─ ─ with Sonya Commander\x01",
            "You came here to talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah. That's right\x02\x03",
            "#00001FFrom Mr. Mireille three,\x01",
            "Those who have doubts on the Defense Forces\x01",
            "I heard that there are not a few.\x02\x03",
            "To overcome this situation\x01",
            "I want to hear the commander's true intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10208F#11P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PNoel…\x01",
            "Now, Fran?\x01",
            "We are acting together.\x02\x03",
            "#00201FI'm totally in good shape ……\x01",
            "I also want to meet Noel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6PI know that you need to stick to your principles but\x02\x03",
            "#00300FAt least the room for discussion\x01",
            "Is not it okay to leave it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10203F#11PEven still\x02",
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
            "#10201F#11PStill I feel you guys\x01",
            "I can not let you go next.\x02\x03",
            "As a soldier of the Defense Army\x02\x03",
            "Infiltration of resistance to the state\x01",
            "Because I can not miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6PNoel…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6P… …. Good luck.\x01",
            "Really, you are clumsy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10206F#11PPlease turn back, everyone\x02\x03",
            "Not yet …\x01",
            "I can do what I have not seen.\x02\x03",
            "#10208FIn any case to contend\x01",
            "Even though only it disappears …\x02\x03",
            "#10213FAt least for now….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6PYou're naive, aren't you Noel\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        "#10205F#11P!?\x02",
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
            "#00001F#6PIf you are truly a defense army soldier\x01",
            "Such a question and answer should not be necessary.\x02\x03",
            "Surround yourself with no questions\x01",
            "We can neutralize us.\x02\x03",
            "#00006FNevertheless in such a sentimental word\x01",
            "I try to leave us …\x02\x03",
            "#00013FWith such a sweet preparedness true#4R噵 噵#Into\x01",
            "Are you intending to murder a cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10210F#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6PLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6P#NHa ha …\x01",
            "It's hard not to be any good.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PLet's clearly say - ─\x01",
            "Noel, you have become weaker.\x02\x03",
            "Without any fraud, just just beginning\x01",
            "It is because I can not stay straight.\x02\x03",
            "#00000FIf you are a current opponent ……\x01",
            "I can win, even I am not a soldier.\x02",
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
        "#00205F#6P#NL-Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6POi oi what are you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P── Armament is free.\x01",
            "I will do your partner by myself.\x02\x03",
            "If you win\x01",
            "You can catch all of us.\x02\x03",
            "#00013FInstead ─\x01",
            "If I win, you will receive me#14R噵 噵 噵 噵 噵 噵 噵#.\x02",
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
        "#10205F#3527V#11P#10A#30W#4SHUH?\x02",
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

    def lambda_198E():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_198E)
    SetChrFlags(0x8, 0x20)
    OP_9B(0x1, 0x8, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
    ClearChrFlags(0x8, 0x20)
    WaitChrThread(0x8, 2)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x8,
        "#10214F#3528V#11P#20A#50WW-what are you saying!?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI can't keep watching\x02\x03",
            "#00008FYou, as you are#2RAh#In a place that is not\x01",
            "I stay still …\x02\x03",
            "#00013FNo more as the same companion,\x01",
            "I can not leave it alone.\x02\x03",
            "#00007FYou will have a match - ─\x01",
            "Noel Seoker lieutenant!\x02",
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
        "#10210F#11P#6A!?\x02",
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
            "#00306F#6P(Oooio o … …!!\x01",
            "Is it such an ant! Is it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P(This is insane)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#6P(Uhh)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6P(Well, something's okay?\x01",
            "I guess I will not say … ….? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#3C#6P(Hehe, indeed)\x02",
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
            "#10210F#3529V#11P#30A#30W── It is good!\x01",
            "I can not lose!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#10207F#3530V#4S#11P#25AIt is a game!\x01",
            "Lloyd · Bannings investigator!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCA)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(4116, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00007F#4S#6P#20ARight! Come at me!\x02",
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

    def lambda_1EAC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EAC)

    def lambda_1EC1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EC1)
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

    # Function_4_A91 end

    def Function_5_1F35(): pass

    label("Function_5_1F35")

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
            "#00015F#40W#6PAhh … ahh\x02\x03",
            "#00000F#30WIt's my win\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20EA():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_20EA)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10206F#40W#11P… … cum … … …\x01",
            "………… Uu …………\x02\x03",
            "#10208F……Excuse me……\x01",
            "……… Sonya command ………\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x8)

    NpcTalk(
        0x9,
        "Female voice",
        "#12PNo need to apologize\x02",
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
        "#00005F#6P#NAh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#10213F#30W#6P#NC-Commander\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#NUghh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x107,
        "#01200F#3C#6P#NHmm. So we were found out\x02",
    )

    CloseMessageWindow()
    OP_68(-500, 1000, 1300, 3000)

    def lambda_2336():
        OP_9B(0x0, 0xFE, 0x8, 0x2260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2336)
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
            "You, the sound of battle\x01",
            "I was echoing to the upper one?\x02\x03",
            "At least the area was clear\x02",
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
        "#00006F#6PS-sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6P#N……Long time no see.\x01",
            "Sonja Commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#10602F#11PYes, indeed\x02\x03",
            "#10606FFor what reason did you visit?\x01",
            "I have an idea ….\x02\x03",
            "#10600FTentatively in my room\x01",
            "Would you tell me a story.\x02",
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

    # Function_5_1F35 end

    def Function_6_2590(): pass

    label("Function_6_2590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25AE")
    OP_A1(0xFE, 0x320, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_2590")

    label("loc_25AE")

    Return()

    # Function_6_2590 end

    def Function_7_25AF(): pass

    label("Function_7_25AF")

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
        "#5P#00005FIn this place … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10103FWritten on the card,\x01",
            "\"The way of iron passing through the feet of the west guard\" …\x02\x03",
            "#10100FThis Belgard gate which protects the western border,\x01",
            "It was about the underground cargo line home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FAnyway, here we have a trunk\x01",
            "I do not seem to be able to open it.\x02\x03",
            "#10302FShall we move to the home there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FOh, carry it carefully.\x02",
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
            "On the back of the trunk\x01",
            "There was a card attached.\x07\x00\x02",
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
            "The last cage is in the city.\x01",
            "Skyscraper skyscraper,\x01",
            "Top of 16 layers#2RThank you#Go down from 21 more layers\x01",
            "Find numerous windows looking into different worlds.\x07\x00\x02",
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
            "#6P#00100FNo doubt, this is Bell\x01",
            "I call it \"Sharon\"\x01",
            "It should have been a doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThis is the 4th body …\x01",
            "Is there only one more place left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FThe problem was written on the card\x01",
            "It is the place of the last doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103F\"High towering skyscraper\" of \"city\" … …\x01",
            "It is a considerably tall building.\x02\x03",
            "#10101FPerhaps, to that Orkis Tower …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FWell, the Orkis Tower\x01",
            "It's about 40 stories above the ground … …\x02\x03",
            "#00100F\"16 layers\" as \"top\"\x01",
            "It is contradictory to saying,\x01",
            "I wonder if it is wrong.\x02\x03",
            "#00106F\"Top of 16 layers#2RThank you#Go down from 21 more layers. \"\x01",
            "It is contradictory though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIt's a mystery\x01",
            "It may be a point.\x02\x03",
            "#10304FAlso, \"a lot of windows looking into different worlds\" … …\x01",
            "What this is pointing at\x01",
            "It seems necessary to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FAs before,\x01",
            "I think it's a similar example.\x02\x03",
            "#00000FWhile thinking the meaning of words\x01",
            "Let's find the city.\x02",
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
            "#16IRosenberg doll · S\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｓ', 1)
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

    # Function_7_25AF end

    def Function_8_2E62(): pass

    label("Function_8_2E62")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB7")

    ChrTalk(
        0x101,
        (
            "#00000FIt is dangerous to walk a railroad more.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF7")

    label("loc_2EB7")


    ChrTalk(
        0x101,
        (
            "#00001F…… This is Galleria Fortress.\x01",
            "I can not go any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF7")

    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F1F")
    SetChrPos(0x0, -34000, -2220, -18820, 90)
    Jump("loc_2F30")

    label("loc_2F1F")

    SetChrPos(0x0, -34000, -2220, -10970, 90)

    label("loc_2F30")

    EventEnd(0x4)
    Return()

    # Function_8_2E62 end

    def Function_9_2F33(): pass

    label("Function_9_2F33")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt is dangerous to walk a railroad more.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FA1")
    SetChrPos(0x0, 27940, -2220, -18600, 270)
    Jump("loc_2FB2")

    label("loc_2FA1")

    SetChrPos(0x0, 28100, -2220, -10060, 270)

    label("loc_2FB2")

    EventEnd(0x4)
    Return()

    # Function_9_2F33 end

    SaveToFile()

Try(main)
