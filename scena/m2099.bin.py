from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Demon",                  # 1
        "Demon",                  # 2
        "Demon",                  # 3
        "SE制御",                 # 4
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
        "Function_3_3D1",          # 03, 3
        "Function_4_DB8",          # 04, 4
        "Function_5_DDD",          # 05, 5
        "Function_6_DFA",          # 06, 6
        "Function_7_E33",          # 07, 7
        "Function_8_222D",         # 08, 8
        "Function_9_225E",         # 09, 9
        "Function_10_23FC",        # 0A, 10
        "Function_11_241B",        # 0B, 11
        "Function_12_2436",        # 0C, 12
        "Function_13_24BE",        # 0D, 13
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
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2")
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

    label("loc_3C2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_2DB end

    def Function_3_3D1(): pass

    label("Function_3_3D1")

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

    def lambda_501():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_501)
    Sleep(50)

    def lambda_51E():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51E)
    Sleep(50)

    def lambda_53B():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53B)
    Sleep(50)

    def lambda_558():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_558)
    Sleep(50)

    def lambda_575():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_575)
    Sleep(50)

    def lambda_592():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_592)
    Sleep(50)

    def lambda_5AF():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AF)
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
            "#00006F*phew*...\x01",
            "At last, we've arrived.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FElie, this time it looks\x01",
            "like you're somehow fine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00102FY-Yes.\x01",
            "Miss Ries is with us too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, it's true that you\x01",
            "could be feeling safe by\x01",
            "having a Sister in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FAfter all, it's a "temple".\x02\x03",
            "#00304FWell, although being together with such a\x01",
            "cutie motivates me in a different sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00211FSlick as always.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FMiss Ries,\x01",
            "what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81B():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81B)
    Sleep(50)

    def lambda_82B():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82B)
    Sleep(300)
    OP_64(0x18D)

    ChrTalk(
        0x18D,
        (
            "#12P#04403FHm, this big crest\x01",
            "interests me.\x02\x03",
            "#04400FCould it be of\x01",
            "that "Cult"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FAh...do you know it?\x02\x03",
            "#00001FYes, it appears it's a crest they\x01",
            "were using in the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt appears it was used in bloody\x01",
            "rituals for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FAt any rate, it was pretty tough\x01",
            "when we came here before.\x02\x03",
            "#00309FWhen we noticed that a bell suddenly rang,\x01",
            "a "demon" appeared on the spot──\x02",
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

    def lambda_ABD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABD)
    Sleep(50)

    def lambda_ACD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACD)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FN-No way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10301FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#6P#04401FThis isn't the presence of a mere "evil spirit"...\x02",
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
        "#12P#00105FA-A demon...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FTch, it came out with\x01",
            "an odd timin'!\x02\x03",
            "#00306FIt just seems like I was the one who summoned it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FPlease be careful...!\x01",
            "I sense it has a fiercer spirit energy\x01",
            "than the one of back then...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#12P#04401FHere it comes...!\x02",
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

    # Function_3_3D1 end

    def Function_4_DB8(): pass

    label("Function_4_DB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DDC")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_4_DB8")

    label("loc_DDC")

    Return()

    # Function_4_DB8 end

    def Function_5_DDD(): pass

    label("Function_5_DDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF9")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_5_DDD")

    label("loc_DF9")

    Return()

    # Function_5_DDD end

    def Function_6_DFA(): pass

    label("Function_6_DFA")

    ClearChrFlags(0xFE, 0x1)

    def lambda_E04():
        OP_98(0xFE, 0x0, 0xAF0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E04)

    def lambda_E1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E1E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_DFA end

    def Function_7_E33(): pass

    label("Function_7_E33")

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
        "#6P#00003F*phew*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FW-We did it, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FEh, it was no great opponent\x01",
            "for how we're now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00204F...You should stop bluffing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301F...Wait a moment.\x01",
            "It looks like it's still early to be relieved.\x02",
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

    def lambda_12DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12DB)
    Sleep(50)

    def lambda_12EB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12EB)
    Sleep(50)

    def lambda_12FB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12FB)
    Sleep(50)

    def lambda_130B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_130B)
    Sleep(50)

    def lambda_131B():
        OP_95(0xFE, 34530, 250, 2090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_131B)

    def lambda_1335():
        OP_95(0xFE, 34440, 250, -3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1335)
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
            "#6P#00010FKh...\x01",
            "Is it still alive!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203F...It looks like it is a demon\x01",
            "related to the undead type...\x02\x03",
            "#00200FIt could be impossible to completely\x01",
            "vanquish it with the weapons and\x01",
            "Arts we have at our disposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00110FI-Impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00310FTch...\x01",
            "What a pain of a guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FAnd so, we must cut our way \x01",
            "through in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00007FMiss Ries, stay behind\x01",
            "us for the time being!\x02\x03",
            "We'll protect you\x01",
            "no matter what──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#6P#04403F...No.\x01",
            "It won't be necessary.\x02",
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
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#6P#04407FGo──\x01",
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
        "#6P#00005FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00305FFor real...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#00205FSuch demons in an instant...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#6P#04403F...It's over.\x02",
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

    def lambda_181F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_181F)

    def lambda_1830():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1830)

    def lambda_1841():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1841)
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
        "#11P#10305F#10AEeh...\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#00105F#10AThey've been purificated...\x02",
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

    def lambda_1A2E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A2E)
    Sleep(50)

    def lambda_1A3E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A3E)
    Sleep(50)

    def lambda_1A4E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A4E)
    Sleep(50)

    def lambda_1A5E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A5E)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10101FM-Mr. Lloyd, that\x01",
            "magic circle, I'm sure it's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah...\x01",
            "That's what Mr. Kevin was\x01",
            "using at the Altair Lodge...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18D, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00001FMiss Ries,\x01",
            "could you be...?\x02",
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
            "#5P#04402F...Miss Elie.\x01",
            "It appears that you didn't\x01",
            "tell them about my identity?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x18D, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00106FYes...\x01",
            "I wondered how to say it\x01",
            "in a roundabout way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#5P#04404FUh uh...thank you.\x02",
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
            "...It appears it was\x01",
            "already slightly sensed\x01",
            "by the Archbishop, but...\x02\x03",
            "I belong to a special organization\x01",
            "among the Church.\x02\x03",
            "──The "Gralsritter".\x01",
            "It's an organization\x01",
            "that collects Artifacts.\x02\x03",
            "It belongs to the Congregation\x01",
            "for the Sacraments.\x02",
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
        "#6P#00011FThe Gralsritter...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10111FThey helped us at\x01",
            "the Altair Lodge...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FWho helped you was...\x01",
            "Kevin Graham, right?\x02\x03",
            "#04402FI have the rank of "squire"\x01",
            "and I am his supporter.\x02\x03",
            "#04406FOriginally, the plan was for\x01",
            "him to come to Crossbell for\x01",
            "various investigations, but...\x02\x03",
            "#04400FBeing not very liked by the Archbishop,\x01",
            "I was dispatched as intelligence\x01",
            "gatherer instead of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10103FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAnd that means that this matter too\x01",
            "is a part of those investigations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FOr like, it seems that even the Church\x01",
            "has got a variety of restraints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04403FYes, it's embarrassing to admit.\x02\x03",
            "#04400F...I intend to go the rooftop\x01",
            "to investigate now.\x02\x03",
            "If possible, since I would like\x01",
            "to have your opinions too, I\x01",
            "would like you to accompany me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...Right.\x02\x03",
            "#00200FAs long as we stay in this\x01",
            "place, demons like those\x01",
            "could appear once again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThen, let's immediately\x01",
            "head up to the belfry.\x02",
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

    # Function_7_E33 end

    def Function_8_222D(): pass

    label("Function_8_222D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_225D")

    def lambda_223D():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_223D)
    WaitChrThread(0xFE, 2)
    Sleep(100)
    Jump("Function_8_222D")

    label("loc_225D")

    Return()

    # Function_8_222D end

    def Function_9_225E(): pass

    label("Function_9_225E")

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

    # Function_9_225E end

    def Function_10_23FC(): pass

    label("Function_10_23FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_241A")
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_10_23FC")

    label("loc_241A")

    Return()

    # Function_10_23FC end

    def Function_11_241B(): pass

    label("Function_11_241B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2435")
    OP_A1(0x18D, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_11_241B")

    label("loc_2435")

    Return()

    # Function_11_241B end

    def Function_12_2436(): pass

    label("Function_12_2436")

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

    # Function_12_2436 end

    def Function_13_24BE(): pass

    label("Function_13_24BE")

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

    # Function_13_24BE end

    SaveToFile()

Try(main)
