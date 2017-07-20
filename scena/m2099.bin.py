from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m2099.bin",                # FileName
        "m2099",                    # MapName
        "m2099",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2099",                  # 0
        "Demon",                   # 1
        "Demon",                   # 2
        "Demon",                   # 3
        "SE control",                 # 4
        "bm2099",                 # 5
    ))

    ATBonus("ATBonus_158", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_178", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_200", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_204", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_208", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_210", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_218", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_178", "MonsterBattlePostion_1F8", "ed7405", "ed7453", "ATBonus_158"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294883796, 0,       4294962296, 1200,    4294883796, 1500,    4294962296, 0x007C, 0,  2,  0x0000)

    ChipFrameInfo(660, 0)                                        # 0

    ScpFunction((
        "Function_0_294",          # 00, 0
        "Function_1_2C2",          # 01, 1
        "Function_2_2DB",          # 02, 2
        "Function_3_3D7",          # 03, 3
        "Function_4_D5B",          # 04, 4
        "Function_5_D80",          # 05, 5
        "Function_6_D9D",          # 06, 6
        "Function_7_DD6",          # 07, 7
        "Function_8_2126",         # 08, 8
        "Function_9_2157",         # 09, 9
        "Function_10_22F5",        # 0A, 10
        "Function_11_2314",        # 0B, 11
        "Function_12_232F",        # 0C, 12
        "Function_13_23B7",        # 0D, 13
    ))


    def Function_0_294(): pass

    label("Function_0_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1")
    Event(0, 3)

    label("loc_2C1")

    Return()

    # Function_0_294 end

    def Function_1_2C2(): pass

    label("Function_1_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_2D4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D4")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_2C2 end

    def Function_2_2DB(): pass

    label("Function_2_2DB")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are devices that can recover the orbment.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3C8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_2DB end

    def Function_3_3D7(): pass

    label("Function_3_3D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch75150.itc", 0x1E)
    LoadEffect(0x0, "event\\ev501_00.eff")
    SoundLoad(825)
    OP_68(39850, -450, 2630, 0)
    MoveCamera(64, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x18D, 33000, 250, 0, 90)
    SetChrPos(0x101, 32000, 250, 1200, 90)
    SetChrPos(0x102, 32000, 250, -1200, 90)
    SetChrPos(0x103, 30500, 250, 780, 90)
    SetChrPos(0x104, 30400, 250, -560, 90)
    SetChrPos(0x109, 29120, 250, 1200, 90)
    SetChrPos(0x105, 29000, 250, -920, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, 50000, -2500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 5)

    def lambda_507():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_507)
    Sleep(50)

    def lambda_524():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_524)
    Sleep(50)

    def lambda_541():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_541)
    Sleep(50)

    def lambda_55E():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55E)
    Sleep(50)

    def lambda_57B():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_57B)
    Sleep(50)

    def lambda_598():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_598)
    Sleep(50)

    def lambda_5B5():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B5)
    OP_68(45280, -450, 2660, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x105, 1)
    Sleep(500)
    Fade(500)
    OP_68(46790, -850, 1390, 0)
    MoveCamera(64, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21390, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006FFuu …\x01",
            "Finally we arrived here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FEly, this time\x01",
            "Does not it seem to be okay for me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00102FWell, yeah.\x01",
            "Lease-san is here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, certainly in such a place\x01",
            "When there is a sister,\x01",
            "You may be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FAnyway, it's a \"monastery\".\x02\x03",
            "#00304FWell, if you are with Kawaiko like this\x01",
            "I get motivated in a different way though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00211FI feel as well as ever.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FMr. Lease,\x01",
            "What on earth happened?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_816():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_816)
    Sleep(50)

    def lambda_826():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_826)
    Sleep(300)
    OP_64(0x18D)

    ChrTalk(
        0x18D,
        (
            "#12P#04403FNo, this big emblem\x01",
            "With what I was concerned about.\x02\x03",
            "#04400FBy any chance\x01",
            "An example of the \"cult\" … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FOh … did you know?\x02\x03",
            "#00001FYeah, they are in the medieval times\x01",
            "It looks like a coat of arms used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FSomehow blood smelling ceremony\x01",
            "It seems that it was done … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FBut when I came earlier\x01",
            "It was pretty tough.\x02\x03",
            "#00309FI think that the bell rang, suddenly,\x01",
            "Suddenly \"devil\" appears and ─ ─\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(827, 0, 100, 0)
    Sleep(500)
    OP_63(0x18D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A92():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A92)
    Sleep(50)

    def lambda_AA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FWell, no way …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10301FHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#6P#04401FSigns of indigenous \"demons\" ……\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1500)
    OP_68(49940, 1150, 0, 1500)
    SetCameraDistance(16020, 1500)
    OP_6F(0x11)
    Fade(1000)
    SetCameraDistance(15520, 0)
    Sound(826, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    BeginChrThread(0x101, 3, 0, 4)
    Sound(825, 2, 50, 0)
    OP_68(49940, 1550, 0, 2500)
    SetCameraDistance(12520, 2500)
    Sleep(1500)
    BeginChrThread(0x8, 3, 0, 6)
    OP_6F(0x79)
    Fade(2000)
    Sound(817, 0, 100, 0)
    WaitChrThread(0x8, 3)
    OP_0D()
    Sleep(1000)
    OP_68(49940, 250, 0, 1000)
    MoveCamera(90, 12, 0, 1000)
    SetCameraDistance(21370, 1000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#12P#00105FOh, Devil ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FWell, at a strange timing\x01",
            "Get out!\x02\x03",
            "#00306FIt sounded like it was called by me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FPlease be careful……!\x01",
            "From what I saw before\x01",
            "I feel terrible spirit pressure ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#12P#04401Fcome……!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15980, 500)
    OP_68(50940, 1050, 0, 500)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sound(830, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x8, 0x0)
    Battle("BattleInfo_218", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 7)
    Return()

    # Function_3_3D7 end

    def Function_4_D5B(): pass

    label("Function_4_D5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7F")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_4_D5B")

    label("loc_D7F")

    Return()

    # Function_4_D5B end

    def Function_5_D80(): pass

    label("Function_5_D80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9C")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_5_D80")

    label("loc_D9C")

    Return()

    # Function_5_D80 end

    def Function_6_D9D(): pass

    label("Function_6_D9D")

    ClearChrFlags(0xFE, 0x1)

    def lambda_DA7():
        OP_98(0xFE, 0x0, 0xAF0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA7)

    def lambda_DC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_D9D end

    def Function_7_DD6(): pass

    label("Function_7_DD6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04400.itp")
    LoadChrToIndex("monster/ch75150.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    LoadChrToIndex("apl/ch51256.itc", 0x25)
    LoadChrToIndex("apl/ch51257.itc", 0x26)
    LoadChrToIndex("monster/ch75153.itc", 0x27)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "event\\ev12026.eff")
    LoadEffect(0x4, "event\\ev12027.eff")
    LoadEffect(0x5, "battle\\ms00001.eff")
    LoadEffect(0x6, "event\\ev12028.eff")
    LoadEffect(0x7, "event\\ev12029.eff")
    SoundLoad(852)
    OP_68(46380, -450, 2210, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x18D, 43000, 250, 0, 90)
    SetChrPos(0x101, 42000, 250, 1200, 90)
    SetChrPos(0x102, 42000, 250, -1200, 90)
    SetChrPos(0x103, 40500, 250, 780, 90)
    SetChrPos(0x104, 40400, 250, -560, 90)
    SetChrPos(0x109, 39120, 250, 1400, 90)
    SetChrPos(0x105, 39000, 250, -1400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
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
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 50000, 0, 0, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x5)
    SetChrPos(0x9, 29320, 0, 4940, 90)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x5)
    SetChrPos(0xA, 26970, 0, -4670, 90)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00003FWow ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FNee, I managed to do something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHeck, for us now\x01",
            "I was not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00204F…… Should I stop stiffening?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301F……Wait a minute.\x01",
            "It seems to be still soon to be relieved.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(100)
    Sound(827, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 8)
    Sleep(1000)
    Fade(1000)
    Sound(202, 0, 50, 0)
    SetChrPos(0x8, 50000, 300, 0, 270)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 5)
    BeginChrThread(0xA, 0, 0, 5)
    OP_68(43050, -450, 1610, 3000)
    MoveCamera(56, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(28950, 3000)

    def lambda_127B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_127B)
    Sleep(50)

    def lambda_128B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_128B)
    Sleep(50)

    def lambda_129B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_129B)
    Sleep(50)

    def lambda_12AB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12AB)
    Sleep(50)

    def lambda_12BB():
        OP_95(0xFE, 34530, 250, 2090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12BB)

    def lambda_12D5():
        OP_95(0xFE, 34440, 250, -3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12D5)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x5A, 0x0)
    Sound(831, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00010FDamn\x01",
            "Have you still breathed? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203F…… Apparently Immortal#4RUndead#In the family of\x01",
            "It looks like a series of demons ……\x02\x03",
            "#00200FWith weapons and magic on hand\x01",
            "Who knocks down completely\x01",
            "It may be impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00110FSounds like that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00310FChit\x01",
            "It's a nasty trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHowever, somehow\x01",
            "I have to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00007FFor a while Lease\x01",
            "Go behind us!\x02\x03",
            "No matter what we do\x01",
            "I will protect you ─ ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#6P#04403F……House.\x01",
            "That is not necessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(44800, -450, 1370, 1500)
    MoveCamera(62, 27, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18970, 1500)
    OP_6F(0x79)
    Fade(500)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x18D, 0x25)
    SetChrSubChip(0x18D, 0x0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 60, 0)
    Sound(852, 2, 100, 0)
    BeginChrThread(0x18D, 1, 0, 11)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00005Feh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#6P#04407FForward#2RYes#Erase\x01",
            "Infinity Sparrow!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18D, 0x1)
    BeginChrThread(0x18D, 3, 0, 9)
    OP_68(44180, -450, 1040, 1000)
    MoveCamera(62, 27, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(32119, 1000)
    OP_6F(0x79)
    WaitChrThread(0x18D, 3)
    Sleep(500)
    StopBGM(0xFA0)
    Fade(500)
    Sound(831, 0, 60, 0)
    Sound(514, 0, 100, 0)
    SetChrPos(0x8, 50000, 0, 0, 270)
    SetChrPos(0x9, 34530, 0, 2090, 90)
    SetChrPos(0xA, 34440, 0, -3100, 90)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrChipByIndex(0x9, 0x27)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    BeginChrThread(0xB, 1, 0, 12)
    PlayEffect(0x6, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x6, 0x2)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#6P#00005FBecome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00305FAre you serious……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#00205FIn that moment … that much demon ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#6P#04403F… It is finishing.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0x26)
    SetChrSubChip(0x18D, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 60, 0)
    Sound(852, 2, 100, 0)
    BeginChrThread(0x18D, 3, 0, 10)

    def lambda_17A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17A3)

    def lambda_17B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17B4)

    def lambda_17C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17C5)
    OP_68(43230, -450, 2400, 10000)
    MoveCamera(45, 27, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(32119, 10000)
    Sleep(500)
    PlayEffect(0x7, 0x2, 0x8, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x3, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xA, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(843, 0, 80, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#11P#10305F#10AOh\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#00105F#10AIt will be purified …\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    StopSound(852, 3000, 100)
    WaitChrThread(0xA, 2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x1, 0x2)
    EndChrThread(0x18D, 0x3)
    Sleep(1500)
    Fade(500)
    OP_68(46790, -850, 1390, 0)
    MoveCamera(64, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21390, 0)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_19AB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19AB)
    Sleep(50)

    def lambda_19BB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19BB)
    Sleep(50)

    def lambda_19CB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19CB)
    Sleep(50)

    def lambda_19DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19DB)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10101FB, Mr. Lloyd,\x01",
            "The current magic team, surely ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FAh……\x01",
            "This is Altair Lodge\x01",
            "Kevin used it … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18D, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00001FMr. Lease,\x01",
            "Did you mean …?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0xFF)
    SetChrSubChip(0x18D, 0x0)
    OP_0D()
    TurnDirection(0x18D, 0x102, 500)

    ChrTalk(
        0x18D,
        (
            "#5P#04402F…… Ellie.\x01",
            "About my status\x01",
            "You seem to be silent, are not you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x18D, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00106FYeah ….\x01",
            "To say too much\x01",
            "Please feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#5P#04404FHehe … … I thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x18D,
        (
            "… … It is already thin to the archbishop,\x01",
            "It seems to have been hit … …\x02\x03",
            "Even within the church,\x01",
            "I belong to a special organization.\x02\x03",
            "── \"Star Cup Order\".\x01",
            "It belongs to the institution named Seaplane Province\x01",
            "Ancient artifacts#8RArtifact#It is an organization that collects.\x02",
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
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FThe Star Cup Knights … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10111FAt Altair Lodge\x01",
            "He lent me a hand …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FI said that he lent his hand …\x01",
            "Is that about Kevin Graham?\x02\x03",
            "#04402FI will support him\x01",
            "It is on the rank of \"Adjunctor\".\x02\x03",
            "#04406FOriginally, for various investigations\x01",
            "He himself enters the crossbell\x01",
            "Although it was a line, … ….\x02\x03",
            "#04400FBecause there was an archbishop's eyes\x01",
            "Instead I as an information collector\x01",
            "It was dispatched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10103FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAlso in this case,\x01",
            "It is part of the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FSomehow, church too\x01",
            "You seem to have a lot of distortions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04403FYeah, shy.\x02\x03",
            "#04400F…… I will stay as it is on the rooftop\x01",
            "I am going to go check up.\x02\x03",
            "If you can\x01",
            "I also want to hear opinions,\x01",
            "I'd like to accompany you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F……I agree.\x02\x03",
            "#00200FIf I stayed in this place forever,\x01",
            "And that demon is\x01",
            "It may appear … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThen,\x01",
            "Let's go up to the bell tower.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(129, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x157, 7)
    SetScenarioFlags(0x22, 2)
    NewScene("m2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_DD6 end

    def Function_8_2126(): pass

    label("Function_8_2126")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2156")

    def lambda_2136():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2136)
    WaitChrThread(0xFE, 2)
    Sleep(100)
    Jump("Function_8_2126")

    label("loc_2156")

    Return()

    # Function_8_2126 end

    def Function_9_2157(): pass

    label("Function_9_2157")

    Sound(280, 0, 50, 0)
    PlayEffect(0x2, 0x2, 0x18D, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x3)
    StopEffect(0x1, 0x0)
    StopSound(852, 1000, 100)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 13)
    PlayEffect(0x3, 0x3, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x4)
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(287, 0, 100, 0)
    PlayEffect(0x4, 0x4, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x8, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_9_2157 end

    def Function_10_22F5(): pass

    label("Function_10_22F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2313")
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_10_22F5")

    label("loc_2313")

    Return()

    # Function_10_22F5 end

    def Function_11_2314(): pass

    label("Function_11_2314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_232E")
    OP_A1(0x18D, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_11_2314")

    label("loc_232E")

    Return()

    # Function_11_2314 end

    def Function_12_232F(): pass

    label("Function_12_232F")

    Sleep(900)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(308, 0, 50, 0)
    Sound(540, 0, 70, 0)
    Return()

    # Function_12_232F end

    def Function_13_23B7(): pass

    label("Function_13_23B7")

    Sound(250, 0, 100, 0)
    Sound(212, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Return()

    # Function_13_23B7 end

    SaveToFile()

Try(main)
